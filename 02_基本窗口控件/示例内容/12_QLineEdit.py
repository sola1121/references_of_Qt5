import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QFont
from PyQt5.QtWidgets import QApplication, QWidget, QFormLayout, QLineEdit, QLabel, QToolTip


class LineEditDemo(QWidget):
    """主窗口"""
    def __init__(self, parent=None):
        super(LineEditDemo, self).__init__(parent=parent)
        self.setWindowTitle("QLineEdit 综合使用")

        self.hint_label = QLabel()

        linedit_1 = QLineEdit()   # QLineEdit对象
        linedit_1.setMaxLength(4)   # 设置能输入最长字符长度
        linedit_1.setAlignment(Qt.AlignRight)   # 设置对齐方式
        linedit_1.setValidator(QIntValidator())   # 设置验证器, 只能输入整形
        linedit_1.setFont(QFont("Consolas", 20))   # 设置字体

        linedit_2 = QLineEdit()   # QLineEdit对象
        validator_float = QDoubleValidator()
        validator_float.setRange(0.0, 100.0, 2)
        linedit_2.setValidator(validator_float)   # 设置验证器, 只能输入浮点型

        linedit_3 = QLineEdit()   # QLineEdit对象
        linedit_3.setInputMask("+99_99_999_9999")   # 设置掩码

        linedit_4 = QLineEdit()   # QLineEdit对象
        linedit_4.setPlaceholderText("发送文本改变了的信号")
        linedit_4.textChanged.connect(self.text_change_hint)   # 触发文本改变事件

        linedit_5 = QLineEdit()   # QLineEdit对象
        linedit_5.setEchoMode(QLineEdit.Password)   # 设置文本显示格式
        linedit_5.editingFinished.connect(self.enter_press)

        linedit_6 = QLineEdit()   # QLineEdit对象
        linedit_6.setText("只读内容")
        linedit_6.setReadOnly(True)   # 设置内容只读
        linedit_6.setToolTip("这是只读的, 不能更改")

        form_layout = QFormLayout(parent=self)
        form_layout.addRow(self.hint_label)
        form_layout.addRow("整形验证", linedit_1)
        form_layout.addRow("浮点验证", linedit_2)
        form_layout.addRow("具有输入掩码", linedit_3)
        form_layout.addRow("文本改变会触发事件", linedit_4)
        form_layout.addRow("显示格式密码", linedit_5)
        form_layout.addRow("只读", linedit_6)

    def text_change_hint(self, text):
        """QLineEdit.textChange事件, 会向其中传入当前输入框中的内容"""
        self.hint_label.setText("现在输入框中的内容: <font color='blue'>%s</font>" % text)

    def enter_press(self):
        """QLineEdit.enditingFinished事件, 在更改焦点的时候触发"""
        self.hint_label.setText("<font color='green'>password已输入.</font>")


if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = LineEditDemo()
    win.show()
    sys.exit(app.exec())
