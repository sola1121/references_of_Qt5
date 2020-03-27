import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

from firstWindow import Ui_MainWindow


class firstWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = firstWindow()
    win.show()
    sys.exit(app.exec_())