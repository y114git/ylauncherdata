# DELTAMOD (1.3.1) and DELTAHUB (2.3.2) Feature Comparison
<img width="425" height="500" alt="image" src="https://github.com/user-attachments/assets/058103fd-aa9f-42da-b600-3405ac5c7e4a" />
<img width="575" height="1108" alt="image" src="https://github.com/user-attachments/assets/3a5473b3-9189-442f-8690-cad9b0664dc4" />


## Mod Management Features

| Feature | DELTAMOD | DELTAHUB |
|---------|----------|----------|
| **Mod Library** | ✅ Yes - View all installed mods | ✅ Yes - View all installed mods with filtering |
| **Mod Installation** | ✅ Yes - Import from file | ✅ Yes - Import from file or URL |
| **Mod Deletion** | ✅ Yes | ✅ Yes |
| **Mod Search** | ✅ Yes - Browse GameBanana mods | ✅ Yes - Built-in search with filters (downloads, date, game, tags, name/description) |
| **Mod Sorting** | ✅ Yes - By name (A-Z, Z-A), size | ✅ Yes - By downloads, update date, creation date, ascending/descending |
| **Mod Filtering** | ❌ No | ✅ Yes - By game type, tags, search text |
| **Multi-Mod Support** | ✅ Yes - Enable multiple mods | ✅ Yes - Select multiple mods with priority system |
| **Mod Priority System** | ❌ No | ✅ Yes - Configure priority for conflicting mods |
| **Modpacks** | ❌ No | ✅ Yes - Create and save mod combinations |
| **Chapter-by-Chapter Mode** | ❌ No | ✅ Yes - Select different mods for each chapter |
| **Direct Launch** | ❌ No | ✅ Yes - Launch specific chapter directly |
| **Mod Import/Export** | ✅ Yes - Import mods | ✅ Yes - Import/export in DELTAHUB/Deltamod format |
| **Deltamod Compatibility** | ✅ Native format | ✅ Yes - Automatic conversion from Deltamod format |
| **Mod Updates** | ❌ No | ✅ Yes - Smart update system (component-based) |
| **Mod Screenshots** | ❌ No | ✅ Yes - Up to 10 screenshots per mod |
| **Mod Tags** | ❌ No | ✅ Yes - Text Edit, Customization, Gameplay, Other |
| **Public vs Local Mods** | ❌ No | ✅ Yes - Public mods appear in search, local mods for personal use |
| **Mod Versioning** | ✅ Yes - Basic version info | ✅ Yes - Overall mod version + component versions |
| **Mod Hiding** | ❌ No | ✅ Yes - Hide mods from library |
| **Full Install Mode** | ❌ No | ✅ Yes - Install DELTARUNEdemo or Undertale Yellow directly from DELTAHUB |

## Game Support

| Feature | DELTAMOD | DELTAHUB |
|---------|----------|----------|
| **DELTARUNE Full** | ✅ Yes | ✅ Yes |
| **DELTARUNE Demo** | ✅ Yes | ✅ Yes |
| **UNDERTALE** | ❌ No | ✅ Yes |
| **UNDERTALE Yellow** | ❌ No | ✅ Yes |
| **Future GameMaker Games** | ❌ No | ✅ Planned |
| **Game Download** | ❌ No | ✅ Yes - Direct download for free games (demo, UTY) |
| **Multiple Game Installations** | ✅ Yes - Installation manager | ✅ Yes - Separate paths for each game |

## Installation & Patching

| Feature | DELTAMOD | DELTAHUB |
|---------|----------|----------|
| **XDELTA Patching** | ❌ No | ✅ Yes - Plugin (XDELTA Patcher) |
| **Patch Creation** | ❌ No | ✅ Yes - Plugin (XDELTA Patcher) |
| **File Types Supported** | ✅ .xdelta, .vcdiff, .csx, .win | ✅ .xdelta, .vcdiff, .csx, .win |
| **Archive Formats** | ✅ .zip, .7z, .tar.gz, .lzma | ✅ .zip, .7z, .rar, .tar.gz, .lzma |
| **Installation Manager** | ✅ Yes - Manage multiple installations | ❌ No (not needed) |
| **One-Click Install** | ✅ Yes | ✅ Yes |
| **Installation from GameBanana** | ✅ Yes - Browse and download | ✅ Yes - Browse, search, and install |

