import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton


class WinFrom(QWidget):
    """主窗口"""
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.resize(320, -1)

        vbox = QVBoxLayout()
        # 按钮1, 设置可以check, 点击样式切换toggle
        self.btn_1 = QPushButton("按钮 1")
        self.btn_1.setCheckable(True)   # 设置可以被check
        self.btn_1.toggle()   # 每点一次切换样式
        self.btn_1.clicked.connect(lambda:self.which_btn(self.btn_1))   # 绑定单击事件, 使用lambda可以传参哦
        self.btn_1.clicked.connect(self.state_btn)
        # 按钮2, 设置svg图片文QIcon
        self.btn_2 = QPushButton("具有Icon")
        self.btn_2.setIcon(QIcon("02_基本窗口控件/示例内容/sources/images/python-512.svg"))
        self.btn_2.clicked.connect(lambda:self.which_btn(self.btn_2))
        # 按钮3, 设置不可用
        self.btn_3 = QPushButton("Disabled")
        self.btn_3.setEnabled(False)
        # 按钮4, 设置默认选中, 设置跨借鉴
        self.btn_4 = QPushButton("&Download")
        self.btn_4.setDefault(True)
        self.btn_4.clicked.connect(lambda:self.which_btn(self.btn_4))

        vbox.addWidget(self.btn_1)
        vbox.addWidget(self.btn_2)
        vbox.addWidget(self.btn_3)
        vbox.addWidget(self.btn_4)
        self.setLayout(vbox)

    def state_btn(self):
        if self.btn_1.isChecked():
            self.btn_1.setText("check=True, toggle切换样式")
        else:
            self.btn_1.setText("check=False, toggle切换样式")
        
    def which_btn(self, btn):
        self.setWindowTitle("click: {}".format(btn.text()))


if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = WinFrom()
    win.show()
    sys.exit(app.exec())