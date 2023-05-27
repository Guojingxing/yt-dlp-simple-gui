import subprocess
from subprocess import CalledProcessError
import shlex
import re
import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

"""简易视频/字幕下载软件（yt-dlp GUI）"""

# 字幕语言代码
sub_langs = ('af', 'ak', 'sq', 'am', 'ar', 'hy', 'as', 'ay', 'az', 'bn', 'eu', 'be', 'bho', 'bs', 'bg', 'my', 'ca', 'ceb', 'zh-Hans', 'zh-Hant', 'zh-CN', 'co', 'hr', 'cs', 'da', 'dv', 'nl', 'en', 'eo', 'et', 'ee', 'fil', 'fi', 'fr', 'gl', 'lg', 'ka', 'de', 'el', 'gn', 'gu', 'ht', 'ha', 'haw', 'iw', 'hi', 'hmn', 'hu', 'is', 'ig', 'id', 'ga', 'it', 'ja', 'jv', 'kn', 'kk', 'km', 'rw', 'ko', 'kri', 'ku', 'ky', 'lo', 'la', 'lv', 'ln', 'lt', 'lb', 'mk', 'mg', 'ms', 'ml', 'mt', 'mi', 'mr', 'mn', 'ne', 'nso', 'no', 'ny', 'or', 'om', 'ps', 'fa', 'pl', 'pt', 'pa', 'qu', 'ro', 'ru', 'sm', 'sa', 'gd', 'sr', 'sn', 'sd', 'si', 'sk', 'sl', 'so', 'st', 'es', 'su', 'sw', 'sv', 'tg', 'ta', 'tt', 'te', 'th', 'ti', 'ts', 'tr', 'tk', 'uk', 'ur', 'ug', 'uz', 'vi', 'cy', 'fy', 'xh', 'yi', 'yo', 'zu')

def download_video():
    video_link = link_entry.get()
    if video_link == "":
        messagebox.showinfo("提示", "请输入视频链接")
        return
    save_folder = os.path.normpath(folder_entry.get()).replace("\\", "/")
    video_quality = selected_video_quality.get()
    audio_quality = selected_audio_quality.get()
    video_format = selected_video_format.get()
    audio_format = selected_audio_format.get()
    browser_to_import_cookie = selected_browser.get()
    only_download_audio = only_download_audio_var.get()
    recode_video = recode_video_var.get()
    recode_video_format = selected_recode_video.get()
    download_thumbnail = download_thumbnail_var.get()

    if save_folder == "":
        save_folder = "./"  # 默认为当前文件夹

    #命令行代码，添加命令时一定要在前面加一个空格
    cmd_append = ""

    if is_bilibili_url(video_link):
        cmd_append += f" --cookies-from-browser {browser_to_import_cookie}"

    if recode_video:
        cmd_append += f" --recode-video {recode_video_format}"

    if download_thumbnail:
        cmd_append += f" --write-thumbnail {video_link} --convert-thumbnails jpg"

    if only_download_audio:
        cmd_append += f" -x --audio-format {audio_format}"
        if audio_quality != '0':
            cmd_append += f" --audio-quality {audio_quality}"
    
    command = f"./yt-dlp.exe {video_link} -f 'bestvideo[height<={video_quality}][ext={video_format}]+bestaudio[ext={audio_format}]/best[height<={video_quality}][ext={video_format}]' --paths \"{save_folder}\"" + cmd_append + subtitle_command()
    print("执行命令：\n"+command)
    #return
    
    run_ytdlp(command, save_folder)

