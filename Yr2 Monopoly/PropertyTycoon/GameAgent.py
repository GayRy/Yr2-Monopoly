import pygame, sys
from pygame.locals import *
import PlayerFunctions as p
import Button
import Token
import PopUp
import random
import BoardDefinition as bd
import Bank as bk
import SpecialCardFunctions as SCF
import numpy as np

gb = bd.game_board()
mainClock = pygame.time.Clock()
pygame.init()
SCREEN_WIDTH = 1270
SCREEN_HEIGHT = 768
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
xcount = 0

# board map
MapXYvalue = [(903, 651), (827, 664), (772, 664), (714, 664), (659, 664), (602, 664), (543, 664), (486, 664), (429, 664), (370, 664), (293, 656),

                  (280, 576), (280, 519), (280, 463), (280, 406), (280, 348), (280, 291), (280, 234), (280, 177), (280, 120), (294, 44),

                  (372, 30), (427, 30), (484, 30), (541, 30), (598, 30), (658, 30), (714, 30), (722, 30), (829, 30), (907, 42),

                  (919, 120), (919, 177), (919, 234), (919, 291), (919, 348), (919, 405), (919, 462), (919, 519), (919, 576)
            ]

# background images
background = pygame.image.load('resources/backgrounds/GameStart.png')
menu_background = pygame.image.load('resources/backgrounds/menu.png')
board = pygame.image.load('resources/gameboard_assets/board_final.png')
about_page = pygame.image.load('resources/backgrounds/about_img.png').convert_alpha()
credits_background = pygame.image.load('resources/backgrounds/Credit.png')

# load button images
start_game = pygame.image.load('resources/buttons/button_start.png').convert_alpha()
start_game_hover = pygame.image.load('resources/buttons/button_start_hover.png').convert_alpha()
credits = pygame.image.load('resources/buttons/button_credits.png').convert_alpha()
credits_hover = pygame.image.load('resources/buttons/button_credits_hover.png').convert_alpha()
about = pygame.image.load('resources/buttons/button_about.png').convert_alpha()
about_hover = pygame.image.load('resources/buttons/button_about_hover.png').convert_alpha()
quit_game = pygame.image.load('resources/buttons/button_quit.png').convert_alpha()
quit_game_hover = pygame.image.load('resources/buttons/button_quit_hover.png').convert_alpha()

back = pygame.image.load('resources/buttons/button_back.png').convert_alpha()
back_hover = pygame.image.load('resources/buttons/button_back_hover.png').convert_alpha()
skip = pygame.image.load('resources/buttons/button_skip.png').convert_alpha()
skip_hover = pygame.image.load('resources/buttons/button_skip_hover.png').convert_alpha()

pvp = pygame.image.load('resources/buttons/pvp_button.png').convert_alpha()
pvp_hover = pygame.image.load('resources/buttons/pvp_button_hover.png').convert_alpha()

pve = pygame.image.load('resources/buttons/pve_button.png').convert_alpha()
pve_hover = pygame.image.load('resources/buttons/pve_button_hover.png').convert_alpha()

select_player = pygame.image.load('resources/buttons/button_select-player.png').convert_alpha()
select_player_hover = pygame.image.load('resources/buttons/button_select-player_hover.png').convert_alpha()
select_ai = pygame.image.load('resources/buttons/button_select-ai.png').convert_alpha()
select_ai_hover = pygame.image.load('resources/buttons/button_select-ai_hover.png').convert_alpha()
winner_background = pygame.image.load('resources/backgrounds/winner.png').convert_alpha()
game_mode = pygame.image.load('resources/buttons/button_game-modes.png').convert_alpha()
game_mode_hover = pygame.image.load('resources/buttons/button_game-modes_hover.png').convert_alpha()
normal = pygame.image.load('resources/buttons/button_normal.png').convert_alpha()
timed_mode = pygame.image.load('resources/buttons/button_timed-mode.png').convert_alpha()
play_game_mode = pygame.image.load('resources/buttons/button_play_game.png').convert_alpha()

play_game = pygame.image.load('resources/buttons/button_play.png').convert_alpha()
play_game_hover = pygame.image.load('resources/buttons/button_play_hover.png').convert_alpha()
yes = pygame.image.load('resources/buttons/button_yes.png').convert_alpha()
yes_hover = pygame.image.load('resources/buttons/button_yes_hover.png').convert_alpha()
no = pygame.image.load('resources/buttons/button_no.png').convert_alpha()
no_hover = pygame.image.load('resources/buttons/button_no_hover.png').convert_alpha()
buy = pygame.image.load('resources/buttons/button_buy.png').convert_alpha()
buy_hover = pygame.image.load('resources/buttons/button_buy_hover.png').convert_alpha()
sell = pygame.image.load('resources/buttons/button_sell.png').convert_alpha()
sell_hover = pygame.image.load('resources/buttons/button_sell_hover.png').convert_alpha()
cancel = pygame.image.load('resources/buttons/button_cancel.png').convert_alpha()
cancel_hover = pygame.image.load('resources/buttons/button_cancel_hover.png').convert_alpha()
ok = pygame.image.load('resources/buttons/button_ok.png').convert_alpha()
ok_hover = pygame.image.load('resources/buttons/button_ok_hover.png').convert_alpha()
bankrupt = pygame.image.load('resources/buttons/button_bankrupt.png').convert_alpha()
bankrupt_hover = pygame.image.load('resources/buttons/button_bankrupt_hover.png').convert_alpha()
pay = pygame.image.load('resources/buttons/button_pay.png').convert_alpha()
pay_hover = pygame.image.load('resources/buttons/button_pay_hover.png').convert_alpha()
pay_red_hover = pygame.image.load('resources/buttons/button_pay_red_hover.png').convert_alpha()

ten = pygame.image.load('resources/buttons/button_10.png').convert_alpha()
ten_hover = pygame.image.load('resources/buttons/button_10_hover.png').convert_alpha()
fifty = pygame.image.load('resources/buttons/button_50.png').convert_alpha()
fifty_hover = pygame.image.load('resources/buttons/button_50_hover.png').convert_alpha()
hundered = pygame.image.load('resources/buttons/button_100.png').convert_alpha()
hundered_hover = pygame.image.load('resources/buttons/button_100_hover.png').convert_alpha()

wait_till_release = pygame.image.load('resources/buttons/button_wait-till-release.png').convert_alpha()
wait_till_release_hover = pygame.image.load('resources/buttons/button_wait-till-release_hover.png').convert_alpha()
cards_owned = pygame.image.load('resources/buttons/button_cards-owned.png').convert_alpha()
cards_owned_hover = pygame.image.load('resources/buttons/button_cards-owned_hover.png').convert_alpha()

buy_house = pygame.image.load('resources/buttons/button_buy-house.png').convert_alpha()
buy_house_hover = pygame.image.load('resources/buttons/button_buy-house_hover.png').convert_alpha()
sell_house = pygame.image.load('resources/buttons/button_sell-house.png').convert_alpha()
sell_house_hover = pygame.image.load('resources/buttons/button_sell-house_hover.png').convert_alpha()

red = pygame.image.load('resources/buttons/button_red.png').convert_alpha()
red_hover = pygame.image.load('resources/buttons/button_red_hover.png').convert_alpha()
yellow = pygame.image.load('resources/buttons/button_yellow.png').convert_alpha()
yellow_hover = pygame.image.load('resources/buttons/button_yellow_hover.png').convert_alpha()
green = pygame.image.load('resources/buttons/button_green.png').convert_alpha()
green_hover = pygame.image.load('resources/buttons/button_green_hover.png').convert_alpha()
orange = pygame.image.load('resources/buttons/button_orange.png').convert_alpha()
orange_hover = pygame.image.load('resources/buttons/button_orange_hover.png').convert_alpha()
brown = pygame.image.load('resources/buttons/button_brown.png').convert_alpha()
brown_hover = pygame.image.load('resources/buttons/button_brown_hover.png').convert_alpha()
blue = pygame.image.load('resources/buttons/button_blue.png').convert_alpha()
blue_hover = pygame.image.load('resources/buttons/button_blue_hover.png').convert_alpha()
deep_blue = pygame.image.load('resources/buttons/button_deep-blue.png').convert_alpha()
deep_blue_hover = pygame.image.load('resources/buttons/button_deep-blue_hover.png').convert_alpha()
purple = pygame.image.load('resources/buttons/button_purple.png').convert_alpha()
purple_hover = pygame.image.load('resources/buttons/button_purple_hover.png').convert_alpha()

railroad = pygame.image.load('resources/buttons/button_railroad.png').convert_alpha()
railroad_hover = pygame.image.load('resources/buttons/button_railroad_hover.png').convert_alpha()
utilities = pygame.image.load('resources/buttons/button_utilities.png').convert_alpha()
utilities_hover = pygame.image.load('resources/buttons/button_utilities_hover.png').convert_alpha()

knock_free = pygame.image.load('resources/buttons/button_use-jail-knocks-card.png').convert_alpha()
knock_free_hover = pygame.image.load('resources/buttons/button_use-jail-knocks-card_hover.png').convert_alpha()
pot_free = pygame.image.load('resources/buttons/button_use-jail-pot-card.png').convert_alpha()
pot_free_hover = pygame.image.load('resources/buttons/button_use-jail-pot-card_hover.png').convert_alpha()

small_exit = pygame.image.load('resources/buttons/button_exit.png').convert_alpha()
small_exit_hover = pygame.image.load('resources/buttons/button_exit_hover.png').convert_alpha()
exit_jail = pygame.image.load('resources/buttons/button_exit-jail.png').convert_alpha()
exit_jail_hover = pygame.image.load('resources/buttons/button_exit-jail.png').convert_alpha()
mortgage = pygame.image.load('resources/buttons/button_mortgaged.png').convert_alpha()
mortgage_hover = pygame.image.load('resources/buttons/button_mortgaged_hover.png').convert_alpha()
sell_page_hover = pygame.image.load('resources/buttons/button_sell_page_hover.png').convert_alpha()
sell_page = pygame.image.load('resources/buttons/button_sell_page.png').convert_alpha()
pay_mortgage = pygame.image.load('resources/buttons/button_pay-mortgage.png').convert_alpha()
pay_mortgage_hover = pygame.image.load('resources/buttons/button_pay-mortgage_hover.png').convert_alpha()

player_info_overlay1 = pygame.image.load('resources/token_display/1.png').convert_alpha()
player_info_overlay2 = pygame.image.load('resources/token_display/2.png').convert_alpha()
player_info_overlay3 = pygame.image.load('resources/token_display/3.png').convert_alpha()
player_info_overlay4 = pygame.image.load('resources/token_display/4.png').convert_alpha()
player_info_overlay5 = pygame.image.load('resources/token_display/5.png').convert_alpha()
player_info_overlay6 = pygame.image.load('resources/token_display/6.png').convert_alpha()

# create button instances
pay_mortgage_button = Button.Button(71, 750, pay_mortgage, 1)
pay_mortgage_hover_button = Button.Button(71, 750, pay_mortgage_hover, 1)
sell_page_button = Button.Button(500, 500, sell_page, 1)
sell_page_button_hover = Button.Button(500, 500, sell_page_hover, 1)
mortgage_button = Button.Button(60, 650, mortgage, 1)
mortgage_button_hover = Button.Button(60, 650, mortgage_hover, 1)
start_game_button = Button.Button(535, 450, start_game, 1)
start_game_button_hover = Button.Button(535, 450, start_game_hover, 1)
credits_button = Button.Button(330, 575, credits, 1)
credits_button_hover = Button.Button(330, 575, credits_hover, 1)
about_button = Button.Button(560, 575, about, 1)
about_button_hover = Button.Button(560, 575, about_hover, 1)
quit_game_button = Button.Button(800, 575, quit_game, 1)
quit_game_button_hover = Button.Button(800, 575, quit_game_hover, 1)

back_button = Button.Button(10, 690, back, 1)
back_button_hover = Button.Button(10, 690, back_hover, 1)
skip_button = Button.Button(1150, 650, skip, 1)
skip_button_hover = Button.Button(1150, 650, skip_hover, 1)

play_game_button = Button.Button(550, 600, play_game, 1)
play_game_button_hover = Button.Button(550, 600, play_game_hover, 1)

pvp_button = Button.Button(100, 50, pvp, 1)
pvp_button_hover = Button.Button(100, 50, pvp_hover, 1)

pve_button = Button.Button(780, 50, pve, 1)
pve_button_hover = Button.Button(780, 50, pve_hover, 1)

select_player_button = Button.Button(300, 500, select_player, 1)
select_player_button_hover = Button.Button(300, 500, select_player_hover, 1)

select_ai_button = Button.Button(800, 500, select_ai, 1)
select_ai_button_hover = Button.Button(800, 500, select_ai_hover, 1)

