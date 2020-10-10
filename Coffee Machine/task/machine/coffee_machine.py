# Write your code here
water = 400
milk = 540
beans = 120
cups = 9
money = 550


def main():
    while True:

        action = input("Write action (buy, fill, take, remaining, exit):\n")

        if action == "fill":
            fill()
        elif action == "buy":
            buy()
        elif action == "take":
            take()
        elif action == "remaining":
            state()
        elif action == "exit":
            break
        else:
            print("Wrong option")


def buy():
    coffee_type = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")
    if coffee_type == "back":
        return
    else:
        if int(coffee_type) == 1:
            espresso()
        elif int(coffee_type) == 2:
            latte()
        elif int(coffee_type) == 3:
            cappuccino()
        else:
            print("Wrong option")


def espresso():
    global water, beans, cups, money

    if water >= 250 and beans >= 16 and cups >= 1:
        water -= 250
        beans -= 16
        cups -= 1
        money += 4
    else:
        print('Sorry, not enough resources!')


def latte():
    global water, milk, beans, cups, money

    if water >= 350 and beans >= 20 and cups >= 1 and milk >= 75:
        water -= 350
        milk -= 75
        beans -= 20
        cups -= 1
        money += 7
    else:
        print('Sorry, not enough resources!')


def cappuccino():
    global water, milk, beans, cups, money

    if water >= 200 and beans >= 12 and cups >= 1 and milk >= 100:
        water -= 200
        milk -= 100
        beans -= 12
        cups -= 1
        money += 6
    else:
        print('Sorry, not enough resources!')


def fill():
    global water, milk, beans, cups, money
    amt_water = int(input("Write how many ml of water do you want to add:\n"))
    amt_milk = int(input("Write how many ml of milk do you want to add:\n"))
    amt_beans = int(input("Write how many grams of coffee beans do you want to add:\n"))
    amt_cups = int(input("Write how many disposable cups of coffee do you want to add:\n"))

    water += amt_water
    milk += amt_milk
    beans += amt_beans
    cups += amt_cups


def take():
    global money
    print("I gave you $", money)
    money = 0


def state():
    global water, milk, beans, cups, money
    print(f'''
        The coffee machine has:
        {water} of water
        {milk} of milk
        {beans} of coffee beans
        {cups} of disposable cups
        {money} of money
        '''
          )


main()
