"""
coding:utf-8
file: setting_window.py
@author: jiangwei
@contact: jiangwei_1994124@163.com
@time: 2020/6/27 23:07
@desc:
"""
from ui.setting_window import Ui_Form
from PyQt5.QtWidgets import QWidget


class SettingWindow(Ui_Form, QWidget):
    def __init__(self):
        super(SettingWindow, self).__init__()
        self.setupUi(self)
