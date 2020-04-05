import sys

from PyQt5.QtWidgets import QApplication, QDialog, QGridLayout, QLabel, QLineEdit, QPushButton


class QLabelDemo(QDialog):
    """继承对话框, 主窗口
       在定义QLabel对象的时候, 就是用助记符"&"+文本的方式定义他的内容, 这样按Alt+文本第一个字母就可以切换到该控件焦点
       然后用setBuddy()将按下快捷键的焦点转移到绑定的控件上
    """
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle("Qlabel 使用快捷键")
        # self.resize(400, 200)
        # 第一行name
        name_label = QLabel("&Name", parent=self)   # Alt+N
        name_edit = QLineEdit(parent=self)
        name_label.setBuddy(name_edit)
        # 第二行password
        pass_label = QLabel("&PassWord", parent=self)   # Alt+P
        pass_edit = QLineEdit(parent=self)
        pass_label.setBuddy(pass_edit)
        # 第三行按钮
        btn_ok = QPushButton("&OK")   # Alt+O
        btn_cancel = QPushButton("&Cancel")   # Alt+C
        # 创建格栅布局管理器, 并添加到父窗口, 这里没有用self.addLayout(), 而是创建的时候就绑到父窗口了
        grid_layout = QGridLayout(self)
        # 向格栅添加name
        grid_layout.addWidget(name_label, 0, 0)
        grid_layout.addWidget(name_edit, 0, 1, 1, 2)
        # 向格栅添加password
        grid_layout.addWidget(pass_label, 1, 0)
        grid_layout.addWidget(pass_edit, 1, 1, 1, 2)
        # 向格栅添加按钮
        grid_layout.addWidget(btn_ok, 2, 1)
        grid_layout.addWidget(btn_cancel, 2, 2)

        btn_cancel.clicked.connect(self.close_process)

    def close_process(self):
        app = QApplication.instance()
        app.quit()


if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = QLabelDemo()
    win.show()
    sys.exit(app.exec())
