from euler import fib


if __name__ == '__main__':
    print(sum(x for x in fib(4000000) if x % 2 == 0))