game_mode_button = Button.Button(530, 510, game_mode, 1)
game_mode_button_hover = Button.Button(530, 510, game_mode_hover, 1)
normal_button = Button.Button(550, 250, normal, 1)
play_game_normal_button = Button.Button(550, 250, play_game_mode, 1)
timed_mode_button = Button.Button(550, 350, timed_mode, 1)
play_game_timed_button = Button.Button(550, 350, play_game_mode, 1)

buy_button = Button.Button(71, 444, buy, 1)
buy_button_hover = Button.Button(71, 444, buy_hover, 1)
sell_button = Button.Button(71, 509, sell, 1)
sell_button_hover = Button.Button(71, 509, sell_hover, 1)
cancel_button = Button.Button(71, 565, cancel, 1)
cancel_button_hover = Button.Button(71, 565, cancel_hover, 1)

ok_button = Button.Button(70, 350, ok, 1)
ok_button_hover = Button.Button(70, 350, ok_hover, 1)

yes_button = Button.Button(560, 497, yes, 1)
yes_button_hover = Button.Button(560, 497, yes_hover, 1)
no_button = Button.Button(680, 497, no, 1)
no_button_hover = Button.Button(680, 497, no_hover, 1)
pay_button = Button.Button(588, 535, pay, 1)
pay_button_hover = Button.Button(588, 535, pay_hover, 1)
pay_red_button_hover = Button.Button(588, 535, pay_red_hover, 1)

hundered_button = Button.Button(690, 535, hundered, 1)
hundered_button_hover = Button.Button(690, 535, hundered_hover, 1)
ten_button = Button.Button(500, 535, ten, 1)
ten_button_hover = Button.Button(500, 535, ten_hover, 1)
fifty_button = Button.Button(595, 535, fifty, 1)
fifty_button_hover = Button.Button(595, 535, fifty_hover, 1)

wait_till_release_button = Button.Button(20, 175, wait_till_release, 1)
wait_till_release_button_hover = Button.Button(20, 175, wait_till_release_hover, 1)

cards_owned_button = Button.Button(60, 535, cards_owned, 1)
cards_owned_hover_button_hover = Button.Button(60, 535, cards_owned_hover, 1)

bankrupt_button = Button.Button(574, 169, bankrupt, 1)
bankrupt_hover_button = Button.Button(574, 169, bankrupt_hover, 1)

small_exit_button = Button.Button(550, 200, small_exit, 1)
small_exit_button_hover = Button.Button(550, 200, small_exit_hover, 1)
exit_jail_button = Button.Button(20, 400, exit_jail, 1)
exit_jail_button_hover = Button.Button(20, 400, exit_jail_hover, 1)

buy_house_button = Button.Button(57, 45, buy_house, 1)
buy_house_button_hover = Button.Button(57, 45, buy_house_hover, 1)
sell_house_button = Button.Button(57, 107, sell_house, 1)
sell_house_button_hover = Button.Button(57, 107, sell_house_hover, 1)
red_button = Button.Button(57, 130, red, 1)
red_button_hover = Button.Button(57, 130, red_hover, 1)
yellow_button = Button.Button(57, 192, yellow, 1)
yellow_button_hover = Button.Button(57, 192, yellow_hover, 1)
green_button = Button.Button(57, 254, green, 1)
green_button_hover = Button.Button(57, 254, green_hover, 1)
orange_button = Button.Button(57, 318, orange, 1)
orange_button_hover = Button.Button(57, 318, orange_hover, 1)
brown_button = Button.Button(57, 380, brown, 1)
brown_button_hover = Button.Button(57, 380, brown_hover, 1)
blue_button = Button.Button(57, 441, blue, 1)
blue_button_hover = Button.Button(57, 441, blue_hover, 1)
deep_blue_button = Button.Button(57, 502, deep_blue, 1)
deep_blue_button_hover = Button.Button(57, 502, deep_blue_hover, 1)
purple_button = Button.Button(57, 565, purple, 1)
purple_button_hover = Button.Button(57, 565, purple_hover, 1)
railroad_button = Button.Button(57, 628, railroad, 1)
railroad_button_hover = Button.Button(57, 628, railroad_hover, 1)
utilities_button = Button.Button(57, 691, utilities, 1)
utilities_button_hover = Button.Button(57, 691, utilities_hover, 1)

knock_free_button = Button.Button(20, 600, knock_free, 1)
knock_free_button_hover = Button.Button(20, 600, knock_free_hover, 1)


pot_free_button = Button.Button(20, 700, pot_free, 1)
pot_free_button_hover = Button.Button(20, 700, pot_free_hover, 1)

# load token images
smartphone = pygame.image.load('resources/token/token1.png').convert_alpha()
cat = pygame.image.load('resources/token/token2.png').convert_alpha()
iron = pygame.image.load('resources/token/token3.png').convert_alpha()
hatstand = pygame.image.load('resources/token/token4.png').convert_alpha()
boot = pygame.image.load('resources/token/token5.png').convert_alpha()
ship = pygame.image.load('resources/token/token6.png').convert_alpha()

# create token instances for board
play1_info = Token.Token(500, 109, player_info_overlay1, 0.25)
play2_info = Token.Token(999, 313, player_info_overlay2, 0.25)
play3_info = Token.Token(999, 424, player_info_overlay3, 0.25)
play4_info = Token.Token(999, 535, player_info_overlay4, 0.25)
play5_info = Token.Token(999, 646, player_info_overlay5, 0.25)
play6_info = Token.Token(999, 646, player_info_overlay6, 0.25)

smartphone_player = Token.Token(903, 651, smartphone, 0.5)
cat_player = Token.Token(903, 651, cat, 0.5)
iron_player = Token.Token(903, 651, iron, 0.5)
hatstand_player = Token.Token(903, 651, hatstand, 0.5)
boot_player = Token.Token(903, 651, boot, 0.5)
ship_player = Token.Token(903, 651, ship, 0.5)

# create token instances
cat_token = Button.Button(489, 222, cat, 1)
cat_button_hover = Button.Button(489, 222, cat, 1.5)
smartphone_token = Button.Button(238, 222, smartphone, 1)
smartphone_button_hover = Button.Button(238, 222, smartphone, 1.5)
iron_token = Button.Button(760, 222, iron, 1)
iron_button_hover = Button.Button(760, 222, iron, 1.5)
hatstand_token = Button.Button(977, 222, hatstand, 1)
hatstand_button_hover = Button.Button(977, 222, hatstand, 1.5)
boot_token = Button.Button(489, 399, boot, 1)
boot_button_hover = Button.Button(489, 399, boot, 1.5)
ship_token = Button.Button(760, 399, ship, 1)
ship_button_hover = Button.Button(760, 399, ship, 1.5)

# choose banker
bank = pygame.image.load('resources/buttons/button_pick-your-banker.png').convert_alpha()
bank_hover = pygame.image.load('resources/buttons/button_pick-your-banker_hover.png').convert_alpha()
bank_button = Button.Button(470, 530, bank, 1)
bank_button_hover = Button.Button(470, 530, bank_hover, 1)
banker = 0

collect = pygame.image.load('resources/buttons/button_collect.png').convert_alpha()
collect_hover = pygame.image.load('resources/buttons/button_collect_hover.png').convert_alpha()
collect_button = Button.Button(588, 535, collect, 1)
collect_button_hover = Button.Button(588, 535, collect_hover, 1)

# dice
roll = 0

bigdice_image = pygame.image.load('resources/buttons/dice.png').convert_alpha()
dice_1 = pygame.image.load('resources/elements/dice_1.png')
dice_2 = pygame.image.load('resources/elements/dice_2.png')
dice_3 = pygame.image.load('resources/elements/dice_3.png')
dice_4 = pygame.image.load('resources/elements/dice_4.png')
dice_5 = pygame.image.load('resources/elements/dice_5.png')
dice_6 = pygame.image.load('resources/elements/dice_6.png')
dices = [dice_1, dice_2, dice_3, dice_4, dice_5, dice_6]

dice_1_token = Token.Token(903, 651, dice_1, 0.5)
dice_2_token = Token.Token(903, 651, dice_2, 0.5)
dice_3_token = Token.Token(903, 651, dice_3, 0.5)
dice_4_token = Token.Token(903, 651, dice_4, 0.5)
dice_5_token = Token.Token(903, 651, dice_5, 0.5)
dice_6_token = Token.Token(903, 651, dice_6, 0.5)
dice_token = [dice_1_token,dice_2_token,dice_3_token,dice_4_token,dice_5_token,dice_6_token]

bigdice_button = Button.Button(500, 530, bigdice_image, 0.5)
bigdice_hover = Button.Button(500, 530, bigdice_image, 0.8)
dice_board_button = Button.Button(1050, 650, bigdice_image, 0.5)
dice_board_button_hover = Button.Button(1050, 650, bigdice_image, 0.65)


pay_global = False
cat_bool = False
iron_bool = False
ship_bool = False
hatstand_bool = False
smartphone_bool = False
boot_bool = False
show_bool = False
bank_bool = False
select_player_bool  =False
select_ai_bool = False
bankrupt = False
pay_out_jail = False
timed = False

# game font
font = pygame.font.Font(pygame.font.get_default_font(), 15)
our_players = []

'''
Display the start menu
'''
def start_screen():
    while True:
        screen.blit(background, (0, 0))
        if start_game_button.hover():
            start_game_button_hover.draw(screen)
        else:
            start_game_button.draw(screen)
        if start_game_button.click():
            menu()

        if credits_button.hover():
            credits_button_hover.draw(screen)
        else:
            credits_button.draw(screen)
        if credits_button.click():
            credits_menu()

        if about_button.hover():
            about_button_hover.draw(screen)
        else:
            about_button.draw(screen)
        if about_button.click():
            about_menu()

        if quit_game_button.hover():
            quit_game_button_hover.draw(screen)
        else:
            quit_game_button.draw(screen)
        if quit_game_button.click():
            sys.exit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.update()
        mainClock.tick(60)

'''
Display the about menu
'''
def about_menu():
    menu = True
    while menu:
        screen.blit(about_page, (0,0))
        if back_button.hover():
            back_button_hover.draw(screen)
        else:
            back_button.draw(screen)
        if back_button.click():
            menu = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.update()
        mainClock.tick(60)
    start_screen()

'''
Display the credits menu
'''
def credits_menu():
    while True:
        screen.blit(credits_background, (0, 0))
        if back_button.hover():
            back_button_hover.draw(screen)
        else:
            back_button.draw(screen)
        if back_button.click():
            start_screen()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.update()
        mainClock.tick(60)

'''
Display the menu where the player chooses pvp or pve
'''
def menu():
    while True:
        screen.blit(menu_background, (0, 0))
        if pvp_button.hover():
            pvp_button_hover.draw(screen)
        else:
            pvp_button.draw(screen)
        if pvp_button.click():
            print('pvp')
            only_players()

        if pve_button.hover():
            pve_button_hover.draw(screen)
        else:
            pve_button.draw(screen)
        if pve_button.click():
            print('pve')
            ai_and_player()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.update()
        mainClock.tick(60)

