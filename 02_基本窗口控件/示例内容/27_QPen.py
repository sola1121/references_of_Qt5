import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPen, QPainter
from PyQt5.QtWidgets import QApplication, QWidget


class DrawPen(QWidget):
    """主窗口"""
    def  __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle("QPen 使用")
        self.resize(420, 300)

    def paintEvent(self, QPaintEvent):
        painter = QPainter()
        painter.begin(self)
        self.to_draw_lines(painter)
        painter.end()

    def to_draw_lines(self, painter):
        # 初始化, 使用实线
        pen = QPen(Qt.black, 2.0, Qt.SolidLine)
        painter.setPen(pen)
        painter.drawLine(20, 40, 250, 40)

        pen.setStyle(Qt.DashLine)
        painter.setPen(pen)
        painter.drawLine(20, 80, 250, 80)

        pen.setStyle(Qt.DashDotLine)
        painter.setPen(pen)
        painter.drawLine(20, 120, 250, 120)

        pen.setStyle(Qt.DotLine)
        painter.setPen(pen)
        painter.drawLine(20, 160, 250, 160)

        pen.setStyle(Qt.DashDotDotLine)
        painter.setPen(pen)
        painter.drawLine(20, 200, 250, 200)

        pen.setStyle(Qt.CustomDashLine)
        painter.setPen(pen)
        painter.drawLine(20, 240, 250, 240)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = DrawPen()
    win.show()
    sys.exit(app.exec())
