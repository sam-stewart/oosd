import usphonenumber
import ukphonenumber
import usaddress
import ukaddress

class AbstractContactFactory(object):

    def create_phone_number(self):
        raise NotImplementedError()

    def create_address(self):
        raise NotImplementedError()

class UkContactFactory(AbstractContactFactory):

    def create_phone_number(self, area_code, prefix, number):
        return ukphonenumber.UkPhoneNumber(area_code, prefix, number)

    def create_address(self, recipient, org, building, address, 
            locality, city, post_code):
        return ukaddress.UkAddress(recipient, org, building, address,
                locality, city, post_code)

class UsContactFactory(AbstractContactFactory):
    
    def create_phone_number(self, area_code, prefix, number):
        return usphonenumber.UsPhoneNumber(area_code, prefix, number)

    def create_address(self):
        pass
