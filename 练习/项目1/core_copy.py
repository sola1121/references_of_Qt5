import os, sys, shutil, collections

from PySide6.QtCore import QThread, QMutex, Signal


mutex = QMutex()


class CopyThread(QThread):
    """
    文件复制线程
    构造函数参数:
        copy_files: 源文件路径与复制的进度(小数), 为有序字典
        target_address: 目标文件路径, 为字符串
        mutex: 互斥锁
    """
    status_signal = Signal(collections.OrderedDict)

    def __init__(self, copy_files: collections.OrderedDict, target_address: str, mutex: QMutex):
        # 初始化将要复制的源文件地址, 目标地址, 线程锁
        super().__init__()
        self.copy_files = copy_files
        self.target_address = target_address
        self.mutex = mutex

    def run(self):
        # 复制线程运行

        # MARK: 测试的代码

        self.mutex.lock()

        # 开始进行复制
        for src_file in self.copy_files.keys():
            dst = os.path.join(self.target_address ,os.path.basename(src_file))
            total_size = os.path.getsize(src_file)
            # print("源地址:", src_file)
            # print("目标地址:", dst)

            # MARK
            self.sleep(2)

            self.copy_files[src_file] = (total_size/3)/total_size
            self.status_signal.emit(self.copy_files)


            # MARK
            self.sleep(2)

            self.copy_files[src_file] = (total_size/3*2)/total_size
            self.status_signal.emit(self.copy_files)

            # MARK
            self.sleep(2)

            self.copy_files[src_file] = 1.0
            self.status_signal.emit(self.copy_files)


            # # 打开源文件和目标文件
            # with open(src, 'rb') as fsrc, open(dst, 'wb') as fdst:
            #     copied_size = 0
            #     while True:
            #         # 读取数据块
            #         data = fsrc.read(1024 * 1024)  # 每次读取1MB
            #         if not data:
            #             break
            #         # 写入数据块到目标文件
            #         fdst.write(data)
            #         copied_size += len(data)
                    
            #         # 计算进度百分比
            #         progress = (copied_size / total_size) * 100

        self.mutex.unlock()

        self.finished.emit()


