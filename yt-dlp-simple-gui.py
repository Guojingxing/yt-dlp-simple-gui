# Author: Guo Jingxing
# GitHub: https://github.com/Guojingxing/yt-dlp-simple-gui

import yt_dlp
import re
import os
import webbrowser
import datetime
import yaml

import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import filedialog
from tkinter import messagebox

from ttkthemes import ThemedStyle

"""简易视频/字幕下载软件 (yt-dlp GUI)"""

# 字幕语言代码
SUB_LANGS = ('sq', 'aa', 'akk', 'ak', 'ar', 'arc', 'am', 'as', 'az', 'ee', 'ay', 'ga', 'et', 'oc', 'or', 'om', 'ba', 'eu', 'be', 'bm', 'bg', 'nd', 'nso', 'bi', 'is', 'pl', 'bs', 'fa', 'fa-AF', 'fa-IR', 'brx', 'bh', 'br', 'bo', 'tn', 'ts', 'tt', 'da', 'tok', 'de', 'de-AT', 'de-DE', 'de-CH', 'doi', 'ru', 'ru-Latn', 'fo', 'fr', 'fr-BE', 'fr-FR', 'fr-CA', 'fr-CH', 'sa', 'fil', 'fj', 'fi', 'ff', 'km', 'kl', 'ka', 'gu', 'guz', 'gn', 'ie', 'ia', 'kk', 'ht', 'ko', 'ha', 'nl', 'nl-BE', 'nl-NL', 'mxp', 'ki', 'gl', 'ca', 'cs', 'kln', 'kam', 'kn', 'ky', 'cop', 'xh', 'co', 'cr', 'tlh', 'hr', 'qu', 'ks', 'hak', 'hak-TW', 'kok', 'ku', 'lad', 'la', 'lv', 'lo', 'lt', 'ln', 'rn', 'luo', 'lg', 'lb', 'rw', 'luy', 'lu', 'ro', 'mo', 'rm', 'mt', 'mr', 'mg', 'ml', 'ms', 'mk', 'mas', 'mai', 'mni', 'mi', 'mer', 'mn', 'mn-Mong', 'bn', 'lus', 'my', 'nan', 'nan-TW', 'nv', 'nr', 'af', 'st', 'na', 'ne', 'pcm', 'no', 'pap', 'pa', 'pt', 'pt-BR', 'pt-PT', 'ps', 'tw', 'cho', 'chr', 'ja', 'sv', 'sc', 'sm', 'sh', 'sr', 'sr-Latn', 'sr-Cyrl', 'sg', 'sat', 'si', 'sn', 'eo', 'sk', 'sl', 'ss', 'sw', 'gd', 'so', 'tl', 'tg', 'te', 'ta', 'th', 'to', 'ti', 'tr', 'tk', 'tpi', 'wal', 'cy', 'ug', 've', 'vo', 'wo', 'ur', 'uk', 'uz', 'es', 'es-419', 'es-US', 'es-MX', 'es-ES', 'fy', 'scn', 'iw', 'el', 'ho', 'haw', 'sd', 'hu', 'su', 'hy', 'ig', 'ik', 'it', 'yi', 'iu', 'hi', 'hi-Latn', 'id', 'en', 'en-IE', 'en-CA', 'en-US', 'en-IN', 'en-GB', 'yo', 'yue', 'yue-HK', 'vi', 'jv', 'zh', 'zh-Hant', 'zh-Hans', 'zh-TW', 'zh-HK', 'zh-SG', 'zh-CN', 'dz', 'zu', 'ase', 'bgc', 'sdp', 'vro')
TRANS_DEST_LANGS = ('af', 'ak', 'sq', 'am', 'ar', 'hy', 'as', 'ay', 'az', 'bn', 'eu', 'be', 'bho', 'bs', 'bg', 'my', 'ca', 'ceb', 'zh-Hans', 'zh-Hant', 'co', 'hr', 'cs', 'da', 'dv', 'nl', 'en', 'eo', 'et', 'ee', 'fil', 'fi', 'fr', 'gl', 'lg', 'ka', 'de', 'el', 'gn', 'gu', 'ht', 'ha', 'haw', 'iw', 'hi', 'hmn', 'hu', 'is', 'ig', 'id', 'ga', 'it', 'ja', 'jv', 'kn', 'kk', 'km', 'rw', 'ko', 'kri', 'ku', 'ky', 'lo', 'la', 'lv', 'ln', 'lt', 'lb', 'mk', 'mg', 'ms', 'ml', 'mt', 'mi', 'mr', 'mn', 'ne', 'nso', 'no', 'ny', 'or', 'om', 'ps', 'fa', 'pl', 'pt', 'pa', 'qu', 'ro', 'ru', 'sm', 'sa', 'gd', 'sr', 'sn', 'sd', 'si', 'sk', 'sl', 'so', 'st', 'es', 'su', 'sw', 'sv', 'tg', 'ta', 'tt', 'te', 'th', 'ti', 'ts', 'tr', 'tk', 'uk', 'ur', 'ug', 'uz', 'vi', 'cy', 'fy', 'xh', 'yi', 'yo', 'zu')