'''
Goes to player vs player mode
'''
def only_players():
    global cat_bool, iron_bool, hatstand_bool, ship_bool, smartphone_bool, boot_bool, bank_bool, our_players
    name_list = []
    while True:
        screen.blit(menu_background, (0, 0))
        text = font.render('Pick your token', True, (230, 230, 250))
        text_rect = text.get_rect()
        screen.blit(text, text_rect)

        if len(our_players) <= 5 or len(our_players) >= 2:
            if (len(our_players) <= 5 and len(our_players) >= 2):
                bank_button.draw(screen)
                if bank_button.hover():
                    bank_button_hover.draw(screen)
                if bank_button.click() and (len(our_players) <= 6 or len(our_players) >= 2):
                    pick_banker(0, name_list)
            if cat_token.hover() and cat_bool == False and len(our_players) <= 5:
                cat_button_hover.draw(screen)
            else:
                cat_token.draw(screen)

            if cat_token.click() and cat_bool == False and len(our_players) <= 4:
                name_list.append("Cat")
                print('cat')
                cat_bool = True
                cat_player = p.token("Cat", 0, 1500, [], False, 0, False, 0, 0, False, False, False, [], 0,
                                False)
                our_players.append(cat_player)
            if iron_token.hover() and iron_bool == False and len(our_players) <= 4:
                iron_button_hover.draw(screen)
            else:
                iron_token.draw(screen)

            if iron_token.click() and iron_bool == False and len(our_players) <= 4:
                name_list.append("Iron")
                print('iron')
                iron_bool = True
                iron_player = p.token("Iron", 0, 1500, [], False, 0, False, 0, 0, False, False, False, [], 0,
                                False)
                our_players.append(iron_player)
            if hatstand_token.hover() and hatstand_bool == False and len(our_players) <= 4:
                hatstand_button_hover.draw(screen)
            else:
                hatstand_token.draw(screen)

            if hatstand_token.click() and hatstand_bool == False and len(our_players) <= 4:
                name_list.append("Hatstand")
                print('hatstand')
                hatstand_bool = True
                hatstand_player = p.token("Hatstand", 0, 1500, [], False, 0, False, 0, 0, False, False, False, [], 0,
                                    False)
                our_players.append(hatstand_player)
            if boot_token.hover() and boot_bool == False and len(our_players) <= 4:
                boot_button_hover.draw(screen)
            else:
                boot_token.draw(screen)

            if boot_token.click() and boot_bool == False and len(our_players) <= 4:
                name_list.append("Boot")
                print('boot')
                boot_bool = True
                boot_player = p.token("Boot", 0, 1500, [], False, 0, False, 0, 0, False, False, False, [], 0,
                                    False)
                our_players.append(boot_player)
            if ship_token.hover() and ship_bool == False and len(our_players) <= 4:
                ship_button_hover.draw(screen)
            else:
                ship_token.draw(screen)

            if ship_token.click() and ship_bool == False and len(our_players) <= 4:
                name_list.append("Ship")
                print('ship')
                ship_bool = True
                ship_player = p.token("Ship", 0, 1500, [], False, 0, False, 0, 0, False, False, False, [], 0,
                                    False)
                our_players.append(ship_player)
            if smartphone_token.hover() and smartphone_bool == False and len(our_players) <= 4:
                smartphone_button_hover.draw(screen)
            else:
                smartphone_token.draw(screen)
            if smartphone_token.click() and smartphone_bool == False and len(our_players) <= 4:
                name_list.append("Smartphone")
                print('smartphone')
                smartphone_bool = True
                smartphone_player = p.token("Smartphone", 0, 1500, [], False, 0, False, 0, 0, False, False, False, [], 0,
                                    False)
                our_players.append(smartphone_player)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            pygame.display.update()
            mainClock.tick(60)

'''
Goes to player vs ai mode
'''
def ai_and_player():
    number_of_ai = 0
    global cat_bool, iron_bool, hatstand_bool, ship_bool, smartphone_bool, boot_bool, bank_bool,our_players,select_player_bool, select_ai_bool
    press = False
    name_list = []
    while True:
        screen.blit(menu_background, (0, 0))
        text = font.render('Pick your token', True, (230, 230, 250))
        text_rect = text.get_rect()
        screen.blit(text, text_rect)
        if select_player_button.hover() and select_ai_bool == False:
            select_player_button_hover.draw(screen)
        else:
            select_player_button.draw(screen)

        if select_player_button.click() and select_ai_bool == False:
            select_player_bool = True
            press = True


        if select_ai_button.hover() and select_player_bool == False:
            select_ai_button_hover.draw(screen)
        else:
            select_ai_button.draw(screen)

        if select_ai_button.click() and select_player_bool == False:
            select_ai_bool = True
            press = True

        if len(our_players) <= 5 or len(our_players) >= 2:
            if (len(our_players) <= 6 and len(our_players) >= 2):
                if bank_button.hover():
                    bank_button_hover.draw(screen)
                else:
                    bank_button.draw(screen)
                if bank_button.click() and (len(our_players) <= 5 or len(our_players) >= 2):
                    #bank_bool = True
                    pick_banker(number_of_ai, name_list)
            if cat_token.hover() and cat_bool == False and len(our_players) <= 4 and press == True:
                cat_button_hover.draw(screen)
            else:
                cat_token.draw(screen)

            if cat_token.click() and cat_bool == False and len(our_players) <= 4 and press == True:
                print('cat')
                name_list.append("Cat")
                if select_player_bool == True:
                    cat_player = p.token("Cat", 0, 1500, [], False, 0, False, 0, 0, False, False, False, [], 0,
                                         False)
                    select_player_bool = False
                else:
                    cat_player = p.token("Cat", 0, 1500, [], False, 0, False, 0, 0, False, False, False, [], 0.4,
                                         False)
                    number_of_ai += 1
                    select_ai_bool = False
                cat_bool = True
                press = False
                our_players.append(cat_player)
            if iron_token.hover() and iron_bool == False and len(our_players) <= 4 and press == True:
                iron_button_hover.draw(screen)
            else:
                iron_token.draw(screen)

            if iron_token.click() and iron_bool == False and len(our_players) <= 4 and press == True:
                name_list.append("Iron")
                if select_player_bool == True:
                    iron_player = p.token("Iron", 0, 1500, [], False, 0, False, 0, 0, False, False, False, [], 0,
                                         False)
                    select_player_bool = False
                else:
                    iron_player = p.token("Iron", 0, 1500, [], False, 0, False, 0, 0, False, False, False, [], 0.4,
                                         False)
                    select_ai_bool = False
                    number_of_ai += 1
                iron_bool = True
                press = False
                our_players.append(iron_player)
            if hatstand_token.hover() and hatstand_bool == False and len(our_players) <= 4 and press == True:
                hatstand_button_hover.draw(screen)
            else:
                hatstand_token.draw(screen)

            if hatstand_token.click() and hatstand_bool == False and len(our_players) <= 4 and press == True:
                print('hatstand')
                name_list.append("Hatstand")
                if select_player_bool == True:
                    hatstand_player = p.token("Hatstand", 0, 1500, [], False, 0, False, 0, 0, False, False, False, [], 0,
                                         False)
                    select_player_bool = False
                else:
                    hatstand_player = p.token("Hatstand", 0, 1500, [], False, 0, False, 0, 0, False, False, False, [], 0.4,
                                         False)
                    select_ai_bool = False
                    number_of_ai += 1
                hatstand_bool = True
                press = False
                our_players.append(hatstand_player)
            if boot_token.hover() and boot_bool == False and len(our_players) <= 4 and press == True:
                boot_button_hover.draw(screen)
            else:
                boot_token.draw(screen)

            if boot_token.click() and boot_bool == False and len(our_players) <= 4 and press == True:
                print('boot')
                name_list.append("Boot")
                if select_player_bool == True:
                    boot_player = p.token("Boot", 0, 1500, [], False, 0, False, 0, 0, False, False, False, [], 0,
                                         False)
                    select_player_bool = False
                else:
                    boot_player = p.token("Boot", 0, 1500, [], False, 0, False, 0, 0, False, False, False, [], 0.4,
                                         False)
                    select_ai_bool = False
                    number_of_ai += 1
                boot_bool = True
                press = False
                our_players.append(boot_player)
            if ship_token.hover() and ship_bool == False and len(our_players) <= 4 and press == True:
                ship_button_hover.draw(screen)
            else:
                ship_token.draw(screen)

            if ship_token.click() and ship_bool == False and len(our_players) <= 4 and press == True:
                print('ship')
                name_list.append("Ship")
                if select_player_bool == True:
                    ship_player = p.token("Ship", 0, 1500, [], False, 0, False, 0, 0, False, False, False, [], 0,
                                         False)
                    select_player_bool = False
                else:
                    ship_player = p.token("Ship", 0, 1500, [], False, 0, False, 0, 0, False, False, False, [], 0.4,
                                         False)
                    select_ai_bool = False
                    number_of_ai += 1
                ship_bool = True
                press = False
                our_players.append(ship_player)
            if smartphone_token.hover() and smartphone_bool == False and len(our_players) <= 4 and press == True:
                smartphone_button_hover.draw(screen)
            else:
                smartphone_token.draw(screen)
            if smartphone_token.click() and smartphone_bool == False and len(our_players) <= 4 and press == True:
                print('smartphone')
                name_list.append("Smartphone")
                if select_player_bool == True:
                    smartphone_player = p.token("Smartphone", 0, 1500, [], False, 0, False, 0, 0, False, False, False, [], 0,
                                         False)
                    select_player_bool = False
                else:
                    smartphone_player = p.token("Smartphone", 0, 1500, [], False, 0, False, 0, 0, False, False, False, [], 0.4,
                                         False)
                    select_ai_bool = False
                    number_of_ai += 1
                smartphone_bool = True
                press = False
                our_players.append(smartphone_player)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            pygame.display.update()
            mainClock.tick(60)


'''
# Picks the banker
# @param: num_of_ai
# @param: names
'''
def pick_banker(num_of_ai, names):
    global cat_bool, iron_bool, hatstand_bool, ship_bool, smartphone_bool, boot_bool, bank_bool, our_players,banker
    cat_select = True
    iron_select = True
    hatstand_select = True
    ship_select = True
    smartphone_select = True
    boot_select = True
    dice_rolled = False
    pick_banker = False
    list_banker = []
    print(names)
    if num_of_ai == len(our_players):
        print("Since we have all ai, our banker is", our_players[0].player)
        money = 1500 * len(our_players)
        in_bank = 50000 - money
        banker = bk.bank_creations(our_players[list_banker[0]].player, in_bank)
        p.token.player_banker(our_players[0], banker)
        print("start_game")
    while True:
        screen.blit(menu_background, (0, 0))
        text = font.render('Pick your banker', True, (230, 230, 250))
        text_rect = text.get_rect()
        screen.blit(text, text_rect)

        if (pick_banker and (len(list_banker) == 1) or dice_rolled):
            if game_mode_button.hover():
                game_mode_button_hover.draw(screen)
            else:
                game_mode_button.draw(screen)

            if game_mode_button.click():
                print(names[list_banker[0]], "is now the banker")
                money = 1500 * len(our_players)
                in_bank = 50000 - money
                banker = bk.bank_creations(our_players[list_banker[0]].player, in_bank)
                p.token.player_banker(our_players[0], banker)
                print('start game')
                game_mode_choose_menu()
        if len(list_banker) > 1 and dice_rolled == False:
            if bigdice_button.hover():
                bigdice_hover.draw(screen)
            else:
                bigdice_button.draw(screen)
            if bigdice_button.click():
                dice = random.randint(0, len(list_banker) - 1)
                screen.blit(dices[dice], (400, 450))
                print(dice)
                index = list_banker[dice]
                list_banker.clear()
                list_banker.append(index)
                print(names[index], "is now the banker")
                dice_rolled = True
        if cat_bool and cat_select:
            if cat_token.hover():
                cat_button_hover.draw(screen)
            else:
                cat_token.draw(screen)

            if cat_token.click():
                print('cat')
                pick_banker = True
                cat_select = False
                list_banker.append(names.index("Cat"))
        if iron_bool and iron_select:
            if iron_token.hover():
                iron_button_hover.draw(screen)
            else:
             iron_token.draw(screen)

            if iron_token.click():
                print('iron')
                pick_banker = True
                list_banker.append(names.index("Iron"))
                iron_select = False
        if hatstand_bool and hatstand_select:
            if hatstand_token.hover():
                hatstand_button_hover.draw(screen)
            else:
                hatstand_token.draw(screen)

            if hatstand_token.click():
                print('hatstand')
                list_banker.append(names.index("Hatstand"))
                pick_banker = True
                hatstand_select = False
        if boot_bool and boot_select:
            if boot_token.hover():
                boot_button_hover.draw(screen)
            else:
                boot_token.draw(screen)

            if boot_token.click():
                print('boot')
                list_banker.append(names.index("Boot"))
                pick_banker = True
                boot_select = False
        if ship_bool and ship_select:
            if ship_token.hover():
                ship_button_hover.draw(screen)
            else:
                ship_token.draw(screen)
            if ship_token.click():
                print('ship')
                list_banker.append(names.index("Ship"))
                pick_banker = True
                ship_select = False
        if smartphone_bool and smartphone_select:
            if smartphone_token.hover() and smartphone_bool:
                smartphone_button_hover.draw(screen)
            else:
                smartphone_token.draw(screen)
            if smartphone_token.click() and smartphone_bool :
                print('smartphone')
                pick_banker = True
                list_banker.append(names.index("Smartphone"))
                smartphone_select = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.update()
        mainClock.tick(60)

'''
# Display the game modes
# User will choose the game modes
'''
def game_mode_choose_menu():
    while True:
        screen.blit(menu_background, (0, 0))
        if normal_button.hover():
            play_game_normal_button.draw(screen)
        else:
            normal_button.draw(screen)

        if normal_button.click():
            start_game()

        if timed_mode_button.hover():
            play_game_timed_button.draw(screen)
        else:
            timed_mode_button.draw(screen)

        if timed_mode_button.click():
            timer_mode()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.update()
        mainClock.tick(60)

