from bin.constants import *
from bin.lu_method.eigen_pairs import eigen_pairs
from bin.pretty_print import pretty_print

pairs = eigen_pairs(MATRIX_1, EPS)

pretty_print(pairs)
print('===========================')
