import sys

from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget, QLabel


if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = QWidget()
    win.resize(512, 480)
    vbox = QVBoxLayout()
    img = QPixmap("02_基本窗口控件/示例内容/sources/images/python-simple-color-96.png")
    label = QLabel()
    label.setPixmap(img)
    vbox.addWidget(label)
    win.setLayout(vbox)
    win.show()
    sys.exit(app.exec())
    