'''
Game with timed mode
'''
def timer_mode():
    global cat_bool, iron_bool, hatstand_bool, ship_bool, smartphone_bool, boot_bool
    global press
    global roll
    global count
    global skip
    global xdskip
    global timed
    timed = True
    global bankrupt, pay_global, ai_play, double_roll, pay_out_jail
    start_ticks = pygame.time.get_ticks()
    running = True
    while len(our_players) != 1:
        screen.blit(board, (0, 0))
        count = count % len(our_players)
        card_list, mydict = our_players[count].check_set()
        mortgaged_cards = our_players[count].check_mortgage()
        text = font.render("Current player "+our_players[count].player, True, (0, 0, 0), (255, 255, 255))
        screen.blit(text, (600, 300))
        seconds = (pygame.time.get_ticks() - start_ticks)/1000
        if seconds < 600 and count == 0:
            print('running')
        else:
            running = False
            if running == False and count == 0:
                print("End")
                winner(our_players)

        if pay_out_jail:
            pay_out_jail = False
            count += 1
            if count >= len(our_players):
                count = 0

        if our_players[count].jail_count > 0:
            print("Player in jail")
            print("SKIP")
            jail(our_players[count])
            count += 1
            if count >= len(our_players):
                count = 0
        press = False
        skip = False
        if our_players[count].probability > 0:

            if len(card_list) > 0:
                gb[our_players[count].position].card.buy_houses(gb[our_players[count].position], gb[our_players[count]],
                                                                banker)
            ai_menu(our_players[count])
            count += 1
            if count >= len(our_players):
                count = 0

        if our_players[count].money < 0:
            check_sellable(our_players[count], our_players[count].money, pay_player=False)
        if mortgage_button.hover() and len(mortgaged_cards) > 1:
            mortgage_button_hover.draw(screen)
        else:
            mortgage_button.draw(screen)
        if mortgage_button.click() and len(mortgaged_cards) > 1:
            pay_mortgage(our_players[count])
        if buy_house_button.hover() and (len(card_list) > 0 and press):
            buy_house_button_hover.draw(screen)
        else:
            buy_house_button.draw(screen)
        if buy_house_button.click() and (len(card_list) > 0 and press):
            print("In")
            buy_houses(our_players[count], mydict, card_list)
        if cards_owned_button.hover() and len(our_players[count].cards) > 0:
            cards_owned_hover_button_hover.draw(screen)
        else:
            cards_owned_button.draw(screen)

        if cards_owned_button.click() and len(our_players[count].cards) > 0:
            display_player_properties(our_players[count], gb[:])
        if press:
            d1 = dice_token[roll[0] - 1]
            d2 = dice_token[roll[1] - 1]
            d1.draw(screen, 400, 450)
            d2.draw(screen, 400, 550)
        if smartphone_bool:
            idx = get_player(our_players, "Smartphone")
            smartphone_player.draw(board, MapXYvalue[our_players[idx].position][0],
                              MapXYvalue[our_players[idx].position][1])
            play1_info.draw(board, 500, 500)
            text = font.render("£" + str(our_players[idx].money), True, (0, 0, 0), (255, 255, 255))
            screen.blit(text, (1007, 30))
        if cat_bool:
            idx = get_player(our_players, "Cat")
            cat_player.draw(screen, MapXYvalue[our_players[idx].position][0], MapXYvalue[our_players[idx].position][1])
            play2_info.draw(screen, 1007, 109)
            text = font.render("£" + str(our_players[idx].money), True, (0, 0, 0), (255, 255, 255))
            # textRect = text.get_rect()
            screen.blit(text, (1007, 109))
        if iron_bool:
            idx = get_player(our_players, "Iron")
            iron_player.draw(screen, MapXYvalue[our_players[idx].position][0], MapXYvalue[our_players[idx].position][1])
            play3_info.draw(screen, 1007, 215)
            text = font.render("£" + str(our_players[idx].money), True, (0, 0, 0), (255, 255, 255))
            screen.blit(text, (1007, 109))
        if hatstand_bool:
            idx = get_player(our_players, "Hatstand")
            hatstand_player.draw(screen, MapXYvalue[our_players[idx].position][0], MapXYvalue[our_players[idx].position][1])
            play4_info.draw(screen, 1007, 294)
            text = font.render("£" + str(our_players[idx].money), True, (0, 0, 0), (255, 255, 255))
            screen.blit(text, (1007, 109))
        if boot_bool:
            idx = get_player(our_players, "Boot")
            boot_player.draw(screen, MapXYvalue[our_players[idx].position][0], MapXYvalue[our_players[idx].position][1])
            play5_info.draw(screen, 1007, 400)
            text = font.render("£" + str(our_players[idx].money), True, (0, 0, 0), (255, 255, 255))
            screen.blit(text, (1007, 109))
        if ship_bool:
            idx = get_player(our_players, "Ship")
            ship_player.draw(screen, MapXYvalue[our_players[idx].position][0], MapXYvalue[our_players[idx].position][1])
            play6_info.draw(screen, 1108, 400)
            text = font.render("£"+str(our_players[idx].money), True, (0,0,0), (255,255,255))
            screen.blit(text, (1103, 109))
        if dice_board_button.hover() and press == False:
            dice_board_button_hover.draw(screen)
        else:
            dice_board_button.draw(screen)

        if dice_board_button.click() and press == False:
            roll = our_players[count].dice_roll()
            if roll[0] == roll[1]:
                press = False
                skip = False
                double_roll += 1
                print("Double")
                if double_roll == 3:
                    double_roll = 0
                    skip = True
                    press = True
                    our_players[count].position = 10
                    jail(our_players[count])
                else:
                    our_players[count].move_player(sum(roll))
                    buy_skip_card_menu(our_players[count], roll)
            else:
                skip = True
                press = True
                our_players[count].move_player(sum(roll))
                buy_skip_card_menu(our_players[count], roll)

        if skip_button.hover() and skip:
            skip_button_hover.draw(screen)
        else:
            skip_button.draw(screen)

        if skip_button.click() and skip:
            count += 1
            press = False
            skip = False
            xdskip = False
            double_roll = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.update()
        mainClock.tick(60)
    winner(our_players)

auction_list = []
count = 0
skip = False
press = False
xdskip = False
ai_play = True
double_roll = 0

'''
Starts the game
'''
def start_game():
    global cat_bool, iron_bool, hatstand_bool, ship_bool, smartphone_bool, boot_bool
    global press
    global roll
    global count
    global skip
    global xdskip
    global bankrupt, pay_global, ai_play, double_roll, pay_out_jail
    while len(our_players) != 1:
        screen.blit(board, (0, 0))
        count = count % len(our_players)
        card_list, mydict = our_players[count].check_set()
        mortgaged_cards = our_players[count].check_mortgage()
        text = font.render("Current player "+our_players[count].player, True, (0, 0, 0), (255, 255, 255))
        screen.blit(text, (570, 300))
        text_bank = font.render("Bank:"+str(banker.money), True, (0, 0, 0), (255, 255, 255))
        screen.blit(text_bank, (700, 3))
        text_free = font.render("Free Parking:" + str(gb[20].rent), True, (0, 0, 0), (255, 255, 255))
        screen.blit(text_free, (400, 3))

        if pay_out_jail:
            pay_out_jail = False
            count += 1
            if count >= len(our_players):
                count = 0

        if our_players[count].jail_count > 0:
            jail(our_players[count])
            count += 1
            if count >= len(our_players):
                count = 0
            press = False
            skip = False
        if our_players[count].probability > 0:

            if len(card_list) > 0:
                gb[our_players[count].position].card.buy_houses(gb[our_players[count].position], gb[our_players[count]], banker)
            ai_menu(our_players[count])
            count += 1
            if count >= len(our_players):
                count = 0

        if our_players[count].money < 0:
            sell_card(our_players[count], our_players[count].money, pay_player=False)
        if mortgage_button.hover() and (len(mortgaged_cards) > 1 and press):
            mortgage_button_hover.draw(screen)
        else:
            mortgage_button.draw(screen)
        if mortgage_button.click() and (len(mortgaged_cards) > 1 and press):
            pay_mortgage(our_players[count])
        if buy_house_button.hover() and (len(card_list) > 0 and press):
            buy_house_button_hover.draw(screen)
        else:
            buy_house_button.draw(screen)
        if buy_house_button.click() and (len(card_list) > 0 and press):
            buy_houses(our_players[count], mydict, card_list)
        if cards_owned_button.hover() and len(our_players[count].cards) > 0:
            cards_owned_hover_button_hover.draw(screen)
        else:
            cards_owned_button.draw(screen)

        if cards_owned_button.click() and len(our_players[count].cards) > 0:
            display_player_properties(our_players[count], gb[:])
        if press:
            d1 = dice_token[roll[0] - 1]
            d2 = dice_token[roll[1] - 1]
            d1.draw(screen, 400, 450)
            d2.draw(screen, 400, 550)
        if smartphone_bool:
            idx = get_player(our_players, "Smartphone")
            smartphone_player.draw(screen, MapXYvalue[our_players[idx].position][0], MapXYvalue[our_players[idx].position][1])
            play1_info.draw(screen, 1108, 1)
            text1 = font.render("£"+str(our_players[idx].money), True, (0,0,0), (255,255,255))
            screen.blit(text1, (1130,100))
        if cat_bool:
            idx = get_player(our_players, "Cat")
            cat_player.draw(screen, MapXYvalue[our_players[idx].position][0], MapXYvalue[our_players[idx].position][1])
            play2_info.draw(screen, 1108, 96)
            text2 = font.render("£"+str(our_players[idx].money), True, (0,0,0), (255,255,255))
            screen.blit(text2, (1130,202))
        if iron_bool:
            idx = get_player(our_players, "Iron")
            iron_player.draw(screen, MapXYvalue[our_players[idx].position][0], MapXYvalue[our_players[idx].position][1])
            play3_info.draw(screen, 1108, 202)
            text3 = font.render("£"+str(our_players[idx].money), True, (0,0,0), (255,255,255))
            screen.blit(text3, (1130, 308))
        if hatstand_bool:
            idx = get_player(our_players, "Hatstand")
            hatstand_player.draw(screen, MapXYvalue[our_players[idx].position][0], MapXYvalue[our_players[idx].position][1])
            play4_info.draw(screen, 1108, 308)
            text4 = font.render("£"+str(our_players[idx].money), True, (0,0,0), (255,255,255))
            screen.blit(text4, (1130, 414))
        if boot_bool:
            idx = get_player(our_players, "Boot")
            boot_player.draw(screen, MapXYvalue[our_players[idx].position][0], MapXYvalue[our_players[idx].position][1])
            play5_info.draw(screen, 1108, 414)
            text5 = font.render("£"+str(our_players[idx].money), True, (0,0,0), (255,255,255))
            screen.blit(text5, (1130, 520))
        if ship_bool:
            idx = get_player(our_players, "Ship")
            ship_player.draw(screen, MapXYvalue[our_players[idx].position][0], MapXYvalue[our_players[idx].position][1])
            play6_info.draw(screen, 1108, 520)
            text6 = font.render("£"+str(our_players[idx].money), True, (0,0,0), (255,255,255))
            screen.blit(text6, (1130, 626))
        if dice_board_button.hover() and press == False:
            dice_board_button_hover.draw(screen)
        else:
            dice_board_button.draw(screen)

        if dice_board_button.click() and press == False:

            roll = our_players[count].dice_roll()
            if roll[0] == roll[1]:
                press = False
                skip = False
                double_roll += 1
                if double_roll == 3:
                    double_roll = 0
                    skip = True
                    press = True
                    our_players[count].position = 10
                    jail(our_players[count])
                else:
                    our_players[count].move_player(sum(roll))

                    buy_skip_card_menu(our_players[count],roll)
                    #press = True
                    #skip = True
            else:
                skip = True
                press = True
                our_players[count].move_player(sum(roll))

                buy_skip_card_menu(our_players[count], roll)

        if skip_button.hover() and skip:
            skip_button_hover.draw(screen)
        else:
            skip_button.draw(screen)
        if skip_button.click() and skip:
            count += 1
            press = False
            skip = False
            xdskip = False
            double_roll = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.update()
        mainClock.tick(60)
    winner(our_players)

'''
# Gets the player
# @param: pplayers
# @param: name
'''
def get_player(players, name):
    for idx, player in enumerate(players):
        if player.player == name:
            return idx

