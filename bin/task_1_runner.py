from bin.power_method.max_eigen_pair import max_eigen_pair
from bin.power_method.min_eigen_pair import min_eigen_pair
from bin.power_method.second_max_pair import second_max_pair
from bin.power_method import second_min_pair
from bin.pretty_print import pretty_print
from bin.constants import *

max_pair = max_eigen_pair(MATRIX_1, EPS, P, EPS)
second_max = second_max_pair(MATRIX_1, max_pair, EPS, EPS)
min_pair = min_eigen_pair(MATRIX_1, EPS, P, EPS)
second_min = second_min_pair(MATRIX_1, min_pair, EPS, EPS)

print('Max eigen pair:')
pretty_print(max_pair)
print('===========================')

print('Second max eigen pair:')
pretty_print(second_max)
print('===========================')

print('Min eigen pair:')
pretty_print(min_pair)
print('===========================')

print('Second min eigen pair:')
pretty_print(second_min)
print('===========================')
