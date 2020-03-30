import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget

from child_QWidget import Ui_ChildrenForm
from main_window import Ui_MainWindow


class ChildrenForm(QWidget, Ui_ChildrenForm):
    """子窗口类"""
    def __init__(self):
        super(ChildrenForm, self).__init__()
        self.setupUi(self)


class MainWindow(QMainWindow, Ui_MainWindow):
    """主窗口类"""
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        # self.child = children()生成子窗口实例self.child
        self.child = ChildrenForm()
        # 单击菜单栏对应动作触发子窗口
        self.openNewWindowAction.triggered.connect(self.childshow)
        # 单击按钮发出信号调用槽隐藏子窗口
        self.pushButton.clicked.connect(self.childhide)

    def childshow(self):
        # 添加子窗口
        self.gridLayout.addWidget(self.child)
        self.child.show()
    
    def childhide(self):
        # 关闭子窗口
        self.gridLayout.removeWidget(self.child)
        self.child.hide()


if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())