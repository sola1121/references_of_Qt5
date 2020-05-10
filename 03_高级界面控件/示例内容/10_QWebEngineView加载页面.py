import sys

from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView


class MainWin(QMainWindow):
    """主窗口"""
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle("QWebEngineView 使用")
        
        self.browser = QWebEngineView()
        self.browser.load(QUrl("https://www.bilibili.com"))

        self.setCentralWidget(self.browser)
    

if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = MainWin()
    win.show()
    sys.exit(app.exec())
