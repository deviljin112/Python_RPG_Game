import random
import time
import pickle
import sys
from classes import Human, Orc, Elf, Wolf, Zombie, Wraith
from area import rooms

        ##################################
        ########## CLASS CHOICE ##########
        ##################################

race = "None"

def set_global_race(c_race):
    global race
    race = c_race

def set_global_call(character):
    global char
    char = character

print("Human, Elf, Orc")
c_pick = input("Choose your class: ")

if c_pick == "Human":
    set_global_race(c_pick)
    c_class = eval(race)
    set_global_call(c_class("Dev"))
    char.say("Hello")
    char.grunt()

elif c_pick == "Elf":
    set_global_race(c_pick)
    c_class = eval(race)
    set_global_call(c_class("Lothaysa"))
    char.say("Good Day to you!")
    char.grunt()

elif c_pick == "Orc":
    set_global_race(c_pick)
    c_class = eval(race)
    set_global_call(c_class("Garosh"))
    char.say("Bloody Mortals")
    char.grunt()
else:
    text = """
    You have not selected a class.
    Please restart the game and pick a valid class
    """
    print(text)
    time.sleep(10)
    sys.exit()

        ##############################
        ########## LEVELING ##########
        ##############################


## Create level dict
lvl_name = "Level"
dict_lvl = 1
lvl_dict = {}
lvl_max = 100

while dict_lvl <= lvl_max:
    lvl_dict[lvl_name + "_{}".format(dict_lvl)] = dict_lvl
    dict_lvl += 1


## Moves one up the dict
lvl_inter = lvl_dict.keys()
lvl_inter = iter(lvl_inter)
next_lvl_func = next(lvl_inter)


## Checks EXP and triggers movement of dict
char.exp = 10

level_up, exp_leftover = divmod(char.exp, 100)

print(level_up, exp_leftover)


        ##############################
        ########## MOVEMENT ##########
        ##############################

