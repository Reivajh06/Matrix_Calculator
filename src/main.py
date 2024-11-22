from src.matrix_operations import *
from ai import explain_with_ai, ai_is_available


NUM_MATRICES_BY_OPERATION = {
    'add': 2,
    'subtract': 2,
    'multiply': 2,
    'transpose': 1,
    'trace': 1,
    'determinant': 1,
    'scalar multiplication': 1,
    'matrix identity': 0
}


def calculate(user_operation, matrices):
    if user_operation == 'add':
        return add(matrices[0], matrices[1])

    elif user_operation == 'subtract':
        return subtract(matrices[0], matrices[1])

    elif user_operation == 'multiply':
        return multiply(matrices[0], matrices[1])

    elif user_operation == 'transpose':
        return transpose(matrices)

    elif user_operation == 'trace':
        return trace(matrices)

    elif user_operation == 'determinant':
        return determinant(matrices)

    elif user_operation == 'scalar multiplication':
        scalar_value = float(input("Indicate the scalar value for the operation: "))

        return multiply_scalar(matrices, scalar_value)

    elif user_operation == 'identity matrix':
        return identity_matrix(matrices)

    else:
        raise ValueError("Unknown operation")


def create_matrix_based_on_operation(number_of_matrices=1):
    if number_of_matrices == 2:
        matrix1 = create_matrix()
        matrix2 = create_matrix()

        return matrix1, matrix2

    return create_matrix()


def run_calculator(user_operation):
    if user_operation not in NUM_MATRICES_BY_OPERATION:
        print(f"Unknown operation {user_operation}")
        return

    matrices = create_matrix_based_on_operation(NUM_MATRICES_BY_OPERATION[user_operation])

    result = calculate(user_operation, matrices)

    if isinstance(result, float):
        print(result)

    print_matrix(result)

    if ai_is_available():
        user_help = input("Do you need an explanation for the operation result from the AI?: yes/no ")

        if user_help == 'yes':
            explain_with_ai(user_operation, matrices, result)



if __name__ == "__main__":
    user_operation = input("Introduce which operation you want to do: add/subtract/multiply/trace/determinant/transpose/identity matrix/scalar multiplication:\n ")

    run_calculator(user_operation.strip().lower())

