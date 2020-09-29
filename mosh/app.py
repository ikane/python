from ecommerce.shopping import sales
<<<<<<< HEAD
=======

from pathlib import Path
>>>>>>> 74eed78e5502ac8116527a5be5a4aab6ac1200f2

#import sales
import sys

# calc_shipping()

# sales.calc_tax()


print(sys.path)
# print(dir(sales))
# print(sales.__name__)
# print(sales.__package__)
# print(sales.__file__)

# path = Path("ecommerce/__init__.py")
# print(path.exists())

# path = path.with_suffix(".txt")
# print(path)

path = Path(r"D:\DEV\sources\python\mosh\ecommerce")
print(path.exists())
print(path.iterdir)

for p in path.iterdir():
    print(p)
