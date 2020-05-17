import sys

from PyQt5.QtCore import Qt, QDateTime
from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout, QDialog, QDialogButtonBox, 
                             QLineEdit, QPushButton, QVBoxLayout, QDateTimeEdit)


class DateDialog(QDialog):
    """对话窗口"""
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle("多窗口利用控件属性传递参数")
        self.resize(200, 100)

        self.datetimedit = QDateTimeEdit(parent=self)
        self.datetimedit.setCalendarPopup(True)
        self.datetimedit.setMinimumSize(100, 20)
        self.datetimedit.setDateTime(QDateTime.currentDateTime())
        
        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, Qt.Horizontal, parent=self)
        # 两个按钮, 分别连接dialog.accept()和dialog.reject()
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)

        v_layout = QVBoxLayout()
        v_layout.addWidget(self.datetimedit)
        v_layout.addWidget(buttons)
        self.setLayout(v_layout)

    def date_time(self):
        """从对话框中获取当前日期和时间"""
        return self.datetimedit.dateTime()

    @staticmethod
    def get_date_time(parent=None):
        """静态方法, 创建一个自己, 返回时间"""
        dialog = DateDialog(parent)
        result = dialog.exec()
        date = dialog.date_time()
        return date.date(), date.time(), result==QDialog.Accepted


class WinForm(QWidget):
    """主窗口"""
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle("对话窗口关闭时返回值给该主窗口")
        self.resize(400, 100)

        self.linedit = QLineEdit(parent=self)

        self.button_1 = QPushButton("弹出对话框 1")
        self.button_2  = QPushButton("弹出对话框 2")
        self.button_1.clicked.connect(self.button_1_clicked)
        self.button_2.clicked.connect(self.button_2_clicked)

        grid_layout = QGridLayout()
        grid_layout.addWidget(self.linedit)
        grid_layout.addWidget(self.button_1)
        grid_layout.addWidget(self.button_2)
        self.setLayout(grid_layout)

    def button_1_clicked(self):
        dialog = DateDialog(parent=self)
        result = dialog.exec()
        date = dialog.date_time()
        self.linedit.setText(date.date().toString())
        print("\n日期对话框的返回值")
        print("date=%s" % str(date.date()))
        print("time=%s" % str(date.time()))
        print("result=%s" % result)
        dialog.close()

    def button_2_clicked(self):
        date, time, result = DateDialog.get_date_time()
        self.linedit.setText(date.toString())
        print("\n日期对话框的返回值")
        print("date=%s" % str(date))
        print("time=%s" % str(time))
        print("result=%s" % result)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = WinForm()
    win.show()
    sys.exit(app.exec())