from collections import Counter
from time import time

from euler import prime_factors


def join_factors(f1, f2):
    fs = {}
    for k in set(f1.keys()) | set(f2.keys()):
        fs[k] = max(f1.get(k, 0), f2.get(k, 0))
    return fs


def multiply_factors(f):
    n = 1
    for k in f:
        n *= k**f[k]
    return n


if __name__ == '__main__':
    start = time()
    n = 100
    facs = {}

    for i in xrange(2, n+1):
        facs = join_factors(facs, Counter(prime_factors(i)))

    print(multiply_factors(facs))
    print('elapsed: %f seconds' % (time() - start))