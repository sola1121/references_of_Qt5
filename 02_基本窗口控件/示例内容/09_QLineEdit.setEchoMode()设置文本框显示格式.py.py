import sys

from PyQt5.QtWidgets import QApplication, QWidget, QFormLayout, QLabel, QLineEdit


class LineEditDemo(QWidget):
    """lineEdit, 主窗口"""
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle("QLineEdit, EchoMode(输出显示)")
        # 创建表格布局管理器, 创建QLineEdit
        form_layout = QFormLayout()
        normal_linedit = QLineEdit()
        noEcho_linedit = QLineEdit()
        password_linedit = QLineEdit()
        passwordEchoOnEdit_linedit = QLineEdit()
        # 向表格布局管理器中添加QLineEdit
        form_layout.addRow("Normal", normal_linedit)
        form_layout.addRow("NoEcho", noEcho_linedit)
        form_layout.addRow("Password", password_linedit)
        form_layout.addRow("PasswordEchoOnEdit", passwordEchoOnEdit_linedit)
        # 设置placeholder
        normal_linedit.setPlaceholderText("Normal")
        noEcho_linedit.setPlaceholderText("NoEcho")
        password_linedit.setPlaceholderText("Password")
        passwordEchoOnEdit_linedit.setPlaceholderText("PasswordEchoOnEdit")
        # 设置显示格式
        normal_linedit.setEchoMode(QLineEdit.Normal)
        noEcho_linedit.setEchoMode(QLineEdit.NoEcho)
        password_linedit.setEchoMode(QLineEdit.Password)
        passwordEchoOnEdit_linedit.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.setLayout(form_layout)   # 向主窗口中添加布局管理器


if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = LineEditDemo()
    win.show()
    sys.exit(app.exec())
