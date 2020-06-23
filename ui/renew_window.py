# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'renew_window.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(253, 142)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.book_name_label = QtWidgets.QLabel(Form)
        self.book_name_label.setObjectName("book_name_label")
        self.verticalLayout.addWidget(self.book_name_label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.renew_days_lineEdit = QtWidgets.QLineEdit(Form)
        self.renew_days_lineEdit.setText("")
        self.renew_days_lineEdit.setObjectName("renew_days_lineEdit")
        self.horizontalLayout.addWidget(self.renew_days_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.return_date_lineEdit = QtWidgets.QLineEdit(Form)
        self.return_date_lineEdit.setText("")
        self.return_date_lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.return_date_lineEdit.setReadOnly(True)
        self.return_date_lineEdit.setObjectName("return_date_lineEdit")
        self.horizontalLayout_2.addWidget(self.return_date_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.renew_pushButton = QtWidgets.QPushButton(Form)
        self.renew_pushButton.setObjectName("renew_pushButton")
        self.horizontalLayout_3.addWidget(self.renew_pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.book_name_label.setText(_translate("Form", "图书续借"))
        self.label_2.setText(_translate("Form", "天数:"))
        self.renew_days_lineEdit.setPlaceholderText(_translate("Form", "请输入续借天数"))
        self.label_3.setText(_translate("Form", "日期:"))
        self.renew_pushButton.setText(_translate("Form", "续借"))

