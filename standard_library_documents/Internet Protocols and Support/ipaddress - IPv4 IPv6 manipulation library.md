# ipaddress - IPv4/IPv6 manipulation library
## Table of Contents

1. [1. Creating an IPv4 Address](#1-creating-an-ipv4-address)
2. [2. Creating an IPv4 Network](#2-creating-an-ipv4-network)
3. [3. Checking if an IP is in a Network](#3-checking-if-an-ip-is-in-a-network)
4. [4. Iterating Over an IPv4 Network](#4-iterating-over-an-ipv4-network)
5. [5. Creating an IPv6 Address](#5-creating-an-ipv6-address)
6. [6. Creating an IPv6 Network](#6-creating-an-ipv6-network)
7. [7. Checking if an IPv6 is in a Network](#7-checking-if-an-ipv6-is-in-a-network)
8. [8. Iterating Over an IPv6 Network](#8-iterating-over-an-ipv6-network)
9. [9. Working with CIDR Notation](#9-working-with-cidr-notation)
10. [10. Comparing IP Addresses and Networks](#10-comparing-ip-addresses-and-networks)



The `ipaddress` module in Python provides a way to manipulate IPv4 and IPv6 addresses and networks efficiently. Below are comprehensive and well-documented examples covering various functionalities of this module:

### 1. Creating an IPv4 Address

```python
import ipaddress

# Create an IPv4 address object
ipv4_address = ipaddress.IPv4Address('192.168.1.1')

print(ipv4_address)  # Output: 192.168.1.1
```

### 2. Creating an IPv4 Network

```python
import ipaddress

# Create an IPv4 network object
ipv4_network = ipaddress.IPv4Network('192.168.1.0/24')

print(ipv4_network)  # Output: 192.168.1.0/24
```

### 3. Checking if an IP is in a Network

```python
import ipaddress

# Create a network and an address to check
network = ipaddress.IPv4Network('192.168.1.0/24')
address = ipaddress.IPv4Address('192.168.1.5')

if address in network:
    print(f"{address} is in the network {network}")
else:
    print(f"{address} is not in the network {network}")
```

### 4. Iterating Over an IPv4 Network

```python
import ipaddress

# Create a network and iterate over its addresses
network = ipaddress.IPv4Network('192.168.1.0/25')

for address in network:
    print(address)
```

### 5. Creating an IPv6 Address

```python
import ipaddress

# Create an IPv6 address object
ipv6_address = ipaddress.IPv6Address('2001:db8::1')

print(ipv6_address)  # Output: 2001:db8::1
```

### 6. Creating an IPv6 Network

```python
import ipaddress

# Create an IPv6 network object
ipv6_network = ipaddress.IPv6Network('2001:db8::/48')

print(ipv6_network)  # Output: 2001:db8::/48
```

### 7. Checking if an IPv6 is in a Network

```python
import ipaddress

# Create a network and an address to check
network = ipaddress.IPv6Network('2001:db8::/48')
address = ipaddress.IPv6Address('2001:db8::5')

if address in network:
    print(f"{address} is in the network {network}")
else:
    print(f"{address} is not in the network {network}")
```

### 8. Iterating Over an IPv6 Network

```python
import ipaddress

# Create a network and iterate over its addresses
network = ipaddress.IPv6Network('2001:db8::/56')

for address in network:
    print(address)
```

### 9. Working with CIDR Notation

```python
import ipaddress

# Parse an IPv4 address from a string and check the prefix length
ipv4_address = ipaddress.ip_address('192.168.1.1/24')
print(ipv4_address)  # Output: 192.168.1.1
print(ipv4_address.network)  # Output: 192.168.1.0/24

# Parse an IPv6 address from a string and check the prefix length
ipv6_address = ipaddress.ip_address('2001:db8::1/48')
print(ipv6_address)  # Output: 2001:db8::1
print(ipv6_address.network)  # Output: 2001:db8::/48
```

### 10. Comparing IP Addresses and Networks

```python
import ipaddress

# Create two IPv4 addresses
ip1 = ipaddress.IPv4Address('192.168.1.1')
ip2 = ipaddress.IPv4Address('192.168.1.2')

if ip1 < ip2:
    print(f"{ip1} is less than {ip2}")
elif ip1 > ip2:
    print(f"{ip1} is greater than {ip2}")
else:
    print(f"{ip1} is equal to {ip2}")

# Create two IPv4 networks
network1 = ipaddress.IPv4Network('192.168.1.0/24')
network2 = ipaddress.IPv4Network('192.168.2.0/24')

if network1 < network2:
    print(f"{network1} is less than {network2}")
elif network1 > network2:
    print(f"{network1} is greater than {network2}")
else:
    print(f"{network1} is equal to {network2}")
```

### 11. Address and Network Classifications

```python
import ipaddress

# Create an IPv4 address and classify it
ipv4_address = ipaddress.IPv4Address('192.168.1.1')
print(ipv4_address.is_loopback)  # Output: False
print(ipv4_address.is_multicast)  # Output: False
print(ipv4_address.is_private)  # Output: True

# Create an IPv6 address and classify it
ipv6_address = ipaddress.IPv6Address('2001:db8::1')
print(ipv6_address.is_loopback)  # Output: False
print(ipv6_address.is_multicast)  # Output: False
print(ipv6_address.is_private)  # Output: True

# Create an IPv4 network and classify it
ipv4_network = ipaddress.IPv4Network('192.168.1.0/24')
print(ipv4_network.is_link_local)  # Output: False
print(ipv4_network.is_global)  # Output: True

# Create an IPv6 network and classify it
ipv6_network = ipaddress.IPv6Network('2001:db8::/48')
print(ipv6_network.is_link_local)  # Output: True
print(ipv6_network.is_global)  # Output: False
```

### 12. Conversion between Address Types

```python
import ipaddress

# Create an IPv4 address and convert it to an integer
ipv4_address = ipaddress.IPv4Address('192.168.1.1')
integer_value = int(ipv4_address)
print(integer_value)  # Output: 3232235777

# Convert an integer back to an IPv4 address
reversed_ipv4_address = ipaddress.IPv4Address(integer_value)
print(reversed_ipv4_address)  # Output: 192.168.1.1
```

### 13. Creating and Manipulating Masks

```python
import ipaddress

# Create an IPv4 address with a custom mask
ipv4_address_with_mask = ipaddress.ip_address('192.168.1.1/25')
print(ipv4_address_with_mask)  # Output: 192.168.1.1/25

# Create an IPv4 network with a custom mask
ipv4_network_with_mask = ipaddress.ip_network('192.168.1.0/25')
print(ipv4_network_with_mask)  # Output: 192.168.1.0/25

# Get the subnet mask as an integer
subnet_mask = ipv4_network_with_mask.netmask
print(subnet_mask)  # Output: 4294967295 (full subnet mask)
```

These examples cover the basic functionalities of the `ipaddress` module, including creating and manipulating IPv4 and IPv6 addresses and networks, checking their properties, performing comparisons, and converting between different types.
