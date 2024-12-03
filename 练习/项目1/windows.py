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

        # 将要复制的源文件列表, 目标目录
        self.copy_files = collections.OrderedDict()   # 为 目录:进度(0~1)
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
        self.tagefile_btn = QPushButton("选择目标地址")
        self.restfile_btn = QPushButton("清空内容")
        self.start_btn = QPushButton("开始")
        self.stop_btn = QPushButton("停止")
        self.stop_btn.setEnabled(False)

        # 按钮的槽与信号
        self.sourfile_btn.clicked.connect(self.choice_file)
        self.tagefile_btn.clicked.connect(self.set_target_address)
        self.restfile_btn.clicked.connect(self.rset_file_list)
        self.start_btn.clicked.connect(self.start_copy_file)
        self.stop_btn.clicked.connect(self.stop_copy_file)

        # 设置布局
        grid_layout.addWidget(self.sourfile_desc, 0, 0, 2, 3)
        vbox_layout.addWidget(self.sourfile_btn)
        vbox_layout.addWidget(self.tagefile_btn)
        vbox_layout.addWidget(self.restfile_btn)
        grid_layout.addLayout(vbox_layout, 0, 3)
        grid_layout.addWidget(self.tagefile_desc, 2, 0, 1, 3)
        grid_layout.addWidget(self.start_btn, 2, 3)
        grid_layout.addWidget(self.probar, 3, 0, 1, 3)
        grid_layout.addWidget(self.stop_btn, 3, 3, 1, 1)

        # 添加格栅到窗口
        self.setLayout(grid_layout)

    def choice_file(self):
        """选择文件"""
        source_files = QFileDialog().getOpenFileNames()

        if source_files[0] == []:
            QMessageBox.warning(self, "警告", "未选择文件.")
            return

        for source_file in source_files[0]:
            if source_file in self.copy_files.keys():
                warning_format = f"请勿重复选择文件, {source_file} 已选择."
                QMessageBox.warning(self, f"警告", warning_format)
                return 

        for source_file in source_files[0]:
            self.copy_files[source_file] = 0.0
        self.sourfile_desc.setText(format_textedit(self.copy_files))

    def set_target_address(self):
        """设置目标目录 """
        starget_address = QFileDialog().getExistingDirectory()
        if starget_address == '':
            QMessageBox.warning(self, "警告", "目标地址为空.")
        else:
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

        # 重置将要复制的文件进度为0
        for key in self.copy_files.keys():
            self.copy_files[key] = 0.0
        self.sourfile_desc.setText(format_textedit(self.copy_files))

        # 线程的创建
        if not self.copy_files:
            QMessageBox.critical(self, "错误", "请设置源文件.")
            self.sourfile_desc.setText("源文件地址")
            self.buttons_enable(True)
        elif self.target_address == "":
            QMessageBox.critical(self, "错误", "请设置目标地址.")
            self.buttons_enable(True)
        else:
            # TODO: 改造为线程池
            # 创建线程, 进行复制操作
            self.copy_thread = CopyThread(self.copy_files, self.target_address, mutex)
            self.copy_thread.status_signal.connect(self.update_copy_progress)   # 运行中的自定义信号
            self.copy_thread.finished.connect(self.thread_finished)   # 完成后的信号
            self.copy_thread.start()
            self.stop_btn.setEnabled(True)
    
    def stop_copy_file(self):
        """停止复制操作"""
        if self.copy_thread is None:
            return
        self.sourfile_desc.setText(format_textedit(self.copy_thread.copy_files))
        print("停止中的内容：",  self.copy_thread.copy_files)
        self.copy_files = self.copy_thread.copy_files
        self.copy_thread.stop()
        self.stop_btn.setEnabled(False)

    def thread_finished(self):
        """线程完成时"""
        # 开启所有按钮为可用, 停止线程按钮不可用, 设置进度为100
        self.buttons_enable(True)
        self.stop_btn.setEnabled(False)
        self.probar.setValue(100)

    def update_copy_progress(self, odit: collections.OrderedDict):
        """线程运行时, 复制的进度"""
        # 更新字典
        self.copy_files = odit

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

    def closeEvent(self, event):
        """重载关闭窗口事件"""
        reply = QMessageBox.question(self, "警告", "是否关闭当前窗口, 可能会导致进行中的复制操作失败.",
                                     QMessageBox.Yes|QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            if self.copy_files.items() is not None:
                for src_file, process in self.copy_files.items():
                    if process < 1.0:
                        dst_file = os.path.join(self.target_address, os.path.basename(src_file))
                        if os.path.exists(dst_file):
                            os.remove(dst_file)
            event.accept()
        else:
            event.ignore()


def format_textedit(odit: collections.OrderedDict) -> str:
    """格式化文本框"""
    ret_text = str()
    
    for key, val in odit.items():
        proshow = str(round(val*100, 2)) + '%' if val >= 0.0  else "<span style=\"color: red;\">失败</span>"
        ret_text += os.path.basename(key) + "<b> -处理进度 " + proshow + "</b><br>"
    return ret_text
