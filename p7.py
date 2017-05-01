from collections import defaultdict
from time import time

from euler import primes_sieve


if __name__ == '__main__':
    start = time()
    print(primes_sieve(150000)[10000])
    print('elapsed: %f seconds' % (time() - start))    
