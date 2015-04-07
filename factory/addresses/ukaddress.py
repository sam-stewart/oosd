from abstractpostaladdress import AbstractPostalAddress
import re

class UkAddress(AbstractPostalAddress):

    def __init__(self, recipient="", org="", building="", address="",
            locality="", city="", post_code=""):
        self.recipient = recipient
        self.organisation = org
        self.building = building
        self.address = address
        self.locality = locality
        self.city = city
        self.post_code = post_code

    @property
    def post_code(self):
        return self._post_code

    @post_code.setter
    def post_code(self, value):
        # highly simplified UK post code #### ###
        p = re.compile('^[A-Z0-9]{4}\s[A-Z0-9]{3}$')
        if p.match(value) != None:
            self._post_code = value
        else:
            raise ValueError("Post codes A-Z 0-9 in #### ### format")

    def print_address(self):
        self.address_string = self.recipient + "\n"
        if self.organisation != "":
            self.address_string += self.organisation + "\n"
        if self.building != "":
            self.address_string += self.building + "\n"
        self.address_string += self.address + "\n"
        if self.locality != "":
            self.address_string += self.address + "\n"
        self.address_string += self.city + "\n" + self.post_code
        print self.address_string

     
