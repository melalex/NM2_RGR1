from scipy import linalg as ln

import bin.aitken_process.max_eigen_pair
from bin.dot_product.max_eigen_pair import max_eigen_pair
from bin.dot_product.next_pair import next_pair
from bin.jacobi_method.eigen_pairs import eigen_pairs
from bin.lu.decompose import decomposition
from bin.lu.solve import solve
from bin.lu_method.eigen_pairs import eigen_pairs

from bin.power_method.second_max_pair import second_max_pair
from bin.power_method.second_min_pair import second_min_pair
from bin.constants import *

# eigen_pair = max_eigen_pair(MATRIX_1, EPS, P, EPS)
# print(second_max_pair(MATRIX_1, eigen_pair, EPS, EPS))
# min_pir = min_eigen_pair(MATRIX_1, eigen_pair[0], EPS, P, EPS)
# print(second_min_pair(MATRIX_1, min_pir, EPS, EPS))

# print(bin.aitken_process.max_eigen_pair.max_eigen_pair(MATRIX_1, EPS, P, P, EPS))

# max_pair = max_eigen_pair(MATRIX_2, EPS)
# print(next_pair(MATRIX_2, [max_pair], 3, EPS))

# print(eigen_pairs(MATRIX_2, EPS))

print(eigen_pairs(MATRIX_2, EPS))
