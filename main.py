import random
import time
import sys
import os
import platform
import textwrap
import cmd
from classes import human, orc, elf, wolf, zombie, wraith
from area import rooms
from say import say
from items import items
from dice import dice_rolls, print_dice_rolls, Die

##############
##          ##
##  STATIC  ##
##          ##
##############

asdf = platform.system()

if asdf is "Windows":
    clear_command = "cls"
else:
    clear_command = "clear"

def text_printer(text):
    for character in text:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)

def text_printer_a(text):
    for character in text:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.02)

def title_screen():
    os.system(clear_command)

    title_text = '''
    #########################
    # WELCOME TO PYTHON RPG #
    #########################
    #                       #
    #       - PLAY -        #
    #       - HELP -        #
    #       - QUIT -        #
    #                       #
    #########################

    '''
    print(title_text)

    option_a = input("=> ")
    option = option_a.lower()

    if option == "play":
        first_boot()
    elif option == "help":
        help_menu()
    elif option == "quit":
        sys.exit()
    else:
        text_to_print = ("Please pick a valid option from the menu!\n")

        text_printer(text_to_print)

        time.sleep(3)
        title_screen()

def help_menu():
    os.system(clear_command)

    text_to_print = ("This is a help menu\n")

    text_printer(text_to_print)

    option_a = input("=> ")
    option = option_a.lower()

    if option == "done":
        title_screen()
    else:
        text_to_print = "Please type in a valid command.\n"

        text_printer(text_to_print)

        time.sleep(3)
        help_menu()

def set_global_race(c_race):
    global race
    race = c_race

def set_global_call(character):
    global char
    char = character

def race_pick():
    os.system(clear_command)

    text_to_print = "What's your name mortal?\n"

    text_printer(text_to_print)
    name_player = input("=> ")

    text_to_print = '''
    Pick a race for your character.
    (Human, Elf or Orc.)
    '''
    text_printer(text_to_print)

    c_pick_a = input("=> ")
    c_pick = c_pick_a.lower()

    if c_pick == "human":
        set_global_race(c_pick)
        c_class = eval(race)
        set_global_call(c_class(name_player))

    elif c_pick == "elf":
        set_global_race(c_pick)
        c_class = eval(race)
        set_global_call(c_class(name_player))

    elif c_pick == "orc":
        set_global_race(c_pick)
        c_class = eval(race)
        set_global_call(c_class(name_player))

    else:
        text_to_print = "Please choose a valid race.\n"
        
        text_printer(text_to_print)

        time.sleep(3)
        race_pick()

##################
##              ##
##  Functions   ##
##              ##
##################

def money_functionality(gp):
    print("----------")

    gained_gp = gp

    gp += char.money_b
    new_gp, leftover_gp = divmod(gp, 100)
    new_gp += char.money_a

    if gp >= 100:

        char.money_a = new_gp
        char.money_b = 0
        char.money_b += leftover_gp

        text_to_print = '''
    You found some coins
    Currently you have {} gold and {} copper coins.
    '''.format(char.money_a, char.money_b)
        text_printer(text_to_print)
    
    elif gained_gp == 0:
        text_to_print = '''
    You have {} gold and {} copper coins.
    '''.format(char.money_a, char.money_b) 

        text_printer(text_to_print)

    else:
        char.money_b = gp

        text_to_print = '''
    You gained {} copper coins.
    You now have {} gold and {} copper coins.
    '''.format(gained_gp, char.money_a, char.money_b)

        text_printer(text_to_print)

    time.sleep(3)

def check_lvl(x):
    global level_up, exp_leftover
    
    print("----------")

    gained_exp = x
    x += char.exp
    level_up, exp_leftover = divmod(x, 100)
    level_up += char.level

    if x >= 100:

        char.level = level_up
        char.exp = 0
        char.exp += exp_leftover

        lvl_up_text = '''
    You've Level'ed up!
    Current Level: {}
    Current Experiance: {}'''.format(char.level, char.exp)
        
        text_printer(lvl_up_text)        

    elif gained_exp == 0:
        level_check = '''
    Current Level: {}
    Current Experiance: {}'''.format(char.level, char.exp)

        text_printer(level_check)

    else:
        char.exp = x
        
        exp_left_text = '''
    You've gained {} experiance.
    Current Experiance: {}.'''.format(gained_exp, char.exp)

        text_printer(exp_left_text)
    
    time.sleep(3)

def current_pos(cat, pos):
    if cat in rooms:
        if pos in rooms[cat]:
            y = rooms[cat][pos]
            return y
    else:
        print("not found")

def connect_pos(z):
    w = z["connects"].values()
    return w

def output_convert(from_to):
    if from_to in ["alleyway_1", "alleyway_2"]:
        from_to = "alley"
        char.category = from_to
    elif from_to in ["hall", "closet", "bedroom"]:
        from_to = "house"
        char.category = from_to
    elif from_to in ["living_room_1", "living_room_2", "living_room_3", "living_room_4"]:
        from_to = "living_room"
        char.category = from_to
    elif from_to in ["balcony_1", "balcony_2"]:
        from_to = "terrace"
        char.category = from_to
    elif from_to in ["spawn"]:
        from_to = "spawner"
        char.category = from_to
    else:
        print("missing input")

def char_position():
    char_pos = current_pos(cat, pos)
    return char_pos

def char_connect():
    char_position_a = char_position()
    connect_pos_a = connect_pos(char_position_a)
    return connect_pos_a

