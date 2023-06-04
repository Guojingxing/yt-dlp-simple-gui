import re
import os
import sys
import shutil

import yt_dlp
import yaml

# 开发 - 导入所有包
#from PyQt5.QtWidgets import *
# 编译 - 导入部分包
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QPushButton, QRadioButton,\
QComboBox, QFileDialog, QApplication, QCheckBox, QShortcut, QMessageBox, QAction, \
    QDialog, QLabel, QActionGroup, QProgressBar
from PyQt5.QtCore import QThread, pyqtSignal, QUrl, Qt, QTranslator, QLocale, QLibraryInfo
from PyQt5.QtGui import QIcon, QDesktopServices, QFont, QKeySequence
from PyQt5 import uic
from constants import *
from ui import Ui_MainWindow

current_folder = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_folder)

class MainWindow(QMainWindow):
    folderSelected = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        #self.ui = uic.loadUi(UI, self) # 开发用
        self.ui = Ui_MainWindow()  # 创建 UI 对象
        self.ui.setupUi(self) 

        self.title = ' - '.join([TITLE, VERSION, LAST_EDIT_DATE])
        self.icon = QIcon("download_icon.ico")

        # 设置窗口
        self.setWindowTitle(self.title)
        self.setWindowIcon(self.icon)
        self.setFixedSize(624, 436)
        self.setWindowFlag(Qt.WindowMinimizeButtonHint) # 禁用最大化
        
        self.configs = self.load_configs()
        self.status_bar = self.statusBar()

        # 获取当前地理位置的语言代码
        locale = QLocale.system().name()
        self.lang_code = self.configs['lang_code'] if 'lang_code' in self.configs else locale
        self.texts = TRANSLATE[self.lang_code]

        # 根据地理位置的语言代码加载相应的翻译文件
        translator = QTranslator()
        translator.load(f'./translations/{locale}')
        app.installTranslator(translator)

        # 设置应用程序的语言环境，如复制粘贴菜单、QMessagebox的按钮语言等
        source_path = './translations/qtbase_zh_CN.qm'
        target_folder = QLibraryInfo.location(QLibraryInfo.TranslationsPath)
        if not os.path.exists(os.path.join(target_folder, 'qtbase_zh_CN.qm')):
            shutil.copy2(source_path, target_folder) # 导入简体中文包

        app_translator = QTranslator(app)
        app_translator.load(QLibraryInfo.location(QLibraryInfo.TranslationsPath) + f'/qtbase_{locale}.qm')
        app.installTranslator(app_translator)

        # 配置菜单
        self.addActions(self.findChildren(QAction))
        self.my_actions = [action for action in self.actions() if action.objectName().startswith('action')]
        for action in self.my_actions:
            action.triggered.connect(self.runAction)

        # 语言菜单一次只能选择一项
        self.lang_action_group = QActionGroup(self)
        self.lang_action_group.setExclusive(True)  # 设置动作组为互斥模式
        self.lang_action_group.addAction(self.findChild(QAction, 'actionSimplifiedChinese'))
        self.lang_action_group.addAction(self.findChild(QAction, 'actionTraditionalChinese'))
        self.lang_action_group.addAction(self.findChild(QAction, 'actionEnglish'))

        # 配置底部status bar
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setFixedSize(200, 15)
        self.status_bar.addWidget(self.progress_bar) # 添加进度条
        self.progress_bar.hide()
        self.progress_bar.setValue(0)

        self.downloaded_label = QLabel(self)
        self.status_bar.addPermanentWidget(self.downloaded_label)

        self.total_label = QLabel(self)
        self.status_bar.addPermanentWidget(self.total_label)

        #self.total_bytes_estimate_label = QLabel(self)
        #self.status_bar.addPermanentWidget(self.total_bytes_estimate_label)

        #self.elapsed_label = QLabel(self)
        #self.status_bar.addPermanentWidget(self.elapsed_label)

        #self.eta_label = QLabel(self)
        #self.status_bar.addPermanentWidget(self.eta_label)

        self.speed_label = QLabel(self)
        self.status_bar.addPermanentWidget(self.speed_label)
       
        # 配置文件夹widgets
        self.folder_edit = self.findChild(QLineEdit, "folder_edit")
        path = os.path.join(os.path.abspath("./"), 'videos').replace("\\", "/")
        self.folder_edit.setText(path)
        self.save_folder = self.folder_edit.text()

        self.folder_button = self.findChild(QPushButton, "folder_button")
        self.folder_button.clicked.connect(self.selectFolder)
        self.folder_edit.textChanged.connect(self.updateFolderEdit)

        # 是否下载字幕/视频(radiobutton)
        self.only_sub_radio_button = self.findChild(QRadioButton,"only_sub_radio_button")
        self.sub_and_video_radio_button = self.findChild(QRadioButton, "sub_and_video_radio_button")
        self.only_video_radio_button = self.findChild(QRadioButton,"only_video_radio_button")

        # 选择：仅下载视频
        self.subtitle_setting = 2

        # 将radiobutton绑定subtitle setting
        self.only_sub_radio_button.toggled.connect(lambda: self.on_subtitle_setting_changed(self.only_sub_radio_button)) 
        self.sub_and_video_radio_button.toggled.connect(lambda: self.on_subtitle_setting_changed(self.sub_and_video_radio_button))
        self.only_video_radio_button.toggled.connect(lambda: self.on_subtitle_setting_changed(self.only_video_radio_button))

        # 字幕格式/语言等下拉菜单(Combobox)
        self.subtitle_format_menu = self.findChild(QComboBox, "subtitle_format_menu")
        self.subtitle_format_menu.addItems(SUBTITLE_FORMAT_LIST)
        self.subtitle_format_menu.setCurrentText("srt")

        self.subtitle_langs_menu = self.findChild(QComboBox, "subtitle_langs_menu")
        self.subtitle_langs_menu.addItems(SUB_LANGS)
        self.subtitle_langs_menu.setCurrentText("zh-CN")
        
        self.translation_dest_lang_menu = self.findChild(QComboBox, "translation_dest_lang_menu")
        self.translation_dest_lang_menu.addItems(TRANS_DEST_LANGS)
        self.translation_dest_lang_menu.setCurrentText("en")

        # 视频设置: 下拉菜单设置(Combobox)
        self.video_quality_menu = self.findChild(QComboBox, "video_quality_menu")
        self.video_quality_menu.addItems(VIDEO_QUALITY_LIST)
        self.video_quality_menu.setCurrentText("720")
        
        self.video_format_menu = self.findChild(QComboBox, "video_format_menu")
        self.video_format_menu.addItems(VIDEO_FORMAT_LIST)

        self.audio_quality_menu = self.findChild(QComboBox, "audio_quality_menu")
        self.audio_quality_menu.addItems(AUDIO_QUALITY_LIST)
        self.audio_quality_menu.setCurrentText('0')   

        self.audio_format_menu = self.findChild(QComboBox, "audio_format_menu")
        self.audio_format_menu.addItems(AUDIO_FORMAT_LIST)
        self.audio_format_menu.setCurrentText("m4a")

        self.browser_menu = self.findChild(QComboBox, "browser_menu")
        self.browser_menu.addItems(BROWSER_LIST)
        self.browser_menu.setCurrentText("chrome")

        self.recode_video_menu = self.findChild(QComboBox, "recode_video_menu") 
        self.recode_video_menu.addItems(RECODE_VIDEO_LIST)
        self.recode_video_menu.setCurrentText("mp4")

        # 所有ComboBox绑定槽函数
        self.comboboxes = self.findChildren(QComboBox)
        [setattr(self, COMBOBOX_PARAMETER[combobox.objectName()], combobox.currentText()) for combobox in self.comboboxes]
        [combobox.currentTextChanged.connect(self.updateParameter) for combobox in self.comboboxes]       

        # 视频链接框
        self.link_edit = self.findChild(QLineEdit, "link_edit")
        self.link_edit.setFocus()
        self.paste_if_link_copied()
        QApplication.clipboard().dataChanged.connect(self.paste_if_link_copied)

        # 所有checkbox
        self.needs_translation_checkbox = self.findChild(QCheckBox, "needs_translation_checkbox") 
        self.embed_sub_checkbox = self.findChild(QCheckBox, "embed_sub_checkbox")  
        self.live_chat_subs_checkbox = self.findChild(QCheckBox, "live_chat_subs_checkbox")  
        self.all_subtitles_checkbox = self.findChild(QCheckBox, "all_subtitles_checkbox")  
        self.recode_video_checkbox = self.findChild(QCheckBox, "recode_video_checkbox")    
        self.import_cookies_from_browser_checkbox = self.findChild(QCheckBox, "import_cookies_from_browser_checkbox")  
        self.only_download_audio_checkbox = self.findChild(QCheckBox, "only_download_audio_checkbox")  
        self.download_all_playlist_checkbox = self.findChild(QCheckBox, "download_all_playlist_checkbox")   
        self.download_thumbnail_checkbox = self.findChild(QCheckBox, "download_thumbnail_checkbox")

        # 所有checkbox绑定槽函数
        self.checkboxes = self.findChildren(QCheckBox)
        [setattr(self, CHECKBOX_PARAMETER[checkbox.objectName()], False) for checkbox in self.checkboxes]
        [checkbox.stateChanged.connect(self.updateParameter) for checkbox in self.checkboxes]

        # 开始下载按钮
        self.download_button = self.findChild(QPushButton, "download_button")
        self.download_button.clicked.connect(self.download_video)
        self.shortcut = QShortcut(QKeySequence(Qt.Key_Enter), self)
        self.shortcut.activated.connect(self.download_button.click)
        
        self.update_texts(self.lang_code)
        self.init_parameters()

    # 根据本地配置文件初始化所有widget的参数值
    def init_parameters(self):
        self.folder_edit.setText(self.configs['save_folder'] if 'save_folder' in self.configs else os.path.join(os.path.abspath("./"), 'videos').replace("\\", "/"))
        
        self.subtitle_setting = self.configs['subtitle_setting'] if 'subtitle_setting' in self.configs else 2
        self.set_subtitle_setting_radio_button()

        self.switch_language(self.configs['lang_code'] if 'subtitle_setting' in self.configs else self.lang_code)
        for action in self.lang_action_group.actions():
            action.setChecked(LANG_ACTION[action.objectName()] == self.lang_code)

        for checkbox in self.checkboxes: # 加载本地所有checkbox的参数
            checkbox_param_name = CHECKBOX_PARAMETER[checkbox.objectName()]
            checkbox.setChecked(self.configs[checkbox_param_name] if checkbox_param_name in self.configs else False)
        for combobox in self.comboboxes: # 加载本地所有combobox的参数
            combobox_param_name = COMBOBOX_PARAMETER[combobox.objectName()] # 比如 "video_format_menu" 得到 "video_format"
            combobox.setCurrentText(self.configs[combobox_param_name] if combobox_param_name in self.configs else COMBOBOX_INITS[combobox_param_name])

    # 选择文件夹
    def selectFolder(self):
        folder_path = QFileDialog.getExistingDirectory(self, self.texts['choose_folder'])
        if folder_path:
            self.folder_edit.setText(folder_path)

    # 更新folder_edit框，并保存至本地
    def updateFolderEdit(self, folder_path):
        self.save_folder = folder_path
        self.update_configs()
    
    # 当radiobutton按下状态发生变化时
    def on_subtitle_setting_changed(self, radio_button): 
        if radio_button.isChecked():
            if radio_button == self.only_sub_radio_button:
                self.subtitle_setting = 0
            elif radio_button == self.sub_and_video_radio_button:
                self.subtitle_setting = 1
            else:
                self.subtitle_setting = 2
            self.update_configs()

    # 根据subtitle_setting的值更新radiobutton
    def set_subtitle_setting_radio_button(self):
        if self.subtitle_setting == 0:
            self.only_sub_radio_button.setChecked(True)
        elif self.subtitle_setting == 1:
            self.sub_and_video_radio_button.setChecked(True)
        else:
            self.only_video_radio_button.setChecked(True)

    # 更新widget对应的参数
    def updateParameter(self):
        widget = self.sender()
        widget_name = widget.objectName() # 获取该widget在ui文件中的objectName
        if isinstance(widget, QCheckBox):
            setattr(self, CHECKBOX_PARAMETER[widget_name], widget.isChecked())
        if isinstance(widget, QComboBox):
            setattr(self, COMBOBOX_PARAMETER[widget_name], widget.currentText())
        self.update_configs()
    
    # 如果复制了视频链接，就自动粘贴
    def paste_if_link_copied(self):
        try:
            clipboard_text = QApplication.clipboard().text()
            match = re.search(r'https?://\S+', clipboard_text)
            if match:
                url = clipboard_text
                if self.is_youtube_url(url) or self.is_bilibili_url(url) or self.is_video_url(url):
                    self.link_edit.setText(clipboard_text)
                    self.link_edit.selectAll() # 将文本全部选中
        except: pass

    # 判断是否为YouTube链接
    def is_youtube_url(self, video_link):
        pattern = r"(?:https?:\/\/)?(?:www\.)?youtu(?:be\.com\/watch\?v=|\.be\/|be\.com\/shorts\/)([\w\-_]+)(&\S+)?"
        match = re.search(pattern, video_link)
        return match is not None

    # 判断是否为b站网址
    def is_bilibili_url(self, video_link):
        pattern = r'(https?://)?(www\.)?(bilibili\.com|b23\.tv)'
        match = re.search(pattern, video_link)
        return match is not None

    # 判断其他视频网址(部分)
    def is_video_url(self, url):
        video_websites = ['douyin', 'iqiyi', 'ixigua', 'youku', 'acfun', 'qq', 'pptv', 'cctv', 'sohu', 'ximalaya', 
                        'instagram', 'tiktok', 'twitter', 'facebook', 'vimeo']
        pattern = r'(https?://)?' + \
                    r'(www\.|v\.|tv\.|video\.)?(' + '|'.join(video_websites) + r')\.(com|cn|clip|tv)'
        match = re.search(pattern, url)
        return match is not None

    def video_domain_keyword(self, url, *domain_keywords):
        domain_keyword_list = list(domain_keywords)
        pattern = r'(https?://)?' + \
                    r'(www\.|v\.|tv\.|video\.)?(' + '|'.join(domain_keyword_list) + r')\.(com|cn|clip|tv)'
        match = re.search(pattern, url)
        return match is not None
    
    # 下载视频（核心代码）
    def download_video(self):
        self.video_link = self.link_edit.text()
        if self.video_link == "":
            QMessageBox.information(self, self.texts['notice'], self.texts['please_enter_link'])
            return

        # 所有下载参数
        ytdl_opts = {
            'outtmpl': f"{self.save_folder}/%(title)s.%(ext)s",
            'format': f'bestvideo[height<={self.video_quality}][ext={self.video_format}]+bestaudio[ext={self.audio_format}]/best[height<={self.video_quality}][ext={self.video_format}]',
            'default_search': 'auto',
            'noplaylist': True,
            'postprocessors': [],
        }

        # 更新字幕参数
        ytdl_opts.update(self.subtitle_settings())

        # 如果是bilibili的链接/导入cookie
        if self.is_bilibili_url(self.video_link) or self.import_cookies_from_browser:
            ytdl_opts["cookiesfrombrowser"] = (self.browser_to_import_cookie, None, None, None) # 从浏览器导入cookie

        if self.download_thumbnail:
            ytdl_opts['writethumbnail'] = True  # 是否下载视频缩略图
            ytdl_opts['postprocessors'].append({
                'key': 'FFmpegThumbnailsConvertor',
                'format': 'jpg', # 此处设为jpg，也可修改为其他的
            })

        # 如果想重新编码视频
        if self.recode_video:
            ytdl_opts['postprocessors'].append({
                'key': 'FFmpegVideoConvertor',
                'preferedformat': self.recode_video_format # 设置重新编码的格式
            })

        # 如果只想下载音频
        if self.only_download_audio:
            ytdl_opts['format'] = f"{self.audio_format}/bestaudio/best"
            ytdl_opts['postprocessors'].append({
                'key': 'FFmpegExtractAudio',
                'preferredcodec': self.audio_format,
                'preferredquality': self.audio_quality
            })

        # 如果下载整个播放列表
        if self.download_all_playlist:
            ytdl_opts['noplaylist'] = False

        for key, value in ytdl_opts.items():
            print(f'{key}: {value}')

        self.download_button.setEnabled(False)  # 禁用窗口上的控件
        self.progress_bar.setValue(0) # 初始化进度条
        
        # 创建并启动后台线程，并传递参数
        self.download_thread = DownloadThread(self.video_link, ytdl_opts)
        self.download_thread.started.connect(self.progress_bar.show)
        self.download_thread.finished.connect(self.handleDownloadFinished)
        self.download_thread.errorOccurred.connect(self.handleDownloadError)
        self.download_thread.progress_updated.connect(self.update_progress)
        self.download_thread.start()

    # 根据下载情况更新进度条和状态栏
    def update_progress(self, downloaded_bytes, total_bytes, total_bytes_estimate, elapsed, eta, speed):
        self.progress_bar.setMaximum(total_bytes)
        self.progress_bar.setValue(downloaded_bytes)

        self.downloaded_label.setText(f"{self.texts['downloaded_label']}: {self.format_bytes(downloaded_bytes)}")
        self.total_label.setText(f"{self.texts['total_label']}: {self.format_bytes(total_bytes)}")
        #self.total_bytes_estimate_label.setText(f"{self.texts['total_bytes_estimate_label']}: {self.format_bytes(total_bytes_estimate)}")
        #self.elapsed_label.setText(f"{self.texts['elapsed_label']}: {self.format_time(elapsed)}")
        #self.eta_label.setText(f"{self.texts['eta_label']}: {self.format_speed(eta)}")
        self.speed_label.setText(f"{self.texts['speed_label']}: {self.format_speed(speed)}")
    
    def format_bytes(self, num_bytes):
        if num_bytes == -1:
            return self.texts['unknown']
        elif num_bytes < 1024:
            return f"{num_bytes} B"
        elif num_bytes < 1024**2:
            return f"{num_bytes / 1024:.2f} KB"
        elif num_bytes < 1024**3:
            return f"{num_bytes / (1024**2):.2f} MB"
        else:
            return f"{num_bytes / (1024**3):.2f} GB"

    def format_time(self, seconds):
        if seconds == -1:
            return self.texts['unknown']
        minutes, seconds = divmod(int(seconds), 60)
        hours, minutes = divmod(minutes, 60)
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    
    def format_speed(self, speed):
        if speed == -1:
            return self.texts['unknown']
        elif speed < 1024:
            return f"{speed} B/s"
        elif speed < 1024**2:
            return f"{speed / 1024:.2f} KB/s"
        elif speed < 1024**3:
            return f"{speed / (1024**2):.2f} MB/s"
        else:
            return f"{speed / (1024**3):.2f} GB/s"
    
    # 处理下载错误
    def handleDownloadError(self, e):
        #self.status_bar.showMessage(self.tr("下载失败"))

        def errmsg_format(e):
            return str(e).replace('\x1b[0;31mERROR:\x1b[0m', '')
        def dl_err(hint, e):
            QMessageBox.critical(self, self.texts['DownloadError'], f'{hint}: {errmsg_format(e)}')

        error_list = (
            yt_dlp.utils.ContentTooShortError,
            yt_dlp.utils.DownloadError,
            yt_dlp.utils.EntryNotInPlaylist,
            yt_dlp.utils.ExistingVideoReached,
            yt_dlp.utils.GeoRestrictedError,
            yt_dlp.utils.ExtractorError,
            yt_dlp.utils.MaxDownloadsReached,
            yt_dlp.utils.PostProcessingError,
            yt_dlp.utils.SameFileError,
            yt_dlp.utils.UnavailableVideoError
            )
        if isinstance(e, error_list):
            dl_err(self.texts[type(e).__name__], e)
        else:
            QMessageBox.critical(self, self.texts['error'], errmsg_format(e))
        
        self.download_button.setEnabled(True)  # 启用下载按钮

    # 字幕参数设置
    def subtitle_settings(self):
        sub_options = {
            'writesubtitles': True if self.subtitle_setting != 2 else False,
            'writeautomaticsub': True if self.needs_translation and self.subtitle_setting != 2 else False,
            'subtitleslangs': [],
            'subtitlesformat': self.subtitle_format,
            'embedsubtitles': self.embed_sub,
            'skip_download': True if self.subtitle_setting == 0 else False,
            'postprocessors': [{
                'key': 'FFmpegSubtitlesConvertor',
                'format': self.subtitle_format,
            }]
        }

        # 组合“语言”和“翻译语言”的字符串
        def concatenate_strings(subtitle_trans_dest_lang, subtitle_langs):
            result = ''
            if subtitle_langs == 'auto':
                subtitle_langs = r'^[a-z]{2,3}-orig$' # YouTube的自动字幕以'-orig'结尾
                sub_options['writeautomaticsub'] = True
                if self.needs_translation:
                    subtitle_langs = ''

            result = subtitle_trans_dest_lang if subtitle_trans_dest_lang != '' else subtitle_langs
            if subtitle_trans_dest_lang != '' and subtitle_langs != '':
                result += '-' + subtitle_langs

            if self.is_bilibili_url(self.video_link): # bilibili字幕
                if subtitle_langs == 'auto':
                    result = r'^ai-[a-z]{2,3}$'
                    sub_options['writeautomaticsub'] = True
                elif 'zh' in subtitle_langs:
                    result = r'^zh.*$'

            if not self.needs_translation:
                result = subtitle_langs
            return result

        if self.download_all_subs:
            sub_options['subtitleslangs'].append('all')
        else:
            sub_options['subtitleslangs'].append(concatenate_strings(self.subtitle_trans_dest_lang, self.subtitle_langs))

        if self.embed_sub:
            sub_options['postprocessors'].append({
                'key': 'FFmpegEmbedSubtitle',
                'already_have_subtitle': True,
            })
        
        if self.live_chat_subs:
            if self.is_bilibili_url(self.video_link) or self.video_domain_keyword(self.video_link, 'acfun', 'niconico'):
                sub_options['subtitleslangs'].append('danmaku')
            else:
                sub_options['subtitleslangs'].append('live_chat')
        else:
            sub_options['subtitleslangs'].append('-live_chat')
            
        return sub_options
    
    # 从文件中加载配置（若有）
    def load_configs(self):
        file_path = CONFIG_YML
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                all_configs = yaml.safe_load(f)
            if all_configs is not None:
                return all_configs
        # 处理文件不存在或为空的情况，返回空字典
        return {}
        
    # 获取部件参数,写至字典里返回
    def config(self): 
        config_rules = {} # 配置规则,从相应部件获取参数
        config_rules['save_folder'] = os.path.normpath(self.folder_edit.text()).replace("\\", "/")
        config_rules['subtitle_setting'] = self.subtitle_setting
        config_rules['lang_code'] = self.lang_code
        for combobox in self.comboboxes:
            config_rules[COMBOBOX_PARAMETER[combobox.objectName()]] = combobox.currentText()
        for checkbox in self.checkboxes:
            config_rules[CHECKBOX_PARAMETER[checkbox.objectName()]] = checkbox.isChecked()
        return config_rules
    
    # 实时将软件配置写入文件保存
    def update_configs(self):
        with open(CONFIG_YML, 'w') as f:
            yaml.dump(self.config(), f) 

    # 下载完成时的处理
    def handleDownloadFinished(self):
        self.progress_bar.setMaximum(100)
        self.progress_bar.setValue(100)
        self.downloaded_label.setText(f"{self.texts['downloaded_label']}: {self.format_bytes(self.download_thread.last_progress['downloaded_bytes'])}")
        self.total_label.setText(f"{self.texts['total_label']}: {self.format_bytes(self.download_thread.last_progress['total_bytes'])}")
        #self.total_bytes_estimate_label.setText(f"{self.texts['total_bytes_estimate_label']}: {self.format_bytes(self.download_thread.last_progress['total_bytes_estimate'])}")
        #self.elapsed_label.setText(f"{self.texts['elapsed_label']}: {self.format_time(self.download_thread.last_progress['elapsed'])}")
        #self.eta_label.setText(f"{self.texts['eta_label']}: {self.format_time(self.download_thread.last_progress['eta'])}")
        self.speed_label.setText(f"{self.texts['speed_label']}: {self.format_speed(self.download_thread.last_progress['speed'])}")

        if QMessageBox.Yes == QMessageBox.question(self, self.texts['success'], self.texts['open_folder?'], QMessageBox.Yes | QMessageBox.No):
            abs_folder = os.path.abspath(self.save_folder)
            if not os.path.exists(abs_folder):
                os.makedirs(abs_folder)
            os.startfile(abs_folder)

        #self.progress_bar.hide()
        self.download_button.setEnabled(True)  # 启用下载按钮
        
        self.sender().quit()
        self.sender().wait()

    # 所有的action在这里绑定
    def runAction(self):
        action_name = self.sender().objectName()
        if 'actionDefault' == action_name:
            self.configs = {}
            self.init_parameters()
            with open(CONFIG_YML, 'w') as f:
                yaml.dump(self.configs, f)
        elif 'actionHelp' == action_name:
            url = QUrl("https://github.com/Guojingxing/yt-dlp-simple-gui#readme")  # 替换为你要跳转的网站
            QDesktopServices.openUrl(url)
        elif 'actionShowLicense' == action_name:
            url = QUrl("https://github.com/Guojingxing/yt-dlp-simple-gui/blob/main/LICENSE")  # 替换为你要跳转的网站
            QDesktopServices.openUrl(url)
        elif 'actionAbout' == action_name:
            self.about_dialog = AboutDialog()
            self.about_dialog.exec_()
        elif 'actionViewLogs' == action_name:
            current_dir = os.getcwd()
            log_file_path = os.path.join(current_dir, "output.log")
            if not os.path.exists(log_file_path):
                open(log_file_path, "w").close()
            os.startfile(log_file_path)

        # 语言配置
        elif 'actionSimplifiedChinese' == action_name:
            self.switch_language('zh_CN')
        elif 'actionEnglish' == action_name:
            self.switch_language('en')
        elif 'actionTraditionalChinese' == action_name:
            self.switch_language('zh_TW')

    # 切换界面语言
    def switch_language(self, lang_code):
        self.lang_code = lang_code
        translator = QTranslator()
        if lang_code != 'zh_CN':  # 如果选择的语言不是中文简体，则加载对应的翻译文件
            translator.load(f'translations/{lang_code}')
            app.installTranslator(translator)
            title_trans = ""
            if lang_code == 'zh_TW' : title_trans = "影片下載助手(yt-dlp QtGUI)"
            elif lang_code == "en" : title_trans = "Video Downloader(yt-dlp QtGUI)"
            else : title_trans = TITLE
            self.title = [title_trans, VERSION, LAST_EDIT_DATE]
        else:
            app.removeTranslator(translator)
            self.title = [TITLE, VERSION, LAST_EDIT_DATE]
        
        font = getFont(lang_code)
        app.setFont(font)
        self.setFont(font)
        self.ui.retranslateUi(self)
        self.update_texts(lang_code)

        self.update_configs()
    
    # 该文件yt-dlp-simple-gui-qt.py的文本语言转换
    def update_texts(self, lang_code):
        self.texts = TRANSLATE[lang_code]
        self.downloaded_label.setText(f"{self.texts['downloaded_label']}: 0 B")
        self.total_label.setText(f"{self.texts['total_label']}: 0 B")
        #self.total_bytes_estimate_label.setText(f"{self.texts['total_bytes_estimate_label']}: 0 B")
        #self.elapsed_label.setText(f"{self.texts['elapsed_label']}: 00:00:00")
        #self.eta_label.setText(f"{self.texts['eta_label']}: {self.texts['unknown']}")
        self.speed_label.setText(f"{self.texts['speed_label']}: 0 B/s")

