import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QBrush
from PyQt5.QtWidgets import QApplication, QWidget


class DrawBrush(QWidget):
    """主窗口"""
    def __init__(self, parent=None):
        super().__init__(parent=None)
        self.setWindowTitle("QBrush 使用")
        self.resize(365, 280)

    def paintEvent(self, QPaintEvent):
        painter = QPainter()
        painter.begin(self)
        self.to_draw_lines(painter)
        painter.end()

    def to_draw_lines(self, painter):
        # 初始化刷子, 使用实心刷子
        brush = QBrush(Qt.SolidPattern)
        painter.setBrush(brush)
        painter.drawRect(10, 15, 90, 60)

        brush = QBrush(Qt.Dense1Pattern)
        painter.setBrush(brush)
        painter.drawRect(130, 15, 90, 60)

        brush = QBrush(Qt.Dense2Pattern)
        painter.setBrush(brush)
        painter.drawRect(250, 15, 90, 60)

        brush = QBrush(Qt.Dense3Pattern)
        painter.setBrush(brush)
        painter.drawRect(10, 105, 90, 60)

        brush = QBrush(Qt.DiagCrossPattern)
        painter.setBrush(brush)
        painter.drawRect(10, 105, 90, 60)

        brush = QBrush(Qt.Dense5Pattern)
        painter.setBrush(brush)
        painter.drawRect(130, 105, 90, 60)

        brush = QBrush(Qt.Dense6Pattern)
        painter.setBrush(brush)
        painter.drawRect(250, 105, 90, 60)

        brush = QBrush(Qt.HorPattern)
        painter.setBrush(brush)
        painter.drawRect(10, 195, 90, 60)

        brush = QBrush(Qt.VerPattern)
        painter.setBrush(brush)
        painter.drawRect(130, 195, 90, 60)

        brush = QBrush(Qt.BDiagPattern)
        painter.setBrush(brush)
        painter.drawRect(250, 195, 90, 60)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = DrawBrush()
    win.show()
    sys.exit(app.exec())