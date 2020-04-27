import sys

from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout


app = QApplication(sys.argv)
win = QWidget()
win.setWindowFlags(Qt.SplashScreen|Qt.FramelessWindowHint)   # 模仿开机画面, 程序设置为无边框

hbox = QHBoxLayout()
hbox.addWidget(QLabel("<h2 style='font-size: 128; color: red; background-color: yellow'>窗口在10s后关闭.</h2>"))
win.setLayout(hbox)

timer = QTimer()
timer.singleShot(10000, app.exit)   # 计时器单次触发, 与退出事件绑定

win.show()
sys.exit(app.exec())