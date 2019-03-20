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

# PLAYER GLOBAL CALLER

def set_global_race(c_race):
    global race
    race = c_race

def set_global_call(character):
    global char
    char = character

# ENEMY GLOBAL CALLER

def set_global_race_e(c_race_e):
    global race_e
    race_e = c_race_e

def set_global_call_e(character_e):
    global enem
    enem = character_e

# PLAYER RACE PICK

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

    if interactive["solved"] is True:
        text_to_print = "You've already cleared this area.\n"

        text_printer(text_to_print)
    else:
        text_to_print = "You're searching the area.\n"

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

            if interactive["interact"] in ("zombie", "wolf", "wraith"):
                if interactive["interact"] == "zombie":
                    c_pick_e = "zombie"
                    set_global_race_e(c_pick_e)
                    c_class_e = eval(race_e)
                    set_global_call_e(c_class_e("Zombie"))
                
                    text_printer("BATTLE BEGINS!")
                    time.sleep(2)
                    os.system(clear_command)
                    attack_stage()
                    if enem.health <= 0:
                        interactive["solved"] = True
                        text_printer("Area Cleared!\n")
                    else:
                        interactive["solved"] = False
                elif interactive["interact"] == "wolf":
                    c_pick_e = "wolf"
                    set_global_race_e(c_pick_e)
                    c_class_e = eval(race_e)
                    set_global_call_e(c_class_e("Wolf"))

                    text_printer("BATTLE BEGINS!")
                    time.sleep(2)
                    os.system(clear_command)
                    attack_stage()
                    if enem.health <= 0:
                        interactive["solved"] = True
                        text_printer("Area Cleared!\n")
                    else:
                        interactive["solved"] = False
                elif interactive["interact"] == "wraith":
                    c_pick_e = "wraith"
                    set_global_race_e(c_pick_e)
                    c_class_e = eval(race_e)
                    set_global_call_e(c_class_e("Wraith"))

                    text_printer("BATTLE BEGINS!")
                    time.sleep(2)
                    os.system(clear_command)
                    attack_stage()
                    if enem.health <= 0:
                        interactive["solved"] = True
                        text_printer("Area Cleared!\n")
                    else:
                        interactive["solved"] = False
                
                else:
                    print("Enemy not found? Error Maybe")
            elif interactive["interact"] is "chest":
                text_printer("Do you want to open it?")
                chest_input = input("=> ")

                if chest_input.lower() == "yes":
                    print("You've Opened the chest")
                    time.sleep(2)

                    chest_item_a = random.choice(list(items.values()))
                    chest_item_b = random.choice(list(chest_item_a.values()))
                    chest_item_name = chest_item_b["name"]
                    chest_item_slot = chest_item_b["slot"]
                    text_printer("You found a {}".format(chest_item_name))
                    text_to_print = '''
                    {} goes in {}.
                    You currently have {} in {}.
                    Do you want to wear it?
                    Or put it in a bag?
                    (Write 'wear' or 'bag')
                    '''.format(chest_item_name, chest_item_slot, char.armour[chest_item_slot].values(), char.armour[chest_item_slot].key())

                    text_printer(text_to_print)
                    
                    char_input_action = input("=> ")
                    if char_input_action == "wear":
                        char.armour[chest_item_slot].values = chest_item_name
                        text_printer("{} put {} on.".format(char.name, chest_item_name))
                        time.sleep(3)
                        interactive["solved"] = True
                    elif char_input_action == "bag":
                        mydict = char.bag
                        find_empty_bag = list(mydict.keys())[list(mydict.values()).index("empty")]
                        char.bag[find_empty_bag].values = chest_item_name
                        text_printer("{} put {} in the bag".format(char.name, chest_item_name))
                        time.sleep(3)
                        interactive["solved"] = True
                    else:
                        text_printer("Write a valid command.")
                        time.sleep(2)
                        interactive["solved"] = False
                        return
                    
                elif chest_input.lower() == "no":
                    print("You stepped away from a closed chest")
                    interactive["solved"] = False
                    time.sleep(3)
                    return
                else:
                    print("Please use a valid command.")
                    time.sleep(2)
                    search()
            else:
                print("Other Search Bit...")

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
            text_to_print = '''
            Your name is {}. You are an {} {}.
            You are currently in the {}.
            You have {} copper and {} gold coins.
            You have {} health and {} mana.
            You are {} level and have {} experiance.
            \n'''.format(char.name, char.species, char.job, current_position["name"], char.money_a, char.money_b, char.health, char.mana, char.level, char.exp)
            text_printer(text_to_print)
            time.sleep(3)

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

            time.sleep(5)

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
    text_printer("Attack begins\n")

    turn_decider = random.randint(1,2)

    if turn_decider == 1:
        who_turn("p_turn", 0, False, False)
    else:
        who_turn("e_turn", 0, False, False)

