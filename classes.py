import sys
import time
import os


########################
#### PLAYER CLASSES ####
########################


class player:
    species = "Player"

    def __init__(self, name):
        self.name = name
        self.armour = {
            "head"          : "nothing",
            "torso"         : "nothing",
            "legs"          : "nothing",
            "feet"          : "nothing",
            "arms"          : "nothing",
            "left_hand"     : "nothing",
            "right_hand"    : "nothing"
        }
        self.bag = {
            1   : "empty",
            2   : "empty",
            3   : "empty",
            4   : "empty",
            5   : "empty",
            6   : "empty",
            7   : "empty",
            8   : "empty",
            9   : "empty",
            10  : "empty",
            11  : "empty",
            12  : "empty"
        }
        self.c_strike = 0.0
        self.luck = 0.0
        self.speed = 0.0
        self._money_a = 0
        self._money_b = 0
        self._damage = 0
        self._defence = 0
        self._health = 100
        self._mana = 0
        self._exp = 0
        self._level = 0
        self._job = "peasant"
        self._position = "spawn"
        self._category = "spawner"

    def say(self, msg):
        text = "{name}: {message}".format(name=self.name, message=msg)
        for character in text:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)

    @classmethod
    def get_species(cls):
        return cls.species

    @staticmethod
    def grunt():
        print("*grunts*")

    @property
    def damage(self):
        return self._damage
    
    @damage.setter
    def damage(self, damage):
        self._damage = damage

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, health):
        self._health = health

    @property
    def mana(self):
        return self._mana

    @mana.setter
    def mana(self, mana):
        self._mana = mana

    @property
    def exp(self):
        return self._exp

    @exp.setter
    def exp(self, exp):
        self._exp = exp

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, level):
        self._level = level
    
    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, position):
        self._position = position

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        self._category = category

    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, job):
        self._job = job

    @property
    def money_a(self):
        return self._money_a

    @money_a.setter
    def money_a(self, money_a):
        self._money_a = money_a

    @property
    def money_b(self):
        return self._money_b

    @money_b.setter
    def money_b(self, money_b):
        self._money_b = money_b

class human(player):
    species = "Human"
    
    def __init__(self, name):
        self.c_strike = 0.15         # 15% chance for critical strike
        self.luck = 0.25             # 25% for an extra move
        self.speed = 0.10            # 10% chance of dodging

    @staticmethod
    def grunt():
        print("*grunts* You foolish monster!")


class elf(player):
    species = "Elf"

    def __init__(self, name):
        self.c_strike = 0.10         # 10% chance for critical strike
        self.luck = 0.15             # 15% for an extra move
        self.speed = 0.25            # 25% chance of dodging

    @staticmethod
    def grunt():
        print("*grunts* Amarth!")

class orc(player):
    species = "Orc"

    def __init__(self, name):
        self.c_strike = 0.25         # 25% chance for critical strike
        self.luck = 0.10             # 10% for an extra move
        self.speed = 0.15            # 15% chance of dodging

    @staticmethod
    def grunt():
        print("*grunts* Ashdautas Vrasubatlat!")


#######################
#### ENEMY CLASSES ####
#######################


class enemy:
    species = "Enemy"

    def __init__(self, name):
        self.name = name
        self.c_strike = 0.0
        self.luck = 0.0
        self.speed = 0.0
        self._damage = 0
        self._health = 50
        self._exp = 25
        self.drop_rate = 1
        self.drop = ""
    
    def say (self, msg):
        print("{name}: {message}".format(name=self.name, message=msg))

    @classmethod
    def get_species(cls):
        return cls.species

    @staticmethod
    def grunt():
        print("*grunts* Paaaain!")
    
    @property
    def damage(self):
        return self._damage
    
    @damage.setter
    def damage(self, damage):
        self._damage = damage

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, health):
        self._health = health

    @property
    def exp(self):
        return self._exp

    @exp.setter
    def exp(self, exp):
        self._exp = exp

class zombie(enemy):
    species = "Zombie"

    def __init__(self, name):
        self._damage = 1
        self._health = 50
        self._exp = 50
        self.c_strike = 0.15
        self.luck = 0.10
        self.speed = 0.05

class wolf(enemy):
    species = "Wolf"

    def __init__(self, name):
        self._damage = 1
        self._health = 25
        self._exp = 25
        self.c_strike = 0.10
        self.luck = 0.05
        self.speed = 0.15

class wraith(enemy):
    species = "Wraith"

    def __init__(self, name):
        self._damage = 2
        self._health = 75
        self._exp = 75
        self.c_strike = 0.05
        self.luck = 0.15
        self.speed = 0.10