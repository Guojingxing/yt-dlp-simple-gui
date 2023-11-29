# 简易视频/字幕下载软件
[![MIT License](https://img.shields.io/badge/license-MIT-red)](https://github.com/Guojingxing/yt-dlp-simple-gui/blob/main/LICENSE)
[![latest version](https://img.shields.io/github/v/release/Guojingxing/yt-dlp-simple-gui?label=latest%20release)](https://github.com/Guojingxing/yt-dlp-simple-gui/releases/latest)
[![GitHub release downloads(latest version)](https://img.shields.io/github/downloads/Guojingxing/yt-dlp-simple-gui/total?color=brightgreen)](https://github.com/Guojingxing/yt-dlp-simple-gui/releases)
![framework](https://img.shields.io/badge/framework-Qt-green)

[English](README_en.md) | **中文（简体）** | [中文（繁體）](https://github.com/Guojingxing/yt-dlp-simple-gui/wiki/Wiki-zh-TW)

该脚本为[`yt-dlp`](https://github.com/yt-dlp/yt-dlp)命令的简易可视化界面。无需安装，打开软件粘贴视频链接，点击“开始下载”或按`Enter`键即可下载视频。

## 系统要求
系统要求 | 说明
-|-
操作系统 | Windows 7及以上
其他软件 | **ffmpeg（重要，必须安装）**

### ffmpeg安装、配置环境变量
1. 从[ffmpeg官网](https://www.ffmpeg.org/download.html#get-sources)下载并解压ffmpeg。
2. 打开“编辑系统环境变量”设置。
3. 在系统变量中找到名为“Path”的变量，点击“编辑”。
4. 添加ffmpeg的安装目录路径（例如：“C:\path\to\ffmpeg”）。
5. 确认更改并关闭窗口。重启计算机或打开新的命令提示符以使环境变量生效。
## 基本功能
- **视频下载**：可指定任意画质的视频（最高可支持YouTube 8K）以及音频，支持下载播放列表和缩略图
- **支持大多数视频网站**：支持**哔哩哔哩、YouTube、优酷、抖音**等几乎所有视频网站，详见[支持的网站](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md)
- **支持关键词搜索**：在视频链接处输入搜索关键词，可下载YouTube中最匹配的视频
- **字幕下载**：可下载指定语言和格式的字幕文件（若有），勾选“字幕翻译”即可翻译为想要的语言
## 使用教程
下载软件，无需安装，打开后粘贴视频链接，直接点击“开始下载”或按`Enter`键即可下载视频。
### 常见问题
- **导入Cookie**：对于部分需要登录或者开通会员才能看的视频，可能需要勾选导入Cookie后才可下载（[V1.1.2版本](https://github.com/Guojingxing/yt-dlp-simple-gui/releases/tag/v1.1.2)及以后）
- **下载短视频**：由于视频画质为视频最大高度，那么下载抖音、YouTube Shorts或其他短视频时，视频画质应选择大于1920的数字
- **默认当前文件夹**：下载文件夹选填，默认下载至当前软件所在目录的`videos`下
- **下载弹幕**：若要下载B站等弹幕网站的弹幕文件，勾选“下载全部字幕”（V2.1.0新增下载弹幕选项）
- **字幕翻译和自动生成字幕**：
  - 除YouTube外，并非所有网站都支持字幕翻译；
  - **V2.1.0版本前**：若要下载自动生成字幕，视频首先得有自动字幕，然后勾选“翻译”，并将右侧任意一行改为`LANG_CODE-orig`（`LANG_CODE`为[语言代码](https://github.com/yt-dlp/yt-dlp/blob/c26f9b991a0681fd3ea548d535919cec1fbbd430/yt_dlp/extractor/youtube.py#L381-L390)），另一行改成空白。如：将`en`改为`en-orig`（英语自动生成字幕）
  - **V2.1.0版本及以后**：下载自动生成字幕，“语言”选择`auto`即可；若要翻译自动生成字幕，勾选“翻译为”，选择需要翻译成的语言即可。
  
更多常见问题和注意事项，详见[Wiki#注意事项](https://github.com/Guojingxing/yt-dlp-simple-gui/wiki#注意事项)。
## 自编译exe文件
本部分介绍如何将`yt-dlp-simple-gui.py`打包成exe文件，具体步骤详见[Wiki#自编译exe文件](https://github.com/Guojingxing/yt-dlp-simple-gui/wiki#自编译exe文件)。

## 授权许可
本项目使用[MIT许可证](LICENSE)进行授权许可。
