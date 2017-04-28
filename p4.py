from p3 import *


def is_palindrome(word):
    word = str(word)
    for k in xrange(len(word) / 2):
        if word[k] != word[-1-k]:
            return False
    return True

if __name__ == '__main__':
    print(max(((x, y, x*y) for x in xrange(100, 1000) for y in xrange(100, 1000)
          if is_palindrome(x*y)), key=lambda r: r[2]))
