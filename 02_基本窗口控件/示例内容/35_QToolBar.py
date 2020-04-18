import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QAction, QActionGroup


class MainWin(QMainWindow):
    """主窗口"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("QToolBar 使用")
        self.resize(300, 200)

        self.label = QLabel(parent=self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setText("------")
        self.label.setOpenExternalLinks(True)   # 可以打开链接
        self.setCentralWidget(self.label)
 
        toolbar = self.addToolBar("编程语言")   # 向QMianWindow 中添加QToolBar
        toolbar.setMovable(True)    # 设置QToolBar可以移动
        group_actions = QActionGroup(self)   #　设置一个QActionGroup, 用于包容所有的acitons
        action_python = QAction(QIcon("02_基本窗口控件/示例内容/sources/images/python-simple-color-96.png"), "Python", parent=self)
        action_python.setActionGroup(group_actions)
        action_golang = QAction(QIcon("02_基本窗口控件/示例内容/sources/images/golang-96.png"), "Golang", parent=self)
        action_golang.setActionGroup(group_actions)
        action_javascript = QAction(QIcon("02_基本窗口控件/示例内容/sources/images/javascript-96.png"), "JavaScript", parent=self)
        action_javascript.setActionGroup(group_actions)
        action_c = QAction("C" , parent=self)
        action_c.setData("C Language Wiki")   # 设置传输的数据, 任意类型
        action_c.setActionGroup(group_actions)
        
        group_actions.triggered.connect(self.language)   # 设置QActionGroup的好处就是可以都共同绑定一个槽函数
        
        toolbar.addAction(action_python)
        toolbar.addAction(action_golang)
        toolbar.addAction(action_javascript)
        toolbar.addAction(action_c)

    def language(self, action):
        format_link = "<a href='{link}'>{name}</a>"
        if str(action.text()).lower() == "python":
            self.label.setText(format_link.format(link="https://www.python.org", name="Python"))
        elif str(action.text()).lower() == "golang":
            self.label.setText(format_link.format(link="https://www.golang.org", name="Golang"))
        elif str(action.text()).lower() == "javascript":
            self.label.setText(format_link.format(link="https://www.javascript.com", name="JavaScript"))
        elif str(action.text()).lower() == "c":
            self.label.setText(format_link.format(link="https://en.wikipedia.org/wiki/The_C_Programming_Language", name=action.data()))
        else:
            self.label.setText("<span style='color: red;'>unkonw</span>")


if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = MainWin()
    win.show()
    sys.exit(app.exec())