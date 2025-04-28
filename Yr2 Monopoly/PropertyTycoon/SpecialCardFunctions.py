import SpecialCards as s
import pygame
import random

'''
    #Shffule 
    # @param: pot -> list
'''
def shuffle_pot(pot):
    random.shuffle(pot)
    return pot

'''
    #Shffule 
    # @param: pot -> list
'''
def shuffle_knocks(knocks):
    random.shuffle(knocks)
    return knocks
'''
    #Returns an image absed on the string
    # @param: Sentence -> String
'''
def pot_luck_draw_img(sentence):
    pot1 = pygame.image.load('resources/pot_luck/pot1.png').convert_alpha()
    pot2 = pygame.image.load('resources/pot_luck/pot2.png').convert_alpha()
    pot3 = pygame.image.load('resources/pot_luck/pot3.png').convert_alpha()
    pot4 = pygame.image.load('resources/pot_luck/pot4.png').convert_alpha()
    pot5 = pygame.image.load('resources/pot_luck/pot5.png').convert_alpha()
    pot6 = (pygame.image.load('resources/pot_luck/pot6.png').convert_alpha())
    pot7 = (pygame.image.load('resources/pot_luck/pot7.png').convert_alpha())
    pot8 = (pygame.image.load('resources/pot_luck/pot8.png').convert_alpha())
    pot9 = (pygame.image.load('resources/pot_luck/pot9.png').convert_alpha())
    pot10 = (pygame.image.load('resources/pot_luck/pot10.png').convert_alpha())
    pot11 = (pygame.image.load('resources/pot_luck/pot11.png').convert_alpha())
    pot12 = (pygame.image.load('resources/pot_luck/pot12.png').convert_alpha())
    pot13 = (pygame.image.load('resources/pot_luck/pot13.png').convert_alpha())
    pot14 = (pygame.image.load('resources/pot_luck/pot14.png').convert_alpha())
    pot15 = (pygame.image.load('resources/pot_luck/pot15.png').convert_alpha())
    pot16 = (pygame.image.load('resources/pot_luck/pot16.png').convert_alpha())
    pot17 = (pygame.image.load('resources/pot_luck/pot17.png').convert_alpha())

    img_list = [(pot1, "You inherit £200"), (pot2, "You have won 2nd prize in a beauty contest, collect £50"),
                (pot3, "You are up the creek with no paddle - go back to the Old Creek"),
                (pot4, "Student loan refund collect £20"), (pot5, "Bank error in your favour collect £200"),
                (pot6, "Pay bill for text books of £100"),
                (pot7, "Mega late night taxi bill pay £50"),
                (pot8, "Advance to go"), (pot9, "From sale of Bitcoin you get £50"),
                (pot10, "Bitcoin assets fall - pay off Bitcoin short fall"),
                (pot11, "Pay a £10 fine or take opportunity knocks"), (pot12, "Pay insurance fee of £50"),
                (pot13, "Savings bond matures, collect £100"), (pot14, "Go to jail. Do not pass GO, do not collect £200"),
                (pot15, "Received interest on shares of £25"), (pot16, "It's your birthday. Collect £10 from each player"),
                (pot17, "Get out of jail free")]

    for i in range(len(img_list)):
        if img_list[i][1] == sentence:
            return img_list[i][0]
'''
    Returns the card
    P for paying 
    G for giving money
    #M to move
    #SM move with 200 bounus 
    #J for jail 
    #PJ for pot pass jail
'''
def potluck_draw():
    inherit = s.special_cards("Pot", "You inherit £200", "G", 200)
    beauty = s.special_cards("Pot", "You have won 2nd prize in a beauty contest, collect £50", "G", 50)
    move_to_creek = s.special_cards("Pot", "You are up the creek with no paddle - go back to the Old Creek", "M", 1)
    loan = s.special_cards("Pot", "Student loan refund collect £20", "G", 20)
    bank_error = s.special_cards("Pot", "Bank error in your favour collect £200", "G", 200)
    pay_bill = s.special_cards("Pot", "Pay bill for text books of £100", "P", 100)
    tax_bill = s.special_cards("Pot", "Mega late night taxi bill pay £50", "P", 50)
    move_to_go = s.special_cards("Pot", "Advance to go", "M", 0)
    sale_bitcoin = s.special_cards("Pot", "From sale of Bitcoin you get £50", "G", 50)
    bitcoin_fail = s.special_cards("Pot", "Bitcoin assets fall - pay off Bitcoin short fall", "P", 50)  # change
    choice = s.special_cards("Pot", "Pay a £10 fine or take opportunity knocks", "C", 10)
    insurance = s.special_cards("Pot", "Pay insurance fee of £50", "P", 50)
    bonds = s.special_cards("Pot", "Savings bond matures, collect £100", "G", 100)
    jail = s.special_cards("Pot", "Go to jail. Do not pass GO, do not collect £200", "J", 10)
    shares = s.special_cards("Pot", "Received interest on shares of £25", "G", 25)
    birthday = s.special_cards("Pot", "It's your birthday. Collect £10 from each player", "B", 10)
    free_jail_pass = s.special_cards("Jail_Pot", "Get out of jail free", "PJ", True)
    pot = [inherit,
           beauty,
           move_to_creek,
           loan,
           bank_error,
           pay_bill,
           tax_bill,
           move_to_go,
           sale_bitcoin,
           bitcoin_fail,
           choice,
           insurance,
           bonds,
           jail,
           shares,
           birthday,
           free_jail_pass]
    return pot
