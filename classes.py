#### PLAYER CLASSES

class Player:
    species = "Player"
    c_strike = 0.0
    luck = 0.0
    speed = 0.0

    def __init__(self, name):
        self.name = name
        self._damage = 0
        self._health = 100
        self._exp = 0
        self._level = 0
        self._position = "spawn"
        self._category = "spawner"

    def say(self, msg):
        print("{name}: {message}".format(name=self.name, message=msg))

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

class Human(Player):
    species = "Human"
    c_strike = 0.15         # 15% chance for critical strike
    luck = 0.25             # 25% for an extra move
    speed = 0.10            # 10% chance of dodging

    @staticmethod
    def grunt():
        print("*grunts* You foolish monster!")


class Elf(Player):
    species = "Elf"
    c_strike = 0.10         # 10% chance for critical strike
    luck = 0.15             # 15% for an extra move
    speed = 0.25            # 25% chance of dodging

    @staticmethod
    def grunt():
        print("*grunts* Amarth!")

class Orc(Player):
    species = "Orc"
    c_strike = 0.25         # 25% chance for critical strike
    luck = 0.10             # 10% for an extra move
    speed = 0.15            # 15% chance of dodging

    @staticmethod
    def grunt():
        print("*grunts* Ashdautas Vrasubatlat!")


#### ENEMY CLASSES


class Enemy:
    species = "Enemy"
    c_strike = 0.0
    luck = 0.0
    speed = 0.0

    def __init__(self, name):
        self.name = name
        self._damage = 0
        self._health = 50
        self._exp = 25
    
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

class Zombie(Enemy):
    species = "Zombie"
    c_strike = 0.15
    luck = 0.10
    speed = 0.05

    def __init__(self, name):
        self._damage = 1
        self._health = 50
        self._exp = 50

class Wolf(Enemy):
    species = "Wolf"
    c_strike = 0.10
    luck = 0.05
    speed = 0.15

    def __init__(self, name):
        self._damage = 1
        self._health = 25
        self._exp = 25

class Wraith(Enemy):
    species = "Wraith"
    c_strike = 0.05
    luck = 0.15
    speed = 0.10

    def __init__(self, name):
        self._damage = 2
        self._health = 75
        self._exp = 75