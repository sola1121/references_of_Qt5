import sys

from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QRegExpValidator
from PyQt5.QtWidgets import QApplication, QWidget, QFormLayout, QLineEdit


class LineEditDemo(QWidget):
    """主窗口"""
    def __init__(self, parent=None):
        super(LineEditDemo, self).__init__(parent=parent)
        self.setWindowTitle("QLineEdit.setValidator 验证输入")

        form_layout = QFormLayout()
        linedit_int = QLineEdit()
        linedit_float = QLineEdit()
        linedit_regex = QLineEdit()

        form_layout.addRow("整形", linedit_int)
        form_layout.addRow("浮点型", linedit_float)
        form_layout.addRow("使用正则, 字母和数字", linedit_regex)

        linedit_int.setPlaceholderText("整形")
        linedit_float.setPlaceholderText("浮点型")
        linedit_regex.setPlaceholderText("字母和数字")

        # 定义整形验证器, 在[1, 99]
        validator_int = QIntValidator(parent=self)
        validator_int.setRange(1, 99)

        # 定义浮点验证器, [-360, 360], 精度小数点后两位
        validator_float = QDoubleValidator(parent=self)
        validator_float.setRange(-360.0, 360.0, 2)
        # validator_float.setDecimals(2)
        validator_float.setNotation(QDoubleValidator.StandardNotation)   # 使用标准符号

        # 正则验证, 字母和数字
        reg = QRegExp("[a-zA-Z0-9]+$")
        validator_regex = QRegExpValidator(parent=self)
        validator_regex.setRegExp(reg)

        # 设置验证器
        linedit_int.setValidator(validator_int)
        linedit_float.setValidator(validator_float)
        linedit_regex.setValidator(validator_regex)

        self.setLayout(form_layout)   # 向主窗口添加布局管理器


if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = LineEditDemo()
    win.show()
    sys.exit(app.exec())
