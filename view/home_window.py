"""
coding:utf-8
file: home_window.py
@author: jiangwei
@contact: jiangwei_1994124@163.com
@time: 2020/5/9 22:03
@desc:
"""
from PyQt5.QtWidgets import QWidget
from ui.home_window import Ui_Form


class HomeWindow(Ui_Form, QWidget):

    def __init__(self):
        super(HomeWindow, self).__init__()
        self.setupUi(self)
