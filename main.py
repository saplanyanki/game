import sys
import time

def delay_print(s):
    # print one character at a time
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

char_decisions = ['Trade', 'Talk', 'Fight']
available_types = ['Wizard', 'Warrior', 'Explorer']
char_inventory = {'MONEY': 0, 'ITEMS': []}

char_username = str(input('Enter Your Name: '))
print('Available Character Types: {}'.format(available_types))
char_type = str(input('Select Your Type: '))
char_decision = char_decisions
char_invent = char_inventory

class Character:
    def __init__(self, name, types, decisions, money, health='===================='):
        self.name = name
        self.types = types
        self.decisions = decisions
        self.money = money
        self.health = health
        self.bars = 20

    def introduce(self, Character2):
        print('------YOU HAVE ENCOUNTERED A STRANGER------')
        print(f"n{self.name}")
        print("TYPE/", self.types)
        print("DECISIONS/", self.decisions)
        print("\nENCOUNTERED")
        print(f"n{Character2.name}")
        print("TYPE/", Character2.types)
        print("DECISIONS/", Character2.decisions)
        time.sleep(1)

Trader = Character('Trader', 'Trader', ['Trade', 'Talk', 'Fight'], {'MONEY': 1000, "ITEMS": []})
char = Character(char_username, char_type, char_decision, char_invent)

char.introduce(Trader)