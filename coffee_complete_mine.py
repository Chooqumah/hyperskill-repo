machine = {
    "water": 400,
    "milk": 540,
    "beans": 120,
    "money": 550,
    "cups": 9
}

ingredients = ['water', 'milk', 'beans']

MENU = {
    "1": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "beans": 18,
        },
        "cost": 1.50,
    },
    "2": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "beans": 24,
        },
        "cost": 2.50,
    },
    "3": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "beans": 24,
        },
        "cost": 3.00,
    }
}


def sufficient(cups, available):
    if cups == available:
        print("Yes, I can make that amount of coffee")
    elif cups > available:
        print(f"No, I can only make {available} cups of coffee")
    elif available > cups:
        print(f"Yes, I can make that amount of coffee (and even {available - cups} more than that)")


def report():
    print("The coffee machine has: ")
    print(f"{machine['water']} ml of water")
    print(f"{machine['milk']} ml of milk")
    print(f"{machine['beans']} g of coffee beans")
    print(f"{machine['cups']} disposable cups")
    print(f"${machine['money']} of money")
    print()


def make_espresso():
    machine['water'] -= 250
    machine['beans'] -= 16
    machine['money'] += 4
    machine['cups'] -= 1


def make_latte():
    machine['water'] -= 350
    machine['milk'] -= 75
    machine['beans'] -= 20
    machine['money'] += 7
    machine['cups'] -= 1


def make_cappuccino():
    machine['water'] -= 200
    machine['milk'] -= 100
    machine['beans'] -= 12
    machine['money'] += 6
    machine['cups'] -= 1


def is_resource_sufficient(choice):
    for item in ingredients:
        if machine[item] < MENU[choice]['ingredients'][item]:
            print(f"Sorry, not enough {item}!")
            return False
    print("I have enough resources, making you a coffee!")
    return True


def buy():
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: ")
    choice = input()
    if choice == "1":
        if is_resource_sufficient(choice):
            make_espresso()
    elif choice == "2":
        if is_resource_sufficient(choice):
            make_latte()
    elif choice == "3":
        if is_resource_sufficient(choice):

            make_cappuccino()


def fill():
    print("Write how many ml of water you want to add: ")
    water = int(input())
    machine['water'] += water
    print("Write how many ml of milk you want to add: ")
    milk = int(input())
    machine['milk'] += milk
    print("Write how many grams of coffee beans you want to add: ")
    beans = int(input())
    machine['beans'] += beans
    print("Write how many disposable cups you want to add: ")
    cups = int(input())
    machine['cups'] += cups


def main():
    while True:
        print("Write action (buy, fill, take, remaining, exit): ")
        action = input().lower()
        if action == "remaining":
            report()
        elif action == "buy":
            buy()
        elif action == "fill":
            fill()
        elif action == "take":
            print(f"I give you ${machine['money']}")
            machine['money'] = 0
        elif action == "exit":
            break


if __name__ == "__main__":
    main()
