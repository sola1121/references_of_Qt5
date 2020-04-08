import sys

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QRadioButton, QButtonGroup


class RadioDemo(QWidget):
    """主窗口"""
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle("QRadioButton 使用")
        self.resize(320, -1)

        # 没有定义Group的RadioButton, 直接放在布局管理vbox中, 成一组
        vbox = QVBoxLayout()
        self.label = QLabel()
        vbox.addWidget(self.label)
        vbox.addStretch()

        # 单选按钮1, 默认选中
        self.radio_btn_1 = QRadioButton()
        self.radio_btn_1.setChecked(True)
        self.radio_btn_1.setText("单选按钮1")
        self.radio_btn_1.toggled.connect(lambda:self.state_btn(self.radio_btn_1))
        # 单选按钮2
        self.radio_btn_2 = QRadioButton()
        self.radio_btn_2.setText("单选按钮2")
        self.radio_btn_2.toggled.connect(lambda:self.state_btn(self.radio_btn_2))

        vbox.addWidget(self.radio_btn_1)
        vbox.addWidget(self.radio_btn_2)

        # 定义了Group的RadioButton, 应该为一组
        # 单选按钮3
        self.radio_btn_3 = QRadioButton()
        self.radio_btn_3.setChecked(True)
        self.radio_btn_3.setText("单选按钮3")
        # self.radio_btn_3.toggled.connect(lambda:self.state_btn(self.radio_btn_3))
        # 单选按钮4
        self.radio_btn_4 = QRadioButton()
        self.radio_btn_4.setText("单选按钮4")
        # self.radio_btn_4.toggled.connect(lambda:self.state_btn(self.radio_btn_4))

        self.btn_group = QButtonGroup(vbox)
        # self.btn_group.setParent()
        self.btn_group.addButton(self.radio_btn_3, 3)
        self.btn_group.addButton(self.radio_btn_4, 4)
        self.btn_group.buttonClicked.connect(self.state_btn2)

        vbox.addWidget(self.radio_btn_3)
        vbox.addWidget(self.radio_btn_4)

        self.setLayout(vbox)

    def state_btn(self, radio_btn):
        self.label.setText("%s, check=%s" % (radio_btn.text(), radio_btn.isChecked()))

    def state_btn2(self, radio_btn):
        self.label.setText("分组器单击触发, 控件id: %d,  %s, check=%s" 
                            %(self.btn_group.checkedId(), radio_btn.text(), radio_btn.isChecked()))


if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = RadioDemo()
    win.show()
    sys.exit(app.exec())