import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QApplication, QLabel, QWidget


class GifWin(QWidget):
    """主窗口"""
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowFlags(Qt.Dialog | Qt.CustomizeWindowHint)

        self.movie = QMovie("06_图形和特效/示例内容/sources/dancing.gif")
        self.label = QLabel("", parent=self)
        self.label.setMovie(self.movie)
        self.movie.start()

        self.resize(400, 400)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = GifWin()
    win.show()
    sys.exit(app.exec())
    