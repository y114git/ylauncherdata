# DELTAHUB Plugins List

Welcome everyone! This file contains a list of all available plugins for the community.

  - [#0 System Monitor (ONLY FOR EXAMPLE)](#0-system-monitor-only-for-example)
  - [#1 XDELTA Patcher](#1-xdelta-patcher)
  - [#2 Mod Editor](#2-mod-editor)
  - [#3 DR Save Manager](#3-dr-save-manager)

<details>

<summary><h1>How to Add Your Plugin</h1></summary>

To add your plugin to this list, follow these steps:

1. **Prepare your plugin archive:**

   - Ensure your plugin contains a `plugin_init.py` file in the root of the archive

   - The plugin should be packaged in a supported archive format (ZIP, 7Z, RAR, TAR.GZ, LZMA)

   - The archive should extract to a folder containing `plugin_init.py` in its root

2. **Upload the archive:**

   - Upload your plugin archive to a file hosting service that provides direct download links (GitHub Releases, Dropbox, Google Drive, etc.)

   - Get a direct download link (the link should immediately start the file download, not open a preview page)

3. **Create a Pull Request:**

   - Fork the `ylauncherdata` repository

   - Edit the `PLUGINS.md` file

   - Add your plugin information in the format specified below

   - Create a Pull Request with a description of your plugin

## Plugin Entry Format

Each plugin should be added in the following format:

## #(Next number after previous plugin) Plugin Name
<ins>Want to add some screenshots?</ins>
```
<details>
<summary>Screenshots</summary>
<img src="https://example.com" alt="IMG1" width="800">
<img src="https://example.com" alt="IMG1" width="800">
</details>
```

**Version:** X.X.X  

**Author:** Author Name (optional)  

**Description:** Brief description of the plugin's functionality  

**Download:** [Direct link to archive](URL)   

**Additional Information:** Any additional information (optional)

## Plugin Requirements

- The plugin must be functional and tested

- The plugin must not contain malicious code

- The plugin must comply with DELTAHUB standards

- The download link must be direct (should not require additional actions from the user)

- The plugin must have a valid `plugin_init.py` file with required fields: `PLUGIN_NAME`, `VERSION`, `DESCRIPTION`

</details>

## #0 System Monitor (ONLY FOR EXAMPLE)

**Version:** 1.0.0  

**Author:** DELTAHUB  

**Description:** A plugin for monitoring system resources. Displays information about CPU, memory, and disk in a separate interface tab.  

**Download:** https://github.com/example/system-monitor/releases/download/v1.0.0/system-monitor.zip  

**Additional Information:**  

- Requires smart brain

## #1 XDELTA Patcher
<details>
<summary>Screenshots</summary>
<img src="https://i.imgur.com/Woxlrql.png" alt="IMG1" width="800">
<img src="https://i.imgur.com/XOVcWzr.png" alt="IMG2" width="800">
</details>

**Version:** 1.0.0  

**Author:** Y114  

**Description:** Create and apply XDELTA patches. This plugin provides tool for creating binary patches from original and modified files, as well as applying existing patches to files.  

**Download:** https://github.com/y114git/ylauncherdata/releases/download/TESTRD/xdelta_patcher.zip

**Additional Information:**  

- None

## #2 Mod Editor

<details>
<summary>Screenshots</summary>
<img src="https://i.imgur.com/6yxY27d.png" alt="IMG1" width="800">
<img src="https://i.imgur.com/6YdmsAp.png" alt="IMG2" width="800">
<img src="https://i.imgur.com/qaniYxr.png" alt="IMG3" width="800">
</details>

**Version:** 1.0.1  

**Author:** Y114  

**Description:** Create, edit, and publish mods in DELTAHUB format easily. This plugin provides a comprehensive interface for mod management, including mod creation, editing metadata, file management, and publishing capabilities.  

**Download:** https://github.com/y114git/ylauncherdata/releases/download/TESTRD/mod_editor.zip  

**Additional Information:**  

- None

## #3 DR Save Manager

<details>
<summary>Screenshots</summary>
<img src="https://i.imgur.com/SvqcN1j.png" alt="IMG1" width="800">
<img src="https://i.imgur.com/teB1Quw.png" alt="IMG2" width="800">
<img src="https://i.imgur.com/4BBNuym.png" alt="IMG3" width="800">
</details>

**Version:** 1.0.1  

**Author:** Y114  

**Description:** Manages save collections for DELTARUNE and DELTARUNEdemo. This plugin allows you to organize, import, export, and manage multiple save collections for different game sessions.  

**Download:** https://github.com/y114git/ylauncherdata/releases/download/TESTRD/dr_save_manager.zip  

**Additional Information:**  

- Supports both DELTARUNE and DELTARUNEdemo save management.  
