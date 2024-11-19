import sys

from PySide6.QtWidgets import QApplication

from windows import Ui_MainWindow


if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = Ui_MainWindow()
    win.show()
    sys.exit(app.exec())
