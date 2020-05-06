import sys

from PyQt5.QtWidgets import (QApplication, QWidget, QStackedWidget, QWidget, QListWidget,
                             QHBoxLayout, QFormLayout, QLineEdit, QCheckBox, QRadioButton)


class StackedForm(QWidget):
    """主窗口"""
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle("QStackedWidget 使用")

        self.widget_1 = QWidget()
        self.widget_2 = QWidget()
        self.widget_3 = QWidget()
        self.set_widget_1()
        self.set_widget_2()
        self.set_widget_3()

        # 在左边的QListWidget
        self.leftlist = QListWidget()
        self.leftlist.addItem("姓名")
        self.leftlist.addItem("操作系统")
        self.leftlist.addItem("使用开发语言")
        self.leftlist.currentRowChanged.connect(self.display)   # 向槽函数传入索引

        # 实例化QStackedWidget, 并向其中添加窗口控件
        self.stack_widget = QStackedWidget()
        self.stack_widget.addWidget(self.widget_1)
        self.stack_widget.addWidget(self.widget_2)
        self.stack_widget.addWidget(self.widget_3)

        h_layout = QHBoxLayout()
        h_layout.addWidget(self.leftlist)
        h_layout.addWidget(self.stack_widget)
        self.setLayout(h_layout)


    def display(self, index):
        self.stack_widget.setCurrentIndex(index)   # QListWidget的索引正好对应QStackedWidget的索引

    def set_widget_1(self):
        form_layout = QFormLayout()
        form_layout.addRow("姓氏:", QLineEdit())
        form_layout.addRow("名字:", QLineEdit())
        self.widget_1.setLayout(form_layout)

    def set_widget_2(self):
        h_layout = QHBoxLayout()
        h_layout.addWidget(QRadioButton("Windows"))
        h_layout.addWidget(QRadioButton("Linux"))
        h_layout.addWidget(QRadioButton("macOS"))
        
        form_layout = QFormLayout()
        form_layout.addRow("使用系统", h_layout)
        form_layout.addRow("其他", QLineEdit())

        self.widget_2.setLayout(form_layout)

    def set_widget_3(self):
        h_layout = QHBoxLayout()
        h_layout.addWidget(QCheckBox("Python"))
        h_layout.addWidget(QCheckBox("Golang"))
        h_layout.addWidget(QCheckBox("C"))
        h_layout.addWidget(QCheckBox("Javascript"))

        form_layout = QFormLayout()
        form_layout.addRow("开发语言", h_layout)

        self.widget_3.setLayout(form_layout)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = StackedForm()
    win.show()
    sys.exit(app.exec())