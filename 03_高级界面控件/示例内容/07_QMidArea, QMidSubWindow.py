import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMdiArea, QMdiSubWindow, QTextEdit


class MainWin(QMainWindow):
    """主窗口"""
    count = 0

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle("QMdiArea QMdiSubWidow 使用")

        self.mdi_area = QMdiArea()
        self.setCentralWidget(self.mdi_area)

        menu_bar = self.menuBar()
        menu_file = menu_bar.addMenu("文件")
        action_new = menu_file.addAction("新建")
        action_new.setData("new")
        action_save = menu_file.addAction("保存")
        action_save.setData("save")
        action_cascade = menu_file.addAction("级联&Cascade")
        action_cascade.setData("cascade")
        action_tiled = menu_file.addAction("平铺&Tiled")
        action_tiled.setData("tiled")
        menu_file.triggered.connect(self.window_action)

    def window_action(self, action):
        print("点击", action.data())
        if action.data() == "new":
            MainWin.count += 1
            sub_win = QMdiSubWindow()
            sub_win.setWidget(QTextEdit())
            sub_win.setWindowTitle("子窗口 %d" % MainWin.count)
            self.mdi_area.addSubWindow(sub_win)
        if action.data() == "csscade":
            self.mdi_area.cascadeSubWindows()   # 级联模式排列
        if action.data() == "tiled":
            self.mdi_area.tileSubWindows()   # 平铺排列


if __name__ ==  "__main__":

    app = QApplication(sys.argv)
    win =  MainWin()
    win.show()
    sys.exit(app.exec())