'''
# Display the auction menu
# @param: players
# @param: card
# @param: idx
'''
def auction_menu(players, card, idx):
    bet = card.card_cost
    count = 0
    player_bet = {i.player: card.card_cost for i in players if i.circuit == True}
    print("In")
    auction = False
    while auction == False:
        screen.blit(board, (0, 0))
        board_card = Token.Token(530, 267, bd.board_images(idx), 0.7)
        board_card.draw(screen, 530, 267)
        if len(player_bet) != 0:
            max_value = max(player_bet.values())
            if max_value == card.card_cost:
                text1 = font.render("No bids price is "+str(card.card_cost), True, (0, 0, 0), (255, 255, 255))
                screen.blit(text1, (600, 200))
            else:
                max_bet_player = max(player_bet, key=player_bet.get)
                text1 = font.render("Highest bid is " + str(max_value) + " by " + max_bet_player, True, (0, 0, 0),
                                    (255, 255, 255))
                screen.blit(text1, (600, 200))

        if count >= len(players) or count < 0:
            count = 0
        if len(player_bet) == 1 and list(player_bet.values())[0] > card.card_cost:
            print(players[count].player, " has won the bet")
            card.buy_card((players[0]), list(player_bet.values())[0], players, banker)
            del player_bet[players[count].player]
            auction = True
            break
        if len(player_bet) == 0 and len(players) == 0:
            auction = True
            print("No one won")

        else:
            if len(player_bet) == 0:
                break
            print(count)
            if players[count].probability > 0:
                max_value = max(player_bet.values())
                bet = card.ai_auction(players[count], our_players, max_value, players[count].probability)
                if bet > max_value and bet < players[count].money:
                    print("Has done a bet")
                    player_bet[players[count].player] = bet
                    print("The current list is", player_bet)
                else:
                    print(players[count].player, " bet wasnt accept")
                    del player_bet[players[count].player]
                    del players[count]
                    count -= 1
                count += 1
            if skip_button.hover():
                skip_button_hover.draw(screen)

            else:
                skip_button.draw(screen)
            if skip_button.click():
                print(players[count].player, "has eliminated himself")
                del player_bet[players[count].player]
                del players[count]
                count -= 1
                if count >= len(players) or count < 0:
                    count = 0
            if hundered_button.hover():
                hundered_button_hover.draw(screen)
                text_name = font.render("Current player " + players[count].player + str(players[count].money), True, (0, 0, 0),
                                        (255, 255, 255))
                screen.blit(text_name, (550, 150))
            else:
                hundered_button.draw(screen)
            if hundered_button.click():
                bet += 100
                print(bet)
                print(players[count].player)
                max_value = max(player_bet.values())
                if bet > max_value and bet < players[count].money:
                    player_bet[players[count].player] = bet
                    print("The current list is", player_bet)
                else:
                    print(players[count].player, " bet wasn't accepted")
                    del player_bet[players[count].player]
                    del players[count]
                    count -= 1
                count += 1
            if ten_button.hover():
                ten_button_hover.draw(screen)
                text_name = font.render("Current player " + players[count].player + str(players[count].money), True, (0, 0, 0),
                                        (255, 255, 255))
                screen.blit(text_name, (550, 150))
            else:
                ten_button.draw(screen)
            if ten_button.click():
                bet += 10
                print(bet)
                print(players[count].player)
                max_value = max(player_bet.values())
                if bet > max_value and bet < players[count].money:
                    player_bet[players[count].player] = bet
                    print("The current list is", player_bet)
                else:
                    print(players[count].player, " bet wasn't accepted")
                    del player_bet[players[count].player]
                    del players[count]
                    count -= 1
                count += 1
            if fifty_button.hover():
                fifty_button_hover.draw(screen)
                text_name = font.render("Current player " + players[count].player + str(players[count].money), True, (0, 0, 0),
                                        (255, 255, 255))
                screen.blit(text_name, (550, 150))
            else:
                fifty_button.draw(screen)
            if fifty_button.click():
                bet += 50
                print(bet)
                print(players[count].player)
                max_value = max(player_bet.values())
                if bet > max_value and bet < players[count].money:
                    player_bet[players[count].player] = bet
                    print("The current list is", player_bet)
                else:
                    print(players[count].player, " bet wasn't accepted")
                    del player_bet[players[count].player]
                    del players[count]
                    count -= 1
                count += 1
            if count >= len(players):
                count = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.update()
        mainClock.tick(60)

def ai_menu(player):
    global cat_bool, car_bool, hatstand_bool, ship_bool, smartphone_bool, boot_bool
    global roll_click
    global count
    auction = False
    roll_click = False
    buy = False
    roll_counter = 0
    while auction == False:
        screen.blit(board, (0, 0))
        if smartphone_bool:
            idx = get_player(our_players, "Smartphone")
            smartphone_player.draw(screen, MapXYvalue[our_players[idx].position][0], MapXYvalue[our_players[idx].position][1])
        if cat_bool:
            idx = get_player(our_players, "Cat")
            cat_player.draw(screen, MapXYvalue[our_players[idx].position][0], MapXYvalue[our_players[idx].position][1])
        if iron_bool:
            idx = get_player(our_players, "Iron")
            iron_player.draw(screen, MapXYvalue[our_players[idx].position][0], MapXYvalue[our_players[idx].position][1])
        if hatstand_bool:
            idx = get_player(our_players, "Hatstand")
            hatstand_player.draw(screen, MapXYvalue[our_players[idx].position][0], MapXYvalue[our_players[idx].position][1])
        if boot_bool:
            idx = get_player(our_players, "Boot")
            boot_player.draw(screen, MapXYvalue[our_players[idx].position][0], MapXYvalue[our_players[idx].position][1])
        if ship_bool:
            idx = get_player(our_players, "Ship")
            ship_player.draw(screen, MapXYvalue[our_players[idx].position][0], MapXYvalue[our_players[idx].position][1])

        if roll_click == False:
            roll = player.dice_roll()
            if roll[0] == roll[1]:
                print("Double")
                roll_click = False
                buy = True
                roll_counter += 1
                if roll_counter == 3:
                    player.in_jail = True
                    player.position = 10
                    player.currently_in_jail()
                    auction = True
                    roll_click = True
                else:
                    player.move_player(sum(roll))
                    if player.circuit == True:
                        buy_ai_menu(player, roll)

            else:
                player.move_player(sum(roll))
                if player.circuit == True:
                    buy_ai_menu(player, roll)
                auction = True
            d1 = dice_token[roll[0] - 1]
            d2 = dice_token[roll[1] - 1]
            d1.draw(screen, 400, 450)
            d2.draw(screen, 400, 550)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.update()
        mainClock.tick(60)

'''
# Used for the ai to buy the cards
# @param: player
# @param: roll
'''
def buy_ai_menu(player, roll):
    if gb[player.position].card_owner == player.player:
        print("You own this card")
    elif gb[player.position].card_owner != "Bank" and gb[player.position].card_cost != -1:
        for user in our_players:
            if user.player == gb[player.position].card_owner:
                if gb[player.position].mortgage == True:
                    print(gb[player.position].card_name, " is currently mortgaged")
                    print("You do not need to pay because card is mortgaged")
                    card_show = False
                elif gb[player.position].card_color == "Railroad":
                    pay = gb[player.position].pay_railroads(user)
                    if pay > player.money:
                        player.sell(player, pay,banker)
                        buy_ai_menu(player,roll)
                    else:
                        gb[player.position].pay_player2(player, user, pay)
                elif gb[player.position].card_color == "Utilities":
                    pay = gb[player.position].pay_utilities(user, roll)
                    if pay > player.money:
                        player.sell(player, pay,banker)
                        buy_ai_menu(player, roll)
                    else:
                        gb[player.position].pay_player2(player, user, pay)
                else:
                    pay = gb[player.position].check_payment_cost(player, user)
                    print(pay, "payment is and current player is", player.money)
                    if pay > player.money:
                        player.sell(player, pay,banker)
                        buy_ai_menu(player, roll)
                    else:
                        gb[player.position].pay_player2(player, user, pay)
    elif gb[player.position].card_owner == "Bank" and gb[player.position].card_cost == -1:
            if gb[player.position].card_name == "Income Tax":

                gb[20].rent += player.deduct_money(200)

            elif gb[player.position].card_name == "Super Tax":
                gb[20].rent += player.deduct_money(100)

            elif gb[player.position].card_name == "Go to Jail":
                # player.currently_in_jail()
                player.in_jail = True
                player.position = 10
                player.currently_in_jail()
            elif gb[player.position].card_name == "Visiting Jail":
                print("visiting jail")

            elif gb[player.position].card_name == "go":
                print("landed on go")
            elif gb[player.position].card_name == "Pot Luck":
                print("Pot luck")
                if SCF.pot[0].function == "C":
                    choices(player, roll)
                else:
                    special_cards(player, roll, type="Pot")
            elif gb[player.position].card_name == "Opportunity Knocks":
                special_cards(player, roll, type="Knocks")
            elif gb[player.position].card_name == "Free Parking":
                if gb[player.position].rent > 0:
                    player.give_money(gb[player.position].rent)
                    gb[player.position].rent = 0

    else:
        if player.money <= gb[player.position].card_cost:
                print("To broke buy a card")
                auction_menu(player, gb[player.position],player.position)
        elif gb[player.position].card_owner == "Bank" and gb[player.position].card_cost != -1:
            x = np.random.uniform(low=0, high=player.probability + 0.1)
            print(gb[player.position].card_name)
            if player.probability > 0 and player.probability >= x:
                print("bot buy")
                gb[player.position].buy_card(player, 0, our_players, banker)
            else:
                auction_menu(player, gb[player.position],player.position)

pay = False

'''
# Used for the player to buy or skip the cards
# @param: player
# @param: roll
'''
def buy_skip_card_menu(player, roll):
    card_show = True
    global bankrupt
    global pay_global
    debt = False
    while card_show:
        screen.blit(board, (0, 0))
        if card_show:
            board_card = Token.Token(530, 267, bd.board_images(player.position), 0.7)
            board_card.draw(screen, 530, 267)
            text_balance = font.render("Money:" + str(player.money), True, (0, 0, 0), (255, 255, 255))
            screen.blit(text_balance, (600, 175))
            if gb[player.position].card_owner == player.player:
                print("You own this card")
                card_show = False
            elif gb[player.position].card_owner != "Bank" and gb[player.position].card_cost != -1:
                text = font.render("Property number: "+str(gb[player.position].houses), True, (0, 0, 0), (255, 255, 255))
                screen.blit(text, (600, 200))
                for user in our_players:
                    if user.player == gb[player.position].card_owner:
                        if gb[player.position].mortgage == True:
                            text = font.render(user.player+ " card is currently mortgaged", True, (0, 0, 0),(255, 255, 255))
                            screen.blit(text, (600, 200))
                            if pay_button.hover():
                                pay_red_button_hover.draw(screen)
                            else:
                                pay_button.draw(screen)
                            if pay_button.click():
                                print("nO PAY")
                                card_show = False
                        elif user.jail_count > 0:
                            text = font.render(user.player+ " currently in jail so do not pay", True, (0, 0, 0),(255, 255, 255))
                            screen.blit(text, (600, 200))
                            if pay_button.hover():
                                pay_red_button_hover.draw(screen)
                            else:
                                pay_button.draw(screen)
                            if pay_button.click():
                                print("nO PAY")
                                card_show = False
                        elif gb[player.position].card_color == "Railroad":
                            pay = gb[player.position].pay_railroads(user)
                            text = font.render(str(pay)+ " is currently owed to "+ user.player, True, (0, 0, 0),(255, 255, 255))
                            screen.blit(text, (600, 200))
                            if pay_button.hover():
                                pay_button_hover.draw(screen)
                            else:
                                pay_button.draw(screen)
                            if pay_button.click():
                                if pay > player.money:
                                    sell_card(player, pay, pay_player=True)
                                else:
                                    gb[player.position].pay_player2(player, user, pay)
                                card_show = False
                        elif gb[player.position].card_color == "Utilities":
                            pay = gb[player.position].pay_utilities(user, roll)
                            text = font.render(str(pay)+ " is currently owed to "+ user.player, True, (0, 0, 0),(255, 255, 255))
                            screen.blit(text, (600, 200))
                            if pay_button.hover():
                                pay_button_hover.draw(screen)
                            else:
                                pay_button.draw(screen)
                            if pay_button.click():
                                if pay > player.money:
                                    sell_card(player, pay, pay_player=True)
                                else:
                                    gb[player.position].pay_player2(player, user, pay)
                                card_show = False
                        elif bankrupt:
                            if bankrupt_button.hover() and bankrupt:
                                bankrupt_hover_button.draw(screen)
                            else:
                                bankrupt_button.draw(screen)
                            if bankrupt_button.click() and bankrupt:
                                if pay_global == False:
                                    bankrupt_player(player)
                                elif pay_global == True:
                                    gb[player.position].pay_player2(player, user, player.money)
                                    bankrupt_player(player)
                                bankrupt = False
                                card_show = False
                        else:
                            pay = gb[player.position].check_payment_cost(player, user)
                            text = font.render(str(pay)+ " is currently owed to "+ user.player, True, (0, 0, 0),(255, 255, 255))
                            screen.blit(text, (600, 200))
                            if pay_button.hover():
                                pay_button_hover.draw(screen)
                            else:
                                pay_button.draw(screen)
                            if pay_button.click():
                                print(pay, "payment is and current player is", player.money)
                                if pay > player.money:
                                    sell_card(player, pay, pay_player=True)
                                else:
                                    card_show = False
                                    gb[player.position].pay_player2(player, user, pay)
            elif gb[player.position].card_owner == "Bank" and gb[player.position].card_cost == -1:
                if ok_button.hover():
                    ok_button_hover.draw(screen)
                else:
                    ok_button.draw(screen)
                if ok_button.click():
                    card_show = False
                    if gb[player.position].card_name == "Income Tax":
                        if player.money < 200:
                            sell_card(player, 200, pay_player="Tax")
                        else:
                            gb[20].rent += player.deduct_money(200)
                            card_show = False
                    elif gb[player.position].card_name == "Super Tax":
                        if player.money < 100:
                            sell_card(player, 100, pay_player="Tax")
                        else:
                            gb[20].rent += player.deduct_money(100)
                            card_show = False
                    elif gb[player.position].card_name == "Go to Jail":
                        print("HI")
                        player.in_jail = True
                        player.position = 10
                        jail(player)
                        card_show = False
                    elif gb[player.position].card_name == "Visiting Jail":
                        print("visiting jail")
                        card_show = False
                    elif gb[player.position].card_name == "go":
                        print("landed on go")
                        card_show = False
                    elif gb[player.position].card_name == "Pot Luck":
                        print("Pot luck")
                        card_show = False
                        if SCF.pot[0].function == "C":
                            choices(player, roll)
                        elif SCF.pot[0].function == "PJ":
                            jail_passes(player,roll, type = "Pot")
                        else:
                            special_cards(player, roll, type = "Pot")
                    elif gb[player.position].card_name == "Opportunity Knocks":
                        if SCF.knocks[0].function == "KJ":
                            jail_passes(player, roll, type="Knock")
                        else:
                            special_cards(player, roll, type="Knock")
                        card_show = False

                    elif gb[player.position].card_name == "Free Parking":
                        if gb[player.position].rent > 0:
                            player.give_money(gb[player.position].rent)
                            gb[player.position].rent = 0
                        card_show = False

            elif player.circuit == True:
                if buy_button.hover():
                    buy_button_hover.draw(screen)
                else:
                    buy_button.draw(screen)
                if buy_button.click():
                    print(gb[player.position].card_owner, "12")
                    if player.money <= gb[player.position].card_cost and len(player.cards) >= 1:
                        print("To broke must sell a card")
                        sell_card(player, gb[player.position].card_cost, pay_player="C")
                    elif player.money <= gb[player.position].card_cost:
                        print("You are unable to buy this card, you also do not have a card to sell")
                        card_show = False
                    elif gb[player.position].card_owner == "Bank" and gb[player.position].card_cost != -1:
                        print(gb[player.position].card_name)
                        if player.probability > 0:
                            print("bot buy")
                            card_show = False
                        else:
                            press = True
                            gb[player.position].buy_card(player, 0, our_players, banker)
                            card_show = False
                if cancel_button.hover():
                    cancel_button_hover.draw(screen)
                else:
                    cancel_button.draw(screen)
                if cancel_button.click():
                    card_show = False
                    player_list = [i for i in our_players if i.circuit == True]
                    auction_menu(player_list, gb[player.position],player.position)
            else:
                card_show = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.update()
        mainClock.tick(60)

