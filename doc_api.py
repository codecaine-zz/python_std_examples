from ollama import chat

def generate_code_example(module):
    messages = [
        {
            'role': 'system',
            'content': 'You are a Python version 3.12 code generator. Your job is to create every code examples for every possible thing that be done in the python module from the standard library when provided with a module name. Add comments to the code',
        },
        {
            'role': 'user',
            'content': module,
        },
    ]
    response = chat(model='llama3.2', messages=messages)
    return response['message']['content']

