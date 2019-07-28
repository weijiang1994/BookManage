"""
coding:utf-8
file: frozen_dir.py
@author: jiangwei
@contact: 804022023@qq.com
@time: 2019/7/27 10:19
@desc:
"""
import sys
import os


def app_path():
    if hasattr(sys, 'frozen'):
        return os.path.dirname(sys.executable)
    return os.path.dirname(__file__)