VERSION = "V1.2.0"
CONFIG_YML = './configs.yml'

configs = {}
# 从文件中加载配置（若有）
def load_configs():
    file_path = CONFIG_YML
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            print("加载用户配置...")
            all_configs = yaml.safe_load(f)
        if all_configs is not None:
            print("配置加载完成")
            return all_configs
    # 处理文件不存在或为空的情况，返回空字典
    print("创建用户配置")
    return {}
    
# 仅开启软件时执行
configs = load_configs() 

# 下载视频
def download_video(event=None):
    global configs
    configs = config()

    video_link = link_entry.get()
    if video_link == "":
        messagebox.showinfo("提示", "请输入视频链接")
        return
    save_folder = configs['save_folder']  
    video_quality = configs['video_quality']
    audio_quality = configs['audio_quality']   
    video_format = configs['video_format']
    audio_format = configs['audio_format']
    browser_to_import_cookie = configs['browser_to_import_cookie']  
    only_download_audio = configs['only_download_audio']
    recode_video = configs['recode_video']
    recode_video_format = configs['recode_video_format']
    download_thumbnail = configs['download_thumbnail']
    import_cookies_from_browser = configs['import_cookies_from_browser']  
    download_all_playlist = configs['download_all_playlist']

    # 所有下载参数
    ytdl_opts = {
        'outtmpl': f"{save_folder}/%(title)s.%(ext)s",
        'format': f'bestvideo[height<={video_quality}][ext={video_format}]+bestaudio[ext={audio_format}]/best[height<={video_quality}][ext={video_format}]',
        'default_search': 'auto',
        'noplaylist': True,
        'postprocessors': [],
    }

    # 更新字幕参数
    ytdl_opts.update(subtitle_command())

    # 如果是bilibili的链接/导入cookie
    if is_bilibili_url(video_link) or import_cookies_from_browser:
        ytdl_opts["cookiesfrombrowser"] = (browser_to_import_cookie, None, None, None) # 从浏览器导入cookie

    if download_thumbnail:
        ytdl_opts['writethumbnail'] = True  # 是否下载视频缩略图
        ytdl_opts['postprocessors'].append({
            'key': 'FFmpegThumbnailsConvertor',
            'format': 'jpg',
        })

    # 如果想重新编码视频
    if recode_video:
        ytdl_opts['postprocessors'].append({
            'key': 'FFmpegVideoConvertor',
            'preferedformat': recode_video_format # 设置重新编码的格式
        })

    # 如果只想下载音频
    if only_download_audio:
        ytdl_opts['format'] = f"{audio_format}/bestaudio/best"
        ytdl_opts['postprocessors'].append({
            'key': 'FFmpegExtractAudio',
            'preferredcodec': audio_format,
            'preferredquality': audio_quality
        })

    # 如果下载整个播放列表
    if download_all_playlist:
        ytdl_opts['noplaylist'] = False

    for key, value in ytdl_opts.items():
        print(f'{key}: {value}')


    def errmsg_format(e):
        return str(e).replace('\x1b[0;31mERROR:\x1b[0m', '')
    try:
        root.title(title + "  下载中……") # 显示下载状态

        with yt_dlp.YoutubeDL(ytdl_opts) as ytdl:
            ytdl.download([video_link])
        
        if messagebox.askyesno("成功", "下载完成!\n"
                            "是否要打开文件夹?"):
            abs_folder = os.path.abspath(save_folder)
            if not os.path.exists(abs_folder):
                os.makedirs(abs_folder)
            os.startfile(abs_folder)

    except yt_dlp.utils.ContentTooShortError as e: 
        messagebox.showerror("失败", f'内容太短错误: {errmsg_format(e)}')
    except yt_dlp.utils.DownloadError as e:
        messagebox.showerror("失败", f'下载错误: {errmsg_format(e)}')
    except yt_dlp.utils.EntryNotInPlaylist as e: 
        messagebox.showerror("失败", f'播放列表中无此条目错误: {errmsg_format(e)}')
    except yt_dlp.utils.ExistingVideoReached as e: 
        messagebox.showerror("失败", f'已达到现有视频数目上限错误: {errmsg_format(e)}')
    except yt_dlp.utils.GeoRestrictedError as e: 
        messagebox.showerror("失败", f'地理位置受限错误: {errmsg_format(e)}')
    except yt_dlp.utils.ExtractorError as e: 
        messagebox.showerror("失败", f'提取器错误: {errmsg_format(e)}')
    except yt_dlp.utils.MaxDownloadsReached: 
        messagebox.showerror("失败", "已达最大下载数")
    except yt_dlp.utils.PostProcessingError as e: 
        messagebox.showerror("失败", f'后处理错误: {errmsg_format(e)}')
    except yt_dlp.utils.SameFileError as e: 
        messagebox.showerror("失败", f'相同文件错误: {errmsg_format(e)}')
    except yt_dlp.utils.UnavailableVideoError as e: 
        messagebox.showerror("失败", f'视频不可用: {errmsg_format(e)}')
    except Exception as e: 
        messagebox.showerror("失败", errmsg_format(e))
    root.title(title)

