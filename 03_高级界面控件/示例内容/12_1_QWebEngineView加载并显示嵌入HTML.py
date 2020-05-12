import sys

from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication, QMainWindow


class MainWin(QMainWindow):
    """主窗口"""
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle("QWebEngineView 嵌入HTML")

        self.browser = QWebEngineView()
        self.browser.setHtml("""\
        <!DOCTYPE html>
        <html>
            <head>
                <meta charset="utf-8">
                <title>标题</title>
            </head>
            <body>
                <h3>标题 3</h3>
                <div>Lorem ipsum dolor sit amet consectetur adipisicing elit. Ab perferendis eveniet consequatur quae. 
                    Voluptatum ipsam facere pariatur rem, dolor eveniet, distinctio dolorem, eum aperiam nisi reiciendis ducimus maiores vero amet?
                </div>
            </body>
        </html>
        """)
        self.setCentralWidget(self.browser)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = MainWin()
    win.show()
    sys.exit(app.exec())

