from abstractpostaladdress import AbstractPostalAddress
import re

class UsAddress(AbstractPostalAddress):

    def __init__(self, recipient, org="", address1="", address2="",
            city="", state="", post_code=""):
        self.recipient = recipient
        self.organisation = org
        self.address1 = address1
        self.address2 = address2
        self.city = city
        self.state = state
        self.post_code = post_code
    
    @property
    def state(self):
        return _state

    @state.setter
    def state(self, value):
        p = re.compile('^[A-Z]{2}$')
        if p.match(value) != None:
            _state = value
        else:
            raise ValueError('State must be abbreviated two letter eg.) CA')

    @property
    def post_code(self):
        return _post_code

    @post_code.setter
    def post_code(self, value):
        p = re.compile('^[0-9]{9}$')
        if p.match(value) != None:
            _post_code = value
        else:
            raise ValueError("Post codes need to be 9 digits long")

