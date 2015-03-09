import unittest
import myset
import random

class TestMySet(unittest.TestCase):
    
    def setUp(self):
        # Create a list with duplicate values
        self.sample = [2, 4, 5, 6, 7, 8, 8, 2, 3, 4, 7]
        self.set_from_sample = [2, 3, 4, 5, 6, 7, 8]

        # Instantiate myset with the list of duplicate values
        self.test_set = myset.MySet(self.sample)

    def test_constructor(self):
        self.assertItemsEqual(self.test_set.my_set, self.set_from_sample)

    
    # add an item not already in set, test (51 guaranteed not to be in set)
    def test_add_item(self):
        self.test_set.add_item(10)
        self.assertTrue(self.test_set.has_item(10))

    def test_remove_item(self):
        self.test_set.remove_item(2)
        self.assertFalse(self.test_set.has_item(2))

    def test_is_empty(self):
        self.assertFalse(self.test_set.is_empty())

    def test_has_item(self):
        self.assertTrue(self.test_set.has_item(2))

    def test_intersection(self):
        self.intersect_set = [4, 9, 2, 5, 13]
        self.expected_set = [4, 2, 5]
        self.assertItemsEqual(self.test_set.intersection(self.intersect_set),
                self.expected_set)

    def test_union(self):
        self.union_set = [2, 3, 10, 12, 4]
        self.expected_set = [2, 3, 4, 5, 6, 7, 8, 10, 12]
        self.assertItemsEqual(self.test_set.union(self.union_set),
            self.expected_set)

    def test_subset_of(self):
        self.true_set = [2, 3, 4, 5, 6, 7, 8, 34, 34]
        self.false_set = [1, 2, 3]
        self.assertTrue(self.test_set.is_subset_of(self.true_set))
        self.assertFalse(self.test_set.is_subset_of(self.false_set))

    def test_equal_to(self):
        self.true_set = [2, 3, 4, 5, 6, 7, 8]
        self.false_set = [2, 3, 4, 5, 6, 7, 8, 9]
        self.assertTrue(self.test_set.is_equal_to(self.true_set))
        self.assertFalse(self.test_set.is_equal_to(self.false_set))

    def test_proper_subset(self): 
        self.true_set = [2, 3, 4, 5, 6, 7, 8, 9]
        self.false_set = [2, 3, 4, 5, 6, 7, 8]
        self.assertTrue(self.test_set.is_proper_subset_of(self.true_set))
        self.assertFalse(self.test_set.is_proper_subset_of(self.false_set))

if __name__ == '__main__':
    unittest.main()
