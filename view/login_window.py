"""
coding:utf-8
file: login_window.py
@author: jiangwei
@contact: jiangwei_1994124@163.com
@time: 2020/5/9 19:47
@desc:
"""
from threading import Thread

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal
from ui.login_window import Ui_Form
from view.main_window import MainWindow
from util.dbutil import DBHelp
from util.common_util import msg_box, get_md5, APP_ICON
from view.register_window import RegisterWindow


class LoginWindow(Ui_Form, QWidget):
    login_done_signal = pyqtSignal(int)

    def __init__(self):
        super(LoginWindow, self).__init__()
        self.setupUi(self)
        self.role = None
        self.init_ui()
        self.main_window = None
        self.register_win = None
        self.init_slot()

    def init_ui(self):
        self.setWindowTitle('用户登录')
        self.setWindowIcon(QIcon(APP_ICON))

    def init_slot(self):
        self.register_pushButton.clicked.connect(lambda: self.btn_slot('register'))
        self.login_pushButton.clicked.connect(lambda: self.btn_slot('login'))
        self.login_done_signal.connect(self.handle_login)

    def btn_slot(self, tag):
        if tag == 'register':
            self.register_win = RegisterWindow()
            self.register_win.show()

        if tag == 'login':
            username = self.username_lineEdit.text()
            password = self.password_lineEdit.text()
            if username == '' or password == '':
                msg_box(self, '提示', '请输入用户名或密码!')
                return
            login_th = Thread(target=self.login, args=(username, password))
            login_th.start()

    def login(self, username, password):
        db = DBHelp()
        count, res = db.query_super(table_name='user', column_name='username', condition=username)
        if count == 0:
            self.login_done_signal.emit(1)
            return
        if get_md5(password) != res[0][2]:
            self.login_done_signal.emit(11)
            return
        self.role = res[0][3]
        self.login_done_signal.emit(111)

    def handle_login(self, login_result):
        if login_result == 1:
            msg_box(self, '提示', '用户名不存在,请重试!')
            return
        if login_result == 11:
            msg_box(self, '提示', '用户名或密码错误!')
            return
        if login_result == 111:
            username = self.username_lineEdit.text()
            self.main_window = MainWindow(username=username, role=self.role)
            self.main_window.show()
            self.close()
