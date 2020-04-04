import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget


class MainWin(QMainWindow):
    """主窗口"""
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle("PyQt主窗口居中显示")
        self.resize(400, 200)
        # 运行居中
        self.center()

    def center(self):
        """
        通过获得系统桌面大小, 扣除应用窗口的大小, 在除以2以求得居中位置. 定位点在窗口左上角.
        """
        screen = QDesktopWidget().screenGeometry()   # 返回系统桌面的QRect对象
        size = self.geometry()   # 返回主窗口大小的QRect对象
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)   # 移动到指定位置


if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = MainWin()
    win.show()
    sys.exit(app.exec())
