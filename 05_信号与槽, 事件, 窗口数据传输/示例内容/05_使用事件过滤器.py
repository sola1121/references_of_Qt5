import sys

from PyQt5.QtGui import QImage, QPixmap, QMouseEvent, QTransform
from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QGridLayout


class EventFilter(QDialog):
    """主窗口"""
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle("使用事件过滤器")

        self.label_1 = QLabel("请点击")
        self.label_2 = QLabel("请点击")
        self.label_3 = QLabel("请点击")
        self.label_state = QLabel("test")

        self.image_1 = QImage("05_信号与槽, 事件, 窗口数据传输/示例内容/sources/python-color-128.png")
        self.image_2 = QImage("05_信号与槽, 事件, 窗口数据传输/示例内容/sources/python-color-128.png")
        self.image_3 = QImage("05_信号与槽, 事件, 窗口数据传输/示例内容/sources/python-color-128.png")

        self.width = 600; self.height = 300
        self.resize(self.width, self.height)

        self.label_1.installEventFilter(self)
        self.label_2.installEventFilter(self)
        self.label_3.installEventFilter(self)

        grid_layout = QGridLayout()
        grid_layout.addWidget(self.label_1, 500, 0)
        grid_layout.addWidget(self.label_2, 500, 1)
        grid_layout.addWidget(self.label_3, 500, 2)
        grid_layout.addWidget(self.label_state, 600, 1)
        self.setLayout(grid_layout)

    def eventFilter(self, qobject, qevent):
        """重载eventFilter事件过滤器"""
        if qobject == self.label_1:   # 只对label_1的点击事件进行过滤, 重写其行为, 其他事件会忽略 
            if qevent.type() == QEvent.MouseButtonPress:   # 对鼠标按下事件进行过滤, 重写其行为
                event_mouse = QMouseEvent(qevent)
                if event_mouse.buttons() == Qt.LeftToolBarArea:
                    self.label_state.setText("按下鼠标左键")
                elif event_mouse.buttons() == Qt.MidButton:
                    self.label_state.setText("按下鼠标中键")
                elif event_mouse.buttons() == Qt.RightButton:
                    self.label_state.setText("按下鼠标右键")

                # 转换图片大小
                transform = QTransform()
                transform.scale(0.5, 0.5)
                temp = self.image_1.transformed(transform)
                self.label_1.setPixmap(QPixmap.fromImage(temp))
            
            if qevent.type() == QEvent.MouseButtonRelease:   # 这里对鼠标释放事件进行过滤, 重写其行为
                self.label_state.setText("释放鼠标按键")
                self.label_1.setPixmap(QPixmap.fromImage(self.image_1))

        return QDialog.eventFilter(self, qobject, qevent)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = EventFilter()
    win.show()
    sys.exit(app.exec())