from dictfactory import DictFactory

if __name__ == "__main__":

    with open('student.json') as j:
        jsonstr = j.read()

    with open('student.xml') as x:
        xmlstr = x.read()

    print DictFactory.parse(xmlstr)
    print DictFactory.parse(jsonstr)

