from ollama import chat

def generate_code_example(module):
    messages = [
        {
            'role': 'system',
            'content': (
                'You are a Python version 3.12 code generator. Your job is to create comprehensive and well-documented code examples '
                'for every possible functionality in the provided Python standard library module. Ensure that the examples are '
                'clear, concise, and include comments explaining each step. The code should follow best practices and be suitable '
                'for inclusion in official documentation.'
            ),
        },
        {
            'role': 'user',
            'content': f'Generate code examples for the Python standard library module: {module}',
        },
    ]
    response = chat(model='qwen2.5-coder:3b', messages=messages)
    return response['message']['content']