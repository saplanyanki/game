import sys
import time
from environment import *
import random


def delay_print(s):
    # print one character at a time
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

blacksmith_store = {'Bronze Sword': [380, 10],
                    'Bronze Shield': [400, 10],
                    'Health Potion': 100,
                    'Silver Apple': 500}
price = {'Book': 100,
         'Map': 1000,
         'Sword': 350,
         'Shield': 300}

talky = {1: 'Who are you?',
         2: 'What am I supposed to do?',
         3: 'Exit'}


actions = ['Dig', 'Wave', 'Eat Food']


char_decisions = ['Trade', 'Talk', 'Fight']
available_types = ['Wizard', 'Warrior', 'Explorer']
char_inventory = {'MONEY': 1000, 'HOLDER': []}



class Character:
    def __init__(self, name, types, decisions, ITEMS, xp, health='===================='):
        self.name = name
        self.types = types
        self.decisions = decisions
        self.money = ITEMS['MONEY']
        self.items = ITEMS['HOLDER']
        self.xp = xp
        self.health = health
        self.bars = 20


    def run(self):
        menu = str(input('\nWould you like to view Inventory?: '))
        if menu == 'Yes':
            print(char.money)
            print(char.items)
            travel = str(input('\nWould you like to travel to the nearest town?: '))
            if travel == 'Yes':
                char.town(travel)
            else:
                char.run()
        else:
            event_randomizer = random.randint(1, 100)
            if event_randomizer <= 50:
                char.action()
            else:
                char.introduce(Trader)

    def action(self):
        print(actions)
        action = str(input('\nYou encountered a random tile! Select an option: '))
        if action == 'Dig' or action == 'Wave':
            char.ground_coins(action)
        else:
            char.action()

    def ground_coins(self, action):
        if action == 'Dig':
            delay_print('You chose to dig the area!')
            random_dig = random.randint(0, 100)
            print('\nYou earned {} money!'.format(random_dig))
            char.money += random_dig
            char.run()

        if action == 'Wave':
            delay_print('You waved to the horizon!')
            chance = random.randint(0, 100)
            if chance >= 85:
                delay_print('You see a stranger in the horizon!')
                wave_action = str(input('Would you like to walk towards to the stranger?: '))
                if wave_action == 'Yes' or 'Y':
                    print('You approached the stranger!')
                    char.introduce(Trader)
                else:
                    char.run()
            else:
                char.run()


    def town(self, travel):
        print('\n1:Blacksmith \n2:Go Fishing \n3:Visit Warrior Den \n4:Talk with a Townie')
        travel_t = str(input('\nWhere would you like to visit in the town?: '))
        if travel_t == 'Blacksmith':
            delay_print('\nHello there... What brings you to my store?')
            print(blacksmith_store)
            bs_store_cart = str(input('\nWhat would you like to buy {}, {}?: '.format(char.types, char.name)))
            if bs_store_cart == 'Bronze Sword' or bs_store_cart == 'Bronze Shield':
                item_price = blacksmith_store[bs_store_cart][0]
                print('The price of the item will be {}'.format(blacksmith_store[bs_store_cart][0]))
                decision = str(input('Do you want to buy the item?: '))
                if decision == 'Yes':
                    char.money -= item_price
                    char.items.append(bs_store_cart)
                    delay_print('Item is added to your inventory')
                    exit_store = str(input('\nWould like to leave the store?: '))
                    if exit_store == 'Yes':
                        char.town(travel)
                    else:
                        char.town(travel_t)
                else:
                    delay_print('bye now...')
                    char.town(travel)
            else:
                char.town(travel)
        else:
            exit_town = str(input('\nWould like to leave the town?: '))
            if exit_town == 'Yes':
                char.run()
            else:
                char.town(travel)

    def trade(self, answer):
        print('These are the items you currently have: {}'.format(char.items))
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
                    char.run()
                else:
                    print('You walked away')
                    char.run()
            else:
                print('Item is not available!')
                char.run()
        else:
            print('You walked away')
            char.run()

    def talk(self, answer):
        print('==== {}, YOU CHOOSE TO TALK WITH THE {} ===='.format(char.name, Trader.name))
        print(talky)
        decision = int(input('Choose a dialog option:'))
        if decision in talky.keys():
            if decision == 1:
                print('\nI am the {}. You encountered me and wanted to talk with me'.format(Trader.name))
                delay_print('\nYou can trade goods with me and talk with me')
                char.introduce(Trader)
            elif decision == 2:
                print('\nYou are on a journey to become a great {}'.format(char.types))
                delay_print('\nYou will encounter many strangers in your journey')
                delay_print('\nYou can always talk with me to buy items!')
                char.introduce(Trader)
            elif decision == 3:
                delay_print('\nGoodbye dear friend...')
                char.introduce(Trader)
        else:
            delay_print('Goodbye')
            char.run()

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
            if answer == 'Talk':
                char.talk(answer)
            if answer == 'Fight':
                if char.xp < Trader.xp:
                    print('Oh... {} your XP is too low to fight!'.format(char.name))
                    char.introduce(Trader)
                else:
                    # Create fight function later
                    char.run()
        else:
            print('You left the area...')
            char.run()


while __name__ == '__main__':
    char_username = str(input('Enter Your Name: '))
    print('Available Character Types: {}'.format(available_types))
    char_type = str(input('Select Your Type: '))
    char_decision = char_decisions
    char_invent = char_inventory
    char_xp = 0
    char = Character(char_username, char_type, char_decision, char_invent, char_xp, 0)
    Trader = Character('Trader', 'Trader', ['Trade', 'Talk', 'Fight'],
                       {'MONEY': 1000, "HOLDER": ['Book', 'Map', 'Sword', 'Shield']}, 100)
    delay_print('Welcome to the Josuku Region!')
    print('\nYou will embark on a journey to become a Great {}'.format(char_type))
    print('\nBut first here are some tips and rules for you {}!'.format(char_username))
    print('\n1: Game flow is designed around random events')
    print('\n2: Your selections will determine your outcome of those events')
    print('\n3: Keep track of your money and items throughout your journey')
    print('\nGood luck... {}, {}'.format(char_type, char_username))
    char.run()
