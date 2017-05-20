from bin.constants import *
from bin.pretty_print import pretty_print
from bin.rq_method.eigen_pairs import eigen_pairs

pairs = eigen_pairs(MATRIX_1, EPS)

pretty_print(pairs)
print('===========================')
