# codecs — Codec registry and base classes

Here's an example of using the `codecs` module from Python's standard library:

```python
import codecs

# List all available encodings
print("Available Encodings:")
for encoding in codecs.encode_names():
    print(encoding)

# List all available codecs
print("\nAvailable Codecs:")
for codec in codecs.CodecInfo:
    print(codec.name)

# Register a custom codec
class CustomCodec(codecs.Codec):
    def encode(self, text, errors='strict'):
        # Implement your encoding logic here
        return "Encoded text"

    def decode(self, text, errors='strict'):
        # Implement your decoding logic here
        return "Decoded text"

codecs.register(CustomCodec)

# Create an instance of the custom codec
custom_codec = codecs.CodecInfo("custom_codec")

# List all registered codecs
print("\nRegistered Codecs:")
for codec in codecs.getreg():
    print(codec.name)
```

And here's an example of using the `coder` class from the `codecs` module:

```python
import codecs

class TextEncoder(codecs.Coder):
    def encode(self, text, errors='strict'):
        # Implement your encoding logic here
        return "Encoded text"

class TextDecoder(codecs.Decoder):
    def decode(self, text, errors='strict'):
        # Implement your decoding logic here
        return "Decoded text"

# Create an instance of the encoder and decoder
encoder = codecs.TextEncoder()
decoder = codecs.TextDecoder()

# Encode some text using the encoder
text = "Hello World!"
encoded_text = encoder.encode(text)
print(f"Encoded Text: {encoded_text}")

# Decode some text using the decoder
decoded_text = decoder.decode(encoded_text)
print(f"Decoded Text: {decoded_text}")
```

Here's an example of using the `open` function with codecs from the `codecs` module:

```python
import codecs

def read_file_with_codec(file_path, codec_name):
    try:
        # Open the file in binary mode
        with open(file_path, 'rb') as file:
            # Read the contents of the file using the specified codec
            data = file.read()
            # Decode the data using the specified codec
            decoded_data = codecs.decode(data, codec_name)
            return decoded_data
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print(f"An error occurred: {e}")

# Read a file with the specified codec
file_path = "path_to_your_file.txt"
codec_name = "utf-8"

decoded_data = read_file_with_codec(file_path, codec_name)
print(decoded_data)

# Write data to a file using the specified codec
def write_data_to_file(data, file_path, codec_name):
    try:
        # Open the file in binary mode
        with open(file_path, 'wb') as file:
            # Encode the data using the specified codec
            encoded_data = codecs.encode(data, codec_name)
            # Write the encoded data to the file
            file.write(encoded_data)
    except Exception as e:
        print(f"An error occurred: {e}")

# Write some data to a file with the specified codec
data = "Hello World!"
file_path = "path_to_your_file.txt"
codec_name = "utf-8"

write_data_to_file(data, file_path, codec_name)
```

Note that these examples are just illustrations and you should adjust them according to your needs. Also note that not all codecs can be used for every type of data (e.g., some codecs may not work well with binary data).
