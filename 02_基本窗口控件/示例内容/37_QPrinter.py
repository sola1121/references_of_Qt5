import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QIcon, QPixmap,  QPainter
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QSizePolicy, QAction


class MainWin(QMainWindow):
    """主窗口"""
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle("QPrinter 使用")

        self.image_label = QLabel()
        self.image_label.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.setCentralWidget(self.image_label)
        self.image = QImage("02_基本窗口控件/示例内容/sources/images/python-color-128.png")
        self.image_label.setPixmap(QPixmap(self.image))
        self.resize(self.image.width()+100, self.image.height()+100)

        self.createActions()
        self.createMenus()
        self.createToolbars()

    def createActions(self):
        """创建打印动作"""
        self.action_print = QAction(
            QIcon("02_基本窗口控件/示例内容/sources/icons/android_02.ico"),
            self.tr("打印"),
            parent=self
        )
        self.action_print.setShortcut("Ctrl+P")
        self.action_print.setStatusTip(self.tr("打印"))
        self.action_print.triggered.connect(self.slot_print)

    def createMenus(self):
        """创建菜单"""
        menu_bar = self.menuBar()
        new_menu = menu_bar.addMenu(self.tr("打印"))
        new_menu.addAction(self.action_print)

    def createToolbars(self):
        """创建工具框"""
        toolbar_file = self.addToolBar("打印")
        toolbar_file.setMovable(True)
        toolbar_file.addAction(self.action_print)

    # FIXME: 有问题, 真有问题
    def slot_print(self):
        """打印动作触发的槽函数, 用于打印, 
           会创建一个QPrinter给QPainter用作绘画"""
        printer = QPrinter()
        printer.setOutputFormat(QPrinter.PdfFormat)
        print_dialog = QPrintDialog(printer, parent=self)   # 打印对话框, 用于设置printer
        if print_dialog.exec_():
            painter = QPainter(printer)
            rect = painter.viewport()   # 实例化视图窗口
            size = self.image.size()   # 获取图片的尺寸
            size.scale(rect.size(), Qt.KeepAspectRatio)   # Qt.KeepAspectRatio  保持纵横比
            painter.setViewport(rect.x(), rect.y(), size.width(), size.height())  #设置窗口的大小为图片的磁村，并在窗口内绘制
            painter.setWindow(self.image.rect())
            painter.drawImage(0, 0, self.image)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = MainWin()
    win.show()
    sys.exit(app.exec())
