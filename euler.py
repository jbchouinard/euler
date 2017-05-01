"""
Functions for solving Project Euler problems.
https://projecteuler.net
"""
import math
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


def prime_factors(n):
    " Returns prime factors of n "
    facs = []
    while not is_prime(n):
        for p in primes_naive(2, n):
            if n % p == 0:
                facs.append(p)
                n = n / p
                break
    return facs + [n]


def primes_sieve(n):
    " List primes in range up to n. "
    candidates = defaultdict(lambda: 1)
    for p in range(2, n):
        if candidates[p]:
            for k in range(2*p, n, p):
                candidates[k] = 0
    return sorted(p for p in candidates if candidates[p])


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


class Grid(object):

    def __init__(self, grid, rowsep='\n', colsep=' ', conv=int):
        """
        Create a 2d grid from a string representation.

        The grid is indexed in row-major order starting at the top left corner.
        """
        lines = grid.split(rowsep)
        self.width = len(lines)
        self.height = len(lines[0].split(colsep))
        self.array = []
        self.transposed = [[] for _ in range(self.width)]
        for line in lines:
            vals = [conv(x) for x in line.split(colsep)]
            self.array.append(vals)
            for i in range(self.width):
                self.transposed[i].append(vals[i])

    def __getitem__(self, val):
        return self.array.__getitem__(val)

    def is_in_grid(self, x, y):
        return (0 <= x < self.width) and (0 <= y < self.height)

    def row(self, x, y, n):
        " Take a row slice of n elements starting at (x,y). "
        try:
            return self.array[x][y:y+n]
        except IndexError:
            return []

    def col(self, x, y, n):
        " Take a column slice of n elements starting at (x,y). "
        try:
            return self.transposed[y][x:x+n]
        except IndexError:
            return []

    def rdiag(self, x, y, n):
        " Take a right-diagonal slice of n elements starting at (x,y). "
        idx = [(x+i, y+i) for i in range(n) if self.is_in_grid(x+i, y+i)]
        return [self.array[x][y] for x, y in idx]

    def ldiag(self, x, y, n):
        " Take a left-diagonal slice of n elements starting at (x,y). "
        idx = [(x-i, y+i) for i in range(n) if self.is_in_grid(x+i, y+i)]
        return [self.array[x][y] for x, y in idx]