'''
# Used for the pot lucks and opportunity knocks
# @param: player
# @param: roll
# @param: type
'''
def special_cards(player, roll, type):
    if type == "Pot":
        img = SCF.pot_luck_draw_img(SCF.pot[0].statement)
        print(SCF.pot[0].function)
        print(SCF.pot[0].statement)
    else:
        img = SCF.opportunity_knocks_draw_img(SCF.knocks[0].statement)
        print(SCF.knocks[0].function)
    card = True
    while card:
        screen.blit(board, (0, 0))
        if card:
            board_card = Token.Token(530, 267, img, 0.7)
            board_card.draw(screen, 530, 267)

            if player.probability > 0:
                if type == "Pot":
                    if SCF.pot[0].function == "M" or SCF.pot[0].function == "SM":
                        SCF.pick_pot(player, our_players, roll, choice = None)
                        buy_ai_menu(player, roll)
                    elif SCF.pot[0].function == "B":
                        SCF.pick_pot(player, our_players, roll, choice=None)
                        birthday(player,our_players)
                    else:
                        SCF.pick_pot(player, our_players, roll, choice = None)
                else:
                    if SCF.knocks[0].function == "M" or SCF.knocks[0].function == "SM":
                        SCF.pick_knock(player, our_players, roll, choice=None)
                        buy_ai_menu(player, roll)
                    elif SCF.knocks[0].function == "H":
                        knock_pay_house(player,img, SCF.knocks[0].decision)
                    else:
                        SCF.pick_knock(player, our_players, roll, choice=None)
                card = False


            if back_button.hover():
                back_button_hover.draw(screen)
            else:
                back_button.draw(screen)
            if back_button.click():
                if type == "Pot":
                    if SCF.pot[0].function == "M" or SCF.pot[0].function == "SM":
                        SCF.pick_pot(player, our_players, roll, choice = None)
                        buy_skip_card_menu(player, roll)
                    elif SCF.pot[0].function == "B":
                        SCF.pick_pot(player, our_players, roll, choice=None)
                        birthday(player,our_players)
                    else:
                        SCF.pick_pot(player, our_players, roll, choice = None)
                    card = False
                else:
                    if SCF.knocks[0].function == "M" or SCF.knocks[0].function == "SM":
                        SCF.pick_knock(player, our_players, roll, choice = None)
                        buy_skip_card_menu(player, roll)
                    else:
                        SCF.pick_knock(player, our_players, roll, choice = None)
                    card = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.update()
        mainClock.tick(60)

'''
# Used for opportunity knocks to pay the house
# @param: player
# @param: img
# @param: payment
'''
def knock_pay_house(player, img, payment):
    card = True
    global bankrupt
    while card:
        screen.blit(board, (0, 0))
        board_card = Token.Token(530, 267, img, 0.7)
        board_card.draw(screen, 530, 267)

        if bankrupt:
            bankrupt_person(player)
            card = False
        if player.probability > 0:
            house, hotel = player.check_hotels_and_houses()
            if (house + hotel == 0):
                print("You are lucky you currently do not own any properties")
            else:
                print("Since ",player.player , " owns ", house, " houses and ", hotel, "hotel", " the deducted money is ", house*payment[0] + hotel*payment[1])
                total_payment = house*payment[0] + hotel*payment[1]
                if player.money < total_payment:
                    player.sell(total_payment, banker)
                else:
                    gb[20].rent += player.deduct_money(total_payment)
                    card = False
        if pay_button.hover():
            pay_button_hover.draw(screen)
        else:
            pay_button.draw(screen)
        if pay_button.click():
            house, hotel = player.check_hotels_and_houses()
            if (house + hotel == 0):
                print("You are lucky you currently do not own any properties")
            else:
                print("Since ", player.player, " owns ", house, " houses and ", hotel, "hotel", " the deducted money is ", house*payment[0] + hotel*payment[1])
                total_payment = house*payment[0] + hotel*payment[1]
                if player.money < total_payment:
                    sell_card(player, total_payment, pay_player="Tax")
                else:
                    gb[20].rent += player.deduct_money(total_payment)
                card = False

'''
# Choice from the players
'''
def choices(player, roll):
    card = True
    while card:
        screen.blit(board, (0, 0))
        img = SCF.pot_luck_draw_img(SCF.pot[0].statement)
        board_card = Token.Token(530, 267, img, 0.7)
        board_card.draw(screen, 530, 267)

        if player.probability > 0:
            x = np.random.uniform(low=0, high=player.probability + 0.1)
            if x <= player.probability:
                SCF.pick_pot(player, our_players, roll, choice="y")
            else:
                special_cards(player, roll, type="Knock")

        if yes_button.hover():
            yes_button_hover.draw(screen)
        else:
            yes_button.draw(screen)
        if yes_button.click():
            SCF.pick_pot(player, our_players, roll, choice = "y")
            card = False
        if no_button.hover():
            no_button_hover.draw(screen)
        else:
            no_button.draw(screen)
        if no_button.click():
            SCF.pick_pot(player, our_players, roll, choice="n")
            special_cards(player,roll,type="Knock")
            card = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            pygame.display.update()
            mainClock.tick(60)

'''
# Birthday card
# @param: player
# @param: allplayers
'''
def birthday(player, allplayers):
    for otherplayers in allplayers:
        if player.player == otherplayers.player:
            print("You cannot pay yourself")
        else:
            if otherplayers.money <= 10:
                sell_card(player, 10, pay_player="Tax")
                #check_sellable(player,10,pay_player=True)
            else:
                player.give_money(otherplayers.deduct_money(10))

'''
# Jail passes
# @param: player
# @param: roll
# @param: type
'''
def jail_passes(player, roll, type):
    card = True
    while card:
        screen.blit(board, (0, 0))
        img = SCF.pot_luck_draw_img(SCF.pot[0].statement)
        board_card = Token.Token(530, 267, img, 0.7)
        board_card.draw(screen, 530, 267)
        if collect_button.hover():
            collect_button_hover.draw(screen)
        else:
            collect_button.draw(screen)
        if collect_button.click():
            if type == "Pot":
                SCF.pick_pot(player, our_players, roll, choice=None)
                card = False
            else:
                SCF.pick_knock(player,our_players,roll,choice=None)
                card = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            pygame.display.update()
            mainClock.tick(60)

'''
# Display the player properties
# @param: player
# @param: cards
'''
def display_player_properties(player, cards):
    card = True
    count = 0
    if len(player.cards) == 0:
        card = False
    else:
        list_cards_index = [index.img_index for index in player.cards]
        print(list_cards_index[count])
    while card:
        if cards_owned_button.hover():
            cards_owned_hover_button_hover.draw(screen)
        else:
            cards_owned_button.draw(screen)
        if cards_owned_button.click():
            if count == len(player.cards):
                count = 0
            board_card = Token.Token(530, 267, bd.board_images(list_cards_index[count]), 0.7)
            board_card.draw(screen, 530, 267)
            if cards[count].houses == -1:
                print("Dont show")
            else:
                text = font.render("Property number: " + str(cards[count].houses), True, (0, 0, 0), (255, 255, 255))
                screen.blit(text, (600, 200))
            count +=1
        if small_exit_button.hover():
            small_exit_button_hover.draw(screen)
        else:
            small_exit_button.draw(screen)
        if small_exit_button.click():
            card = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            pygame.display.update()
            mainClock.tick(60)

'''
# In jail player function
# @param: player
'''
def jail(player):
    jail = True
    global pay_out_jail
    print("In jail player function")
    global xdskip
    click = False
    while jail:
        screen.blit(board, (0, 0))
        text = font.render(player.player+ " is currently in jail with a counter of " + str(player.jail_count), True, (0, 0, 0), (255, 255, 255))
        screen.blit(text, (600, 200))

        if player.jail_count < 5 and click:
            jail = False
            player.jail_count += 1
        if pot_free_button.hover() and player.pot_jail_pass == True:
            pot_free_button_hover.draw(screen)
        else:
            pot_free_button.draw(screen)
        if pot_free_button.click() and player.pot_jail_pass == True:
            player.use_jail_pass_name(card_name="Jail_Pot")
            jail = False
        if knock_free_button.hover() and player.knock_jail_pass == True:
            knock_free_hover.draw(screen)
        else:
            knock_free_button.draw(screen)
        if knock_free_button.click() and player.knock_jail_pass == True:
            player.use_jail_pass_name(card_name="Jail_Knocks")
            jail = False
        if exit_jail_button.hover() and player.jail_count == 5:
            exit_jail_button_hover.draw(screen)
        else:
            exit_jail_button.draw(screen)
        if exit_jail_button.click() and player.jail_count == 5:
            player.in_jail = False
            print("Enter")
            jail = False
            player.jail_count = 0
        if wait_till_release_button.hover() and player.jail_count <5:
            wait_till_release_button_hover.draw(screen)
        else:
            wait_till_release_button.draw(screen)
        if wait_till_release_button.click() and player.jail_count <5:
            click = True
            xdskip = True
        if pay_button.hover() and (player.jail_count == 0 and player.money > 50):
            pay_button_hover.draw(screen)
        else:
            pay_button.draw(screen)
        if pay_button.click() and (player.jail_count == 0 and player.money > 50):
            player.buy_out_of_jail()
            jail = False
            pay_out_jail = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.update()
        mainClock.tick(60)

