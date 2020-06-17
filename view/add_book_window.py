"""
coding:utf-8
file: add_book_window.py
@author: jiangwei
@contact: jiangwei_1994124@163.com
@time: 2020/5/9 22:40
@desc:
"""
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget
from ui.add_book_window import Ui_Form
from util.common_util import msg_box, get_current_time, get_uuid, APP_ICON, SYS_STYLE
from util.dbutil import DBHelp


class AddBookWindow(Ui_Form, QWidget):
    add_book_don_signal = pyqtSignal()

    def __init__(self):
        super(AddBookWindow, self).__init__()
        self.setupUi(self)
        self.setWindowModality(Qt.ApplicationModal)
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        self.setWindowTitle('添加新图书')
        self.add_book_pushButton.clicked.connect(self.add)
        self.setWindowIcon(QIcon(APP_ICON))
        self.add_book_pushButton.setProperty('class', 'Aqua')
        self.setStyleSheet(SYS_STYLE)

    def add(self):
        book_name = self.book_name_lineEdit.text()
        author = self.author_lineEdit.text()
        publish_company = self.publish_company_lineEdit.text()
        publish_date = self.publish_date_lineEdit.text()
        store_num = self.store_num_lineEdit.text()
        if '' in [book_name, author, publish_company, publish_date, store_num]:
            msg_box(self, '错误', '请输入图书的关键信息!')
            return
        db = DBHelp()
        count, res = db.query_super(table_name='book', column_name='book_name', condition=book_name)
        if count:
            msg_box(self, '错误', '已存在同名书籍!')
            return
        book_info = [get_uuid(), book_name, author, publish_company, store_num, 0, get_current_time(), publish_date]
        db.add_book(data=book_info)
        db.db_commit()
        db.instance = None
        del db
        self.add_book_don_signal.emit()
        self.close()
        msg_box(self, '提示', '添加新图书成功!')
