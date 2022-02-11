import sys
import time
import random


def delay_print(s):
    # print one character at a time
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)


blacksmith_store = {'Bronze Sword': 380,
                    'Bronze Shield': 400,
                    'Health Potion': 100,
                    'Silver Apple': 500}

wizard_store = {'Wand': 500,
                'Book of Wizardry': 1200}


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
char_inventory = {'MONEY': 1000, 'HOLDER': [], 'FOOD': ['Apple']}


class Character:
    def __init__(self, name, types, decisions, MOVES, ITEMS, xp, health='===================='):
        self.name = name
        self.types = types
        self.decisions = decisions
        self.moves = MOVES['MAGIC MOVES']
        self.money = ITEMS['MONEY']
        self.items = ITEMS['HOLDER']
        self.food = ITEMS['FOOD']
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

        if action == 'Eat Food':
            if bool(char.food) == False:
                delay_print('You have no food!')
                char.action()
            else:
                delay_print('\nYou have some food in your inventory!')
                print(char.food)
                food_choice = str(input('\nSelect a food to eat?: '))
                if food_choice in char.food:
                    char.food.remove(food_choice)
                    delay_print('You health has replenished!')
                    char.bars += 5
                    char.health = ""
                    for j in range(int(char.bars)):
                        char.health += "="
                    print(char.health)
                    char.run()
                else:
                    delay_print('You do not have that food available')
                    char.action()
        else:
            char.run()

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

    def fight(self, fighter2):
        print('==== {}, YOU CHOOSE TO FIGHT WITH THE {} ===='.format(char.name, fighter2.name))
        print(f"\n{self.name}")
        print("YOUR TYPE", self.types)
        delay_print("=====FIGHTER CREDENTIALS=====")
        delay_print(f"\n{fighter2.name}")
        print("\nSTRANGER TYPE", fighter2.types)
        time.sleep(2)

        while char.bars > 0 and fighter2.bars > 0:
            fight_menu = ['ATTACK', 'DEFEND']
            print(fight_menu)
            user_fight_choice = str(input('Choose a Style: '))
            if user_fight_choice == 'ATTACK':
                user_fight_item = str(input('Choose a weapon: '))
                if user_fight_item in char.items:
                    print('\nYou chose {} to fight with!'.format(user_fight_item))
                    delay_print('You made damage')
                    fighter2.bars -= 5
                    fighter2.health = ""
                    for j in range(int(fighter2.bars)):
                        fighter2.health += "="
                    print('\nRemaining Opponent Health: {}'.format(fighter2.health))
                    print('\nYour Health: {}'.format(char.health))
                    if char.bars <= 0:
                        delay_print("\n..." + char.name + ' fainted.')
                        break
                    if fighter2.bars <= 0:
                        delay_print("\n..." + fighter2.name + ' fainted.')
                        break
                    delay_print('Opponent Attacked You!')
                    char.bars -= 3
                    char.health = ""
                    for j in range(int(char.bars)):
                        char.health += "="
                    print('\nRemaining Opponent Health: {}'.format(fighter2.health))
                    print('\nYour Health: {}'.format(char.health))
                    if char.bars <= 0:
                        delay_print("\n..." + char.name + ' fainted.')
                        break
                    if fighter2.bars <= 0:
                        delay_print("\n..." + fighter2.name + ' fainted.')
                        break
                else:
                    delay_print('You stumbled...')
                    break

            if user_fight_choice == 'DEFEND':
                user_fight_item = str(input('Choose a weapon to defend: '))
                if user_fight_item in char.items:
                    print('\nYou chose {} to defend with!'.format(user_fight_item))
                    delay_print('Opponent attacked you!')
                    delay_print('You blocked attack')
                    print('\nRemaining Opponent Health: {}'.format(fighter2.health))
                    print('\nYour Health: {}'.format(char.health))
                    if char.bars <= 0:
                        delay_print("\n..." + char.name + ' fainted.')
                        break
                    if fighter2.bars <= 0:
                        delay_print("\n..." + fighter2.name + ' fainted.')
                        break
                    break
                else:
                    delay_print('You stumbled...')
                    delay_print('Opponent Attacked You!')
                    char.bars -= 3
                    char.health = ""
                    for j in range(int(char.bars)):
                        char.health += "="
                    print('\nRemaining Opponent Health: {}'.format(fighter2.health))
                    print('\nYour Health: {}'.format(char.health))
                    if char.bars <= 0:
                        delay_print("\n..." + char.name + ' fainted.')
                        break
                    if fighter2.bars <= 0:
                        delay_print("\n..." + fighter2.name + ' fainted.')
                        break
                break

        if char.bars > 0 and fighter2.bars <= 0:
            delay_print('Congratulations you won the fight!')
            xp_fight = 2
            print('{} XP Gained'.format(xp_fight))
            char.xp += xp_fight
            delay_print('Getting dark... better leave the town!')
            char.run()

        if char.bars <= 0 and fighter2.bars > 0:
            delay_print('...You lost the fight!')
            delay_print('Getting dark... better leave the town!')
            char.run()

    def town(self, travel):
        print('\n1:Blacksmith \n2:Go Fishing \n3:Warrior Den \n4:Talk with a Drunk Townie')
        travel_t = str(input('\nWhere would you like to visit in the town?: '))
        if travel_t == 'Blacksmith':
            delay_print('\nHello there... What brings you to my store?')
            print(blacksmith_store)
            bs_store_cart = str(input('\nWhat would you like to buy {}, {}?: '.format(char.types, char.name)))
            if bs_store_cart == 'Bronze Sword' or bs_store_cart == 'Bronze Shield':
                item_price = blacksmith_store[bs_store_cart]
                print('The price of the item will be {}'.format(blacksmith_store[bs_store_cart]))
                decision = str(input('Do you want to buy the item?: '))
                if decision == 'Yes' and char.money >= item_price:
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

            if bs_store_cart == 'Health Potion' or bs_store_cart == 'Silver Apple':
                item_price = blacksmith_store[bs_store_cart]
                print('The price of the item will be {}'.format(blacksmith_store[bs_store_cart]))
                decision = str(input('Do you want to buy the item?: '))
                if decision == 'Yes' and char.money >= item_price:
                    char.money -= item_price
                    char.food.append(bs_store_cart)
                    delay_print('Item is added to your inventory')
                    exit_store = str(input('\nWould like to leave the store?: '))
                    if exit_store == 'Yes':
                        char.town(travel)
                    else:
                        char.town(travel_t)
                else:
                    delay_print('bye now...')
                    char.town(travel)

        if travel_t == 'Go Fishing':
            fishes = ['Tuna', 'Salmon', 'Cod', 'Crab', 'Golden Yellow-tail']
            print('\nYou went to fish!')
            print('\nYou have to pick a spot to fish!')
            print('\n1:Grey Fog\n2:Random Sand Pile\n3:Golden Beak')
            fish_area = str(input('Pick a Fishing Spot!: '))
            if fish_area == 'Grey Fog':
                delay_print('Fishing at Grey Frog...')
                fish_rand_gf = random.randint(0, 10)
                if fish_rand_gf >= 6:
                    print('You caught a Tuna Fish!')
                    char.food.append(fishes[0])
                    char.town(travel)
                if fish_rand_gf <= 5:
                    print('You caught a Cod Fish!')
                    char.food.append(fishes[2])
                    char.town(travel)
            if fish_area == 'Random Sand Pile':
                delay_print('Fishing at Random Sand Pile...')
                delay_print('It is warm and cozy here...')
                fish_rand_gf = random.randint(0, 10)
                if fish_rand_gf >= 7:
                    print('You caught a Tuna Fish!')
                    char.food.append(fishes[0])
                    char.town(travel)
                else:
                    print('You caught a Cod Fish!')
                    char.food.append(fishes[2])
                    char.town(travel)
            if fish_area == 'Golden Beak':
                delay_print('Fishing at Golden Beak...')
                delay_print('You stopped and looked around')
                delay_print('... Such a beautiful view')
                fish_rand_gf = random.randint(0, 10)
                if fish_rand_gf >= 9:
                    print('You caught a Golden Yellow-Tail!')
                    print('It is the rarest fish in town!')
                    char.food.append(fishes[4])
                    char.town(travel)
                if 5 <= fish_rand_gf <= 8:
                    print('You caught a Salmon Fish!')
                    char.food.append(fishes[1])
                    char.town(travel)
                if fish_rand_gf <= 4:
                    print('You caught a Crab')
                    delay_print('It bit your hand!')
                    delay_print('You health has diminished!')
                    char.bars -= 5
                    char.health = ""
                    for j in range(int(char.bars)):
                        char.health += "="
                    print(char.health)
                    char.town(travel)

            else:
                print('Hmm... Not sure what you meant')
                char.town(travel)

        if travel_t == 'Warrior Den':
            delay_print('You chose to go to Warrior Den!')
            delay_print('You see warriors talking...')
            print('Hello {} {} we were notified that you were in town!'.format(char.types, char.name))
            if char.xp < 25:
                print('Your XP level is too low to go inside')
                print('\nCurrent XP level: {}'.format(char.xp))
                print('\nHowever, you can practise and gain XP in the yards!')
                warrior_den_yards = str(input('Would you like to practice in the yards?: '))
                if warrior_den_yards == 'Yes':
                    char.fight(Practise_Warrior)
                else:
                    char.town(travel)
            else:
                print('I will take you inside!')
                char.town(travel)

        if travel_t == 'Talk with a Drunk Townie':
            delay_print('You approached the Drunk Townie')
            print('\nThis towns booze is not good enough')
            print('\nHmm... I do not know who you are')
            print('\nLet me guess you are a {}'.format(char.types))
            print('\nWell what do you do here {}'.format(char.types))
            print('\nPick a dialog option:\n1: I am exploring the area\n2: I honestly do not know what I am doing...')
            usr_choice = str(input('Write the dialog here: '))
            if usr_choice == 'I am exploring the area':
                print('\nAhh... keep exploring then this is a mysterious town they say')
                print('\nLet me know... if you have more interesting things to discuss..')
                char.town(travel_t)

            if usr_choice == 'I honestly do not know what I am doing':
                print('\nArent you a {}? You should explore the area to help you get stronger'.format(char.types))
                print('\nI hear there is a {} Temple in a nearby town...'.format(char.types))
                while 'Carson Potion' in char.items:
                    usr_choice = str(input('Are you ready to go?: '))
                    if usr_choice == 'Yes':
                        char.mysterytown(usr_choice)
                    else:
                        print('Come to me when you are ready!')
                        char.town(travel)

                while 'Carson Potion' not in char.items:
                    print('\nI can take you there if you can do one thing for me... {}'.format(char.types))
                    usr_choice = str(input('Would like to do mission for the drunk townie?'))
                    if usr_choice == 'Yes':
                        if 'Golden Yellow-Tail' not in char.food:
                            print('\nI need you to get me a golden yellow-tail')
                            print('\nI heard that there is couple in one of the fishing spots!')
                            print('\nYou left the area in a hurry to complete the mission!')
                            char.town(travel)

                        else:
                            print('\nAhh... I see you already have what we need!')
                            print('\nA golden yellow-tail...')
                            print('\nAlmost forgot we also need a crabs shell!')
                            if 'Crab' in char.food:
                                print('\nAhh... I see you already have what we need!')
                                print('\nNow I need to mix them in my bottle...')
                                delay_print('You observe that the drunk townie is actually a Witch!')
                                char.food.remove('Crab')
                                char.food.remove('Golden Yellow-Tail')
                                char.items.append('Carson Potion')
                                delay_print('Carson Potion added to inventory!')
                                print(char.items)
                                print('Here we go!')
                                usr_choice = str(input('Are you ready to go?: '))
                                if usr_choice == 'Yes':
                                    char.mysterytown(usr_choice)
                                else:
                                    print('Come to me when you are ready!')
                                    char.town(travel)
                    else:
                        print('Well then, goodbye friend...')
                        char.town(travel)

            else:
                print('You left the area...')
                char.town(travel)

        else:
            exit_town = str(input('\nWould like to leave the town?: '))
            if exit_town == 'Yes':
                char.run()
            else:
                char.town(travel)

    def mysterytown(self, usr_choice):
        delay_print('You share the potion with the drunk townie!')
        print('Welcome to the unknown town, {}'.format(char.types))
        print('\n1:Wizardry \n2:Wizard Market')
        travel_m = str(input('\nWhere would you like to visit in the mystery town?: '))
        if travel_m == 'Wizardry' and char.xp >= 10:
            delay_print('You chose to go to the Wizardry!')
            print('\nWelcome to the Wizardry')
            print('\n1:Go Inside Wizardry\n2:Practise Wizardry\n3:Meet with Grandmaster Wizard')
            wizardry_choice = str(input('Enter your choice: '))
            if wizardry_choice == 'Go Inside Wizardry':
                delay_print('You entered inside the Wizardry')
                if 'Vision Maxifier' not in char.items:
                    print('\nIt seems like you are not seeing everything around you...')
                    print('\nYou are asked to leave... maybe you are missing an item??')
                    char.mysterytown(usr_choice)
                if 'Vision Maxifier' in char.items:
                    print('\nYou should use your Vision Maxifier')
                    usr_item_wizardry = str(input('Equip Vision Maxifier?: '))
                    if usr_item_wizardry == 'Yes':
                        print('\nYou have used Vision Maxifier!')
                        print('\nYou are seeing so many things!')
                        print('\nThe legends! The old magic moves!')
                        usr_learn_wizardry = str(input('\nWould you like to learn a move?: '))
                        if usr_learn_wizardry == 'Yes':
                            if 'Blue Twizzle' in char.moves and 'Blue Glosser' in char.moves:
                                print('\nYou already learned these moves {}'.format(char.moves))
                                print('Spirits are cursing you...')
                                print('You couldnt find anything else to do so you left')
                                char.mysterytown(usr_choice)

                            else:
                                char.moves.append('Blue Twizzle')
                                char.moves.append('Blue Protestant')
                                print('\nYou learned two new moves {}'.format(char.moves))
                                print('\nYou left the building')
                                char.mysterytown(usr_choice)
                        else:
                            print('Spirits are cursing you...')
                            print('You couldnt find anything else to do so you left')
                            char.mysterytown(usr_choice)

                    else:
                        print('\nIt seems like you are not seeing everything around you...')
                        print('\nYou are asked to leave... maybe you are missing an item??')
                        char.mysterytown(usr_choice)

            if wizardry_choice == 'Practise Wizardry' and bool(char.moves) == True and 'Wand' in char.items:
                delay_print('You chose to practise Wizardry')
                char.wizardfight(Practise_Wizard)

            if wizardry_choice == 'Practise Wizardry' and bool(char.moves) == False and 'Wand' not in char.items:
                delay_print('You have no wizardry move, explore the area more')
                delay_print('You also dont have a wand!')
                print('\nBuy a wand from the Wizard Market')
                char.mysterytown(usr_choice)

            if wizardry_choice == 'Meet with Grandmaster wizard' and char.xp <=49:
                delay_print('You cannot go in...')
                print('Needed XP: 50, Your XP: {}'.format(char.xp))
                char.mysterytown(usr_choice)

            if wizardry_choice == 'Meet with Grandmaster Wizard' and char.xp >= 50:
                delay_print('You passed through halls and climbed stairs...')

        if travel_m == 'Wizardry' and char.xp <= 10:
            delay_print('Your XP is too low to enter the Wizardry!')
            print('Your XP:{}, Needed XP: 10'.format(char.xp))
            char.mysterytown(usr_choice)

        if travel_m == 'Wizard Market':
            delay_print('Welcome to the Wizard Mart!')
            print(wizard_store)
            wm_store_cart = str(input('\nWhat would you like to buy {}, {}?: '.format(char.types, char.name)))
            if wm_store_cart in wizard_store:
                item_price = wizard_store[wm_store_cart]
                print('The price of the item will be {}'.format(wizard_store[wm_store_cart]))
                decision = str(input('Do you want to buy the item?: '))
                if decision == 'Yes' and char.money >= item_price:
                    char.money -= item_price
                    char.items.append(wm_store_cart)
                    delay_print('Item is added to your inventory')
                    exit_store = str(input('\nWould like to leave the store?: '))
                    if exit_store == 'Yes':
                        char.mysterytown(usr_choice)
                    else:
                        char.mysterytown(usr_choice)
                if decision == 'Yes' and char.money < item_price:
                    delay_print('You do not have enough money...')
                    char.mysterytown(usr_choice)

                else:
                    delay_print('bye now...')
                    char.mysterytown(usr_choice)
            else:
                print('\nHmm item is not available... come back later')
                char.mysterytown(usr_choice)

        else:
            print('You wandered around confused...')
            exit_town = str(input('\nWould like to leave the mystery town?: '))
            if exit_town == 'Yes':
                char.run()
            else:
                char.mysterytown(usr_choice)



    def wizardfight(self, wizard2):
        print('==== {}, YOU CHOOSE TO DUEL WITH THE {} ===='.format(char.name, wizard2.name))
        print(f"\n{self.name}")
        print("YOUR TYPE", self.types)
        delay_print("=====WIZARD CREDENTIALS=====")
        delay_print(f"\n{wizard2.name}")
        print("\nWIZARD TYPE", wizard2.types)
        time.sleep(2)

        while char.bars > 0 and wizard2.bars > 0:
            fight_menu = char.moves
            print(fight_menu)
            user_fight_choice = str(input('Choose a Move: '))
            if user_fight_choice in fight_menu:
                user_fight_item = str(input('Choose a wand: '))
                if user_fight_item in char.items and user_fight_item == 'Wand':
                    print('\nYou chose {} to duel with!'.format(user_fight_item))
                    delay_print('You made damage')
                    if user_fight_choice == 'Blue Twizzle':
                        wizard2.bars -= 8
                        wizard2.health = ""
                    if user_fight_choice == 'Blue Protestant':
                        wizard2.bars -= 6
                        wizard2.health = ""
                    else:
                        delay_print('You stumbled...')

                    for j in range(int(wizard2.bars)):
                        wizard2.health += "="
                    print('\nRemaining Opponent Health: {}'.format(wizard2.health))
                    print('\nYour Health: {}'.format(char.health))
                    if char.bars <= 0:
                        delay_print("\n..." + char.name + ' fainted.')
                        break
                    if wizard2.bars <= 0:
                        delay_print("\n..." + wizard2.name + ' fainted.')
                        break
                    delay_print('Opponent Attacked You!')
                    char.bars -= 5
                    char.health = ""
                    for j in range(int(char.bars)):
                        char.health += "="
                    print('\nRemaining Opponent Health: {}'.format(wizard2.health))
                    print('\nYour Health: {}'.format(char.health))
                    if char.bars <= 0:
                        delay_print("\n..." + char.name + ' fainted.')
                        break
                    if wizard2.bars <= 0:
                        delay_print("\n..." + wizard2.name + ' fainted.')
                        break
                else:
                    delay_print('You stumbled...')
                    break

            if user_fight_choice == 'DEFEND':
                user_fight_item = str(input('Choose a weapon to defend: '))
                if user_fight_item in char.items:
                    print('\nYou chose {} to defend with!'.format(user_fight_item))
                    delay_print('Opponent attacked you!')
                    delay_print('You blocked attack')
                    print('\nRemaining Opponent Health: {}'.format(wizard2.health))
                    print('\nYour Health: {}'.format(char.health))
                    if char.bars <= 0:
                        delay_print("\n..." + char.name + ' fainted.')
                        break
                    if wizard2.bars <= 0:
                        delay_print("\n..." + wizard2.name + ' fainted.')
                        break
                    break
                else:
                    delay_print('You stumbled...')
                    delay_print('Opponent Attacked You!')
                    char.bars -= 10
                    char.health = ""
                    for j in range(int(char.bars)):
                        char.health += "="
                    print('\nRemaining Opponent Health: {}'.format(wizard2.health))
                    print('\nYour Health: {}'.format(char.health))
                    if char.bars <= 0:
                        delay_print("\n..." + char.name + ' fainted.')
                        break
                    if wizard2.bars <= 0:
                        delay_print("\n..." + wizard2.name + ' fainted.')
                        break
                break

        if char.bars > 0 and wizard2.bars <= 0:
            delay_print('Congratulations you won the duel!')
            xp_fight = 3
            print('{} XP Gained'.format(xp_fight))
            char.xp += xp_fight
            delay_print('Getting dark... better leave the town!')
            char.run()

        if char.bars <= 0 and wizard2.bars > 0:
            delay_print('...You lost the duel!')
            delay_print('Getting dark... better leave the town!')
            char.run()

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
                if final_decision_trader == 'Yes' and char.money >= final_price:
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
    char = Character(char_username, char_type, char_decision, [], char_invent, char_xp)

    Trader = Character('Trader', 'Trader', ['Trade', 'Talk', 'Fight'], [],
                       {'MONEY': 1000, "HOLDER": ['Book', 'Map'], 'FOOD': []}, 100)

    Practise_Warrior = Character('Novice Warrior', 'Warrior', ['Fight', 'Fight', 'Fight'], [],
                                 {'MONEY': 1000, "HOLDER": ['Bronze Sword', 'Bronze Shield'], 'FOOD': []}, 10)

    Practise_Wizard = Character('Novice Wizard', 'Wizard', ['Wizard Fight', 'Wizard Fight', 'Wizard Fight'], ['Yellow Twister'],
                                 {'MONEY': 1000, "HOLDER": ['Wand'], 'FOOD': []}, 10)

    delay_print('Welcome to the Josuku Region!')
    print('\nYou will embark on a journey to become a Great {}'.format(char_type))
    print('\nBut first here are some tips and rules for you {}!'.format(char_username))
    print('\n1: Game flow is designed around random events')
    print('\n2: Your selections will determine your outcome of those events')
    print('\n3: Keep track of your money and items throughout your journey')
    print('\nGood luck... {}, {}'.format(char_type, char_username))
    char.run()
