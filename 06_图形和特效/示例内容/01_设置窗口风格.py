import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QStyleFactory, QLabel, QComboBox


class WinForm(QWidget):
    """主窗口"""
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle("设置窗口的样式")
        self.resize(200, 100)

        self.label_style = QLabel("设置 Style:")
        self.combobox_style = QComboBox()

        # 从QStyleFactory中增加多个显示样式
        self.combobox_style.addItems(QStyleFactory.keys())

        # 选择当前窗口风格
        index = self.combobox_style.findText(QApplication.style().objectName(), Qt.MatchFixedString)

        # 设置当前窗口风格
        self.combobox_style.setCurrentIndex(index)
        
        # 通过combobox控件选择窗口风格
        self.combobox_style.activated[str].connect(self.handle_style_change)

        h_layout = QHBoxLayout()
        h_layout.addWidget(self.label_style)
        h_layout.addWidget(self.combobox_style)
        self.setLayout(h_layout)

    def handle_style_change(self, style):
        """让整个应用都应用这个风格, 参数style是可用的风格名"""
        # QApplication.setStyle(style)
        qstyle = QStyleFactory.create(style)
        QApplication.setStyle(qstyle)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = WinForm()
    win.show()
    sys.exit(app.exec())
