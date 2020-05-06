import sys, random

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QMenu, QTableWidget, QTableWidgetItem, 
                             QHBoxLayout, QHeaderView)


ROW = 9
COLUMN = 3


def generate_name():
    words = "abcdefghijklmnopqrstuvwxyz"
    length = random.randrange(3, 13, 1)
    name = str()
    for _ in range(length):
        name += words[random.randrange(0, len(words), 1)]
    return name.title()


class TableForm(QWidget):
    """主窗口"""
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle("QTableWidget 使用右键菜单")
        self.resize(500, 300)

        self.table_widget = QTableWidget()
        self.table_widget.setRowCount(ROW)
        self.table_widget.setColumnCount(COLUMN)
        self.table_widget.setHorizontalHeaderLabels(["姓名", "性别", "体重(kg)"])
        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # 允许右键产生
        self.table_widget.setContextMenuPolicy(Qt.CustomContextMenu)
        # 将右键菜单绑定到槽函数
        self.table_widget.customContextMenuRequested.connect(self.generate_menu)

        self.generate_data()

        h_layout = QHBoxLayout()
        h_layout.addWidget(self.table_widget)
        self.setLayout(h_layout)

    def generate_data(self):
        gender = ("female", "male")
        for row in range(0, ROW):
            for column in  range(0, COLUMN):
                if column == 0:
                    table_item = QTableWidgetItem(generate_name())
                elif column == 1:
                    table_item = QTableWidgetItem(gender[random.randint(0, 1)])
                elif column == 2:
                    table_item = QTableWidgetItem(str(random.randrange(40, 150)))
                else:
                    raise ValueError("列数据错误")
                self.table_widget.setItem(row, column, table_item)

    def generate_menu(self, pos):
        print("点击位置", pos)
        row_num = -1
        for item in self.table_widget.selectionModel().selection().indexes():
            row_num = item.row()
        
        # 表格中只有两条有效数据, 所以只在前两行支持右键弹出菜单
        if row_num > -1:
            menu = QMenu()
            action_1 = menu.addAction("选项 1")
            action_2 = menu.addAction("选项 2")
            action_3 = menu.addAction("选项 3")
            action = menu.exec_(self.table_widget.mapToGlobal(pos))   # 全局位置映射
            if action == action_1:
                print(action_1.text(), "触发, 对应", self.table_widget.item(row_num, 0).text(), 
                      self.table_widget.item(row_num, 1).text(), self.table_widget.item(row_num, 2).text())
            elif action == action_2:
                print(action_2.text(), "触发, 对应", self.table_widget.item(row_num, 0).text(), 
                      self.table_widget.item(row_num, 1).text(), self.table_widget.item(row_num, 2).text())
            elif action == action_3:
                print(action_3.text(), "触发, 对应", self.table_widget.item(row_num, 0).text(), 
                      self.table_widget.item(row_num, 1).text(), self.table_widget.item(row_num, 2).text())
            else:
                return None


if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = TableForm()
    win.show()
    sys.exit(app.exec())
