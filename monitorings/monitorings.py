import random


class Warrior:

    def __init__(self, name, health, dmg):
        self.name = name
        self.health = health
        self.dmg = dmg

    def set_name(self, name):
        self.name = name
        return self.name

    def get_name(self):
        return self.name

    def set_health(self, health):
        self.health = health
        return health

    def get_health(self):
        return self.health

    def attack(self, enemy):

        if enemy.health > 0:
            enemy.health -= self.dmg
        else:
            print('{} уже хорошенько получил монитором по ебалу и не может принять ещё один удар'.format(enemy.name))

        return enemy.health


w1 = Warrior('Andrew', 100, 110)
w2 = Warrior('Nicola', 100, 10)

warriors = (w1, w2)

attacker = random.choice(warriors)
print(attacker.name)


def return_enm(number):
    if number == w2:
        enm = w1

    else:
        enm = w2

    return enm


enemy = return_enm(attacker)
print(enemy.name)
while enemy.health > 0:
    attacker.attack(enemy)


