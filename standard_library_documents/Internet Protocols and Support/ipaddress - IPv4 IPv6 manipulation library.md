# ipaddress - IPv4/IPv6 manipulation library

Here's an example of using the `ipaddress` module from Python's standard library:

```python
# Import the ipaddress module
import ipaddress

# Create an IPv4 address object
ipv4_addr = ipaddress.IPv4Address("192.168.1.100")

# Get the IP address as a string
print(f"IPv4 Address: {ipv4_addr}")

# Check if the address is valid
print(f"Is Valid: {ipv4_addr.is_valid()}")

# Create an IPv6 address object
ipv6_addr = ipaddress.IPv6Address("2001:0db8:85a3:0000:0000:8a2e:0370:7334")

# Get the IP address as a string
print(f"IPv6 Address: {ipv6_addr}")

# Check if the address is valid
print(f"Is Valid: {ipv6_addr.is_valid()}")

# Create an IPv4 network object
ipv4_network = ipaddress.IPv4Network("192.168.1.0/24", strict=False)

# Get the network as a string
print(f"IPv4 Network: {ipv4_network}")

# Check if the address is in the network
print(f"Is Address in Network: {ipv4_addr in ipv4_network}")

# Create an IPv6 network object
ipv6_network = ipaddress.IPv6Network("2001:0db8:85a3:0000:0000:8a2e:0370:7334/64", strict=False)

# Get the network as a string
print(f"IPv6 Network: {ipv6_network}")

# Check if the address is in the network
print(f"Is Address in Network: {ipv6_addr in ipv6_network}")

# Create an IPv4 prefix object
ipv4_prefix = ipaddress.IPv4PrefixNetwork("192.168.1.0/24", strict=False)

# Get the prefix as a string
print(f"IPv4 Prefix: {ipv4_prefix}")

# Create an IPv6 prefix object
ipv6_prefix = ipaddress.IPv6PrefixNetwork("2001:0db8:85a3:0000:0000:8a2e:0370:7334/64", strict=False)

# Get the prefix as a string
print(f"IPv6 Prefix: {ipv6_prefix}")

# Create an IPv4 network with specific parameters
ipv4_network_params = ipaddress.IPv4Network("192.168.1.100/32")

# Get the network as a string
print(f"IPv4 Network Parameters: {ipv4_network_params}")

# Create an IPv6 network with specific parameters
ipv6_network_params = ipaddress.IPv6Network("2001:0db8:85a3:0000:0000:8a2e:0370:7334/64")

# Get the network as a string
print(f"IPv6 Network Parameters: {ipv6_network_params}")

# Create an IPv4 address from a string (valid)
ipv4_addr_str = ipaddress.IPv4Address("192.168.1.100")

# Check if the address is valid
print(f"Is Valid Address: {ipv4_addr_str.is_valid()}")

# Create an IPv6 address from a string (valid)
ipv6_addr_str = ipaddress.IPv6Address("2001:0db8:85a3:0000:0000:8a2e:0370:7334")

# Check if the address is valid
print(f"Is Valid Address: {ipv6_addr_str.is_valid()}")
```

This script creates various objects from the `ipaddress` module, including addresses and networks, and demonstrates how to manipulate them. The output includes information about each object's validity, string representation, and other properties.

Here are some key concepts demonstrated in this code:

*   Creating IP address objects: You can create IP address objects using the `IP` class from the `ipaddress` module.
*   Validating IP addresses: You can use the `is_valid()` method to check if an IP address is valid or not.
*   Working with networks: You can create network objects using the `IPv4Network` and `IPv6Network` classes, which provide methods for working with networks such as checking if an address is within a given network range.
*   Creating prefixes: You can create prefix objects using the `IPv4PrefixNetwork` and `IPv6PrefixNetwork` classes, which provide methods for working with prefixes.
*   Converting between strings and IP address objects: You can use the `IP` class to create IP address objects from string representations.
