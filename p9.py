from euler import product


def find_pyth():
    for a in range(1, 999):
        for b in range(a, 1000):
            c = 1000 - a - b
            if c**2 == a**2 + b**2:
                return (a, b, c)

if __name__ == '__main__':
    print(product(find_pyth()))
    print('elapsed: %f seconds' % (time() - start))