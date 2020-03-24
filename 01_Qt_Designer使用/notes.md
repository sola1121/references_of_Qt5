# 笔记

## 将ui文件转换为py文件

使用qt designer设计出自己想要的样子, 在转换为py文件, 然后调用这个文件就行了.

主要使用的工具是`pyuic5`命令

    pyuic5 firstWindow.ui -o firstWindow.py

[pyuic5官网](https://www.riverbankcomputing.com/static/Docs/PyQt5/designer.html)