import subprocess
from subprocess import CalledProcessError
import shlex
import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

"""简易视频/字幕下载软件（yt-dlp GUI）"""

#字幕语言代码
sub_langs = ('af', 'ak', 'sq', 'am', 'ar', 'hy', 'as', 'ay', 'az', 'bn', 'eu', 'be', 'bho', 'bs', 'bg', 'my', 'ca', 'ceb', 'zh-Hans', 'zh-Hant', 'zh-CN', 'co', 'hr', 'cs', 'da', 'dv', 'nl', 'en', 'eo', 'et', 'ee', 'fil', 'fi', 'fr', 'gl', 'lg', 'ka', 'de', 'el', 'gn', 'gu', 'ht', 'ha', 'haw', 'iw', 'hi', 'hmn', 'hu', 'is', 'ig', 'id', 'ga', 'it', 'ja', 'jv', 'kn', 'kk', 'km', 'rw', 'ko', 'kri', 'ku', 'ky', 'lo', 'la', 'lv', 'ln', 'lt', 'lb', 'mk', 'mg', 'ms', 'ml', 'mt', 'mi', 'mr', 'mn', 'ne', 'nso', 'no', 'ny', 'or', 'om', 'ps', 'fa', 'pl', 'pt', 'pa', 'qu', 'ro', 'ru', 'sm', 'sa', 'gd', 'sr', 'sn', 'sd', 'si', 'sk', 'sl', 'so', 'st', 'es', 'su', 'sw', 'sv', 'tg', 'ta', 'tt', 'te', 'th', 'ti', 'ts', 'tr', 'tk', 'uk', 'ur', 'ug', 'uz', 'vi', 'cy', 'fy', 'xh', 'yi', 'yo', 'zu')

def download_video():
    video_link = link_entry.get()
    save_folder = folder_entry.get()
    video_quality = selected_quality.get()
    
    if save_folder == "":
        save_folder = "./"  # 默认为当前文件夹
    
    command = f"yt-dlp -f 'bestvideo[height<={video_quality}][ext=mp4]+bestaudio[ext=m4a]/best[height<={video_quality}][ext=mp4]'" + subtitle_command() + f" --paths {save_folder} {video_link}"
    print("执行命令：\n"+command)
    
    # 运行yt-dlp命令并捕获输出
    try:
        # 使用subprocess模块运行命令并显示命令行窗口
        subprocess.run(shlex.split(command), check=True)
        
        if messagebox.askyesno("成功", "视频下载完成！\n"
                              "是否要打开文件夹？"):
            abs_folder = os.path.abspath(save_folder)
            if not os.path.exists(abs_folder):
                os.makedirs(abs_folder)
            os.startfile(abs_folder)
    except CalledProcessError as e:
        messagebox.showerror("下载失败", f"下载过程中出现错误：{e.output.decode('utf-8')}")

def download_bilibili_video():
    video_link = link_entry2.get()
    save_folder = folder_entry.get()
    video_quality = selected_quality.get()
    browser_to_import_cookie = selected_browser.get()
    
    if save_folder == "":
        save_folder = "./"  # 默认为当前文件夹

    command = f"yt-dlp --cookies-from-browser {browser_to_import_cookie} -f 'bestvideo[height<={video_quality}][ext=mp4]+bestaudio[ext=m4a]/best[height<={video_quality}][ext=mp4]'" + subtitle_command() + f" --paths {save_folder} {video_link}"
    print("执行命令：\n"+command)

    # 运行yt-dlp命令并捕获输出
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
        messagebox.showerror("失败", f"下载过程中出现错误：{e.output.decode('utf-8')}")

def subtitle_command():
    subtitle_setting = selected_subtitle_setting.get()
    subtitle_format = subtitle_format_var.get()
    subtitle_langs = subtitle_langs_var.get()
    needs_translation = needs_translation_checkbox_var.get()
    subtitle_trans_dest_lang = translation_dest_lang.get()

    if needs_translation:
        formatted_subtitle_command = f" --write-auto-subs --sub-format {subtitle_format} --sub-langs {subtitle_trans_dest_lang}-{subtitle_langs}"
    else:
        formatted_subtitle_command = f" --write-subs --sub-format {subtitle_format} --sub-langs {subtitle_langs}"

    if subtitle_setting == 2:
        return ""
    elif subtitle_setting == 1:
        return formatted_subtitle_command
    else:
        return " --skip-download " + formatted_subtitle_command


# 创建主窗口
root = tk.Tk()
root.title("视频下载器(yt-dlp)")

# 设置行和列的权重
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)

# 设置窗口最小和最大尺寸
root.minsize(700, 200)
root.maxsize(800, 400)

# 第一行
# 创建保存文件夹选择按钮
folder_label = tk.Label(root, text="保存文件夹")
folder_label.grid(row=0, column=0, sticky="e")

folder_entry = tk.Entry(root, width=50)
folder_entry.grid(row=0, column=1, columnspan=1, padx=10, pady=5, sticky="we")

folder_button = tk.Button(root, text="选择文件夹", command=lambda: folder_entry.insert(tk.END, filedialog.askdirectory()))
folder_button.grid(row=0, column=2, padx=10, pady=5, sticky="we")

folder_entry.grid_rowconfigure(0, weight=1)
folder_entry.grid_columnconfigure(0, weight=1)

