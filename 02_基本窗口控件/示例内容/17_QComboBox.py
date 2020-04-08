import sys

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QComboBox, QLabel


class ComboBoxDemo(QWidget):
    """主窗口"""
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle("QComboBox 下拉框使用")
        self.resize(200, -1)

        vbox = QVBoxLayout()

        self.label = QLabel()
        vbox.addWidget(self.label)
        vbox.addStretch(1)

        # 初始化QComboBox, 并通过addItems()添加一个item列表
        self.combobox = QComboBox()
        self.combobox.addItems(["Python", "Golang", "JavaScript", "C"])
        self.combobox.currentIndexChanged.connect(self.select_change)   # 会自动向关联函数传入索引

        vbox.addWidget(self.combobox)
        self.setLayout(vbox)
        
    def select_change(self, index):
        color = "white"
        if index == 0:
            color = "#003366"
        elif index == 1:
            color = "#00CCFF"
        elif index == 2:
            color = "#FFCC33"
        elif index == 3:
            color = "#242424"
        current_text = self.combobox.currentText()
        format_html = f"<span style='color: {color}'>● {index}, {current_text}</span>"
        self.label.setText(format_html)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = ComboBoxDemo()
    win.show()
    sys.exit(app.exec())