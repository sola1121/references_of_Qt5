import sys

from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QApplication, QWidget, QCalendarWidget, QLabel


class CalendarDemo(QWidget):
    """主窗口"""
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.calendar = QCalendarWidget(parent=self)
        self.calendar.setMinimumDate(QDate(1980,1, 1))   # 设置最小日期
        self.calendar.setMaximumDate(QDate(3000, 1, 1))   # 设置最大日期
        self.calendar.setGridVisible(True)   # 设置网格可见
        self.calendar.move(20, 20)
        self.calendar.clicked.connect(self.show_date)   # 单击时会将点击到的QDate传递给槽函数

        self.label = QLabel(parent=self)
        date = self.calendar.selectedDate()
        self.label.setText(date.toString("yyyy-MM-dd dddd"))
        self.label.move(20, 300)
        self.setGeometry(100, 100, 460, 360)
        self.setWindowTitle("QCalendarWidget 使用")

    def show_date(self, date):
        self.label.setText(date.toString("yyyy-MM-dd dddd"))


if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    win = CalendarDemo()
    win.show()
    clicked_value = win.calendar.clicked
    sys.exit(app.exec())