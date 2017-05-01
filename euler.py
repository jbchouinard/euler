"""
Functions for solving Project Euler problems.
https://projecteuler.net
"""
from collections import defaultdict


def is_prime(n):
    " Is n prime? "
    if n < 1:
        return False
    if n < 3:
        return True
    for k in xrange(2, n):
        if n % k == 0:
            return False
    return True


def primes_naive(n, m):
    " Yields primes in range [n, m). "
    for x in xrange(n, m):
        if is_prime(x):
            yield x


def primes_sieve(n):
    " List primes in range up to n. "
    candidates = defaultdict(lambda: 1)
    for p in range(2, n):
        if candidates[p]:
            for k in range(2*p, n, p):
                candidates[k] = 0
    return sorted(p for p in candidates if candidates[p])


def prime_factors(n):
    " Returns prime factors of n "
    facs = []
    while not is_prime(n):
        for p in primes_sieve(n):
            if n % p == 0:
                facs.append(p)
                n = n / p
                break
    return facs + [n]


def fib(n, x=1, y=2):
    while x <= n:
        yield x
        x, y = y, x + y


def is_palindrome(word):
    word = str(word)
    for k in xrange(len(word) / 2):
        if word[k] != word[-1-k]:
            return False
    return True


def moving_box(series, n, pad=False):
    if pad is not False:
        series = ([pad] * (n-1)) + series + ([pad] * (n-1))
    for i in range(len(series) - n + 1):
        yield series[i:i+n]


def product(lst):
    n = 1
    for x in lst:
        n *= int(x)
    return n
