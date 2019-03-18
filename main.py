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
    
    print("---")

    gained_exp = x
    x += char.exp
    level_up, exp_leftover = divmod(x, 100)
    level_up += char.level

    if x >= 100:

        if level_up > char.level:
            char.level = level_up
            char.exp = 0
            char.exp += exp_leftover

            lvl_up_text = '''
                You've Level'ed up!
                Current Level: {}
                Current Experiance: {}
            '''.format(char.level, char.exp)
            print(lvl_up_text)
            print(x, "x")

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

def current_pos(cat, pos):
    print("current_pos", cat, pos)
    if cat in rooms:
        print("found")

        if pos in rooms[cat]:
            current_position = rooms[cat][pos]["name"]
            print(current_position)

            y = rooms[cat][pos]
            return y
    else:
        print("not found")

def connect_pos(z):
    w = z["connects"].values()
    return w
    
def pos_setter(p_set):
    print("setting category")
    if p_set == "spawner":
        char.category = "spawner"
        print("cat set to, ", char.category)
    elif p_set == "alley":
        char.category = "alley"
        print("cat set to, ", char.category)
    elif p_set == "house":
        char.category = "house"
        print("cat set to, ", char.category)
    elif p_set == "living_room":
        char.category = "living_room"
        print("cat set to, ", char.category)
    elif p_set == "terrace":
        char.category = "terrace"
        print("cat set to, ", char.category)
    else:
        print("Missing Category")

def output_convert(from_to):
    print("converting")
    print(from_to)
    if from_to in ("alleyway_1", "alleyway_2"):
        from_to = "alley"
        print("set to ", from_to)
        return from_to
    elif from_to in ("hall", "closet", "bedroom"):
        from_to = "house"
        print("set to ", from_to)
        return from_to
    elif from_to in ("living_room_1", "living_room_2", "living_room_3", "living_room_4"):
        from_to = "living_room"
        print("set to ", from_to)
        return from_to
    elif from_to in ("balcony_1", "balcony_2"):
        from_to = "terrace"
        print("set to ", from_to)
        return from_to
    elif from_to in "spawn":
        from_to = "spawner"
        print("set to ", from_to)
        return from_to
    else:
        print("missing input")

def char_position():
    char_pos = current_pos(cat, pos)
    return char_pos

def char_connect():
    char_position_a = char_position()
    connect_pos_a = connect_pos(char_position_a)
    return connect_pos_a

def level_movement():
    global cat, pos
    cat = char.category
    pos = char.position

    print(list(char_connect()))
    player_move = input("Next move: ")
    p_move = player_move
    
    if p_move == "kill":
        char.health = 0
    else:
        for p_move in char_connect():
            if p_move == player_move:
                char.position = p_move
                print(char.position)
                print("step 1")
                p_converted = output_convert(char.position)
                print("step 2")
                pos_setter(p_converted)
                print("step 3")
                print("player moved")
                break

        print(char.category)
        print(char.position)

        print("Next Turn")

while char.health > 0:
    level_movement()
    print(char.category)
    print(char.position)   

print("Game Over")
