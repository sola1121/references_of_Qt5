import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow


class MainWin(QMainWindow):
    """主窗口"""
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        # 设置窗口标志, 无边框
        self.setWindowFlags(Qt.FramelessWindowHint)
        # 为了便于显示, 设置窗口背景颜色, 使用QSS
        self.setStyleSheet("""background-color: green;""")

        # 获取桌面控件QDesktopWidget
        desktop = QApplication.desktop()
        # 获取桌面可用尺寸QRect
        rect = desktop.availableGeometry()
        # 设置当前窗口尺寸
        self.setGeometry(rect)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = MainWin()
    win.show()
    sys.exit(app.exec())