# 字幕参数设置
def subtitle_command():
    global configs
    configs = config()

    subtitle_setting = configs['subtitle_setting']  
    subtitle_format = configs['subtitle_format']  
    subtitle_langs = configs['subtitle_langs']
    needs_translation = configs['needs_translation']
    subtitle_trans_dest_lang = configs['subtitle_trans_dest_lang']  
    embed_sub = configs['embed_sub']
    download_all_subs = configs['download_all_subs'] 

    sub_options = {
        'writesubtitles': True if subtitle_setting != 2 else False,
        'writeautomaticsub': True if needs_translation and subtitle_setting != 2 else False,
        'subtitleslangs': [],
        'subtitlesformat': subtitle_format,
        'embedsubtitles': embed_sub,
        'skip_download': True if subtitle_setting == 0 else False,
        'postprocessors': [{
            'key': 'FFmpegSubtitlesConvertor',
            'format': subtitle_format,
        }]
    }

    def concatenate_strings(subtitle_trans_dest_lang, subtitle_langs):
        result = subtitle_trans_dest_lang if subtitle_trans_dest_lang != '' else subtitle_langs
        if subtitle_trans_dest_lang != '' and subtitle_langs != '':
            result += '-' + subtitle_langs
        return result

    if download_all_subs:
        sub_options['subtitleslangs'].append('all')
    else:
        sub_options['subtitleslangs'].append(concatenate_strings(subtitle_trans_dest_lang,subtitle_langs))

    if embed_sub:
        sub_options['postprocessors'].append({
            'key': 'FFmpegEmbedSubtitle',
            'already_have_subtitle': True,
        })
        
    return sub_options