'''
    #Returns an image based on the string
    # @param: sentences -> String
'''
def opportunity_knocks_draw_img(sentence):
    knocks1 = pygame.image.load('resources/opportunity_knocks/knocks1.png').convert_alpha()
    knocks2 = pygame.image.load('resources/opportunity_knocks/knocks2.png').convert_alpha()
    knocks3 = pygame.image.load('resources/opportunity_knocks/knocks3.png').convert_alpha()
    knocks4 = pygame.image.load('resources/opportunity_knocks/knocks4.png').convert_alpha()
    knocks5 = pygame.image.load('resources/opportunity_knocks/knocks5.png').convert_alpha()
    knocks6 = (pygame.image.load('resources/opportunity_knocks/knocks6.png').convert_alpha())
    knocks7 = (pygame.image.load('resources/opportunity_knocks/knocks7.png').convert_alpha())
    knocks8 = (pygame.image.load('resources/opportunity_knocks/knocks8.png').convert_alpha())
    knocks9 = (pygame.image.load('resources/opportunity_knocks/knocks9.png').convert_alpha())
    knocks10 = (pygame.image.load('resources/opportunity_knocks/knocks10.png').convert_alpha())
    knocks11 = (pygame.image.load('resources/opportunity_knocks/knocks11.png').convert_alpha())
    knocks12 = (pygame.image.load('resources/opportunity_knocks/knocks12.png').convert_alpha())
    knocks13 = (pygame.image.load('resources/opportunity_knocks/knocks13.png').convert_alpha())
    knocks14 = (pygame.image.load('resources/opportunity_knocks/knocks14.png').convert_alpha())
    knocks15 = (pygame.image.load('resources/opportunity_knocks/knocks15.png').convert_alpha())
    knocks16 = (pygame.image.load('resources/opportunity_knocks/knocks16.png').convert_alpha())

    img_list = [(knocks1, "Bank pays you dividend of £50"), (knocks2, "You have won a lip sync battle. Collect £100"),
                (knocks3, "Advance to Turing Heights"),
                (knocks4, "Advance to Han Xin Gardens. If you pass GO, collect £200"),
                (knocks5, "Fined £15 for speeding"), (knocks6, "Pay university fees of £150"),
                (knocks7, "Take a trip to Hove station. If you pass GO, collect £200"),
                (knocks8, "Loan matures, collect £150"),
                (knocks9, "You are assessed for repairs, £40/house, £115/hotel"),
                (knocks10, "Advance to go"), (knocks11, "You are assessed for repairs, £25/house, £100/hotel"),
                (knocks12, "Go back 3 spaces"), (knocks13, "Advance to Skywalker Dive. If you pass GO, collect £200"),
                (knocks14, "Go to jail. Do not pass GO, do not collect £200"),
                (knocks15, "Drunk in charge of a hoverboard. Fine £30"),
                (knocks16, "Get out of jail free")]

    for i in range(len(img_list)):
        if img_list[i][1] == sentence:
            return img_list[i][0]
'''
    Returns the card
    H for paying house
    KJ for free jail pass
'''
def opportunity_knocks_draw():
    pay_bank = s.special_cards("Knocks","Bank pays you dividend of £50", "G", 50)
    won = s.special_cards("Knocks","You have won a lip sync battle. Collect £100", "G", 100)
    move_to_turing_heights = s.special_cards("Knocks","Advance to Turing Heights", "M", 39)
    move_to_han_xin = s.special_cards("Knocks","Advance to Han Xin Gardens. If you pass GO, collect £200", "SM", 24)
    fine = s.special_cards("Knocks","Fined £15 for speeding", "P", 15)
    pay_uni = s.special_cards("Knocks","Pay university fees of £150", "P", 150)
    hove_station = s.special_cards("Knocks","Take a trip to Hove station. If you pass GO, collect £200", "SM", 15)
    loan_matures = s.special_cards("Knocks","Loan matures, collect £150", "G", 150)
    assessed_repairs_expensive = s.special_cards("Knocks","You are assessed for repairs, £40/house, £115/hotel", "H", (40, 115))
    move_to_go = s.special_cards("Knocks","Advance to go", "M", 0)
    assessed_repairs_cheap = s.special_cards("Knocks","You are assessed for repairs, £25/house, £100/hotel", "H", (25, 100))
    go_back = s.special_cards("Knocks","Go back 3 spaces", "M", -3)
    move_to_skywalker_dive = s.special_cards("Knocks","Advance to Skywalker Dive. If you pass GO, collect £200", "SM", 11)
    jail = s.special_cards("Knocks","Go to jail. Do not pass GO, do not collect £200", "J", 10)
    drunk = s.special_cards("Knocks","Drunk in charge of a hoverboard. Fine £30", "P", 30)
    free_jail_pass = s.special_cards("Jail_Knocks","Get out of jail free", "KJ", True)

    opportunity_knocks = [pay_bank,
                          won,
                          move_to_turing_heights,
                          move_to_han_xin,
                          fine,
                          pay_uni,
                          hove_station,
                          loan_matures,
                          assessed_repairs_expensive,
                          move_to_go,
                          assessed_repairs_cheap,
                          go_back,
                          move_to_skywalker_dive,
                          jail,
                          drunk,
                          free_jail_pass]

    return opportunity_knocks


pot = shuffle_pot(potluck_draw())
knocks = shuffle_knocks(opportunity_knocks_draw())

'''
    #Picks a pot card
    # @param: token -> player
    # @param: player_list -> list
    # @param: total -> int
    # @param choice -> string
'''
def pick_pot(token, plist, total, choice):
    s.special_cards.card_usage(pot[0], token, plist, total, choice)

'''
    #Picks a knocks card
    # @param: token -> player
    # @param: player_list -> list
    # @param: total -> int
    # @param choice -> string
'''
def pick_knock(token, plist, total, choice):
    s.special_cards.card_usage(knocks[0], token, plist, total, choice)

