# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'borrow_info_window.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(240, 203)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setStyleSheet("font: 12pt \"宋体\";")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.line = QtWidgets.QFrame(Form)
        self.line.setMaximumSize(QtCore.QSize(16777215, 1))
        self.line.setStyleSheet("background-color: rgb(126, 127, 113);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setMinimumSize(QtCore.QSize(72, 0))
        self.label_2.setStyleSheet("font: 12pt \"宋体\";")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.book_name_lineEdit = QtWidgets.QLineEdit(Form)
        self.book_name_lineEdit.setStyleSheet("font: 12pt \"宋体\";")
        self.book_name_lineEdit.setReadOnly(True)
        self.book_name_lineEdit.setObjectName("book_name_lineEdit")
        self.horizontalLayout.addWidget(self.book_name_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setMaximumSize(QtCore.QSize(16777215, 1))
        self.line_2.setStyleSheet("background-color: rgb(126, 127, 113);")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setStyleSheet("font: 12pt \"宋体\";")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.borrow_day_lineEdit = QtWidgets.QLineEdit(Form)
        self.borrow_day_lineEdit.setStyleSheet("font: 12pt \"宋体\";")
        self.borrow_day_lineEdit.setObjectName("borrow_day_lineEdit")
        self.horizontalLayout_2.addWidget(self.borrow_day_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.line_4 = QtWidgets.QFrame(Form)
        self.line_4.setMaximumSize(QtCore.QSize(16777215, 1))
        self.line_4.setStyleSheet("background-color: rgb(126, 127, 113);")
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout.addWidget(self.line_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.borrow_pushButton = QtWidgets.QPushButton(Form)
        self.borrow_pushButton.setStyleSheet("font: 12pt \"宋体\";")
        self.borrow_pushButton.setObjectName("borrow_pushButton")
        self.horizontalLayout_3.addWidget(self.borrow_pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "图书借阅"))
        self.label_2.setText(_translate("Form", "书名:"))
        self.label_3.setText(_translate("Form", "借阅天数:"))
        self.borrow_pushButton.setText(_translate("Form", "借阅"))

