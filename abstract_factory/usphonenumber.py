from abstractphonenumber import AbstractPhoneNumber

class UsPhoneNumber(AbstractPhoneNumber):

    def __init__(self, area_code, prefix, number):
        self.area_code = area_code
        self.prefix = prefix
        self.number = number

    def print_number(self):
        print area_code + "=" + prefix + "=" + number

    @property
    def area_code(self):
        return self.__area_code

    @area_code.setter
    def area_code(self, area_code):
        if len(area_code) != 3:
            raise ValueError("Area code needs to be 3 digits long")
        self.__area_code = area_code

    @property
    def prefix(self):
        return self.__prefix

    @prefix.setter
    def prefix(self, prefix):
       if len(prefix) != 3:
           raise ValueError("Prefix needs to be 3 digits long")
       self.__prefix = prefix

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):
        if len(str(number)) != 4:
            raise ValueError("Number needs to be 4 digits long")
        self.__number = number
