import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

from layout_example import Ui_MainWindow


class LayoutWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = LayoutWindow()
    win.show()
    sys.exit(app.exec_())