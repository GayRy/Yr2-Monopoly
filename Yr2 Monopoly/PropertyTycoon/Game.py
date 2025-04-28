# This is a sample Python script.
import time
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from BoardDefinition import game_board as gb
import PlayerFunctions as p
import SpecialCardFunctions as SCF
import AI as ai_functions
import Bank as bk
import CardFunctions as c
import numpy as np
import random
gameboard = gb()


Horse = p.token("Horse", 0, 1500, [], False, 0, False,0,0, False, False, False,[],0, False)
Car = p.token("Car", 0, 1500, [], False, 0, False,0,0, False, False, False,[],0, False)
Boot = p.token("Boot", 0 ,1500,[], False, 0, False,0,0, False,False, False,[],0, True)
Duck = p.token("Duck",0,1500,[], False, 0, False,0,0, False,False, False,[],0, False)
Ship = p.token("Ship",0,1500,[], False, 0, False,0,0, False, False, False,[],0,False)
Trex = p.token("Trex",0,1500,[], False, 0, False,0,0, False, False, False,[],0,False)
Cat = p.token("Cat",0,1500,[], False, 0, False,0,0, False,False, False,[],0,False)
Hat = p.token("Hat",0,1500,[], False, 0, False,0,0, False,False, False,[],0,False)

list_of_players = [Horse,Car,Boot,Ship,Hat,Cat,Trex,Duck]
string_of_players = ["Horse","Car","Boot","Ship","Hat","Cat","Trex","Duck"]
player_list = []

def start_game():
    flag = True
    while (flag):
        print("Please enter the number of players you want")
        num = input("Enter:")
        if num.isnumeric():
            print("Hi")
            if int(num) == 8:
                number_player(int(num), bots=0)
                flag = False
            else:
                fk = True
                while fk:
                    print("Do you want to have bots?")
                    bots = input("Enter number of bots:")
                    if int(num) + int(bots) <= 8:
                        number_player(int(num), int(bots))
                        fk = False
                        flag = False
                    elif int(bots) == 0:
                        if int(bots) + int(num) == 0:
                            fk = False
                            flag = False
                            print("Start over again since no players were added")
                            start_game()
                        else:
                            number_player(int(num), int(bots))
                            fk = False
                            flag = False
                    elif int(num) + int(bots) > 8:
                        print("The number of players is greater than the limit")
                    else:
                        print("Enter the correct value")

def number_player(players, bots):
    i = 1
    print("as")
    while(players != 0 or bots != 0):
        if players != 0:
            print("Player:",i," please select the character you want from", string_of_players,
                  "\n Please select from 0 to",len(list_of_players))
            for idx, name in enumerate(string_of_players):
                print(idx,":", name)
            num_of_player = input("Enter the player number")
            if num_of_player.isnumeric():
                player_list.append(list_of_players.pop(int(num_of_player)))
                string_of_players.remove(string_of_players[int(num_of_player)])
                players -= 1
        elif bots != 0:
            print("Do you want a easy, medium, hard bot?")
            skill = input("Enter:")
            if skill == "easy" or skill == "medium" or skill == "hard":
                if skill == "easy":
                    skill_value = np.random.uniform(low=0.1, high=0.4)
                elif skill == "medium":
                    skill_value = np.random.uniform(low=0.4, high=0.6)
                elif skill == "hard":
                    skill_value = np.random.uniform(low=0.6, high=0.85)
                print(skill_value, "sv")
                bot = list_of_players.pop(0)
                bot.probability = skill_value
                player_list.append(bot)
                string_of_players.remove(string_of_players[0])
                bots -= 1
            else:
                print("Incorrect value")

def select_banker():
    n = random.randint(0, len(player_list) - 1)
    print(player_list[n].player, " is now the banker")
    player_list[n].banker = True
    Banker = bk.bank_creations(player_list[n].player, 50000, player_list[n].probability)
    return Banker

def game():
    i = 0
    start_game()
    Banker = select_banker()
    #a = player_list[i].get_banker(player_list)
    #player_list[i].bank.get_banker()
    #print(player_list.player_list())
    while(len(player_list) != 1):
        #user_choice = input("Please enter a r to roll")
        i = i % len(player_list)
        if player_list[i].in_jail is True:
            print("Player in jail")
            player_list[i].currently_in_jail()
        else:
            result = player_list[i].player_action(gameboard[player_list[i].position],Banker)
            player_list[i].move_player(sum(result))
            player_list[i].check_double(player_list, result[0], result[1])
            c.card.buy_houses(gameboard[player_list[i].position], player_list[i],Banker)
        player_list[i].display_player_properties()
        if player_list[i].bankrupt == True:
            print(player_list.pop(i).player, " is bankrupt and is out of the game")
        else:
            print("\n\n" ,player_list[i].player, player_list[i].money)
            i = i + 1

    winner(player_list)

def winner(player):
    print("The winner is ",player[0].player)

game()