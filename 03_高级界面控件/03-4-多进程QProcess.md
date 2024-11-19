# 笔记

<!-- TOC -->

- [笔记](#笔记)
    - [QProcess](#qprocess)

<!-- /TOC -->

## QProcess

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
