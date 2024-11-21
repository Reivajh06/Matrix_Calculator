from src.matrix_operations import *
import re
import ollama


NUM_MATRICES_BY_OPERATION = {
    'add': 2,
    'subtract': 2,
    'multiply': 2,
    'transpose': 1,
    'trace': 1,
    'determinant': 1,
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

    else:
        raise ValueError("Unknown operation")


def create_matrix_based_on_operation(number_of_matrices=1):
    if number_of_matrices == 2:
        matrix1 = create_matrix()
        matrix2 = create_matrix()

        return matrix1, matrix2

    return create_matrix()


def run_calculator(user_operation):
    matrices = create_matrix_based_on_operation(NUM_MATRICES_BY_OPERATION[user_operation])

    result = calculate(user_operation, matrices)

    if isinstance(result, float):
        print(result)

    print_matrix(result)

    user_help = input("Do you need an explanation for the operation result from the AI?: yes/no ")

    if user_help == 'yes':
        input_matrices = f"{matrices[0]} {matrices[1]}" if isinstance(matrices, tuple) else str(matrices)

        prompt = f"""
        You're a Teacher AI that excels at matrix operations.
        
        Explain the result of the operation {user_operation} step by step:
        
        {input_matrices} = {result}
        
        Answer in a friendly way in plain text only. Represent matrices in a pretty way
        """

        response = ollama.generate(model='qwen2-math:7b-instruct-q8_0', prompt=prompt, stream=True)

        for part in response:
            print(part["response"], end='')



if __name__ == "__main__":
    user_operation = input("Introduce which operation you want to do: add/subtract/multiply/trace/determinant/transpose/identity matrix/scalar multiplication:\n ")

    run_calculator(user_operation.strip().lower())

