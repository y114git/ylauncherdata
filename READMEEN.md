### Version 2.0.0 — 16.08.25

- **YLauncher is now DELTAHUB!** This is more than just a name change — the launcher has been rebranded and is now a full-fledged platform for not only translations, but for any mods. You now have a huge library with a convenient search function at your disposal.

- **A completely new interface!** The launcher has received a fully redesigned look that is more modern and convenient. Finally!
  - **Updated startup screen:** Now, when you launch the launcher, you are greeted not by just an icon, but by an animated splash screen. You can turn it off in the settings.
  - **Built-in mod library:** All your installed mods are now in one place, where you can configure anything you want, such as whether to launch a mod immediately without any extra settings, or to set up mods for each chapter separately. Also, the DEMO VERSION checkbox has been moved from the settings to the library.

- **Complete mod management**
  - Now you can create your own mods and publish them. You can update them yourself, customize them, and have full control over them.
  - Now, if you need to update a file, you can update just one of the mod's components, and users will no longer need to reinstall the entire mod from scratch, as was the case before. It will be enough to simply update only the changed components.
  - You can also add your own local mods and now, you can even edit them!

- **Full launcher customization and other changes:**
  - You can now customize the launcher to suit your preferences — ABSOLUTELY EVERYTHING! The background music, the splash screen sound, the background, the color of backgrounds, the color of text and other elements, and so on!
  - The launcher now runs even faster. The basic initialization has been sped up many times over, and you can make the launcher start even faster by disabling the splash screen in the settings.
  - The button to update the interface and mod information is now located to the right of the Settings button.
  - The Erase button is gone; in its place, the save manager has been moved from the settings.
  - Now, when you launch the game with a mod, the files are no longer mindlessly copied into the game folder. Instead, the original files are moved to a temporary folder while the game is running, and when the game ends, the mod files are deleted from the game folder, and the original files are returned to their place.
  - Many other minor changes, which I advise you to check out for yourself :)

### Version 1.7.4 — 23.07.25

- Minor bug fixes + fixes for MacOS issues.

### Version 1.7.3 — 19.07.25

- Minor bug fixes.

### Version 1.7.2 — 18.07.25

* **A few bug fixes!**

- Now, each time you launch, it will not constantly ask you to re-select the game folder.
- The online counter used to jump around like crazy, but now it shouldn't.
- The launcher window should now always appear on top of the screen, and you don't have to constantly click on it in the taskbar to open it.

### Version 1.7.1 — 16.07.25

* **Micro-update!**
- For some, the launcher did not start properly after the last patch, and for others, the launcher could freeze almost every 5 seconds. In this update, I tried to fix this.
- Now, while the launcher is starting, you can look at a cool icon that appears in the center of the screen (Ahahahah).
- Now, when exporting save slots, if they were completed, not only the main file is exported, but also the completion file associated with it.

### Version 1.7.0 — 15.07.25

* **Full support for the Deltarune demo version!**
- Now you can launch and manage the demo version of the game directly from the launcher — without any extra hassle!
- If you haven't installed the DEMO version yet, you can download it from scratch in the launcher thanks to the Full Installation feature!
- Automatic search and installation of the demo version, including downloading the latest build directly from the interface.
- Fully compatible with Steam.

* **Improved translation manager:**
- New "Backup Server" feature — now, even if the main servers are unavailable, you can always download the translation you need.
- Support for new archive formats: now the launcher works easily not only with ZIP, but also with RAR files.
- Improved system for searching and downloading translations — faster, more convenient, more stable!

* **Interface updates:**
- An online counter has been added, which displays the number of players who launched the game through the launcher.
- The launcher's interface has become even more user-friendly, and compatibility with Linux and macOS has been improved.
- Advanced dialogues for saving and managing translations.
- Improved adaptability, new tips, and quick access to the necessary functions.

* **Additional improvements and fixes:**
- Optimized work with the Internet and temporary files, fixed rare errors when downloading translations.
- Builds on MacOS are now immediately signed, and you do not need to constantly run them from the console.
- Increased stability on all supported systems.
- Improved support for custom executable files for advanced users.

