import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QDockWidget, QListWidget, QTextEdit


class DockMain(QMainWindow):
    """主窗口"""
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle("QMainWindow使用QDockWidget")
        self.setCentralWidget(QTextEdit())

        # 设置QMainWindow的菜单栏
        menu_bar = self.menuBar()
        menu_file = menu_bar.addMenu("文件")
        menu_file.addAction("新建")
        menu_file.addAction("保存")
        action_quit = menu_file.addAction("退出")
        action_quit.triggered.connect(self.to_quit)

        # 设置QDockWidget使用的QListWidget
        list_widget = QListWidget()
        list_widget.addItem("list 1")
        list_widget.addItem("lsit 2")
        list_widget.addItem("list 3")
        # 实例化一个QDockWidget, 父控件为QMainWindow
        dock_widget = QDockWidget("Dock控件", parent=self)
        dock_widget.setWidget(list_widget)   # 设置显示的控件为
        dock_widget.setFloating(False)

        self.addDockWidget(Qt.RightDockWidgetArea, dock_widget)


    def to_quit(self):
        app = QApplication.instance()
        app.quit()
      

if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = DockMain()
    win.show()
    sys.exit(app.exec())
