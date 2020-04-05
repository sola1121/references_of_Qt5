import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon


class MainWin(QMainWindow):
    """主窗口"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("PyQt主窗口")   # 设置主窗口标题
        self.resize(400, 200)   # 设置窗口大小
        self.status = self.statusBar()   # 获取状态栏
        self.status.showMessage("状态栏的提示", 5000)   # 设置状态栏显示信息


if __name__ == "__main__":

    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("02_基本窗口控件/示例内容/sources/icons/android_01.ico"))   # 设置窗口图标
    win = MainWin()
    win.show()
    sys.exit(app.exec())
