import sys

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QFontDialog


class FontDialogDemo(QWidget):
    """主窗口"""
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle("QFontDialog 使用")
        self.resize(320, 200)

        self.label = QLabel()
        self.label.setText("Hello, World. 我能生吞玻璃而不伤到身体.")

        self.btn = QPushButton()
        self.btn.setText("设置字体")
        self.btn.clicked.connect(self.change_font)

        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(self.btn)

        self.setLayout(vbox)

    def change_font(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.label.setFont(font)


if __name__ == "__main__":

    app = QApplication(sys.argv)            
    win = FontDialogDemo()
    win.show()
    sys.exit(app.exec())
