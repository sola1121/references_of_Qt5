import sys

from PyQt5.QtGui import QBrush, QColor
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QTableWidget, QTableWidgetItem


class TableForm(QWidget):
    """主窗口"""
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle("QTableWidget 表格快速定位")
        self.resize(600, 800)
        
        # 初始化QTableWidget
        table_widget = QTableWidget()
        table_widget.setRowCount(30)
        table_widget.setColumnCount(4)
        
        for m in range(30):
            for n in range(4):
                item_content = "(%d, %d)" % (m , n)
                table_widget.setItem(m, n, QTableWidgetItem(item_content))
        
        h_layout = QHBoxLayout()
        h_layout.addWidget(table_widget)
        self.setLayout(h_layout)

        # 遍历表格查找对应项
        text = "(10, 1)"
        items = table_widget.findItems(text, Qt.MatchExactly)
        item = items[0]

        # 选中单元格
        item.setSelected(True)
        # 设置单元格的背景颜色
        item.setForeground(QBrush(QColor(255, 0, 0)))

        row = item.row()
        # 通过鼠标滚轮定位, 快速定位
        table_widget.verticalScrollBar().setSliderPosition(row)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = TableForm()
    win.show()
    sys.exit(app.exec())
