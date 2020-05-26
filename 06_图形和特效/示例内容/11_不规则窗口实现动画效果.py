import sys

from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPixmap, QPainter, QCursor
from PyQt5.QtWidgets import QApplication, QWidget


class ShapeWidget(QWidget):
    """主窗口"""
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.i = 1
        self.my_pix()
        self.timer = QTimer()
        self.timer.setInterval(1500)   # 定时器每1500ms更新一次
        self.timer.timeout.connect(self.time_change)
        self.timer.start()

    def my_pix(self):
        """显示不规则图片"""
        self.update()

        if self.i == 5:
            self.i = 1
        self.my_pic = {
            1: "06_图形和特效/示例内容/sources/arrows/arrow-left-48.png",
            2: "06_图形和特效/示例内容/sources/arrows/arrow-up-48.png",
            3: "06_图形和特效/示例内容/sources/arrows/arrow-right-48.png",
            4: "06_图形和特效/示例内容/sources/arrows/arrow-down-48.png"
        }
        self.pix = QPixmap(self.my_pic[self.i], "0", Qt.AvoidDither | Qt.ThresholdDither | Qt.ThresholdAlphaDither)
        self.resize(self.pix.size())
        self.dragPosition = None

    def mousePressEvent(self, event):
        """重载鼠标点击事件"""
        if event.button() == Qt.LeftButton:
            self.m_drag = True
            self.m_dragPositon = event.globalPos()-self.pos()
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))

    def mouseMoveEvent(self, event):
        """重载鼠标移动事件"""
        if Qt.LeftButton and self.m_drag:
            self.move(event.globalPos()-self.m_dragPositon)
            event.accept()

    def mouseReleaseEvent(self, event):
        """重载鼠标释放事件"""
        self.m_drag = False
        self.setCursor(QCursor(Qt.ArrowCursor))

    def mouseDoubleClickEvent(self, event):
        """鼠标双击事件"""
        if event.button() == 1:
            self.i += 1
            self.my_pix()

    def paintEvent(self, event):
        """绘画事件"""
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.pix.width(), self.pix.height(), self.pix)

    def time_change(self):
        """每1500ms窗口执行一次更新操作, 重绘窗口"""
        self.i += 1
        self.my_pix()


if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = ShapeWidget()
    win.show()
    sys.exit(app.exec())