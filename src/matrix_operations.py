def is_square(matrix):
    """
    Evaluates whether a matrix is square or not
    :param matrix:
    :return: True if it is square, else False
    """
    for index in range(len(matrix)):
        if len(matrix) != len(matrix[index]):
            return False

    return True


def print_matrix(matrix):
    matrix_printed = ""
    for row in matrix:
        matrix_printed += str(row) + "\n"

    return matrix_printed


def trace(matrix):
    """
    Method which evaluate the trace of a square matrix
    :param matrix:
    :return: diagonal sum if it is a square matrix, else return a string advice
    """
    trace_result = 0

    if is_square(matrix):

        for i in range(len(matrix)):
            trace_result += matrix[i][i]

        return trace_result

    return f"The given matrix: \n{print_matrix(matrix)}is not a square matrix!"


def determinant(matrix):
    """
    Method which calculates the determinant of a square matrix
    :param matrix:
    :return: determinant of a square matrix
    """

    if is_square(matrix):
        if len(matrix) == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

        determinant_result: int = 0

        for j in range(len(matrix)):
            #Using the cofactors method, recursive is required, being the square matrix of 2 the base case
            cofactor_matrix = [row[:j] + row[j + 1:] for row in matrix[1:]]
            determinant_result += (-1) ** j * matrix[0][j] * determinant(cofactor_matrix)

        return determinant_result

    return f"The given matrix: \n{print_matrix(matrix)}is not a square matrix!"

