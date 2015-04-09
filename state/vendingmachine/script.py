# Script for vending machine

import vendingmachine

vm = vendingmachine.VendingMachine()

money_input = raw_input("Enter how much money to insert: ")
vm.insert_money(float(money_input))

i = 0;

for product in vm.products:
    print "Index: " + str(i) + " " + product.name + " " + str(product.price)
    i += 1

selection = raw_input("Enter product index or c to cancel: ")

if selection == 'c':
    vm.cancel_transaction()

elif int(selection) < len(vm.products):
    vm.make_selection(selection)

else:
    print "Invalid selection"
    exit()

exit()

