from abc import ABC, abstractmethod

from numpy import shape


class Shape(ABC):

    shape_count = 0

    def __init__(self, name, heights="", base="",diameter="",radius="",area="",perimeter="",side=""):
        self.name = name
        self.heights = heights
        self.bases = base
        self.diameter = diameter
        self.radius = radius
        self.area = area 
        self.perimeter = perimeter
        self.side = side
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
    def radiu(self):
        radiusss = float(self.diameter) / 2
        return radiusss

    def calculation_of_area(self):
        if self.radius == "":
            radius = self.radiu()
            area = 3.14 * (float(radius) ** 2)
        else:
            area = 3.14 * (float(self.radius) **2)
        self.area = area 

    def calculation_of_perimeter(self):
        if self.diameter == "":
            perimeter = 2 *(3.14 * float(self.radius))
        else:
            perimeter = 3.14 * float(self.diameter)
        self.perimeter = perimeter

class Rectangle(Shape):
    
    def calculation_of_area(self):
        area = float(self.bases) * float(self.heights)
        self.area = area 

    def calculation_of_perimeter(self):
        perimeter = 2 * (float(self.bases) + float(self.heights))
        self.perimeter = perimeter

class Square(Shape):

    def calculation_of_area(self):
        area = float(self.side) ** 2
        self.area = area

    def calculation_of_perimeter(self):
        perimeter = float(self.side) * 4
        self.perimeter = perimeter


# ---------------- TESTS ----------------
circle1 = Circle("circle", radius=2)
circle2 = Circle("big circle", diameter=10)
rectangle = Rectangle("rectangle", heights=3, base=4)
square = Square("square", side=5)

shapes = [circle1, circle2, rectangle, square]

for s in shapes:
    s.calculation_of_area()
    s.calculation_of_perimeter()
    s.describe()

print("Shapes created:", Shape.shape_count)