## 创建一个变量来存储选择的画质
selected_quality = tk.StringVar(root)
selected_quality.set("720")  # 设置默认选项为720

## 创建下拉菜单
quality_label = tk.Label(root, text="视频画质")
quality_label.grid(row=0, column=3, sticky="e")

video_quality_list = ("144", "240", "360", "480", "720", "1080", "1440", "2160", "4320")
quality_menu = ttk.Combobox(root, values=video_quality_list, textvariable=selected_quality, width=10)
quality_menu.grid(row=0, column=4, columnspan=1, padx=10, pady=5, sticky="we")

# 第二行
# 创建字幕设置
subtitle_label = tk.Label(root, text="字幕选项")
subtitle_label.grid(row=1, column=0, sticky="e")

## 创建一个变量来存储字幕下载设置
selected_subtitle_setting = tk.IntVar()
selected_subtitle_setting.set(2)

## 创建单选框
subtitle_setting_frame = tk.Frame(root)
subtitle_setting_frame.columnconfigure(0, weight=1)
subtitle_setting_frame.columnconfigure(1, weight=1)
subtitle_setting_frame.columnconfigure(2, weight=1)

only_sub_radio_button = tk.Radiobutton(subtitle_setting_frame, text="仅下载字幕", variable=selected_subtitle_setting, value=0)
only_sub_radio_button.grid(row=0, column=0, sticky="we")

sub_and_video_radio_button = tk.Radiobutton(subtitle_setting_frame, text="下载字幕和视频", variable=selected_subtitle_setting, value=1)
sub_and_video_radio_button.grid(row=0, column=1, sticky="we")

only_video_radio_button = tk.Radiobutton(subtitle_setting_frame, text="仅下载视频", variable=selected_subtitle_setting, value=2)
only_video_radio_button.grid(row=0, column=2, sticky="we")

subtitle_setting_frame.grid(row=1, column=1, sticky="we")

## 字幕格式和语言部分
sub_format_langs_label = tk.Label(root, text="格式/语言")
sub_format_langs_label.grid(row=1, column=2, sticky="e")

### 创建两个变量来存储字幕格式和语言设置
subtitle_format_var = tk.StringVar()
subtitle_format_var.set("srt")

subtitle_format_list = ("best", "srt", "sub", "ssa", "smi", "vtt", "sub", "ass", "txt", "psb", "txt", "ttml", "srv3", "srv2", "srv1", "json3")
subtitle_format_menu = ttk.Combobox(root, values=subtitle_format_list, textvariable=subtitle_format_var, width=10)
subtitle_format_menu.grid(row=1, column=3, padx=10, pady=5, sticky="e")

subtitle_langs_var = tk.StringVar()
subtitle_langs_var.set("zh-CN")

subtitle_langs_menu = ttk.Combobox(root, values=sub_langs, textvariable=subtitle_langs_var, width=10)
subtitle_langs_menu.grid(row=1, column=4, padx=10, pady=5, sticky="we")

# 第三行
# 创建视频链接输入框
link_label = tk.Label(root, text="视频链接")
link_label.grid(row=2, column=0, sticky="e")

link_entry = tk.Entry(root, width=50)
link_entry.grid(row=2, column=1, columnspan=1, padx=10, pady=5, sticky="we")

# 是否需要字幕翻译？
needs_translation_checkbox_var = tk.BooleanVar(value=False)
needs_translation_checkbox = tk.Checkbutton(root, text="字幕翻译为", variable=needs_translation_checkbox_var)
needs_translation_checkbox.grid(row=2, column=2, padx=10, pady=5, sticky="we")

#翻译语言选择
translation_dest_lang = tk.StringVar()
translation_dest_lang.set("zh-Hans")

translation_dest_lang_menu = ttk.Combobox(root, values=sub_langs, textvariable=translation_dest_lang, width=10)
translation_dest_lang_menu.grid(row=2, column=3, columnspan=1, padx=10, pady=5, sticky="we")

download_button = tk.Button(root, text="开始下载", command=download_video)
download_button.grid(row=2, column=4, padx=10, pady=5, sticky="we")

link_entry.grid_rowconfigure(0, weight=1)
link_entry.grid_columnconfigure(0, weight=1)

# 第四行
# 创建B站视频下载部分
bilibili_label = tk.Label(root, text="B站视频链接")
bilibili_label.grid(row=3, column=0, sticky="e")

link_entry2 = tk.Entry(root, width=50)
link_entry2.grid(row=3, column=1, columnspan=1, padx=10, pady=5, sticky="we")

browser_label = tk.Label(root, text="登陆的浏览器")
browser_label.grid(row=3, column=2, sticky="e")

selected_browser = tk.StringVar()
selected_browser.set("chrome")

browser_list = ("brave", "chrome", "chromium", "edge", "firefox", "opera", "safari", "vivaldi")
browser_menu = ttk.Combobox(root, values=browser_list, textvariable=selected_browser, width=10)
browser_menu.grid(row=3, column=3, columnspan=1, padx=10, pady=5, sticky="we")

download_button2 = tk.Button(root, text="开始下载", command=download_bilibili_video)
download_button2.grid(row=3, column=4, padx=10, pady=5, sticky="we")

link_entry2.grid_rowconfigure(0, weight=1)
link_entry2.grid_columnconfigure(0, weight=1)

# 运行主循环
root.mainloop()