# 判断是否为YouTube链接
def is_youtube_url(video_link):
    pattern = r"(?:https?:\/\/)?(?:www\.)?youtu(?:be\.com\/watch\?v=|\.be\/)([\w\-_]+)(&\S+)?"
    match = re.search(pattern, video_link)
    return match is not None

# 判断是否为b站网址
def is_bilibili_url(video_link):
    pattern = r'(https?://)?(www\.)?(bilibili\.com|b23\.tv)'
    match = re.search(pattern, video_link)
    return match is not None

# 判断其他视频网址(部分)
def is_video_url(url):
    video_websites = ['douyin', 'iqiyi', 'ixigua', 'youku', 'acfun', 'qq', 'pptv', 'cctv', 'sohu', 'ximalaya', 
                      'instagram', 'tiktok', 'twitter', 'facebook', 'vimeo']
    pattern = r'(https?://)?' + \
                r'(www\.|v\.|tv\.|video\.)?(' + '|'.join(video_websites) + r')\.(com|cn|clip|tv)'
    match = re.search(pattern, url)
    return match is not None

# 创建主窗口
root = tk.Tk()
root.withdraw()  # 隐藏窗口

last_edit_date = datetime.datetime.now().strftime("%Y/%#m/%#d")
title = " - ".join(["视频下载器(yt-dlp GUI)", VERSION, last_edit_date])
root.title(title)

# 设置窗口尺寸
root.geometry("600x350")
root.resizable(width=False, height=False)

# 窗口部件参数初始化
def init_vars():
    folder_entry.delete(0, tk.END)
    folder_entry.insert(tk.END, configs['save_folder'] if 'save_folder' in configs else os.path.join(os.path.abspath("./"), 'videos').replace("\\", "/"))
    selected_subtitle_setting.set(configs['subtitle_setting'] if 'subtitle_setting' in configs else 2)
    subtitle_format_var.set(configs['subtitle_format'] if 'subtitle_format' in configs else "srt")
    subtitle_langs_var.set(configs['subtitle_langs'] if 'subtitle_langs' in configs else "zh-CN")
    embed_sub_checkbox_var.set(configs['embed_sub'] if 'embed_sub' in configs else False)
    needs_translation_checkbox_var.set(configs['needs_translation'] if 'needs_translation' in configs else False)
    translation_dest_lang.set(configs['subtitle_trans_dest_lang'] if 'subtitle_trans_dest_lang' in configs else "en")
    all_subtitles_checkbox_var.set(configs['download_all_subs'] if 'download_all_subs' in configs else False)
    selected_video_quality.set(configs['video_quality'] if 'video_quality' in configs else "720")
    selected_video_format.set(configs['video_format'] if 'video_format' in configs else "mp4")
    selected_audio_quality.set(configs['audio_quality'] if 'audio_quality' in configs else '0')
    selected_audio_format.set(configs['audio_format'] if 'audio_format' in configs else "m4a")
    selected_browser.set(configs['browser_to_import_cookie'] if 'browser_to_import_cookie' in configs else "chrome")
    recode_video_var.set(configs['recode_video'] if 'recode_video' in configs else False)
    selected_recode_video.set(configs['recode_video_format'] if 'recode_video_format' in configs else "mp4")
    only_download_audio_var.set(configs['only_download_audio'] if 'only_download_audio' in configs else False)
    import_cookies_from_browser_var.set(configs['import_cookies_from_browser'] if 'import_cookies_from_browser' in configs else False)
    download_all_playlist_var.set(configs['download_all_playlist'] if 'download_all_playlist' in configs else False)
    download_thumbnail_var.set(configs['download_thumbnail'] if 'download_thumbnail' in configs else False)

# 创建主题样式
style = ThemedStyle(root)
style.set_theme("arc")

menuBar = Menu(root)

# 添加恢复默认值菜单
def set_default():
    global configs
    configs = {}
    init_vars()
    with open(CONFIG_YML, 'w') as f:
        yaml.dump(configs, f)
menuBar.add_command(label='恢复默认值', command=set_default)

