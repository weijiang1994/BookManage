"""
coding:utf-8
file: main_window.py
@author: jiangwei
@contact: jiangwei_1994124@163.com
@time: 2020/5/9 19:52
@desc:
"""
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from ui.main_window import Ui_MainWindow
from util.common_util import read_qss, SUPER_DIR, ROLE_MAP, APP_ICON
from view.home_window import HomeWindow
from view.book_manage_window import BookManageWindow
from view.borrow_info_window import BorrowInfoWindow


# noinspection PyCallByClass
class MainWindow(Ui_MainWindow, QMainWindow):

    def __init__(self, username=None, role=None):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.username = username
        self.role = ROLE_MAP.get(str(role))
        self.init_slot()
        self.init_ui()

    def init_ui(self):
        self.setWindowIcon(QIcon(APP_ICON))
        qss = read_qss(SUPER_DIR + r'/res/style/style.qss')
        self.setWindowTitle('图书管理系统-Version 1.0.0.0 Beta')
        self.listWidget.setStyleSheet(qss)
        self.setStyleSheet("QWidget:focus{outline: none;}")
        self.listWidget.setCurrentRow(0)
        self.current_username_label.setText(self.username)
        self.current_role_label.setText(self.role)
        self.stackedWidget.removeWidget(self.page)
        self.stackedWidget.removeWidget(self.page_2)
        self.stackedWidget.addWidget(HomeWindow())
        self.stackedWidget.addWidget(BorrowInfoWindow(user_role=self.role, username=self.username))
        self.stackedWidget.addWidget(BookManageWindow(self.role, self.username))

    def init_slot(self):
        self.listWidget.currentItemChanged.connect(self.item_changed)

    def item_changed(self):
        self.stackedWidget.setCurrentIndex(self.listWidget.currentRow())

    def closeEvent(self, event):
        reply = QMessageBox.question(self, '消息', '确定退出系统吗?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
