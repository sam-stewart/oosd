import yamldocument
from yamldocument import YamlDocument
from jsondocument import JsonDocument
from xmldocument import XmlDocument

class DocumentFactory:

    @staticmethod
    def get_doc(doctype, dictionary):
        if doctype == 'yaml':
            return YamlDocument.dumps(dictionary)
        elif doctype == 'json':
            return JsonDocument.dumps(dictionary)
        elif doctype == 'xml':
            return XmlDocument.dumps(dictionary) 
    
