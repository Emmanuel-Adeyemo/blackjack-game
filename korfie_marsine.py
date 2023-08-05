
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# TODO: 1. Prompt user by asking what would you like. Prompt should show again to serve next customer.
# TODO: 2. Turn off machine for maintainers by entering 'off'.
# TODO: 3. Print report.
# TODO: 4. Check resources sufficient.
# TODO: 5. Process coins. Quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01. Calc value of coins
#  inserted.
# TODO: 6. Check successful transaction. Reject if not sufficient.
# TODO: 7. MAke coffee. Add money as profit

def coffee_machine(resources):
    MONEY = 0
    resources["Money"] = MONEY
    coffee = True
    while coffee:

        choice = input("  What would you like? (espresso/latte/cappuccino: ")

        # off button for maintenance. The only time coffee machine is off.
        if choice == "off":
            break


        def choice_is_report():
            for key in resources:
                if key == "water" or key == "milk":
                    print(f"{key.title()}: {resources[key]}ml")
                elif key == "coffee":
                    print(f"{key.title()}: {resources[key]}g")
                else:
                    print(f"Money: ${resources[key]}")
            return resources


        def choice_is_drink():
            drink = MENU[choice]
            return drink


        process_money = True
        while process_money:
            if choice == "report":
                resources = choice_is_report()
                break
            else:
                drink_type = choice_is_drink()
                pass


            def make_coffee(drink_type, resources):
                """ make coffee, called later in the money sufficient function if everything is good """
                drink_ingredients = drink_type["ingredients"]
                for key in drink_ingredients:
                    resources[key] = resources[key] - drink_ingredients[key]
                resources["Money"] += drink_type["cost"]
                print(f"Here's your {choice} ☕ Enjoy!")

            def money_sufficient(drink_type):
                """ prompts user to insert coins, process money, and provides feedback. Also calls the make_coffee
                function """
                print("Please insert coins.")
                quarters = int(input("How many quarters?: "))
                dimes = int(input("How many dimes?: "))
                nickles = int(input("How many nickles?: "))
                pennies = int(input("How many pennies? "))

                total_inserted = 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies
                cost_of_drink = drink_type["cost"]

                if cost_of_drink > total_inserted:
                    print("Sorry, that's not enough money. Money refunded.")
                    return
                else:
                    if total_inserted > cost_of_drink:
                        change = total_inserted - cost_of_drink
                        change = "{:.2f}".format(change)
                        print(f"Here is ${change} in change.")
                        # call the make_coffee function if everything is good
                        make_coffee(drink_type, resources)
                    else:
                        print("No change")
                        # call the make_coffee function if everything is good
                        make_coffee(drink_type, resources)


            def check_resources(drink_type, resources):
                """checks if there are enough resources to make that type of drink"""
                drink_ingredients = drink_type["ingredients"]
                for key in drink_ingredients:
                    if resources[key] > drink_ingredients[key]:
                        money_sufficient(drink_type)
                        break
                    else:
                        print(f"Sorry, there's not enough {key}.")
                        return


            check_resources(drink_type, resources)

            process_money = False

coffee_machine(resources)