# 添加帮助菜单
menuHelp = Menu(root, tearoff=False)
menuBar.add_cascade(label='帮助', menu=menuHelp)

# 弹出菜单内建立3个指令列表
menuHelp.add_command(label='帮助文档', command=lambda: help())
menuHelp.add_command(label='查看许可证', command=lambda: showLicense())
menuHelp.add_separator()
menuHelp.add_command(label='关于', command=lambda: showInfo())

root.config(menu=menuBar)

def help():
    webbrowser.open_new_tab("https://github.com/Guojingxing/yt-dlp-simple-gui#readme")

def showLicense():
    webbrowser.open_new_tab("https://github.com/Guojingxing/yt-dlp-simple-gui/blob/main/LICENSE")

def showInfo():
    about_dialog = tk.Toplevel(root)
    about_dialog.title("关于")
    about_dialog.geometry(f"350x50+{root.winfo_x() + 50}+{root.winfo_y() + 50}")
    about_dialog.grab_set()  # 设置为模态窗口
    about_dialog.resizable(False, False)  # 禁止调整大小和最大化
    about_dialog.focus_set()  # 将焦点转移到 about_dialog 窗口

    # 设置行和列的权重
    for i in range(2):
        about_dialog.rowconfigure(i, weight=1)
    for i in range(2):
        about_dialog.columnconfigure(i, weight=1)

    label_1 = tk.Label(about_dialog, text="作者:")
    label_1.grid(row=0, column=0, sticky="e")
    label_2 = tk.Label(about_dialog, text="GitHub:")
    label_2.grid(row=1, column=0, sticky="e")
    author_label = tk.Label(about_dialog, text="Guo Jingxing")
    author_label.grid(row=0, column=1, sticky="w")
    link_label = tk.Label(about_dialog, text="https://github.com/Guojingxing/yt-dlp-simple-gui",
                          fg="blue", cursor="hand2")
    link_label.grid(row=1, column=1, sticky="w")

    def open_link(event):
        webbrowser.open_new("https://github.com/Guojingxing/yt-dlp-simple-gui")

    link_label.bind("<Button-1>", open_link) 

# 设置行和列的权重
for i in range(5):
    root.rowconfigure(i, weight=1)
for i in range(3):
    root.columnconfigure(i, weight=1)

def handle_text(operation):
    try:
        selected_widget = root.focus_get()
        if operation == 'cut':
            selected_widget.clipboard_clear()
            selected_widget.clipboard_append(selected_widget.selection_get())
            selected_widget.delete(tk.SEL_FIRST, tk.SEL_LAST)
        elif operation == 'copy':
            selected_widget.clipboard_clear()
            selected_widget.clipboard_append(selected_widget.selection_get())
        elif operation == 'paste':
            selected_widget.insert(tk.INSERT, selected_widget.clipboard_get())
    except:
        return

supported_context_widgets = (tk.Entry, ttk.Combobox) # 支持文本的窗口部件
def show_context_menu(event):
    selected_widget = event.widget
    if isinstance(selected_widget, supported_context_widgets):
        if 'state' in selected_widget.keys() and 'readonly' == str(selected_widget.cget("state")):
            return
        context_menu.post(event.x_root, event.y_root) # 弹出菜单

# 创建复制、粘贴菜单
context_menu = Menu(root, tearoff=0)
context_menu.add_command(label="剪切", command=lambda:handle_text('cut'))
context_menu.add_command(label="复制", command=lambda:handle_text('copy'))
context_menu.add_command(label="粘贴", command=lambda:handle_text('paste'))
root.bind("<Button-3>", lambda e: show_context_menu(e)) # 绑定右键菜单

# 第一行 创建保存文件夹和浏览器选项
folder_label = tk.Label(root, text="保存文件夹")
folder_label.grid(row=0, column=0, sticky="e")

folder_entry = tk.Entry(root, width=50)
folder_entry.grid(row=0, column=1, columnspan=1, padx=10, pady=5, sticky="we")

