import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QVBoxLayout, QLabel, QAction


class MainWin(QMainWindow):
    """主窗口, 继承QMainWindow"""
    def __init__(self, parent=None):
        super(MainWin, self).__init__(parent)
        self.setWindowTitle("QMenuBar 使用")
        self.resize(240, 100)

        self.label = QLabel(parent=self)
        self.label.setText("-------")
        self.label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(self.label)

        menubar = self.menuBar()   # 从QMainWindow中获得其QMenuBar

        menu_file = menubar.addMenu("文件(&F)")   # 新建QMenu
        menu_file.addAction("新建(&N)")   # 新建QAction

        action_save = QAction("保存(&S)", parent=self)   # 新建QAction
        action_save.setShortcut("Ctrl+S")
        menu_file.addAction(action_save)   # 将该新建的动作添加到菜单中

        menu_edit = menu_file.addMenu("编辑(&E)")   # 新建QMenu
        menu_edit.addAction("复制")   # 向刚建的菜单中添加新的QAction, 没有做获取其QACtion对象
        menu_edit.addAction("粘贴")

        action_quit = QAction("退出", parent=self)   # 新建QAction
        menu_file.addAction(action_quit)   # 将该新动作添加到菜单中
        action_quit.triggered.connect(self.to_quit)   # 绑定触发事件

    def to_quit(self):
        app = QApplication.instance()
        app.exit()


if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = MainWin()
    win.show()
    sys.exit(app.exec())