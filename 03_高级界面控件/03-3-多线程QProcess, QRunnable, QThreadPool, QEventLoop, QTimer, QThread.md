# 笔记

<!-- TOC -->

- [笔记](#笔记)
    - [补充](#补充)
        - [窗口样式设置](#窗口样式设置)
        - [QProcess](#qprocess)
        - [QRunnable](#qrunnable)
        - [QThreadPool](#qthreadpool)
        - [QEventLoop](#qeventloop)
        - [信号](#信号)
    - [QTimer](#qtimer)
        - [QTimer常用方法](#qtimer常用方法)
        - [QTimer常用信号](#qtimer常用信号)
        - [QTimer使用](#qtimer使用)
    - [QThread](#qthread)
        - [QThread方法](#qthread方法)
        - [QThread常用信号](#qthread常用信号)
        - [QThread使用](#qthread使用)
    - [事件处理](#事件处理)

<!-- /TOC -->

一般情况下, 应用程序都是单线程运行的, 但是对于GUI程序来说, 单线程有时候不能满足需求. 比如执行一个特别耗时的操作, 在执行过程.

多线程技术的实现在QT中一般有使用计时器模块QTimer, 使用多线程模块QThread, 使用事件处理的功能.

## 补充

### 窗口样式设置

    win = QWidget()
    win.setWindowFlags(Qt.SplashScreen|Qt.FramelessWindowHint)   # 模仿开机画面, 程序设置为无边框

### QProcess

`PyQt5.QtCore.QProcess`

![QProcess](./img/3-1-QProcess.png)

用于执行外部进程, 并与之通信.

要开始一个进程, 将要运行的程序的命令行和执行参数传递给start(). 参数支持作为单独的字符串在QStringList中.

或者, 你可以设置程序用setProgram()和setArguments()一起运行, 之后调用start()和open().

比如, 下面的代码片段通过传递包括"-style"和"fusion"的字符串在x11平台上以Fusion风格运行模拟时钟例子

    QObject *parent;
    ...
    QString program = "./path/to/Qt/examples/widgets/analogclock";
    QStringList arguments;
    arguments << "-style" << "fusion";

    QProcess *myProcess = new QProcess(parent);
    myProcess->start(program, arguments);

QProcess这之后进Starting状态, 而且当该程序启动后, QProcess进入正在Running状态, 并返回started().

QProces允许用户想一个顺序I/O设备一样对待一个进程. 通过使用QTcpSocket创建的网络连接可以从进程中写入和读取. 连接好后, 调用write()可以向进程标准输入, 调用read(), readLine(), gatChar()可以读取其标准输出. 因为其继承了QIODevice, QProcess也可以被用作一个QXmlReader的输入源, 或者生成要使用QNetworkAccessManager上传的数据.

当进程退出时, QProcess变回NotRunning状态(初始状态), 并且发送finished()信号.

finished()信号提供进程退出码和退出状态作为参数, 也可以调用exitCode()来获得最后一个完成的进程的退出码, 调用exitStatus()来获得其退出状态. 如果在执行中发生了一个错误, QProcess将会发出errorOccurred()信号. 也可以调用error()来找到最后发生的错误的了类型, state()用以找到当前进程的状态.

注意: QProcess不被VxWorks, iOS, tvOS, watchOS, 或者Universal Windows平台支持.

**使用Channel通信**  
进程有两个预定义定义的Channels: 标准输出Channel(stdout), 提供了标准的终端输出; 错误输出Channel(stderr), 提供了错误输出. 这些Channels代表了两个独立的数据流. 可以在两者之间使用setReadChannel()进行切换. 当数据在read Channel上可用时QProcess发出readyRead(). 当一个新的标准输出数据可用时, 其也同样发出readyReadStandardoutput(), 当一个新的标准错误输出数据可用时, 会发出readyReadStandardError(). 替代调用read(), readLine(), getChar(), 可以明确地使用readAllStandatOutput()或readAllStandardError()来读取对应Channel的所有数据.

对于Channels这个术语可能有点误导性. 明确认识进程的输出Channels对应QProcess的read(读取)Channels, 而进程的输入Channels对应QProcess的write(写入)Channels. 这是因为read其实是使用的QProcess的输出, write则是使用QProcess的输入.

QProcess可以合并两个输出Channels, 这样来自运行中进程的标准输出和标准错误数据将共同使用标准输出Channel. 在开始启用这个特性之前, 使用MergedChannels调用setProcessChannelMode(). 通过传入ForwardedChannels作为参数, 也可以转发正在运行中进程的输出到调用, 主进程. 它也可以转发其中一个输出Channel-典型的其中一个使用ForwardedErrorChannel, 但是FrowardedOutputChannel 也存在. 注意, 在GUI应用中使用Channel转化是典型的一个不好的办法-应该以图形化的方式代替.

某些进程为了操作需要特殊的环境配置. 可以调用setProcessEnviroment()设置进程的环境变量. 设置一个工作目录, 调用setWorkingDirectory(). 默认的, 进程在当前执行进程的工作目录中运行.

属于QProcess开头的GUI应用程序的窗口的位置和屏幕Z-order由基础窗口系统控制. 对于Qt5应用, 位置可以使用 -qwindowgeometry 命令选项指定; X11应用通常接受一个 -geometry 命令行选项.

**注意**:  
在QNX, 设置工作目录可能造成所有应用线程, 调用者线程除外, 在产生时会暂时冻结, 这取决于操作系统的限制.

**同步进程API Synchronous Process API**  
QProcess提供一系列允许不使用一个事件循环的方法, 通过直到某些信号发出, 延迟调用线程.
  + waitForStarted() 阻塞直到进行已经开始
  + waitForReadyRead() 阻塞直到新的在read Channel上的可读取数据数据可用
  + waitForBytesWritten() 阻塞直到一个数据的有效载荷已经被写入进程
  + waitForFinished() 阻塞直到进程完成

从主线程(已经调用exec()的)调用这些方法可能造成用户界面冻结(点求不动).

下面的例子运行gzip压缩字符串"Qt rocks", 没有一个事件循环

    QProcess gzip;
    gzip.start("gzip", QStringList() << "-c");
    if (!gzip.waitForStarted())
        return false;

    gzip.write("Qt rocks!");
    gzip.closeWriteChannel();

    if (!gzip.waitForFinished())
        return false;

    QByteArray result = gzip.readAll();

**微软系统注意 Notes for Windows Users**  
一些微软系统命令(比如: dir)没有被单独的应用支持, 但是通过命令交互终端提供. 如果尝试使用QProcess来直接执行这些命令, 那将不会工作. 一个可能的解决方法是执行这个命令交互终端自己(cmd.exe, powershell.exe), 并让交互终端执行期望的命令.

**方法**

arguments ()  
environment ()  
error ()  
exitCode ()  
exitStatus ()  
inputChannelMode ()  
processChannelMode ()  
processEnvironment ()  
processId ()  
program ()  
readChannel ()  
workingDirectory ()  

closeReadChannel (channel) : 关闭read Channel. 在调用该方法后, QProcess将不在从该Channel接收数据. 已经接收了的可以读取.  
The write channel is implicitly opened when start() is called.  
closeWriteChannel () : 计划关闭QProcess的write Channel. 一旦所有数据都写入进程, Channel将会关闭. 在在调用该方法后, 任何尝试写入该进程都会失败. 在start()被调用后, write channel是隐式开启的.

    more = QProcess()
    more.start("more")
    more.write("Text to display")
    more.closeWriteChannel()
    #QProcess will emit readyRead() once "more" starts printing

readAllStandardError (): 读取所有标准输出错误  
readAllStandardOutput () : 读取所有标准输出  
setArguments (arguments) : 设置将要传给调用程序的参数, 必须在start()之前调用  
setEnvironment (environment) : 设置QProcess将会传递给其子进程的环境. 参数是一个键值对的列表. 注意该方法没有setProcessEnvironment来得有效率. 如下创建一个TMPDIR环境变量  

    QProcess process;
    QStringList env = QProcess::systemEnvironment();
    env << "TMPDIR=C:\\MyApp\\temp"; // Add an environment variable
    process.setEnvironment(env);
    process.start("myapp");

setInputChannelMode (mode) : 设置QProcess标准输入Channel的模式, 设置的模式将会在下次start()后使用.  
setProcessChannelMode (mode) : 设置QProcess的标准输出和错误输出的Channel模式, 在下次start()调用时使用.

    builder = QProcess()
    builder.setProcessChannelMode(QProcess.MergedChannels)
    builder.start("make", ["-j2"])

    import sys
    if not builder.waitForFinished():
        sys.stderr.write("Make failed:" + builder.errorString())
    else
        sys.stderr.write("Make output:" + builder.readAll())  

setProcessEnvironment (environment) : 设置QProcess将会传递给其子进程的环境. 如下创建一个TMPDIR环境变量

    QProcess process;
    QProcessEnvironment env = QProcessEnvironment::systemEnvironment();
    env.insert("TMPDIR", "C:\\MyApp\\temp"); // Add an environment variable
    process.setProcessEnvironment(env);
    process.start("myapp");

setProcessState (state) : 设置当前进程的状态  
setProgram (program) : 设置开始一个进程时调用的程序. 这个方法一定要在start()之前调用.  
setReadChannel (channel) : 设置当前QProcess的read Channel为给定的Channel. 当前输入Channel被read(), readAll(), readLine(), getChar()使用. 其同样确定哪个通道触发QProcess发出readyRead().  
setStandardErrorFile (fileName[, mode=QIODevice.Truncate]) : 指定重定向输出错误的文件. 重定向后, 原通道关闭, 调用read(), readAllStandardError()都会失败. 如果使用的是添加模式, 会向文件中添加, 否则会被截断.  
setStandardInputFile (fileName) : 设置重定向进程的标准输入为指定文件. 当被设置为该模式, QProcess对象将会变为只读模式(调用write()将会造成错误). 为了让进程立即的读取到EOF, 传入nullDevice(). 这比在写入数据时使用closeWriteChannel()来得更清楚, 因为其可以在启用前设置. 如果指定的fileName不存在或不可读, 在使用start()启动时将会失败. 进程后开始后调用无效.  
setStandardOutputFile (fileName[, mode=QIODevice.Truncate]) :  设置重定向进程标准输出到指定的文件. 当重定向成功, 标准的输出read Channel将会关闭, 使用read(), readAllStandardOutput()将会失败. 从进程中丢弃所有标准输出, 传入nullDevice(). 这个比简单的不读取标准输出来得更有效, 因为没有QProcess缓冲填满. 如果文件不存在当start()开始时, 其将会被创建, 如果不能创建, 启动将会失败. 如果文件存在并且模式是Truncate, 文件将会被截断. 如果模式是添加, 文件将会被添加. 进程开始后调用无效.  
setStandardOutputProcess (destination) : 将此流程的标准输出流通过管道传输到目标流程的标准输入.

下面的命令

    command1 | command2

能够被QProcess以下面代码实现

    process1 = QProcess()
    process2 = QProcess()

    process1.setStandardOutputProcess(process2)

    process1.start("command1")
    process2.start("command2")  

setWorkingDirectory (dir) : 设置工作目录为指定目录. QProcess将在这个目录开始该进程. 默认的行为是在进程被调用的工作目录开始该进程.  
start ([mode=QIODevice.ReadWrite]) : 这是一个重载方法. 开始由setProgram()和setArgument()设置的程序.  
start (command[, mode=QIODevice.ReadWrite]) : 这是一个重载方法. 开始执行一个命令的进程.

    process = QProcess()
    process.start("del /s *.txt")
    # same as process.start("del", ["/s", "*.txt"])

start (program, arguments[, mode=QIODevice.ReadWrite]) : 开始制定的程序, 并向其传入指定的参数.  
startDetached ([pid=None]) : 在一个新进程开始由setProgram()和setArgument()或setArguments()指定的程序, 并脱离它. 返回True如果成功; 否返回False. 如果调用它的进程退出, 已经分离的进程会继续不受影响的运行. Unix上, 开始的进程将会在其自己的会话中运行, 表现得像个守护进程.  进程将会被开始在由setWorkingDirectory()指定的目录. 如果没有设置, 将会继承启用它的进程的目录. 如果方法运行成功, pid将会被设置到进程上用以标识. 注意, 子进程也许退出, pid也许变成在没有察觉的时候变为无效. 进一步的, 在子进程退出后, 一个相同pid也许会由其它不同进程循环使用. 用户的代码需要明确知道何时使用这些变量, 特别是如果打算通过操作系统手段强制终止该进程. 只有下面的方法被支持, 其他的忽略.
  + setArguments()
  + setCreateProcessArgumentsModifier()
  + setNativeArguments()
  + setProcessEnvironment()
  + setProgram()
  + setStandardErrorFile()
  + setStandardInputFile()
  + setStandardOutputFile()
  + setWorkingDirectory()

startDetached(program, arguments)  
startDetached(command)  
startDetached(program, arguments, workingDirectory) : 这个方法重载startDetached(). 在一个新的进程开始指定的程序和其参数, 并分离它. 返回True如果成功; 否返回False. 如果调用它的进程退出, 已经分离的进程会继续不受影响的运行.  
state () : 返回当前deep进程的状态.  
waitForFinished ([msecs=30000]) : 阻塞直到进程执行完成, finished()信号将会发出, 或者在指定时间内阻塞. 返回True如果进程完成, 否返回False(操作超时, 错误发生, QProcess已经完成). 这个方法可以不用一个事件循环操作. 在写入没有GUI的应用和在没有GUI的线程I/O操作时很有效.  
waitForStarted ([msecs=30000]) :  阻塞直到进程执行开始, started()信号将会发出, 或者在指定时间内阻塞. 返回True如果进程完成, 否返回False(操作超时, 错误发生). 这个方法可以不用一个事件循环操作. 在写入没有GUI的应用和在没有GUI的线程I/O操作时很有效. 个方法可以不用一个事件循环操作. 在写入没有GUI的应用和在没有GUI的线程I/O操作时很有效.  

**槽方法**

kill() : kill 当前进程, 让其立刻退出.  
terminate() : 尝试终止进程.  

**虚函数**

setupChildProcess() : 这个方法被
在子程序上下文中恰好在Unix或macOS上执行程序之前（即在fork（）之后但在execve（）之前）调用此函数。重新实现此功能以完成子进程的最后一刻初始化。

    class SandboxProcess(QProcess):
        def setupChildProcess(self)
            # Drop all privileges in the child process, and enter
            # a chroot jail.
            os.setgroups(0, 0)
            os.chroot("/etc/safe")
            os.chdir("/")
            os.setgid(safeGid)
            os.setuid(safeUid)
            os.umask(0)

您不能从此函数退出进程（例如，通过调用exit（））。如果需要在开始执行之前停止该程序，解决方法是发出finish（），然后调用exit（）。

**信号**

errorOccurred (error)  
finished (exitCode, exitStatus)  

**静态方法**

execute(command)  
execute(program, arguments)  
nullDevice ()  
startDetached (command)  
startDetached (program, arguments)  
startDetached (program, arguments, workingDirectory)  
systemEnvironment() : 返回调用进程的环境, 以一个字典的列表返回.  

    environment = QProcess.systemEnvironment()
    # environment = [PATH=/usr/bin:/usr/local/bin", "USER=greg", "HOME=/home/greg"]

### QRunnable

`PyQt5.QtCore.QRunable`

![QRunnable](./img/3-2-QRunnable.png)

QRunnable类是一个接口, 用于代表一个需要执行的任务或一段代码, 重载run()实现自己的业务代码.

可以使用QThreadPool来单独的执行代码. 如果autoDelete()返回True, QThreadPool会自动的删除QRunnable(默认处理方式). 使用setAutoDelete()来改变自动删除标记.

QThreadPool支持使用通过从run()中执行tryStartt(this)重复调用相同的QRunnable. 如果autoDelete开启, QRunnable将会在最后一个线程退出run()方法时被删除. 当autoDelete开启时调用同一个QRunnable的start()方法多次将会造成竞争, 这是不推荐的.

**方法**

autoDelete () : 是否开启了autoDelete.  
setAutoDelete (_autoDelete) : 设置是否开启autoDelete, 设置True开启, 其他关闭. 开启, QThreadPool将会在这个runnable自动地删除它; 其他, 所有者就会保留它. 注意, 其必须在start()之前被设置, 如果在之后调用这个方法, 将没有任何表现.

**虚函数**

run () : 抽象函数, 用于继承后实现.

### QThreadPool

`PyQt5.QtCore.QThreadPool`

![QThreadPool](./img/3-3-QThreadPool.png)

QThreadPool管理和回收单独的QThread对象, 以帮助减少使用线程的程序中创建线程的成本. 每个Qt应用有一个全局的QThreadPool 对象, 可以使用globalInstance() 来获得它.

使用QThreadPool中的一个线程, 可通过子类QRunnable并实现它的run()虚函数. 然后创建一个该类的对象, 并将这个对象传递给QThreadPool的start()方法.

    class HelloWorldTask(QRunnable):
        def run(self):
            print "Hello world from thread", QThread.currentThread()

    hello = HelloWorldTask()
    # QThreadPool takes ownership and deletes 'hello' automatically
    QThreadPool.globalInstance().start(hello)

QThreadPool默认自动删除QRunnable. 使用setAutoDelete()来改变自动删除标记.

QThreadPool支持通过从run()内调用tryStart(this)执行同样的QRunnable多次. 如果autoDelete是开启的, QRunnable将在最后一次run()的exit()执行后被删除. 当autoDelete开启的时候调用同一个QRunnable的start()多次会造成竞争, 这是不被推荐的.

在一定时间内没有使用的线程将会过期. 默认的过期时间为30000毫秒(30秒). 可以使用setExpiryTimeout()设置. 设置一个负数deep过期时间将禁用过期机制.

调用maxThreadCount()查询可用的线程最大值. 如果需要, 可以改变这个限制使用setMaxThreadCount(). 默认的maxThreadCount()是idealThreadCount(). activeThreadCount()方法返回当前运行中的线程数.

reverseThread()方法保留一个线程用于额外deep使用. 使用releaseThread()用来释放做完事儿的线程, 这样就可以在次使用它了. 实质上, 这些方法临时增加或减少活动线程的数量, 用以实现不可见的QThreadTool的耗时操作很有用.

注意: QThreadPool是一个用于管理线程的底层类.

**方法**  

activeThreadCount ()  
clear () : 移除那些还没有运行的QRunnable对象. 那些runnable.autoDelete()返回Truedeep将会被删除.  
expiryTimeout ()  
maxThreadCount () :  
releaseThread () : 释放先前通过调用reserveThread()保留的线程. 调用这个方法的时候没有预先临时保留一个线程会增加maxThreadCount(). 当一个线程睡眠等待更多事务时是很有用的, 允许其他的线程继续. 当需要保留线程的时候, 确保调用reserveThread(), 这样线程池可以正确的维护activeThreadCount().  
reserveThread () : 保留一个线程, 不顾activeThreadCount() 和 maxThreadCount(). 当完成一个线程, 调用releaseThread()来确保其可在使用. 注意, 这个方法总是会增加活动的线程数. 这意味者调用这个方法可能会让activeThreadCount()的返回值比maxThreadCount()还大.  
setExpiryTimeout (expiryTimeout)  
setMaxThreadCount (maxThreadCount)  
setStackSize (stackSize)  
stackSize ()  
start (runnable[, priority=0]) : 保留一个线程并使用它来运行runnable, 除非这个线程会让当前线程计数超过maxThreadCount(). 在这样的情况下, 只将runnable加入到执行队列中. priority参数可以用来定义在队列中的执行优先级. 注意, 如果runnable.autoDelete()返回True, 线程池将会获得该runnable的所有权. 并且, 如果runnable.run()返回了的话, 该runnable将会被自动地被删除. 如果runnable.autoDelete()返回False, 所有权将依然在其创建者手里. 需要知道的是, 在调用start()后改变runnable的自动删除设置, 将会造成未知行为.  
tryStart (runnable) : 尝试保留一个线程来运行runnable. 如果在使用该方法时没有任何一个线程可用, 其将不会做任何操作并返回False. 之外, runnable将会立刻被使用一个可用的线程执行, 并且该方法返回True. 注意, 如果runnable.autoDelete()返回True, 线程池将会获得该runnable的所有权. 并且, 如果runnable.run()返回了的话, 该runnable将会被自动地被删除. 如果runnable.autoDelete()返回False, 所有权将依然在其创建者手里. 需要知道的是, 在调用tryStart()后改变runnable的自动删除设置, 将会造成未知行为.  
tryTake (runnable) : 尝试移除在队列中指定的runnable, 当然前提是这个runnable没有启动. 如果runnable没有启动, 返回True, 并且runnable的所有权将会被传给该runnable的调用者(即使runnable.autoDelete()==True). 其他情况返回False. 注意, 如果runnable.autoDelete()==True, tryTake()将会移除错误的runnable. 这被称为ABA问题: 原始的runnable也许已经执行了并且已经被删除了. 内存被另一个runnable重用, 这将会导致这个runnable被移除. 所以, 推荐调用这个方法只在runnable没有设置自动删除的时候.  
waitForDone ([msecs=-1]) : 等所有线程退出并从线程池中移除所有的线程. 移除成功返回True, 失败返回False. 如果毫秒设置为-1(默认值), 超时将会被忽略(等待最后一个线程退出).

**静态方法**

globalInstance () : 返回全局的QThreadPool对象.

### QEventLoop

`PyQt5.QtCore.QEventLoop`

![QEventLoop](./img/3-4-QEventLoop.png)

At any time, you can create a QEventLoop object and call exec() on it to start a local event loop. From within the event loop, calling exit() will force exec() to return.

任何时间, 都能创建一个QEventLoop对象并在其上调用exec()以开始一个本地事件循环. 从这个事件循环中, 调用exit()将会强制exec()返回.

**方法**

exec_ ([flags=QEventLoop.AllEvents]) : 进入事件并等待其退出, 返回值将交给exit()  
exit ([returnCode=0]) : 告诉事件退出, 并返回执行码  
isRunning () : 是否运行中  
processEvents ([flags=QEventLoop.AllEvents])  
processEvents (flags, maximumTime)  
  + **note**: 所有事件中deleteLater()是单独处理的.
  + QEventLoop.ExcludeUserInputEvents : 不处理用户输入事件, 比如: 按钮点击和键盘点击. 注意: 这些事件没有被丢弃, 而是放到了下一个没有设置flag的processEvents()来处理
  + QEventLoop.ExcludeSocketNotifiers : 不处理套接字通知事件. 注意: 这些事件没有被丢弃, 而是放到了下一个没有设置flag的processEvents()来处理
  + QEventLoop.WaitForMoreEvents : 如果没有事件处理, 等待.

**槽函数**

quit()

### 信号

`PyQt5.QtCore.pyqtSignal`

可以为控件绑定一个自定义的信号. 可以用在线程的信号交流.

    from PyQt5.QtCore import pyqtSignal

    class MyThread(QThread):
        """线程对象"""

        MySignal = pyqtSignal( str )   # 指定了一个传递给槽的数据类型

        ......

        def run(self):
            ....
            self.MySignal.emit( str_data )
            ....

    thread = MyThread()
    thread.MySignal.connect(do_something)   # 如果设置了传递值, 槽函数还会接收值
    thread.start()
    thread.wait()

## QTimer

`PyQt5.QtCore.QTimer`

![QTimer](./img/3-5-QTimer.png)

如果要在应用程序中周期性地进行某项操作, 比如周期行地检测主机的CPU值, 则可以使用QTimer(定时器), QTimer类提供了重复的和单次的定时器. 要使用定时器, 要先创建一个QTimer实例, 将其timeout信号连接到相应的槽, 并调用start(). 然后, 定时器会以恒定的间隔发出timeout信号.

当窗口控件收到timeout信号后, 它就会停止这个计时器. 这是在图形用户界面中实现复杂工作的一个典型方法, 更现代的方法则是使用线程来替代.

### QTimer常用方法

start(milliseconds) : 启动或重新启动定时器, 时间间隔为毫秒. 如果定时器已经运行, 它将被停止并重新启动. 如果singleShot信号为真, 定时器将仅被激活一次  
stop() : 停止定时器  

### QTimer常用信号

singleShot(int, QtTimerType, PYQT_SLOT) : 在给定的时间间隔后调用一个槽函数时发射此信号  
timeout : 当定时器超时时发射此信号  

### QTimer使用

    from PyQt5.QtCore import QTimer

    timer = QTimer()
    
    # 使用timeout, 以一定间隔时间触发一个事件
    timer.timeout.connect(do_something)   # 每隔一个timeout将会启动do_something
    timer.start(1000)   # 设置间隔时间1s
    ...
    timer.stop()   # 停止这个计时器    

    # 使用singleShot, 就在一个时间间隔内触发一次
    timer.singleShot(1000, do_something)   # 在指定时间后启动一次do_something

## QThread

`PyQt5.QtCore.QThread`

![QThread](./img/3-6-QThread.png)

QThread是Qt线程类中最核心的底层类. 由于Qt的跨平台性, QThread要隐藏所有与平台相关的代码.

一个QThread对象管理程序中的一个线程. QThread开始于执行run(). 默认的, run()通过调用exec()开始事件循环并且开始一个Qt事件循环代替线程.

使用moveToThread()把一个工作对象移入线程.

### QThread方法

start([priority=InheritPriority]) : 启动线程, 可指定优先级  
wait([time=ULONG_MAX]) : 阻塞线程, 直到满足以下条件  
  + 与此QThread对象关联的线程已经完成执行(即从run()返回时). 如果线程完成执行, 此函数返回True; 如果线程尚未启动, 此函数也返回True
  + 等待事件单位是ms(毫秒). 如果事件是ULONG_MAX(默认值), 则等待, 永远不会超时(线程必须从run返回) 如果等待超时, 此函数将返回False

exec_ () : 进入事件循环, 等待到exit()被执行, 返回值传递给exit(). 通过quit()调用的exit(), 返回值为0. 该方法在run()内被被调用, 必须调用此函数来开始事件处理.  
exit ([retcode=0]) : 告诉线程的事件循环退出并返回状态码. 在调用该方法之后, 线程将离开事件循环并从exec()返回值. exec()方法返回returnCode. 通常的, 一个returnCode为0表示成功, 任何非零值表示一个错误. 注意, 不像C中同名库, 这个方法不会返回一个调用器-事件处理停止了. 直到exec()被在此滴啊用, 没有QEventloop会被启动. 如果在exec()中的Eventloop没有在运行, 下一个调用的exec()也会立刻返回.  

requestInterruption () : 请求线程中断. 该请求是建议性的, 并取决于在线程上执行的代码来决定是否与怎样来对该请求做出反应. 这个方法不会停止任何在线程上运行的事件循环, 也不会以某种方式终止它.  
isInterruptionRequested ()  
eventDispatcher () : 返回线程的一个指向调度对象的指针. 如果线程没有事件调度存在, 这个方法返回None.  
setEventDispatcher (eventDispatcher) : 为线程设置事件调度
将线程的事件调度器设置为eventDispatcher. 这只适用于没有事件调度的线程. 在线程使用start()开始之前, 或对于主线程来说, 在QCoreApplication之前. 该方法将会接管该对象.  
isFinished ()  
isRunning ()  
loopLevel ()  
priority ()  
setPriority (priority)  
setStackSize (stackSize)  
stackSize ()  

**虚函数**

run () : 一个线程的开始点. 在调用start()之后, 新建的线程将会调用这个方法. 默认 实现只是调用exec(). 可以重载此方法用以实现业务逻辑. 该方法的返回将会结束对应的线程.

**槽函数**

quit () : 告诉线程的事件循环退出并返回0(成功). 等价于调用exit(0). 如果线程没有一个事件循环, 该方法不会做任何事.  
start ([priority=InheritPriority]) : 通过调用run()开始执行线程. 操作系统将会根据设置的优先级参数调度线程任务. 如果该线程已经在运行了, 该方法不会做任何事. 优先级参数的实现依赖于操作系统的调度策略. 不支持的系统会忽略(如Linux).  
terminate () : 终结执行的线程. 线程可能不会被立刻终止, 这取决于操作系统的调度策略. 在这之后使用wait(), 可确保线程终止. 当线程终止了, 所有等待该线程的线程将会被唤醒. 警告, 该方法是危险的并不被推荐. 因为线程可能在任何时候被终结, 如果此时线程正在做一些事, 可能会导致一些错误. 终止通过调用setTerminationEnabled()可以被显式地启用或禁止. 在终止情况下调用此方法会导致终止延迟, 直到终止再被开启.  

**静态方法**

currentThread ()  
idealThreadCount () : 返回系统推荐的线程数. 由系统的进程核心数来决定. 当进程核心数无法判断, 该方法返回1.  
msleep (arg__1)  
setTerminationEnabled ([enabled=true]) : 启用或禁用终止当前的线程. 必须是已经通过QThread启用的线程. 如果禁用, 调用terminate()将会立刻返回没有做任何事. 相对的, 终止将延迟到启用终止为止. 如果启用, 在之后调用terminate()将会正常的终止线程. 如果终止被延迟(比如禁用时terminate()被调用), 这个方法将会立刻终止调用线程. 在这种情况下, 此函数不会返回.  
sleep (arg__1)  
usleep (arg__1)  
yieldCurrentThread () : 产生当前线程的执行到另一个runnable线程, 如果有. 注意, 这是由操作系统来决定如何切换线程.

### QThread常用信号

started : 在开始执行线程的run()函数之前, 从相关线程触发  
finished : 当程序完成业务逻辑时, 从相关线程触发  

### QThread使用

要使用QThread开始一个线程, 可以创建它的一个子类, 重载QThread.run()方法就可以.

初始化定义的线程类可以直接得到Thread实例, 调用其start()方法即可启动线程. 线程启动后, 会滴啊用其实现的run方法.

业务的线程任务就写在run方法中, 当run退出之后, 线程基本就结束了.

    class MyThread(QThread):
        def __init__(self, parent=None):
            super().__init__(parent=parent)

        def run(self):
            # 主代码
            pass

    th = MyThread()
    th.start()

当在窗口中显示的数据比较简单时, 可以把读取数据的业务逻辑放在窗口的初始化代码中; 但是如果读取数据的时间比较长, 比如网络数据请求, 则可以把这部分逻辑放在QThread线程中, 实现界面的数据显示和数据读取的分离, 以满足MVC设计模式的要求.

    from PyQt5.QtCore import QThread, pyqtSignal
    from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QPushButton, QGridLayout


    class ThreadWorker(QThread):
        """线程对象"""

        single_out = pyqtSignal(str)   # 自定义的信号, str为传递给槽函数的数据类型

        def __init__(self, parent=None):
            super().__init__(parent=parent)
            ......
        
        def __del__(self):
            self.wait()   # 在删除QThread的时候等候完成, 这样就不用在主线程中阻塞了

        def run(self):
            ......
            self.single_out.emit(str_info)   # 自定义的信号发出
            # 线程休眠2s
            self.sleep(2)


    class WinForm(QWidget):
        """主窗口"""
        def __init__(self, parent=None):
            super().__init__(parent=parent)
            ......
            self.thread = ThreadWorker()   # 创建一个线程对象
            self.thread.single_out.connect(self.slot_handle_thread)   # 将信号绑定槽函数
            ......          
            

        def slot_handle_thread(self, str_info):
            ......

分离UI主线程与工作线程. 这样可以不让窗口卡死.

    import sys

    from PyQt5.QtCore import QTimer, QThread, pyqtSignal
    from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLCDNumber, QPushButton


    global sec
    sec = 0


    class WorkThread(QThread):
        """工作线程"""

        finish_signal = pyqtSignal()   # 自定义的信号

        def __init__(self, parent=None):
            super().__init__(parent)

            def run(self):
                for i in range(2e16):   # 耗时操作, 放入线程中
                    pass

                # 循环完成后触发自定义的事件
                self.finish_signal.emit()


    def countTime():
        global sec
        sec += 1
        # LED显示数字
        lcd_number.display(sec)


    def work():   # 用于开启计时器, 和线程
        # 计时器每秒计数
        timer.start(1000)
        # 开始线程 计时开始
        work_thread.start()
        work_thread.finish_signal.connect(timeStop)    # 处理线程的完成信号


    def timeStop():
        # 关闭计时器
        timer.stop()
        print("运行结束用时", lcd_number.value())
        # 重设全局时间
        global sec
        sec = 0


    if __name__ == "__main__":

        app = QApplication(sys.argv)
        win = QWidget()
        win.resize(300, 120)

        lcd_number = QLCDNumber()
        button = QPushButton("测试启用线程")
        button.clicked.connect(work)   # 点击开始计时器, 开始工作线程

        layout = QVBoxLayout()
        layout.addWidget(lcd_number)
        layout.addWidget(button)
        win.setLayout(layout)

        timer = QTimer()
        timer.timeout.connect(countTime)   # 计时器时间间隔触发, 刷新led时间
        work_thread = WorkThread()

        win.show()
        sys.exit(app.exec())

## 事件处理

PyQt为事件处理提供了两种机制: 高级的信号与槽机制, 以及低级的事件处理函数. 下面介绍一个低级的事件处理程序processEvents()函数. 其作用是处理事件, 简单说就是刷新页面.

对于执行很耗时的程序来说, 由于PyQt需要等待程序执行完毕才能进行下一步, 这个过程表现在界面上就是卡顿; 而如果在执行这个耗时程序时不多地运行QApplication.processEvents(), 那么就可以实现一边执行耗时程序, 一边刷新页面的功能, 给人的感觉就是程序运行流畅. 因此使用QApplication.processEvents()的使用方法就是在主函数执行耗时操作的地方, 加入QApplication.processEvents().

    class WinForm(QWidget):
        """主窗口"""
        def __init__(self, parent=None):
            super().__init__(parent)
            self.setWindowTitle("processEvents 使用")

            self.list_file = QListWidget()
            self.button_start = QPushButton("开始")
            
            grid_layout = QGridLayout()
            grid_layout.addWidget(self.list_file, 0, 0, 1, 2)   # 0行0列, 占1行, 占2列
            grid_layout.addWidget(self.button_start, 1, 1)   # 1行1列
            self.setLayout(grid_layout)

            self.button_start.clicked.connect(self.slot_add)
        
        def slot_add(self):
            for n in range(10):
                str_n = "file index{}".format(n)
                self.list_file.addItem(str_n)
                QApplication.processEvents()   # 刷新界面, 效果不好
                time.sleep(2)