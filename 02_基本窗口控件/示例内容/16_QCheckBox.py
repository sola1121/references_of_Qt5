import sys

from PyQt5 .QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QCheckBox, QGroupBox


class CheckBoxDemo(QWidget):
    """主窗口"""
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle("QCheckBox 使用")
        self.resize(320, -1)

        vbox_main = QVBoxLayout()   # 主布局管理器
        hbox_sub = QHBoxLayout()   # 次布局管理器, 用于管理check box按钮

        self.label = QLabel()
        vbox_main.addWidget(self.label)
        vbox_main.addStretch(1)

        # 初始化QGroupBox, 并设置了分组名
        group_box = QGroupBox("Group Box - checkbox")
        group_box.setFlat(True)

        self.check_box_1 = QCheckBox("复选框_1")
        self.check_box_1.setChecked(True)
        self.check_box_1.stateChanged.connect(lambda : self.state_btn(self.check_box_1))   # stateChanged 状态发生变化触发

        self.check_box_2 = QCheckBox("复选框_2")
        self.check_box_2.toggled.connect(lambda : self.state_btn(self.check_box_2))   # toggle 切换的时候触发

        self.check_box_3 = QCheckBox("复选框_3")
        self.check_box_3.setTristate(True)   # 是一个三态复选框
        self.check_box_3.setCheckState(Qt.PartiallyChecked)   # 设置成半选中状态
        self.check_box_3.stateChanged.connect(lambda : self.state_btn(self.check_box_3))   # stateChanged 状态发生变化触发

        # 向水平布局管理器中添加内容
        hbox_sub.addWidget(self.check_box_1)
        hbox_sub.addWidget(self.check_box_2)
        hbox_sub.addWidget(self.check_box_3)

        # 设置GroupBox的布局管理器为已布局了的水平管理器
        group_box.setLayout(hbox_sub)
        # 主布局管理器接管groupBox
        vbox_main.addWidget(group_box)

        self.setLayout(vbox_main)   # 主窗口设置管理器

    def state_btn(self, check_box):
        format_html = "当前: <span style='color: green;'><b>{cur_ckb}</b> check: {cur_ckb_check}; checkState: {cur_ckb_checkState}</span><br>\
                       <span>{ckb1} check:{ckb1_check}; checkState: {ckb1_checkState}</span><br>\
                       <span>{ckb2} check:{ckb2_check}; checkState: {ckb2_checkState}</span><br>\
                       <span>{ckb3} check:{ckb3_check}; checkState: {ckb3_checkState}</span>"

        self.label.setText(format_html.format(
            cur_ckb=check_box.text(), cur_ckb_check=check_box.isChecked(), cur_ckb_checkState=check_box.checkState(),
            ckb1=self.check_box_1.text(), ckb1_check=self.check_box_1.isChecked(), ckb1_checkState=self.check_box_1.checkState(),
            ckb2=self.check_box_2.text(), ckb2_check=self.check_box_2.isChecked(), ckb2_checkState=self.check_box_2.checkState(),
            ckb3=self.check_box_3.text(), ckb3_check=self.check_box_3.isChecked(), ckb3_checkState=self.check_box_3.checkState(),
        ))


if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = CheckBoxDemo()
    win.show()
    sys.exit(app.exec())
    