def mortgage_card(token, selected_card):
    # token.display_player_properties()
    check_houses = token.check_houses()
    if check_houses[selected_card.card_color] > 0:
        print("You cannot mortgage ", selected_card.card_color, " as the group has houses")
    elif selected_card.mortgage == True:
        print("You cannot mortgage a property again")
    elif selected_card.mortgage == False and check_houses[selected_card.card_color] == 0:
        print("You are eligble to mortgage the card")
        selected_card.mortgage = True
        token.give_money((int(selected_card.card_cost * 0.5)))
