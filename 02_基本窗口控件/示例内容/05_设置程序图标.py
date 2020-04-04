# coding: utf-8

import sys

from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget
from PyQt5.QtGui import QIcon, QPixmap


app = QApplication(sys.argv)

screen = QDesktopWidget().screenGeometry()

win = QWidget()

win.setWindowTitle("PyQt5 窗口")
# 设置窗口坐标和大小
# win.setGeometry(150, 100, 400, 300)
win.move((screen.width()-win.width())//2, (screen.height()-win.height())//2)
win.resize(300, 200)

# 设置程序图标
win.setWindowIcon(QIcon("./sources/images/python-colot-96.png"))

win.show()

sys.exit(app.exec())
