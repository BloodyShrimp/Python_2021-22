from points import Point
import math

class Circle:
    """Klasa reprezentująca okręgi na płaszczyźnie."""

    def __init__(self, x, y, radius):
        if radius < 0:
            raise ValueError("promień ujemny")
        self.pt = Point(x, y)
        self.radius = radius

    def __repr__(self):       # "Circle(x, y, radius)"
        return "Circle(" + str(self.pt.x) + ", " + str(self.pt.y) + ", " + str(self.radius) + ")"

    def __eq__(self, other):
        if(not isinstance(other, Circle)):
            raise ValueError("argument nie jest okregiem")
            
        return self.pt == other.pt and self.radius == other.radius

    def __ne__(self, other):
        if(not isinstance(other, Circle)):
            raise ValueError("argument nie jest okregiem")

        return not self == other

    def area(self):           # pole powierzchni
        return math.pi * (self.radius ** 2)

    def move(self, x, y):     # przesuniecie o (x, y)
        return Circle(self.pt.x + x, self.pt.y + y, self.radius)

    def cover(self, other):   # najmniejszy okrąg pokrywający oba
        if(not isinstance(other, Circle)):
            raise ValueError("argument nie jest okregiem")

        circle1 = self # mniejszy okrag
        circle2 = other # wiekszy okrag
        if (circle1.area() > circle2.area()): # jesli na odwrot to odwracamy
            circle1, circle2 = circle2, circle1

        distance = math.sqrt((circle1.pt.x - circle2.pt.x) ** 2 + (circle1.pt.y - circle2.pt.y) ** 2)

        if((distance + circle1.radius) <= circle2.radius):
            return circle2
        else:
            radius = (distance + circle1.radius + circle2.radius) / 2.0
            x_center = circle1.pt.x + (radius - circle1.radius) * (circle2.pt.x - circle1.pt.x) / distance
            y_center = circle1.pt.y + (radius - circle1.radius) * (circle2.pt.y - circle1.pt.y) / distance
            return Circle(x_center, y_center, radius)


