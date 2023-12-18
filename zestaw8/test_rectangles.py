import pytest
from rectangles import Point, Rectangle

@pytest.fixture
def sample_rectangle():
    return Rectangle(1, 2, 4, 6)

def test_rectangle_from_points():
    rectangle = Rectangle.from_points([(1, 2), (4, 6)])
    assert rectangle == Rectangle(1, 2, 4, 6)

def test_rectangle_top(sample_rectangle):
    assert sample_rectangle.top == 6

def test_rectangle_left(sample_rectangle):
    assert sample_rectangle.left == 1

def test_rectangle_bottom(sample_rectangle):
    assert sample_rectangle.bottom == 2

def test_rectangle_right(sample_rectangle):
    assert sample_rectangle.right == 4

def test_rectangle_width(sample_rectangle):
    assert sample_rectangle.width == 3

def test_rectangle_height(sample_rectangle):
    assert sample_rectangle.height == 4

def test_rectangle_topleft(sample_rectangle):
    assert sample_rectangle.topleft == Point(1, 6)

def test_rectangle_bottomleft(sample_rectangle):
    assert sample_rectangle.bottomleft == Point(1, 2)

def test_rectangle_topright(sample_rectangle):
    assert sample_rectangle.topright == Point(4, 6)

def test_rectangle_bottomright(sample_rectangle):
    assert sample_rectangle.bottomright == Point(4, 2)

def test_rectangle_str_representation(sample_rectangle):
    assert str(sample_rectangle) == "[(1, 2), (4, 6)]"

def test_rectangle_repr(sample_rectangle):
    assert repr(sample_rectangle) == "Rectangle(1, 2, 4, 6)"

def test_rectangle_equality(sample_rectangle):
    same_rectangle = Rectangle(1, 2, 4, 6)
    different_rectangle = Rectangle(0, 1, 3, 5)

    assert sample_rectangle == same_rectangle
    assert sample_rectangle != different_rectangle

def test_rectangle_center(sample_rectangle):
    assert sample_rectangle.center() == Point(2.5, 4.0)

def test_rectangle_area(sample_rectangle):
    assert sample_rectangle.area() == 12

def test_rectangle_move(sample_rectangle):
    moved_rectangle = sample_rectangle.move(1, -1)
    assert moved_rectangle == Rectangle(2, 1, 5, 5)

def test_rectangle_intersection(sample_rectangle):
    overlapping_rectangle = Rectangle(3, 4, 6, 8)
    non_overlapping_rectangle = Rectangle(10, 12, 14, 16)

    intersection = sample_rectangle.intersection(overlapping_rectangle)
    assert intersection == Rectangle(3, 4, 4, 6)

    no_intersection = sample_rectangle.intersection(non_overlapping_rectangle)
    assert no_intersection is None

def test_rectangle_cover(sample_rectangle):
    other_rectangle = Rectangle(0, 1, 5, 7)
    covered_rectangle = sample_rectangle.cover(other_rectangle)
    assert covered_rectangle == Rectangle(0, 1, 5, 7)

def test_rectangle_make4(sample_rectangle):
    rect_A, rect_B, rect_C, rect_D = sample_rectangle.make4()
    assert rect_A == Rectangle(1, 2, 2.5, 4.0)
    assert rect_B == Rectangle(2.5, 2, 4, 4.0)
    assert rect_C == Rectangle(2.5, 4.0, 4, 6)
    assert rect_D == Rectangle(1, 4.0, 2.5, 6)

if __name__ == "__main__":
    pytest.main()