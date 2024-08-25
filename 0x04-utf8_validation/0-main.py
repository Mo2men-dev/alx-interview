#!/usr/bin/python3
"""
Main file for testing
"""

validUTF8 = __import__('0-validate_utf8').validUTF8

data1 = [467, 133, 108]
print(validUTF8(data1))

data2 = [240, 188, 128, 167]
print(validUTF8(data2))

data3 = [235, 140]
print(validUTF8(data3))

data4 = [345, 467]
print(validUTF8(data4))

data5 = [250, 145, 145, 145, 145]
print(validUTF8(data5))

data6 = [0, 0, 0, 0, 0, 0]
print(validUTF8(data6))

data7 = []
print(validUTF8(data7))
