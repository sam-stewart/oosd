from abstractphonenumber import AbstractPhoneNumber

class UkPhoneNumber(AbstractPhoneNumber):

    def __init__(self, area_code, prefix="", number=""):
        self.area_code = area_code
        self.prefix = prefix
        self.number = number

    def print_number(self):
        if self.prefix == None:
            print "(" + self.area_code + ") " + self.number
        else:
            print "(" + self.area_code + ") " + self.prefix + " " + self.number

    @property
    def area_code(self):
        return self._area_code

    @area_code.setter
    def area_code(self, area_code):
        if len(area_code) < 3 or len(area_code) > 6:
            raise ValueError("Area code needs to be between 3 and 6 digits")
        self._area_code = area_code

    @property
    def prefix(self):
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
       if prefix != "":
           if len(prefix) < 3 or len(prefix) > 4:
               raise ValueError("Provided prefix needs to be 3 or 4 digits long")
       self._prefix = prefix

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, number):
        self.num_min_length = 10 - (len(self.area_code) + len(self.prefix))
        self.num_max_length = self.num_min_length + 1

        if len(number) < self.num_min_length or len(number) > self.num_max_length:
            raise ValueError("Number needs to be between " + str(self.num_min_length) +
                " and " + str(self.num_max_length) + " digits long")
        self._number = number
