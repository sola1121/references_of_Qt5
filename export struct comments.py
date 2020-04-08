# !/usr/bin/env python3
# conding: utf-8
# 用于导出结构性内容

import sys

import PyQt5
import PyQt5.QtWidgets as pck

output_package = PyQt5.QtCore.Qt

ori_out = sys.stdout

sys.stdout = open(r"./{}.txt".format(output_package.__name__), 'w', encoding="utf-8")

help(output_package)

sys.stdout.close()
sys.stdout = ori_out