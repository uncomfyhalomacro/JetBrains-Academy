import random
import sqlite3
from sqlite3 import Error


class BankingSys:
    balance: int
    accounts: list
    num: int

    def __init__(self, deposit=0):
        self.accounts = []
        self.balance = deposit
        self.num = 0
        database = "card.s3db"

        self.sql_create_card_table = """ CREATE TABLE IF NOT EXISTS card(
                                id INTEGER,
                                number TEXT,
                                pin TEXT,
                                balance INTEGER DEFAULT 0);"""

        self.sql_insert_command = """INSERT INTO card VALUES (?,?,?,?)"""
        # create a database connection
        self.conn = BankingSys.create_connection(self, database)

        # create tables
        if self.conn is not None:
            # create card table
            BankingSys.create_table(self, self.conn, self.sql_create_card_table)
            # BankingSys.insert_data(self, self.conn, self.sql_insert_command, sql_insert_list)
            self.conn.commit()

        else:
            print("Error! Cannot create the database connection.")

    def create_table(self, conn, create_sql_table):
        c = conn.cursor()
        c.execute(create_sql_table)
        conn.commit()

    def create_connection(self, db_file):
        try:
            self.conn = sqlite3.connect(db_file)

        except Error as e:
            print(e)

        return self.conn

    def insert_data(self, data):
        c = self.conn.cursor()
        c.executemany(self.sql_insert_command, data)
        self.conn.commit()
        return c.lastrowid

    def action(self) -> object:
        user_input = input('1. Create an account\n'
                           '2. Log into account\n'
                           '0. Exit\n')
        while True:
            if user_input == '1':
                return BankingSys.create_account(self)
            elif user_input == '2':
                return BankingSys.login(self)
            elif user_input == '0':
                print('\nBye!')
                break
            else:
                print("Wrong input. Please try again\n")
                return BankingSys.action(self)

    def create_account(self):
        # Creating account using Luhn Algorithm
        self.accounts = []
        while True:
            ccn_gen = list('{0}'.format(str(random.randint(400000000000000, 400000999999999))))
            ccn_store = ccn_gen
            luhn_total = 0
            for luhn in range(0, len(ccn_store)):
                if (luhn + 1) % 2 != 0:
                    luhn_total += int(ccn_store[luhn]) * 2 \
                        if int(ccn_store[luhn]) * 2 <= 9 else (int(ccn_store[luhn]) * 2) - 9
                else:
                    luhn_total += int(ccn_store[luhn])
            break
        for check_digit in range(0, 10):
            if (luhn_total + check_digit) % 10 == 0:
                ccn_gen.append(str(check_digit))
                final_ccn = ''.join(ccn_gen)
                pin_digits = []
                for looper in range(0, 4):
                    pin = random.randint(0, 9)
                    pin_digits.append(str(pin))
                    convert = ''.join(pin_digits)

            else:
                continue

        self.accounts.append((self.num, final_ccn, convert, self.balance))
        print("\nYour card has been created\
              \nYour card number:\
              \n{}\
              \nYour card PIN:\
              \n{}\n".format(final_ccn, convert))
        self.num += 1
        BankingSys.insert_data(self, self.accounts)
        BankingSys.action(self)

    def menu(self, fetched_data):
        user_input = input('1. Balance\n'
                           '2. Add income\n'
                           '3. Do transfer\n'
                           '4. Close account\n'
                           '5. Log out\n'
                           '0. Exit\n')
        cur = self.conn
        while True:
            if user_input == '1':
                print("\nBalance: {}".format(fetched_data[3]))
                return BankingSys.menu(self, fetched_data)
            elif user_input == '2':
                print('\nEnter income:')
                income = int(input())
                cur.execute("UPDATE card SET balance = balance + {} WHERE number={}".format(income, fetched_data[1]))
                fetched_data = list(fetched_data)
                fetched_data[3] = fetched_data[3] + income
                fetched_data = tuple(fetched_data)
                self.conn.commit()
                print('Income was added!\n')
                BankingSys.menu(self, fetched_data)
                break
            elif user_input == '3':
                BankingSys.transfer(self, fetched_data)
                break
            elif user_input == '4':
                cur.execute("DELETE FROM card WHERE number=" + fetched_data[1])
                self.conn.commit()
                print('\nThe account has been closed!\n')
                BankingSys.action(self)
                break
            elif user_input == '5':
                print("\nYou have successfully logged out!\n")
                BankingSys.action(self)
                break
            elif user_input == '0':
                print('\nBye!')
                break
            else:
                print("\nWrong input. Please try again\n")
                return BankingSys.menu(self)

    def transfer(self, fetched_data):
        print("\nTransfers")
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM card")
        accounts_data = cur.fetchall()
        card_to_transfer = input('Enter card number:\n')
        ctf_temp = list(card_to_transfer) if len(list(card_to_transfer)) == 16 else []
        luhn_ = 0

        if ctf_temp == []:
            print('\nCard number too short!\n')
            BankingSys.menu(self, fetched_data)
        else:
            if card_to_transfer == fetched_data[1]:
                print("\nYou can't transfer money to the same account!\n")
                BankingSys.menu(self, fetched_data)
            else:
                for digit in range(0, len(ctf_temp) - 1):
                    if (digit + 1) % 2 != 0:
                        luhn_ += int(ctf_temp[digit]) * 2 if int(ctf_temp[digit]) * 2 <= 9 else (int(
                            ctf_temp[digit]) * 2) - 9
                    else:
                        luhn_ += int(ctf_temp[digit])
                if (luhn_ + int(ctf_temp[-1])) % 10 == 0:
                    for data in accounts_data:
                        if card_to_transfer == data[1]:
                            how_much = input('Enter how much money you want to transfer:\n')
                            if int(how_much) <= int(fetched_data[3]):
                                cur.execute('UPDATE card SET balance = balance + {} WHERE number = {};'.format(how_much,
                                                                                                               card_to_transfer))
                                cur.execute('UPDATE card SET balance = balance - {} WHERE number = {};'.format(how_much,
                                                                                                               fetched_data[
                                                                                                                   1]))
                                fetched_data = list(fetched_data)
                                fetched_data[3] = fetched_data[3] - int(how_much)
                                fetched_data = tuple(fetched_data)
                                self.conn.commit()
                                print('Success!\n')
                                BankingSys.menu(self, fetched_data)
                                break
                            else:
                                print('Not enough money!\n')
                                BankingSys.menu(self, fetched_data)
                                break
                    else:
                        print('Such a card does not exist.\n')
                        BankingSys.menu(self, fetched_data)
                else:
                    print('Probably you made mistake in the card number. Please try again!\n')
                    BankingSys.menu(self, fetched_data)

    def login(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM card")
        accounts_data = cur.fetchall()
        ccn = input('\nEnter your card number:\n')
        pin = input('Enter your PIN:\n')
        check_ccn = list(ccn)
        luhn_ = 0
        for i in range(0, len(check_ccn) - 1):
            if (i + 1) % 2 != 0:
                luhn_ += int(check_ccn[i]) * 2 if int(check_ccn[i]) * 2 <= 9 else (int(check_ccn[i]) * 2) - 9
            else:
                luhn_ += int(check_ccn[i])
        if (luhn_ + int(check_ccn[-1])) % 10 == 0:
            for data in accounts_data:
                if ccn == data[1]:
                    if pin == data[2]:
                        print("\nYou have successfully logged in!\n")
                        BankingSys.menu(self, data)
                    else:
                        print("\nWrong card number or PIN!\n")
                        BankingSys.action(self)
                        break
        else:
            print("\nWrong card number or PIN!\n")
            BankingSys.action(self)


start = BankingSys()
start.action()
start.conn.close()
