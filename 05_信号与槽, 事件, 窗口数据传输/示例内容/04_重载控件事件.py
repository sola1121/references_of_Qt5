import sys

from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt, QTimer, QEvent
from PyQt5.QtWidgets import QApplication, QWidget, QMenu


class WinForm(QWidget):
    """主窗口"""
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle("重载控件事件")
        self.resize(400, 300)

        self.justDoubleClicked =  False   # 内置阐述
        self.key = str()
        self.text = str()
        self.message = str()

        QTimer.singleShot(0, self.giveHelp)

    def giveHelp(self):
        self.text = "请点击这里出触发追踪鼠标功能"
        self.update()   # 重绘事件, 也就是触发paintEvent函数

    def closeEvent(self, event):
        """重载控件关闭事件"""
        print("控件关闭")
        event.accept()

    def contextMenuEvent(self, event):
        """重载控件上下文菜单事件"""
        menu = QMenu(self)
        action_one = menu.addAction("&One")
        action_two = menu.addAction("&Two")
        action_one.triggered.connect(self.action_one_func)
        action_two.triggered.connect(self.action_two_func)

        if not self.message:
            menu.addSeparator()
            action_three = menu.addAction("&Three")
            action_three.triggered.connect(self.action_three_func)

        menu.exec(event.globalPos())

    def action_one_func(self):
        self.message = "Menu Option One"
        self.update()
    
    def action_two_func(self):
        self.message = "Menu Option Two"
        self.update()

    def action_three_func(self):
        self.message = "Menu Option Three"
        self.update()

    def paintEvent(self, event):
        """重载绘制事件"""
        text = self.text
        i = text.find("\n\n")
        if i >= 0:
            text = text[0:i]
        if self.key:
            text += "\n\n你按下了: {}".format(self.key)
        
        painter = QPainter(self)
        painter.setRenderHint(QPainter.TextAntialiasing)
        painter.drawText(self.rect(), Qt.AlignCenter, text)
        if self.message:
            painter.drawText(self.rect(), Qt.AlignBottom | Qt.AlignHCenter, self.message)
            QTimer.singleShot(5000, self.clearMessage)
            QTimer.singleShot(5000, self.update)
    
    def clearMessage(self):
        self.message = str()

    def resizeEvent(self, event):
        """重载实现调整窗口大小事件"""
        self.text = "调整窗口大小为: QSize({}, {})".format(event.size().width(), event.size().height())
        self.update()

    def mouseReleaseEvent(self, event):
        """重载鼠标按键释放事件"""
        if self.justDoubleClicked:
            self.justDoubleClicked = False
        else:
            self.setMouseTracking(not self.hasMouseTracking())   # 单击鼠标
            if self.hasMouseTracking():
                self.text = "开启鼠标追踪功能.\n请移动鼠标观察!\n单击鼠标关闭这个功能."
            else:
                self.text = "关闭鼠标追踪功能.\n单击鼠标关闭这个功能."

            self.update()

    def mouseMoveEvent(self, event):
        """重载鼠标移动事件"""
        if not self.justDoubleClicked:
            globalPos = self.mapToGlobal(event.pos())   # 将窗口坐标转换为屏幕坐标
            self.text = "鼠标坐标:\n窗口坐标为QPoint({0}, {1})\n屏幕坐标为QPoint({2}, {3})".format(
                         event.pos().x(), event.pos().y(), globalPos.x(), globalPos.y()
            )
            self.update()

    def mouseDoubleClickEvent(self,  event):
        """重载鼠标双击事件"""
        self.justDoubleClicked = True
        self.text = "双击了鼠标"
        self.update()

    def keyPressEvent(self, event):
        """重载键盘按下事件"""
        self.key = str()
        if event.key() == Qt.Key_Home:
            self.key = "Home"
        elif event.key() == Qt.Key_End:
            self.key = "End"
        elif event.key() == Qt.Key_PageUp:
            if event.modifiers() & Qt.ControlModifier:
                self.key = "Ctrl+PageUp"
            else:
                self.key = "PageUp"
        elif event.key() == Qt.Key_PageDown:
            if event.modifiers() & Qt.ControlModifier:
                self.key = "Ctrl+PageDown" 
            else:
                self.key == "PageDown"
        elif Qt.Key_A <= event.key() and event.key() <= Qt.Key_Z:
            if event.modifiers() & Qt.ShiftModifier:
                self.key = "Shift+"
            self.key += event.text()

        if self.key:
            self.key = self.key
            self.update()
        else:
            QWidget.keyPressEvent(self, event)

    def event(self, event):
        """重载event函数, 实现其他事件, 适用于PyQt没有提供该事件的处理函数的情况. 
        Tab键由于设计焦点切换, 不会传递给keyPressEvent, 因此需要在这里重新定义"""
        if event.type() == QEvent.KeyPress and event.key() == Qt.Key_Tab:
            self.key = "在event()中捕获Tab键"
            self.update()
            return True
        return QWidget.event(self, event)


if __name__  == "__main__":

    app = QApplication(sys.argv)
    win = WinForm()
    win.show()
    sys.exit(app.exec())
