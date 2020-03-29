import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QWidget

from menu_toolbar_win import Ui_MainWindow


class MainForm(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        # 菜单的点击事件, 当点击关闭菜单式连接槽函数
        self.fileCloseAction.triggered.connect(self.close)
        # 菜单的点击事件, 当点击打开菜单是连接槽函数 openMsg
        self.fileOpenAction.triggered.connect(self.openMsg)

    def openMsg(self):
        # 判断系统
        root_dir = str()
        if sys.platform == "win32":
            root_dir = "C:/"
        elif sys.platform == "linux":
            root_dir = "/"
        else:
            root_dir = "/"
        file, ok = QFileDialog.getOpenFileName(self, "打开", root_dir, "All Files (*);;Text Files(*.txt)")
        # 在状态栏像是文件地址
        self.statusBar.showMessage(file)


if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_())
