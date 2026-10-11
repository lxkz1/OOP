from abc import ABC, abstractmethod
import math


class Shape(ABC):

    shape_count = 0

    def __init__(self, name, area="",perimeter="",):
        self.name = name
        self.area = area 
        self.perimeter = perimeter
        Shape.shape_count += 1

    def describe(self):
        print(f"The {self.name} has {self.perimeter} meters of perimeter and {self.area} m² of area")

    @abstractmethod
    def calculation_of_area(self):
        pass

    @abstractmethod
    def calculation_of_perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, name, area = "" , perimeter = "" ,radius = 0 , diameter = 0):
        super().__init__(name, area, perimeter)
        self.radius = radius
        self.diameter = diameter


    def get_radius(self):
        radiusss = float(self.diameter) / 2
        return radiusss

    def calculation_of_area(self):
        if self.radius == 0 and self.diameter != 0:
            radius = self.get_radius()
            area = math.pi * (float(radius) ** 2)
        else:
            area = math.pi * (float(self.radius) **2)
        self.area = area 

    def calculation_of_perimeter(self):
        if self.diameter == 0:
            perimeter = 2 *(math.pi * float(self.radius))
        else:
            perimeter = math.pi * float(self.diameter)
        self.perimeter = perimeter

class Rectangle(Shape):
    def __init__(self, name, area = "", perimeter= "",base = 0, heights = 0):
        super().__init__(name, area, perimeter)
        self.bases = base
        self.heights = heights
    
    def calculation_of_area(self):
        area = float(self.bases) * float(self.heights)
        self.area = area 

    def calculation_of_perimeter(self):
        perimeter = 2 * (float(self.bases) + float(self.heights))
        self.perimeter = perimeter

class Square(Shape):
    def __init__(self, name, area="", perimeter="",side = 0):
        super().__init__(name, area, perimeter)
        self.side = side

    def calculation_of_area(self):
        area = float(self.side) ** 2
        self.area = area

    def calculation_of_perimeter(self):
        perimeter = float(self.side) * 4
        self.perimeter = perimeter

circle1 = Circle("circle", radius=2)
circle2 = Circle("big circle", diameter=10)
rectangle = Rectangle("rectangle", heights=3, base=4)
square = Square("square", side=5)

shapes = [circle1, circle2, rectangle, square]

for s in shapes:
    s.calculation_of_area()
    s.calculation_of_perimeter()
    s.describe()

print("Shapes created: ", Shape.shape_count)
