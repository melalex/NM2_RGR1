from bin.constants import *
from bin.pretty_print import pretty_print
from bin.rq_method import *

pairs = eigen_pairs(MATRIX_1, EPS)

pretty_print(pairs)
print('===========================')
