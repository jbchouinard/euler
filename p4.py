from euler import is_palindrome


if __name__ == '__main__':
    print(max(((x, y, x*y) for x in xrange(100, 1000)
          for y in xrange(100, 1000)
          if is_palindrome(x*y)), key=lambda r: r[2]))
