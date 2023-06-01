import re
import os
import sys
import webbrowser

import yt_dlp
import yaml

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QMainWindow
from PyQt5.QtGui import *
from PyQt5 import uic

from constants import *

current_folder = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_folder)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 加载UI文件并初始化界面
        uic.loadUi(UI, self)

        self.title = ' - '.join([TITLE, VERSION, LAST_EDIT_DATE])
        self.icon = QIcon("download_icon.ico")

        # 设置窗口
        self.setWindowTitle(self.title)
        self.setWindowIcon(self.icon)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec_())