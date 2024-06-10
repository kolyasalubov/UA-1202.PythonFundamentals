class Polygon():
    def __init__(self, a, b):
        self.a = a
        self.b = b


class Rectangle(Polygon):

    def square(self):
        return self.a * self.b


rectangle = Rectangle(12, 4)
print(f'The square of rectangle is {rectangle.square()} square meters')
