import sys
from datetime import datetime

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QStatusBar


class MainWin(QMainWindow):
    """主窗口"""
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle("QStatusBar 使用")
        self.resize(320, 200)

        self.textedit = QTextEdit(parent=self)
        self.textedit.setAlignment(Qt.AlignLeft)
        self.textedit.textChanged.connect(lambda : self.text_change(self.textedit.toPlainText()))

        self.setCentralWidget(self.textedit)

        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)

    def text_change(self, text):
        text_len = len(text)
        dt_desc = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        format_info = f"{dt_desc}   字段: {text_len}"
        self.status_bar.showMessage(format_info)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = MainWin()
    win.show()
    sys.exit(app.exec())