## User Interface & Customization

| Feature | DELTAMOD | DELTAHUB |
|---------|----------|----------|
| **Themes** | ✅ Yes - Multiple built-in themes | ✅ Yes - Custom themes with import/export |
| **Background Music** | ✅ Yes - built-in | ✅ Yes - Custom background music |
| **Startup Sound** | ⚠️ No | ✅ Yes - Custom startup sound |
| **Background Images** | ✅ Yes - Theme backgrounds | ✅ Yes - Custom background images |
| **Font Customization** | ✅ Yes - Theme fonts | ✅ Yes - Custom fonts |
| **Color Customization** | ✅ Yes - Theme colors | ✅ Yes - Custom colors (background, border, text, buttons) |
| **Localization** | ❌ No | ✅ Yes - Multi-language support (EN, RU, ZH-CN, ZH-TW, etc.) |
| **Pagination** | ❌ No | ✅ Yes - Customizable mods per page |
| **UI Layout** | Web-based (Electron) | Native (PyQt6) |

## Game Launch Features

| Feature | DELTAMOD | DELTAHUB |
|---------|----------|----------|
| **Game Launch** | ✅ Yes - Patch and run | ✅ Yes - Launch with selected mods |
| **Steam Integration** | ✅ Yes | ✅ Yes - Launch via Steam option |
| **Custom Executable** | ❌ No | ✅ Yes - Select custom game executable |
| **PortProton Support (Linux)** | ❌ No | ✅ Yes - Use PortProton instead of Wine |
| **Game Process Monitoring** | ✅ Yes | ✅ Yes - Monitor game status |
| **Auto File Restoration** | ✅ Yes | ✅ Yes |
| **Shortcuts** | ❌ No | ✅ Yes - Create desktop shortcuts with mods |

## Save Management

| Feature | DELTAMOD | DELTAHUB |
|---------|----------|----------|
| **Save Manager** | ❌ No | ✅ Yes - Plugin (DR Save Manager) |
| **Multiple Save Collections** | ❌ No | ✅ Yes - Unlimited save collections |
| **Save Export/Import** | ❌ No | ✅ Yes - Export/import save collections |
| **Save Editing** | ❌ No | ✅ Yes - Edit save files directly |
| **Save Slot Management** | ❌ No | ✅ Yes - Copy between collections |

## Mod Creation & Editing

| Feature | DELTAMOD | DELTAHUB |
|---------|----------|----------|
| **Mod Editor** | ⚠️ MiscTools | ✅ Yes - Plugin (Mod Editor) |
| **Create Mods** | ❌ No | ✅ Yes - Via plugin |
| **Edit Mods** | ❌ No | ✅ Yes - Via plugin |
| **Mod Metadata** | ✅ Yes - meta.json | ✅ Yes - mod_config.json |
| **Component Versioning** | ❌ No | ✅ Yes - Version each file/component separately |
| **Mod Icons** | ✅ Yes - icon.png | ✅ Yes - Multiple icon formats, URL or local |
| **Mod Descriptions** | ✅ Yes - Basic | ✅ Yes - Short description/tagline + full description |
| **Mod Author** | ✅ Yes | ✅ Yes |
| **External URL** | ⚠️ Yes, but it's for compatibility with DELTAHUB | ✅ Yes - Link to mod page (GameBanana, etc.) |

## Plugin System

