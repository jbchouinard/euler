from collections import Counter


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


def primes(n, m):
    " Yields primes in range [n, m) "
    for x in xrange(n, m):
        if is_prime(x):
            yield x


def prime_factors(n):
    " Returns prime factors of n "
    facs = []
    while not is_prime(n):
        for p in primes(2, n):
            if n % p == 0:
                facs.append(p)
                n = n / p
                break
    return facs + [n]


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


n = 20
facs = {}

for i in xrange(1, n+1):
    facs = join_factors(facs, Counter(prime_factors(i)))

print(multiply_factors(facs))
