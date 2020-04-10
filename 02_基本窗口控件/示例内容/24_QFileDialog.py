import sys

from PyQt5.QtCore import QDir, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QTextEdit, QLineEdit, QFileDialog


class FileDialogDemo(QWidget):
    """主窗口"""

    root_dir = "c://" if sys.platform == "win32" else "/home"

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle("QFileDialog 使用")
        self.resize(500, 600)

        self.btn_1 = QPushButton()
        self.btn_1.setText("获得目录地址")
        self.btn_1.clicked.connect(self.get_directory)
        self.linedit = QLineEdit()

        self.btn_2 = QPushButton()
        self.btn_2.setText("读取图片")
        self.btn_2.clicked.connect(self.get_pic_file)
        self.label = QLabel()
        self.label.setMaximumWidth(500)
        self.label.setMaximumHeight(400)
        self.label.setAlignment(Qt.AlignCenter)

        self.btn_3 = QPushButton()
        self.btn_3.setText("读取文本")
        self.btn_3.clicked.connect(self.get_text_file)
        self.textedit = QTextEdit()

        vbox = QVBoxLayout()
        vbox.addWidget(self.btn_1)
        vbox.addWidget(self.linedit)
        vbox.addWidget(self.btn_2)
        vbox.addWidget(self.label)
        vbox.addWidget(self.btn_3)
        vbox.addWidget(self.textedit)
        self.setLayout(vbox)


    def get_directory(self):
        """只获取目录地址"""
        directory = QFileDialog.getExistingDirectory(parent=self, caption="获取目录", directory=FileDialogDemo.root_dir)
        self.linedit.setText(directory)

    def get_pic_file(self):
        """读取一个已经存在的图片"""
        picfile, ok = QFileDialog.getOpenFileName(parent=self, caption="获取图片文件", directory=FileDialogDemo.root_dir, filter="Image files(*.jpg *.png *.gif *.svg *.bmp)")
        if ok:
            self.label.setPixmap(QPixmap(picfile))

    def get_text_file(self):
        """读取文本内容"""
        file_dialog = QFileDialog(parent=self, caption="获取文本文件", directory=FileDialogDemo.root_dir)
        file_dialog.setFileMode(QFileDialog.AnyFile)
        # file_dialog.setFilter(QDir.Files)
        file_dialog.setNameFilter("all files (*)")

        if file_dialog.exec():
            filenames = file_dialog.selectedFiles()   # -> list(str)
            file = open(filenames[0], 'r', encoding="utf-8", errors='ignore')
            with file:
                data = file.read()
                self.textedit.setText(data)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = FileDialogDemo()
    win.show()
    sys.exit(app.exec())