# 字幕指令格式化
def subtitle_command():
    subtitle_setting = selected_subtitle_setting.get()
    subtitle_format = subtitle_format_var.get()
    subtitle_langs = subtitle_langs_var.get()
    needs_translation = needs_translation_checkbox_var.get()
    subtitle_trans_dest_lang = translation_dest_lang.get()
    embed_sub = embed_sub_checkbox_var.get()
    
    if needs_translation:
        LANGUAGE_CODE = f"{subtitle_trans_dest_lang}-{subtitle_langs}"
        formatted_subtitle_command = f" --write-auto-subs --sub-format {subtitle_format} --sub-langs {LANGUAGE_CODE}"
    else:
        LANGUAGE_CODE = subtitle_langs
        formatted_subtitle_command = f" --write-subs --sub-format {subtitle_format} --sub-langs {LANGUAGE_CODE}"

    if embed_sub:
        formatted_subtitle_command += f" --embed-subs"

    if subtitle_setting == 2:
        return ""
    elif subtitle_setting == 1:
        return formatted_subtitle_command
    else:
        return " --skip-download" + formatted_subtitle_command

# 运行yt-dlp命令并捕获输出
def run_ytdlp(command, save_folder):
    try:
        # 使用subprocess模块运行命令并显示命令行窗口
        subprocess.run(shlex.split(command), check=True)
        
        if messagebox.askyesno("成功", "下载完成！\n"
                              "是否要打开文件夹？"):
            abs_folder = os.path.abspath(save_folder)
            if not os.path.exists(abs_folder):
                os.makedirs(abs_folder)
            os.startfile(abs_folder)
    except CalledProcessError as e:
        error_message = e.stderr.decode('utf-8') if e.stderr else "未知错误"
        messagebox.showerror("失败", f"下载过程中出现错误：{error_message}")

# 判断是否为b站网址
def is_bilibili_url(video_link):
    pattern = r'(https?://)?(www\.)?(bilibili\.com|b23\.tv)'
    match = re.search(pattern, video_link)
    return match is not None

# 创建主窗口
root = tk.Tk()
root.title("视频下载器(yt-dlp)")

# 设置行和列的权重
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)
root.rowconfigure(4, weight=1)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)

# 设置窗口最小和最大尺寸
fixed_height = 320
root.minsize(600, fixed_height)
root.maxsize(700, fixed_height)

# 第一行 创建保存文件夹和浏览器选项
folder_label = tk.Label(root, text="保存文件夹")
folder_label.grid(row=0, column=0, sticky="e")

folder_entry = tk.Entry(root, width=50)
folder_entry.grid(row=0, column=1, columnspan=1, padx=10, pady=5, sticky="we")

folder_button = tk.Button(root, text="选择文件夹", command=lambda: folder_entry.delete(0, tk.END) or folder_entry.insert(tk.END, filedialog.askdirectory()))
folder_button.grid(row=0, column=2, padx=10, pady=5, sticky="we")

folder_entry.grid_rowconfigure(0, weight=1)
folder_entry.grid_columnconfigure(0, weight=1)

# 第二行 创建字幕设置
subtitle_label = tk.Label(root, text="字幕选项")
subtitle_label.grid(row=1, column=0, sticky="e")

## 创建一个变量来存储字幕下载设置
selected_subtitle_setting = tk.IntVar()
selected_subtitle_setting.set(2)

## 创建单选框
subtitle_setting_frame = tk.Frame(root)
for i in range(4):
    subtitle_setting_frame.columnconfigure(i, weight=1)

sub_video_radio_button_frame = tk.Frame(subtitle_setting_frame)
for i in range(3):
    sub_video_radio_button_frame.columnconfigure(i, weight=1)

only_sub_radio_button = tk.Radiobutton(sub_video_radio_button_frame, text="仅下载字幕", variable=selected_subtitle_setting, value=0)
only_sub_radio_button.grid(row=0, column=0, sticky="we")

sub_and_video_radio_button = tk.Radiobutton(sub_video_radio_button_frame, text="下载字幕和视频", variable=selected_subtitle_setting, value=1)
sub_and_video_radio_button.grid(row=0, column=1, sticky="we")

only_video_radio_button = tk.Radiobutton(sub_video_radio_button_frame, text="仅下载视频", variable=selected_subtitle_setting, value=2)
only_video_radio_button.grid(row=0, column=2, sticky="we")

sub_video_radio_button_frame.grid(row=0, column=0, columnspan=4, sticky="we")

