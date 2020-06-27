"""
coding:utf-8
file: main_window.py
@author: jiangwei
@contact: jiangwei_1994124@163.com
@time: 2020/5/9 19:52
@desc:
"""
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QWidget
from ui.main_window import Ui_MainWindow
from util.common_util import ROLE_MAP, APP_ICON, SYS_STYLE
from view.home_window import HomeWindow
from view.book_manage_window import BookManageWindow
from view.borrow_info_window import BorrowInfoWindow
from view.setting_window import SettingWindow


# noinspection PyCallByClass
class MainWindow(Ui_MainWindow, QMainWindow):

    def __init__(self,login=None, username=None, role=None):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.is_change_user = False
        self.username = username
        self.login_win = login
        self.role = ROLE_MAP.get(str(role))
        self.init_slot()
        self.init_ui()

    def init_ui(self):
        self.pushButton.setProperty('class', 'Aqua')
        self.pushButton.setMinimumWidth(60)
        self.listWidget.setProperty('class', 'Normal')
        self.setStyleSheet(SYS_STYLE)
        self.setWindowIcon(QIcon(APP_ICON))
        self.setWindowTitle('图书管理系统-Version 1.0.0.0 Beta')
        self.listWidget.setCurrentRow(0)
        self.current_username_label.setText(self.username)
        self.current_role_label.setText(self.role)
        self.stackedWidget.removeWidget(self.page)
        self.stackedWidget.removeWidget(self.page_2)
        self.stackedWidget.addWidget(HomeWindow())
        self.stackedWidget.addWidget(BorrowInfoWindow(user_role=self.role, username=self.username))
        self.stackedWidget.addWidget(BookManageWindow(self.role, self.username))
        self.stackedWidget.addWidget(SettingWindow())
        self.stackedWidget.addWidget(QWidget())

    def init_slot(self):
        self.listWidget.currentItemChanged.connect(self.item_changed)
        self.pushButton.clicked.connect(self.log_out)

    def item_changed(self):
        self.stackedWidget.setCurrentIndex(self.listWidget.currentRow())

    def log_out(self):
        self.is_change_user = True
        self.close()

    def closeEvent(self, event):
        if self.is_change_user:
            reply = QMessageBox.question(self, '消息', '确定退出当前账号吗?',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        else:
            reply = QMessageBox.question(self, '消息', '确定退出系统吗?',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
            if self.is_change_user:
                self.login_win.show()
        else:
            event.ignore()
            self.is_change_user = False
