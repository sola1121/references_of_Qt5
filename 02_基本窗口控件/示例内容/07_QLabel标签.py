# coding: utf-8

import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QPixmap, QIcon
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget


class WinForm(QWidget):
    """主界面"""
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle("QLabel 文本, 链接, 富文本, 图片, 事件")
        self.setWindowIcon(QIcon("02_基本窗口控件/示例内容/sources/icons/android_02.ico"))
        self.resize(400, 200)
        # 创建QLabel标签, 父窗口为当前主窗口
        label_1 = QLabel(parent=self)
        label_2 = QLabel(parent=self)
        label_3 = QLabel(parent=self)
        label_4 = QLabel(parent=self)

        # 初始化标签控件
        label_1.setText("纯文本标签, 设置调色板, 设置可以选中")
        label_1.setAutoFillBackground(True)
        palette = QPalette()   # 调色板对象
        palette.setColor(QPalette.Window, Qt.yellow)
        label_1.setPalette(palette)
        label_1.setAlignment(Qt.AlignCenter)

        label_2.setText("默认左对齐, 可以跳转<a href='http://www.python.org'>Python超链接</a>标签")

        label_3.setAlignment(Qt.AlignCenter)
        label_3.setToolTip("图片标签, 设置tooltip")
        label_3.setPixmap(QPixmap("02_基本窗口控件/示例内容/sources/images/python-simple-color-96.png"))

        label_4.setText("右对齐, <a href='#'>超链接</a>标签")
        label_4.setAlignment(Qt.AlignRight)

        # 在窗口布局中添加控件
        vbox = QVBoxLayout()   # 垂直布局管理器
        vbox.addWidget(label_1)   # 将QWidget对象添加到布局管理器
        vbox.addStretch()   # 添加间隔伸展
        vbox.addWidget(label_2)
        vbox.addStretch()
        vbox.addWidget(label_3)
        vbox.addStretch()
        vbox.addWidget(label_4)

        # label_1中的文本可以被鼠标选中
        label_1.setTextInteractionFlags(Qt.TextSelectableByMouse)
        # 滑动文本框绑定槽事件
        label_2.linkHovered.connect(self.link_hovered)
        label_2.setOpenExternalLinks(True)   # 打开允许访问超链接, 默认是False, 这样浏览器就可以访问该链接了
        # 点击链接绑定槽事件
        label_4.linkActivated.connect(self.link_clicked)

        self.setLayout(vbox)   # 主窗口设置将管理器

    def link_clicked(self):
        self.setWindowTitle("当鼠标点击label_4标签时, 触发事件")

    def link_hovered(self):
        self.setWindowTitle("当鼠标滑过label_2标签时, 触发事件")


if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = WinForm()
    win.show()
    sys.exit(app.exec())
