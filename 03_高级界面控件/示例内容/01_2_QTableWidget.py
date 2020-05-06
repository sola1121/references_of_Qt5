import sys

from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QHBoxLayout, QTableWidgetItem, QHeaderView


class TableForm(QWidget):
    """主窗口"""
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle("QTableWidget 使用")
        self.resize(400, 300)

        self.table_widget = QTableWidget()
        self.table_widget.setRowCount(4)   # 共4行
        self.table_widget.setColumnCount(3)   # 共3列
        self.table_widget.setHorizontalHeaderLabels(["姓名", "性别", "体重(kg)"])   # 水平标签
        self.table_widget.setVerticalHeaderLabels(["行1", "行2", "行3", "行4"])   # 垂直标签
        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)   # 设置表格拉伸
        
        self.create_table_item()

        h_layout = QHBoxLayout()
        h_layout.addWidget(self.table_widget)
        self.setLayout(h_layout)

    def create_table_item(self):
        """向表格控件中添加QTableWidgetItem"""
        new_item = QTableWidgetItem("名称 1")
        self.table_widget.setItem(0, 0, new_item)

        new_item = QTableWidgetItem("性别 1")
        self.table_widget.setItem(0, 1, new_item)

        new_item = QTableWidgetItem("体重 1")
        self.table_widget.setItem(0, 2, new_item)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = TableForm()
    win.show()
    sys.exit(app.exec())
