def square_matrix_simple(matrix=[]):
    """computes the square value of all ints in a matrix
    matrix - 2d array
    initial matrix not modified
    """

    new_matrix = matrix.copy()

    for row in range(len(matrix)):
        new_matrix[row] = list(map(lambda x: x**2, matrix[row]))
    return new_matrix
