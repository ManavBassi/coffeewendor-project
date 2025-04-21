from money_machine1 import MoneyMachine
from coffeemaker1 import CoffeeMaker
from menu1 import Menu,MenuItem

menu=Menu()
machine=CoffeeMaker()
profit=MoneyMachine()

def coffee():
    choice=""
    while not choice =='off':
        choice =input("what would you like?"+ menu.get_items())
        if choice=='off':
            return 
        elif choice == 'report':
            machine.report()
            profit.report()
        else:
            chosen_drink=menu.find_drinks(choice)
            if machine.is_resources_sufficient(chosen_drink):
                if profit.make_payment(chosen_drink.cost):
                    machine.make_coffee(chosen_drink)
coffee()
      