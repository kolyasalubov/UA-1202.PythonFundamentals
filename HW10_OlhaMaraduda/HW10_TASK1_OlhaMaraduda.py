# HW10_TASK1: 
# Create a polygon class and a rectangle class that inherits from the polygon class and finds the square of a rectangle

class Polygon:
    def __init__(self, length, width):
        self.length = length
        self.width = width

class Rectangle(Polygon):
    def __init__(self, length, width):
        super().__init__(length, width)
    
    def rectangle_square(self):
        area = self.length * self.width
        return f"Square of a rectangle is {area}"
    
rect = Rectangle(7, 10)
print(rect.rectangle_square()) 