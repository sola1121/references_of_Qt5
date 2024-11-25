import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Qt


class MainWin(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setWindowTitle("Say:")  
        self.resize(500, 400)  
          
        # 将放在中央的部件  
        center_widget = QWidget()  
  
        # 创建标签并设置文本和居中对齐  
        label = QLabel("Hello, world.")  
        label.setAlignment(Qt.AlignCenter)

        # 创建垂直布局并添加标签  
        layout = QVBoxLayout()  
        layout.addWidget(label)

        center_widget.setLayout(layout)    # 将垂直布局放在中央
        self.setCentralWidget(center_widget)    # 将QWidget放在中央


if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    win = MainWin()
    win.show()
    sys.exit(app.exec())