import sys

from PyQt5.QtWidgets import QApplication, QWidget, QFormLayout, QLineEdit, QPushButton, QInputDialog


class InputDialogDemo(QWidget):
    """主窗口"""
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle("QInputDialog 使用")
        
        self.btn_1 = QPushButton()
        self.btn_1.setText("获得列表里的选项")
        self.btn_1.clicked.connect(self.get_item)
        self.linedit_1 = QLineEdit()

        self.btn_2 = QPushButton()
        self.btn_2.setText("获得字符串")
        self.btn_2.clicked.connect(self.get_text)
        self.linedit_2 = QLineEdit()

        self.btn_3 = QPushButton()
        self.btn_3.setText("获得整型")
        self.btn_3.clicked.connect(self.get_int)
        self.linedit_3 = QLineEdit()

        form_layout = QFormLayout()
        form_layout.addRow(self.btn_1, self.linedit_1)
        form_layout.addRow(self.btn_2, self.linedit_2)
        form_layout.addRow(self.btn_3, self.linedit_3)
        self.setLayout(form_layout)

    def get_item(self):
        items = ("Python", "Golang", "JavaScript", "C")
        item, ok = QInputDialog.getItem(self, "下拉框输入框", "语言列表", items, current=0, editable=False)
        if ok and item:
            self.linedit_1.setText(item)

    def get_text(self):
        text, ok = QInputDialog.getText(self, "文本输入框", "输入内容", echo=QLineEdit.Normal)
        if ok:
            self.linedit_2.setText(str(text))

    def get_int(self):
        num, ok = QInputDialog.getInt(self, "整型输入框", "输入数字", value=0, min=0, max=100, step=1)
        if ok:
            self.linedit_3.setText(str(num))


if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = InputDialogDemo()
    win.show()
    sys.exit(app.exec())