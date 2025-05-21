from ollama import chat
from typing import Dict

# Manual fallback examples for common modules
manual_examples: Dict[str, str] = {
    'math': '''import math
# Calculate square root
print(math.sqrt(16))
# Compute cosine
print(math.cos(math.pi))''',
    're': '''import re
pattern = r"\\w+"
text = "Hello world!"
print(re.findall(pattern, text))''',
    'datetime': '''from datetime import datetime, timedelta
# Current date and time
now = datetime.now()
print(now)
# Add 5 days
future = now + timedelta(days=5)
print(future)''',
    'json': '''import json
data = {'name': 'Alice', 'age': 30}
# Convert to JSON string
json_str = json.dumps(data)
print(json_str)
# Parse JSON string
parsed = json.loads(json_str)
print(parsed['name'])''',
    'os': '''import os
# Get current working directory
cwd = os.getcwd()
print(f"Current directory: {cwd}")
# List files
print(os.listdir(cwd))''',
    'os.path': '''import os
# Common path manipulations
print(os.path.basename('/folder/file.txt'))
print(os.path.dirname('/folder/file.txt'))''',
    'pathlib': '''from pathlib import Path
# Create a Path object
p = Path('.') / 'test.txt'
# Check existence
print(p.exists())
# Read text if exists
if p.exists():
    print(p.read_text())''',
    'itertools': '''import itertools
# Create product of two lists
for combo in itertools.product([1,2], ['a','b']):
    print(combo)
# Generate permutations
for perm in itertools.permutations([1,2,3], 2):
    print(perm)''',
    'threading': '''import threading, time
def worker():
    print('Worker thread is running')
    time.sleep(1)
# Start thread
t = threading.Thread(target=worker)
t.start()
t.join()
print('Thread completed')''',
    'argparse': '''import argparse
# Create parser
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')
args = parser.parse_args()
print(args.accumulate(args.integers))''',
    'logging': '''import logging
# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logger.info('This is an info message')
logger.error('This is an error message')''',
    'subprocess': '''import subprocess
# Run a command and capture output
result = subprocess.run(['echo', 'Hello, World!'], capture_output=True, text=True)
print('Return code:', result.returncode)
print('Output:', result.stdout)''',
    'random': '''import random
# Generate a random integer between 1 and 10
print(random.randint(1, 10))
# Shuffle a list
items = [1, 2, 3, 4, 5]
random.shuffle(items)
print(items)''',
    'csv': '''import csv
# Write CSV file
data = [['name','age'], ['Alice','30'], ['Bob','25']]
with open('data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)
# Read CSV file
with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)''',
    'asyncio': '''import asyncio
async def say_hello():
    await asyncio.sleep(1)
    print('Hello after 1 second')
# Run the async function
asyncio.run(say_hello())''',
    'socket': '''import socket
# Create a TCP socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('example.com', 80))
    s.sendall(b'GET / HTTP/1.0\r\nHost: example.com\r\n\r\n')
    data = s.recv(1024)
    print(data)''',
    'http.client': '''import http.client
# Create an HTTP connection
conn = http.client.HTTPConnection('example.com')
# Send a GET request
conn.request('GET', '/')
resp = conn.getresponse()
print(resp.status, resp.reason)
print(resp.read())
conn.close()''',
    'functools': '''import functools
# Create a partial function
def add(a, b): return a + b
add_five = functools.partial(add, 5)
print(add_five(10))  # Outputs 15''',
    'collections': '''from collections import deque, Counter, defaultdict
# Deque example
d = deque([1, 2, 3])
d.appendleft(0)
print(d)
# Counter example
cnt = Counter('aabbb')
print(cnt)
# defaultdict example
dd = defaultdict(int)
print(dd['missing'])  # Outputs 0''',
    'sys': '''import sys
# Python version
print(sys.version)
# Platform
print(sys.platform)''',
    'pickle': '''import pickle
# Serialize object
data = {'a': 1, 'b': 2}
with open('data.pkl', 'wb') as f:
    pickle.dump(data, f)
# Deserialize object
with open('data.pkl', 'rb') as f:
    loaded = pickle.load(f)
print(loaded)''',
    'shutil': '''import shutil, os
# Copy file
src = 'data.txt'; dst = 'data_copy.txt'
open(src, 'w').write('example')
shutil.copy(src, dst)
print(os.path.exists(dst))''',
    'decimal': '''from decimal import Decimal, getcontext
# Set precision
getcontext().prec = 4
a = Decimal('1.2345')
b = Decimal('2.3456')
print(a + b)''',
    'fractions': '''from fractions import Fraction
# Create fractions
a = Fraction(1, 3)
b = Fraction(2, 5)
print(a + b)''',
    'statistics': '''import statistics
# Compute mean, median, and mode
data = [1, 2, 2, 3, 4]
print(statistics.mean(data))
print(statistics.median(data))
print(statistics.mode(data))''',
    'zipfile': '''import zipfile
# Create zip archive
with zipfile.ZipFile('test.zip', 'w') as zf:
    zf.writestr('file.txt', 'Hello World')
# Read zip archive
with zipfile.ZipFile('test.zip', 'r') as zf:
    print(zf.namelist())''',
    'tarfile': '''import tarfile
# Create tar archive
t = tarfile.open('test.tar', 'w')
t.add('data.txt')
t.close()
# List tar contents
with tarfile.open('test.tar', 'r') as t:
    print(t.getnames())''',
}

def generate_code_example(module):
    # Return manual example if available
    key = module.split(' - ')[0]
    if key in manual_examples:
        return manual_examples[key]
    # Prepare AI messages
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
    try:
        response = chat(model='qwen2.5-coder:3b', messages=messages)
        return response.get('message', {}).get('content', '')
    except Exception:
        return f"# Example for {module} is unavailable at the moment."