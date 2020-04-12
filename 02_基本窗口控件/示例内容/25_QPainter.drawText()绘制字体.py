import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtWidgets import QApplication, QWidget


class DrawFont(QWidget):
    """主窗口"""
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle("QPainter 使用drawFont")
        self.resize(420, 300)
    
    def paintEvent(self, QPaintEvent):
        # 重载QWidget.paintEvent
        painter = QPainter(self)
        painter.begin(self)
        # 自定义绘制方法
        self.to_draw_text(QPaintEvent, painter)
        painter.end()

    def to_draw_text(self, event, painter):
        # 设置字体
        painter.setFont(QFont("monospace", 20))
        # 设置画笔的颜色
        painter.setPen(Qt.red)   # 使用QColor自定义也可以
        # 绘制文字
        painter.drawText(event.rect(), Qt.AlignCenter, "你是个憨憨. hello, world.")


if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = DrawFont()
    win.show()
    sys.exit(app.exec())