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
from encounters import encounters

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
    elif option == "skip":
        race_pick()
        main_game_loop()
    elif option == "quit":
        sys.exit()
    else:
        text_to_print = ("Please pick a valid option from the menu!\n")

        text_printer(text_to_print)

        time.sleep(3)
        title_screen()

def help_menu():
    os.system(clear_command)

    print('''
    Commands:
    => location_name - Moves the character to the location 
                       (only if available)
    => me - Displays general information about your character
            as well as current worn armour and backpack content
    => search - Your character searches the current area
    => check level - Displays your current level and experience
    => check money - Displays your current copper and gold coins
    => help - Displays this list again

    (Type 'Done' when ready to continue.)
    ''')

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
    {}, huh? Okey...
    What race are you? We never had your kind here.
    (Human, Elf or Orc.)
    '''.format(name_player)
    text_printer(text_to_print)

    picking = False
    
    while picking == False:
        c_pick_a = input("=> ")
        c_pick = c_pick_a.lower()

        if c_pick == "human":
            set_global_race(c_pick)
            c_class = eval(race)
            set_global_call(c_class(name_player))
            picking = True

        elif c_pick == "elf":
            set_global_race(c_pick)
            c_class = eval(race)
            set_global_call(c_class(name_player))
            picking = True

        elif c_pick == "orc":
            set_global_race(c_pick)
            c_class = eval(race)
            set_global_call(c_class(name_player))
            picking = True

        else:
            text_printer("Please choose a valid race.\n")
            picking = False

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
        text_to_print = "\nYou've already cleared this area.\n"

        text_printer(text_to_print)
        time.sleep(3)
    else:
        text_to_print = "\nYou're searching the area.\n"

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

                    text_printer("BATTLE BEGINS!\n")
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
                text_printer("Do you want to open it?\n")

                opening = False
                while opening == False:
                    chest_input = input("=> ")

                    if chest_input.lower() == "yes":
                        text_printer("You've opened the chest.\n")
                        time.sleep(2)

                        items_found = 1

                        while items_found <= 3:

                            chest_item_a = random.choice(list(items.values()))
                            chest_item_b = random.choice(list(chest_item_a.values()))
                            chest_item_name = chest_item_b["name"]
                            chest_item_slot = chest_item_b["slot"]
                            
                            if chest_item_slot == "bag":
                                text_printer("You found a {} potion.\n".format(chest_item_name))
                                text_printer("(You can only 'bag' this item.)\n")
                                char_input_action = input("=> ")
                                
                                potion_bag = False
                                while potion_bag == False:
                                    if char_input_action == "bag":
                                        mydict = char.bag
                                        find_empty_bag = list(mydict.keys())[list(mydict.values()).index("empty")]
                                        char.bag[find_empty_bag] = chest_item_name
                                        text_printer("{} put {} potion in the bag.\n".format(char.name, chest_item_name))
                                        time.sleep(3)
                                        interactive["solved"] = True
                                        potion_bag = True
                                        opening = True
                                    else:
                                        text_printer("Write a valid command.\n")
                                        interactive["solved"] = False

                            else:
                                text_printer("You found a {}.\n".format(chest_item_name))
                                text_to_print = '''
                {} goes in {}.
                You currently have {} in {}.
                Do you want to wear it?
                Or put it in a bag?
                (Write 'wear' or 'bag')
                '''.format(chest_item_name, chest_item_slot, char.armour[chest_item_slot], chest_item_slot)

                                text_printer(text_to_print)
                                
                                wear_or_bag = False

                                while wear_or_bag == False:
                                    char_input_action = input("=> ")
                                    if char_input_action == "wear":
                                        stat_calc(chest_item_name, chest_item_slot)

                                        text_printer("{} put {} on.\n".format(char.name, chest_item_name))

                                        time.sleep(3)
                                        interactive["solved"] = True
                                        wear_or_bag = True
                                        opening = True
                                    elif char_input_action == "bag":
                                        mydict = char.bag
                                        find_empty_bag = list(mydict.keys())[list(mydict.values()).index("empty")]
                                        char.bag[find_empty_bag] = chest_item_name
                                        text_printer("{} put {} in the bag.\n".format(char.name, chest_item_name))
                                        time.sleep(3)
                                        interactive["solved"] = True
                                        wear_or_bag = True
                                        opening = True
                                    else:
                                        text_printer("Write a valid command.\n")
                            
                            items_found += 1
                        
                    elif chest_input.lower() == "no":
                        print("You stepped away from a closed chest.\n")
                        interactive["solved"] = False
                        time.sleep(3)
                        opening = True
                        return
                    else:
                        print("Please use a valid command.\n")
            elif interactive["interact"] is "weapons_chest":
                text_printer("Do you want to open it?\n")
                
                opening = False
                while opening == False:
                    chest_input = input("=> ")

                    if chest_input.lower() == "yes":
                        text_printer("You've opened the chest.\n")
                        time.sleep(2)

                        chest_item_a = items["right_hand"]
                        chest_item_b = random.choice(list(chest_item_a.values()))
                        chest_item_name = chest_item_b["name"]
                        chest_item_slot = chest_item_b["slot"]
                        
                        text_printer("You found a {}.\n".format(chest_item_name))
                        text_to_print = '''
        {} goes in {}.
        You currently have {} in {}.
        Do you want to wear it?
        Or put it in a bag?
        (Write 'wear' or 'bag')
        '''.format(chest_item_name, chest_item_slot, char.armour[chest_item_slot], chest_item_slot)

                        text_printer(text_to_print)

                        wear_or_bag = False
                        while wear_or_bag == False:
                            char_input_action = input("=> ")
                            if char_input_action == "wear":
                                stat_calc(chest_item_name, chest_item_slot)

                                text_printer("{} put {} on.\n".format(char.name, chest_item_name))

                                time.sleep(3)
                                interactive["solved"] = True
                                wear_or_bag = True
                            elif char_input_action == "bag":
                                mydict = char.bag
                                find_empty_bag = list(mydict.keys())[list(mydict.values()).index("empty")]
                                char.bag[find_empty_bag] = chest_item_name
                                text_printer("{} put {} in the bag.\n".format(char.name, chest_item_name))
                                time.sleep(3)
                                interactive["solved"] = True
                                wear_or_bag = True
                            else:
                                text_printer("Write a valid command.\n")
                                interactive["solved"] = False
                        
                    elif chest_input.lower() == "no":
                        print("You stepped away from a closed chest.\n")
                        interactive["solved"] = False
                        time.sleep(3)
                        opening = True
                        return
                    else:
                        print("Please use a valid command.\n")
                
            else:
                print("Other Search Bit...")

def stat_calc(item_name, item_slot):
    armour_t = char.armour
    if armour_t[item_slot] == "nothing":
        armour_t[item_slot] = item_name

        stat = items[item_slot][item_name]

        if "defence" in stat:
            new_stat = stat["defence"]
            char.defence += new_stat
        
        elif "damage" in stat:
            new_stat = stat["damage"]
            char.damage += new_stat
                
        else:
            print("Stat error")
    
    else:
        old_item = armour_t[item_slot]

        mydict = char.bag
        find_empty_bag = list(mydict.keys())[list(mydict.values()).index("empty")]
        char.bag[find_empty_bag] = old_item

        armour_t[item_slot] = "nothing"

        stat_calc(item_name, item_slot)

def char_me_func(x,y):
    char_table_armour = x

    text_to_print = ("| " + "{:<15}".format(y) + "| " + "{:<15}\n".format('Item'))
    text_printer_a(text_to_print.title())
    table_len = len("| " + "{:<15}".format(y) + "| " + "{:<15}".format('Item'))
    text_to_print = (("-" * table_len) + "\n")
    text_printer_a(text_to_print.title())
    for k, v in char_table_armour.items():
        label = v
        text_to_print = ("| " + "{:<15}".format(k) + "| " + "{:<15}\n".format(label))
        text_printer_a(text_to_print.title())

def bag_action():
    char_me_func(char.bag, "Slot")

    text_printer('''
    Please input the slot of an item you wish to use.
    Or type 'exit' to leave this window
    ''')
    while True:
        try:
            bag_choice = input("=> ")
            bag_choice_int = int(bag_choice)

            if char.bag[bag_choice_int] == "empty":
                text_printer("This slot is empty.\n Pick a different slot.\n")
            elif bag_choice_int in range(1,12):
                char_bag_choice = char.bag[bag_choice_int]
                items_bag_choice = items["potions"][char_bag_choice]
                bag_item_name = items_bag_choice["name"]
                bag_item_name_low = items_bag_choice["name"].lower()

                text_printer("You can use the {} potion to gain {} {} or leave it for another time\n".format(bag_item_name,items_bag_choice[bag_item_name_low],bag_item_name))
                text_printer_a("(Write 'use' or 'leave')\n")
                use_choice = input("=> ")

                if use_choice == "use":
                    stat_added = items_bag_choice[bag_item_name_low]
                    
                    char_stat_setter(bag_item_name_low, stat_added)

                    char.bag[bag_choice_int] = "empty"

                    text_printer("You've used the item\n")
                elif use_choice == "leave":
                    text_printer("You left it for later\n")
                else:
                    text_printer("Invalid command.\n")
            elif bag_choice == "exit":
                return

            break
        except ValueError:
            text_printer("\nChoose a valid slot.\n")

    time.sleep(2)

def char_stat_setter(x,y):
    if x == "health":
        char.health += y
        if char.health > 100:
            char.health = 100
    elif x == "mana":
        char.mana += y
        if char.mana > 100:
            char.mana = 100
    elif x == "c_strike":
        char.c_strike += y
        if char.c_strike > 1:
            char.c_strike = 1
    elif x == "luck":
        char.luck += y
        if char.luck > 1:
            char.luck = 1
    elif x == "speed":
        char.speed += y
        if char.speed > 1:
            char.speed = 1

def level_movement():
    global cat, pos
    cat = char.category
    pos = char.position

    current_position = char_position()
    text_to_print = '''
    You are in the: {}.
    You can go to: {}
    Next move: 
    '''.format(current_position["name"],list(char_connect()))

    text_printer(text_to_print)

    player_move = input("=> ")
    p_move = player_move.lower().split()

    if player_move is not "":    
        if p_move[0] == "kill":
            char.health = 0
        elif p_move[0] == "help":
            help_menu()
        elif p_move[0] == "bag":
            bag_action()
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
            You deal {} damage and have {} defence.
            \n'''.format(char.name, char.species, char.job, current_position["name"], 
                            char.money_a, char.money_b, char.health, char.mana, 
                            char.level, char.exp, char.damage, char.defence)
            text_printer(text_to_print)
            time.sleep(3)

            char_me_func(char.armour,"Body Part")
            print("\n")
            char_me_func(char.bag, "Slot")
            
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

    text_to_print = '''
    (See 'help' to learn all commands available)

    You wake up in a strange village.
    You feel confused and lost.

    You look around to see if there are any villagers around,
    but see no one. Instead you see rotten food around the alleyway,
    grass growing onto the houses, and broken doors and windows.
    
    The village smells of rotten bodies and food.
    Something does not feel right about this village.

    You turn away from the disgusting village in front of you
    in attempt to walk away from the nightmare, but a magical sphere
    holds you hostage in nightmare village.

    You look around to find answers.
        Where am I?
        Why am I here?
        Why can't I leave?
        What is going on here?

    The questions in your mind never stop.
    You decide to explore the village and see what is happening.
    See if there is a way out and going back to your normal life.

    As you prepare to step forwards towards the village your sight
    blurs and a vision of a tall humanoid in robes appears
    in front of you. You can't see his face or what it is.
    Nothing other than a silhouette.

    You hear it speak like its right in front of you.
    It asks you a series of questions which you answer in fear.
    After which the vision disappears leaving you stranded in 
    the nightmare village you hoped was only a bad dream.

    After regaining your conciousness, you think to yourself
    what the creature have asked.

    (Type 'ready' when you're ready to start the journey)
    '''

    text_printer_a(text_to_print)

    ready = False
    
    while ready == False:
        option_a = input("=> ")
        option = option_a.lower()

        if option == "ready":
            race_pick()
            main_game_loop()
            ready = True
        else:
            text_printer("Please type in a valid command.\n")
            ready = False

