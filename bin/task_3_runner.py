from bin.inverse_iteration.min_eigen_pair import mix_eigen_pair
from bin.pretty_print import pretty_print
from bin.constants import *

min_pair = mix_eigen_pair(MATRIX_2, EPS)

pretty_print(min_pair)
print('===========================')