### Version 1.6.0 - 12.07.25
* New feature: Save Manager! Now you can manage your saves directly in the launcher.

* How to open: Go to "Settings" and click the new "Saves✨" button.

* Collections: Create separate "collections" of saves for each chapter. This is ideal for storing saves from different playthroughs (for example, "pacifist" and "genocide") and not getting confused.

* Backup: Easily copy saves from the main slots to any collection and back. You can copy one selected slot or all three at once.

* Direct editing: For advanced users! Just double-click on an occupied slot to open a simple editor and manually change the values in the save file. Soon there will be a much more convenient and understandable editor!

Interface and usability improvements:

* The launcher window can now be stretched, and its size is saved after closing.

* Completely redesigned appearance: navigation through chapters is moved to the center, and the Telegram and Discord buttons are now always at hand on the main screen.

* The "Forced launch" checkbox has been removed. Now the launcher itself understands when to launch the game without changes.

* Added support for animated .gif as a background.

Other changes:

* The auto-update logic has been slightly updated and minor bugs have been fixed.

### Version 1.5.3 - 06.07.25

* More extensive support for MacOS systems (Supports all architectures, but only if the version is above 11.0), visual bugs with local translations have been fixed.

### Version 1.5.2 - 05.06.25

* Minor fixes and bug fixes, especially with the fact that translations were not shown on the first installation.

### Version 1.5.1 - 30.06.25

* For those who received an error about a lack of access rights to the game folder, the launcher now tries to fix this automatically, and if it fails, it displays a message asking you to run as an administrator or manually change the folder rights.

### Version 1.5.0 - 28.06.25

* **2 New features: Direct launch and Your own translation!** By enabling direct launch, when you launch the game through the launcher, selecting the desired chapter (Chapter tab), the game will start immediately from that chapter, without the need to first select the chapter separately in the main menu of the game. Due to technical problems, it only works on Windows/Linux, and is also not compatible with launching through Steam.
* **The second feature is Your own translation**, now you can add your own translation/mod/changes for each chapter separately, your added translation is saved in the list and you can select several custom translations and switch between them, if you are too lazy to add a translation for each chapter, you can take an archive that contains everything you need, and also in the folders with chapters, and just add the translation specifically through the Main menu of the game tab (Since everything there works on the root folder). You can give any name to your translation separately, and the most interesting thing is that you can add your own translation directly from a URL without the need to download anything separately.
* Now the No Changes option is grayer, local translations (Which you added) are always yellow and at the top of the list, and the main translations are white if they have not yet been downloaded, green if they have been downloaded and do not need to be updated, and orange if they have been downloaded but need to be updated.
* A little more compatibility with MacOS has been added, and problems with a lack of rights for some users have been fixed.
* Several critical bugs that could lead to the launcher freezing or incorrect operation have been fixed.
* All new features are fully compatible with each other, including Shortcuts.

### Version 1.4.2/1.4.3 - 23.06.25

* The problem with the normal display of text in descriptions has been fixed.
* Several more critical bugs have been fixed.

### Version 1.4.0/1.4.1 - 23.06.25

* **New feature: Shortcuts! (Hey!)** Now you can create a shortcut to launch with your settings. Just set everything up as you like, click "Shortcut", and the launcher will create a special launch file. When you click on it, the game will start with the selected translations and settings, and the launcher itself will not even appear on the screen.
* The "Update" button has been replaced with "Shortcut". The list of translations is now updated automatically on launch. However, you can now perform a Check for Updates, right from the settings menu.
* The launcher's core has been changed, which made it much more stable and pleasant.
* Now by default the launcher has a new beautiful Deltarune theme, but in the settings you can still choose the Legacy Theme, which will return the old, good look of the launcher up to 1.4.0
* "Change log" has been added.
* A check and a warning have been added when selecting a chapter folder instead of a game folder.
* 2 critical bugs have been fixed, one of which did complete nonsense when the data.win file was missing in the game folder.
