# 笔记

## QLabel

`PyQt5.QtWidgets.QLabel`, 作为一个占位符可以显示不可编辑的文本或图片, 也可以放置一个GIF动图, 还可以被用作提示标记. 其内容可以是纯文本, 链接, 富文本. 就是界面中的标签类, 它继承自QFrame类.

    QObject
        |
        +-QPaintDevice
                |
                +-QWidget
                    |
                    +-QFrame
                        |
                        +-QLabel

### QLabel中常用的方法

setAlignment() : 按固定值方式对齐文本
  + PyQt5.QtCore.Qt.AlignLeft , 水平方向靠左对齐, 默认选项
  + PyQt5.QtCore.Qt.AlignRight , 水平方向靠右对齐
  + PyQt5.QtCore.Qt.AlignCenter , 水平方向居中对齐
  + PyQt5.QtCore.Qt.AlignJustify , 水平方向调整间距两端对齐
  + PyQt5.QtCore.Qt.AlignTop , 垂直方向靠上对齐
  + PyQt5.QtCore.Qt.AlignButtom , 垂直方向靠下对齐
  + PyQt5.QtCore.Qt.AlignVCenter , 垂直方向居中对齐

setIndent() : 设置文本缩进值  
setPixmap() : 设置QLabel为一个QPixmap图片  
text() : 返回QLabel文本内容  
setText() : 设置QLabel文本内容, 支持富文本, 超链接  
setTextInteractionFlags() : 设置文本的交互方式, 如可以被选中, 默认是没有交互的  
selectedText() : 返回所选的字符  
setBuddy() : 设置QLabel的助记符及buddy(伙伴), 即使用QLabel设置快捷键, 会在快捷键后讲焦点设置到其buddy上, 这里用到了QLabel的交互控件功能. 此外, buddy可以是任何一个Widget空间. 使用setBuddy(QWidget *)设置, 其QLabel必须是文本内容, 并且使用"&"符号设置了助记符  
setWordWrap() : 设置是否允许换行  
setOpenExternalLinks() : 设置是否允许打开链接

**设置快捷键**

    name_label = QLabel("&Name", parent=self)   # Alt+N
    name_edit = QLineEdit(parent=self)
    name_label.setBuddy(name_edit)

直接在QLabel初始化名称的时候使用"&"+单个字母 助记符就可以绑定一个快捷键, 运行是使用Alt+该单个字母就可以了. 以上还使用setBuddy()绑定一个控件, 这样使用快捷键后, 焦点就会切换到该控件上.

### QLbel中常用的信号事件

linkActivated : 当单击标签中嵌入的超链接, 希望在新窗口中打开这个超连接时, setOpenExternalLinks属性必须设置为true  
linkHovered : 当鼠标指针滑过标签中嵌入的超链接时, 需要用槽函数与这个信号事件进行绑定

## 文本框类控件

`PyQt5.QtWidgets.QLineEdit` 类, 单行文本框控件; `PyQt5.QtWidgets.QTextEdit` 类, 文本框控件.

### QLineEdit

#### QLineEdit类中常用方法

setAlignment() : 按固定值方式对齐文本
  + PyQt5.QtCore.Qt.AlignLeft , 水平方向靠左对齐, 默认选项
  + PyQt5.QtCore.Qt.AlignRight , 水平方向靠右对齐
  + PyQt5.QtCore.Qt.AlignCenter , 水平方向居中对齐
  + PyQt5.QtCore.Qt.AlignJustify , 水平方向调整间距两端对齐
  + PyQt5.QtCore.Qt.AlignTop , 垂直方向靠上对齐
  + PyQt5.QtCore.Qt.AlignButtom , 垂直方向靠下对齐
  + PyQt5.QtCore.Qt.AlignVCenter , 垂直方向居中对齐

clear() : 清除文本框内容  
setEchoMode() : 设置文本框显示格式  
  + QLineEdit.Normal , 正常显示所输入的字符, 默认选项
  + OLineEdit.NoEcho , 不显示任何输入的字符, 常用于密码类型的输入, 且其密码长度需要保密时
  + QLineEdit.Password , 显示与平台相关的密码掩码字符, 而不是实际输入的字符
  + QLineEdit.PasswordEchoOnEdit , 在编辑时显示字符, 负责显示密码类型的输入

