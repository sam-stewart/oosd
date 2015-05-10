import xmltodict
import parser

class XmlParser(parser.Parser):

    @classmethod
    def parse(self, doc):
        return xmltodict.parse(doc, xml_attribs=True)
        


