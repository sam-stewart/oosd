class VendingMachineState(object):

    def idle(self):
        pass
   
    def receive_money(self, vm, money):
        pass

    def make_selection(self, vm, money):
        pass

    def cancel_transaction(self, vm):
        pass

    def refund(self, vm):
        pass

    def change_state(self, vm, state):
        vm.state = state

class IdleState(VendingMachineState):
    
    def receive_money(self, vm, money):
        self.change_state(vm, MoneyReceivedState())
        vm.state.receive_money(vm, money)

class MoneyReceivedState(VendingMachineState):
    
    def receive_money(self, vm, money):
        vm.money_input += money

    def make_selection(self, vm, selection):
        self.change_state(vm, SelectionState())
        vm.make_selection(selection)

    def cancel_transaction(self, vm):
        self.change_state(vm, RefundState())
        vm.refund()

class SelectionState(VendingMachineState):

    def make_selection(self, vm, selection):
        self.product = vm.products[int(selection)]
        if vm.money_input >= self.product.price:
            vm.money_input -= self.product.price
            print "Product has been vended"
        else:
            print "Insufficient funds"

        self.change_state(vm, RefundState())
        vm.refund()

class RefundState(VendingMachineState):

    def refund(self, vm):
        print "Refunded: " + str(vm.money_input)
