#!/usr/bin/python3
"""
Veryfing UTF-8 encoding
"""
from typing import List


def int_to_bin(num: int, bin_str: str = "") -> str:
    """
    Function that converts an int to a bin
    """

    if num > 1:
        bin_str = int_to_bin(num // 2, bin_str)

    bin_str += str(num % 2)

    if len(bin_str) < 8:
        bin_str = "0" * (8 - len(bin_str)) + bin_str

    return bin_str[-8:]


def utf8_bytes(num: int) -> int:
    """
    Method that gets the num of bytes
    for an int num
    """

    bn = int_to_bin(num)
    bit = 0

    while (int(bn[bit]) != 0):
        bit += 1

    return bit - 1


def validUTF8(data: List[int]) -> bool:
    """
    Method that determines if a given
    data set represents a valid UTF-8 encoding
    """

    i = 0
    while i < len(data):
        bytes = utf8_bytes(int(data[i]))
        if bytes > 0:
            while (bytes > 0):
                i += 1
                bn = int_to_bin(data[i])

                if (bn[:2] != "10"):
                    return False

                bytes -= 1
        else:
            i += 1

    return True
