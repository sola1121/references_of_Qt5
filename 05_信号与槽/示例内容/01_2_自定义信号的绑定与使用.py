from PyQt5.QtCore import QObject, pyqtSignal


class QTypeSignal(QObject):
    """信号对象"""
    send_msg = pyqtSignal(str, str)   # 定义一个信号

    def __init__(self):
        super().__init__()

    def run(self):
        """发射信号"""
        self.send_msg.emit("参数1", "参数2")


class QTypeSlot(QObject):
    """槽对象"""
    def __init__(self):
        super().__init__()

    def get(self, msg1, msg2):
        """槽对象里的槽函数"""
        print("获得信号, %s, %s" % (msg1, msg2))


if __name__ == "__main__":

    signal_send = QTypeSignal()
    slot_recive = QTypeSlot()

    # 1 将信号与槽函数连接
    signal_send.send_msg.connect(slot_recive.get)
    signal_send.run()

    # 2 断开信号与槽函数的连接
    signal_send.send_msg.disconnect(slot_recive.get)