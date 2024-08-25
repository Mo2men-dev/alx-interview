#!/usr/bin/python3
"""
Main file for testing
"""

validUTF8 = __import__('0-validate_utf8').validUTF8

data1 = [226, 130, 172]
print(validUTF8(data1))

data2 = [65]
print(validUTF8(data2))

data3 = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data3))

data4 = [229, 65, 127, 256]
print(validUTF8(data4))
