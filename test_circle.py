"""Unit tests of the Circle class using unittest or pytest (your choice).

Write unit tests as described in README.md.

1. Unit test for add_area using typical values.
2. Unit test for add_area for an "edge case" where one circle has radius 0.
3. Unit test that circle constructor raises exception of radius is negative.

"""
from circle import Circle
import unittest
from math import pi


class CircleTest(unittest.TestCase):

    def setUp(self):
        self.c1 = Circle(3)
        self.c2 = Circle(4)
        self.assertEqual(3, self.c1.get_radius())
        self.assertEqual(4, self.c2.get_radius())

    def test_add_area_positive(self):
        """ test adding two circles with positive radius"""
        result_circle = self.c1.add_area(self.c2)
        self.assertEqual(5, result_circle.get_radius())
        # each circle knows its own area
        expected = self.c1.get_area() + self.c2.get_area()
        self.assertAlmostEqual(expected, result_circle.get_area(), delta=1.0e-8)

    def test_add_area_zero(self):
        """ test adding two circles when one has a radius of zero"""
        c3 = Circle(0)
        result_circle = c3.add_area(self.c1)
        self.assertEqual( self.c1.get_radius(), result_circle.get_radius())
        self.assertEqual(self.c1.get_area(), result_circle.get_area())

    def test_r_is_not_negative(self):
        """ test if radius is not negative """
        with self.assertRaises(ValueError):
            Circle(-1)
            Circle(-5)
            Circle(-10)


