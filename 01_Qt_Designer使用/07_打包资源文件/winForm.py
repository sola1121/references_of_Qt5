# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/sola1121/practices_projects/references_of_Qt5/01_Qt_Designer使用/07_打包资源文件/winForm.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_winForm(object):
    def setupUi(self, winForm):
        winForm.setObjectName("winForm")
        winForm.resize(498, 201)
        self.pythonLabel = QtWidgets.QLabel(winForm)
        self.pythonLabel.setGeometry(QtCore.QRect(10, 20, 91, 91))
        self.pythonLabel.setText("")
        self.pythonLabel.setPixmap(QtGui.QPixmap(":/pics/source/pics/python-96.png"))
        self.pythonLabel.setObjectName("pythonLabel")
        self.GolangLabel = QtWidgets.QLabel(winForm)
        self.GolangLabel.setGeometry(QtCore.QRect(130, 10, 101, 101))
        self.GolangLabel.setText("")
        self.GolangLabel.setPixmap(QtGui.QPixmap(":/pics/source/pics/golang-96.png"))
        self.GolangLabel.setObjectName("GolangLabel")
        self.JSLabel = QtWidgets.QLabel(winForm)
        self.JSLabel.setGeometry(QtCore.QRect(260, 20, 101, 91))
        self.JSLabel.setText("")
        self.JSLabel.setPixmap(QtGui.QPixmap(":/pics/source/pics/javascript-96.png"))
        self.JSLabel.setObjectName("JSLabel")
        self.CLabel = QtWidgets.QLabel(winForm)
        self.CLabel.setGeometry(QtCore.QRect(390, 20, 91, 91))
        self.CLabel.setText("")
        self.CLabel.setPixmap(QtGui.QPixmap(":/pics/source/pics/c-96.png"))
        self.CLabel.setObjectName("CLabel")
        self.horizontalLayoutWidget = QtWidgets.QWidget(winForm)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 130, 471, 71))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pythonButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/pics/source/pics/python-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pythonButton.setIcon(icon)
        self.pythonButton.setObjectName("pythonButton")
        self.horizontalLayout.addWidget(self.pythonButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.golangButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/pics/source/pics/golang-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.golangButton.setIcon(icon1)
        self.golangButton.setObjectName("golangButton")
        self.horizontalLayout.addWidget(self.golangButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.javascriptButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/pics/source/pics/javascript-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.javascriptButton.setIcon(icon2)
        self.javascriptButton.setObjectName("javascriptButton")
        self.horizontalLayout.addWidget(self.javascriptButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.cButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/pics/source/pics/c-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cButton.setIcon(icon3)
        self.cButton.setObjectName("cButton")
        self.horizontalLayout.addWidget(self.cButton)

        self.retranslateUi(winForm)
        QtCore.QMetaObject.connectSlotsByName(winForm)

    def retranslateUi(self, winForm):
        _translate = QtCore.QCoreApplication.translate
        winForm.setWindowTitle(_translate("winForm", "Form"))
        self.pythonButton.setText(_translate("winForm", "python"))
        self.golangButton.setText(_translate("winForm", "golang"))
        self.javascriptButton.setText(_translate("winForm", "javascript"))
        self.cButton.setText(_translate("winForm", "c"))


import apprcc_rc
