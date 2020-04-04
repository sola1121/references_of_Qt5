# coding: utf-8

import sys

from PyQt5.QtWidgets import QApplication, QWidget, QToolTip
from PyQt5.QtGui import QFont


class WinForm(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.initUi()

    def initUi(self):
        QToolTip.setFont(QFont("SansSerif", 10))
        self.setToolTip("这是一个<b>气泡提示</b>")
        self.setGeometry(200, 300, 400, 400)
        self.setWindowTitle("会有气泡提示")


if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    win = WinForm()
    win.show()
    sys.exit(app.exec())