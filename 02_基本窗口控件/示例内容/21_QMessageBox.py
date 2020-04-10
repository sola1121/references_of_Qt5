import sys

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox


class MessageBoxDemo(QWidget):
    """主窗口"""
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle("QMessageBox 使用")
        self.resize(320, 200)

        vbox = QVBoxLayout()
        self.label = QLabel()
        vbox.addWidget(self.label)

        btn = QPushButton()
        btn.setText("弹出各种对话框")
        btn.clicked.connect(self.msg)

        vbox.addWidget(btn)
        self.setLayout(vbox)

    def msg(self):
        info = QMessageBox.information(self, "标题", "消息对话框正文", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        question = QMessageBox.question(self, "标题", "提问框消息正文", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        warn = QMessageBox.warning(self, "标题", "警告框消息正文", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        critical = QMessageBox.critical(self, "标题", "严重错误框消息正文", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        about = QMessageBox.about(self, "标题", "关于对话框消息正文")
        format_html = f"<span style='color: green;'>info: {info}</span><br><span style='color: blue;'>question: {question}</span><br>\
                        <span style='color: orange;'>warn: {warn}</span><br><span style='color: red;'>critical: {critical}</span><br>\
                        <span style='color: block;'>about: {about}</span>"
        self.label.setText(format_html)
        if info == QMessageBox.Yes:
            print("选中了info yes")


if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = MessageBoxDemo()
    win.show()
    sys.exit(app.exec())