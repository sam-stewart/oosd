import json

class JsonDocument:

    @staticmethod
    def dumps(dictionary):
        return json.dumps(dictionary)
