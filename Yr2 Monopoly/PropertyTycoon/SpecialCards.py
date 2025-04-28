import SpecialCardFunctions as s
from BoardDefinition import game_board
import numpy as np
import Bank as bk
gb = game_board()

class special_cards:
    def __init__(self, card_name, statement, function, decision):
        self.card_name = card_name
        self.statement = statement
        self.function = function
        self.decision = decision
    #Add housing later when i add the housing function

    '''
        #picks a card based on statement, and uses the function which helps us find out what the card is meant to do 
        # @param: token -> player
        # @param: plist -> list
        # @param: total -> Int
        # @param: choice -> String
    '''
    def card_usage(self, token,plist,total,choice):
        flag = False
        x = self.statement
        print(self.statement)
        if self.function == "G":
            token.give_money(self.decision)
        elif self.function == "P":
            gb[20].rent += token.deduct_money(self.decision)
        elif self.function == "M":
            #Need to check the card after moving
            if self.decision < 0:
                token.position -= self.decision
                print(token.position)
            else:
                print(token.position)
                #token.check_card(gb[token.position], plist, total, token.probability)
                token.position = self.decision
                print(token.position)
            #token.move_from_special_card(plist, total)
            print("DJJ")
            #might use gb[token.move(total)] instead
            flag = True
        elif self.function == "C":
            if token.probability > 0:
                choice = "n"
                x = np.random.uniform(low=0, high=token.probability +  0.1)
                if x <= token.probability:
                    choice = "y"
            else:
                if choice == "y":
                    gb[20].rent += token.deduct_money(self.decision)
                else:
                    #Need to change this
                    s.pick_knock(token,plist,total,0)
        #Check if this works
        elif self.function == "KJ":
            token.stored_jail_cards.append(self)
            s.knocks.remove(self)
            token.knock_jail_pass = self.decision
        elif self.function == "PJ":
            token.stored_jail_cards.append(self)
            s.pot.remove(self)
            token.pot_jail_pass = self.decision
        elif self.function == "J":
            token.in_jail = True
            token.position = self.decision
        elif self.function == "SM":
            print(token.position, "xspas")
            if token.position > self.decision:
                print("You have passed go and received $200")
                token.position = self.decision
                bk.bank_creations.reduce_banks_money(token.get_player_banker(), 200, token)
                token.give_money(200)
                print(token.position, "assaaaa")
                #token.check_card(gb[token.position], plist, total, token.probability)

            else:
                token.position = self.decision
                print(token.position, "assaaaa")
            #token.move_from_special_card(plist, total)

        if self.card_name == "Pot":
            s.pot.remove(self)
            s.pot.append(self)

        elif self.card_name == "Knocks":
            s.knocks.remove(self)
            s.knocks.append(self)

