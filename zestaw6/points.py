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


class TestPoint(unittest.TestCase):
    def test_str(self):
        self.assertEqual(str(Point(1, 2)), "(1, 2)")

    def test_repr(self):
        self.assertEqual(repr(Point(1, 2)), "Point(1, 2)")

    def test_eq(self):
        self.assertTrue(Point(1, 2) == Point(1, 2))
        self.assertFalse(Point(1, 2) == Point(3, 4))

    def test_ne(self):
        self.assertTrue(Point(1, 2) - Point(1, 2) != Point(1, 2))
        self.assertFalse(Point(3, 4) != Point(1,2) + Point(2,2))

    def test_add(self):
        self.assertEqual(Point(1, 2) + Point(3, 4), Point(4, 6))

    def test_sub(self):
        self.assertEqual(Point(3, 4) - Point(1, 2), Point(2, 2))

    def test_mul(self):
        self.assertEqual(Point(1, 2) * Point(3, 4), 11)

    def test_cross(self):
        self.assertEqual(Point(1, 2).cross(Point(3, 4)), -2)

    def test_length(self):
        self.assertEqual(Point(3, 4).length(), 5)

if __name__ == "__main__":
    unittest.main()