## CALL FUNCTION WHEN ITEM PUT ON CHAR ARMOUR SLOT
## ADD DAMAGE ONLY WHEN PUT ON
## ADD DEFENCE ONLY WHEN PUT ON

def character_damage_calc():
    current_dmg = 0
    current_defence = 0

    armour_table = char.armour

    for k, x in armour_table.items():
        if x == "nothing":
            continue
        else:
            items_table_stat = items[k]
            search_stat = items_table_stat[x]

            if "defence" in search_stat:
                new_stat = search_stat["defence"]
                current_defence += new_stat
            elif "damage" in search_stat:
                new_stat = search_stat["damage"]
                current_dmg += new_stat
    char.damage += current_dmg
    char.defence += current_defence

def who_turn(x_turn, had_turn, enem_dead, play_dead):
    global next_turn, call_turn

    call_turn = x_turn
    if play_dead == False:
        if enem_dead == False:
            if had_turn < 2:

                if x_turn == "p_turn":
                    text_printer("Player's turn\n")

                    next_turn = "e_turn"

                    dice_game("both")

                    if p_wins == e_wins:
                        text_printer("Round Draw.\n")

                        p_dmg_done = char.damage * p_wins
                        e_dmg_done = enem.damage * e_wins
                        
                        if apply_unique_stats(char.c_strike):
                            text_printer("You feel the God's power within you.\n")
                            p_dmg_done = p_dmg_done + (p_dmg_done * 0.25)
                            time.sleep(2)
                        
                        if apply_unique_stats(char.luck):
                            text_printer("You got lucky, and can throw your dice again!\n")
                            text_printer("Type throw if you want to throw your dice again.\n")
                            if input("=> ") == "throw":
                                dice_game("player")
                                
                                p_dmg_done = char.damage * p_wins
                                e_dmg_done = enem.damage * e_wins

                                time.sleep(3)

                        if apply_unique_stats(char.speed):
                            text_printer("You've dodged the enemy's attack.\n")
                            e_dmg_done = 0
                            time.sleep(3)
                            
                        dmg_difference_p = p_dmg_done - e_dmg_done
                        if dmg_difference_p >= 0:
                            enem.health = enem.health - dmg_difference_p
                        else:
                            dmg_difference_p = 0

                        dmg_difference_e = e_dmg_done - p_dmg_done
                        if dmg_difference_e >= 0:
                            char.health = char.health - dmg_difference_e
                        else:
                            dmg_difference_e = 0

                        text_printer("You've dealt {} damage\n".format(dmg_difference_p))
                        text_printer("Enemy has {} health remaining.\n".format(enem.health))
                        text_printer("The enemy dealt {} damage.\n".format(dmg_difference_e))
                        text_printer("You have {} health remaining.\n".format(char.health))

                    elif p_wins > e_wins:
                        text_printer("Player Wins The Round.\n")

                        p_dmg_done = char.damage * p_wins
                        e_dmg_done = 0
                        
                        if apply_unique_stats(char.c_strike):
                            text_printer("You feel the God's power within you.\n")
                            p_dmg_done = p_dmg_done + (p_dmg_done * 0.25)

                        dmg_difference_p = p_dmg_done - e_dmg_done
                        if dmg_difference_p >= 0:
                            enem.health = enem.health - dmg_difference_p
                        else:
                            dmg_difference_p = 0

                        text_printer("You've dealt {} damage\n".format(dmg_difference_p))
                        text_printer("Enemy has {} health remaining.\n".format(enem.health))

                    elif p_wins < e_wins:
                        p_dmg_done = 0
                        e_dmg_done = enem.damage * e_wins
                        
                        if apply_unique_stats(char.luck):
                            text_printer("You got lucky, and can throw your dice again!\n")
                            text_printer("Type throw if you want to throw your dice again.\n")
                            if input("=> ") == "throw":
                                dice_game("player")

                                p_dmg_done = char.damage * p_wins
                                e_dmg_done = enem.damage * e_wins

                                time.sleep(3)

                        if apply_unique_stats(char.speed):
                            text_printer("You've dodged the enemy's attack.\n")
                            e_dmg_done = enem.damage * (e_wins - 1)
                        
                        dmg_difference_e = e_dmg_done - p_dmg_done
                        if dmg_difference_e >= 0:
                            char.health = char.health - dmg_difference_e
                        else:
                            dmg_difference_e = 0

                        text_printer("The enemy dealt {} damage.\n".format(dmg_difference_e))
                        text_printer("You have {} health remaining.\n".format(char.health))

                    if enem.health <= 0:
                        text_printer("Enemy Killed!\n")
                        time.sleep(2)
                        check_lvl(enem.exp)
                        enem_dead = True
                        return
                    elif char.health <= 0:
                        play_dead = True
                        return
                        
                    time.sleep(3)
                    os.system(clear_command)
                    had_turn += 1
                    who_turn(next_turn, had_turn, False, False)
                elif x_turn == "e_turn":
                    text_printer("Enemy's turn.\n")

                    next_turn = "p_turn"

                    dice_game_e("both")

                    if p_wins_e == e_wins_e:
                        text_printer("Round Draw.\n")

                        p_dmg_done = char.damage * p_wins_e
                        e_dmg_done = enem.damage * e_wins_e
                        
                        if apply_unique_stats(char.c_strike):
                            text_printer("You feel the God's power within you.\n")
                            p_dmg_done = p_dmg_done + (p_dmg_done * 0.25)
                            time.sleep(2)
                        
                        if apply_unique_stats(char.luck):
                            text_printer("You got lucky, and can throw your dice again!\n")
                            text_printer("Type throw if you want to throw your dice again.\n")
                            if input("=> ") == "throw":
                                dice_game("player")
                                
                                p_dmg_done = char.damage * p_wins_e
                                e_dmg_done = enem.damage * e_wins_e

                                time.sleep(3)

                        if apply_unique_stats(char.speed):
                            text_printer("You've dodged the enemy's attack.\n")
                            e_dmg_done = 0
                            time.sleep(3)
                            
                        dmg_difference_p = p_dmg_done - e_dmg_done
                        if dmg_difference_p >= 0:
                            enem.health = enem.health - dmg_difference_p
                        else:
                            dmg_difference_p = 0

                        dmg_difference_e = e_dmg_done - p_dmg_done
                        if dmg_difference_e >= 0:
                            char.health = char.health - dmg_difference_e
                        else:
                            dmg_difference_e = 0

                        text_printer("You've dealt {} damage\n".format(dmg_difference_p))
                        text_printer("Enemy has {} health remaining.\n".format(enem.health))
                        text_printer("The enemy dealt {} damage.\n".format(dmg_difference_e))
                        text_printer("You have {} health remaining.\n".format(char.health))

                    elif p_wins_e > e_wins_e:
                        text_printer("Player Wins The Round.\n")

                        p_dmg_done = char.damage * p_wins_e
                        e_dmg_done = 0
                        
                        if apply_unique_stats(char.c_strike):
                            text_printer("You feel the God's power within you.\n")
                            p_dmg_done = p_dmg_done + (p_dmg_done * 0.25)

                        dmg_difference_p = p_dmg_done - e_dmg_done
                        if dmg_difference_p >= 0:
                            enem.health = enem.health - dmg_difference_p
                        else:
                            dmg_difference_p = 0

                        text_printer("You've dealt {} damage\n".format(dmg_difference_p))
                        text_printer("Enemy has {} health remaining.\n".format(enem.health))

                    elif p_wins_e < e_wins_e:
                        p_dmg_done = 0
                        e_dmg_done = enem.damage * e_wins_e
                        
                        if apply_unique_stats(char.luck):
                            text_printer("You got lucky, and can throw your dice again!\n")
                            text_printer("Type throw if you want to throw your dice again.\n")
                            if input("=> ") == "throw":
                                dice_game("player")

                                p_dmg_done = char.damage * p_wins_e
                                e_dmg_done = enem.damage * e_wins_e

                                time.sleep(3)

                        if apply_unique_stats(char.speed):
                            text_printer("You've dodged the enemy's attack.\n")
                            e_dmg_done = enem.damage * (e_wins_e - 1)
                        
                        dmg_difference_e = e_dmg_done - p_dmg_done
                        if dmg_difference_e >= 0:
                            char.health = char.health - dmg_difference_e
                        else:
                            dmg_difference_e = 0

                        text_printer("The enemy dealt {} damage.\n".format(dmg_difference_e))
                        text_printer("You have {} health remaining.\n".format(char.health))

                    if enem.health <= 0:
                        text_printer("Enemy Killed!\n")
                        time.sleep(2)
                        check_lvl(enem.exp)
                        enem_dead = True
                        return
                    elif char.health <= 0:
                        play_dead = True
                        return

                    time.sleep(3)
                    os.system(clear_command)
                    had_turn += 1
                    who_turn(next_turn, had_turn, False, False)

            else:
                text_printer("Attack again? or walk away?\n")
                text_printer_a("Type 'Attack' to go again.\n")
                text_printer_a("Type 'Walk' to walk away.\n")
                p_input_dice = input("=> ")

                if p_input_dice.lower() == "attack":
                    text_printer("New Turn Begins.\n")
                    time.sleep(2)
                    os.system(clear_command)
                    who_turn(next_turn, 0, False, False)
                elif p_input_dice.lower() == "walk":
                    text_printer("You walk away in shame.\n")
                    time.sleep(2)
                    os.system(clear_command)
                    return
                else:
                    text_printer_a("Please type a valid command!\n")
                    time.sleep(2)
                    os.system(clear_command)
                    who_turn(call_turn, 2, False, False)
        else:
            return
    else:
        return