'''
# Used to buy the houses
# @param: player
# @param: cards
# @param: color_set
'''
def buy_houses(player, cards, color_set):
    red = False
    yellow = False
    green = False
    orange = False
    brown = False
    blue = False
    purple = False
    deep_blue = False
    selection = True
    if "Brown" in color_set:
        brown = True
    if "Deep Blue" in color_set:
        deep_blue = True
    if "Red" in color_set:
        red = True
    if "Purple" in color_set:
        purple = True
    if "Blue" in color_set:
        blue = True
    if "Yellow" in color_set:
        yellow = True
    if "Green" in color_set:
        green = True
    if "Orange" in color_set:
        orange = True
    while selection:
        screen.blit(board, (0, 0))
        if brown_button.hover() and brown:
            brown_button_hover.draw(screen)
        else:
            brown_button.draw(screen)
        if brown_button.click() and brown:
            two_house_set(player, cards["Brown"])
            selection = False
        if deep_blue_button.hover() and deep_blue:
            deep_blue_button_hover.draw(screen)
        else:
            deep_blue_button.draw(screen)
        if deep_blue_button.click() and deep_blue:
            two_house_set(player, cards["Deep Blue"])
            selection = False
        if blue_button.hover() and blue:
            blue_button_hover.draw(screen)
        else:
            blue_button.draw(screen)
        if blue_button.click() and blue:
            #Change to three house set
            print("i")
            three_house_set(player, cards["Blue"])
            selection = False
        if red_button.hover() and red:
            red_button_hover.draw(screen)
        else:
            red_button.draw(screen)
        if red_button.click() and red:
            #Change to three house set
            three_house_set(player, cards["Red"])
            selection = False
        if green_button.hover() and green:
            green_button_hover.draw(screen)
        else:
            green_button.draw(screen)
        if green_button.click() and green:
            #Change to three house set
            two_house_set(player, cards["Green"])
            selection = False
        if yellow_button.hover() and yellow:
            yellow_button_hover.draw(screen)
        else:
            yellow_button.draw(screen)
        if yellow_button.click() and yellow:
            #Change to three house set
            two_house_set(player, cards["Yellow"])
            selection = False
        if purple_button.hover() and purple:
            purple_button_hover.draw(screen)
        else:
            purple_button.draw(screen)
        if purple_button.click() and purple:
            #Change to three house set
            two_house_set(player, cards["Purple"])
            selection = False
        if orange_button.hover() and orange:
            orange_button_hover.draw(screen)
        else:
            orange_button.draw(screen)
        if orange_button.click() and orange:
            #Change to three house set
            two_house_set(player, cards["Orange"])
            selection = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.update()
        mainClock.tick(60)

'''
# Used to buy two house set
# @param: player
# @param: cards
'''
def two_house_set(player, cards):
    count = 0
    temp = 0
    flag = False
    done = True
    list_cards_index = [index.img_index for index in cards]
    while done:
        my_card = Token.Token(530, 267, bd.board_images(list_cards_index[count]), 0.7)
        my_card.draw(screen, 530, 267)
        text_balance = font.render("Money:" + str(player.money), True, (0, 0, 0), (255, 255, 255))
        screen.blit(text_balance, (600, 175))
        text = font.render("Property number: " + str(cards[count].houses), True, (0, 0, 0), (255, 255, 255))
        screen.blit(text, (600, 200))
        if buy_button.hover():
            buy_button_hover.draw(screen)
        else:
            buy_button.draw(screen)
        if buy_button.click():
            index_max = max(player.cards.index(cards[0]), player.cards.index(cards[1]))
            if cards[count].houses == 5:
                print("You have reached max amount of properties")
            elif cards[count].houses <= player.cards[index_max].houses:
                if player.money >= cards[count].house_cost:
                    print("AI BUY HOUSE")
                    bk.bank_creations.add_bank_money(banker, player.deduct_money(cards[count].house_cost), player)
                    cards[count].houses += 1
                    if flag:
                        index_temp = player.cards.index(temp)
                        player.cards[index_temp] = player.cards[index_max]
                        player.cards[index_max] = temp
                        flag = False
                        # check if the money is bigger
                else:
                    print("You cannot afford the house")

            else:
                print(cards[count].card_name,
                      " currently owns more houses than the rest, please buy a house for the others")
        if skip_button.hover():
            skip_button_hover.draw(screen)
        else:
            skip_button.draw(screen)
        if skip_button.click():
            temp = cards[count]
            flag = True
            count += 1
            if count >= len(cards):
                count = 0
                done = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.update()
        mainClock.tick(60)

'''
# Used to buy three house set
# @param: player
# @param: cards
'''
def three_house_set(player, cards):
    count = 0
    temp = 0
    flag = False
    done = True
    buy = False
    list_cards_index = [index.img_index for index in cards]
    while done:
        screen.blit(board, (0, 0))
        my_card = Token.Token(530, 267, bd.board_images(list_cards_index[count]), 0.7)
        my_card.draw(screen, 530, 267)
        text_balance = font.render("Money:" + str(player.money), True, (0, 0, 0), (255, 255, 255))
        screen.blit(text_balance, (600, 175))
        text = font.render("Property number: " + str(cards[count].houses), True, (0, 0, 0), (255, 255, 255))
        screen.blit(text, (600, 200))
        index_max = player.max_index(cards)
        # index_max = max(player.cards.index(cards[0]), player.cards.index(cards[1]), player.cards.index(cards[2]))
        if flag:
            index_temp = player.cards.index(temp)
            player.cards[index_temp] = player.cards[index_max]
            player.cards[index_max] = temp
            flag = False
        if buy_button.hover():
            buy_button_hover.draw(screen)
        else:
            buy_button.draw(screen)
        if buy_button.click():
            if cards[count].houses == 5:
                print(cards[count], "currently has 5 houses")
            elif cards[count].houses <= player.cards[index_max].houses:
                print("To buy a house in,", cards[count].card_name, " will cost", cards[count].house_cost)
                if player.money >= cards[count].house_cost:
                    bk.bank_creations.add_bank_money(banker, player.deduct_money(cards[count].house_cost), player)
                    cards[count].houses += 1
                    count += 1
                    print(cards[0].card_name, cards[0].houses)
                    print(cards[1].card_name, cards[1].houses)
                    print(cards[2].card_name, cards[2].houses)
                    if count >= len(cards):
                        count = 0
                else:
                    print("You do not have enough money")
            else:
                print(cards[0].card_name, cards[0].houses)
                print(cards[1].card_name, cards[1].houses)
                print(cards[2].card_name, cards[2].houses)
                print(cards[count].card_name,
                      " currently owns more houses than the rest, please buy a house for the others")
                count += 1
                if count >= len(cards):
                    count = 0
        if skip_button.hover():
            skip_button_hover.draw(screen)
        else:
            skip_button.draw(screen)
        if skip_button.click():
            temp = cards[count]
            flag = True
            count += 1
            if count >= len(cards):
                count = 0
        if small_exit_button.hover():
            small_exit_button_hover.draw(screen)
        else:
            small_exit_button.draw(screen)
        if small_exit_button.click():
            done = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.update()
        mainClock.tick(60)

'''
# Checks the sellable cards
# @param: player
# @param: amount
# @param: pay_player
'''
def check_sellable(player, amount, pay_player):
    red = False
    yellow = False
    green = False
    orange = False
    brown = False
    blue = False
    purple = False
    deep_blue = False
    utilities = False
    railroad = False
    selection = True
    global bankrupt
    color_set = player.cards_available()
    if color_set == 0 and pay_player:
        bankrupt = True
        buy_skip_card_menu(player,roll)
        selection = False
    elif color_set == 0 and (pay_player == False and player.money <= amount):
        print("Broke")
        bankrupt = True
        bankrupt_player(player)
        selection = False
    else:
        if "Brown" in color_set.keys():
            brown = True
        if "Deep Blue" in color_set.keys():
            deep_blue = True
        if "Red" in color_set.keys():
            red = True
        if "Purple" in color_set.keys():
            purple = True
        if "Blue" in color_set.keys():
            blue = True
        if "Yellow" in color_set.keys():
            yellow = True
        if "Green" in color_set.keys():
            green = True
        if "Orange" in color_set.keys():
            orange = True
        if "Utilities" in color_set.keys():
            utilities = True
        if "Railroad" in color_set.keys():
            railroad = True
    houses = player.check_houses()
    while selection:
        screen.blit(board, (0, 0))
        if brown_button.hover() and brown:
            brown_button_hover.draw(screen)
        else:
            brown_button.draw(screen)
        if brown_button.click() and brown:
            if houses["Brown"] > 0:
                sell_two_house_set(player,color_set["Brown"])
            else:
                sell_card(player, color_set["Brown"], amount, "Brown", pay_player)
                selection = False
        if deep_blue_button.hover() and deep_blue:
            deep_blue_button_hover.draw(screen)
        else:
            deep_blue_button.draw(screen)
        if deep_blue_button.click() and deep_blue:
            if houses["Deep Blue"] > 0:
                sell_two_house_set(player,color_set["Deep Blue"])
            else:
                sell_card(player, color_set["Deep Blue"], amount, "Deep Blue", pay_player)
                selection = False
        if blue_button.hover() and blue:
            blue_button_hover.draw(screen)
        else:
            blue_button.draw(screen)
        if blue_button.click() and blue:
            # Change to three house set
            if houses["Blue"] > 0:
                print("i")
                sell_three_house_set(player,color_set["Blue"])
            else:
                sell_card(player, color_set["Blue"],amount, "Blue", pay_player)
                selection = False
        if red_button.hover() and red:
            red_button_hover.draw(screen)
        else:
            red_button.draw(screen)
        if red_button.click() and red:
            # Change to three house set
            if houses["Red"] > 0:
                sell_three_house_set(player,color_set["Red"])
            else:
                selection = False
                sell_card(player, color_set["Red"], amount, "Red", pay_player)
            #selection = False
        if green_button.hover() and green:
            green_button_hover.draw(screen)
        else:
            green_button.draw(screen)
        if green_button.click() and green:
            if houses["Green"] > 0:
                sell_three_house_set(player,color_set["Green"])
            else:
                sell_card(player, color_set["Green"],amount, "Green", pay_player)
                selection = False
        if yellow_button.hover() and yellow:
            yellow_button_hover.draw(screen)
        else:
            yellow_button.draw(screen)
        if yellow_button.click() and yellow:
            if houses["Yellow"] > 0:
                sell_three_house_set(player,color_set["Yellow"])
            else:
                # Change to three house set
                sell_card(player, color_set["Yellow"],amount, "Yellow", pay_player)
                selection = False
        if purple_button.hover() and purple:
            purple_button_hover.draw(screen)
        else:
            purple_button.draw(screen)
        if purple_button.click() and purple:
            # Change to three house set
            if houses["Purple"] > 0:
                sell_three_house_set(player,color_set["Purple"])
            else:
                sell_card(player, color_set["Purple"],amount, "Purple", pay_player)
                selection = False
        if orange_button.hover() and orange:
            orange_button_hover.draw(screen)
        else:
            orange_button.draw(screen)
        if orange_button.click() and orange:
            if houses["Orange"] > 0:
                sell_three_house_set(player,color_set["Orange"])
            else:
                sell_card(player, color_set["Orange"],amount, "Orange", pay_player)
                selection = False
        if railroad_button.hover() and railroad:
            railroad_button_hover.draw(screen)
        else:
            railroad_button.draw(screen)
        if railroad_button.click() and railroad:
            # Change to three house set
            selection = False
            sell_card(player, color_set["Railroad"], amount, "Railroad", pay_player)
            #selection = False
        if utilities_button.hover() and utilities:
            utilities_button_hover.draw(screen)
        else:
            utilities_button.draw(screen)
        if utilities_button.click() and utilities:
            # Change to three house set
            sell_card(player, color_set["Utilities"],amount, "Utilities", pay_player)
            selection = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.update()
        mainClock.tick(60)