## 字幕格式和语言部分
sub_format_langs_label = tk.Label(subtitle_setting_frame, text="格式")
sub_format_langs_label.grid(row=1, column=0, sticky="e")

### 创建两个变量来存储字幕格式和语言设置
subtitle_format_var = tk.StringVar()
subtitle_format_var.set("srt")

subtitle_format_list = ("best", "srt", "sub", "ssa", "smi", "vtt", "sub", "ass", "txt", "psb", "txt", "ttml", "srv3", "srv2", "srv1", "json3")
subtitle_format_menu = ttk.Combobox(subtitle_setting_frame, values=subtitle_format_list, textvariable=subtitle_format_var, width=10)
subtitle_format_menu.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

sub_format_langs_label = tk.Label(subtitle_setting_frame, text="语言")
sub_format_langs_label.grid(row=1, column=2, sticky="e")

subtitle_langs_var = tk.StringVar()
subtitle_langs_var.set("zh-CN")

subtitle_langs_menu = ttk.Combobox(subtitle_setting_frame, values=sub_langs, textvariable=subtitle_langs_var, width=10)
subtitle_langs_menu.grid(row=1, column=3, padx=10, pady=5, sticky="we")

#是否内嵌字幕？
embed_sub_checkbox_var = tk.BooleanVar(value=False)
embed_sub_checkbox = tk.Checkbutton(subtitle_setting_frame, text="内嵌字幕(仅mp4,webm,mkv)", variable=embed_sub_checkbox_var)
embed_sub_checkbox.grid(row=2, column=0, columnspan=2, sticky="e")

# 是否需要字幕翻译？
needs_translation_checkbox_var = tk.BooleanVar(value=False)
needs_translation_checkbox = tk.Checkbutton(subtitle_setting_frame, text="翻译为", variable=needs_translation_checkbox_var)
needs_translation_checkbox.grid(row=2, column=2, sticky="we")

#翻译语言选择
translation_dest_lang = tk.StringVar()
translation_dest_lang.set("en")

translation_dest_lang_menu = ttk.Combobox(subtitle_setting_frame, values=sub_langs, textvariable=translation_dest_lang, width=10)
translation_dest_lang_menu.grid(row=2, column=3, columnspan=1, padx=10, pady=5, sticky="we")

#分割线
separator = ttk.Separator(subtitle_setting_frame, orient='horizontal')
separator.grid(row=3, column=0, columnspan=4, padx=10, pady=10, sticky="we")

subtitle_setting_frame.grid(row=1, column=1, sticky="we")


# 第三行 创建视频设置
video_label = tk.Label(root, text="视频设置")
video_label.grid(row=2, column=0, sticky="e")

video_setting_frame = tk.Frame(root)#视频设置框架头
for i in range(4):
    video_setting_frame.columnconfigure(i, weight=1)

## 创建视频画质菜单
video_quality_label = tk.Label(video_setting_frame, text="视频画质")
video_quality_label.grid(row=0, column=0, sticky="e")

selected_video_quality = tk.StringVar(root)
selected_video_quality.set("720")  # 设置默认选项为720
video_quality_list = ("144", "240", "360", "480", "720", "1080", "1440", "2160", "4320")
quality_menu = ttk.Combobox(video_setting_frame, values=video_quality_list, textvariable=selected_video_quality, width=10)
quality_menu.grid(row=0, column=1, columnspan=1, padx=10, pady=5, sticky="we")

## 创建视频格式菜单
video_format_label = tk.Label(video_setting_frame, text="视频格式")
video_format_label.grid(row=0, column=2, sticky="e")

selected_video_format = tk.StringVar(root)
selected_video_format.set("mp4")
video_format_list = ("avi", "flv", "mkv", "mov", "mp4", "webm")
video_format_menu = ttk.Combobox(video_setting_frame, values=video_format_list, textvariable=selected_video_format, width=10)
video_format_menu.grid(row=0, column=3, columnspan=1, padx=10, pady=5, sticky="we")

