import sys

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QHBoxLayout, QPushButton
from PyQt5.QtGui import QIcon

class MainWin(QMainWindow):
    """主窗口"""
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle("PyQt关闭主窗口")
        self.setGeometry(100, 100, 400, 200)

        # 创建一个按钮, 并绑定单击事件
        self.closeButton = QPushButton()
        self.closeButton.setText("关闭主窗口")
        self.closeButton.setIcon(QIcon("./sources/icons/android_02.ico"))
        self.closeButton.clicked.connect(self.on_click_close_button)

        # 设置窗口中心的控件, 先创建窗口使用的布局管理器, 然后让其变为窗口控件的一部分, 最后将其作为主窗口控件
        layout = QHBoxLayout()
        layout.addWidget(self.closeButton)
        main_frame = QWidget()
        main_frame.setLayout(layout)
        self.setCentralWidget(main_frame)

    def on_click_close_button(self):
        sender = self.sender()   # sender是发送信号的对象
        print(sender.text() + "被按下了.")
        QApp = QApplication.instance()
        QApp.quit()


if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = MainWin()
    win.show()
    sys.exit(app.exec_())
