class CoffeeMachine:
    def __init__(self, water, milk, coffee, disp, money):
        self.ml_water = water  # 400
        self.ml_milk = milk  # 540
        self.coffee_beans = coffee  # 120
        self.disp_cups = disp  # 9
        self.money = money   # 550
    def __repr__(self):
        return 'Water:{}ml Milk:{}ml\nCoffee Beans:{}g Disposable Cups:{} pc/s\nMoney:${}'.format(self.ml_water,
                                                                                                  self.ml_milk,
                                                                                                  self.coffee_beans,
                                                                                                  self.disp_cups,
                                                                                                  self.money)

    def __str__(self):
        return f"""\nThe coffee machine has:\n{self.ml_water} of water\n{self.ml_milk} of milk\
\n{self.coffee_beans} of coffee beans\n{self.disp_cups} of disposable cups\n${self.money} of money\n"""

    def buy(self) -> object:
        user_buy = input("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")
        if user_buy == '1':
            return CoffeeMachine.espresso(self)
        elif user_buy == '2':
            return CoffeeMachine.latte(self)
        elif user_buy == '3':
            return CoffeeMachine.cappuccino(self)
        elif user_buy == 'back':
            return CoffeeMachine.action(self)
        else:
            print("No such input found. Please enter again")
        return CoffeeMachine.buy(self)

    def fill(self):
        fill_water = int(input('\nHow much ml water?\n'))
        fill_milk = int(input('How much ml milk?\n'))
        fill_beans = int(input('How much grams of coffee beans?\n'))
        fill_cups = int(input('How many disposable cups?\n'))
        self.ml_water += fill_water
        self.ml_milk += fill_milk
        self.coffee_beans += fill_beans
        self.disp_cups += fill_cups
        print('')
        CoffeeMachine.action(self)

    def action(self) -> object:
        user_action = input("What do you want to do? -Buy- -Fill- -Take- -Remaining- -Exit-\n")
        while True:
            if user_action == 'Buy':
                CoffeeMachine.buy(self)
            elif user_action == "Fill":
                CoffeeMachine.fill(self)
            elif user_action == "Take":
                print(f'You get ${self.money}.\n')
                self.money -= self.money
                CoffeeMachine.action(self)
                break
            elif user_action == 'Remaining':
                print(CoffeeMachine.__str__(self))
                CoffeeMachine.action(self)
            elif user_action == 'Exit':
                exit()
            else:
                print("No such input. Restarting coffee machine.\n")
                CoffeeMachine.action(self)

    def latte(self):
        if self.ml_water - 350 >= 0 and self.ml_milk - 75 >= 0 and self.coffee_beans - 20 >= 0 and self.disp_cups - 1 >= 0:
            print('I have enough resources, making you a coffee!\n')
            self.ml_water -= 350
            self.ml_milk -= 75
            self.coffee_beans -= 20
            self.disp_cups -= 1
            self.money += 7
        elif self.ml_water - 350 < 0:
            print("Sorry, not enough water!\n")
        elif self.ml_milk - 75 < 0:
            print("Sorry, not enough milk!\n")
        elif self.coffee_beans - 20 < 0:
            print("Sorry,not enough coffee beans!\n")
        elif self.disp_cups - 1 < 0:
            print("Sorry, not enough disposable cups!\n")
        else:
            pass
        CoffeeMachine.action(self)

    def cappuccino(self):
        if self.ml_water - 200 >= 0 and self.ml_milk - 100 >= 0 and self.coffee_beans - 12 >= 0 and self.disp_cups - 1 >= 0:
            print('I have enough resources, making you a coffee!\n')
            self.ml_water -= 200
            self.ml_milk -= 100
            self.coffee_beans -= 12
            self.disp_cups -= 1
            self.money += 6
        elif self.ml_water - 200 < 0:
            print("Sorry, not enough water!\n")
        elif self.ml_milk - 100 < 0:
            print("Sorry, not enough milk!\n")
        elif self.coffee_beans - 12 < 0:
            print("Sorry,not enough coffee beans!\n")
        elif self.disp_cups - 1 < 0:
            print("Sorry, not enough disposable cups!\n")
        else:
            pass
        CoffeeMachine.action(self)

    def espresso(self):
        if self.ml_water - 250 >= 0 and self.ml_milk - 0 >= 0 and self.coffee_beans - 16 >= 0 and self.disp_cups - 1 >= 0:
            print('I have enough resources, making you a coffee!\n')
            self.ml_water -= 250
            self.ml_milk -= 0
            self.coffee_beans -= 16
            self.disp_cups -= 1
            self.money += 4
        elif self.ml_water - 250 < 0:
            print("Sorry, not enough water!\n")
        elif self.ml_milk - 0 < 0:
            print("Sorry, not enough milk!\n")
        elif self.coffee_beans - 16 < 0:
            print("Sorry,not enough coffee beans!\n")
        elif self.disp_cups - 1 < 0:
            print("Sorry, not enough disposable cups!\n")
        else:
            pass
        CoffeeMachine.action(self)


while True:
    start = CoffeeMachine(400, 540, 120, 9, 550)
    start.action()
