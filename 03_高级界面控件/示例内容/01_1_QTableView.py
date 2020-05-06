import sys

from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableView


class TableForm(QWidget):
    """主窗口"""
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.resize(500, 300)

        # 储存任意层次结构的数据
        self.model = QStandardItemModel(4, 4)   # 共4行4列
        self.model.setHorizontalHeaderLabels(["标题1", "标题2", "标题3", "标题4"])

        for row in range(4):
            for column in range(4):
                item = QStandardItem("row %s, clomun %s" % (row, column))
                self.model.setItem(row, column, item)

        # 创建QTableView控件
        self.table_view = QTableView()
        self.table_view.setModel(self.model)

        v_layout = QVBoxLayout()
        v_layout.addWidget(self.table_view)

        self.setLayout(v_layout)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = TableForm()
    win.show()
    sys.exit(app.exec())
