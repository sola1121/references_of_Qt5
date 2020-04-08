import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QSlider


class SliderDemo(QWidget):
    """主窗口"""
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle("QSlider 使用")
        self.resize(320, -1)

        vbox = QVBoxLayout()
        self.label = QLabel()
        vbox.addWidget(self.label)
        vbox.addStretch(1)

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0, 50)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.setTickInterval(5)
        self.slider.valueChanged.connect(self.info_slider)

        vbox.addWidget(self.slider)

        self.setLayout(vbox)

    def info_slider(self, value):
        self.label.setText(str(value))


if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = SliderDemo()
    win.show()
    sys.exit(app.exec())