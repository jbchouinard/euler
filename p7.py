from collections import defaultdict


def primes(n):
    ' Find primes up to n. '
    candidates = defaultdict(lambda: 1)
    for p in range(2, n):
        if candidates[p]:
            for k in range(2*p, n, p):
                candidates[k] = 0
    return sorted(p for p in candidates if candidates[p])


print(primes(12000)[10000])
