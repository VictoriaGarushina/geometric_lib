import unittest
from rectangle import area, perimeter

class RectangleTestCase(unittest.TestCase):
    
    def test_area_positive_values(self):

        self.assertEqual(area(4, 3), 12)
        self.assertEqual(area(5, 7), 35)
        
    def test_area_zero_values(self):

        self.assertEqual(area(0, 5), 0)
        self.assertEqual(area(5, 0), 0)
        self.assertEqual(area(0, 0), 0)
        
    def test_area_large_values(self):

        self.assertEqual(area(1000, 1000), 1000000)
        self.assertEqual(area(100000, 2), 200000)
        
    def test_area_negative_values(self):

        self.assertEqual(area(-4, 3), -12)
        self.assertEqual(area(4, -3), -12)
        self.assertEqual(area(-4, -3), 12)
        
    def test_area_decimal_values(self):

        self.assertAlmostEqual(area(2.5, 4.2), 10.5)
        self.assertAlmostEqual(area(5.5, 5.5), 30.25)

    def test_perimeter_positive_values(self):

        self.assertEqual(perimeter(3, 2), 10)
        self.assertEqual(perimeter(7, 5), 24)
        
    def test_perimeter_zero_values(self):

        self.assertEqual(perimeter(0, 5), 10)
        self.assertEqual(perimeter(5, 0), 10)
        self.assertEqual(perimeter(0, 0), 0)
        
    def test_perimeter_large_values(self):

        self.assertEqual(perimeter(1000, 1000), 4000)
        self.assertEqual(perimeter(100000, 200000), 600000)
        
    def test_perimeter_negative_values(self):

        self.assertEqual(perimeter(-4, 3), -2)
        self.assertEqual(perimeter(4, -3), 2)
        self.assertEqual(perimeter(-4, -3), -14)
        
    def test_perimeter_decimal_values(self):

        self.assertAlmostEqual(perimeter(2.5, 4.2), 13.4)
        self.assertAlmostEqual(perimeter(5.5, 5.5), 22)