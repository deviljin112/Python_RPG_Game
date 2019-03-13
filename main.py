import random
import time
import pickle
import sys
from classes import Human, Orc, Elf, Wolf, Zombie, Wraith
from area import rooms

        ###############################
        ########## FUNCTIONS ##########
        ###############################

race = "None"

def set_global_race(c_race):
    global race
    race = c_race

def set_global_call(character):
    global char
    char = character

def check_lvl(x):
    global level_up, exp_leftover
    
    gained_exp = x

    x += char.exp
    level_up, exp_leftover = divmod(x, 100)

    if x > 100:

        if level_up > char.level:
            char.level = char.level + (level_up - char.level)
            char.exp = 0
            char.exp += exp_leftover

            lvl_up_text = '''
                You've Level'ed up!
                Current Level: {}
                Current Experiance: {}
            '''.format(char.level, char.exp)

            print(lvl_up_text)

            x = 0

    else:
        char.exp = x
        
        exp_left_text = '''
            You've gained {} experiance.
            Current Experiance: {}.
        '''.format(gained_exp, char.exp)
        print(exp_left_text)


        ##################################
        ########## CLASS CHOICE ##########
        ##################################


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
        ########## MOVEMENT ##########
        ##############################

check_lvl(20)   #20
check_lvl(110)  #130
check_lvl(280)  #410
check_lvl(576)  #986
print(char.level)
print(char.exp)
func = 20 + 110 + 280 + 576
print(func)