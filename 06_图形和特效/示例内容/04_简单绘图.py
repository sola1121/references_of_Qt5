import sys

from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QPixmap
from PyQt5.QtWidgets import QApplication, QWidget


class WinForm(QWidget):
    """主窗口"""
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle("绘图例子")
        self.resize(600, 500)

        # 初始化
        self.pix = QPixmap(400, 400)
        self.pix.fill(Qt.white)
        self.last_point = QPoint()
        self.end_point = QPoint()
    
    def paintEvent(self, event):
        """重载绘制函数"""
        painter_pix = QPainter(self.pix)
        # 根据鼠标指针前后两个位置绘制直线
        painter_pix.drawLine(self.last_point, self.end_point)
        # 让前一个坐标值等于后一个坐标值, 就能画出连续的线
        self.last_point = self.end_point
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.pix)

    def mousePressEvent(self, event):
        """重载鼠标按键按下事件"""
        if event.button() == Qt.LeftButton:   # 事件由鼠标左键发起
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
            # 重新绘制
            self.update()


if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = WinForm()
    win.show()
    sys.exit(app.exec())
