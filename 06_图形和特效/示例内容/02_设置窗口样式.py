import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow


class MainWin(QMainWindow):
    """主窗口"""
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle("设置窗口样式")
        self.resize(200, 100)

        # 设置无边框窗口样式
        self.setWindowFlags(Qt.WindowSystemMenuHint | Qt.WindowCloseButtonHint)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = MainWin()
    win.show()
    sys.exit(app.exec())
