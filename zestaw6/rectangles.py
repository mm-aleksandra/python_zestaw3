import unittest
from points import Point


class Rectangle:
    

    def __init__(self, x1, y1, x2, y2):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):
        return f"[({self.pt1.x}, {self.pt1.y}), ({self.pt2.x}, {self.pt2.y})]"

    def __repr__(self):
        return f"Rectangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y})"

    def __eq__(self, other):
        return self.pt1 == other.pt1 and self.pt2 == other.pt2

    def __ne__(self, other):
        return not self == other

    def center(self):
        return Point((self.pt1.x + self.pt2.x) / 2, (self.pt1.y + self.pt2.y) / 2)

    def area(self):
        width = abs(self.pt1.x - self.pt2.x)
        height = abs(self.pt1.y - self.pt2.y)
        return width * height

    def move(self, x, y):
        self.pt1.x += x
        self.pt1.y += y
        self.pt2.x += x
        self.pt2.y += y
        return self


class TestRectangle(unittest.TestCase):
    def test_str(self):
        self.assertEqual(str(Rectangle(1, 2, 3, 4)), "[(1, 2), (3, 4)]")

    def test_repr(self):
        self.assertEqual(repr(Rectangle(1, 2, 3, 4)), "Rectangle(1, 2, 3, 4)")

    def test_eq(self):
        self.assertEqual(Rectangle(1, 2, 3, 4), Rectangle(1, 2, 3, 4))
        self.assertNotEqual(Rectangle(1, 2, 3, 4), Rectangle(3, 4, 5, 6))

    def test_ne(self):
        self.assertEqual(Rectangle(1, 2, 3, 4), Rectangle(1, 2, 3, 4))
        self.assertEqual(Rectangle(1, 2, 3, 4), Rectangle(3, 4, 5, 6).move(-2,-2))

    def test_center(self):
        self.assertEqual(Rectangle(1, 2, 3, 4).center(), Point(2, 3))
        self.assertEqual(Rectangle(-2, 2, 0, 8).center(), Point(-1, 5))

    def test_area(self):
        self.assertEqual(Rectangle(1, 2, 4, 6).area(), 12)

    def test_move(self):
        self.assertEqual(Rectangle(1, 2, 3, 4).move(1,1), Rectangle(2, 3, 4, 5))
        self.assertEqual(Rectangle(-2, 2, 0, 8).move(-1,0), Rectangle(-3, 2, -1, 8))
        


if __name__ == "__main__":
    unittest.main()