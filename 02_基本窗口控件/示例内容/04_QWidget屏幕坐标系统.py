import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel


app = QApplication(sys.argv)

widget = QWidget()

btn = QPushButton(parent=widget)

btn.setText("按钮")

# 以QWidget左上角为(0, 0)
btn.move(20, 20)

# 不同的操作系统可能对窗口的最小宽度有规定, 若设置宽度小于规定值, 则会以规定值进行显示
widget.resize(600, 400)

# 以屏幕上左上角为(0, 0)点
widget.move(250, 200)


label = QLabel(parent=widget)
label.setGeometry(60, 60, 500, 300)

widget.setWindowTitle("PyQt 坐标系统")
widget.show()


info = "QWidget对象窗口的坐标和大小\n\
QWidget.x() = {QWx}, QWidget.y() = {QWy}, \n\
QWidget.width() = {QWw}, QWidget.height = {QWh} \n\n\
窗口客户区的坐标和大小\n\
QWidget.geometry().x() = {QWgx}, QWidget.geometry().y() = {QWgy}, \n\
QWidget.geometry().width() = {QWgw}, QWidget.geometry().height() = {QWgh}\n".format(
            QWx = widget.x(), QWy = widget.y(),
            QWw = widget.width(), QWh = widget.height(),
            QWgx = widget.geometry().x(), QWgy = widget.geometry().y(),
            QWgw = widget.geometry().x(), QWgh = widget.geometry().y()
        )

label.setText(info)


sys.exit(app.exec())
