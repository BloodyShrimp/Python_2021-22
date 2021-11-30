from points import Point


class Rectangle:
    """Klasa reprezentująca prostokąty na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        # Chcemy, aby x1 < x2, y1 < y2.
        if(x1 < x2 and y1 < y2):
            self.pt1 = Point(x1, y1)
            self.pt2 = Point(x2, y2)
        else:
            raise ValueError("niepoprawne punkty")

    def __str__(self):        # "[(x1, y1), (x2, y2)]"
        return "[" + str(self.pt1) + ", " + str(self.pt2) + "]"

    def __repr__(self):        # "Rectangle(x1, y1, x2, y2)"
        return "Rectangle(" + str(self.pt1.x) + ", " + str(self.pt1.y) + ", " + str(self.pt2.x) + ", " + str(self.pt2.y) + ")"

    def __eq__(self, other):   # obsługa rect1 == rect2
        if(not isinstance(other, Rectangle)):
            raise ValueError("argument nie jest prostokatem")

        return self.pt1 == other.pt1 and self.pt2 == other.pt2

    def __ne__(self, other):        # obsługa rect1 != rect2
        if(not isinstance(other, Rectangle)):
            raise ValueError("argument nie jest prostokatem")

        return not self == other

    def center(self):          # zwraca środek prostokąta
        return Point((self.pt1.x + self.pt2.x) / 2, (self.pt1.y + self.pt2.y) / 2)

    def area(self):            # pole powierzchni
        return (self.pt2.x - self.pt1.x)*(self.pt2.y - self.pt1.y)

    def move(self, x, y):      # przesunięcie o (x, y)
        return Rectangle(self.pt1.x + x, self.pt1.y + y, self.pt2.x + x, self.pt2.y + y)

    def intersection(self, other):  # część wspólna prostokątów
        if(not isinstance(other, Rectangle)):
            raise ValueError("argument nie jest prostokatem")

        x1 = max(self.pt1.x, other.pt1.x)
        y1 = max(self.pt1.y, other.pt1.y)
        x2 = min(self.pt2.x, other.pt2.x)
        y2 = min(self.pt2.y, other.pt2.y)
        return Rectangle(x1, y1, x2, y2)


    def cover(self, other):    # prostąkąt nakrywający oba
        if(not isinstance(other, Rectangle)):
            raise ValueError("argument nie jest prostokatem")
            
        x1 = min(self.pt1.x, other.pt1.x)
        y1 = min(self.pt1.y, other.pt1.y)
        x2 = max(self.pt2.x, other.pt2.x)
        y2 = max(self.pt2.y, other.pt2.y)
        return Rectangle(x1, y1, x2, y2)

    def make4(self):           # zwraca krotkę czterech mniejszych
        x_half = (self.pt1.x + self.pt2.x) / 2.0
        y_half = (self.pt1.y + self.pt2.y) / 2.0
        R1 = Rectangle(self.pt1.x, self.pt1.y, x_half, y_half)
        R2 = Rectangle(x_half, self.pt1.y, self.pt2.x, y_half)
        R3 = Rectangle(self.pt1.x, y_half, x_half, self.pt2.y)
        R4 = Rectangle(x_half, y_half, self.pt2.x, self.pt2.y)
        return (R1, R2, R3, R4)