## 创建音质菜单
audio_quality_label = tk.Label(video_setting_frame, text="音质(0为最佳)")
audio_quality_label.grid(row=1, column=0, sticky="e")

selected_audio_quality = tk.StringVar(root)
selected_audio_quality.set('0')
audio_quality_list = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10')
quality_menu = ttk.Combobox(video_setting_frame, values=audio_quality_list, textvariable=selected_audio_quality, width=10)
quality_menu.grid(row=1, column=1, columnspan=1, padx=10, pady=5, sticky="we")

## 创建音频格式菜单
audio_format_label = tk.Label(video_setting_frame, text="音频格式")
audio_format_label.grid(row=1, column=2, sticky="e")

selected_audio_format = tk.StringVar(root)
selected_audio_format.set("m4a")
audio_format_list = ("best", "aac", "alac", "flac", "m4a", "mp3", "opus", "vorbis", "wav")
audio_format_menu = ttk.Combobox(video_setting_frame, values=audio_format_list, textvariable=selected_audio_format, width=10)
audio_format_menu.grid(row=1, column=3, columnspan=1, padx=10, pady=5, sticky="we")

browser_label = tk.Label(video_setting_frame, text="登陆的浏览器")
browser_label.grid(row=2, column=0, sticky="e")

selected_browser = tk.StringVar()
selected_browser.set("chrome")
browser_list = ("brave", "chrome", "chromium", "edge", "firefox", "opera", "safari", "vivaldi")
browser_menu = ttk.Combobox(video_setting_frame, values=browser_list, textvariable=selected_browser, width=10)
browser_menu.grid(row=2, column=1, columnspan=1, padx=10, pady=5, sticky="we")

# 是否视频转码？
recode_video_var = tk.BooleanVar(value=False)
recode_video_checkbox = tk.Checkbutton(video_setting_frame, text="格式转换", variable=recode_video_var)
recode_video_checkbox.grid(row=2, column=2, sticky="e")

selected_recode_video = tk.StringVar(root)
selected_recode_video.set("mp4") 
recode_video_list = ("avi", "flv", "gif", "mkv", "mov", "mp4", "webm", "aac", "aiff", "alac", "flac", "m4a", "mka", "mp3", "ogg", "opus", "vorbis", "wav")
recode_video_menu = ttk.Combobox(video_setting_frame, values=recode_video_list, state="readonly", textvariable=selected_recode_video, width=10)
recode_video_menu.grid(row=2, column=3, columnspan=1, padx=10, pady=5, sticky="we")

video_setting_frame.grid(row=2, column=1, sticky="we") # 视频设置框架尾

# 是否仅下载音频？
only_download_audio_var = tk.BooleanVar(value=False)
only_download_audio_checkbox = tk.Checkbutton(root, text="仅下载音频", variable=only_download_audio_var)
only_download_audio_checkbox.grid(row=2, column=2, sticky="w")


# 第四行 创建视频链接输入框
link_label = tk.Label(root, text="视频链接")
link_label.grid(row=3, column=0, sticky="e")

link_entry = tk.Entry(root, width=50)
link_entry.grid(row=3, column=1, columnspan=1, padx=10, pady=5, sticky="we")

link_entry.grid_rowconfigure(0, weight=1)
link_entry.grid_columnconfigure(0, weight=1)

# 是否下载缩略图？
download_thumbnail_var = tk.BooleanVar(value=False)
download_thumbnail_checkbox = tk.Checkbutton(root, text="下载缩略图", variable=download_thumbnail_var)
download_thumbnail_checkbox.grid(row=3, column=2, sticky="w")

# 第五行 下载按钮
download_btn_frame = tk.Frame(root)
download_btn_frame.grid(row=4, column=0, columnspan=5, sticky="we")

download_btn_frame.columnconfigure(0, weight=5)
download_btn_frame.columnconfigure(1, weight=1)
download_btn_frame.columnconfigure(2, weight=5)

download_button = tk.Button(download_btn_frame, text="开始下载", command=download_video, width=10)
download_button.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

# 运行主循环
root.mainloop()
