import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

from container_example import Ui_MainWindow


class ContainerWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = ContainerWindow()
    win.show()
    sys.exit(app.exec_())
