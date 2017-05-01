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


if __name__ == '__main__':
    print(max(prime_factors(600851475143)))
