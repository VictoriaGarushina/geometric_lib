import unittest
from square import area, perimeter

class SquareTestCase(unittest.TestCase):
    def test_area(self):

        self.assertEqual(area(4), 16)
        
        self.assertEqual(area(0), 0)
        
        self.assertEqual(area(1000), 1000000)
        
        self.assertEqual(area(-3), 9)

    def test_perimeter(self):

        self.assertEqual(perimeter(3), 12)
        
        self.assertEqual(perimeter(0), 0)
        
        self.assertEqual(perimeter(1000), 4000)

        self.assertEqual(perimeter(-3), -12)