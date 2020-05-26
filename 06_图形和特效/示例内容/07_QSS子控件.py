import sys

from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QVBoxLayout


class WinForm(QWidget):
    """主窗口"""
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle("QComboBox 样式")
        self.resize(200, 100)

        combobox = QComboBox(parent=self)
        combobox.setObjectName("myComboBox")
        combobox.addItems(["Ubuntu", "CentOS", "Mint", "RedHat", "Debian"])
        combobox.move(50, 50)


if __name__ == "__main__":

    qss_style = """
        QComboBox#myComboBox::drop-down {image: url(06_图形和特效/示例内容/sources/down-arrow-48.png)}
    """

    app = QApplication(sys.argv)
    win = WinForm()
    win.setStyleSheet(qss_style)
    win.show()
    sys.exit(app.exec())
