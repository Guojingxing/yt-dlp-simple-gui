# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'yt-dlp-simple-gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(624, 436)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(20, -1, 20, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_4.setContentsMargins(10, 10, 10, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.folder_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.folder_edit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.folder_edit.setText("")
        self.folder_edit.setObjectName("folder_edit")
        self.horizontalLayout_4.addWidget(self.folder_edit)
        self.folder_button = QtWidgets.QPushButton(self.centralwidget)
        self.folder_button.setAutoDefault(False)
        self.folder_button.setDefault(False)
        self.folder_button.setFlat(False)
        self.folder_button.setObjectName("folder_button")
        self.horizontalLayout_4.addWidget(self.folder_button)
        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 5)
        self.horizontalLayout_4.setStretch(2, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setContentsMargins(9, -1, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(10, -1, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.only_sub_radio_button = QtWidgets.QRadioButton(self.groupBox)
        self.only_sub_radio_button.setMinimumSize(QtCore.QSize(130, 0))
        self.only_sub_radio_button.setMaximumSize(QtCore.QSize(200, 16777215))
        self.only_sub_radio_button.setAcceptDrops(False)
        self.only_sub_radio_button.setAutoFillBackground(False)
        self.only_sub_radio_button.setObjectName("only_sub_radio_button")
        self.horizontalLayout.addWidget(self.only_sub_radio_button)
        self.sub_and_video_radio_button = QtWidgets.QRadioButton(self.groupBox)
        self.sub_and_video_radio_button.setMinimumSize(QtCore.QSize(170, 0))
        self.sub_and_video_radio_button.setMaximumSize(QtCore.QSize(220, 16777215))
        self.sub_and_video_radio_button.setSizeIncrement(QtCore.QSize(0, 0))
        self.sub_and_video_radio_button.setObjectName("sub_and_video_radio_button")
        self.horizontalLayout.addWidget(self.sub_and_video_radio_button)
        self.only_video_radio_button = QtWidgets.QRadioButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.only_video_radio_button.sizePolicy().hasHeightForWidth())
        self.only_video_radio_button.setSizePolicy(sizePolicy)
        self.only_video_radio_button.setMinimumSize(QtCore.QSize(0, 0))
        self.only_video_radio_button.setMaximumSize(QtCore.QSize(200, 16777215))
        self.only_video_radio_button.setChecked(True)
        self.only_video_radio_button.setObjectName("only_video_radio_button")
        self.horizontalLayout.addWidget(self.only_video_radio_button)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 1)
        self.horizontalLayout.setStretch(3, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setMinimumSize(QtCore.QSize(50, 0))
        self.label_2.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.subtitle_format_menu = QtWidgets.QComboBox(self.groupBox)
        self.subtitle_format_menu.setEditable(True)
        self.subtitle_format_menu.setCurrentText("")
        self.subtitle_format_menu.setObjectName("subtitle_format_menu")
        self.horizontalLayout_2.addWidget(self.subtitle_format_menu)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setMaximumSize(QtCore.QSize(90, 16777215))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.subtitle_langs_menu = QtWidgets.QComboBox(self.groupBox)
        self.subtitle_langs_menu.setMinimumSize(QtCore.QSize(80, 0))
        self.subtitle_langs_menu.setEditable(True)
        self.subtitle_langs_menu.setObjectName("subtitle_langs_menu")
        self.horizontalLayout_2.addWidget(self.subtitle_langs_menu)
        self.needs_translation_checkbox = QtWidgets.QCheckBox(self.groupBox)
        self.needs_translation_checkbox.setMaximumSize(QtCore.QSize(80, 16777215))
        self.needs_translation_checkbox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.needs_translation_checkbox.setAutoFillBackground(False)
        self.needs_translation_checkbox.setObjectName("needs_translation_checkbox")
        self.horizontalLayout_2.addWidget(self.needs_translation_checkbox)
        self.translation_dest_lang_menu = QtWidgets.QComboBox(self.groupBox)
        self.translation_dest_lang_menu.setMinimumSize(QtCore.QSize(80, 0))
        self.translation_dest_lang_menu.setEditable(True)
        self.translation_dest_lang_menu.setObjectName("translation_dest_lang_menu")
        self.horizontalLayout_2.addWidget(self.translation_dest_lang_menu)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(8, -1, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.embed_sub_checkbox = QtWidgets.QCheckBox(self.groupBox)
        self.embed_sub_checkbox.setMaximumSize(QtCore.QSize(220, 16777215))
        self.embed_sub_checkbox.setObjectName("embed_sub_checkbox")
        self.horizontalLayout_3.addWidget(self.embed_sub_checkbox)
        self.live_chat_subs_checkbox = QtWidgets.QCheckBox(self.groupBox)
        self.live_chat_subs_checkbox.setMinimumSize(QtCore.QSize(130, 0))
        self.live_chat_subs_checkbox.setMaximumSize(QtCore.QSize(150, 16777215))
        self.live_chat_subs_checkbox.setObjectName("live_chat_subs_checkbox")
        self.horizontalLayout_3.addWidget(self.live_chat_subs_checkbox)
        self.all_subtitles_checkbox = QtWidgets.QCheckBox(self.groupBox)
        self.all_subtitles_checkbox.setMaximumSize(QtCore.QSize(130, 16777215))
        self.all_subtitles_checkbox.setObjectName("all_subtitles_checkbox")
        self.horizontalLayout_3.addWidget(self.all_subtitles_checkbox)
        spacerItem2 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.horizontalLayout_3.setStretch(0, 2)
        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.setStretch(2, 1)
        self.horizontalLayout_3.setStretch(3, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setCheckable(False)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setContentsMargins(-1, -1, 15, -1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)
        self.video_quality_menu = QtWidgets.QComboBox(self.groupBox_2)
        self.video_quality_menu.setEditable(True)
        self.video_quality_menu.setObjectName("video_quality_menu")
        self.gridLayout_2.addWidget(self.video_quality_menu, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 0, 2, 1, 1)
        self.video_format_menu = QtWidgets.QComboBox(self.groupBox_2)
        self.video_format_menu.setEditable(True)
        self.video_format_menu.setCurrentText("")
        self.video_format_menu.setObjectName("video_format_menu")
        self.gridLayout_2.addWidget(self.video_format_menu, 0, 3, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 1, 0, 1, 1)
        self.audio_quality_menu = QtWidgets.QComboBox(self.groupBox_2)
        self.audio_quality_menu.setEditable(True)
        self.audio_quality_menu.setObjectName("audio_quality_menu")
        self.gridLayout_2.addWidget(self.audio_quality_menu, 1, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 1, 2, 1, 1)
        self.audio_format_menu = QtWidgets.QComboBox(self.groupBox_2)
        self.audio_format_menu.setEditable(True)
        self.audio_format_menu.setObjectName("audio_format_menu")
        self.gridLayout_2.addWidget(self.audio_format_menu, 1, 3, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 2, 0, 1, 1)
        self.browser_menu = QtWidgets.QComboBox(self.groupBox_2)
        self.browser_menu.setObjectName("browser_menu")
        self.gridLayout_2.addWidget(self.browser_menu, 2, 1, 1, 1)
        self.recode_video_checkbox = QtWidgets.QCheckBox(self.groupBox_2)
        self.recode_video_checkbox.setMaximumSize(QtCore.QSize(80, 16777215))
        self.recode_video_checkbox.setSizeIncrement(QtCore.QSize(0, 0))
        self.recode_video_checkbox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.recode_video_checkbox.setObjectName("recode_video_checkbox")
        self.gridLayout_2.addWidget(self.recode_video_checkbox, 2, 2, 1, 1)
        self.recode_video_menu = QtWidgets.QComboBox(self.groupBox_2)
        self.recode_video_menu.setObjectName("recode_video_menu")
        self.gridLayout_2.addWidget(self.recode_video_menu, 2, 3, 1, 1)
        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(1, 2)
        self.gridLayout_2.setColumnStretch(2, 1)
        self.gridLayout_2.setColumnStretch(3, 2)
        self.horizontalLayout_5.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.import_cookies_from_browser_checkbox = QtWidgets.QCheckBox(self.groupBox_3)
        self.import_cookies_from_browser_checkbox.setObjectName("import_cookies_from_browser_checkbox")
        self.verticalLayout_4.addWidget(self.import_cookies_from_browser_checkbox)
        self.only_download_audio_checkbox = QtWidgets.QCheckBox(self.groupBox_3)
        self.only_download_audio_checkbox.setObjectName("only_download_audio_checkbox")
        self.verticalLayout_4.addWidget(self.only_download_audio_checkbox)
        self.download_all_playlist_checkbox = QtWidgets.QCheckBox(self.groupBox_3)
        self.download_all_playlist_checkbox.setObjectName("download_all_playlist_checkbox")
        self.verticalLayout_4.addWidget(self.download_all_playlist_checkbox)
        self.download_thumbnail_checkbox = QtWidgets.QCheckBox(self.groupBox_3)
        self.download_thumbnail_checkbox.setObjectName("download_thumbnail_checkbox")
        self.verticalLayout_4.addWidget(self.download_thumbnail_checkbox)
        self.horizontalLayout_5.addWidget(self.groupBox_3)
        self.horizontalLayout_5.setStretch(0, 5)
        self.horizontalLayout_5.setStretch(1, 2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        self.link_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.link_edit.setInputMask("")
        self.link_edit.setText("")
        self.link_edit.setObjectName("link_edit")
        self.horizontalLayout_6.addWidget(self.link_edit)
        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.download_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.download_button.sizePolicy().hasHeightForWidth())
        self.download_button.setSizePolicy(sizePolicy)
        self.download_button.setMaximumSize(QtCore.QSize(150, 16777215))
        self.download_button.setObjectName("download_button")
        self.horizontalLayout_7.addWidget(self.download_button)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 4)
        self.verticalLayout_2.setStretch(2, 4)
        self.verticalLayout_2.setStretch(3, 1)
        self.verticalLayout_2.setStretch(4, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 624, 23))
        self.menubar.setObjectName("menubar")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionShowLicense = QtWidgets.QAction(MainWindow)
        self.actionShowLicense.setObjectName("actionShowLicense")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionDefault = QtWidgets.QAction(MainWindow)
        self.actionDefault.setObjectName("actionDefault")
        self.actionSimplifiedChinese = QtWidgets.QAction(MainWindow)
        self.actionSimplifiedChinese.setCheckable(True)
        self.actionSimplifiedChinese.setChecked(False)
        self.actionSimplifiedChinese.setObjectName("actionSimplifiedChinese")
        self.actionTraditionalChinese = QtWidgets.QAction(MainWindow)
        self.actionTraditionalChinese.setCheckable(True)
        self.actionTraditionalChinese.setObjectName("actionTraditionalChinese")
        self.actionEnglish = QtWidgets.QAction(MainWindow)
        self.actionEnglish.setCheckable(True)
        self.actionEnglish.setObjectName("actionEnglish")
        self.actionViewLogs = QtWidgets.QAction(MainWindow)
        self.actionViewLogs.setObjectName("actionViewLogs")
        self.menuSettings.addAction(self.actionViewLogs)
        self.menuSettings.addAction(self.actionDefault)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addAction(self.actionShowLicense)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout)
        self.menu.addAction(self.actionSimplifiedChinese)
        self.menu.addAction(self.actionTraditionalChinese)
        self.menu.addAction(self.actionEnglish)
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "视频下载器(yt-dlp QtGUI)"))
        self.label.setText(_translate("MainWindow", "保存文件夹"))
        self.folder_button.setText(_translate("MainWindow", "选择文件夹"))
        self.groupBox.setTitle(_translate("MainWindow", "字幕设置"))
        self.only_sub_radio_button.setText(_translate("MainWindow", "仅下载字幕"))
        self.sub_and_video_radio_button.setText(_translate("MainWindow", "下载字幕和视频"))
        self.only_video_radio_button.setText(_translate("MainWindow", "仅下载视频"))
        self.label_2.setText(_translate("MainWindow", "格式"))
        self.label_3.setText(_translate("MainWindow", "语言"))
        self.needs_translation_checkbox.setText(_translate("MainWindow", "翻译为"))
        self.embed_sub_checkbox.setText(_translate("MainWindow", "内嵌字幕(仅mp4,webm,mkv,mov)"))
        self.live_chat_subs_checkbox.setText(_translate("MainWindow", "下载实时聊天/弹幕"))
        self.all_subtitles_checkbox.setText(_translate("MainWindow", "下载全部字幕"))
        self.groupBox_2.setTitle(_translate("MainWindow", "视频设置"))
        self.label_5.setText(_translate("MainWindow", "视频画质"))
        self.label_6.setText(_translate("MainWindow", "视频格式"))
        self.label_7.setText(_translate("MainWindow", "音质(0为最佳)"))
        self.label_8.setText(_translate("MainWindow", "音频格式"))
        self.label_9.setText(_translate("MainWindow", "浏览器"))
        self.recode_video_checkbox.setText(_translate("MainWindow", "格式转换"))
        self.groupBox_3.setTitle(_translate("MainWindow", "下载设置"))
        self.import_cookies_from_browser_checkbox.setText(_translate("MainWindow", "导入Cookies"))
        self.only_download_audio_checkbox.setText(_translate("MainWindow", "仅下载音频"))
        self.download_all_playlist_checkbox.setText(_translate("MainWindow", "下载整个列表"))
        self.download_thumbnail_checkbox.setText(_translate("MainWindow", "下载缩略图"))
        self.label_4.setText(_translate("MainWindow", "视频链接"))
        self.link_edit.setPlaceholderText(_translate("MainWindow", "请输入可支持的视频链接"))
        self.download_button.setText(_translate("MainWindow", "开始下载"))
        self.menuSettings.setTitle(_translate("MainWindow", "设置"))
        self.menuHelp.setTitle(_translate("MainWindow", "帮助"))
        self.menu.setTitle(_translate("MainWindow", "语言/Language"))
        self.actionHelp.setText(_translate("MainWindow", "帮助文档"))
        self.actionShowLicense.setText(_translate("MainWindow", "查看许可证"))
        self.actionAbout.setText(_translate("MainWindow", "关于"))
        self.actionDefault.setText(_translate("MainWindow", "恢复默认值"))
        self.actionSimplifiedChinese.setText(_translate("MainWindow", "中文（简体）"))
        self.actionTraditionalChinese.setText(_translate("MainWindow", "中文（繁體）"))
        self.actionEnglish.setText(_translate("MainWindow", "English"))
        self.actionViewLogs.setText(_translate("MainWindow", "查看日志"))
