import os, collections

from PySide6.QtWidgets import QWidget, QGridLayout, QVBoxLayout, QTextEdit, QLabel, \
                              QProgressBar, QPushButton, QFileDialog, QMessageBox
from PySide6.QtCore import Qt

from core_copy import CopyThread, mutex


class Ui_MainWindow(QWidget):
    """
    主窗口
    """
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        # 窗口设置
        self.setWindowTitle("文件复制器")
        self.setFixedWidth(720)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMaximizeButtonHint)

        # 将要复制的源文件列表, 目标地址
        self.copy_files = collections.OrderedDict()
        self.target_address = str()

        # 创建布局
        grid_layout = QGridLayout()
        vbox_layout = QVBoxLayout()
        
        # 源文件文本框
        self.sourfile_desc = QTextEdit()
        self.sourfile_desc.setReadOnly(True)
        self.sourfile_desc.setText("源文件地址")

        # 目标地址标签
        self.tagefile_desc = QLabel()
        self.tagefile_desc.setText("目标地址")

        # 进度条
        self.probar = QProgressBar()

        # 操作按扭
        self.sourfile_btn = QPushButton("添加源文件")
        self.tagefile_btn = QPushButton("目标地址")
        self.restfile_btn = QPushButton("清空内容")
        self.start_btn = QPushButton("开始")
        
        # 按钮的槽与信号
        self.sourfile_btn.clicked.connect(self.choice_file)
        self.tagefile_btn.clicked.connect(self.set_target_address)
        self.restfile_btn.clicked.connect(self.rset_file_list)
        self.start_btn.clicked.connect(self.start_copy_file)

        # 设置布局
        grid_layout.addWidget(self.sourfile_desc, 0, 0, 2, 3)
        vbox_layout.addWidget(self.sourfile_btn)
        vbox_layout.addWidget(self.tagefile_btn)
        vbox_layout.addWidget(self.restfile_btn)
        grid_layout.addLayout(vbox_layout, 0, 3)
        grid_layout.addWidget(self.tagefile_desc, 2, 0, 1, 3)
        grid_layout.addWidget(self.start_btn, 2, 3)
        grid_layout.addWidget(self.probar, 3, 0, 1, 4)

        # 添加格栅到窗口
        self.setLayout(grid_layout)

    def choice_file(self):
        """选择文件"""
        source_file = QFileDialog().getOpenFileName()
        if source_file[0] == "":
            QMessageBox.warning(self, "警告", "选择文件为空.")
        elif source_file[0] in self.copy_files.keys():
            QMessageBox.warning(self, "警告", "请勿重复选择文件.")
        else:
            self.copy_files[source_file[0]] = 0.0
        self.sourfile_desc.setText(format_textedit(self.copy_files))

    def set_target_address(self):
        """设置目标目录 """
        starget_address = QFileDialog().getExistingDirectory()
        if starget_address != "":
            self.tagefile_desc.setText(starget_address)
            self.tagefile_desc.setToolTip(starget_address)
            self.target_address = starget_address

    def rset_file_list(self):
        """重新进行复制操作"""
        # 清空将要复制的文件
        self.copy_files = collections.OrderedDict()
        self.target_address = str()
        # 重新设置文字框内容, 进度条
        self.sourfile_desc.setText("源文件地址")
        self.tagefile_desc.setText("目标地址")
        self.tagefile_desc.setToolTip(self.tagefile_desc.text())
        self.probar.setValue(0)

    def start_copy_file(self):
        """开始进行复制操作"""
        # 关闭所有按钮, 设置进度条为0
        self.buttons_enable(False)
        self.probar.setValue(0)

        if self.copy_files is None or self.target_address == "":
            QMessageBox.critical(self, "错误", "请设置源文件和目标地址.")
            self.buttons_enable(True)
        else:
            # 创建线程, 进行复制操作
            self.copy_thread = CopyThread(self.copy_files, self.target_address, mutex)
            self.copy_thread.status_signal.connect(self.update_copy_progress)   # 运行中的自定义信号
            self.copy_thread.finished.connect(self.thread_finished)   # 完成后的信号
            self.copy_thread.start()
        
    def thread_finished(self):
        """线程完成时"""
        # 开启所有按钮为可用, 设置进度为100
        self.buttons_enable(True)
        self.probar.setValue(100)

    def update_copy_progress(self, odit: collections.OrderedDict):
        """线程运行时, 复制的进度"""
        # 更新TextEdit
        self.sourfile_desc.setText(format_textedit(odit))

        # 更新进度条
        self.probar.setValue(sum(odit.values())/len(odit)*100)

    def buttons_enable(self, bl: bool):
        """设置所有按钮的可用性"""
        self.sourfile_btn.setEnabled(bl)
        self.tagefile_btn.setEnabled(bl)
        self.restfile_btn.setEnabled(bl)
        self.start_btn.setEnabled(bl)


def format_textedit(odit: collections.OrderedDict) -> str:
    """格式化文本框"""
    ret_text = str()
    for key, val in odit.items():
        ret_text += os.path.basename(key) + " <b>-处理进度 " + str(round(val*100, 2)) + "%</b><br>"
    return ret_text
