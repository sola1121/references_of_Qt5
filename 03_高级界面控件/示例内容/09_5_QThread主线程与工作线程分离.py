import sys

from PyQt5.QtCore import QTimer, QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLCDNumber, QPushButton


global sec
sec = 0


class WorkThread(QThread):
    """工作线程"""

    finish_signal = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)

        def run(self):
            for i in range(2e16):   # 耗时操作, 放入线程中
                pass

            # 循环完成后触发自定义的事件
            self.finish_signal.emit()


def countTime():
    global sec
    sec += 1
    # LED显示数字
    lcd_number.display(sec)


def work():
    # 计时器每秒计数
    timer.start(1000)
    # 开始线程 计时开始
    work_thread.start()
    work_thread.finish_signal.connect(timeStop)


def timeStop():
    # 关闭计时器
    timer.stop()
    print("运行结束用时", lcd_number.value())
    # 重设全局时间
    global sec
    sec = 0


if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = QWidget()
    win.resize(300, 120)

    lcd_number = QLCDNumber()
    button = QPushButton("测试启用线程")
    button.clicked.connect(work)   # 点击开始计时器, 开始工作线程

    layout = QVBoxLayout()
    layout.addWidget(lcd_number)
    layout.addWidget(button)
    win.setLayout(layout)

    timer = QTimer()
    timer.timeout.connect(countTime)   # 计时器时间间隔触发, 刷新led时间
    work_thread = WorkThread()

    win.show()
    sys.exit(app.exec())
