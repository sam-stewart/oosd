import xmltodict
import parser

class XmlParser(parser.Parser):

    @staticmethod
    def parse(doc):
        return xmltodict.parse(doc, xml_attribs=True)
        


