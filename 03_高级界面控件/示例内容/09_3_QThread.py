import sys

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QPushButton, QGridLayout


class ThreadWorker(QThread):
    """线程对象"""

    single_out = pyqtSignal(str)   # 自定义的信号, str为传递给槽函数的数据类型

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.working = True
        self.num = 0
    
    def __del__(self):
        self.working = False
        self.wait()   # 在删除QThread的时候等候完成

    def run(self):
        while self.working == True:
            file_str = "File index {}".format(self.num)
            self.num += 1
            # 发射信号
            self.single_out.emit(file_str)   # 自定义的信号发出
            # 线程休眠2s
            self.sleep(2)


class WinForm(QWidget):
    """主窗口"""
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle("QThread 使用")

        self.thread = ThreadWorker()   # 创建一个线程对象
        self.thread.single_out.connect(self.slot_add)   # 将信号绑定槽函数

        self.list_file = QListWidget()
        self.button_start = QPushButton("开始")        
        self.button_start.clicked.connect(self.slot_start)
        # 布局
        grid_layout = QGridLayout()
        grid_layout.addWidget(self.list_file, 0, 0, 1, 2)   # 0行0列, 占用1行, 占用2列
        grid_layout.addWidget(self.button_start, 1, 1)   # 1行1列

        self.setLayout(grid_layout)

    def slot_add(self, file_inf):
        self.list_file.addItem(file_inf)

    def slot_start(self):
        self.button_start.setEnabled(False)
        self.thread.start()   # 开始一个线程


if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = WinForm()
    win.show()
    sys.exit(app.exec())