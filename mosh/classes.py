class Point:

    # defining class attribute - shared by all instances
    default_color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point({self.x}, {self.y})")


point = Point(1, 2)
point.draw()
print(point.x)
print(Point.default_color)
print(point.default_color)
