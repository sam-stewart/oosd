import json
import parser
from collections import OrderedDict

class JsonParser(parser.Parser):

    @staticmethod
    def parse(doc):
        return json.loads(doc, object_pairs_hook=OrderedDict)
