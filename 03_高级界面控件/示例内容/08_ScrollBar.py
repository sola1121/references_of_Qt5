import sys

from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import QApplication, QWidget, QScrollBar, QHBoxLayout, QLabel


class ScrollDemo(QWidget):
    """主窗口"""
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle("QScrollBar 使用")

        self.label = QLabel("拖动滑块改变颜色")

        self.scroll_red = QScrollBar()
        self.scroll_green = QScrollBar()
        self.scroll_blue = QScrollBar()

        self.scroll_red.setRange(0, 255)
        self.scroll_green.setRange(0, 255)
        self.scroll_blue.setRange(0, 255)

        self.scroll_red.sliderMoved.connect(self.slider_value)
        self.scroll_green.sliderMoved.connect(self.slider_value)
        self.scroll_blue.sliderMoved.connect(self.slider_value)

        h_layout = QHBoxLayout()
        h_layout.addWidget(self.label)
        h_layout.addWidget(self.scroll_red)
        h_layout.addWidget(self.scroll_green)
        h_layout.addWidget(self.scroll_blue)

        self.setLayout(h_layout)

    def slider_value(self):
        # print("rgb(%s, %s, %d)" % (self.scroll_red.value(), self.scroll_green.value(), self.scroll_blue.value()))
        palette = QPalette()
        color = QColor(self.scroll_red.value(), self.scroll_green.value(), self.scroll_blue.value())
        palette.setColor(QPalette.Foreground, color)
        self.label.setPalette(palette)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = ScrollDemo()
    win.show()
    sys.exit(app.exec())