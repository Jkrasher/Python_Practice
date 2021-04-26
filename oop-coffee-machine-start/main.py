from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# print(MoneyMachine.CURRENCY)
# print(MoneyMachine.COIN_VALUES)
# print(MoneyMachine.COIN_VALUES["quarters"])
# print(MoneyMachine.COIN_VALUES)

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

# coffee_report1 = CoffeeMaker()
# coffee_report2 = MoneyMachine()
# print(coffee_report1.report(), "\n", coffee_report2.report())
# (coffee_report1.report(), "\n", coffee_report2.report())

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f" what would you like? ({options})")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        is_enough_ingredients = coffee_maker.is_resource_sufficient(drink)
        is_payment_successful = money_machine.make_payment(drink.cost)
        if is_enough_ingredients and is_payment_successful:
            coffee_maker.make_coffee(drink)