| Feature | DELTAMOD | DELTAHUB |
|---------|----------|----------|
| **Plugin System** | ❌ No | ✅ Yes - Full plugin architecture |
| **Plugin Installation** | ❌ No | ✅ Yes - From file, URL, or deltahub:// |
| **Plugin Management** | ❌ No | ✅ Yes - Enable/disable/delete plugins |
| **Plugin Search** | ❌ No | ✅ Yes - Browse plugin list |
| **UI Plugins** | ❌ No | ✅ Yes - Add custom tabs |
| **Background Plugins** | ❌ No | ✅ Yes - Event hooks (game launch/exit) |
| **Plugin API** | ❌ No | ✅ Yes - PluginAPI for configuration and access |
| **Plugin Localization** | ❌ No | ✅ Yes - Multi-language plugin support |
| **Built-in Plugins** | ❌ No | ✅ Yes - Save Manager, Mod Editor, XDELTA Patcher |

## Social & Communication

| Feature | DELTAMOD | DELTAHUB |
|---------|----------|----------|
| **Built-in Chat** | ❌ No | ✅ Yes - Anonymous chat with language channels |
| **Online User Count** | ❌ No | ✅ Yes - Display online users |

## Settings & Configuration

| Feature | DELTAMOD | DELTAHUB |
|---------|----------|----------|
| **Settings Menu** | ✅ Yes - General, UI, Installation, Advanced | ✅ Yes - Comprehensive settings |
| **Game Path Configuration** | ✅ Yes | ✅ Yes - Separate paths for each game |
| **Mods Folder Path** | ✅ Yes | ✅ Yes - Customizable |
| **Settings Export/Import** | ❌ No | ✅ Yes - Theme import/export |
| **Settings Reset** | ❌ No | ✅ Yes - Reset to defaults |
| **Open Program Folder** | ❌ No | ✅ Yes - Quick access button |

## Updates & Maintenance

| Feature | DELTAMOD | DELTAHUB |
|---------|----------|----------|
| **Auto-updates** | ✅ Yes - Windows only | ✅ Yes - Cross-platform |
| **Update Notifications** | ✅ Yes | ✅ Yes |
| **Changelog** | ✅ Yes | ✅ Yes - View changelog |
| **Mod Update Checking** | ❌ No | ✅ Yes - Check for mod updates from GameBanana |
| **Version Display** | ✅ Yes | ✅ Yes |

## Platform Support

| Feature | DELTAMOD | DELTAHUB |
|---------|----------|----------|
| **Windows** | ✅ Yes - Officially supported | ✅ Yes - Fully supported |
| **Linux** | ⚠️ Partial - Requires Proton, limited support | ✅ Yes - Native support |
| **macOS** | ❌ No - Not officially supported | ✅ Yes - Supported |
| **Cross-platform** | ❌ No | ✅ Yes - Python/PyQt6 |

## Additional Features

| Feature | DELTAMOD | DELTAHUB |
|---------|----------|----------|
| **Credits Page** | ✅ Yes | ✅ Yes - Help & Info page |
| **Error Handling** | ✅ Yes - Error dialogs | ✅ Yes - Comprehensive error handling |
| **Mod Validation** | ✅ Yes | ✅ Yes - Validate mod structure |
| **Mod Conflict Detection** | ❌ No | ✅ Yes - Priority system handles conflicts |
| **Backup System** | ✅ Yes - File restoration | ✅ Yes - Automatic backup before modding |
| **Logging** | ✅ Yes - Console logs | ✅ Yes - Error logging |
| **GameBanana Integration** | ✅ Yes - Browse mods | ✅ Yes - Browse, search, install, update check |
| **Mod Verification** | ❌ No | ✅ Yes - Public mod verification |
| **Secret Key System** | ❌ No | ✅ Yes - For editing public mods |
| **Mod Hiding** | ❌ No | ✅ Yes - Hide mods from library |
| **Mod Statistics** | ❌ No | ✅ Yes - Downloads, creation/update dates |

## Summary

**DELTAMOD** focuses on:
- Simple mod management for DELTARUNE
- GameBanana integration
- Basic theming
- Windows-first approach

**DELTAHUB** provides:
- Comprehensive mod management for multiple games
- Advanced features (modpacks, priority system, chapter mode)
- Plugin system for extensibility
- Full customization (themes, localization, UI)
- Cross-platform support
- Social features (chat)
- Advanced mod creation tools
- Save management
- One-click installation system


