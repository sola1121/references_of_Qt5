import sys

from PyQt5.QtGui import QPixmap, QPainter, QBitmap
from PyQt5.QtWidgets import QApplication, QWidget


class WinForm(QWidget):
    """主窗口"""
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle("不规则窗口的实现例子")

    def paintEvent(self, event):
        """重载绘制"""
        painter = QPainter(self)
        painter.drawPixmap(0, 0, 280, 390, QPixmap("06_图形和特效/示例内容/sources/golang.png"))
        painter.drawPixmap(300, 0, 280, 390, QBitmap("06_图形和特效/示例内容/sources/golang.png"))


if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = WinForm()
    win.show()
    sys.exit(app.exec())
