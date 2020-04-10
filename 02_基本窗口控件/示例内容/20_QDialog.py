import sys
import random

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QDialog, QLabel


class DialogDemo(QWidget):
    """主窗口"""
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle("QDialog 使用")
        self.setFixedSize(320, 200)
        
        self.label = QLabel(parent=self)
        self.label.resize(300, 50)

        self.btn = QPushButton(parent=self)
        self.btn.setText("Pop-up dialog")
        self.btn.setGeometry(150, 100, 100, 30)
        self.btn.clicked.connect(self.pup_up)
    
        # 创建对话框, 设置为程序模态
        self.dialog = QDialog()
        self.dialog.setWindowTitle("dialog poped")
        self.dialog.setWindowModality(Qt.ApplicationModal)

        self.ok_btn = QPushButton(parent=self.dialog)
        self.ok_btn.setText("OK")
        self.ok_btn.move(50, 50)
        self.ok_btn.clicked.connect(self.ok_func)

    def pup_up(self):
        self.dialog.exec()   # 记得让对话框执行

    def ok_func(self):
        # self.dialog.done(random.randint(0, 1))
        self.dialog.setResult(3)
        acc = self.dialog.Accepted
        rej = self.dialog.Rejected
        res = self.dialog.result()
        self.dialog.destroy()
        format_text = f"Accepted: {acc}; Rejected: {rej}, result: {res}"
        self.label.setText(format_text)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = DialogDemo()
    win.show()
    sys.exit(app.exec())
    