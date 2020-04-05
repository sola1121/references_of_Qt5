# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/sola1121/practices_projects/references_of_qt5/02_基本窗口控件/示例内容/QWidget_with_icon.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(360, 160)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("02_基本窗口控件/示例内容/sources/images/python-simple-color-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(150, 72, 75, 30))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("02_基本窗口控件/示例内容/sources/icons/android_02.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(16, 16))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "按钮"))


import sys

from PyQt5.QtWidgets import QApplication, QWidget


class WinForm(QWidget, Ui_Form):
    """显示窗口"""
    def __init__(self, parent=None):
        super(WinForm, self).__init__(parent=parent)
        self.setupUi(self)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = WinForm()
    win.show()
    sys.exit(app.exec())