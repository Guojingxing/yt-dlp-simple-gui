# 简易视频/字幕下载软件
[![latest version](https://img.shields.io/github/v/release/Guojingxing/yt-dlp-simple-gui)](https://github.com/Guojingxing/yt-dlp-simple-gui/releases/tag/v1.1.3)
[![stable version](https://img.shields.io/badge/version-1.1.3-blue?label=stable%20version)](https://github.com/Guojingxing/yt-dlp-simple-gui/releases/tag/v1.1.3)
![GitHub release downloads(latest version)](https://img.shields.io/github/downloads/Guojingxing/yt-dlp-simple-gui/total)

该脚本为[`yt-dlp`](https://github.com/yt-dlp/yt-dlp)命令的简易可视化界面。

请确保系统安装了以下安装包：`yt-dlp`、`ffmpeg`、`pyinstaller`。如果没有安装，请在命令行运行以下代码进行安装：
```bat
pip install yt-dlp ffmpeg pyinstaller
```
在项目目录下，执行以下命令运行：
```bat
python .\yt-dlp-simple-gui.py
```
或者执行以下代码将其封装成`exe`文件使用（[稳定发行版](https://github.com/Guojingxing/yt-dlp-simple-gui/releases/tag/v1.1.3)），封装后的`exe`文件在`dist`目录下：
```bat
pyinstaller -F --onefile .\yt-dlp-simple-gui.py --paths C:\users\dell\appdata\local\programs\python\python310\lib\site-packages\yt-dlp,ffmpeg,websockets,pycryptodomex,brotli,certifi,mutagen,ttkthemes,pillow --clean
```
主要功能：
- **默认当前文件夹**：下载文件夹选填，默认下载至当前`yt-dlp-simple-gui.exe`文件所在目录的`videos`下
- **下载指定画质视频**：可指定任意画质的视频（最高可支持YouTube 8K）以及音频，支持下载播放列表和缩略图
- **支持大多数视频网站**：支持**哔哩哔哩、YouTube、优酷、抖音**等几乎所有视频网站，详见[支持的网站](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md)
- **字幕可指定语言格式**：可下载指定语言和格式的字幕文件（若有），勾选“字幕翻译”即可翻译为想要的语言
- **下载B站高清视频**：若要下载B站高清视频，需要先在浏览器中登录，然后选择已登录的相应浏览器即可
- **支持导入Cookie**：对于部分开通会员或者登录才能看的视频，勾选导入Cookie即可下载（[V1.1.2版本](https://github.com/Guojingxing/yt-dlp-simple-gui/releases/tag/v1.1.2)及以后）
