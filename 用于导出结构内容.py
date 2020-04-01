import sys

import PyQt5.QtWidgets as pck

output_package = pck.QDesktopWidget

ori_out = sys.stdout

sys.stdout = open(r"./{}.txt".format(output_package.__name__), 'w')

help(output_package)

sys.stdout.close()
sys.stdout = ori_out