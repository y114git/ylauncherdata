# =============================================================================
#                           YLAUNCHER
#             Версия 1.2 - Стабильность и исправления
# =============================================================================
import customtkinter as ctk
import tkinter.filedialog
import tkinter.messagebox
import os
import sys
import platform
import requests
import zipfile
import shutil
import subprocess
import psutil
import threading
import json
import re
from io import BytesIO
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from base64 import urlsafe_b64encode, urlsafe_b64decode
from typing import Optional, Dict, List, Tuple, Any

# --- ГЛАВНАЯ КОНФИГУРАЦИЯ ---
# !!! ИЗМЕНИТЕ ЭТИ ДАННЫЕ, ЕСЛИ НУЖНО !!!
GITHUB_REPO = "y114git/ylauncherdata" # Репозиторий с данными (переводами)
ZIP_PASSWORD = b"P5iy%jsAwd3mtGi4Y*G#" # Пароль от архивов с переводами
CACHE_ENCRYPTION_KEY = b"@2nuD6xqNA&X$4kS*hbs" # Ключ для шифрования кэша
# --- КОНЕЦ КОНФИГУРАЦИИ ---

class YLauncherApp(ctk.CTk):
    """Основной класс приложения-лаунчера YLAUNCHER."""
    def __init__(self):
        super().__init__()
        self.title("YLAUNCHER для Deltarune")
        self.geometry("600x450")
        self.resizable(False, False)
        ctk.set_appearance_mode("dark")
        self.protocol("WM_DELETE_WINDOW", self._on_closing)

        # --- Инициализация всех атрибутов класса ---
        self.app_is_closing = False
        self.game_path: str = ""
        self.cache_path: str = self._get_app_support_path()
        self.config_path: str = os.path.join(self.cache_path, "config.json")
        self.versions_path: str = os.path.join(self.cache_path, "local_versions.json")
        self.local_config: Dict[str, Any] = {}
        self.local_versions: Dict[str, Any] = {}
        self.translations_by_chapter: Dict[int, List[Tuple]] = {i: [] for i in range(5)}
        self.fernet: Optional[Fernet] = self._init_encryption(CACHE_ENCRYPTION_KEY)

        # --- Инициализация виджетов (объявляем их как Optional) ---
        self.vanilla_mode_var: Optional[ctk.BooleanVar] = None
        self.vanilla_mode_checkbox: Optional[ctk.CTkCheckBox] = None
        self.change_path_button: Optional[ctk.CTkButton] = None
        self.tab_view: Optional[ctk.CTkTabview] = None
        self.tabs: Dict[int, Dict[str, Any]] = {}
        self.status_label: Optional[ctk.CTkLabel] = None
        self.progress_bar: Optional[ctk.CTkProgressBar] = None
        self.action_button: Optional[ctk.CTkButton] = None
        self.delete_button: Optional[ctk.CTkButton] = None

        self._create_widgets()
        # Запускаем инициализацию в отдельном потоке, чтобы не блокировать UI
        self.after(100, lambda: threading.Thread(target=self.initialize_launcher, daemon=True).start())

    def _init_encryption(self, password: bytes) -> Optional[Fernet]:
        """Создает ключ шифрования из пароля."""
        try:
            salt = b'salt_for_ylauncher_!@#$'
            kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=480000)
            key = urlsafe_b64encode(kdf.derive(password))
            return Fernet(key)
        except Exception as e:
            print(f"Ошибка инициализации шифрования: {e}")
            self.after(0, lambda: self._update_status(f"Ошибка шифрования: {e}", "red"))
            return None

    def _create_widgets(self):
        """Создает все виджеты интерфейса."""
        top_frame = ctk.CTkFrame(self)
        top_frame.pack(fill="x", padx=10, pady=10)

        self.vanilla_mode_var = ctk.BooleanVar()
        self.vanilla_mode_checkbox = ctk.CTkCheckBox(
            top_frame, text="Играть без модов",
            variable=self.vanilla_mode_var, command=self._toggle_vanilla_mode
        )
        self.vanilla_mode_checkbox.pack(side="left", padx=(10, 5), pady=10)

        self.change_path_button = ctk.CTkButton(
            top_frame, text="Сменить папку игры",
            command=lambda: threading.Thread(target=self._prompt_for_game_path, daemon=True).start()
        )
        self.change_path_button.pack(side="right", padx=(5, 10), pady=10)

        self.tab_view = ctk.CTkTabview(self, anchor="w", command=lambda: self._update_ui_for_selection())
        self.tab_view.pack(expand=True, fill="both", padx=10, pady=0)
        self.tabs = {}
        for i, name in enumerate(["Гл. меню", "Глава 1", "Глава 2", "Глава 3 & 4", "Глава 5"]):
            tab = self.tab_view.add(name)
            label = ctk.CTkLabel(tab, text="Выберите перевод:")
            label.pack(pady=(20, 5))
            menu = ctk.CTkOptionMenu(tab, values=["Загрузка..."], command=lambda _, c_id=i: self._update_ui_for_selection(c_id))
            menu.pack()
            self.tabs[i] = {"menu": menu, "label": label}
        self.tab_view.set("Глава 1") # Устанавливаем вкладку по умолчанию

        bottom_frame = ctk.CTkFrame(self)
        bottom_frame.pack(fill="x", side="bottom", padx=10, pady=(5, 10))
        self.status_label = ctk.CTkLabel(bottom_frame, text="Инициализация...", text_color="gray")
        self.status_label.pack(pady=5)
        self.progress_bar = ctk.CTkProgressBar(bottom_frame)
        self.progress_bar.set(0)

        action_frame = ctk.CTkFrame(bottom_frame, fg_color="transparent")
        action_frame.pack(fill="x", expand=True)
        self.action_button = ctk.CTkButton(
            action_frame, text="Подождите...", state="disabled",
            command=self._on_action_button_click
        )
        self.action_button.pack(side="left", expand=True, padx=(10, 5), pady=5, ipady=5)
        self.delete_button = ctk.CTkButton(
            action_frame, text="🗑️", width=40, state="disabled",
            command=self._on_delete_button_click
        )
        self.delete_button.pack(side="right", padx=(5, 10), pady=5, ipady=5)

    # --- Основная логика ---

    def initialize_launcher(self):
        """Полный цикл инициализации лаунчера в фоновом потоке."""
        if self._is_game_running():
            self._update_status("Ошибка: Deltarune уже запущен!", "red")
            if self.action_button:
                self.action_button.configure(state="disabled")
            return

        self._load_local_config()
        if not self._find_and_validate_game_path():
            return

        self._update_status("Загрузка списка переводов с GitHub...", "gray")
        if self._fetch_translations_from_github():
            self._populate_ui_with_translations()
            self.after(0, self._update_ui_for_selection)
        else:
            self._update_status("Нет сети. Доступен только оффлайн-режим.", "orange")
            if self.vanilla_mode_checkbox:
                self.vanilla_mode_checkbox.select()
            self._toggle_vanilla_mode()
            if not self.local_versions:
                 self._update_status("Нет сети и нет кэшированных переводов. Запуск невозможен.", "red")
                 if self.action_button:
                     self.action_button.configure(state="disabled")

    def _on_action_button_click(self):
        """Обработчик нажатия главной кнопки, запускает операции в потоке."""
        if self.vanilla_mode_var and self.vanilla_mode_var.get():
            threading.Thread(target=self._launch_vanilla, daemon=True).start()
        else:
            if self.action_button: self.action_button.configure(state="disabled")
            if self.delete_button: self.delete_button.configure(state="disabled")
            if self.progress_bar:
                self.progress_bar.pack(fill="x", padx=10, pady=(0, 5))
                self.progress_bar.set(0)
            threading.Thread(target=self._handle_modded_action, daemon=True).start()

    def _handle_modded_action(self):
        """Определяет, какую операцию (установка/обновление/запуск) выполнить."""
        if not self.action_button: return
        status = self.action_button.cget("text")
        if status in ["Установить", "Обновить"]:
            self._install_translation()
        elif status == "Запустить":
            self._launch_modded()

        self.after(0, self._update_ui_for_selection)
        if self.progress_bar:
            self.after(0, self.progress_bar.pack_forget)

    # --- Под-процессы (Выполняются в потоках) ---

    def _install_translation(self):
        """Скачивает, расшифровывает и кэширует выбранный перевод."""
        selected_info = self._get_selected_mod_info()
        if not selected_info: return

        chapter_id, full_id, name, version, url, _ = selected_info

        try:
            self._update_status(f"Скачивание {name} v{version}...", "yellow")
            response = requests.get(url, stream=True, timeout=30)
            response.raise_for_status()
            zip_content = BytesIO()
            total_size = int(response.headers.get('content-length', 0))
            downloaded_size = 0
            for data in response.iter_content(chunk_size=8192):
                zip_content.write(data)
                downloaded_size += len(data)
                if total_size > 0:
                    progress = 0.1 + (downloaded_size / total_size) * 0.4
                    self.after(0, lambda p=progress: self.progress_bar.set(p) if self.progress_bar else None) # Проверка внутри lambda

            self._update_status("Распаковка архива...", "yellow")
            self.after(0, lambda: self.progress_bar.set(0.6) if self.progress_bar else None)
            zip_content.seek(0)
            extracted_files = {}
            with zipfile.ZipFile(zip_content, 'r') as zip_ref:
                for file_info in zip_ref.infolist():
                    if not file_info.is_dir():
                        extracted_files[file_info.filename] = zip_ref.read(file_info.filename, pwd=ZIP_PASSWORD)

            if not self.fernet: raise ValueError("Ошибка шифрования (Fernet не инициализирован)")
            self._update_status("Шифрование и сохранение в кэш...", "yellow")
            self.after(0, lambda: self.progress_bar.set(0.8) if self.progress_bar else None)
            serializable_files = {path: urlsafe_b64encode(content).decode('ascii') for path, content in extracted_files.items()}
            encrypted_data = self.fernet.encrypt(json.dumps(serializable_files).encode('utf-8'))
            with open(os.path.join(self.cache_path, f"{full_id}.encrypted"), 'wb') as f:
                f.write(encrypted_data)

            self.local_versions[full_id] = {"version": version, "name": name}
            self._write_json(self.versions_path, self.local_versions)
            self._update_status(f"Установка {name} v{version} завершена!", "green")

        except Exception as e:
            self._update_status(f"Ошибка установки: {e}", "red")
        finally:
            self.after(0, lambda: self.progress_bar.pack_forget() if self.progress_bar else None)
            self.after(0, lambda c_id=chapter_id: self._update_ui_for_selection(c_id))


    def _launch_modded(self):
        """Запускает игру с защитой и подменой файлов."""
        selected_info = self._get_selected_mod_info()
        if not selected_info: return
        chapter_id, full_id, name, _, _, is_protected = selected_info

        target_dir = self._get_target_dir()
        if not target_dir: return

        backup_dir = os.path.join(self.cache_path, "backup", str(chapter_id))

        try:
            self._update_status("Подготовка к запуску...", "yellow")
            self.after(0, lambda: self.progress_bar.set(0.1) if self.progress_bar else None)

            if not self.fernet: raise ValueError("Ошибка шифрования (Fernet не инициализирован)")
            cache_file = os.path.join(self.cache_path, f"{full_id}.encrypted")
            with open(cache_file, 'rb') as f:
                decrypted_data = self.fernet.decrypt(f.read())
            serializable_files = json.loads(decrypted_data)
            decrypted_files = {path: urlsafe_b64decode(content) for path, content in serializable_files.items()}

            if is_protected:
                self._update_status("Создание резервной копии...", "yellow")
                self.after(0, lambda: self.progress_bar.set(0.3) if self.progress_bar else None)
                if os.path.exists(backup_dir): shutil.rmtree(backup_dir)
                os.makedirs(backup_dir)
                for rel_path in decrypted_files.keys():
                    game_file_path = os.path.join(target_dir, rel_path.replace('/', os.sep))
                    if os.path.exists(game_file_path):
                        backup_file_path = os.path.join(backup_dir, rel_path.replace('/', os.sep))
                        os.makedirs(os.path.dirname(backup_file_path), exist_ok=True)
                        shutil.copy2(game_file_path, backup_file_path)

            self._update_status(f"Установка перевода '{name}'...", "yellow")
            self.after(0, lambda: self.progress_bar.set(0.6) if self.progress_bar else None)
            for rel_path, content in decrypted_files.items():
                game_file_path = os.path.join(target_dir, rel_path.replace('/', os.sep))
                os.makedirs(os.path.dirname(game_file_path), exist_ok=True)
                if platform.system() == "Darwin" and os.path.basename(game_file_path) == "data.win":
                     game_file_path = os.path.join(os.path.dirname(game_file_path), "game.ios")
                with open(game_file_path, "wb") as f: f.write(content)

            self._update_status("Запуск игры... Лаунчер останется в фоне.", "green")
            self.after(0, lambda: self.progress_bar.set(1.0) if self.progress_bar else None)

            exe_path = self.game_path

            self.after(100, self.withdraw)
            game_process = subprocess.Popen([exe_path], cwd=os.path.dirname(exe_path))
            game_process.wait()

        except Exception as e:
            self._update_status(f"Критическая ошибка при запуске: {e}", "red")
        finally:
            if is_protected and os.path.exists(backup_dir):
                print("Игра закрыта. Восстановление оригинальных файлов...")
                for root, _, files in os.walk(backup_dir):
                    for file in files:
                        backup_file = os.path.join(root, file)
                        original_rel_path = os.path.relpath(backup_file, backup_dir)
                        original_abs_path = os.path.join(target_dir, original_rel_path)
                        os.makedirs(os.path.dirname(original_abs_path), exist_ok=True)
                        shutil.copy2(backup_file, original_abs_path)
                shutil.rmtree(backup_dir)
                print("Восстановление завершено.")
            self.after(100, self.destroy)

    def _launch_vanilla(self):
        """Запускает игру без модов."""
        self._update_status("Запуск обычной версии...", "green")
        exe_path = self.game_path
        try:
            subprocess.Popen([exe_path], cwd=os.path.dirname(exe_path))
            self.after(100, self.destroy)
        except Exception as e:
            self._update_status(f"Ошибка запуска: {e}", "red")

    # --- Функции UI и состояния ---

    def _update_status(self, message: str, color: str = "white"):
        """Обновляет текстовый статус в UI (потокобезопасно)."""
        def update():
            if self.status_label:
                self.status_label.configure(text=message, text_color=color)
        if not self.app_is_closing:
            self.after(0, update)

    def _toggle_vanilla_mode(self):
        """Переключает режим "без модов"."""
        if not self.vanilla_mode_var or not self.tab_view or not self.delete_button or not self.action_button:
            return

        is_vanilla = self.vanilla_mode_var.get()
        new_state = "disabled" if is_vanilla else "normal"
        self.tab_view.configure(state=new_state)
        self.delete_button.configure(state=new_state if not is_vanilla else "disabled")

        if is_vanilla:
            self.action_button.configure(text="Запустить (без модов)", state="normal")
            self._update_status("Готов к запуску игры без модов.", "gray")
        else:
            self._update_ui_for_selection()

    def _update_ui_for_selection(self, chapter_id: Optional[int] = None):
        """Обновляет UI на основе выбранного перевода."""
        if not self.tab_view or not self.action_button or not self.delete_button:
            return
        if self.vanilla_mode_var and self.vanilla_mode_var.get(): return

        current_tab_name = self.tab_view.get()
        if current_tab_name is None: return

        if chapter_id is None:
            try:
                chapter_id = self.tab_view.index(current_tab_name)
            except tkinter.TclError:
                return

        selected_info = self._get_selected_mod_info(chapter_id)

        self.action_button.configure(state="normal" if selected_info else "disabled")

        if not selected_info:
            self.action_button.configure(text="Выберите перевод")
            self.delete_button.configure(state="disabled")
            self._update_status("Выберите перевод для продолжения.", "gray")
            return

        _, full_id, name, version, _, _ = selected_info
        self.local_config["last_selected"][str(chapter_id)] = f"{name}_{version}"
        self._write_local_config()

        is_installed = full_id in self.local_versions
        local_version = self.local_versions.get(full_id, {}).get("version", "0.0.0")

        self.delete_button.configure(state="normal" if is_installed else "disabled")

        if not is_installed:
            self.action_button.configure(text="Установить")
            self._update_status(f"Готово к установке: {name} v{version}", "white")
        elif version != local_version:
            self.action_button.configure(text="Обновить")
            self._update_status(f"Доступно обновление для '{name}' до v{version}", "green")
        else:
            self.action_button.configure(text="Запустить")
            self._update_status(f"Перевод '{name}' установлен. Готов к запуску.", "lightgreen")

    def _on_delete_button_click(self):
        """Обрабатывает удаление кэшированного перевода."""
        selected_info = self._get_selected_mod_info()
        if not selected_info: return

        _, full_id, name, _, _, _ = selected_info
        if full_id not in self.local_versions: return

        if tkinter.messagebox.askyesno("Подтверждение удаления", f"Вы уверены, что хотите удалить кэш перевода '{name}'?"):
            cache_file = os.path.join(self.cache_path, f"{full_id}.encrypted")
            if os.path.exists(cache_file):
                os.remove(cache_file)
            if full_id in self.local_versions:
                del self.local_versions[full_id]
                self._write_json(self.versions_path, self.local_versions)

            self._update_status(f"Перевод '{name}' удален.", "gray")
            self._update_ui_for_selection()

    # --- Вспомогательные функции ---

    def _on_closing(self):
        self.app_is_closing = True
        self.destroy()

    def _get_app_support_path(self) -> str:
        """Возвращает путь к папке данных приложения в зависимости от ОС."""
        system = platform.system()
        path = ""
        if system == "Windows":
            appdata = os.getenv('APPDATA')
            if appdata:
                path = os.path.join(appdata, "YLauncher")
            else: # Резервный вариант, если APPDATA не определена
                path = os.path.join(os.path.expanduser('~'), ".YLauncher")
        elif system == "Darwin": # macOS
            path = os.path.join(os.path.expanduser('~'), "Library/Application Support/YLauncher")
        else: # Linux
            path = os.path.join(os.path.expanduser('~'), ".local/share/YLauncher")

        os.makedirs(os.path.join(path, "cache", "backup"), exist_ok=True)
        return os.path.join(path, "cache")

    def _load_local_config(self):
        """Загружает локальные конфиги."""
        self.local_config = self._read_json(self.config_path) or {"game_path": "", "last_selected": {}}
        self.local_versions = self._read_json(self.versions_path) or {}
        self.game_path = self.local_config.get("game_path", "")

    def _write_local_config(self):
        self._write_json(self.config_path, self.local_config)

    def _read_json(self, path: str) -> Dict:
        try:
            with open(path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def _write_json(self, path: str, data: Dict):
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def _is_game_running(self) -> bool:
        """Проверяет, запущен ли процесс игры."""
        names = ["DELTARUNE.exe", "DELTARUNE", "runner"]
        for proc in psutil.process_iter(['name']):
            if proc.info['name'] in names:
                return True
        return False

    def _get_selected_mod_info(self, chapter_id: Optional[int] = None) -> Optional[Tuple]:
        """Возвращает полную информацию о выбранном в меню моде."""
        if not self.tab_view: return None
        try:
            if chapter_id is None:
                 chapter_id = self.tab_view.index(self.tab_view.get())
        except (tkinter.TclError, IndexError):
            return None

        if chapter_id not in self.tabs: return None

        selected_display_name = self.tabs[chapter_id]["menu"].get()

        for mod_data in self.translations_by_chapter.get(chapter_id, []):
            name, version = mod_data[2], mod_data[3]
            if f"{name}_{version}" == selected_display_name:
                full_id = f"{mod_data[0]}{'p' if mod_data[1] else ''}_{name.replace(' ', '_')}_{version}_{mod_data[4]}"
                return chapter_id, full_id, name, version, mod_data[5], mod_data[1]
        return None

    def _parse_asset_name(self, filename: str) -> Optional[Tuple]:
        """Парсит имя файла ассета из релиза GitHub."""
        match = re.match(r"(\d)(p?)_([^_]+)_(\d+\.\d+\.\d+)_(\d+)\.zip", filename)
        if not match: return None
        groups = match.groups()
        return (int(groups[0]), bool(groups[1]), groups[2].replace("_", " "), groups[3], int(groups[4]))

    def _fetch_translations_from_github(self) -> bool:
        """Загружает список переводов из релизов на GitHub."""
        api_url = f"https://api.github.com/repos/{GITHUB_REPO}/releases"
        try:
            response = requests.get(api_url, timeout=10)
            response.raise_for_status()
            releases = response.json()

            for i in range(5): self.translations_by_chapter[i] = []

            for release in releases:
                for asset in release.get("assets", []):
                    parsed_info = self._parse_asset_name(asset['name'])
                    if parsed_info:
                        chapter, protected, name, version, priority = parsed_info
                        url = asset['browser_download_url']
                        if 0 <= chapter < 5:
                            self.translations_by_chapter[chapter].append((chapter, protected, name, version, priority, url))

            for chapter in self.translations_by_chapter:
                self.translations_by_chapter[chapter].sort(key=lambda x: (x[4], x[2], x[3]), reverse=True)
            return True
        except requests.RequestException as e:
            print(f"Ошибка сети при загрузке релизов: {e}")
            return False

    def _populate_ui_with_translations(self):
        """Заполняет выпадающие меню загруженными переводами."""
        last_selected_map = self.local_config.get("last_selected", {})

        for chapter_id, translations in self.translations_by_chapter.items():
            if chapter_id not in self.tabs: continue
            menu = self.tabs[chapter_id]["menu"]
            if not translations:
                menu.configure(values=["Нет переводов"], state="disabled")
                menu.set("Нет переводов")
            else:
                display_names = [f"{t[2]}_{t[3]}" for t in translations]
                menu.configure(values=display_names, state="normal")
                last_selected = last_selected_map.get(str(chapter_id))
                if last_selected in display_names:
                    menu.set(last_selected)
                else:
                    menu.set(display_names[0])
        self.after(0, self._update_ui_for_selection)

    def _get_target_dir(self) -> Optional[str]:
        """Возвращает путь к директории с файлами игры."""
        if not self.game_path: return None
        if platform.system() == "Darwin": # macOS
             return os.path.join(os.path.dirname(self.game_path), "Resources")
        else:
             return os.path.dirname(self.game_path)

    def _is_valid_game_path(self, path: str) -> bool:
        """Проверяет, является ли путь корректным путем к игре."""
        if not path: return False

        check_path = path
        # На macOS .app это папка, так что path уже правильный
        if platform.system() in ["Windows", "Linux"] and os.path.isfile(path):
            check_path = os.path.dirname(path)

        if not os.path.isdir(check_path): return False

        if platform.system() == "Windows":
            exe = os.path.join(check_path, "DELTARUNE.exe")
            if os.path.exists(exe) and os.path.exists(os.path.join(check_path, "data.win")):
                self.game_path = exe
                return True
        elif platform.system() == "Linux":
            exe = os.path.join(check_path, "DELTARUNE")
            if os.path.exists(exe) and os.path.exists(os.path.join(check_path, "data.win")):
                self.game_path = exe
                return True
        elif platform.system() == "Darwin":
            if check_path.endswith(".app"):
                runner = os.path.join(check_path, "Contents/MacOS/runner")
                resources = os.path.join(check_path, "Contents/Resources/game.ios")
                if os.path.exists(runner) and os.path.exists(resources):
                     self.game_path = runner
                     return True
        return False

    def _find_and_validate_game_path(self) -> bool:
        """Ищет, проверяет и запрашивает путь к игре."""
        if self._is_valid_game_path(self.game_path):
            self._update_status(f"Путь к игре найден: {os.path.dirname(self.game_path)}", "gray")
            return True

        self._update_status("Автоопределение папки с игрой...", "gray")
        autodetected_path = self._autodetect_game_path()
        if self._is_valid_game_path(autodetected_path or ""):
            self.local_config['game_path'] = self.game_path
            self._write_local_config()
            self._update_status(f"Игра найдена: {os.path.dirname(self.game_path)}", "green")
            return True

        return self._prompt_for_game_path(is_initial=True)

    def _prompt_for_game_path(self, is_initial: bool = False) -> bool:
        """Открывает диалог выбора папки и проверяет ее."""
        if is_initial:
            self._update_status("Папка с игрой не найдена! Укажите её вручную.", "orange")
            tkinter.messagebox.showwarning("Путь не найден", "Не удалось найти DELTARUNE. Укажите папку с игрой (где DELTARUNE.exe) или файл DELTARUNE.app на macOS.")

        title = "Выберите папку с игрой (где DELTARUNE.exe) или файл DELTARUNE.app"
        path = ""
        if platform.system() == "Darwin":
            path = tkinter.filedialog.askdirectory(title=title, initialdir=os.path.expanduser("~") + "/Applications")
            if path and not path.endswith(".app"):
                path += ".app" # Пользователи могут выбрать папку, а не сам пакет
        else:
            path = tkinter.filedialog.askdirectory(title=title)

        if path and self._is_valid_game_path(path):
            self.local_config['game_path'] = self.game_path
            self._write_local_config()
            self._update_status(f"Путь к игре установлен: {os.path.dirname(self.game_path)}", "green")
            if is_initial and not self.app_is_closing:
                self.after(10, lambda: threading.Thread(target=self.initialize_launcher, daemon=True).start())
            return True
        elif path:
            self._update_status("Выбрана неверная папка. Попробуйте еще раз.", "red")
            tkinter.messagebox.showerror("Ошибка", "Это не похоже на папку с игрой DELTARUNE.")

        if is_initial and not self.app_is_closing:
             self.after(100, self.destroy)
        return False

    def _autodetect_game_path(self) -> Optional[str]:
        """Пытается найти игру в стандартных папках Steam."""
        system = platform.system()
        paths_to_check = []
        if system == "Windows":
            for env_var in ["ProgramFiles(x86)", "ProgramFiles"]:
                root = os.getenv(env_var)
                if root:
                    paths_to_check.append(os.path.join(root, "Steam/steamapps/common/DELTARUNE"))
        elif system == "Linux":
            paths_to_check.append(os.path.expanduser("~/.steam/steam/steamapps/common/DELTARUNE"))
            paths_to_check.append(os.path.expanduser("~/.local/share/Steam/steamapps/common/DELTARUNE"))
        elif system == "Darwin":
            paths_to_check.append(os.path.expanduser("~/Library/Application Support/Steam/steamapps/common/DELTARUNE/DELTARUNE.app"))

        for path in paths_to_check:
            if os.path.exists(path):
                return path
        return None

if __name__ == "__main__":
    if sys.platform == "win32":
        import ctypes
        myappid = 'y114.ylauncher.1'
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

    app = YLauncherApp()
    app.mainloop()