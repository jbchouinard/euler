from p1 import *


def fib(n, x=1, y=2):
    while x <= n:
        yield x
        x, y = y, x + y

if __name__ == '__main__':
    print(sum(x for x in fib(4000000) if x % 2 == 0))