def main_game_loop():
    while char.health > 0:
        os.system(clear_command)

        char.say(random_turn_speech())

        level_movement()

    text_printer("You've Died\nGame Over\n")
    time.sleep(2)

def attack_stage():
    text_printer("Attack begins\n")

    turn_decider = random.randint(1,2)

    if turn_decider == 1:
        who_turn("p_turn", 0, False, False)
    else:
        who_turn("e_turn", 0, False, False)

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

                        if apply_unique_stats(enem.c_strike):
                            text_printer("Enemy strikes you with huge power..\n")
                            e_dmg_done = e_dmg_done + (e_dmg_done * 0.25)
                            time.sleep(2)
                        
                        if apply_unique_stats(char.luck):
                            text_printer("You got lucky, and can throw your dice again!\n")
                            print("(Answer 'throw' or 'skip')\n")
                            
                            choosing = False
                            while choosing == False:
                                player_input = input("=> ")
                                if player_input == "throw":
                                    dice_game("player")
                                    
                                    p_dmg_done = char.damage * p_wins
                                    e_dmg_done = enem.damage * e_wins

                                    time.sleep(3)
                                    choosing = True
                                elif player_input == "skip":
                                    choosing = True
                                else:
                                    print("Choose a valid command.\n")
                        
                        if apply_unique_stats(enem.luck):
                            text_printer("Enemy felt lucky and got to throw the dice again!\n")
                            dice_game("enemy")
                            
                            p_dmg_done = char.damage * p_wins_e
                            e_dmg_done = enem.damage * e_wins_e

                            time.sleep(3)

                        if apply_unique_stats(char.speed):
                            text_printer("You've dodged the enemy's attack.\n")
                            e_dmg_done = 0
                            time.sleep(3)

                        if apply_unique_stats(char.speed):
                            text_printer("Enemy dodged your attack.\n")
                            p_dmg_done = 0
                            time.sleep(3)
                            
                        dmg_difference_p = p_dmg_done - enem.defence
                        if dmg_difference_p >= 0:
                            enem.health = enem.health - dmg_difference_p
                        else:
                            dmg_difference_p = 0

                        dmg_difference_e = e_dmg_done - char.defence
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
                        
                        if apply_unique_stats(enem.luck):
                            text_printer("Enemy felt lucky and got to throw the dice again!\n")
                            dice_game("enemy")
                            
                            p_dmg_done = char.damage * p_wins_e
                            e_dmg_done = enem.damage * e_wins_e

                            time.sleep(3)

                        if apply_unique_stats(char.speed):
                            text_printer("Enemy dodged your attack.\n")
                            p_dmg_done = char.damage * (p_wins - 1)
                            time.sleep(3)

                        if apply_unique_stats(char.c_strike):
                            text_printer("You feel the God's power within you.\n")
                            p_dmg_done = p_dmg_done + (p_dmg_done * 0.25)
                        
                        dmg_difference_p = p_dmg_done - enem.defence
                        if dmg_difference_p >= 0:
                            enem.health = enem.health - dmg_difference_p
                        else:
                            dmg_difference_p = 0

                        dmg_difference_e = e_dmg_done - char.defence
                        if dmg_difference_e >= 0:
                            char.health = char.health - dmg_difference_e
                        else:
                            dmg_difference_e = 0

                        text_printer("You've dealt {} damage\n".format(dmg_difference_p))
                        text_printer("Enemy has {} health remaining.\n".format(enem.health))
                        text_printer("The enemy dealt {} damage.\n".format(dmg_difference_e))
                        text_printer("You have {} health remaining.\n".format(char.health))

                    elif p_wins < e_wins:
                        p_dmg_done = 0
                        e_dmg_done = enem.damage * e_wins

                        if apply_unique_stats(char.luck):
                            text_printer("You got lucky, and can throw your dice again!\n")
                            print("(Answer 'throw' or 'skip')\n")
                            
                            choosing = False
                            while choosing == False:
                                player_input = input("=> ")
                                if player_input == "throw":
                                    dice_game("player")
                                    
                                    p_dmg_done = char.damage * p_wins
                                    e_dmg_done = enem.damage * e_wins

                                    time.sleep(3)
                                    choosing = True
                                elif player_input == "skip":
                                    choosing = True
                                else:
                                    print("Choose a valid command.\n")

                        if apply_unique_stats(char.speed):
                            text_printer("You've dodged the enemy's attack.\n")
                            e_dmg_done = enem.damage * (e_wins - 1)
                        
                        if apply_unique_stats(enem.c_strike):
                            text_printer("Enemy strikes you with huge power..\n")
                            e_dmg_done = e_dmg_done + (e_dmg_done * 0.25)
                            time.sleep(2)
                        
                        dmg_difference_p = p_dmg_done - enem.defence
                        if dmg_difference_p >= 0:
                            enem.health = enem.health - dmg_difference_p
                        else:
                            dmg_difference_p = 0

                        dmg_difference_e = e_dmg_done - char.defence
                        if dmg_difference_e >= 0:
                            char.health = char.health - dmg_difference_e
                        else:
                            dmg_difference_e = 0

                        text_printer("You've dealt {} damage\n".format(dmg_difference_p))
                        text_printer("Enemy has {} health remaining.\n".format(enem.health))
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
                        
                        if apply_unique_stats(enem.c_strike):
                            text_printer("Enemy strikes you with huge power.\n")
                            e_dmg_done = e_dmg_done + (e_dmg_done * 0.25)
                            time.sleep(2)

                        if apply_unique_stats(char.luck):
                            text_printer("You got lucky, and can throw your dice again!\n")
                            print("(Answer 'throw' or 'skip')\n")
                            
                            choosing = False
                            while choosing == False:
                                player_input = input("=> ")
                                if player_input == "throw":
                                    dice_game("player")
                                    
                                    p_dmg_done = char.damage * p_wins
                                    e_dmg_done = enem.damage * e_wins

                                    time.sleep(3)
                                    choosing = True
                                elif player_input == "skip":
                                    choosing = True
                                else:
                                    print("Choose a valid command.\n")

                        if apply_unique_stats(enem.luck):
                            text_printer("Enemy felt lucky and got to throw the dice again!\n")
                            dice_game_e("enemy")
                            
                            p_dmg_done = char.damage * p_wins_e
                            e_dmg_done = enem.damage * e_wins_e

                            time.sleep(3)

                        if apply_unique_stats(char.speed):
                            text_printer("You've dodged the enemy's attack.\n")
                            e_dmg_done = 0
                            time.sleep(3)

                        if apply_unique_stats(char.speed):
                            text_printer("Enemy dodged your attack.\n")
                            p_dmg_done = 0
                            time.sleep(3)
                            
                        dmg_difference_p = p_dmg_done - enem.defence
                        if dmg_difference_p >= 0:
                            enem.health = enem.health - dmg_difference_p
                        else:
                            dmg_difference_p = 0

                        dmg_difference_p = p_dmg_done - enem.defence
                        if dmg_difference_p >= 0:
                            enem.health = enem.health - dmg_difference_p
                        else:
                            dmg_difference_p = 0

                        dmg_difference_e = e_dmg_done - char.defence
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
                            time.sleep(2)
                        
                        if apply_unique_stats(enem.luck):
                            text_printer("Enemy felt lucky and got to throw the dice again!\n")
                            dice_game_e("enemy")
                            
                            p_dmg_done = char.damage * p_wins_e
                            e_dmg_done = enem.damage * e_wins_e

                            time.sleep(3)

                        if apply_unique_stats(char.speed):
                            text_printer("Enemy dodged your attack.\n")
                            p_dmg_done = char.damage * (p_wins_e - 1)
                            time.sleep(3)

                        dmg_difference_p = p_dmg_done - enem.defence
                        if dmg_difference_p >= 0:
                            enem.health = enem.health - dmg_difference_p
                        else:
                            dmg_difference_p = 0

                        dmg_difference_e = e_dmg_done - char.defence
                        if dmg_difference_e >= 0:
                            char.health = char.health - dmg_difference_e
                        else:
                            dmg_difference_e = 0

                        text_printer("You've dealt {} damage\n".format(dmg_difference_p))
                        text_printer("Enemy has {} health remaining.\n".format(enem.health))
                        text_printer("The enemy dealt {} damage.\n".format(dmg_difference_e))
                        text_printer("You have {} health remaining.\n".format(char.health))

                    elif p_wins_e < e_wins_e:
                        p_dmg_done = 0
                        e_dmg_done = enem.damage * e_wins_e
                        
                        if apply_unique_stats(enem.c_strike):
                            text_printer("Enemy strikes you with huge power.\n")
                            e_dmg_done = e_dmg_done + (e_dmg_done * 0.25)
                            time.sleep(2)

                        if apply_unique_stats(char.luck):
                            text_printer("You got lucky, and can throw your dice again!\n")
                            print("(Answer 'throw' or 'skip')\n")
                            
                            choosing = False
                            while choosing == False:
                                player_input = input("=> ")
                                if player_input == "throw":
                                    dice_game("player")
                                    
                                    p_dmg_done = char.damage * p_wins
                                    e_dmg_done = enem.damage * e_wins

                                    time.sleep(3)
                                    choosing = True
                                elif player_input == "skip":
                                    choosing = True
                                else:
                                    print("Choose a valid command.\n")

                        if apply_unique_stats(char.speed):
                            text_printer("You've dodged the enemy's attack.\n")
                            e_dmg_done = enem.damage * (e_wins_e - 1)
                            time.sleep(3)
                                           
                        dmg_difference_p = p_dmg_done - enem.defence
                        if dmg_difference_p >= 0:
                            enem.health = enem.health - dmg_difference_p
                        else:
                            dmg_difference_p = 0

                        dmg_difference_e = e_dmg_done - char.defence
                        if dmg_difference_e >= 0:
                            char.health = char.health - dmg_difference_e
                        else:
                            dmg_difference_e = 0

                        text_printer("You've dealt {} damage\n".format(dmg_difference_p))
                        text_printer("Enemy has {} health remaining.\n".format(enem.health))
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

                next_turn_q = False

                while next_turn_q == False:
                    p_input_dice = input("=> ")

                    if p_input_dice.lower() == "attack":
                        text_printer("New Turn Begins.\n")
                        time.sleep(2)
                        os.system(clear_command)
                        next_turn_q = True
                        who_turn(next_turn, 0, False, False)
                    elif p_input_dice.lower() == "walk":
                        text_printer("You walk away in shame.\n")
                        time.sleep(2)
                        os.system(clear_command)
                        next_turn_q = True
                        return
                    else:
                        text_printer_a("Please type a valid command!\n")

        else:
            return
    else:
        return

