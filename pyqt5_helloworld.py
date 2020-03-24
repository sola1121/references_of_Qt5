import sys
from PyQt5.QtWidgets import QWidget, QApplication

class WinForm(QWidget):
    def __init__(self, parent=None,):
        super().__init__(parent=parent)
        self.setGeometry(300, 300, 350, 350)
        self.setWindowTitle("Hello, world.")

if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = WinForm()
    win.show()
    sys.exit(app.exec_())
