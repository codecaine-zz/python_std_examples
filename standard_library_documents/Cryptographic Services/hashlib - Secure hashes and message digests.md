# hashlib — Secure hashes and message digests

Here's an example of how you can use the `hashlib` module from Python's standard library:

```python
import hashlib

# Create a new SHA-256 hash object
sha256_hash = hashlib.sha256()

# Update the hash object with some data
data_to_hash = b'Hello, World!'
sha256_hash.update(data_to_hash)

# Get the hexadecimal representation of the hash
hash_hex = sha256_hash.hexdigest()
print(f"SHA-256 Hash: {hash_hex}")

# Create a new SHA-512 hash object
sha512_hash = hashlib.sha512()

# Update the hash object with some data
data_to_hash = b'Hello, World!'
sha512_hash.update(data_to_hash)

# Get the hexadecimal representation of the hash
hash_hex = sha512_hash.hexdigest()
print(f"SHA-512 Hash: {hash_hex}")

# Create a new MD5 hash object
md5_hash = hashlib.md5()

# Update the hash object with some data
data_to_hash = b'Hello, World!'
md5_hash.update(data_to_hash)

# Get the hexadecimal representation of the hash
hash_hex = md5_hash.hexdigest()
print(f"MD5 Hash: {hash_hex}")

# Create a new RIPEMD-160 hash object
ripemd160_hash = hashlib.new('ripemd160')

# Update the hash object with some data
data_to_hash = b'Hello, World!'
ripemd160_hash.update(data_to_hash)

# Get the hexadecimal representation of the hash
hash_hex = ripemd160_hash.hexdigest()
print(f"RIPEMD-160 Hash: {hash_hex}")

# Create a new SHA-3 (Keccak-256) hash object
keccak_256_hash = hashlib.sha3_256()

# Update the hash object with some data
data_to_hash = b'Hello, World!'
keccak_256_hash.update(data_to_hash)

# Get the hexadecimal representation of the hash
hash_hex = keccak_256_hash.hexdigest()
print(f"SHA-3 (Keccak-256) Hash: {hash_hex}")
```

Here's a more advanced example that demonstrates how to use the `hashlib` module with different types of data:

```python
import hashlib

# Create a dictionary and convert it to bytes
data_dict = {'name': 'John', 'age': 30}
data_bytes = str(data_dict).encode('utf-8')

# Create a new SHA-256 hash object
sha256_hash = hashlib.sha256()

# Update the hash object with some data
sha256_hash.update(data_bytes)

# Get the hexadecimal representation of the hash
hash_hex = sha256_hash.hexdigest()
print(f"SHA-256 Hash: {hash_hex}")

# Create an image file and convert it to bytes
image_data = open('image.jpg', 'rb').read()
sha512_hash = hashlib.sha512()

# Update the hash object with some data
sha512_hash.update(image_data)

# Get the hexadecimal representation of the hash
hash_hex = sha512_hash.hexdigest()
print(f"SHA-512 Hash: {hash_hex}")

# Create a list and convert it to bytes
data_list = [1, 2, 3]
data_bytes_list = str(data_list).encode('utf-8')
md5_hash = hashlib.md5()

# Update the hash object with some data
md5_hash.update(data_bytes_list)

# Get the hexadecimal representation of the hash
hash_hex = md5_hash.hexdigest()
print(f"MD5 Hash: {hash_hex}")
```

These examples show how you can use the `hashlib` module to create secure hashes and message digests for different types of data, including strings, bytes, dictionaries, images, and lists.
