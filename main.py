import sys
import time

def delay_print(s):
    # print one character at a time
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1)

price = {'Book' : 100}
char_decisions = ['Trade', 'Talk', 'Fight']
available_types = ['Wizard', 'Warrior', 'Explorer']
char_inventory = {'MONEY': 1000, 'HOLDER': []}

char_username = str(input('Enter Your Name: '))
print('Available Character Types: {}'.format(available_types))
char_type = str(input('Select Your Type: '))
char_decision = char_decisions
char_invent = char_inventory

class Character:
    def __init__(self, name, types, decisions, ITEMS, health='===================='):
        self.name = name
        self.types = types
        self.decisions = decisions
        self.money = ITEMS['MONEY']
        self.items = ITEMS['HOLDER']
        self.health = health
        self.bars = 20

    def trade(self, answer):
        print('These are the items you currently have: {}'.format(char_inventory))
        answer_options = str(input('Would you like to buy an Item?: '))
        if answer_options == 'Yes' or answer_options == 'Y':
            print('Which item are you interested in?: {}'.format(Trader.items))
            selection = str(input('Enter Selection: '))
            if selection in Trader.items:
                print('{} Will cost you {}'.format(selection, price[selection]))
                final_decision_trader = str(input('Do you proceed?: '))
                final_price = price[selection]
                if final_decision_trader == 'Yes':
                    char.money -= final_price
                    char.items.append(selection)
                    Trader.money += final_price
                    print('Transaction Successful!')
                    print('Remaining money is {}'.format(char.money))
                else:
                    print('You walked away')
                    None
            else:
                None
        else:
            print('You walked away')
            None




    def introduce(self, Character2):
        delay_print('------YOU HAVE ENCOUNTERED A STRANGER------')
        print(f"\n{self.name}")
        print("YOUR TYPE", self.types)
        delay_print("=====STRANGER CREDENTIALS=====")
        delay_print(f"\n{Character2.name}")
        print("\nSTRANGER TYPE", Character2.types)
        time.sleep(2)

        delay_print('\nHello there {}! Nice to meet you'.format(char_username))
        delay_print('\nWhat do you need from me?')
        print("\nDECISIONS/", self.decisions)
        answer = str(input('Select an option from the list: '))
        if answer in Trader.decisions:
            if answer == 'Trade':
                char.trade(answer)


Trader = Character('Trader', 'Trader', ['Trade', 'Talk', 'Fight'], {'MONEY': 1000, "HOLDER": ['Book']})
char = Character(char_username, char_type, char_decision, char_invent)

char.introduce(Trader)