from bin.power_method.max_eigen_pair import max_eigen_pair
from bin.power_method.second_eigen_pair import next_eigen_pair
from bin.constants import *

# eigen_pair = max_eigen_pair(MATRIX_1, EPS, P, EPS)
print(next_eigen_pair(TEST_MATRIX_1, [(4.45, [[0.88], [0.45], [0.15]])], EPS, 4))
