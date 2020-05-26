import sys

import qdarkstyle
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow


app = QApplication(sys.argv)
win = QMainWindow()

app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())   # 指定使用pyqt5的

win.show()
sys.exit(app.exec())