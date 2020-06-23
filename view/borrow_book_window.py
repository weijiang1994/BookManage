"""
coding:utf-8
file: borrow_book_window.py
@author: jiangwei
@contact: jiangwei_1994124@163.com
@time: 2020/5/10 14:25
@desc:
"""
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget
from ui.borrow_info_window import Ui_Form
from util.common_util import msg_box, get_uuid, get_return_day, get_current_time, APP_ICON, SYS_STYLE, PATTERS, \
     set_le_reg
from util.dbutil import DBHelp


class BorrowBookWindow(Ui_Form, QWidget):

    def __init__(self, book_id=None, book_name=None, current_user=None):
        super(BorrowBookWindow, self).__init__()
        self.setupUi(self)
        self.book_id = book_id
        self.book_name = book_name
        self.current_user = current_user
        self.setWindowTitle('借书')
        self.setWindowIcon(QIcon(APP_ICON))
        self.book_name_lineEdit.setText(self.book_name)
        self.borrow_pushButton.clicked.connect(self.borrow_book)
        self.setWindowModality(Qt.ApplicationModal)
        self.borrow_pushButton.setProperty('class', 'Aqua')
        set_le_reg(self, self.borrow_day_lineEdit, pattern=PATTERS[0])
        self.setStyleSheet(SYS_STYLE)

    def borrow_book(self):
        borrow_day = self.borrow_day_lineEdit.text()
        if borrow_day == '':
            msg_box(self, '提示', '借阅天数不能为空！')
            return
        db = DBHelp()
        db.update_borrow(book_id=self.book_id)
        borrow_info = [get_uuid(), self.book_id, self.book_name, self.current_user, 1, borrow_day, get_current_time(),
                       get_return_day(int(borrow_day)), 0]
        db.insert_borrow_info(data=borrow_info)
        db.db_commit()
        db.instance = None
        del db
        self.close()
        msg_box(self, '提示', '借阅成功')
