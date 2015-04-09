import vendingmachinestate
from product import Product

class VendingMachine(object):
    

    def __init__(self):
        self.money_input = 0.00
        self.state = vendingmachinestate.IdleState()

        self.products = [Product("Moro", 2.55),
                Product("Skittles", 3.00),
                Product("S&V Chips", 1.75)]

    def idle(self):
        self.state.idle()

    def insert_money(self, money):
        self.state.receive_money(self, money)

    def make_selection(self, selection):
        self.state.make_selection(self, selection)

    def cancel_transaction(self):
        self.state.cancel_transaction(self)

    def refund(self):
        self.state.refund(self)


    
