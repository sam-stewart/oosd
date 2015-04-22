import unittest
from labexercises import *

class TestExercises(unittest.TestCase):

    def setUp(self):
        self.c = 'c'
        self.st = """Never test drive Vin Diesel's car, Vin's car has at least
            26 gears. It is much too difficult"""

        # List, expected list and function for testing map functions. 
        self.l = [2, 4, 6, 7]
        self.e = [4, 8, 12, 14]
        self.f = lambda x : x * 2

    def test_mymap_loop(self):
        self.assertItemsEqual(mymap_recursive(self.f, self.l),
                self.e)

    def test_mymap_recursive(self):
        self.assertItemsEqual(mymap_recursive(self.f, self.l),
                self.e)

if __name__ == '__main__':
    unittest.main();
    
