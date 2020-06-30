"""
coding:utf-8
file: setting_window.py
@author: jiangwei
@contact: jiangwei_1994124@163.com
@time: 2020/6/27 23:07
@desc:
"""
import sys

from ui.setting_window import Ui_Form
from PyQt5.QtWidgets import QWidget, QApplication
from util.common_util import SYS_STYLE


class SettingWindow(Ui_Form, QWidget):
    def __init__(self):
        super(SettingWindow, self).__init__()
        self.setupUi(self)
        self.setStyleSheet(SYS_STYLE)
        self.init_ui()
        self.init_slot()
        self.init_data()

    def init_data(self):
        pass

    def init_ui(self):
        self.pushButton.setProperty('class', 'Aqua')
        self.pushButton.setMinimumWidth(70)
        self.setStyleSheet(SYS_STYLE)

    def init_slot(self):
        self.pushButton.clicked.connect(self.save_setting)

    def save_setting(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = SettingWindow()
    win.show()
    sys.exit(app.exec_())

