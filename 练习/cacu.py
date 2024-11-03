import sys

from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton, QLineEdit, QLabel


class MainWin(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("加法计算器")
        self.resize(600, 400)

        self.num_edit1 = QLineEdit()
        self.num_edit2 = QLineEdit()
        self.ret_label = QLabel()
        self.ret_label.setText("还未计算.")

        but = QPushButton()
        but.setText("计算")
        but.clicked.connect(self.add)   # 连接信号

        self.layout = QHBoxLayout()
        self.layout.addWidget(self.num_edit1)
        self.layout.addSpacing(4)
        self.layout.addWidget(self.num_edit2)
        self.layout.addSpacing(4)
        self.layout.addWidget(self.ret_label)
        self.layout.addSpacing(4)
        self.layout.addWidget(but)

        self.setLayout(self.layout)

    def add(self):
        if (self.num_edit1.text()=='') or (self.num_edit2.text()==''):
            self.ret_label.setText("无计算内容.")
        else:
            ret = int(self.num_edit1.text()) + int(self.num_edit2.text())
            self.ret_label.setText(str(ret))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWin()
    main.show()
    sys.exit(app.exec())