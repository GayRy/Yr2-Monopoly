import numpy as np
import AI as ai
import Bank as bk

bank = ""


class card:
    def __init__(self, card_name, card_color, card_cost, house_cost, card_owner, rent, houses, mortgage, img_index):
        self.card_name = card_name
        self.card_color = card_color
        self.house_cost = house_cost
        self.card_cost = card_cost
        self.card_owner = card_owner
        self.rent = rent
        self.houses = houses
        self.mortgage = mortgage
        self.img_index = img_index

    '''
    Buying the card, if auction price is bigger than 0 then we know the player came fromm the auction function
    Used to buy cards
    # @param: token -> player
    # @param: auction_price -> INT
    # @param: player_list -> List
    # @param banker -> Banker
    '''

    def buy_card(self, token, auction_price, player_list, banker):
        global bank
        bank = banker
        if auction_price > 0:
            bk.bank_creations.add_bank_money(bank, token.deduct_money(auction_price), token)
            self.card_owner = token.player
            token.cards.append(self)
            if self.card_color == "Railroad":
                token.stations += 1
            print(self.card_name, "This cards current owners is", self.card_owner, "currently spent:", auction_price,
                  "current\n balance:", token.money)
            if self.card_color == "Utilities":
                token.utlity += 1
                print(self.card_name, "This cards current owners is", self.card_owner, "currently spent:",
                      auction_price, "current\n balance:", token.money)
        else:
            if int(self.card_cost) > int(token.money):
                print('You are to broke to buy this card', self.card_name)
                token.sell(0, 0)
            else:
                if token.probability > 0:
                    player_cards, your_cards = token.play_list_cards(player_list)
                    print(player_cards)
                    flag = False
                    if your_cards[self.card_color] >= 1:
                        x = np.random.uniform(low=0, high=token.probability + your_cards[self.card_color] * 0.1)
                        if token.probability <= x:
                            if token.probability <= x:
                                if token.money - self.card_cost >= 0:
                                    flag = True
                    elif player_cards[self.card_color] == 1:
                        x = np.random.uniform(low=0, high=token.probability + 0.2)
                        if token.probability <= x:
                            if token.money - self.card_cost >= 0:
                                flag = True
                    elif player_cards[self.card_color] == 2:
                        x = np.random.uniform(low=0, high=token.probability + 0.1)
                        if token.probability <= x:
                            if token.money - self.card_cost >= 0:
                                flag = True
                    elif player_cards[self.card_color] == 0:
                        x = np.random.uniform(low=0, high=1)
                        if token.probability <= x:
                            if token.money - self.card_cost >= 0:
                                flag = True
                    if flag == True:
                        bk.bank_creations.add_bank_money(bank, token.deduct_money(self.card_cost), token)
                        self.card_owner = token.player
                        if self.card_color == "Railroad":
                            token.stations += 1
                        elif self.card_color == "Utilities":
                            token.utlity += 1
                        token.cards.append(self)
                        print(self.card_name, "This cards current owners is", self.card_owner, "currently spent:",
                              self.card_cost,
                              "current\n balance:", token.money)
                else:
                    bk.bank_creations.add_bank_money(bank, token.deduct_money(self.card_cost), token)
                    self.card_owner = token.player
                    if self.card_color == "Railroad":
                        token.stations += 1
                    elif self.card_color == "Utilities":
                        token.utlity += 1
                    token.cards.append(self)
                    print(self.card_name, "This cards current owners is", self.card_owner, "currently spent:",
                          self.card_cost, "current\n balance:", token.money)

    '''
    Buying the card houses by finding which card has the lowest number of houses so it increases by 1 house for each card
    Used to buy cards
    # @param: token -> player
    # @param banker -> Banker
    '''

    def buy_houses(self, token, banker):
        print(token.check_set())
        x = np.random.uniform(low=0, high=1.1)
        card_list, mydict = token.check_set()
        check_mortgage = token.check_mortgage()
        if len(card_list) > 0:
            print("Select a card from the given", card_list)
            if token.probability > 0:
                select = token.total_property_cost()
            else:
                select = input("input:")
            print(select)
            flag = False
            temp = 0
            print(check_mortgage.keys())
            if select not in check_mortgage.keys():
                if (select == "Brown" or select == "Deep Blue" and (select in card_list)):
                    print(mydict[select])
                    for specfic_card in mydict[select]:
                        index_max = max(token.cards.index(mydict[select][0]), token.cards.index(mydict[select][1]))
                        if specfic_card.houses == 5:
                            print("You have reached max amount of properties")
                        elif specfic_card.houses <= token.cards[index_max].houses:
                            print("To buy a house in,", specfic_card.card_name, " will cost", specfic_card.house_cost)
                            if token.money >= specfic_card.house_cost:
                                if token.probability > 0:
                                    if token.probability >= x:
                                        buy = "y"
                                    else:
                                        buy = "n"
                                else:
                                    buy = input("Press y to buy a house or n to skip")
                                if buy == "y":
                                    print("AI BUY HOUSE")
                                    # token.deduct_money(specfic_card.house_cost)
                                    bk.bank_creations.add_bank_money(bank, token.deduct_money(specfic_card.house_cost),
                                                                     token)
                                    specfic_card.houses += 1
                                    if flag:
                                        index_temp = token.cards.index(temp)
                                        token.cards[index_temp] = token.cards[index_max]
                                        token.cards[index_max] = temp
                                        flag = False
                                else:
                                    temp = specfic_card
                                    flag = True
                            else:
                                print("You cannot afford the house")
                                break
                        else:
                            print(specfic_card.card_name,
                                  " currently owns more houses than the rest, please buy a house for the others")
                elif (
                        select == "Green" or select == "Blue" or select == "Yellow" or select == "Purple" or select == "Orange" or select == "Red") and (
                        select in card_list):
                    print(mydict[select])
                    for specfic_card in mydict[select]:
                        index_max = max(token.cards.index(mydict[select][0]), token.cards.index(mydict[select][1]),
                                        token.cards.index(mydict[select][2]))
                        if specfic_card.houses == 5:
                            print("You have reached max amount of properties")
                        elif specfic_card.houses <= token.cards[index_max].houses:
                            print("To buy a house in,", specfic_card.card_name, " will cost", specfic_card.house_cost)
                            if token.money >= specfic_card.house_cost:
                                if token.probability > 0:
                                    if token.probability >= x:
                                        buy = "y"
                                        print("AI BUY HOUSE")
                                    else:
                                        buy = "n"
                                else:
                                    buy = input("Press y to buy a house or n to skip")
                                if buy == "y":
                                    bk.bank_creations.add_bank_money(banker,
                                                                     token.deduct_money(specfic_card.house_cost), token)
                                    specfic_card.houses += 1
                                    if flag:
                                        index_temp = token.cards.index(temp)
                                        token.cards[index_temp] = token.cards[index_max]
                                        token.cards[index_max] = temp
                                        flag = False
                                else:
                                    temp = specfic_card
                                    flag = True
                            else:
                                print("You cannot afford the house")
                                break
                        else:
                            print(specfic_card.card_name,
                                  " currently owns more houses than the rest, please buy a house for the others")
            else:
                print("You cannot buy properties for a mortgaged card")

    '''
    Used to pay the mortgage of a card if the card is mortgaged
    # @param: token -> player
    '''

    def pay_mortgage(self, token):
        mortgage = token.check_mortgage()
        if len(mortgage.keys()) > 0:
            for color, card in mortgage.items():
                count = 0
                for card_attributes in card:
                    print("card number", count, "card color", color, " has a mortgaged card ",
                          card_attributes.card_name)
                    count += 1
            select = input("Enter the card color you want")
            if select in mortgage.keys():
                number = input("Select the number for your card color group")
                if int(number) > len(mortgage[select]) - 1:
                    print("Invalid number")
                else:
                    payment = (mortgage[select][int(number)].card_cost * 0.5) + (
                                mortgage[select][int(number)].card_cost * 0.5) * 0.1
                    print("The selected card to unmortgage is ", mortgage[select][int(number)].card_name,
                          " you will need to pay", payment)
                    bk.bank_creations.add_bank_money(bank, token.deduct_money(payment), token)
                    mortgage[select][int(number)].mortgage = False
            else:
                print("You do not have a mortgage in this card color group")

    '''
    Used find out the price of landing of this function, if they have 1 card it is 4*the roll else 10*roll
    # @param: token2 -> player
    #dice -> Int
    '''

    def pay_utilities(self, token2, dice):
        print("Currently this card is owned by:", token2.player, " and currently owns:", token2.utlity, self.card_color)
        if token2.utlity == 1:
            pay = dice * 4
            return pay
        else:
            pay = dice * 10
            return pay

    '''
    Used find out the price of landing of this function
    # @param: token2 -> player
    '''

    def pay_railroads(self, token2):
        print(token2.stations)
        print("Currently ", self.card_owner, " owns", token2.stations, " railroads\n")
        number_of_stations_price = [25, 50, 100, 200]
        pay = number_of_stations_price[token2.stations - 1]
        return pay

    '''
    Used for payment
    # @param: token1 -> player
    # @param: token2 -> player
    # @param: pay -> Int
    '''

    def pay_player2(self, token1, token2, pay):
        print(self.card_name, "Is currently owned by:", self.card_owner)
        if token2.in_jail == True:
            print("Since", token2.player, " is in jail, ", token1.player, " does not need to pay")
        elif pay > 0:
            payment = token1.deduct_money(pay)
            token2.give_money(payment)

    '''
    Returns the payment amount for cards
    # @param: token1 -> player
    # @param: token2 -> player
    '''

    def check_payment_cost(self, token1, token2):
        set, mydic = token2.check_set()
        houses = token2.check_houses()
        if self.card_color in set and houses[self.card_color] == 0:
            print("Currently ", token2.player, " has a set of ", self.card_color, " with no houses")
            print(token1.player, " has to pay ", token2.player, self.rent[self.houses] * 2)
            # token1.deduct_money(self.rent[self.houses]*2)
            payment = token1.deduct_money(self.rent[self.houses] * 2)
            return payment
        else:
            payment = self.rent[self.houses]
            print("\n Currently the rent for", self.card_name, " is", payment)
            return payment
            # payment = token1.deduct_money(pay)
            # print(payment, "payment")
            # token2.give_money(payment)

    def boardpos(self, token, board):
        boardposition = board[token.position]
        print(token.player, "position is", boardposition)

    def ai_auction(self, token, plist, price, probability):
        old_price = price
        player_cards, your_cards = ai.play_list_cards(plist)
        print(player_cards)
        if your_cards[self.card_color] >= 1:
            x = np.random.uniform(low=0, high=probability + your_cards[self.card_color] * 0.2)
            if probability <= x:
                if (token.money - price) >= (token.money / len(plist)):
                    price += 10
        elif player_cards[self.card_color] == 1:
            x = np.random.uniform(low=0, high=probability + 0.2)
            if probability <= x:
                if (token.money - price) >= (token.money / len(plist)):
                    price += 10
        elif player_cards[self.card_color] == 2:
            x = np.random.uniform(low=0, high=probability + 0.1)
            if probability <= x:
                if (token.money - price) >= (token.money / len(plist)):
                    price += 10
        elif player_cards[self.card_color] == 0:
            x = np.random.uniform(low=0, high=1)
            if probability <= x:
                if (token.money - price) >= (token.money / len(plist)):
                    price += 10
        if price > old_price:
            return price
        return 0