def apply_unique_stats(probability):
    return random.random() < probability

def dice_game(who_lucky):
    global p_wins, e_wins, e_roll, p_roll

    sides = 6

    if who_lucky == "both":
        p_roll = random.sample(range(1, sides + 1), 3)
        e_roll = random.sample(range(1, sides + 1), 2)

        text_printer("Player Rolled.\n")
        print_dice_rolls(6, p_roll)
        time.sleep(3)

        text_printer("Enemy Rolled.\n")
        print_dice_rolls(6, e_roll)
        time.sleep(3)
        
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
        
        text_printer("Player won {} and Enemy won {}.\n".format(p_wins, e_wins))
        return p_wins, e_wins

    elif who_lucky == "player":
        p_roll = random.sample(range(1, sides + 1), 3)

        text_printer("Player's New Roll.\n")
        print_dice_rolls(6, p_roll)
        time.sleep(3)

        text_printer("Enemy's Previous Roll.\n")
        print_dice_rolls(6, e_roll)
        time.sleep(3)

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
        
        text_printer("Player won {} and Enemy won {}.\n".format(p_wins, e_wins))
        return p_wins, e_wins

    elif who_lucky == "enemy":
        e_roll = random.sample(range(1, sides + 1), 2)

        text_printer("Player's Previous Roll.\n")
        print_dice_rolls(6, p_roll)
        time.sleep(3)

        text_printer("Enemy's New Roll.\n")
        print_dice_rolls(6, e_roll)
        time.sleep(3)

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
        
        text_printer("Player won {} and Enemy won {}.\n".format(p_wins, e_wins))
        return p_wins, e_wins

