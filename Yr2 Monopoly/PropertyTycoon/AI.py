import numpy as np

'''
For testing purposes
'''
def move_ai(ai, probability, player_list):
    roll = ai.dice_roll()
    print("AI rolled", roll)
    ai.move_player(sum(roll))
    return roll[0], roll[1]

def double_roll(ai, probability, player_list):
    if ai.in_jail is False and ai.bankrupt is False:
        count = 0
        flag = True
        while (flag):
            print("You rolled a double")
            roll = ai.dice_roll()
            count += 1
            if roll[0] == roll[1] and count == 2:
                ai.currently_in_jail()
                flag = False
            else:
                ai.move_player(sum(roll))
                ai.check_card(card, player_list, roll, probability)
                flag = False

def ai_buy(ai, probability, player_list, card):
    player_cards = play_list_cards(player_list)
    print(player_cards)
    flag = False
    if player_cards[card.card_color] == 1:
        x = np.random.uniform(low=0, high=probability+0.2)
        if probability <= x:
            if ai.money - card.card_cost >= 0:
                flag = True
    elif player_cards[card.card_color] == 2:
        x = np.random.uniform(low=0, high=probability+0.1)
        if probability <= x:
            if ai.money - card.card_cost >= 0:
                flag = True
    elif player_cards[card.card_color] == 0:
        x = np.random.uniform(low=0, high=1)
        if probability <= x:
            if ai.money - card.card_cost >= 0:
                flag = True
    if flag == True:
        ai.deduct_money(card.card_cost)
        card.card_owner = ai.player
        if card.card_color == "Railroad":
            ai.stations += 1
        elif card.card_color == "Utilities":
            ai.utlity += 1
        ai.cards.append(card)
        print(card.card_name, "This cards current owners is", card.card_owner, "currently spent:", card.card_cost,
              "current\n balance:", ai.money)

def play_list_cards(player_list):
    count = {"Blue":0, "Red":0, "Yellow":0, "Deep Blue":0, "Green":0, "Brown":0, "Purple":0, "Railroad":0, "Utilities":0}
    your_cards = {"Blue":0, "Red":0, "Yellow":0, "Deep Blue":0, "Green":0, "Brown":0, "Purple":0, "Railroad":0, "Utilities":0}
    for player in player_list:
        if len(player.cards) == 0:
            continue
        elif player.probability == 0:
            for card in player.cards:
                count[card.card_color] = count.get(card.card_color, 0) + 1
        elif player.probability > 0:
            for card in player.cards:
                your_cards[card.card_color] = your_cards.get(card.card_color, 0) + 1
    return count,your_cards

