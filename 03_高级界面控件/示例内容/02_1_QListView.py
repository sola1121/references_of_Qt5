import sys

from PyQt5.QtCore import QStringListModel
from PyQt5.QtWidgets import QApplication, QWidget, QListView, QVBoxLayout, QMessageBox


class ListViewDemo(QWidget):
    """主窗口"""
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle("QListView 使用")
        self.resize(300, 270)

        self.qlist = ["Item 1", "Item 2", "Item 3", "Item 4"]
        
        # 创建字符串列表模型
        string_model = QStringListModel()
        # 设置字符串列表模型
        string_model.setStringList(self.qlist)

        # 创建QListView
        list_view = QListView()
        # 向QListView中添加模型
        list_view.setModel(string_model)
        list_view.clicked.connect(self.item_clicked)

        v_layout = QVBoxLayout()
        v_layout.addWidget(list_view)
        self.setLayout(v_layout)

    def item_clicked(self, index):
        QMessageBox.information(self, "list widget", "selected:" + self.qlist[index.row()])


if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = ListViewDemo()
    win.show()
    sys.exit(app.exec())