import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

# import apprcc_rc
# from winForm import apprcc_rc   
# 以上这两段导入似乎可有可无, 因为在winForm.py最后有导入
from winForm import Ui_winForm


class MainForm(QMainWindow, Ui_winForm):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        # 为按钮们绑定click事件
        self.pythonButton.clicked.connect(self.py_btn)
        self.golangButton.clicked.connect(self.go_btn)
        self.javascriptButton.clicked.connect(self.js_btn)
        self.cButton.clicked.connect(self.c_btn)

    def switch_visible(self, widget):
        """可视性切换"""
        if widget.isVisible() is True:
            widget.setVisible(False)
        else:
            widget.setVisible(True)

    def py_btn(self):
        self.switch_visible(self.pythonLabel)
    
    def go_btn(self):
        self.switch_visible(self.GolangLabel)
    
    def js_btn(self):
        self.switch_visible(self.JSLabel)
    
    def c_btn(self):
        self.switch_visible(self.CLabel)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec())