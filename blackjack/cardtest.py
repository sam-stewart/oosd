# unit testing for card class
import unittest
import card

class TestCardFunctions(unittest.TestCase):

    def setUp(self):
        self.validValues = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Ace', 'King', 'Queen', 'Jack']
        self.validSuits = { 1 :'Spades', 2 : 'Clubs', 3 : 'Hearts', 4 : 'Diamonds'}
        self.cardValue = 'Jack'
        self.cardSuit = 2
        self.card = card.Card(self.cardValue, self.cardSuit)

    def test_value(self):
        self.assertEqual(self.cardValue, self.card.get_value())
        self.assertIn(self.card.get_value(), self.validValues)

    def test_str(self):
        self.assertEqual((str(self.cardValue) + " of " + 
            self.validSuits[self.cardSuit]), str(self.card))

if __name__ == '__main__':
    unittest.main()
