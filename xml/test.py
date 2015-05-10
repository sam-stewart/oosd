import unittest
from dictfactory import DictFactory

class TestDoc(unittest.TestCase):

    def setUp(self):
        with open('student.json') as j:
            self.jsonstr = j.read()

        with open('student.xml') as x:
            self.xmlstr = x.read()

    def test_equal(self):
        self.xmldict = DictFactory.parse(self.xmlstr)
        self.jsondict = DictFactory.parse(self.jsonstr)
        self.assertDictEqual(self.xmldict, self.jsondict)

if __name__ == '__main__':
    unittest.main()
