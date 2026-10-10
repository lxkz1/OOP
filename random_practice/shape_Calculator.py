from abc import ABC, abstractmethod


class Shape(ABC):

    shape_count = 0

    def __init__(self, name, heights, base,diameter="",radius="",area="",perimeter=""):
        self.name = name
        self.heights = heights
        self.bases = base
        self.diameter = diameter
        self.radius = radius
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






