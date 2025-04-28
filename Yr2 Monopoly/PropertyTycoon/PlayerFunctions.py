import random
import operator
#from cards import card
#from Game import player_list
import SpecialCardFunctions as SCF
#import CardFunctions as CF
from BoardDefinition import game_board
import numpy as np
import Bank as bk
bank_player = ""

import pygame
pygame.init()
gb = game_board()
SCREEN_WIDTH = 1270
SCREEN_HEIGHT = 768

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))



class token:
    def __init__(self, player, position, money, cards, in_jail, jail_count, circuit, stations, utlity, pot_jail_pass, knock_jail_pass, bankrupt, stored_jail_cards, probability,banker):
        self.player = player
        self.position = position
        self.money = money
        self.cards = cards
        self.in_jail = in_jail
        self.jail_count = jail_count
        self.circuit = circuit
        self.stations = stations
        self.utlity = utlity
        self.pot_jail_pass= pot_jail_pass
        self.knock_jail_pass = knock_jail_pass
        self.bankrupt = bankrupt
        self.stored_jail_cards = stored_jail_cards
        self.probability = probability
        self.banker = banker


    def use_jail_pass(self):
        for idx, free in enumerate(self.stored_jail_cards):
            print(free.card_name)
        if self.probability > 0:
            player_input = random.choice([-1, 0])
            if player_input == len(self.stored_jail_cards) - 1:
                if self.stored_jail_cards[int(player_input)].card_name == "Jail_Pot":
                    print(self.player, " used his get out of jail card")
                    self.in_jail = False
                    SCF.pot.append(self.stored_jail_cards[player_input])
                    self.pot_jail_pass.clear()
                elif self.stored_jail_cards[int(player_input)].card_name == "Jail_Knocks":
                    print(self.player, " used his get out of jail card")
                    self.in_jail = False
                    self.knock_jail_pass.clear()
                    SCF.knocks.append(self.stored_jail_cards[player_input])
            else:
                self.buy_out_of_jail()

    def use_jail_pass_name(self,card_name):
        for idx, free in enumerate(self.stored_jail_cards):
            print(free.card_name)
            if self.probability > 0:
                player_input = random.choice([-1, 0])
            #else:
                #player_input = input("Press the number given number if you want to use the free jail pass")
            if card_name == self.stored_jail_cards[idx].card_name:
                if self.stored_jail_cards[idx].card_name == "Jail_Pot":
                    print(self.player, " used his get out of jail card")
                    self.in_jail = False
                    self.pot_jail_pass = False
                    SCF.pot.append(self.stored_jail_cards[idx])
                elif self.stored_jail_cards[idx].card_name == "Jail_Knocks":
                    print(self.player, " used his get out of jail card")
                    self.in_jail = False
                    self.knock_jail_pass = False
                    SCF.knocks.append(self.stored_jail_cards[idx])
            else:
                self.buy_out_of_jail()

    def buy_out_of_jail(self):
        if self.probability == 0:
            print(self.player, " is currently in jail, press y to pay or anything to skip\n")
            #player_input = input("Enter the value")
            if self.money > 50:
                gb[20].rent += self.deduct_money(50)
                self.in_jail = False
                self.jail_count = 0
                print("You paid out of jail, current balance:", self.money)
                print("You can roll next turn")
            #else:
                #self.turns_spent_jail()
        else:
            print(self.player, " is currently in jail, press y to pay or anything to skip\n")
            x = np.random.uniform(low=0, high=1)
            if self.probability >= x and self.money > 50:
                gb[20].rent += self.deduct_money(50)
                self.in_jail = False
                self.jail_count = 0
                print("You paid out of jail, current balance:", self.money)
                print("You can roll next turn")
            else:
                self.turns_spent_jail()

    def currently_in_jail(self):
        self.in_jail = True
        self.position = 10
        if self.jail_count > 0:
            self.turns_spent_jail()
        elif len(self.stored_jail_cards) > 0:
            self.use_jail_pass()
        else:
            self.buy_out_of_jail()

    def turns_spent_jail(self):
        if self.probability == 0:
            self.jail_count += 1
            print("Currently you are in jail, count", self.jail_count)
            #input("Press something to skip your turn")
        else:
            self.jail_count += 1

            print("Currently you are in jail, count", self.jail_count)
            if self.jail_count == 3:
                print(self.player, " is just visiting in jail")
                self.in_jail = False
                self.jail_count = 0


    def dice_roll(self):
        dice1 = random.randrange(1, 7)
        dice2 = random.randrange(1, 7)
        print(dice1,dice2)
        return dice1, dice2


    def check_double(self,plist, dice1, dice2):
        total = dice1+dice2
        self.check_card(gb[self.position], plist, total, self.probability)
        count = 0
        if self.probability > 0:
            if dice1 == dice2:
                flag = True
                while (flag):
                    total = 0
                    print(
                            "Since we got a double we must roll again, 3 same rolls results in jail time, current roll",
                            count)
                    diceA, diceB = self.dice_roll()
                    print(diceA, diceB)
                    total = diceA + diceB
                    if diceA == diceB:
                        count += 1
                        if count == 2:
                            print(self.player, "Has moved to jail")
                            self.currently_in_jail()
                            flag = False
                        self.check_card(gb[self.move_player(total)], plist, total, self.probability)
                    else:
                        result = dice1 + dice2
                        self.check_card(gb[self.move_player(result)], plist, total, self.probability)
                        flag = False
        else:
            if dice1 == dice2:
                flag = True
                while (flag):
                    total = 0
                    print("Since we got a double we must roll again, 3 same rolls results in jail time, current roll",count)
                    input("Press enter")
                    diceA, diceB = self.dice_roll()
                    print(diceA, diceB)
                    total = diceA + diceB
                    if diceA == diceB:
                        count += 1
                        if count == 2:
                            print(self.player, "Has moved to jail")
                            self.currently_in_jail()
                            flag = False
                        self.check_card(gb[self.move_player(total)], plist, total, self.probability)
                    else:
                        result = dice1 + dice2
                        self.check_card(gb[self.move_player(result)], plist, total, self.probability)
                        flag = False

    def move_player(self, dicesum):
        self.position += dicesum
        if self.position >= 40:
            self.position -= 40
            if self.position > 0:
                print(self.money)
                #bk.bank_creations.reduce_banks_money(bank_player, 200, self)
                #self.give_money(200)
                print(self.money)
                self.circuit = True
            print("Since",self.player, "crosses go they get 200")
        print(self.player,"current pos", self.position)
        return self.position


    def board(self, board):
        boardposition = board[self.position]
        print(self.player, "position is")



    def check_card(self, card, plist,dice, probability):
        print(card.card_owner)
        #print(bank_player.money, "asawq")
        if card.card_owner == "Bank" and card.card_cost != -1:
            print(card.card_name)
            if probability > 0:
                card.buy_card(self, 0, plist,bank_player)
            else:
                decision = input("Currently the card is owned by the bank, would you like to buy this card?: Y or N?\n")
                if decision == "y":
                    card.buy_card(self, 0,plist,bank_player)
                else:
                    print("No")
                    self.auction(card, plist)
        elif card.card_owner != "Bank" and card.card_cost != -1:
            print("The card is owned by", card.card_owner)
            if card.card_owner == self.player:
                print("You own this card")
            else:
                for user in plist:
                    if user.player == card.card_owner:
                        if card.mortgage == True:
                            print(card.card_name, " is currently mortgaged")
                        elif card.card_color == "Railroad":
                            card.pay_railroads(self,user)
                        elif card.card_color == "Utilities":
                            card.pay_utilities(self,user,dice)
                        else:
                            card.pay_player2(self, user, 0)
        else:
            if card.card_name == "Income Tax":
                print(self.player, "Landed on", card.card_name, "so 200 is removed")
                gb[20].rent += self.deduct_money(200)
            elif card.card_name == "Super Tax":
                print(self.player, "Landed on", card.card_name, "so 100 is removed")
                gb[20].rent += self.deduct_money(100)
            elif card.card_name == "Go to Jail":
                print(self.player, "Landed on", card.card_name, "so he is in jail")
                self.currently_in_jail()
            elif card.card_name == "Visiting Jail":
                print(self.player, "Landed on", card.card_name, "so he visiting jail")
            elif card.card_name == "go":
                print(self.player, "Landed on", card.card_name, "once he passes it he will recieve 200")
            elif card.card_name == "Pot Luck":
                print(self.player, " Landed on a Pot Luck")
                SCF.pick_pot(self,plist,dice)
            elif card.card_name == "Opportunity Knocks":
                print(self.player," landed on Opportunity Knocks")
                SCF.pick_knock(self,plist,dice)
            elif card.card_owner == self.player and self.circuit == True: #add self.check_set in here?
                card.buy_houses(token,bank_player)
            elif card.card_name == "Free Parking":
                if card.rent > 0:
                    print(self.player, " has just gotten ",card.rent, " from Free parking")
                    self.give_money(card.rent)
                    card.rent = 0



    def player_banker(self, banker):
        global bank_player
        bank_player = banker
        #bk.bank_creations(banker, 50000)


    def player_action(self,card,banker):
        val = -1
        flag = True
        global bank_player
        bank_player = bk.bank_creations.get_banker(banker)
        while(flag):
            if self.probability > 0:
                val = self.dice_roll()
                flag = False
            else:
                action = input("Please enter r to roll")
                if action == "r":
                    val = self.dice_roll()
                    flag = False
        return val

    '''
     * @param self
     * @param money_added INT
     * Gives the player money
    '''
    def give_money(self, moeny_added):
        self.money += moeny_added
        print(self.player, "Balance is now", self.money)
        return self.money


    '''
     * @param self
     * @param money_removed INT
     * Takes money out of the player money
    '''
    def deduct_money(self, money_removed):
        print(self.money < money_removed)
        #if self.money < money_removed:
            #return self.sell(money_removed,0)
       #else:
        self.money -= money_removed
        print(self.player, "money is now", self.money)
        return money_removed

    '''
     * @param self
     * @param card Instance
     * @param plist List of players
     Auction is used to auction the card and the players make a bet on it
    '''
    def auction(self, card, plist):
        print(card.card_name, " is currently on auction\n please enter a bet greater than 0")
        count = 0
        player_bet = {i.player: 0 for i in plist if i.circuit == True}
        player_list = [i for i in plist if i.circuit == True]
        print(player_bet)
        while(len(player_bet) != 0):
            if len(player_bet) == 1 and list(player_bet.values())[0] > 0:
                print(player_list[count].player, " has won the bet")
                card.buy_card((player_list[0]), list(player_bet.values())[0],plist,bank_player)
                del player_bet[player_list[count].player]
            else:
                print("Current player is", player_list[count].player)
                max_value = max(player_bet.values())
                if player_list[count].probability > 0:
                    bet = card.ai_auction(player_list[count],player_list,max_value,player_list[count].probability)
                else:
                    bet = input("Please enter your bet")
                #max_value = max(player_bet.values())
                if int(bet) > max_value and int(bet) < player_list[count].money:
                    player_bet[player_list[count].player] = int(bet)
                    print("The current list is", player_bet)
                else:
                    print(player_list[count].player, " bet wasnt accept")
                    del player_bet[player_list[count].player]
                    del player_list[count]
                    count -= 1
            count += 1
            if count >= len(player_list):
                count = 0

    def display_player_properties(self):
        #might need to change this code
        print("\nCards owned\n")
        for idx, card in enumerate(self.cards):
            if card.card_color == "Railroad" or card.card_color == "Utilities":
                print(f"{idx}: {card.card_name}: ${card.card_cost}")
            else:
                print(f"{idx}: {card.card_color}: {card.card_name}: ${card.card_cost} Houses:{card.houses}")

    def check_set(self):
        mydict = {}
        count = {}
        card_list = []
        for idx, c in enumerate(self.cards):
            if c.card_color == "Railroad" or c.card_color == "Utilities":
                continue
            else:
                mydict.setdefault(c.card_color, []).append(c)
                count[c.card_color] = count.get(c.card_color, 0) + 1
                card_list.append(c.card_color)
        temp = [(card,card_list.count(card)) for card in card_list]
        card_list.clear()
        for key,value in list(set(temp)):
            if (key == "Brown" or key == "Deep Blue") and value == 2:
                print("bye")
                card_list.append(key)
            elif (key == "Green" or key == "Blue" or key == "Yellow" or key == "Purple" or key == "Red") and value == 3:
                card_list.append(key)
            else:
                print("You do not have a set for this ",key)
        return (list(set(card_list)),mydict)

    def check_houses(self):
        count = {}
        for card in self.cards:
            count[card.card_color] = count.get(card.card_color, 0) + card.houses
        return count
    '''
     * @param self
     Checks the number of houses and hotels for OK "H" function
    '''
    def check_hotels_and_houses(self):
        house_no = 0
        hotel_no = 0
        for card in self.cards:
            if card.houses == 5:
                hotel_no += 1
                house_no += 4
            elif card.houses > 0:
                house_no += card.houses
        return house_no,hotel_no

    '''
     * @param self
     Checks if it has a mortgaged card
    '''
    def check_mortgage(self):
        mydict = {}
        for card in self.cards:
            if card.mortgage == True:
                mydict.setdefault(card.card_color, []).append(card)
        return (mydict)

    '''
        # Bankrupts player
        # @param: self
        '''
    def bankrupt_player(self):
        self.bankrupt = True

    '''
        # Checks total property cost for the ai to buy houses
        # @param: self
        '''
    def total_property_cost(self):
        flag = True
        cost = {}
        #card_list, mydict = self.check_set()
        no_houses = self.check_houses()
        print("hhhhhhh")
        for card in self.cards:
            if card.card_color == "Railroad" or card.card_color == "Utilities":
                #cost[card.card_color] = cost.get(card.card_color, 0) + card.card_cost
                continue
            else:
                print(cost)
                cost[card.card_color] = cost.get(card.card_color, 0) + (card.house_cost * card.houses) + card.card_cost
        while (flag):
            print(self.cards)
            cost_value = sorted(cost.items(), key=operator.itemgetter(1))[len(cost)-1][0]
            print("ghddfeie")
            print(cost_value, "max after")
            if cost_value == "Brown" or cost_value == "Deep Blue":
                if no_houses[cost_value] == 10:
                    if len(cost_value) == 1:
                        flag = False
                        print("cANNOT BUY A HOUSE FOR A MAX LISTING")
                        return cost_value
                    del cost[cost_value]
                else:
                    flag = False
            elif cost_value == "Green" or cost_value == "Blue" or cost_value == "Yellow" or cost_value == "Purple" or cost_value == "Red" or cost_value == "Orange":
                if no_houses[cost_value] == 15:
                    if len(cost_value) == 1:
                        flag = False
                        print("cANNOT BUY A HOUSE FOR A MAX LISTING")
                        return cost_value
                    del cost[cost_value]
                else:
                    flag = False
        return cost_value

    '''
        # Checks if there is a set
        # @param: self
        '''
    def card_color_owned(self):
        color_list = [card.card_color for card in self.cards]
        return list(set(color_list))

    '''
        # Gives total value of properties
        # @param: self
        '''
    def total_value(self):
        cost = {}
        for card in self.cards:
            if card.card_color == "Railroad" or card.card_color == "Utilities":
                cost[card.card_color] = cost.get(card.card_color, 0) + card.card_cost
                continue
            else:
                print(cost)
                cost[card.card_color] = cost.get(card.card_color, 0) + (card.house_cost * card.houses) + card.card_cost
        cost_value = max(cost.keys())
        return cost_value

    '''
        # Returns the card for the specfic set
        # @param: self
        # @param: color String
        '''
    def selected_card_group(self, color):
        cards = []
        for card in self.cards:
            if color == card.card_color:
                cards.append(card)
        return cards

    '''
        #Sells the card mortgaged card if it is called, wont sell a card which is already mortgaged
        # @param: self
        # @param: selected_card
    '''
    def mortgage_card(self, selected_card):
        # token.display_player_properties()
        check_houses = self.check_houses()
        if check_houses[selected_card.card_color] > 0:
            print("You cannot mortgage ", selected_card.card_color, " as the group has houses")
        elif selected_card.mortgage == True:
            print("You cannot mortgage a property again")
        elif selected_card.mortgage == False and check_houses[selected_card.card_color] == 0:
            print("You are eligble to mortgage the card")
            selected_card.mortgage = True
            bk.bank_creations.reduce_banks_money(bank_player, self.give_money((int(selected_card.card_cost * 0.5))),self)
            #self.give_money((int(selected_card.card_cost * 0.5)))


    def sell(self, amount,bank_player):
        #print(len(self.cards))
        flag = True
        while(flag):
            self.display_player_properties()
            check_houses = self.check_houses()
            if len(self.cards) == 0 and self.money <= amount:
                self.bankrupt_player()
                print("-------")
                flag = False
                return self.money
            # elif len(token.cards) == 0 and token.money > -1:
            # print("You do not own any properties")
            else:
                if self.probability > 0:
                    key = self.total_value()
                    if check_houses[key] > 0:
                        print(key)
                        print("asasjwq")
                        self.sell_house(key)
                    else:
                        print("AI IN THE HOUSE")
                        list_of_cards = self.selected_card_group(key)
                        pick = random.randint(0, (len(list_of_cards) - 1))
                        if list_of_cards[pick].card_color == "Railroad":
                            if list_of_cards[pick].mortgage == True:
                                bk.bank_creations.reduce_banks_money(bank_player, self.give_money(list_of_cards[pick].card_cost * 0.5),self)
                                #self.give_money(list_of_cards[pick].card_cost * 0.5)
                                list_of_cards[pick].mortgage = False
                                self.cards[(self.cards.index(list_of_cards[pick]))].card_owners = "Bank"
                                self.cards.pop(self.cards.index(list_of_cards[pick]))
                            else:
                                bk.bank_creations.reduce_banks_money(bank_player, self.give_money(list_of_cards[pick].card_cost),self)
                                #self.give_money(list_of_cards[pick].card_cost)
                                self.cards[(self.cards.index(list_of_cards[pick]))].card_owners = "Bank"
                                self.cards.pop(self.cards.index(list_of_cards[pick]))
                            self.stations -= 1
                        elif list_of_cards[pick].card_color == "Utilities":
                            if list_of_cards[pick].mortgage == True:
                                bk.bank_creations.reduce_banks_money(bank_player, self.give_money(list_of_cards[pick].card_cost * 0.5),self)
                                #self.give_money(list_of_cards[pick].card_cost * 0.5)
                                list_of_cards[pick].mortgage = False
                                self.cards[(self.cards.index(list_of_cards[pick]))].card_owners = "Bank"
                                self.cards.pop(self.cards.index(list_of_cards[pick]))
                            else:
                                bk.bank_creations.reduce_banks_money(bank_player, self.give_money(list_of_cards[pick].card_cost),self)
                                #self.give_money(list_of_cards[pick].card_cost)
                                self.cards[(self.cards.index(list_of_cards[pick]))].card_owners = "Bank"
                                self.cards.pop(self.cards.index(list_of_cards[pick]))
                            self.utlity -= 1
                        elif list_of_cards[pick].mortgage == True:
                            bk.bank_creations.reduce_banks_money(bank_player, self.give_money(list_of_cards[pick].card_cost * 0.5), self)
                            #self.give_money(list_of_cards[pick].card_cost * 0.5)
                            list_of_cards[pick].mortgage = False
                            self.cards[(self.cards.index(list_of_cards[pick]))].card_owners = "Bank"
                            self.cards.pop(self.cards.index(list_of_cards[pick]))
                        elif list_of_cards[pick].mortgage == False:
                            bk.bank_creations.reduce_banks_money(bank_player, self.give_money(list_of_cards[pick].card_cost), self)
                            #self.give_money(list_of_cards[pick].card_cost)
                            self.cards[(self.cards.index(list_of_cards[pick]))].card_owners = "Bank"
                            self.cards.pop(self.cards.index(list_of_cards[pick]))
            if self.money >= amount:
                flag = False
                return amount
            elif self.money < amount and len(self.cards) == 0:
                flag = False
                self.bankrupt_player()
                return self.money

    '''
        #Sells the card mortgaged card if it is called, wont sell a card which is already mortgaged
        # @param: self
        # @param: selected
    '''
    def sell_house(self, select):
        card_list, mydict = self.check_set()
        if len(card_list) > 0:
            flag = False
            temp = 0
            if (select == "Brown" or select == "Deep Blue" and (select in card_list)):
                for specfic_card in mydict[select]:
                    #print(mydict[select][0], mydict[select][1], "sccccccccc")
                    index_max = max(self.cards.index(mydict[select][0]), self.cards.index(mydict[select][1]))
                    if specfic_card.houses == 0:
                        print("You have reached the limited amount of properties")
                    elif specfic_card.houses >= self.cards[index_max].houses:
                        print("To sell a house in,", specfic_card.card_name, " will cost", specfic_card.house_cost)
                        if self.probability > 0:
                            num = np.random.uniform(low=0, high=1.1)
                            if self.probability <= num:
                                sell = "y"
                            else:
                                sell = "n"
                        else:
                            sell = input("Press y to sell a house or n to skip")
                        if sell == "y":
                            bk.bank_creations.reduce_banks_money(bank_player, self.give_money(specfic_card.house_cost),self)
                            #self.give_money(specfic_card.house_cost)
                            specfic_card.houses -= 1
                            if flag:
                                index_temp = self.cards.index(temp)
                                self.cards[index_temp] = self.cards[index_max]
                                self.cards[index_max] = temp
                                flag = False
                        else:
                            temp = specfic_card
                            flag = True
                    else:
                        print(specfic_card.card_name,
                                  " currently owns more houses than the rest, please sell a house for the others")
            elif (select == "Green" or select == "Blue" or select == "Yellow" or select == "Purple" and (select in card_list)):
                for specfic_card in mydict[select]:
                    #print(specfic_card, "sccccccccc")
                    index_max = max(self.cards.index(mydict[select][0]), self.cards.index(mydict[select][1]),
                                    self.cards.index(mydict[select][2]))
                    if specfic_card.houses == 0:
                        print("You have reached the limited amount of properties")
                    elif specfic_card.houses >= self.cards[index_max].houses:
                        print("To sell a house in,", specfic_card.card_name, " will cost", specfic_card.house_cost)
                        if self.probability > 0:
                            num = np.random.uniform(low=0, high=1.1)
                            if self.probability <= num:
                                sell = "y"
                            else:
                                sell = "n"
                        else:
                            sell = input("Press y to sell a house or n to skip")
                        if sell == "y":
                            bk.bank_creations.reduce_banks_money(bank_player, self.give_money(specfic_card.house_cost),self)
                            specfic_card.houses -= 1
                            if flag:
                                index_temp = self.cards.index(temp)
                                self.cards[index_temp] = self.cards[index_max]
                                self.cards[index_max] = temp
                                flag = False
                        else:
                            temp = specfic_card
                            flag = True
                    else:
                        print(specfic_card.card_name,
                                  " currently owns more houses than the rest, please buy a house for the others")
            else:
                print("You do own a set of", select)
        else:
            print("You do not have a set")

    '''
        #Checks what cards other plays has, used for the AI to buy a card to make other players lose
        # @param: self
        # @param: player_list -> list
    '''
    def play_list_cards(self, player_list):
        count = {"Blue": 0, "Red": 0, "Yellow": 0, "Deep Blue": 0, "Green": 0, "Brown": 0, "Purple": 0, "Railroad": 0,
                 "Utilities": 0, "Orange":0}
        your_cards = {"Blue": 0, "Red": 0, "Yellow": 0, "Deep Blue": 0, "Green": 0, "Brown": 0, "Purple": 0,
                      "Railroad": 0, "Utilities": 0, "Orange":0}
        for player in player_list:
            if len(player.cards) == 0:
                continue
            elif player.probability == 0:
                for card in player.cards:
                    count[card.card_color] = count.get(card.card_color, 0) + 1
            elif player.probability > 0:
                for card in player.cards:
                    your_cards[card.card_color] = your_cards.get(card.card_color, 0) + 1
        return count, your_cards


    def get_player_banker(self):
        return bank_player

    def move_from_special_card(self, plist, dice):
        #self.move_player(gb[self.position], dice)
        self.check_card(gb[self.position], plist, dice,self.probability)


    def max_index(self, cards):
        index = []
        house_no = []
        for card in cards:
            index.append(self.cards.index(card))
            house_no.append(card.houses)
        smallest_index = house_no.index(min(house_no))
        print(index[smallest_index], house_no[smallest_index])
        return smallest_index


    def min_index(self, cards):
        index = []
        house_no = []
        for card in cards:
            index.append(self.cards.index(card))
            house_no.append(card.houses)
        smallest_index = house_no.index(max(house_no))
        print(index[smallest_index], house_no[smallest_index])
        return smallest_index

    def cards_available(self):
        cards = {}
        if len(self.cards) == 0:
            return 0
        else:
            for c in self.cards:
                cards.setdefault(c.card_color, []).append(c)
        print(cards)
        return cards


class Text:
    def __init__(self, x, y, color, font, size):
        self.x = x
        self.y = y
        self.color = color
        self.font = font
        self.size = size

    def create_message(self, screen, message):
        font_name = pygame.font.Font(self.font, self.size)
        text = font_name.render(message, False, self.color, None)
        #rect = text.get_rect()
        screen.blit(text, [self.x, self.y])

class option:
    def __init__(self, rect, x, y):
        self.rect = rect
        self.x = x
        self.y = y
        self.done = False

    def draw_screen(self):
        " Draw the rect on the screen "
        self.rect.draw()

    def draw_text(self, screen, text, x, y, size):
        words = Text(x, y, (255, 255, 255), pygame.font.get_default_font(), size)
        words.create_message(screen, text)

    def is_done(self):
        if self.done:
            return True
        return False

    def set_done(self, isdone):
        self.done = isdone

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y