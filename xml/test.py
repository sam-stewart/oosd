import unittest
from script import getdictfromxml
from script import getdictfromjson

class TestDoc(unittest.TestCase):

    def setUp(self):
        self.jsonfile = open('student.json', 'r')
        self.xmlfile = open('student.xml', 'r')
        self.maxDiff = None

    def test_equal(self):
        self.xmldict = getdictfromxml(self.xmlfile)
        self.jsondict = getdictfromjson(self.jsonfile)
        self.assertDictEqual(self.xmldict, self.jsondict)

if __name__ == '__main__':
    unittest.main()
