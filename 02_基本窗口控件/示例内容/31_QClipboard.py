import sys

from PyQt5.QtCore import QMimeData
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QDialog, QGridLayout, QLabel, QPushButton


class Form(QDialog):
    """主窗口"""
    def __init__(self, parent=None):
        super(Form, self).__init__(parent=parent)
        text_copy_btn = QPushButton("&Copy text")       # 复制文本
        text_paste_btn = QPushButton("Paste &Text")     # 粘贴文本
        html_copy_btn = QPushButton("C&opy HTML")       # 复制html文本
        html_paste_btn = QPushButton("Paste &HTML")     # 粘贴html文本
        image_copy_btn = QPushButton("Co&py Image")     # 复制Image图像
        image_paste_btn = QPushButton("Paste &Image")   # 粘贴Image图像

        self.text_label = QLabel("Original text")
        self.image_label = QLabel()
        self.image_label.setMaximumSize(128, 128)
        self.image_label.setPixmap(QPixmap("02_基本窗口控件/示例内容/sources/images/python-simple-color-96.png"))
        
        grid_layout = QGridLayout()
        grid_layout.addWidget(text_copy_btn, 0, 0)
        grid_layout.addWidget(html_copy_btn, 0, 1)
        grid_layout.addWidget(image_copy_btn, 0, 2)
        grid_layout.addWidget(text_paste_btn, 1, 0)
        grid_layout.addWidget(html_paste_btn, 1, 1)
        grid_layout.addWidget(image_paste_btn, 1, 2)
        grid_layout.addWidget(self.text_label, 2, 0, 1, 2)
        grid_layout.addWidget(self.image_label, 2, 2)
        self.setLayout(grid_layout)

        text_copy_btn.clicked.connect(self.copy_text)
        text_paste_btn.clicked.connect(self.paste_text)
        html_copy_btn.clicked.connect(self.copy_html)
        html_paste_btn.clicked.connect(self.paste_html)
        image_copy_btn.clicked.connect(self.copy_image)
        image_paste_btn.clicked.connect(self.paste_image)

    def copy_text(self):
        clipboard = QApplication.clipboard()
        clipboard.setText("I've been clipped!")   # 将文本设置到剪贴板中

    def paste_text(self):
        clipboard = QApplication.clipboard()
        self.text_label.setText(clipboard.text())   # 将剪贴板内的文本内容设置到label

    def copy_html(self):
        mime_data = QMimeData()
        mime_data.setHtml("<b> Bold and <span style='color: red;'>Red</span></b>")
        clipboard = QApplication.clipboard()
        clipboard.setMimeData(mime_data)   # 将html文本设置入剪贴板
    
    def paste_html(self):
        clipboard = QApplication.clipboard()
        mime_data = clipboard.mimeData()
        if mime_data.hasHtml():
            self.text_label.setText(mime_data.html())   # 将剪贴板中的html文本 设置到label

    def copy_image(self):
        clipboard = QApplication.clipboard()
        clipboard.setPixmap(QPixmap("02_基本窗口控件/示例内容/sources/images/python-color-128.png"))   # 将另一图片设置入剪贴板
    
    def paste_image(self):
        clipboard = QApplication.clipboard()
        self.image_label.setPixmap(QPixmap())


if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = Form()
    win.show()
    sys.exit(app.exec())