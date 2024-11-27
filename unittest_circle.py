import unittest
import math
from circle import area, perimeter

class CircleTestCase(unittest.TestCase):
    
    def test_area_positive_values(self):

        self.assertAlmostEqual(area(4), 50.26548245743669, places=2)
        self.assertAlmostEqual(area(5), 78.53981633974483, places=2)
        
    def test_area_zero_value(self):

        self.assertEqual(area(0), 0)
        
    def test_area_large_value(self):

        self.assertAlmostEqual(area(1000), math.pi * 1000 * 1000, places=2)
        
    def test_area_negative_value(self):
        
        self.assertAlmostEqual(area(-4), 50.26548245743669, places=2)
        
    def test_area_decimal_value(self):

        self.assertAlmostEqual(area(2.5), 19.634954084936208, places=2)

    def test_perimeter_positive_values(self):

        self.assertAlmostEqual(perimeter(3), 18.84955592153876, places=2)
        self.assertAlmostEqual(perimeter(5), 31.41592653589793, places=2)
        
    def test_perimeter_zero_value(self):

        self.assertEqual(perimeter(0), 0)
        
    def test_perimeter_large_value(self):

        self.assertAlmostEqual(perimeter(1000), 2 * math.pi * 1000, places=2)
        
    def test_perimeter_negative_value(self):
        
        self.assertAlmostEqual(perimeter(-3), -18.84955592153876, places=2)
        
    def test_perimeter_decimal_value(self):

        self.assertAlmostEqual(perimeter(2.5), 15.707963267948966, places=2)