import sys

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget


class MyThread(QThread):
    """自定义线程"""
    sinOut = pyqtSignal(str)   # 一个可以发送str的信号 

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.identity = None

    def setIdentity(self, text):
        self.identity = text

    def setValue(self, val):
        self.times = int(val)
        # 执行线程的方法
        self.start()

    def run(self):
        """重载run, 可以通过 start()启动"""
        while self.times>0 and self.identity:
            # 发射信号
            self.sinOut.emit(self.identity + " ==> " + str(self.times))
            self.times -= 1


class WinForm(QWidget):
    """主窗口"""
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        # 创建一个线程实例并设置名称, 变量, 信号与槽
        self.thread = MyThread()
        self.thread.setIdentity("th_1")
        self.thread.sinOut.connect(self.outText)
        self.thread.setValue(8)

    def outText(self, text):
        print(text)