setPlaceholderText() : 设置文本框浮显文字  
setReadOnly() :　设置文本框是否为只读  
setText() : 设置文本框内容  
Text() : 返回文本框内容  
setDragEnabled() : 设置文本框是否接受拖动  
setFont() : 设置字体, 接受PyQt5.QtGui.QFont 对象
setMaxLength() : 设置允许输入字符的最大长度  
selectAll() : 全选  
setFocus() : 得到焦点  
setValidator() : 设置文本框的验证器(验证规则), 将限制任何可能输入的文本.
  + PyQt5.QtGui.QintValidator , 限制输入整数
  + PyQt5.QtGui.QDoubleValidator , 限制输入浮点数
  + PyQt5.QtGui.QRegexpValidator , 匹配正则表达式

setInputMask() : 设置掩码  

验证器需要先定义, 然后在放入控件中, 设置了验证器的输入框, 只能输入符合验证器定义的内容

    reg = PyQt5.QtCore.QRegExp("[a-zA-Z0-9]+$")
    validator_regex = PyQt5.QtWidgets.QLineEdit()
    validator_regex = PyQt5.QtGui.QRegExpValidator(parent=None)
    validator_regex.setRegExp(reg)

**掩码字符**

A : ASCII字母字符是必须输入的(A-Z, a-z)  
a : ASCII字母字符是允许输入的, 但不是必须  
N : ASCII字母字符是必须输入的(A-Z, a-z, 0-9)  
n : ASCII字母字符是允许输入的, 但不是必须  
X : 任何字符都是必须输入的  
x : 任何字符都是允许输入的, 但不是必须  
9 : ASCII数字字符是必须输入的(0-9)  
0 : ASCII数字字符是允许输入的, 但不是必须  
D : ASCII数字字符是必须输入的(1-9)  
d : ASCII数字字符是允许输入的, 但不是必须(1-9)  
\# : ASCII数字字符或加/减符号是允许输入的, 但不是必须  
H : 十六进制格式字符是必须输入的(A-F, a-f, 0-9)  
h : 十六进制格式字符是允许输入的, 但不是必须  
B : 二进制格式字符是必须输入的(0, 1)  
b : 二进制格式字符是允许输入的, 但不是必须  
\> : 所有的字母字符都要大写  
< : 所有的字母字符都要小写  
! : 关闭大小写转换  
\ : 使用"\"转义是上面列出的字符

掩码由掩码字符和分隔符字符串组成, 后面可以跟一个分号和空白字符, 空白字符在编辑后会从文本中删除.

**常见的掩码方式**

000.000.000.000;_ : IP地址, 空白字符是"_"  
HH:HH:HH:HH:HH:HH; : MAC地址  
0000-00-00  : 日期, 空白字符是空格  
\>AAAAA-AAAAA-AAAAA-AAAAA-AAAAA;# : 许可证号, 空白字符是"-", 所有字母字符转换为大写

掩码和正则验证器很相似, 都是规定按照什么样的格式输入, 但是掩码在窗口上是会有输入格式的体现的

#### QLineEdit常用信号事件

selectionChanged : 只要选择改变了, 触发  
textChanged : 当修改文本内容时, 触发  
editingFinished : 当编辑文本结束时, 判断依据是焦点的转移动, 触发

更改信号会将更改后的内容传递给槽响应函数

    linedit = QLineEdit()
    linedit.textChanged.connect(text_change_hint)   # 触发文本改变事件

    def text_change_hint(text):
        print("现在在输入框中的内容是: %s", %text)

### QTextEdit

QTextEdit类是一个多行文本框控件, 可以显示多行文本内容, 当文本内容超出控件显示范围时, 自动显示水平和垂直滚动条. QTextEdit不仅可以显示文本还可以显示HTML文档.

#### QTextEdit常用方法

setPlainText() : 设置多行文本框的文本内容  
toPlainText() : 返回多行文本框的文本内容  
setHtml() : 设置多行文本框的内容为HTML文档  
toHtml() : 返回多行文本框的HTML内容  
cleat() : 清除多行文本框内容

多文本框虽说能支持HTML内容, 但是却打不开超链接和支持多媒体.
