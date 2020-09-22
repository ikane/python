# Path hack.
# from ..sub_pkg1 import mod1


import pkg.sub_pkg1.mod1
import sys
import os
sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('..'))

# from pkg.sub_pkg1.mod1 import foo


def baz():
    print('[mod3] baz()')


class Baz:
    pass


# pkg.sub_pkg1.mod1.foo()

print(sys.path)
