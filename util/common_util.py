"""
coding:utf-8
file: common_util.py
@author: jiangwei
@contact: jiangwei_1994124@163.com
@time: 2020/5/9 20:09
@desc:
"""
import datetime
import hashlib

from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QMessageBox
import uuid
import frozen_dir
import yaml

SUPER_DIR = frozen_dir.app_path()
ROLE_MAP = {'0': '管理员', '1': '普通用户'}

APP_ICON = SUPER_DIR + r'/res/img/app-icon.png'
DELETE_ICON = SUPER_DIR + r'/res/img/delete.png'
EDIT_ICON = SUPER_DIR + r'/res/img/edit.png'
BORROW_BOOK = SUPER_DIR + r'/res/img/borrow_book.png'
HOME_PAGE = SUPER_DIR + r'/res/img/home.png'
DELAY_TIME = SUPER_DIR + r'/res/img/delay_time.ico'
RETURN = SUPER_DIR + r'/res/img/return.ico'
DEL_RECORD = SUPER_DIR + r'/res/img/delete.ico'
PUSH_RETURN = SUPER_DIR + r'/res/img/push.ico'

BORROW_STATUS_MAP = {'0': '未还', '1': '已还'}
SEARCH_CONTENT_MAP = {'书名': 'book_name', '出版社': 'publish_company', '作者': 'author', '用户': 'borrow_user'}

CONFIG_FILE_PATH = SUPER_DIR + r'/config/setting.yml'

PATTERS = ['^[0-9]{1,2}$']


def get_md5(data):
    """
    获取md5加密密文
    :param data: 明文
    :return: 加密后的密文
    """
    m = hashlib.md5()
    b = data.encode(encoding='utf-8')
    m.update(b)
    return m.hexdigest()


def read_yaml(path):
    with open(path, encoding='utf-8') as f:
        stm = f.read()
    content = yaml.load(stm, Loader=yaml.FullLoader)
    return content


def get_uuid():
    return str(uuid.uuid1()).replace('-', '')


def msg_box(widget, title, msg):
    QMessageBox.warning(widget, title, msg, QMessageBox.Yes)


def accept_box(widget, title, msg):
    return QMessageBox.warning(widget, title, msg, QMessageBox.Yes|QMessageBox.No, QMessageBox.No)


def get_current_time():
    dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return dt


def read_qss(qss_file):
    with open(qss_file, 'r', encoding='utf-8') as f:
        return f.read()


def get_return_day(day):
    return (datetime.datetime.now() + datetime.timedelta(days=day)).strftime('%Y-%m-%d %H:%M:%S')


def set_le_reg(widget, le, pattern):
    rx = QRegExp()
    rx.setPattern(pattern)
    qrx = QRegExpValidator(rx, widget)
    le.setValidator(qrx)


SYS_STYLE = read_qss(SUPER_DIR + r'/res/style/style.qss')
