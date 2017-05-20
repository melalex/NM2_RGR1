from bin.jacobi_method.eigen_pairs import eigen_pairs
from bin.pretty_print import pretty_print
from bin.constants import *

pairs = eigen_pairs(MATRIX_2, EPS)

pretty_print(pairs)
print('===========================')
