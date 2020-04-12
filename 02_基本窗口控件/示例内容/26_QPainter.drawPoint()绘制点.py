import sys
import math

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QApplication, QWidget


class DrawPoint(QWidget):
    """主窗口"""
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle("QPainter 使用drawPoints()")
        self.resize(300, 200)

    def paintEvent(self, QPaintEvent):
        """重载QWidget.paintEvent"""
        painter = QPainter()
        painter.begin(self)
        self.to_draw_points(painter)
        painter.end()

    def to_draw_points(self, painter):
        painter.setPen(Qt.red)
        size = self.size()   # 获取当前窗口的大小

        for i in range(1000):
            # 绘制正选函数图形, 周期[-100, 100]
            x = 100 * (-1+2.0*i/1000) + size.width()/2.0
            y = -50*math.sin((x-size.width()/2.0)*math.pi/50) + size.height()/2.0
            painter.drawPoint(x, y)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = DrawPoint()
    win.show()
    sys.exit(app.exec())