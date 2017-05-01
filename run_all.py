from __future__ import print_function

import re
from glob import glob


if __name__ == '__main__':
    def get_num(fn):
        return re.search(r'p([0-9]+)\.py', fn).group(1)
    
    files = sorted([(get_num(fn), fn) for fn in glob('p*.py')], key=lambda t: int(t[0]))
    for n, fn in files:
        print('Problem %s: ' % n, end='')
        execfile(fn)
        print()
