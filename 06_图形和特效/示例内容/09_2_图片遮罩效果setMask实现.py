import sys

from PyQt5.QtGui import QPixmap, QPainter, QBitmap
from PyQt5.QtWidgets import QApplication, QWidget


class WinForm(QWidget):
    """主窗口"""
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle("不规则窗口的实现")

        self.pix = QBitmap("06_图形和特效/示例内容/sources/golang.png")
        self.resize(self.pix.size())   # 设置窗口为图片大小
        self.setMask(self.pix)

    def paintEvent(self, event):
        painter = QPainter(self)
        # 在指定区域直接绘制窗口背景
        painter.drawPixmap(0, 0, self.pix.width(), self.pix.height(), 
                QPixmap("06_图形和特效/示例内容/sources/python-color-128.png"))


if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = WinForm()
    win.show()
    sys.exit(app.exec())