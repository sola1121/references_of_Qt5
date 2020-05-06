import sys

from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QBoxLayout, QMessageBox

class ListWidget(QListWidget):
    """继承QListWidget"""
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle("QListWidget 窗口使用")
        self.resize(300, 120)
        self.itemClicked.connect(self.click_item)

    def click_item(self, QListWidgetItem):
        """itemClicked"""
        QMessageBox.information(self, "list widget item", "selected: " + QListWidgetItem.text())


if __name__ == "__main__":

    app = QApplication(sys.argv)

    list_widget = ListWidget()
    list_widget.addItem("Item 1")
    list_widget.addItem("Item 2")
    list_widget.addItem("Item 3")
    list_widget.addItem("Item 4")
    list_widget.show()

    sys.exit(app.exec())