import sys

from PyQt5.QtCore import QTimer, QDateTime
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QListWidget, QLabel, QGridLayout


class WinForm(QWidget):
    """主窗口"""
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle("QTimer 使用")
        
        self.label_time = QLabel("显示当前时间")
        self.button_start = QPushButton("开始")
        self.button_end = QPushButton("结束")

        grid_layout = QGridLayout()

        # 初始化一个定时器
        self.timer = QTimer()
        # show_time() 方法
        self.timer.timeout.connect(self.show_time)

        grid_layout.addWidget(self.label_time, 0, 0, 1, 2)   # 0行0列, 占用行1, 占用列2
        grid_layout.addWidget(self.button_start, 1, 0)   # 1行0列
        grid_layout.addWidget(self.button_end, 1, 1)   # 1行1列
        self.setLayout(grid_layout)

        self.button_start.clicked.connect(self.start_timer)
        self.button_end.clicked.connect(self.end_timer)

    def show_time(self):
        # 获取当前系统时间
        date_time = QDateTime.currentDateTime()
        date_time_format = date_time.toString("yyyy-MM-dd hh:mm:ss dddd")
        self.label_time.setText(date_time_format)   # 表现在标签上

    def start_timer(self):
        # 设置时间间隔并启动定时器
        self.timer.start(1000)

        self.button_start.setEnabled(False)
        self.button_end.setEnabled(True)

    def end_timer(self):
        # 停止定时器
        self.timer.stop()

        self.button_start.setEnabled(True)
        self.button_end.setEnabled(False)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = WinForm()
    win.show()
    sys.exit(app.exec())