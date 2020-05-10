import sys

from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView


class MainWin(QMainWindow):
    """主窗口"""
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle("QWebEngineView 加载本地页面")

        file_path = "03_高级界面控件/示例内容/sources/htmls/localhtml.html"
        with open(file_path, 'r') as file:
            self.browser = QWebEngineView()
            self.browser.setHtml(file.read())

        self.setCentralWidget(self.browser)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = MainWin()
    win.show()
    sys.exit(app.exec_())