'''
# Used to sell the card
# @param: player
# @param: amount
# @param: pay_player
'''
def sell_card(player, amount, pay_player):
    flag = True
    mortgage = False
    click = True
    count = 0
    yes_no = False
    return_zero = -1
    exit = False
    if len(player.cards) == 0 and (amount >= player.money and pay_player != "C"):
        bankrupt_player(player)
        flag = False
    while (flag):
        houses = player.check_houses()
        color_set = player.cards_available()
        screen.blit(menu_background, (0, 0))
        text_balance = font.render("Money:" + str(player.money), True, (0, 0, 0), (255, 255, 255))
        screen.blit(text_balance, (600, 175))
        check_houses = player.check_houses()
        if len(player.cards) > 0:
            if player.cards[count].houses == -1:
                print("Dont show")
            else:
                text = font.render("Property number: " + str(player.cards[count].houses), True, (0, 0, 0),
                                   (255, 255, 255))
                screen.blit(text, (600, 200))
            board_card = Token.Token(530, 267, bd.board_images(player.cards[count].img_index), 0.7)
            board_card.draw(screen, 530, 267)
        if len(player.cards) == 0 and (player.money <= amount and pay_player == True):
            bankrupt_person(player)
            print("-------")
            exit = True
        elif len(player.cards) == 0 and pay_player == "C":
            exit = True
        elif len(player.cards) == 0 and (pay_player == "Tax" and amount > player.money):
            gb[20].rent += player.money
            bankrupt_person(player)
        if cards_owned_button.hover():
            cards_owned_hover_button_hover.draw(menu_background)
        else:
            cards_owned_button.draw(menu_background)
        if cards_owned_button.click():
            count += 1
            if count >= len(player.cards):
                count = 0
        if sell_page_button.hover() and click:
            sell_page_button_hover.draw(menu_background)
        else:
            sell_page_button.draw(menu_background)

        if sell_page_button.click() and click:
            click = True
            print(len(player.cards), "length")
            if len(player.cards) == 0:
                click = False
            elif houses[player.cards[count].card_color] > 0 and (player.cards[count].card_color == "Brown" or player.cards[count].card_color == "Deep Blue"):
                click = False
                exit = True
                sell_two_house_set(player, color_set[player.cards[count].card_color])
            elif houses[player.cards[count].card_color] > 0 and (player.cards[count].card_color != "Brown" or player.cards[count].card_color != "Deep Blue"):
                click = False
                exit = True
                sell_three_house_set(player, color_set[player.cards[count].card_color])
            else:
                index = player.cards.index(player.cards[count])

                if player.cards[index].card_color == "Railroad":
                    if player.cards[index].mortgage == True:
                        bk.bank_creations.reduce_banks_money(banker, player.give_money(
                            (int(player.cards[index].card_cost * 0.5))), player)
                        player.cards[index].mortgage = False
                        player.cards.pop(index).card_owner = "Bank"
                    else:
                        bk.bank_creations.reduce_banks_money(banker,
                                                             player.give_money(player.cards[index].card_cost),
                                                             player)
                        # self.give_money(self.cards[int(select)].card_cost)
                        player.cards.pop(index).card_owner = "Bank"
                    player.stations -= 1
                elif player.cards[index].card_color == "Utilities":
                    if player.cards[index].mortgage == True:
                        bk.bank_creations.reduce_banks_money(banker, player.give_money(
                            (int(player.cards[index].card_cost * 0.5))), player)
                        # self.give_money((int(self.cards[int(select)].card_cost * 0.5)))
                        player.cards[index].mortgage = False
                        player.cards.pop(index).card_owner = "Bank"
                    else:
                        bk.bank_creations.reduce_banks_money(banker,
                                                             player.give_money(player.cards[index].card_cost),
                                                             player)
                        # self.give_money(self.cards[int(select)].card_cost)
                        player.cards.pop(index).card_owner = "Bank"
                    player.utlity -= 1
                elif check_houses[player.cards[index].card_color] > 0:
                    color = player.cards[index].card_color
                    # self.sell_house(color)
                elif player.cards[index].mortgage == True:
                    player.give_money(
                        (int(player.cards[index].card_cost * 0.5)))
                    bk.bank_creations.reduce_banks_money(banker, (int(player.cards[index].card_cost * 0.5)), player)
                    # self.give_money((int(self.cards[int(select)].card_cost * 0.5)))
                    player.cards[index].mortgage = False
                    player.cards.pop(index).card_owner = "Bank"
                elif player.cards[index].mortgage == False:
                    player.give_money((int(player.cards[index].card_cost)))
                    bk.bank_creations.reduce_banks_money(banker,
                                                         player.cards[index].card_cost, player)
                    print(player.money)
                    # self.give_money(self.cards[int(select)].card_cost)
                    player.cards.pop(index).card_owner = "Bank"
                exit = True
        # if self.money < amount and len(self.cards) > 0:
        # print(amount, "amount owned to the bank/player")
        # flag = False
        # return amount
        if mortgage_button.hover() and click:
            mortgage_button_hover.draw(menu_background)
        else:
            mortgage_button.draw(menu_background)

        if mortgage_button.click() and click:
            click = False
            # yes code
            if len(player.cards) == 0:
                exit = True
                click = False
            else:
                index = player.cards.index(player.cards[count])
                player.mortgage_card(player.cards[index])
                exit = True
        if back_button.hover() and exit:
            back_button_hover.draw(menu_background)
        else:
            back_button.draw(menu_background)
        if back_button.click() and exit:
            click = False
            flag = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.update()
        mainClock.tick(60)
    buy_skip_card_menu(player, roll)


def sell_two_house_set(player, cards):
    count = 0
    temp = 0
    flag = False
    done = True
    #list_cards_index = [index.img_index for index in cards]
    while done:
        text_balance = font.render("Money:" + str(player.money), True, (0, 0, 0), (255, 255, 255))
        screen.blit(text_balance, (600, 175))
        index_max = player.min_index(cards)
        list_cards_index = [index.img_index for index in cards]
        my_card = Token.Token(530, 267, bd.board_images(list_cards_index[count]), 0.7)
        my_card.draw(screen, 530, 267)
        if cards[count].houses == -1:
            print("Dont show")
        else:
            text = font.render("Property number: " + str(cards[count].houses), True, (0, 0, 0), (255, 255, 255))
            screen.blit(text, (600, 200))
        if sell_button.hover():
            sell_button_hover.draw(screen)
        else:
            sell_button.draw(screen)
        if sell_button.click():
            #index_max = player.max_index(cards)
            if cards[count].houses == 0:
                print("You have reached miniumn amount of properties")
            elif cards[count].houses >= player.cards[index_max].houses:
                if player.money >= cards[count].house_cost:
                    print("AI BUY HOUSE")
                    bk.bank_creations.reduce_banks_money(banker, player.give_money(cards[count].house_cost), player)
                    cards[count].houses -= 1
                    if flag:
                        index_temp = player.cards.index(temp)
                        player.cards[index_temp] = player.cards[index_max]
                        player.cards[index_max] = temp
                        flag = False
                        # check if the money is bigger
                else:
                    print("You cannot afford the house")

            else:
                print(cards[count].card_name,
                      " currently owns more houses than the rest, please buy a house for the others")
        if skip_button.hover():
            skip_button_hover.draw(screen)
        else:
            skip_button.draw(screen)
        if skip_button.click():
            temp = cards[count]
            flag = True
            count += 1
            if count >= len(cards):
                count = 0
                done = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.update()
        mainClock.tick(60)
    buy_skip_card_menu(player,roll)

def sell_three_house_set(player, cards):
    count = 0
    temp = 0
    flag = False
    done = True
    buy = False
    list_cards_index = [index.img_index for index in cards]
    while done:
        screen.blit(board, (0, 0))
        text_balance = font.render("Money:" + str(player.money), True, (0, 0, 0), (255, 255, 255))
        screen.blit(text_balance, (600, 175))
        my_card = Token.Token(530, 267, bd.board_images(list_cards_index[count]), 0.7)
        my_card.draw(screen, 530, 267)
        text = font.render("Property number: " + str(cards[count].houses), True, (0, 0, 0), (255, 255, 255))
        screen.blit(text, (600, 200))
        index_max = player.min_index(cards)
        # index_max = max(player.cards.index(cards[0]), player.cards.index(cards[1]), player.cards.index(cards[2]))
        if flag:
            index_temp = player.cards.index(temp)
            player.cards[index_temp] = player.cards[index_max]
            player.cards[index_max] = temp
            flag = False
        if sell_button.hover():
            sell_button_hover.draw(screen)
        else:
            sell_button.draw(screen)
        if sell_button.click():
            if cards[count].houses == 0:
                print(cards[count], "currently has 5 houses")
            elif cards[count].houses >= player.cards[index_max].houses:
                print("To buy a house in,", cards[count].card_name, " will cost", cards[count].house_cost)
                bk.bank_creations.add_bank_money(banker, player.deduct_money(cards[count].house_cost), player)
                cards[count].houses -= 1
                count += 1
                print(cards[0].card_name, cards[0].houses)
                print(cards[1].card_name, cards[1].houses)
                print(cards[2].card_name, cards[2].houses)
                if count >= len(cards):
                    count = 0
            else:
                print(cards[0].card_name, cards[0].houses)
                print(cards[1].card_name, cards[1].houses)
                print(cards[2].card_name, cards[2].houses)
                print(cards[count].card_name,
                      " currently owns more houses than the rest, please buy a house for the others")
                count += 1
                if count >= len(cards):
                    count = 0
        if skip_button.hover():
            skip_button_hover.draw(screen)
        else:
            skip_button.draw(screen)
        if skip_button.click():
            temp = cards[count]
            flag = True
            count += 1
            if count >= len(cards):
                count = 0
        if small_exit_button.hover():
            small_exit_button_hover.draw(screen)
        else:
            small_exit_button.draw(screen)
        if small_exit_button.click():
            done = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.update()
        mainClock.tick(60)

'''
# Used to bankrupt player
# @param: player
'''
def bankrupt_person(player):
    global cat_bool, iron_bool, hatstand_bool, ship_bool, smartphone_bool, boot_bool, bank_bool, our_players,timed
    if player.player == "Smartphone":
        smartphone_bool = False
        player.bankrupt = True
        our_players.remove(player)
    if player.player == "Cat":
        cat_bool = False
        player.bankrupt = True
        our_players.remove(player)
    if player.player == "Iron":
        iron_bool = False
        player.bankrupt = True
        our_players.remove(player)
    if player.player == "Hatstand":
        hatstand_bool = False
        player.bankrupt = True
        our_players.remove(player)
    if player.player == "Boot":
        boot_bool = False
        player.bankrupt = True
        our_players.remove(player)
    if player.player == "Ship":
        ship_bool = False
        player.bankrupt = True
        our_players.remove(player)
    if timed:
        timer_mode()
    else:
        start_game()

def pay_mortgage(player):
    #mortgage = token.check_mortgage()
    count = 0
    done = False
    while done:
        mortgage = player.check_mortgage()
        text_balance = font.render("Money:" + str(player.money), True, (0, 0, 0), (255, 255, 255))
        screen.blit(text_balance, (600, 175))
        if len(mortgage) >= 1:
            cards = [(cards,cards.card_color) for keys, cards in mortgage.items()]
            screen.blit(board, (0, 0))
            board_card = Token.Token(530, 267, bd.board_images(cards[0][count].img_index), 0.7)
            board_card.draw(screen, 530, 267)
        if cards_owned_button.hover():
            cards_owned_hover.draw(screen)
        else:
            cards_owned_button.draw(screen)
        if cards_owned_button.click():
            count += 1
            if count >= len(cards):
                count = 0
        if yes_button.hover():
            yes_hover.draw(screen)
        else:
            yes_button.draw(screen)
        if yes_button.click():
            payment = (mortgage[1][count].card_cost * 0.5) + (mortgage[1][count].card_cost * 0.5) * 0.1
            if player.money <= payment:
                print("Not enough money to unmortgage", payment)
                done = False
                print("pop up")
                #start_game()
            else:
                bk.bank_creations.add_bank_money(bank, player.deduct_money(payment), player)
                mortgage[0][count].mortgage = False
                done = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.update()
        mainClock.tick(60)

def bankrupt_player(player):
    done = True
    print(player.player)
    player.bankrupt = True
    while done:
        screen.blit(board, (0, 0))
        if bankrupt_button.hover():
            bankrupt_hover_button.draw(screen)
        else:
            bankrupt_button.draw(screen)
        if bankrupt_button.click():
            bankrupt_person(player)
            done = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.update()
        mainClock.tick(60)

def winner(players):
    winner = True
    smartphone_player = Token.Token(903, 651, smartphone, 4)
    cat_player = Token.Token(903, 651, cat, 4)
    iron_player = Token.Token(903, 651, iron, 4)
    hatstand_player = Token.Token(903, 651, hatstand, 4)
    boot_player = Token.Token(903, 651, boot, 4)
    ship_player = Token.Token(903, 651, ship, 4)
    while winner:
        screen.blit(winner_background, (0, 0))
        if len(players) == 1:
            if smartphone_bool:
                smartphone_player.draw(screen, 450, 300)
            if cat_bool:
                cat_player.draw(screen, 450,300)
            if iron_bool:
                iron_player.draw(screen, 500,500)
            if hatstand_bool:
                hatstand_player.draw(screen, 500,500)
            if boot_bool:
                boot_player.draw(screen, 500,500)
            if ship_bool:
                ship_player.draw(screen, 500,500)
        else:
            get_best(players)

        if quit_game_button.hover():
            quit_game_button_hover.draw(screen)
        else:
            quit_game_button.draw(screen)
        if quit_game_button.click():
            sys.exit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.update()
        mainClock.tick(60)

def get_best(players):
    temp_value = 0
    maybe_winner = []
    for predicted_winner in players:
        credit = predicted_winner.money
        for card in predicted_winner.cards:
            credit += (card.card_cost + (card.houses * card.house_cost))
        if credit > temp_value:
            temp_value = credit
            maybe_winner.clear()
            maybe_winner.append(predicted_winner)
        else:
            bankrupt_person(predicted_winner)
    winner(maybe_winner)


start_screen()

