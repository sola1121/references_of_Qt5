import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QTreeWidget, QTreeWidgetItem, QHBoxLayout


class TreeWidgetDemo(QWidget):
    """主窗口"""
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle("QTreeWidget 使用")
        
        # 实例化
        self.tree_widget = QTreeWidget()
        # 设置列数
        self.tree_widget.setColumnCount(2)
        # 设置树形控件头部标题
        self.tree_widget.setHeaderLabels(["键", "值"])

        # 根节点
        root = QTreeWidgetItem()
        root.setText(0, "根")
        root.setText(1, "---")

        # 设置子节点 1
        child_1 = QTreeWidgetItem(root)
        child_1.setText(0, "子 1 键")   # 第1列
        child_1.setText(1, "子 1 值")   # 第2列
        child_1.setIcon(0, QIcon("03_高级界面控件/示例内容/sources/python-96.png"))   # 为第1列添加图标

        # 设置子节点 2
        child_2 = QTreeWidgetItem(root)
        child_2.setText(0, "子 2 键")   # 第1列
        child_2.setText(1, "子 2 值")   # 第2列
        child_2.setIcon(0, QIcon("03_高级界面控件/示例内容/sources/golang-96.png"))   # 为第2列添加图标

        self.tree_widget.addTopLevelItem(root)
        self.tree_widget.clicked.connect(self.tree_click)

        h_layout = QHBoxLayout()
        h_layout.addWidget(self.tree_widget)
        self.setLayout(h_layout)

    def tree_click(self, qmodelindex):
        print("信号传入值", qmodelindex)
        item = self.tree_widget.currentItem()
        print("键 = %s, 值 = %s" %(item.text(0), item.text(1)))


if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = TreeWidgetDemo()
    win.show()
    sys.exit(app.exec())
