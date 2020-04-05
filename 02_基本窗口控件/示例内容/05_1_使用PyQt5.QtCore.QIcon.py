# coding: utf-8

import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QDesktopWidget
from PyQt5.QtGui import QIcon, QPixmap


app = QApplication(sys.argv)

screen = QDesktopWidget().screenGeometry()

win = QWidget()

win.setWindowTitle("PyQt5 窗口")
# 设置窗口坐标和大小
# win.setGeometry(150, 100, 400, 300)
win.move((screen.width()-win.width())//2, (screen.height()-win.height())//2)
win.resize(300, 200)

# 按钮
btn = QPushButton(parent=win)
btn.setGeometry(150, 100, 100, 50)
btn.setText("按钮")

# 设置程序图标
win.setWindowIcon(QIcon("02_基本窗口控件/示例内容/sources/images/python-simple-color-96.png"))
btn.setIcon(QIcon("02_基本窗口控件/示例内容/sources/icons/android_01.ico"))


win.show()

sys.exit(app.exec())
