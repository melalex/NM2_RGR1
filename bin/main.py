from bin.power_method.max_eigen_pair import max_eigen_pair
from bin.power_method.another_eigen_pair import another_eigen_pair
from bin.constants import *

eigen_pair = max_eigen_pair(MATRIX_1, EPS, P, EPS)
print(another_eigen_pair(MATRIX_1, [eigen_pair], EPS, EPS, P))
