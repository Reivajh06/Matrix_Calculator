import src.matrix_operations


def run_calculator(user_response):
    pass

def create_matrix(rows, columns, elements):

    if len(elements) is not rows * columns:
        print(f"The number of elements introduced should be {rows * columns} instead of {len(elements)}")

    matrix = []

    for i in range(rows):
        row = []
        for j in range(columns):
            row.append(int(elements[columns]))

        matrix = matrix + row

    src.matrix_operations.print(matrix)

user_operation = input("Introduce which operation to do: sum/subtract/multiply/trace/determinant/transpose/identity matrix/scalar multiplication")

rows = input("Introduce how many rows the matrix has: ")

columns = input("Introduce how many columns the matrix has: ")

elements = input("Introduce each element within the matrix separated by single spaces: ")

create_matrix(int(rows), int(columns), elements.split(' '))
