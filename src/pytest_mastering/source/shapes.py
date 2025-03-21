import math


class Shape:

    def area(self):
        pass

    def perimeter(self):
        pass


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius **2
    
    def perimeter(self):
        return 2 * math.pi * self.radius
    


class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __eq__(self, value):
        if not isinstance(value, Rectangle):
            return False
        return self.width == value.width and self.length == value.length
    
    def area(self):
        return self.length * self.width
        
    def perimeter(self):
        return (self.length * 2)  + (2 * self.width)
    

class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)