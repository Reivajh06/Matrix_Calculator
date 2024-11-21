from src.matrix_operations import *
import re


def create_matrix_based_on_operation(number_of_matrixes=1):
    if number_of_matrixes == 2:
        matrix1 = create_matrix()
        matrix2 = create_matrix()

        return matrix1, matrix2

    return create_matrix()


def run_calculator(user_operation):

    if user_operation == 'add':
        matrixes = create_matrix_based_on_operation(2)

        print_matrix(add(matrixes[0], matrixes[1]))

    if user_operation == 'subtract':
        matrixes = create_matrix_based_on_operation(2)

        print_matrix(subtract(matrixes[0], matrixes[1]))

    if user_operation == 'multiply':
        matrixes = create_matrix_based_on_operation(2)

        print_matrix(subtract(matrixes[0], matrixes[1]))
        
    if user_operation == 'transpose':
        print_matrix(transpose(create_matrix_based_on_operation()))
    
    if user_operation == 'trace':
        print_matrix(trace(create_matrix_based_on_operation()))

    if user_operation == 'determinant':
        print_matrix(determinant(create_matrix_based_on_operation()))





user_operation = input("Introduce which operation you want to do: add/subtract/multiply/trace/determinant/transpose/identity matrix/scalar multiplication:\n ")
run_calculator(user_operation.strip().lower())

