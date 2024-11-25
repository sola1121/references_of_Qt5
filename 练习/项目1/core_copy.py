import os, hashlib, collections, filecmp

from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import QThread, QMutex, Signal


mutex = QMutex()


class CopyThread(QThread):
    """
    文件复制线程
    构造函数参数:
        copy_files: 源文件路径与复制的进度(小数), 为有序字典, key为源文件路径, value为进度
        target_address: 目标文件路径, 为字符串
        mutex: 互斥锁
    """
    status_signal = Signal(collections.OrderedDict)

    def __init__(self, copy_files: collections.OrderedDict, target_address: str, mutex: QMutex):
        """初始化将要复制的源文件地址, 目标地址, 线程锁"""
        super().__init__()
        self.copy_files = copy_files
        self.target_address = target_address
        self.mutex = mutex
        self.running = True   # 单个文件是否继续复制


    def run(self):
        """复制线程运行"""
        try:
            # 上锁
            self.mutex.lock()

            # 开始进行复制
            for src_file in self.copy_files.keys():
                # 是否继续复制下一个文件
                if self.running != True:
                    break
                
                # 获取目标地址
                dst_file = os.path.join(self.target_address ,os.path.basename(src_file))

                # 源文件地址与目标文件地址相一致, 直接跳过复制, 并设置进度为100%
                if src_file == dst_file:
                    self.copy_files[src_file] = 1.0
                    self.status_signal.emit(self.copy_files)
                    continue
                
                # 获取源文件大小
                total_size = os.path.getsize(src_file)
                # 打开源文件和目标文件
                with open(src_file, 'rb') as fsrc, open(dst_file, 'wb') as fdst:
                    copied_size = float(0)
                    while True:
                        # 读取大小
                        read_size = 1024 * 1024   # 每次读取1MB
                        # 读取数据块
                        data = fsrc.read(read_size)
                        # 无数据后退出复制
                        if not data:
                            break
                        # 写入数据块到目标文件
                        fdst.write(data)
                        copied_size += float(len(data))

                        # 设置进度
                        self.copy_files[src_file] = copied_size / total_size
                        self.status_signal.emit(self.copy_files)
                
                # 复制完成后比较两个文件的内容
                if filecmp.cmp(src_file, dst_file) != True:
                    self.copy_files[src_file] = -1.0
                else:
                    self.copy_files[src_file] = 1.0
                self.status_signal.emit(self.copy_files)

            # 解锁
            self.mutex.unlock()
        except Exception as ex:
            for src_file, process in self.copy_files.items():
                if process < 1.0:
                    # 统计复制失败的文件
                    self.copy_files[src_file] = -1.0
                    self.status_signal.emit(self.copy_files)
                    # 删除没有复制完成的文件
                    dst_file = os.path.join(self.target_address ,os.path.basename(src_file))
                    if os.path.exists(dst_file):
                        os.remove(dst_file)
            QMessageBox.critical(None, "错误", f"复制失败:{ex}")

        self.finished.emit()

    def stop(self):
        """复制线程退出"""
        # 删除没有复制完成的文件
        for src_file, process in self.copy_files.items():
            if process < 1.0:
                dst_file = os.path.join(self.target_address ,os.path.basename(src_file))
                if os.path.exists(dst_file):
                    os.remove(dst_file)
        # 停止复制
        self.running = False
        # 退出当前的线程
        self.quit()
        self.wait()
