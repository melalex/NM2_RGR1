def pretty_print(eigen_pair):
    eigen_values, eigen_vectors, iter_count = eigen_pair
    print('Eigen values:')
    print(eigen_values)

    print('Eigen vectors:')
    print(eigen_vectors)

    print('Iteration count:', iter_count)