def select_folder():
    folder_path = filedialog.askdirectory()
    if folder_path: # 如果选择了文件夹
        folder_entry.delete(0, tk.END) 
        folder_entry.insert(tk.END, folder_path)
        with open(CONFIG_YML, 'w') as f: # 更新本地配置
            yaml.dump(config(), f)

folder_button = tk.Button(root, text="选择文件夹", command=select_folder) 
folder_button.grid(row=0, column=2, padx=10, pady=5, sticky="we")

folder_entry.grid_rowconfigure(0, weight=1)
folder_entry.grid_columnconfigure(0, weight=1)

# 第二行 创建字幕设置
subtitle_label = tk.Label(root, text="字幕选项")
subtitle_label.grid(row=1, column=0, sticky="e")

## 创建一个变量来存储字幕下载设置
selected_subtitle_setting = tk.IntVar()

## 创建单选框
subtitle_setting_frame = tk.Frame(root) # 字幕设置框架头
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
subtitle_format_list = ("best", "srt", "sub", "ssa", "smi", "vtt", "sub", "ass", "txt", "psb", "txt", "ttml", "srv3", "srv2", "srv1", "json3")
subtitle_format_menu = ttk.Combobox(subtitle_setting_frame, values=subtitle_format_list, textvariable=subtitle_format_var, width=10)
subtitle_format_menu.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

sub_format_langs_label = tk.Label(subtitle_setting_frame, text="语言")
sub_format_langs_label.grid(row=1, column=2, sticky="e")

subtitle_langs_var = tk.StringVar()
subtitle_langs_menu = ttk.Combobox(subtitle_setting_frame, values=SUB_LANGS, textvariable=subtitle_langs_var, width=10)
subtitle_langs_menu.grid(row=1, column=3, padx=10, pady=5, sticky="we")

# 是否内嵌字幕？
embed_sub_checkbox_var = tk.BooleanVar()
embed_sub_checkbox = tk.Checkbutton(subtitle_setting_frame, text="内嵌字幕(仅mp4,webm,mkv)", variable=embed_sub_checkbox_var)
embed_sub_checkbox.grid(row=2, column=0, columnspan=2, sticky="e")

# 是否需要字幕翻译？
needs_translation_checkbox_var = tk.BooleanVar()
needs_translation_checkbox = tk.Checkbutton(subtitle_setting_frame, text="翻译为", variable=needs_translation_checkbox_var)
needs_translation_checkbox.grid(row=2, column=2, sticky="we")

# 翻译语言选择
translation_dest_lang = tk.StringVar()
translation_dest_lang_menu = ttk.Combobox(subtitle_setting_frame, values=TRANS_DEST_LANGS, textvariable=translation_dest_lang, width=10)
translation_dest_lang_menu.grid(row=2, column=3, columnspan=1, padx=10, pady=5, sticky="we")

# 分割线
separator = ttk.Separator(subtitle_setting_frame, orient='horizontal')
separator.grid(row=3, column=0, columnspan=4, padx=10, pady=10, sticky="we")

subtitle_setting_frame.grid(row=1, column=1, sticky="we") # 字幕设置框架尾

# 是否需要字幕全部下载？
all_subtitles_checkbox_var = tk.BooleanVar()
all_subtitles_checkbox = tk.Checkbutton(root, text="下载全部字幕", variable=all_subtitles_checkbox_var)
all_subtitles_checkbox.grid(row=1, column=2, sticky="w")


# 第三行 创建视频设置
video_label = tk.Label(root, text="视频设置")
video_label.grid(row=2, column=0, sticky="e")

video_setting_frame = tk.Frame(root) # 视频设置框架头
for i in range(4):
    video_setting_frame.columnconfigure(i, weight=1)

## 创建视频画质菜单
video_quality_label = tk.Label(video_setting_frame, text="视频画质")
video_quality_label.grid(row=0, column=0, sticky="e")

