import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPainter, QCursor
from PyQt5.QtWidgets import QApplication, QWidget


class ShapeWidget(QWidget):
    """主窗口"""
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle("不规则的可以拖动的窗口")
        
        self.set_pic()

    def set_pic(self):
        self.pic_path = "06_图形和特效/示例内容/sources/golang.png"
        self.pic = QPixmap(self.pic_path, '0', Qt.AvoidDither | Qt.ThresholdAlphaDither | Qt.ThresholdAlphaDither)
        self.resize(self.pic.size())
        self.setMask(self.pic.mask())
        self.drag_position = None

    def mousePressEvent(self, event):
        """重载鼠标按键按下事件, 使不规则窗口能响应鼠标事件, 随意拖动窗口"""
        if event.button() == Qt.LeftButton:
            self.m_drag = True
            self.m_drag_position = event.globalPos()-self.pos()
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))

    def mouseDoubleClickEvent(self, event):
        """重载鼠标双击事件"""
        self.set_pic()

    def mouseMoveEvent(self, event):
        """重载鼠标移动事件"""
        if Qt.LeftButton and self.m_drag:
            # 当使用左键移动窗口时修改偏移值
            self.move(event.globalPos()-self.m_drag_position)
            event.accept()

    def mouseReleaseEvent(self, event):
        """重载鼠标按键释放事件"""
        self.m_drag = False
        self.setCursor(QCursor(Qt.ArrowCursor))

    def paintEvent(self, event):
        """重载窗口绘制"""
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.pic.width(), self.pic.height(), self.pic)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = ShapeWidget()
    win.show()
    sys.exit(app.exec())