from xmlparser import XmlParser
from jsonparser import JsonParser

# EFAP: "Easier to ask for forgiveness than permission"
# Sounds like something entirely different to me, but ok.
class DictFactory:

    @staticmethod
    def parse(doc):
        try:
            return JsonParser.parse(doc)
        except:
            pass #try xml

        try:
            return XmlParser.parse(doc)
        except:
            raise ValueError('Invalid input')

