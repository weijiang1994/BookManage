"""
coding:utf-8
file: borrow_info_window.py
@author: jiangwei
@contact: jiangwei_1994124@163.com
@time: 2020/5/9 22:34
@desc:
"""
from threading import Thread

from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QColor, QFont, QBrush
from PyQt5.QtWidgets import QWidget, QHeaderView, QAbstractItemView, QTableWidgetItem
from ui.book_borrow_info_window import Ui_Form
from util.dbutil import DBHelp
from util.common_util import BORROW_STATUS_MAP


class BorrowInfoWindow(Ui_Form, QWidget):
    init_data_done_signal = pyqtSignal(list)

    def __init__(self, user_role=None, username=None):
        super(BorrowInfoWindow, self).__init__()
        self.setupUi(self)
        self.user_role = user_role
        self.username = username
        self.borrow_info_list = list()
        self.init_data_done_signal.connect(self.show_info)
        self.init_ui()
        self.init_data()

    def init_ui(self):
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def init_data(self):
        th = Thread(target=self.book_info_th)
        th.start()

    def show_info(self, infos):
        for i in range(self.tableWidget.rowCount()):
            self.tableWidget.removeRow(0)
        for info in infos:
            self.tableWidget.insertRow(self.tableWidget.rowCount())
            for i in range(len(info)):
                item = QTableWidgetItem(str(info[i]))
                if info[i] == '未还':
                    item.setBackground(QColor('#ff3333'))
                if info[i] == '已还':
                    item.setBackground(QColor('#33ff33'))
                self.tableWidget.setItem(self.tableWidget.rowCount() - 1, i, item)
        for i in range(self.tableWidget.rowCount()):
            for j in range(self.tableWidget.columnCount()):
                item = self.tableWidget.item(i, j)
                item.setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)

    def book_info_th(self):
        if self.user_role == '管理员':
            db = DBHelp()
            count, res = db.query_all(table_name='borrow_info')
            self.method_name(db, res)
        else:
            db = DBHelp()
            count, res = db.query_super(table_name='borrow_info', column_name='borrow_user', condition=self.username)
            self.method_name(db, res)

    def method_name(self, db, res):
        for record in res:
            book_id = record[1]
            count, book_info = db.query_super(table_name='book', column_name='id', condition=book_id)
            sub_info = [record[3], record[2], book_info[0][3], book_info[0][-1], record[4], str(record[6]),
                        str(record[7]), BORROW_STATUS_MAP.get(str(record[-1]))]
            self.borrow_info_list.append(sub_info)
        self.init_data_done_signal.emit(self.borrow_info_list)