#根据语言选择字体
def getFont(lang_code):
    font = QFont()
    if lang_code == 'zh_CN':
        font.setFamily('Microsoft Yahei')
    elif lang_code == 'zh_TW':
        font.setFamily('Microsoft Jhenghei')
    elif lang_code == 'en':
        font.setFamily('Arial')
    return font

class DownloadThread(QThread):
    finished = pyqtSignal()  # 自定义信号，在任务完成时发出信号
    errorOccurred = pyqtSignal(Exception)
    progress_updated = pyqtSignal(int, int, int, float, int, float)

    def __init__(self, video_link, ytdl_opts):
        super().__init__()
        self.video_link = video_link
        self.ytdl_opts = ytdl_opts
        self.ytdl_opts['progress_hooks'] = [self.my_progress_hook]
        self.last_progress = {
                'downloaded_bytes': 0,      # 已下载的字节数
                'total_bytes': 0,           # 整个文件的大小，如果未知则为None
                'total_bytes_estimate': 0,  # 对最终文件大小的猜测，如果不可用则为None
                'elapsed': 0,               # 自下载开始以来的秒数
                'eta': 0,                   # 预计剩余时间（秒），如果未知则为None
                'speed': 0                  # 下载速度（字节/秒），如果未知则为None
            }

    def run(self):
        try:
        # 使用 self.parameters 中的参数执行耗时的任务
            with yt_dlp.YoutubeDL(self.ytdl_opts) as ytdl:
                ytdl.download([self.video_link])
        except Exception as e:
            self.errorOccurred.emit(e)
        else:
            self.finished.emit()  # 发出任务完成的信号

    def my_progress_hook(self, d):
        if d['status'] == 'downloading':
            total_bytes = d.get('total_bytes')
            downloaded_bytes = d.get('downloaded_bytes')
            total_bytes_estimate = d.get('total_bytes_estimate')
            elapsed = d.get('elapsed')
            eta = d.get('eta')
            speed = d.get('speed')

            self.progress_updated.emit(
                -1 if downloaded_bytes is None else downloaded_bytes,
                -1 if total_bytes is None else total_bytes,
                -1 if total_bytes_estimate is None else total_bytes_estimate,
                -1 if elapsed is None else elapsed,
                -1 if eta is None else eta,
                -1 if speed is None else speed
            )
            self.last_progress = {
                'downloaded_bytes': downloaded_bytes,
                'total_bytes': total_bytes,
                'total_bytes_estimate': total_bytes_estimate,
                'elapsed': elapsed,
                'eta': eta,
                'speed': speed
            }
        elif d['status'] == 'finished':
            self.progress_updated.emit(
                self.last_progress['downloaded_bytes'],
                self.last_progress['total_bytes'],
                self.last_progress['total_bytes_estimate'],
                self.last_progress['elapsed'],
                self.last_progress['eta'],
                self.last_progress['speed']
            )

class AboutDialog(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi(ABOUT_UI, self)

        self.github_label = self.findChild(QLabel, "github_label")
        self.github_label.setText("<a href='https://github.com/Guojingxing/yt-dlp-simple-gui'>https://github.com/Guojingxing/yt-dlp-simple-gui</a>")
        self.github_label.setOpenExternalLinks(True)
        self.github_label.setTextInteractionFlags(Qt.TextBrowserInteraction)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    # 将命令行的输出转移至output.log中，w为复写日志，a为追加日志
    # 若要在命令行中查看输出，注释掉此行
    sys.stdout = open('output.log', 'w')

    sys.exit(app.exec_())