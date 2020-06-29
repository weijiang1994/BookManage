"""
@Time    : 2020/6/29 15:51
@Author  : weijiang
@Site    : 
@File    : ask_return_window.py
@Software: PyCharm
"""
from threading import Thread

from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QIcon

from ui.ask_return_window import Ui_Form
from PyQt5.QtWidgets import QWidget, QApplication
import sys
from util.common_util import SYS_STYLE, APP_ICON, msg_box
from util.dbutil import DBHelp


class AskReturnWindow(Ui_Form, QWidget):
    insert_ask_info_done_signal = pyqtSignal(int)

    def __init__(self, data=None):
        super(AskReturnWindow, self).__init__()
        self.setupUi(self)
        self.init_ui()
        self.init_slot()
        self.data = data

    def init_ui(self):
        self.textEdit.setPlaceholderText('请输入催还理由')
        self.setWindowModality(Qt.ApplicationModal)
        self.setWindowIcon(QIcon(APP_ICON))
        self.setWindowTitle('图书催还')
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        self.submit_pushButton.setProperty('class', 'Aqua')
        self.submit_pushButton.setMinimumWidth(55)
        self.close_pushButton.setMinimumWidth(55)
        self.close_pushButton.setProperty('class', 'Aqua')
        self.setStyleSheet(SYS_STYLE)

    def init_slot(self):
        self.insert_ask_info_done_signal.connect(self.close_win)
        self.close_pushButton.clicked.connect(lambda : self.btn_slot('close'))
        self.submit_pushButton.clicked.connect(lambda : self.btn_slot('submit'))

    def close_win(self, tag):
        if tag == 1:
            msg_box(self, '提示', '图书催还成功!')
            self.close()

    def btn_slot(self, tag):
        if tag == 'close':
            self.close()
        if tag == 'submit':
            if self.textEdit.toPlainText() == '':
                msg_box(self, '提示', '请输入催还理由!')
                return
            ask_reason = self.textEdit.toPlainText()
            self.data.insert(2, ask_reason)
            th = Thread(target=self.insert_ask_return_info, args=(self.data,))
            th.start()

    def insert_ask_return_info(self, data):
        db = DBHelp()
        db.insert_ask_return_info(data=data)
        db.db_commit()
        db.instance = None
        del db
        self.insert_ask_info_done_signal.emit(1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = AskReturnWindow(data=1)
    win.show()
    sys.exit(app.exec_())
