import yaml

class YamlDocument:

    @staticmethod
    def dumps(dictionary):
        return yaml.dump(dictionary)
