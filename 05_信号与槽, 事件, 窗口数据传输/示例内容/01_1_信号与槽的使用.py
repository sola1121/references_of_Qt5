import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox


def show_msg(widget):
    QMessageBox.information(widget, "消息提示框", "弹出测试信息.")


app = QApplication(sys.argv)
widget = QWidget()
btn = QPushButton("点击测试按钮", widget)
btn.clicked.connect(lambda : show_msg(widget))   # 连接信号clicked到槽函数
widget.show()
sys.exit(app.exec())
