import json
import parser
from collections import OrderedDict

class JsonParser(parser.Parser):

    @classmethod
    def parse(self, doc):
        return json.load(doc, object_pairs_hook=OrderedDict)
