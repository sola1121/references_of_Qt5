import sys

from PyQt5.QtCore import QTimer, QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLCDNumber, QPushButton


global sec
sec = 0

def setTime():
    global sec
    sec += 1
    # LED 显示数字
    lcd_number.display(sec)


def work():
    # 计时器每秒计数
    timer.start(1000)   # 设置timer的间隔1s
    for i in range(int(2e100)):   # 会造成主线程卡死, 解决之道就是将主线程和计算线程分离 
        pass

    timer.stop()


if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = QWidget()
    win.resize(300, 120)

    # 添加一个显示面板
    lcd_number = QLCDNumber()
    button = QPushButton("测试")

    layout = QVBoxLayout()
    layout.addWidget(lcd_number)
    layout.addWidget(button)
    win.setLayout(layout)

    timer = QTimer()
    # 每次计时结束, 触发setTime
    timer.timeout.connect(setTime)
    button.clicked.connect(work)

    win.show()
    sys.exit(app.exec())