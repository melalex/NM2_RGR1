from bin.dot_product.max_eigen_pair import max_eigen_pair
from bin.dot_product.next_pair import next_pair
from bin.pretty_print import pretty_print
from bin.constants import *

max_pair = max_eigen_pair(MATRIX_2, EPS)
pairs = [max_pair]

print('Max eigen pair:')
pretty_print(max_pair)
print('===========================')

for i in range(1, len(MATRIX_2)):
    pair = next_pair(MATRIX_2, pairs, P, EPS)
    pairs.append(pair)

    print('Max eigen pair #%d:' % i)
    pretty_print(pair)
    print('===========================')
