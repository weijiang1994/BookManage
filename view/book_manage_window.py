"""
coding:utf-8
file: book_manage_window.py
@author: jiangwei
@contact: jiangwei_1994124@163.com
@time: 2020/5/9 22:24
@desc:
"""
from threading import Thread

from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QHeaderView, QTableWidgetItem, QAbstractItemView, QMenu, QAction, QMessageBox
from ui.book_manage_window import Ui_Form
from util.dbutil import DBHelp
from view.add_book_window import AddBookWindow
from util.common_util import msg_box, SEARCH_CONTENT_MAP, DELETE_ICON, EDIT_ICON, BORROW_BOOK
from view.book_edit_window import BookEditWindow
from view.borrow_book_window import BorrowBookWindow


# noinspection DuplicatedCode
class BookManageWindow(Ui_Form, QWidget):
    query_book_info_done_signal = pyqtSignal(list)

    def __init__(self, user_role=None, username=None):
        super(BookManageWindow, self).__init__()
        self.setupUi(self)
        self.user_role = user_role
        self.username = username
        self.add_book_win = None
        self.book_edit_win = None
        self.borrow_boo_win = None
        self.book_id = list()
        self.init_ui()
        self.init_slot()
        self.init_data()

    def init_ui(self):
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.refresh_pushButton.setProperty('class', 'Aqua')
        self.add_book_pushButton.setProperty('class', 'Aqua')
        self.search_book_pushButton.setProperty('class', 'Aqua')
        self.search_book_pushButton.setMinimumWidth(60)
        self.add_book_pushButton.setMinimumWidth(80)
        self.refresh_pushButton.setMinimumWidth(60)
        self.tableWidget.customContextMenuRequested.connect(self.generate_menu)
        if self.user_role == '普通用户':
            self.add_book_pushButton.setVisible(False)

    def generate_menu(self, pos):
        row_num = -1
        for i in self.tableWidget.selectionModel().selection().indexes():
            row_num = i.row()
        if row_num == -1:
            return
        if self.user_role == '管理员':
            menu = QMenu()
            edit_action = QAction(u'编辑书本')
            edit_action.setIcon(QIcon(EDIT_ICON))
            menu.addAction(edit_action)

            delete_action = QAction(u'删除书本')
            delete_action.setIcon(QIcon(DELETE_ICON))
            menu.addAction(delete_action)
            action = menu.exec_(self.tableWidget.mapToGlobal(pos))
            if action == edit_action:
                self.book_edit_win = BookEditWindow(book_info=self.tableWidget.item(row_num, 0).text())
                self.book_edit_win.show()

            if action == delete_action:
                reply = QMessageBox.warning(self, '消息', '确定删除该书籍吗?',
                                            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if reply == QMessageBox.Yes:
                    db = DBHelp()
                    db.delete(table_name='book', column_name='id', condition=self.book_id[row_num])
                    db.db_commit()
                    db.instance = None
                    del db
                    self.refresh_pushButton.click()
                    msg_box(self, '提示', '删除书本操作成功!')
        else:
            menu = QMenu()
            borrow_action = QAction(u'借书')
            borrow_action.setIcon(QIcon(BORROW_BOOK))
            menu.addAction(borrow_action)
            action = menu.exec_(self.tableWidget.mapToGlobal(pos))
            if action == borrow_action:
                self.borrow_boo_win = BorrowBookWindow(book_id=self.book_id[row_num],
                                                       book_name=self.tableWidget.item(row_num, 0).text(),
                                                       current_user=self.username)
                self.borrow_boo_win.show()

    def init_slot(self):
        self.add_book_pushButton.clicked.connect(lambda: self.btn_slot('add'))
        self.search_book_pushButton.clicked.connect(lambda: self.btn_slot('search'))
        self.query_book_info_done_signal.connect(self.show_book)
        self.refresh_pushButton.clicked.connect(lambda: self.btn_slot('refresh'))

    def init_data(self):
        self.get_book_info()

    def show_book(self, book_info_result):
        self.book_id = list()
        for i in range(self.tableWidget.rowCount()):
            self.tableWidget.removeRow(0)
        count = book_info_result[0]
        self.book_total_label.setText('本图书馆共有藏书' + str(count) + '本~')
        books = book_info_result[1]
        for book in books:
            self.tableWidget.insertRow(self.tableWidget.rowCount())
            self.book_id.append(book[0])
            for i in range(1, 4):
                item = QTableWidgetItem(book[i])
                self.tableWidget.setItem(self.tableWidget.rowCount() - 1, i - 1, item)
            item = QTableWidgetItem(str(book[-1]))
            self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 3, item)
            item = QTableWidgetItem(str(book[4]))
            self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 4, item)
            item = QTableWidgetItem(str(book[5]))
            self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 5, item)
        for i in range(self.tableWidget.rowCount()):
            for j in range(6):
                item = self.tableWidget.item(i, j)
                item.setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)

    def btn_slot(self, tag):
        if tag == 'add':
            self.add_book_win = AddBookWindow()
            self.add_book_win.add_book_don_signal.connect(self.add_book_done)
            self.add_book_win.show()

        if tag == 'search':
            search_type = self.search_comboBox.currentText()
            search_content = self.book_search_content_lineEdit.text()
            if search_content == '':
                msg_box(self, '提示', '请输入搜索内容~')
                return
            db = DBHelp()
            count, res = db.query_super(table_name='book', column_name=SEARCH_CONTENT_MAP.get(search_type),
                                        condition=search_content)
            if count == 0:
                msg_box(self, '提示', '您所搜索的图书不存在!')
                return
            self.show_book([count, res])

        if tag == 'refresh':
            self.get_book_info()

    def get_book_info(self):
        th = Thread(target=self.book_info_th)
        th.start()

    def book_info_th(self):
        db = DBHelp()
        count, res = db.query_all(table_name='book')
        self.query_book_info_done_signal.emit([count, res])

    def add_book_done(self):
        self.refresh_pushButton.click()
