import src.matrix_operations
import re


def run_calculator():
    user_operation = input("Introduce which operation to do: sum/subtract/multiply/trace/determinant/transpose/identity matrix/scalar multiplication:\n ")

    rows = input("Introduce how many rows the matrix has: ")

    columns = input("Introduce how many columns the matrix has: ")

    elements = input("Introduce each element within the matrix separated by single spaces: ")

    src.matrix_operations.create_matrix(int(rows), int(columns), re.split(r" +", elements.strip()))


run_calculator()

