import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout


class WinForm(QWidget):
    """主窗口"""
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle("QSS 样式")
        
        button_1 = QPushButton(parent=self)
        button_1.setText("按钮 1")

        button_2 = QPushButton(parent=self)
        button_2.setText("按钮 2")

        v_layout = QVBoxLayout()
        v_layout.addWidget(button_1)
        v_layout.addWidget(button_2)
        self.setLayout(v_layout)


if __name__ == "__main__":

    qss_style = """
        QPushButton {
            background-color: red;
        }
    """
    
    app = QApplication(sys.argv)
    win = WinForm()
    win.setStyleSheet(qss_style)   # 在此设置QSS样式
    win.show()
    sys.exit(app.exec())
