if __name__ == '__main__':
    # If a, b, c is a Pythagorean triplet, a**2 + b**2 = c**2

    # (ka)**2 + (kb)**2 = k**2 * a**2 + k**2 * b**2
    #                   = k**2(a**2 + b**2)
    #                   = k**2 * c**2
    #                   = (kc)**2

    # Thus ka, kb, kc is also a Pythagorean triplet for any integer k.

    # 3, 4, 5 is a Pythagorean triplet.

    # 3k + 4k + 5k = 12k = 1000
    # k = 1000/12
    print((3*(1000/12), 4*(1000/12), 5*(1000/12)))
