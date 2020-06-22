class CoffeeMachine:
    def __init__(self, ml_water, ml_milk, coffee_beans, disp_cups, money):
        self.ml_water = ml_water
        self.ml_milk = ml_milk
        self.coffee_beans = coffee_beans
        self.disp_cups = disp_cups
        self.money = money

    def __repr__(self):
        return 'Water:{}ml Milk:{}ml\nCoffee Beans:{}g Disposable Cups:{} pc/s\nMoney:${}'.format(self.ml_water, self.ml_milk, self.coffee_beans, self.disp_cups, self.money)
    def __str__(self):
        return '\nThe coffee machine has:\n{} of water\n{} of milk\n{} of coffee beans\n{} of disposable cups\n${} of money\n'.format(self.ml_water, self.ml_milk, self.coffee_beans, self.disp_cups, self.money)

    def take(self):
        print("I gave you ${}\n".format(self.money))
        self.money -= self.money
        user_input(input("Write action (buy, fill, take, remaining, exit):\n"))
    def buy(self, coffee):
    
        if coffee == '1':
            if self.ml_water - 250 >= 0 and self.ml_milk - 0 >= 0 and self.coffee_beans - 16 >= 0 and self.disp_cups - 1 >=0:
                print('I have enough resources, making you a coffee!\n')
                self.ml_water -= 250
                self.ml_milk -= 0
                self.coffee_beans -= 16
                self.disp_cups -= 1
                self.money += 4
                user_input(input("Write action (buy, fill, take, remaining, exit):\n"))
            elif self.ml_water - 250 < 0:
                print("Sorry, not enough water!\n")
                user_input(input("Write action (buy, fill, take, remaining, exit):\n"))
            elif self.ml_milk - 0 < 0:
                print("Sorry, not enough milk!\n")
                user_input(input("Write action (buy, fill, take, remaining, exit):\n"))
            elif self.coffee_beans - 16 < 0:
                print("Sorry,not enough coffee beans!\n")
                user_input(input("Write action (buy, fill, take, remaining, exit):\n"))
            elif self.disp_cups - 1 < 0:
                print("Sorry, not enough disposable cups!\n")
                user_input(input("Write action (buy, fill, take, remaining, exit):\n"))
            else:
                pass
                
                
        elif coffee == '2':            
            if self.ml_water - 350 >= 0 and self.ml_milk - 75 >= 0 and self.coffee_beans - 20 >= 0 and self.disp_cups - 1 >=0:
                print('I have enough resources, making you a coffee!\n')
                self.ml_water -= 350
                self.ml_milk -= 75
                self.coffee_beans -= 20
                self.disp_cups -= 1
                self.money += 7
                user_input(input("Write action (buy, fill, take, remaining, exit):\n"))
            elif self.ml_water - 350 < 0:
                print("Sorry, not enough water!\n")
                user_input(input("Write action (buy, fill, take, remaining, exit):\n"))
            elif self.ml_milk - 75 < 0:
                print("Sorry, not enough milk!\n")
                user_input(input("Write action (buy, fill, take, remaining, exit):\n"))
            elif self.coffee_beans - 20 < 0:
                print("Sorry,not enough coffee beans!\n")
                user_input(input("Write action (buy, fill, take, remaining, exit):\n"))
            elif self.disp_cups - 1 < 0:
                print("Sorry, not enough disposable cups!\n")
                user_input(input("Write action (buy, fill, take, remaining, exit):\n"))
            else:
                pass
        elif coffee == '3':
            if self.ml_water - 200 >= 0 and self.ml_milk - 100 >= 0 and self.coffee_beans - 12 >= 0 and self.disp_cups - 1 >=0:
                print('I have enough resources, making you a coffee!\n')
                self.ml_water -= 200
                self.ml_milk -= 100
                self.coffee_beans -= 12
                self.disp_cups -= 1
                self.money += 6
                user_input(input("Write action (buy, fill, take, remaining, exit):\n"))
            elif self.ml_water - 200 < 0:
                print("Sorry, not enough water!\n")
                user_input(input("Write action (buy, fill, take, remaining, exit):\n"))
            elif self.ml_milk - 100 < 0:
                print("Sorry, not enough milk!\n")
                user_input(input("Write action (buy, fill, take, remaining, exit):\n"))
            elif self.coffee_beans - 12 < 0:
                print("Sorry,not enough coffee beans!\n")
                user_input(input("Write action (buy, fill, take, remaining, exit):\n"))
            elif self.disp_cups - 1 < 0:
                print("Sorry, not enough disposable cups!\n")
                user_input(input("Write action (buy, fill, take, remaining, exit):\n"))
        elif coffee == "back":
            user_input(input("Write action (buy, fill, take, remaining, exit):\n"))
        else:
            print('No such option. Please restart the machine.')
            exit
    def fill(self):
        fill_w = int(input("\nWrite how many ml of water do you want to add:\n"))
        fill_m = int(input("Write how many ml of milk do you want to add:\n"))
        fill_c = int(input("Write how many grams of coffee beans do you want to add:\n"))
        fill_d = int(input("Write how many disposable cups of coffee do you want to add:\n"))
        self.ml_water = self.ml_water + fill_w
        self.ml_milk = self.ml_milk + fill_m
        self.coffee_beans = self.coffee_beans + fill_c
        self.disp_cups = self.disp_cups + fill_d
        user_input(input("\nWrite action (buy, fill, take, remaining, exit):\n"))
            
        
        

start = CoffeeMachine(400, 540 , 120, 9, 550)
def user_input(action = input("Write action (buy, fill, take, remaining, exit):\n")):
    if action == "buy":
        start.buy(input("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n"))
    elif action == "fill":
        start.fill()
    elif action == "take":
        start.take()
    elif action == "remaining":
        print(start)
        user_input(input("Write action (buy, fill, take, remaining, exit):\n"))
    elif action == "exit":
        exit
    else:
        print("Invalid input. Restart the machine again...")
        exit

user_input()
    

    
