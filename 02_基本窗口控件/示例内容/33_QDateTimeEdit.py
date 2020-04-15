import sys

from PyQt5.QtCore import QDateTime
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QDateTimeEdit, QPushButton, QStatusBar, QMessageBox


class DateTimeEditDemo(QWidget):
    """主窗口"""
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle("QDateTimeEdit 使用")
        self.resize(320, 100)
        date_time = QDateTime.currentDateTime()

        self.datetime_edit = QDateTimeEdit(date_time)   # 初始化时设置初始值为当前日期时间
        # self.datetime_edit.setDateTime(date_time)
        self.datetime_edit.setDisplayFormat("yyyy-MM-dd HH:mm:ss")   # 设置显示格式
        self.datetime_edit.setDateTimeRange(date_time.addYears(-1), date_time.addYears(1))   # 设置时间范围
        self.datetime_edit.setCalendarPopup(True)   # 允许使用Calendar

        self.datetime_edit.dateTimeChanged.connect(self.datetime_change)   # 会向槽函数传递QDateTime
        self.datetime_edit.dateChanged.connect(self.date_change)   # 会向槽函数传递QDate
        self.datetime_edit.timeChanged.connect(self.time_change)   # 会向槽函数传递QTime

        self.button = QPushButton()
        self.button.setText("获得日期和时间")
        self.button.clicked.connect(self.btn_click)
        self.status_bar = QStatusBar()

        vbox = QVBoxLayout(self)
        vbox.addWidget(self.datetime_edit)
        vbox.addWidget(self.button)
        vbox.addWidget(self.status_bar)

    def datetime_change(self, date_time):
        self.status_bar.showMessage(date_time.__str__())

    def date_change(self, date):
        self.status_bar.showMessage(date.__str__())

    def time_change(self, time):
        self.status_bar.showMessage(time.__str__())

    def btn_click(self, event):
        date_time = self.datetime_edit.dateTime()
        max_date_time = self.datetime_edit.maximumDateTime()
        max_date = self.datetime_edit.maximumDate()
        max_time = self.datetime_edit.maximumTime()
        min_date_time = self.datetime_edit.minimumDateTime()
        min_date = self.datetime_edit.minimumDate()
        min_time = self.datetime_edit.minimumTime()
        format_str = f"max_date_time: {max_date_time}\nmax_date: {max_date}\nmax_time: {max_time}\n\
                       min_date_time: {min_date_time}\nmin_time: {min_time}\nmin_time: {min_time}\n{event}"
        _ = QMessageBox.information(self, "显示QDateTime中的一些数据", format_str)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = DateTimeEditDemo()
    win.show()
    sys.exit(app.exec())