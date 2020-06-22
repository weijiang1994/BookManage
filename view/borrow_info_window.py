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
from PyQt5.QtGui import QColor, QIcon
from PyQt5.QtWidgets import QWidget, QHeaderView, QAbstractItemView, QTableWidgetItem, QMessageBox, QMenu, QAction
from ui.book_borrow_info_window import Ui_Form
from util.dbutil import DBHelp
from util.common_util import BORROW_STATUS_MAP, SYS_STYLE, SEARCH_CONTENT_MAP, msg_box, RETURN, DELAY_TIME, accept_box


class BorrowInfoWindow(Ui_Form, QWidget):
    init_data_done_signal = pyqtSignal(list)

    def __init__(self, user_role=None, username=None):
        super(BorrowInfoWindow, self).__init__()
        self.setupUi(self)
        self.user_role = user_role
        self.username = username
        self.borrow_info_list = list()
        self.init_data_done_signal.connect(self.show_info)
        self.refresh_pushButton.clicked.connect(self.init_data)
        self.search_borrow_user_pushButton.clicked.connect(self.search_borrow_info)
        self.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tableWidget.customContextMenuRequested.connect(self.generate_menu)
        self.return_flag = []
        self.borrow_info_id = []
        self.init_ui()
        self.init_data()

    def generate_menu(self, pos):
        row_num = -1
        for i in self.tableWidget.selectionModel().selection().indexes():
            row_num = i.row()
        if row_num == -1:
            return
        if self.user_role == '普通用户':
            menu = QMenu()
            return_action = QAction(u'还书')
            return_action.setIcon(QIcon(RETURN))
            menu.addAction(return_action)

            delay_borrow_action = QAction(u'续借')
            delay_borrow_action.setIcon(QIcon(DELAY_TIME))
            menu.addAction(delay_borrow_action)

            # 如果当前条目为已还则菜单栏为不可点击状态
            if self.return_flag[row_num] == 1:
                return_action.setEnabled(False)
                delay_borrow_action.setEnabled(False)
            action = menu.exec_(self.tableWidget.mapToGlobal(pos))

            if action == return_action:
                try:
                    accept_box(self, '提示', '确定归还当前书本吗？', func=self.return_book,
                               arg=self.borrow_info_id[row_num])
                except :
                    import traceback
                    traceback.print_exc()

    def return_book(self, borrow_id):
        db = DBHelp()
        db.update_borrow_statue(borrow_id)
        db.db_commit()
        db.instance = None
        del db


    def search_borrow_info(self):
        if self.borrow_user_search_lineEdit.text() == '':
            msg_box(self, '提示', '请输入需要搜索的内容!')
            return
        if self.user_role == '管理员':
            search_type = self.comboBox.currentText()
            search_content = self.borrow_user_search_lineEdit.text()
            db = DBHelp()
            count, res = db.query_super(table_name='borrow_info', column_name=SEARCH_CONTENT_MAP.get(search_type),
                                        condition=search_content)
            if count == 0:
                msg_box(widget=self, title='提示', msg='未找到相关记录!')
                return
            self.get_data_from_database(db, res=res)

    def init_ui(self):
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        self.setStyleSheet(SYS_STYLE)
        self.refresh_pushButton.setProperty('class', 'Aqua')
        self.search_borrow_user_pushButton.setProperty('class', 'Aqua')
        self.refresh_pushButton.setMinimumWidth(60)
        self.search_borrow_user_pushButton.setMinimumWidth(60)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def init_data(self):
        self.borrow_user_search_lineEdit.clear()
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
            self.get_data_from_database(db, res)
        else:
            db = DBHelp()
            count, res = db.query_super(table_name='borrow_info', column_name='borrow_user', condition=self.username)
            self.get_data_from_database(db, res)

    def get_data_from_database(self, db, res):
        self.return_flag = []
        self.borrow_info_id = []
        self.borrow_info_list.clear()
        for record in res:
            book_id = record[1]
            self.borrow_info_id.append(book_id)
            count, book_info = db.query_super(table_name='book', column_name='id', condition=book_id)
            sub_info = [record[3], record[2], book_info[0][3], book_info[0][-1], record[4], str(record[6]),
                        str(record[7]), BORROW_STATUS_MAP.get(str(record[-1]))]
            self.return_flag.append(record[-1])
            self.borrow_info_list.append(sub_info)
        self.init_data_done_signal.emit(self.borrow_info_list)
