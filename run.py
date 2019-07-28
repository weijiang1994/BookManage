"""
author:jiangwei
project:Sample_01
date:2019/7/27
filename:run
ide:PyCharm
"""

from _class.LoginWinClass import LoginWinClass
import sys
from PyQt5.QtWidgets import QApplication


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = LoginWinClass()
    win.show()
    sys.exit(app.exec_())
