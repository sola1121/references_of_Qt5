import sys

from PyQt5.QtWidgets import QApplication, QWidget, QFormLayout, QLineEdit


class LineEditDemo(QWidget):
    """主窗口"""
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        form_layout = QFormLayout()
        linedit_ip = QLineEdit()
        linedit_mac = QLineEdit()
        linedit_date = QLineEdit()
        linedit_license = QLineEdit()
        # 设置掩码
        linedit_ip.setInputMask("000.000.000.000;_")
        linedit_mac.setInputMask("HH:HH:HH:HH:HH:HH;_")
        linedit_date.setInputMask("0000-00-00")
        linedit_license.setInputMask(">AAAAA-AAAAA-AAAAA-AAAAA;#")

        form_layout.addRow("数字掩码", linedit_ip)
        form_layout.addRow("Mac掩码", linedit_mac)
        form_layout.addRow("日期掩码", linedit_date)
        form_layout.addRow("许可证掩码", linedit_license)

        self.setLayout(form_layout)   # 向主窗口添加布局管理器


if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = LineEditDemo()
    win.show()
    sys.exit(app.exec())