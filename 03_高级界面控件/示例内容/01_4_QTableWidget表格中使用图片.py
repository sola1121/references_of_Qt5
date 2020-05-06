import os, sys

from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QApplication, QWidget, QAbstractItemView, QTableWidget, QTableWidgetItem, QHBoxLayout


ROW = 2
COLUMN = 3


class TableForm(QWidget):
    """主窗口"""
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle("QTableWidget 使用图片")
        self.resize(512, 384)

        self.table_widget = QTableWidget()
        self.table_widget.setRowCount(ROW)
        self.table_widget.setColumnCount(COLUMN)
        self.table_widget.setEditTriggers(QAbstractItemView.NoEditTriggers)   # 不可编辑表格内容
        self.table_widget.setIconSize(QSize(128, 128))   # 设置图片大小
        self.table_widget.setHorizontalHeaderLabels(["图片 1", "图片 2", "图片 3"])

        for m in range(ROW):
            self.table_widget.setColumnWidth(m, 128)   # 设置列宽

        for m in range(COLUMN):
            self.table_widget.setRowHeight(m, 128)   # 设置行高
        
        self.add_picture()

        h_layout = QHBoxLayout()
        h_layout.addWidget(self.table_widget)
        self.setLayout(h_layout)

    def add_picture(self):
        row = 0
        column = 0
        language_names = ["python", "golang", "c", "javascript", "html-5", "css3"]
        for m in range(len(language_names)):
            if m % 3 == 0 and m != 0:
                row += 1
                column = 0
            file_path = os.path.join("03_高级界面控件/示例内容/sources", language_names[m]+"-96.png")
            table_item = QTableWidgetItem()
            table_item.setFlags(Qt.ItemIsEnabled)   # 点击时, 图片能选中
            table_item.setIcon(QIcon(file_path))
            self.table_widget.setItem(row, column, table_item)
            column += 1


if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = TableForm()
    win.show()
    sys.exit(app.exec())
