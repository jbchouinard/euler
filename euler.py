"""
Functions for solving Project Euler problems.
https://projecteuler.net
"""
import math
from collections import defaultdict


def triangle_series():
    n = 1
    s = 0
    while True:
        s += n
        n += 1
        yield s


def divisors(n):
    for x in xrange(1, int(math.sqrt(n))+1):
        if n % x == 0:
            yield x
            yield n / x


def count(series):
    n = 0
    for _ in series:
        n += 1
    return n


def is_prime(n):
    " Is n prime? "
    if n < 2:
        return False
    if n == 2:
        return True
    for x in xrange(2, int(math.sqrt(n))+1):
        if n % x == 0:
            return False
    return True


def primes_naive(m, known=[]):
    " Yields primes up to m. "
    n = 1
    for p in known:
        n = p
        if n > m:
            return
        yield n
    for x in xrange(n+1, m):
        if is_prime(x):
            known.append(x)
            yield x


def prime_factors(n):
    " Returns prime factors of n "
    facs = []
    while not is_prime(n):
        for p in primes_naive(n):
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


class NumberTriangle(object):

    def __init__(self, triangle, rowsep='\n', colsep=' '):
        " Create triangle of numbers from string representation. "
        self.triangle = []
        n = 1
        for line in triangle.split(rowsep):
            vals = map(int, line.split(colsep))
            assert len(vals) == n
            n += 1
            self.triangle.append(vals)

    def __getitem__(self, i):
        return self.triangle[i]

    def left_parent(self, row, i):
        if i == 0:
            return 0
        return self.triangle[row-1][i-1]

    def right_parent(self, row, i):
        if i == (len(self.triangle[row])-1):
            return 0
        return self.triangle[row-1][i]


def binomial_permutations(n, m):
    """
    Number of unique permutations of (n+m) coins such that there are
    n tails and m heads.
    """
    solutions = [[0] * (m+1) for _ in range(n+1)]
    for x in range(1, n+1):
        solutions[x][0] = 1
    for y in range(1, m+1):
        solutions[0][y] = 1
    for x in range(1, n+1):
        for y in range(1, m+1):
            solutions[x][y] = solutions[x-1][y] + solutions[x][y-1]
    return solutions[n][m]


def collatz(n):
    " Find collatz sequence starting at n. "
    path = []
    while n != 1:
        path.append(n)
        if n % 2 == 0:
            n = n / 2
        else:
            n = n * 3 + 1
    path.append(1)
    return path