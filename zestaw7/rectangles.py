import unittest


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self == other

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    def cross(self, other):
        return self.x * other.y - self.y * other.x

    def length(self):
        return (self.x**2 + self.y**2)**0.5

    def __hash__(self):
        return hash((self.x, self.y))


class Rectangle:
    

    def __init__(self, x1, y1, x2, y2):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

        if x1 >= x2 or y1 >= y2:
            raise ValueError('Invalid coordinates')

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
    
    def intersection(self, other):
        x1 = max(self.pt1.x, other.pt1.x)
        y1 = max(self.pt1.y, other.pt1.y)
        x2 = min(self.pt2.x, other.pt2.x)
        y2 = min(self.pt2.y, other.pt2.y)

        if (x1 > x2 or y1 > y2):
            return None
        
        return Rectangle(x1, y1, x2, y2)

    def cover(self, other):
        x1 = min(self.pt1.x, other.pt1.x)
        y1 = min(self.pt1.y, other.pt1.y)
        x2 = max(self.pt2.x, other.pt2.x)
        y2 = max(self.pt2.y, other.pt2.y)

        return Rectangle(x1, y1, x2, y2)
    
    def make4(self):
        mid_x = self.center().x
        mid_y = self.center().y

        rect_A = Rectangle(self.pt1.x, self.pt1.y, mid_x, mid_y)
        rect_B = Rectangle(mid_x, self.pt1.y, self.pt2.x, mid_y)
        rect_C = Rectangle(mid_x, mid_y, self.pt2.x, self.pt2.y)
        rect_D = Rectangle(self.pt1.x, mid_y, mid_x, self.pt2.y)

        return rect_A, rect_B, rect_C, rect_D

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
        
    def test_no_intersection(self):
        rect1 = Rectangle(1, 2, 3, 4)
        rect2 = Rectangle(5, 6, 7, 8)
        intersect_rect = rect1.intersection(rect2)
        self.assertIsNone(intersect_rect)

    def test_cover(self):
        rect1 = Rectangle(1, 2, 3, 4)
        rect2 = Rectangle(5, 6, 7, 8)
        cover_rect = rect1.cover(rect2)
        self.assertEqual(cover_rect, Rectangle(1, 2, 7, 8))

    def test_make4(self):
        rect = Rectangle(1, 2, 7, 8)
        rects = rect.make4()
        expected_rects = [
            Rectangle(1, 2, 4, 5),
            Rectangle(4, 2, 7, 5),
            Rectangle(4, 5, 7, 8),
            Rectangle(1, 5, 4, 8),
        ]
        for i in range(4):
            self.assertEqual(rects[i], expected_rects[i])


if __name__ == "__main__":
    unittest.main()