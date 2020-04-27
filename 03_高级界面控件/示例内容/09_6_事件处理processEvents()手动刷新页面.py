import sys, time

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QListWidget, QGridLayout


class WinForm(QWidget):
    """主窗口"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("processEvents 使用")

        self.list_file = QListWidget()
        self.button_start = QPushButton("开始")
        
        grid_layout = QGridLayout()
        grid_layout.addWidget(self.list_file, 0, 0, 1, 2)   # 0行0列, 占1行, 占2列
        grid_layout.addWidget(self.button_start, 1, 1)   # 1行1列
        self.setLayout(grid_layout)

        self.button_start.clicked.connect(self.slot_add)
    
    def slot_add(self):
        for n in range(10):
            str_n = "file index{}".format(n)
            self.list_file.addItem(str_n)
            QApplication.processEvents()
            time.sleep(2)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = WinForm()
    win.show()
    sys.exit(app.exec())