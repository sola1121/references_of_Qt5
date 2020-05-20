import sys

from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QPixmap
from PyQt5.QtWidgets import QApplication, QWidget

"""
要实现使用鼠标在界面上绘制一个任意到校的矩形而不出现重影, 需要两个画布, 它们都是QPixmap实例,
其中temp_pix作为临时缓冲区, 当拖动鼠标绘制矩形时, 将内容先绘制到temp_pix上, 然后再将temp_pix
绘制到界面上; pix作为缓冲区, 用来保存已经完成的绘制. 当释放鼠标按键完成矩形的绘制后, 则将temp_pix
的内容复制到pix上. 为了在绘制时不出现重影, 而且保证以前绘制的内容不消失, 那么每一次绘制都是在原来的
图形上进行的, 所以需要在绘制temp_pix之前, 先将pix的内容复制到temp_pix上. 因为这里有两个QPixmap对象,
也可以说有两个缓冲区, 所以称之为"双缓冲绘图.
"""

class WinForm(QWidget):
    """主窗口"""
    def __init__(self, parent=None):
        super().__init__(parent=None)
        self.setWindowTitle("绘制矩形, 双缓冲例子")
        self.resize(600, 500)

        self.pix = QPixmap(400, 400)
        self.pix.fill(Qt.white)
        self.last_point = QPoint()
        self.end_point = QPoint()
        # 辅助画布
        self.temp_pix = QPixmap()
        # 标志是否正在绘图
        self.is_drawing = False

    def paintEvent(self, event):
        """重载绘制对象"""
        painter = QPainter(self)
        x = self.last_point.x()
        y = self.last_point.y()
        w = self.end_point.x() - x
        h = self.end_point.y() - y

        # 如果正在绘图
        if self.is_drawing:
            # 将以前pix中的内容复制到temp_pix中, 保证以前的内容不消失
            self.temp_pix = self.pix
            paint_pix = QPainter(self.temp_pix)
            paint_pix.drawRect(x, y, w, h)
            painter.drawPixmap(0, 0, self.temp_pix)
        else:
            paint_pix = QPainter(self.pix)
            paint_pix.drawPixmap(0, 0, self.pix)
            painter.drawPixmap(0, 0, self.pix)

    def mousePressEvent(self, event):
        """重载鼠标按键按下事件"""
        if event.button() == Qt.LeftButton:
            self.last_point = event.pos()
            self.end_point = self.last_point
            self.is_drawing = True

    def mouseReleaseEvent(self, event):
        """重载鼠标按键释放事件"""
        if event.button() == Qt.LeftButton:
            self.end_point = event.pos()
            # 进行重新绘制
            self.update()
            self.is_drawing = False


if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = WinForm()
    win.show()
    sys.exit(app.exec())