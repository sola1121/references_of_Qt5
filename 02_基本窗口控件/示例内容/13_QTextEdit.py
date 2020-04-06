import sys
import urllib3

from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QTextEdit, QPushButton


def request_url(url):
    if url is not None:
        http = urllib3.PoolManager()
        try:
            resp = http.request("GET", url, timeout=5, headers={
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/80.0.3987.149 Chrome/80.0.3987.149 Safari/537.36"
            })
            if resp.status == 200:
                return str(resp.data, encoding="utf-8")
            else:
                return "<span color='red'>请求url出错: {}</span>".format(resp.status)
        except Exception as ex:
            return "<span color='red'>建立连接出错: {}</span>".format(ex.__str__())
    else:
        return "<span color='red'>没有数据.</span>"


class TextEditDemo(QWidget):
    """主窗口"""
    def __init__(self, parent=None):
        super().__init__(parent=None)
        self.setWindowTitle("TextEdit 多行文本框")
        self.resize(600, 400)
        
        vbox = QVBoxLayout()
        self.setLayout(vbox)

        self.linedit = QLineEdit()
        self.linedit.setPlaceholderText("输入url, 如; http://www.mypy-lang.org")
        url_validator = QRegExpValidator()
        url_validator.setRegExp(QRegExp(r"^((ht|f)tps?):\/\/[\w\-]+(\.[\w\-]+)+([\w\-.,@?^=%&:\/~+#]*[\w\-@?^=%&\/~+#])?$"))
        self.linedit.setValidator(url_validator)

        # QTextEdit
        self.textedit = QTextEdit()
        
        btn_plain_text = QPushButton()
        btn_plain_text.setText("显示文本")
        btn_plain_text.clicked.connect(self.get_plain_text)
        btn_html_text = QPushButton()
        btn_html_text.setText("显示HTMl")
        btn_html_text.clicked.connect(self.get_html_text)

        vbox.addWidget(self.linedit)
        vbox.addWidget(self.textedit)
        vbox.addWidget(btn_plain_text)
        vbox.addWidget(btn_html_text)

    def get_plain_text(self):
        """以纯文本设置"""
        text = request_url(self.linedit.text())
        self.textedit.clear()
        self.textedit.setPlainText(text)

    def get_html_text(self):
        """以HTML格式设置"""
        text = request_url(self.linedit.text())
        self.textedit.clear
        self.textedit.setHtml(text)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = TextEditDemo()
    win.show()
    sys.exit(app.exec())
