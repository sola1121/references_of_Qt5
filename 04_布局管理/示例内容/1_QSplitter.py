import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QFrame, QSplitter, QTextEdit


class SplitterDemo(QWidget):
    """主窗口"""
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle("QSplitter 使用")
        self.resize(300, 200)

        topleft = QFrame()
        topleft.setFrameShape(QFrame.StyledPanel)
        bottom = QFrame()
        bottom.setFrameShape(QFrame.StyledPanel)

        splitter_1 = QSplitter(Qt.Horizontal)
        splitter_1.addWidget(topleft)
        splitter_1.addWidget(QTextEdit())
        splitter_1.setSizes([100, 200])

        splitter_2 = QSplitter(Qt.Vertical)
        splitter_2.addWidget(splitter_1)
        splitter_2.addWidget(bottom)

        h_layout = QHBoxLayout()
        h_layout.addWidget(splitter_2)
        self.setLayout(h_layout)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = SplitterDemo()
    win.show()
    sys.exit(app.exec())
