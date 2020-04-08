import sys

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QSpinBox, QDoubleSpinBox


class SpinBoxDemo(QWidget):
    """主窗口"""
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle("SpinBox 使用")
        self.resize(320, -1)

        vbox = QVBoxLayout()
        self.label = QLabel()
        vbox.addWidget(self.label)
        vbox.addStretch(1)

        self.spin_box_1 = QSpinBox()
        self.spin_box_1.setRange(100, 1000)   # 设置范围
        self.spin_box_1.setSingleStep(100)   # 设置步长
        self.spin_box_1.valueChanged.connect(self.info_spin)

        self.spin_box_2 = QDoubleSpinBox()
        self.spin_box_2.setRange(10.0, 20.0)   # 设置范围
        self.spin_box_2.setSingleStep(.1)   # 设置步长
        self.spin_box_2.valueChanged.connect(self.info_spin)
        
        vbox.addWidget(self.spin_box_1)
        vbox.addWidget(self.spin_box_2)
        self.setLayout(vbox)

    def info_spin(self, value):
        self.label.setText(str(value))


if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = SpinBoxDemo()
    win.show()
    sys.exit(app.exec())