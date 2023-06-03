# Simple Video/Subtitle Downloader
[![MIT License](https://img.shields.io/badge/license-MIT-red)](https://github.com/Guojingxing/yt-dlp-simple-gui/blob/main/LICENSE)
[![latest version](https://img.shields.io/github/v/release/Guojingxing/yt-dlp-simple-gui?label=latest%20release)](https://github.com/Guojingxing/yt-dlp-simple-gui/releases/latest)
[![GitHub release downloads(latest version)](https://img.shields.io/github/downloads/Guojingxing/yt-dlp-simple-gui/total?color=brightgreen)](https://github.com/Guojingxing/yt-dlp-simple-gui/releases)
![framework](https://img.shields.io/badge/framework-Qt-green)

**English** | [中文（简体）](README.md) | [中文（繁體）](https://github.com/Guojingxing/yt-dlp-simple-gui/wiki/Wiki-zh-TW)

This script provides a simple graphical interface for the [`yt-dlp`](https://github.com/yt-dlp/yt-dlp) command. No installation is required. Just open the software, paste the video link, and click "Start Download" or press `Enter` to download the video.
## System Requirements 
System Requirements | Description
-|-
Operating System | Windows 7 and above
Other Software | **ffmpeg (important, must be installed)**
### ffmpeg installation and configuration of environment variables
1. Download ffmpeg from the [ffmpeg official website](https://www.ffmpeg.org/download.html).
2. Open "Edit System Environment Variables" settings.
3. Find the variable named "Path" in the system variables and click "Edit".
4. Add the installation directory path of ffmpeg (e.g. "C:\path\to\ffmpeg"). 
5. Confirm the changes and close the window. Restart your computer or open a new command prompt to enable the environment variable.
## Basic Features
- **Video download**: You can specify videos (up to YouTube 8K) and audio of any quality. It supports downloading playlists and thumbnails. 
- **Support for most video websites**: It supports **Bilibili, YouTube, Youku, TikTok** and almost all video websites. See [Supported Websites](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md) for details.
- **Support for keyword search**: Enter a search keyword in the video link to download the most matching video from YouTube. 
- **Subtitle download**: You can download subtitle files (if any) in the specified language and format. Check "Translate Subtitles" to translate them into the desired language. 
## Tutorial
Download the software, no installation is required. After opening, paste the video link and click "Start Download" or press `Enter` to download the video.
### FAQ
For more common issues and precautions, please refer to [Wiki-en#FAQ](https://github.com/Guojingxing/yt-dlp-simple-gui/wiki/Wiki-en#faq).
## Self-compiled exe file
This section describes how to package `yt-dlp-simple-gui.py` into an `exe` file. For specific steps, please refer to [Wiki-en#Self-compiled exe file](https://github.com/Guojingxing/yt-dlp-simple-gui/wiki/Wiki-en#self-compiled-exe-file).
## License
This project is licensed under the [MIT License](LICENSE).