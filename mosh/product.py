class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Invalid price!")
        self.__price = value


p = Product(50)
p.price = -12
print(p.price)
