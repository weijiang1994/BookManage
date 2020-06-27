"""
coding:utf-8
file: home_window.py
@author: jiangwei
@contact: jiangwei_1994124@163.com
@time: 2020/5/9 22:03
@desc:
"""
import sys
from threading import Thread

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QApplication
from ui.home_window import Ui_Form
from util.crawl_util import parse_news, get_cnblogs_recommend_news
from util.common_util import SYS_STYLE, read_yaml, CONFIG_FILE_PATH


class HomeWindow(Ui_Form, QWidget):
    get_news_done_signal = pyqtSignal(int)

    def __init__(self):
        super(HomeWindow, self).__init__()
        self.setupUi(self)
        self.cnblogs_news_listWidget.setProperty('class', 'News')
        self.setStyleSheet(SYS_STYLE)
        self.news = None
        self.titles = None
        self.urls = None
        self.get_news_done_signal.connect(self.refresh_news_ls)
        self.init_data()

    def init_data(self):
        th = Thread(target=self.get_news)
        th.start()

    def get_news(self):
        try:
            count = read_yaml(CONFIG_FILE_PATH)['news_limit']
            self.news = get_cnblogs_recommend_news(count)
            self.titles, self.urls = parse_news(self.news)
            self.get_news_done_signal.emit(1)
        except:
            self.get_news_done_signal.emit(0)

    def refresh_news_ls(self):
        for title in self.titles:
            self.cnblogs_news_listWidget.addItem(title)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = HomeWindow()
    win.show()
    sys.exit(app.exec_())
