import sys

from PyQt5.QtWidgets import QApplication, QWidget, QFormLayout, QLabel, QLineEdit, QComboBox


class ComboxAcceptDrop(QComboBox):
    """自定义QComBox, 让其能够接受拖曳数据"""
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        # 让QComboBox能接受拖曳
        self.setAcceptDrops(True)

    def dragEnterEvent(self, QDragEnterEvent):
        """重载拖拽入控件时事件"""
        print(QDragEnterEvent)
        mime_data = QDragEnterEvent.mimeData()
        if mime_data.hasText():
            QDragEnterEvent.accept()
        else:
            QDragEnterEvent.ignore()

    def dropEvent(self, QDropEvent):
        """重载拖曳释放事件"""
        print(QDropEvent)
        self.addItem(QDropEvent.mimeData().text())


class Win(QWidget):
    """主窗口"""
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.resize(420, -1)
        # 设置窗口控件本身支持拖拽事件
        self.setAcceptDrops(True)

        form_layout = QFormLayout(parent=self)
        self.lable = QLabel("可以将左边的文本拖拽到右边的下拉控件中")
        # 用于产生拖拽内容的单行编辑框
        self.linedit = QLineEdit()
        self.linedit.setDragEnabled(True)   # 设置单行编辑框内容可以拖拽
        self.linedit.setStyleSheet("background: rgb(230,230,200); color: red; min-width: 200px;")
        # 用于接受拖拽的下拉框
        self.combox = ComboxAcceptDrop()
        self.combox.setMaximumWidth(160)

        form_layout.addRow(self.lable)
        form_layout.addRow(self.linedit, self.combox)
        self.setLayout(form_layout)
    

if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = Win()
    win.show()
    sys.exit(app.exec())