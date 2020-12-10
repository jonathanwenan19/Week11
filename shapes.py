class Shape:
    def __init__(self, filled: bool = True, color: str = 'Green'):
        self.filled = filled
        self.color = color

    def is_filled(self):
        fill = self.filled
        if fill is True:
            fill = 'Filled'
        elif fill is False:
            fill = 'Not Filled'
        return fill

    def get_color(self):
        return self.color

    def tostring(self):
        print(f'A shape with color {self.get_color()} and {self.is_filled()}')


class Circle(Shape):
    def __init__(self, radius : float= 1.0):
        self.radius = radius
        self.shape = Shape

    def get_radius(self):
        return self.radius

    def get_area(self):
        area = 3.14 * (self.radius**2)
        return area

    def get_perimeter(self):
        perimeter = 3.14*self.radius*2
        return perimeter

    def tostring(self):
        print(f'A circle with radius of {self.radius}unit, which is a subclass {self.shape.__name__} ')


class Rectangle(Shape):
    def __init__(self, height : float = 1.0, width : float = 1.0):
        self.height = height
        self.width = width
        self.shape = Shape

    def get_area(self):
        return self.height * self.width

    def get_perimeter(self):
        return 2*(self.height+self.width)

    def get_height(self):
        return self.height

    def get_width(self):
        return self.width

    def tostring(self):
        print(f'Rectangle with length of {self.height}, width of {self.width} and a subclass of {self.shape.__name__}')


class Square(Rectangle):
    def __init__(self, height:float, width:float):
        Rectangle.__init__(self, height, width)

    def tostring(self):
        print( f'A square with side {self.height} in subclass {Rectangle.__name__}')


if __name__ == '__main__':
    circle = Circle(10)
    circle.tostring()
    print(circle.get_area())
    print(circle.get_perimeter())
    rectangle = Rectangle()
    square = Square(10,10)
    square.tostring()
    print(square.get_perimeter())