def dice_game_e(who_lucky_e):
    global p_wins_e, e_wins_e, e_roll_e, p_roll_e

    sides = 6

    if who_lucky_e == "both":
        e_roll_e = random.sample(range(1, sides + 1), 3)
        p_roll_e = random.sample(range(1, sides + 1), 2)

        text_printer("Player Rolled.\n")
        print_dice_rolls(6, p_roll_e)
        time.sleep(3)

        text_printer("Enemy Rolled.\n")
        print_dice_rolls(6, e_roll_e)
        time.sleep(3)
        
        p_list = sorted(p_roll_e, reverse=True)
        e_list = sorted(e_roll_e, reverse=True)

        paired_dice = zip(p_list, e_list)

        p_wins_e = 0
        e_wins_e = 0

        for pair in paired_dice:
            p_pair, e_pair = pair

            if p_pair > e_pair:
                p_wins_e += 1
            else:
                e_wins_e += 1
        
        text_printer("Player won {} and Enemy won {}.\n".format(p_wins_e, e_wins_e))
        return p_wins_e, e_wins_e

    elif who_lucky_e == "player":
        p_roll_e = random.sample(range(1, sides + 1), 2)

        text_printer("Player's New Roll.\n")
        print_dice_rolls(6, p_roll_e)
        time.sleep(3)

        text_printer("Enemy's Previous Roll.\n")
        print_dice_rolls(6, e_roll_e)
        time.sleep(3)

        p_list = sorted(p_roll_e, reverse=True)
        e_list = sorted(e_roll_e, reverse=True)

        paired_dice = zip(p_list, e_list)

        p_wins_e = 0
        e_wins_e = 0

        for pair in paired_dice:
            p_pair, e_pair = pair

            if p_pair > e_pair:
                p_wins_e += 1
            else:
                e_wins_e += 1
        
        text_printer("Player won {} and Enemy won {}.\n".format(p_wins_e, e_wins_e))
        return p_wins_e, e_wins_e

    elif who_lucky_e == "enemy":
        e_roll_e = random.sample(range(1, sides + 1), 3)

        text_printer("Player's Previous Roll.\n")
        print_dice_rolls(6, p_roll_e)
        time.sleep(3)

        text_printer("Enemy's New Roll.\n")
        print_dice_rolls(6, e_roll_e)
        time.sleep(3)

        p_list = sorted(p_roll_e, reverse=True)
        e_list = sorted(e_roll_e, reverse=True)

        paired_dice = zip(p_list, e_list)

        p_wins_e = 0
        e_wins_e = 0

        for pair in paired_dice:
            p_pair, e_pair = pair

            if p_pair > e_pair:
                p_wins_e += 1
            else:
                e_wins_e += 1
        
        text_printer("Player won {} and Enemy won {}.\n".format(p_wins_e, e_wins_e))
        return p_wins_e, e_wins_e


##########################
#####  MAP MOVEMENT  #####
##########################
#                        #
#      a1 - a2 - a3      #
#           |            #
#      b1 - b2 - b3      #
#           |    |       #
#      c1 - c2  c3       #
#      |    |    |       #
#      d1 - d2  d3       #
#                        #
##########################


##################
##              ##
##  Boot Order  ##
##              ##
##################


## FOR TESTING PURPOSES
'''
c_pick_e = "zombie"
set_global_race_e(c_pick_e)
c_class_e = eval(race_e)
set_global_call_e(c_class_e("Zombie"))


c_pick = "human"
set_global_race(c_pick)
c_class = eval(race)
set_global_call(c_class("asdf"))

attack_stage()
'''

## GAME START TRIGGER
title_screen()