def apply_unique_stats(probability):
    return random.random() < probability

def dice_game(who_lucky):
    global p_wins, e_wins, e_roll, p_roll

    sides = 8

    if who_lucky == "both":
        p_roll = random.sample(range(1, sides + 1), 3)
        e_roll = random.sample(range(1, sides + 1), 2)

        text_printer("Player Rolled.\n")
        print_dice_rolls(8, p_roll)
        time.sleep(3)

        text_printer("Enemy Rolled.\n")
        print_dice_rolls(8, e_roll)
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
        print_dice_rolls(8, p_roll)
        time.sleep(3)

        text_printer("Enemy's Previous Roll.\n")
        print_dice_rolls(8, e_roll)
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
        print_dice_rolls(8, p_roll)
        time.sleep(3)

        text_printer("Enemy's New Roll.\n")
        print_dice_rolls(8, e_roll)
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

    sides = 8

    if who_lucky_e == "both":
        e_roll_e = random.sample(range(1, sides + 1), 3)
        p_roll_e = random.sample(range(1, sides + 1), 2)

        text_printer("Player Rolled.\n")
        print_dice_rolls(8, p_roll_e)
        time.sleep(3)

        text_printer("Enemy Rolled.\n")
        print_dice_rolls(8, e_roll_e)
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
        print_dice_rolls(8, p_roll_e)
        time.sleep(3)

        text_printer("Enemy's Previous Roll.\n")
        print_dice_rolls(8, e_roll_e)
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
        print_dice_rolls(8, p_roll_e)
        time.sleep(3)

        text_printer("Enemy's New Roll.\n")
        print_dice_rolls(8, e_roll_e)
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

### TO BE DONE... CLUELESS ABOUT A GOOD CODING METHOD...
def random_encounters():
    print("random encounters")

    weights_a = [0.3, 0.1, 0.05, 0.05, 0.5]

    encounter_a = random.choices(encounters, weights_a)
    encounter_b = random.choice(list(encounter_a.values()))
    
    for q, w in rooms.items():
        for a, s in rooms[w].items():
            rooms[w][s]["interact"] = encounter_b



##########################
#####  MAP MOVEMENT  #####
##########################
#                        #
#      S  - a1 - a2      #
#           |            #
#      c -  h -  b       #
#           |    |       #
#      l2 - l1  t1       #
#      |    |    |       #
#      l3 - l4  t2       #
#                        #
##########################


##################
##              ##
##  Boot Order  ##
##              ##
##################


## FOR TESTING PURPOSES

## GAME START TRIGGER
title_screen()