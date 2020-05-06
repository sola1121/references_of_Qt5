import sys

from PyQt5.QtWidgets import (QApplication, QTabWidget, QWidget, 
                             QHBoxLayout, QFormLayout, QLineEdit, QCheckBox, QRadioButton)


class TabForm(QTabWidget):
    """主窗口"""
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle("QTabWidget 使用")

        self.widget_1 = QWidget()
        self.widget_2 = QWidget()
        self.widget_3 = QWidget()
        self.set_widget_1()
        self.set_widget_2()
        self.set_widget_3()

        # 选项卡中添加窗口控件
        self.addTab(self.widget_1, "姓名")
        self.addTab(self.widget_2, "操作系统")
        self.addTab(self.widget_3, "使用开发语言")

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
    win = TabForm()
    win.show()
    sys.exit(app.exec())