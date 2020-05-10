"""
coding:utf-8
file: run.py
@author: jiangwei
@contact: jiangwei_1994124@163.com
@time: 2020/5/9 20:22
@desc:
"""
from view.login_window import LoginWindow
from PyQt5.QtWidgets import QApplication
import sys


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = LoginWindow()
    win.show()
    sys.exit(app.exec_())