def search():
    interactive = char_position()

    if (interactive["solved"] is True) and (interactive["interact"] is ""):
        text_to_print = "You've already searched this area.\n"

        text_printer(text_to_print)
    else:
        text_to_print = "You've searched the area.\n"

        text_printer(text_to_print)

        time.sleep(2)
        
        text_to_print = "...\n"

        text_printer(text_to_print)

        time.sleep(1)

        text_to_print = "....\n"

        text_printer(text_to_print)

        time.sleep(1)

        text_to_print = ".....\n"

        text_printer(text_to_print)

        time.sleep(1)
        
        if (interactive["interact"] is "") and (interactive["solved"] is False):
            text_to_print =  "Nothing found.\n"

            text_printer(text_to_print)

            interactive["solved"] = True

        else:
            text_to_print = "There is a {} here.\n".format(interactive["interact"])

            text_printer(text_to_print)

            if interactive["interact"] is ["zombie", "wolf", "wraith"]:
                print("Attack Stage")
                attack_stage()
            else:
                interactive["solved"] = True

    time.sleep(3)

def level_movement():
    global cat, pos
    cat = char.category
    pos = char.position

    current_position = char_position()
    text_to_print = "You are in the: {}.\n".format(current_position["name"])

    text_printer(text_to_print)

    text_to_print = "You can go to: {}\n".format(list(char_connect()))

    text_printer_a(text_to_print)

    text_to_print = "Next move: \n"

    text_printer(text_to_print)

    player_move = input("=> ")
    p_move = player_move.lower().split()

    if player_move is not "":    
        if p_move[0] == "kill":
            char.health = 0
        elif p_move[0] == "check":
            if len(p_move) <= 1:
                text_to_print = "You need a second argument to check."
                text_printer(text_to_print)
                time.sleep(3)
                os.system(clear_command)
                level_movement()
            else:
                if p_move[1] == "level":
                    check_lvl(0)
                elif p_move[1] == "money":
                    money_functionality(0)
                else:
                    text_to_print = "Please choose a valid command.\n"
                    text_printer(text_to_print)
                    time.sleep(3)
                    os.system(clear_command)
                    level_movement()
        elif p_move[0] == "search":
            search()
        elif p_move[0] == "me":
            char_table_armour = char.armour

            text_to_print = ("| " + "{:<15}".format('Body Part') + "| " + "{:<15}\n".format('Item'))
            text_printer_a(text_to_print.title())
            table_len = len("| " + "{:<15}".format('Body Part') + "| " + "{:<15}".format('Item'))
            text_to_print = (("-" * table_len) + "\n")
            text_printer_a(text_to_print.title())
            for k, v in char_table_armour.items():
                label = v
                text_to_print = ("| " + "{:<15}".format(k) + "| " + "{:<15}\n".format(label))
                text_printer_a(text_to_print.title())

        elif p_move[0]:
            for p_move[0] in char_connect():
                if p_move[0] == player_move.lower():
                    char.position = p_move[0]
                    output_convert(char.position)
                    break
            else:
                text_to_print = "Please choose a valid command.\n"
                text_printer(text_to_print)
                time.sleep(3)
                os.system(clear_command)
                level_movement()
        else:
                text_to_print = "Please choose a valid command.\n"
                text_printer(text_to_print)
                time.sleep(3)
                os.system(clear_command)
                level_movement()
    else:
        text_to_print = "Please choose a valid command.\n"
        text_printer(text_to_print)
        time.sleep(3)
        os.system(clear_command)
        level_movement()

def random_turn_speech():
    random_speech = random.choice(list(say[race].values()))
    return random_speech

##############
##          ##
##  Loops   ##
##          ##
##############

def first_boot():
    os.system(clear_command)

    text_to_print = "This is a first time booting the game\n"

    text_printer(text_to_print)

    option_a = input("=> ")
    option = option_a.lower()

    if option == "ready":
        race_pick()
        main_game_loop()
    else:
        text_to_print = "Please type in a valid command.\n"

        text_printer(text_to_print)

        time.sleep(3)
        first_boot()

def main_game_loop():
    while char.health > 0:
        os.system(clear_command)

        char.say(random_turn_speech())

        level_movement()

    text_to_print = "You've Died\nGame Over\n"

    text_printer(text_to_print)
    time.sleep(2)


def attack_stage():
    print("Attack begins")

    #attacking = True
    turn_decider = random.randint(1,2)

    #while attacking is True:
    if turn_decider == 1:
        who_turn("p_turn")
    else:
        who_turn("p_turn")

def who_turn(x_turn):
    if x_turn == "p_turn":
        print("Player's turn")

        sides = 6

        p_roll = random.sample(range(1, sides + 1), 3)
        e_roll = random.sample(range(1, sides + 1), 2)

        print("Player Rolled")
        print_dice_rolls(6, p_roll)

        print("Enemy Rolled")
        print_dice_rolls(6, e_roll)
        
        p_list = sorted(p_roll, reverse=True)
        e_list = sorted(e_roll, reverse=True)

        paired_dice = zip(p_list, e_list)

        p_wins = 0
        e_wins = 0

        for pair in paired_dice:
            p_pair, e_pair = pair

            if p_pair > e_pair:
                p_wins += 1
            else:
                e_wins += 1
        
        print("Player won {} and Enemy Lost {}".format(p_wins, e_wins))


###### MAP MOVEMENT ######
#      a1 - a2 - a3      #
#           |            #
#      b1 - b2 - b3      #
#           |    |       #
#      c1 - c2  c3       #
#      |    |    |       #
#      d1 - d2  d3       #
##########################


##################
##              ##
##  Boot Order  ##
##              ##
##################

attack_stage()

#title_screen()