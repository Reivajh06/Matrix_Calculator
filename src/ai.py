import time

import ollama

LLM_MODEL = 'qwen2-math:7b-instruct-q8_0'


def explain_with_ai(user_operation, matrices, result):
    input_matrices = f"{matrices[0]} {matrices[1]}" if isinstance(matrices, tuple) else str(matrices)

    prompt = f"""
            You're a Teacher AI that excels at matrix operations.
            
            Explain the result of the operation {user_operation} step by step:
            
            {input_matrices} = {result}
            
            Instructions:
            - Explain step by step the matrix operation
            - Write the response using plain text only
            - Avoid the use of markdown, latex or other code-like syntax
            
            """

    response = ollama.generate(model=LLM_MODEL, prompt=prompt, stream=True)

    for part in response:
        print(part["response"], end='')
        time.sleep(0.1)

def ai_is_available():
    try:
        for model in ollama.list()["models"]:
            if model['name'] == LLM_MODEL:
                return True

        return False
    except:
        return False