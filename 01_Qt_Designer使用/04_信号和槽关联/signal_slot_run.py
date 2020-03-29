import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from signal_slot_win import Ui_Form


class SignalSlotWin(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = SignalSlotWin()
    win.show()
    sys.exit(app.exec_())
