import re
import math

regex_v_n = r"^([a-zA-Z]{1,})=([+-]?)([0-9]*)$"  # regex to match assigned values
regex_v_v = r"([a-zA-Z]{1,})=([a-zA-Z]{1,})$"
regex_wrong = r"([a-zA-Z]{1,})=([a-zA-Z0-9]*)$"
regex_wrong_v = r"([a-zA-Z]{1,})([0-9]{1,})([a-zA-Z0-9]*)$"
regex_wrong_c = r"^(/)([a-zA-Z]{1,})$"
reg_slash = r"^([a-zA-Z0-9]{1,})([/]{2,})([a-zA-Z0-9]{1,})$"
variables = {}  # store values here
operation = []
temp = []  # to update the dict and prevent error


def abstraction(check):
    if re.match(regex_v_n, ''.join(check)):
        equal_sign_index = ''.join(check).index('=')
        variables.update([(''.join(check)[0:equal_sign_index], ''.join(check)[equal_sign_index + 1::])])
        #print(variables)
    elif re.match(regex_v_v, ''.join(check)):
        equal_sign_index = ''.join(check).index('=')
        # print(''.join(check)[0], ''.join(check)[2::])
        if ''.join(check)[equal_sign_index + 1::] in variables:
            for key, values in variables.items():
                # print(key)
                if key == ''.join(check)[equal_sign_index + 1::]:
                    temp.append((''.join(check)[0:equal_sign_index], values))
            variables.update(temp)
            #print(variables)
        else:
            # print(variables)
            print("Unknown variable")
    elif re.match(regex_wrong, ''.join(check)):
        print("Invalid identifier")
    else:
        print("Invalid assignment")


class Calculator:
    def __init__(self, argument):
        self.arg = argument
        self.temp = ''

    def calculate(self):

        if '=' not in self.arg:
            for key, value in variables.items():
                for steer in self.arg:
                    if key == steer:
                        self.arg = self.arg.replace(key, value)
                    #print(self.arg)
            try:
                if not re.match(reg_slash, ''.join(self.arg).replace(' ', '')):
                    #print(''.join(self.arg).replace(' ', ''))
                    print(math.trunc(eval(''.join(self.arg))))
                else:
                    print("Invalid expression")
            except SyntaxError:
                print("Invalid expression")
            except NameError:
                if re.match(regex_wrong_v, ''.join(self.arg)):
                    print("Invalid identifier")
                elif self.arg in variables:
                    print(variables[self.arg])
                else:
                    print("Unknown variable")
        else:
            if '=' in self.arg and self.arg.count('=') == 1:
                try:
                    # print(self.arg.split())
                    self.arg.replace(' ', '')
                    abstraction(self.arg.split())
                except IndexError:
                    abstraction(self.arg)
            else:
                print("Invalid assignment")


def main():
    user_input = ''
    while '/exit' not in user_input:
        user_input = input()
        if user_input == '/help':
            print("A simple calculator that has code so long, you'll wonder if you can read it <3")
        elif user_input == '':
            pass
        elif user_input != '/exit' and user_input != '/help':
            if not re.match(regex_wrong_c, user_input):
                calc = Calculator(user_input)
                calc.calculate()
            else:
                print("Unknown command")
        #else:
            #calc = Calculator(user_input)
            #calc.calculate()

    print("Bye!")


if __name__ == '__main__':
    main()
