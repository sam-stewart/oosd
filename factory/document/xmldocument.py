
class XmlDocument:

    @staticmethod
    def dumps(dictionary):
        ret_string = ""
        for key, value in dictionary.iteritems():
            ret_string += "<" + key + ">"

            if isinstance(value, list):
                pass 
            elif isinstance(value, dict):
                pass
            else:
                ret_string += value + "</" + key + ">"

        return ret_string
