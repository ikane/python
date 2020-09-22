# import sys
# from pkg.mod1 import foo
# from pkg import mod1

# print(sys.path)
# print(foo())

# print(mod1.foo())

#

# import pkg.sub_pkg1.mod1

# print(pkg.sub_pkg1.mod1.foo())

from pkg.sub_pkg1 import mod2

print(mod2.bar())
