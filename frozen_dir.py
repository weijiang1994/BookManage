"""
coding:utf-8
file: frozen_dir.py
@author: jiangwei
@contact: jiangwei_1994124@163.com
@time: 2020/5/9 21:28
@desc:
"""
import sys
import os


def app_path():
    if hasattr(sys, 'frozen'):
        return os.path.dirname(sys.executable)
    return os.path.dirname(__file__)
