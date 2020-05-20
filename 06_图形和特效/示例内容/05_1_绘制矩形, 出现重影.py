import sys

from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QPixmap
from PyQt5.QtWidgets import QApplication, QWidget

"""
在拖动鼠标的过程中, 屏幕已经刷新了很多次, 也可以理解为paintEvent()函数执行了多次, 每执行一次就会绘制一个矩形.
从而出现重影
"""

class WinForm(QWidget):
    """主窗口"""
    def __init__(self, parent=None):
        super().__init__(parent=None)
        self.setWindowTitle("绘制矩形, 有重影")
        self.resize(600, 500)

        self.pix = QPixmap(400, 400)
        self.pix.fill(Qt.white)
        self.last_point = QPoint()
        self.end_point = QPoint()

    def paintEvent(self, event):
        """重载绘制对象"""
        painter = QPainter(self)
        x = self.last_point.x()
        y = self.last_point.y()
        w = self.end_point.x() - x
        h = self.end_point.y() - y

        paint_pix = QPainter(self.pix)
        paint_pix.drawRect(x, y, w, h)
        painter.drawPixmap(0, 0, self.pix)

    def mousePressEvent(self, event):
        """重载鼠标按键按下事件"""
        if event.button() == Qt.LeftButton:
            self.last_point = event.pos()
            self.end_point = self.last_point

    def mouseMoveEvent(self, event):
        """重载鼠标移动事件"""
        if event.buttons() and Qt.LeftButton:
            self.end_point = event.pos()
            # 进行重新绘制
            self.update()

    def mouseReleaseEvent(self, event):
        """重载鼠标按键释放事件"""
        if event.button() == Qt.LeftButton:
            self.end_point = event.pos()
            # 进行重新绘制
            self.update()


if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = WinForm()
    win.show()
    sys.exit(app.exec())