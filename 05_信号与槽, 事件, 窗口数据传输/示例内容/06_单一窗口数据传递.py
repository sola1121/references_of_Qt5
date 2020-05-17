import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSlider, QLCDNumber


class WinForm(QWidget):
    """主窗口"""
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle("信号与槽, 连接滑块和lcd")
        self.resize(400, 200)

        lcd_number = QLCDNumber(parent=self)
        slider = QSlider(Qt.Horizontal, parent=self)
        slider.valueChanged.connect(lcd_number.display)   # 通过信号连接lcd的display()方法

        v_layout = QVBoxLayout()
        v_layout.addWidget(lcd_number)
        v_layout.addWidget(slider)
        self.setLayout(v_layout)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = WinForm()
    win.show()
    sys.exit(app.exec_())