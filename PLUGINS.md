# DELTAHUB Plugins List

Welcome everyone! This file contains a list of all available plugins for the community.

<details>
<summary><h1>How to Add Your Plugin</h1></summary>

To add your plugin to this list, follow these steps:

1. **Prepare your plugin archive:**
   - Ensure your plugin contains a `main.py` file in the root of the archive
   - The plugin should be packaged in a supported archive format (ZIP, 7Z, RAR, TAR.GZ, LZMA)
   - The archive should extract to a folder containing `main.py` in its root

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

## Plugin Name

**Version:** X.X.X  
**Author:** Author Name (optional)  
**Description:** Brief description of the plugin's functionality  
**Download Link:** [Direct link to archive](URL)   
**Additional Information:** Any additional information (optional)## Plugin Requirements

- The plugin must be functional and tested
- The plugin must not contain malicious code
- The plugin must comply with DELTAHUB standards
- The download link must be direct (should not require additional actions from the user)
- The plugin must have a valid `main.py` file with required fields: `PLUGIN_NAME`, `VERSION`, `DESCRIPTION`

</details>

## System Monitor

**Version:** 1.0.0  
**Author:** DELTAHUB  
**Description:** A plugin for monitoring system resources. Displays information about CPU, memory, and disk in a separate interface tab.  
**Download Link:** [https://github.com/example/system-monitor/releases/download/v1.0.0/system-monitor.zip](https://github.com/example/system-monitor/releases/download/v1.0.0/system-monitor.zip)  
**Additional Information:**  
- Requires Python 3.8+.  
- Compatible with DELTAHUB version 1.0.0 and above.