selected_video_quality = tk.StringVar()
video_quality_list = ("144", "240", "360", "480", "720", "1080", "1440", "2160", "4320")
quality_menu = ttk.Combobox(video_setting_frame, values=video_quality_list, textvariable=selected_video_quality, width=10)
quality_menu.grid(row=0, column=1, columnspan=1, padx=10, pady=5, sticky="we")

## 创建视频格式菜单
video_format_label = tk.Label(video_setting_frame, text="视频格式")
video_format_label.grid(row=0, column=2, sticky="e")

selected_video_format = tk.StringVar()
video_format_list = ("avi", "flv", "mkv", "mov", "mp4", "webm")
video_format_menu = ttk.Combobox(video_setting_frame, values=video_format_list, textvariable=selected_video_format, width=10)
video_format_menu.grid(row=0, column=3, columnspan=1, padx=10, pady=5, sticky="we")

## 创建音质菜单
audio_quality_label = tk.Label(video_setting_frame, text="音质(0为最佳)")
audio_quality_label.grid(row=1, column=0, sticky="e")

selected_audio_quality = tk.StringVar()
audio_quality_list = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10')
quality_menu = ttk.Combobox(video_setting_frame, values=audio_quality_list, textvariable=selected_audio_quality, width=10)
quality_menu.grid(row=1, column=1, columnspan=1, padx=10, pady=5, sticky="we")

## 创建音频格式菜单
audio_format_label = tk.Label(video_setting_frame, text="音频格式")
audio_format_label.grid(row=1, column=2, sticky="e")

selected_audio_format = tk.StringVar()
audio_format_list = ("best", "aac", "alac", "flac", "m4a", "mp3", "opus", "vorbis", "wav")
audio_format_menu = ttk.Combobox(video_setting_frame, values=audio_format_list, textvariable=selected_audio_format, width=10)
audio_format_menu.grid(row=1, column=3, columnspan=1, padx=10, pady=5, sticky="we")

browser_label = tk.Label(video_setting_frame, text="登陆的浏览器")
browser_label.grid(row=2, column=0, sticky="e")

selected_browser = tk.StringVar()
browser_list = ("brave", "chrome", "chromium", "edge", "firefox", "opera", "safari", "vivaldi")
browser_menu = ttk.Combobox(video_setting_frame, state="readonly", values=browser_list, textvariable=selected_browser, width=10)
browser_menu.grid(row=2, column=1, columnspan=1, padx=10, pady=5, sticky="we")

# 是否视频转码？
recode_video_var = tk.BooleanVar()
recode_video_checkbox = tk.Checkbutton(video_setting_frame, text="格式转换", variable=recode_video_var)
recode_video_checkbox.grid(row=2, column=2, sticky="e")

selected_recode_video = tk.StringVar()
recode_video_list = ("avi", "flv", "gif", "mkv", "mov", "mp4", "webm", "aac", "aiff", "alac", "flac", "m4a", "mka", "mp3", "ogg", "opus", "vorbis", "wav")
recode_video_menu = ttk.Combobox(video_setting_frame, values=recode_video_list, state="readonly", textvariable=selected_recode_video, width=10)
recode_video_menu.grid(row=2, column=3, columnspan=1, padx=10, pady=5, sticky="we")

video_setting_frame.grid(row=2, column=1, sticky="we") # 视频设置框架尾

video_setting_sidebar_frame = tk.Frame(root)
# 是否仅下载音频？
only_download_audio_var = tk.BooleanVar()
only_download_audio_checkbox = tk.Checkbutton(video_setting_sidebar_frame, text="仅下载音频", variable=only_download_audio_var)
only_download_audio_checkbox.grid(row=0, column=0, sticky="w")

# 是否从浏览器导入cookie？
import_cookies_from_browser_var = tk.BooleanVar()
import_cookies_from_browser_checkbox = tk.Checkbutton(video_setting_sidebar_frame, text="导入Cookies", variable=import_cookies_from_browser_var)
import_cookies_from_browser_checkbox.grid(row=1, column=0, sticky="w")

