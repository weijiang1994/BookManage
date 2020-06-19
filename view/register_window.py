"""
coding:utf-8
file: register_window.py
@author: jiangwei
@contact: jiangwei_1994124@163.com
@time: 2020/5/9 20:47
@desc:
"""
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QApplication
from ui.register_window import Ui_Form
from util.common_util import msg_box, get_md5, get_uuid, get_current_time, SYS_STYLE, APP_ICON
from util.dbutil import DBHelp


class RegisterWindow(Ui_Form, QWidget):
    def __init__(self):
        super(RegisterWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('用户注册')
        self.init_ui()
        self.register_pushButton.clicked.connect(self.register)

    def init_ui(self):
        self.register_pushButton.setProperty('class', 'Aqua')
        self.setStyleSheet(SYS_STYLE)
        self.register_pushButton.setMinimumWidth(60)
        self.setWindowIcon(QIcon(APP_ICON))
        self.setWindowModality(Qt.ApplicationModal)
        self.setWindowFlags(Qt.WindowCloseButtonHint)

    def register(self):
        username = self.username_lineEdit.text()
        password = self.password_lineEdit.text()
        confirm = self.confirm_password_lineEdit.text()
        if '' in [username, password, confirm]:
            msg_box(self, '提示', '关键信息不能为空!')
            return
        db = DBHelp()
        count, res = db.query_super(table_name='user', column_name='username', condition=username)
        if count != 0:
            msg_box(self, '提示', '用户名已存在!')
            return
        if password != confirm:
            msg_box(self, '错误', '两次输入密码不一致!')
            return
        user_info = [get_uuid(), username, get_md5(password), 1, get_current_time(), 0, get_current_time()]
        db.add_user(user_info)
        db.db_commit()
        db.instance = None
        del db
        msg_box(self, '提示', '注册成功!')
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = RegisterWindow()
    win.show()
    sys.exit(app.exec())
