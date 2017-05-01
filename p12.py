import math
from time import time

from euler import prime_factors


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


if __name__ == '__main__':
    start = time()
    for n in triangle_series():
        if count(divisors(n)) >= 500:
            print(n)
            break
    print('elapsed: %f seconds' % (time() - start))