# 是否下载整个播放列表（该链接同时为视频和播放列表）？
download_all_playlist_var = tk.BooleanVar()
download_all_playlist_checkbox = tk.Checkbutton(video_setting_sidebar_frame, text="下载整个列表", variable=download_all_playlist_var)
download_all_playlist_checkbox.grid(row=2, column=0, sticky="w")

video_setting_sidebar_frame.grid(row=2, column=2, sticky="ew")


# 第四行 创建视频链接输入框
link_label = tk.Label(root, text="视频链接")
link_label.grid(row=3, column=0, sticky="e")

link_entry = tk.Entry(root, width=50)
link_entry.grid(row=3, column=1, columnspan=1, padx=10, pady=5, sticky="we")
root.after(0, lambda: link_entry.focus_set()) # 设置窗口打开时光标位于 entry 中

# 自动侦听是否为链接
last_clipboard_text = ""
def paste_to_link_entry(event):
    if event.widget != root:
        return
    global last_clipboard_text
    try:
        clipboard_text = root.clipboard_get(type='STRING')
        if clipboard_text != last_clipboard_text:
            last_clipboard_text = clipboard_text
            match = re.search(r'https?://\S+', clipboard_text)
            if match:
                url = clipboard_text
                if is_youtube_url(url) or is_bilibili_url(url) or is_video_url(url):
                    link_entry.delete(0, tk.END)
                    link_entry.insert(tk.END, url)
    except: pass
root.bind("<FocusIn>", paste_to_link_entry)

link_entry.grid_rowconfigure(0, weight=1)
link_entry.grid_columnconfigure(0, weight=1)

# 是否下载缩略图？
download_thumbnail_var = tk.BooleanVar()
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
root.bind("<Return>", download_video) # 键盘回车键也可开始下载

# 初始化所有参数
init_vars()

##############
# 配置相关代码，所有的窗口部件代码在该部分上方添加
def config(): # 获取部件参数,写至字典里返回
    config_rules = { # 配置规则,从相应部件获取参数,定义部件参数后在此处添加
        'save_folder' : os.path.normpath(folder_entry.get()).replace("\\", "/"),  
        'video_quality' : selected_video_quality.get(),
        'audio_quality' : selected_audio_quality.get(),
        'video_format' : selected_video_format.get(),
        'audio_format' : selected_audio_format.get(),
        'browser_to_import_cookie' : selected_browser.get(),
        'only_download_audio' : only_download_audio_var.get(),  
        'recode_video' : recode_video_var.get(),
        'recode_video_format' : selected_recode_video.get(),  
        'download_thumbnail' : download_thumbnail_var.get(),
        'import_cookies_from_browser' : import_cookies_from_browser_var.get(),
        'download_all_playlist' : download_all_playlist_var.get(),

        'subtitle_setting' : selected_subtitle_setting.get(),  
        'subtitle_format' : subtitle_format_var.get(),
        'subtitle_langs' : subtitle_langs_var.get(),
        'needs_translation' : needs_translation_checkbox_var.get(),
        'subtitle_trans_dest_lang' : translation_dest_lang.get(),  
        'embed_sub' : embed_sub_checkbox_var.get(),
        'download_all_subs' : all_subtitles_checkbox_var.get(),  
    }
    return config_rules

# 需要实时更新配置的窗口部件
update_widgets = (tk.Entry, ttk.Combobox) # 输入框
update_button_widgets = (tk.Checkbutton, tk.Radiobutton) # 按钮
# 实时将软件配置写入文件保存
def update_configs(event, widgets):
    selected_widget = event.widget
    if isinstance(selected_widget, widgets):
        with open(CONFIG_YML, 'w') as f:
            yaml.dump(config(), f)  

# 每次修改完参数,立即保存至本地
root.bind("<FocusOut>", lambda e:update_configs(e, update_widgets))
root.bind("<ButtonRelease>", lambda e:update_configs(e, update_button_widgets))
#############

root.deiconify()
print("主界面加载完成")
# 运行主循环
root.mainloop()