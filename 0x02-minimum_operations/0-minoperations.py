#!/usr/bin/env python3
"""
Minimum Operations Problem - Minimum Operations to Get N from 1
"""


def get_primes(n: int) -> list:
    """
    Get all prime numbers from 1 to n
    Args:
        n: int - The number to get prime numbers from 1 to n
    Returns:
        list - A list of prime numbers from 1 to n
    """
    primes = []
    for i in range(1, n + 1):
        dv_count = 0
        for j in range(2, i + 1):
            if i % j == 0:
                dv_count += 1
        if dv_count == 1:
            primes.append(i)

    return primes


def prime_factor(n: int) -> list:
    """
    Get the prime factors of a number
    Args:
        n: int - The number to get the prime factors
    Returns:
        list - A list of prime factors of the number
    """
    primes = get_primes(n)
    primed = n
    factor = []

    for i in primes:
        while primed % i == 0:
            factor.append(i)
            primed = primed / i

    return factor


def minOperations(n: int) -> int:
    """
    Get the minimum operations to get n from 1
    Args:
        n: int - The number to get the minimum operations
    Returns:
        int - The minimum operations to get n from 1
    """
    return sum(prime_factor(n))
