import sys

from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton


app = QApplication(sys.argv)
win = QWidget()
win.setWindowTitle("通过QWebEngineView的子QWebEnginePage.runJavaScript(str, callable)调用页面的js")

html_file = open("03_高级界面控件/示例内容/sources/htmls/uerlogin.html", 'r')

view = QWebEngineView()
view.setHtml(html_file.read())


# 如果调用的js方法有返回值, 用于处理这个返回值
def js_callback(result):
    print(result)


# 通过QWebEnginePage的runJavaScript(加载的页面中的js函数名, 用以处理js函数返回值的py函数调用指定的js函数, 并获取其返回值
def js_add_value():
    view.page().runJavaScript("addValue()", js_callback)

def js_remove_value():
    view.page().runJavaScript("removeValue()", js_callback)

button_1 = QPushButton("设置内容")
button_2 = QPushButton("移除内容")
button_1.clicked.connect(js_add_value)
button_2.clicked.connect(js_remove_value)
# 按钮连接js_add_value槽函数

layout = QVBoxLayout()
layout.addWidget(view)
layout.addWidget(button_1)
layout.addWidget(button_2)
win.setLayout(layout)

win.show()
sys.exit(app.exec())