import sys

from PyQt5.QtCore import pyqtProperty, QUrl
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QMessageBox
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWebChannel import QWebChannel


class MyShareObject(QWidget):
    """用于传递的对象"""
    def __init__(self):
        super().__init__()

    def _getValue(self):
        return "100"
    
    def _setValue(self, s):
        print("获得页面参数: %s" % s)
        QMessageBox.information(self, "_setValue", "获得页面参数: %s" % s)
    
    # 对外发布的方法
    sVal = pyqtProperty(str, fget=_getValue, fset=_setValue)


app = QApplication(sys.argv)
win = QWidget()
win.setWindowTitle("Web页面中JavaScript也QWebEngineView交互")

remote_url = "http://127.0.0.1:5500/03_高级界面控件/示例内容/sources/htmls/qwebchannel.html"

# 用于传输的QObject子对象
my_object = MyShareObject()

# 创建QWebEngineView对象
view = QWebEngineView()
view.load(QUrl(remote_url))

# 创建一个QWebChannel对象, 用来传递PyQt的参数到JavaScript
channle = QWebChannel()
channle.registerObject("bridge", my_object)

view.page().setWebChannel(channle)

layout = QVBoxLayout()
layout.addWidget(view)
win.setLayout(layout)

win.show()
sys.exit(app.exec())