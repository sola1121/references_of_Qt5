# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signal_slot_win.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(150, 250, 80, 26))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 10, 371, 221))
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "关闭窗口"))
        self.label.setText(_translate("Form", "<html><head/><body><p>由pushButton发出信号 -&gt; Form(窗体)的槽, 对象做出反应关闭.</p><p><br/></p><p>可以直接使用 信号/槽编辑器 添加对象的信号事件-&gt;对象的槽事件. </p><p><br/></p><p>也可以在菜单栏中点击 Edit -&gt; 编辑信号/槽 进行可视化的编辑,</p><p>只需要连线两个协作对象并定义其信号事件和槽事件就可以.</p></body></html>"))
