import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel

class WinForm(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.resize(200, 100)
        buton = QLabel("Hello, world.", parent=self)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = WinForm()
    win.show()
    sys.exit(app.exec_())
