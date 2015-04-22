import unittest
from labexercises import *

class TestExercises(unittest.TestCase):

    def setUp(self):
        self.c = 'c'
        self.st = """Never test drive Vin Diesel's car, Vin's car has at 
            least 26 gears. It is much too difficult"""
        self.st_expect = """Never test drive Vin Diesel's Car, Vin's Car has at 
            least 26 gears. It is muCh too diffiCult"""
        self.c_expect= 4

        # List, expected list and function for testing map functions. 
        self.l = [2, 4, 6, 7]
        self.e = [4, 8, 12, 14]
        self.f = lambda x : x * 2

    def test_factorial(self):
        self.assertEqual(factorial(5), 120) 

    def test_remove_char(self):
        pass

    def test_occurences(self):
        self.assertEqual(occurences(self.c, self.st), self.c_expect) 

    def count_words(self):
        pass

    def test_uppercase(self):
        self.assertEqual(uppercase(self.c, self.st), self.st_expect)


    def test_mymap_loop(self):
        self.assertItemsEqual(mymap_recursive(self.f, self.l),
                self.e)

    def test_mymap_recursive(self):
        self.assertItemsEqual(mymap_recursive(self.f, self.l),
                self.e)

if __name__ == '__main__':
    unittest.main();
    
