from xmlparser import XmlParser
from jsonparser import JsonParser

# EFAP: "Easier to ask for forgiveness than permission"
# Sounds like something entirely different to me, but ok.

def getdictfromjson(doc):
    return JsonParser.parse(doc)

def getdictfromxml(doc):
    return XmlParser.parse(doc)


if __name__ == "__main__":
    jsonfile = open('student.json', 'r')
    xmlfile = open('student.xml', 'r')

    print JsonParser.parse(jsonfile)
    print XmlParser.parse(xmlfile)

