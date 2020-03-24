import sys

import PyQt5

output_package = PyQt5

ori_out = sys.stdout

sys.stdout = open(r"./{}.txt".format(output_package.__name__), 'w')

help(PyQt5)

sys.stdout.close()
sys.stdout = ori_out