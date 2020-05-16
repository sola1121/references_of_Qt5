import sys

from PyQt5.QtCore import QMetaObject, pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton


class WinForm(QWidget):
    """主窗口"""
    def __init__(self, parent=None):
        super().__init__(parent)

        self.btnOK = QPushButton("OK", self)

        self.btnOK.setObjectName("btnOK") # 使用setObjectName设置对象名称

        QMetaObject.connectSlotsByName(self)   # 更具信号名称自动连接到槽函数的核心代码

        h_layout = QHBoxLayout()
        h_layout.addWidget(self.btnOK)
        self.setLayout(h_layout)

    @pyqtSlot()
    def on_btnOK_clicked(self):
        print("单击了OK按钮")


if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = WinForm()
    win.show()
    sys.exit(app.exec())
