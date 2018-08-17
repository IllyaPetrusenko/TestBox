import random


class OfficeWarrior:

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
        elif enemy.health == 0:
            print('{} уже хорошенько получил монитором по ебалу и не может принять ещё один удар'.format(enemy.name))

        # print('Состояние здоровья офисного воина {}: {}'.format(enemy.name, enemy.health))
        return enemy.health


w1 = OfficeWarrior('Andrew', 100, random.randrange(1, 20))
w2 = OfficeWarrior('Nicola', 100, random.randrange(1, 20))
warriors = (w1, w2)


def select_zad(warriors):
    first = random.choice(warriors)
    if first == w1:
        second = w2
    else:
        second = w1
    return first, second


def fight(first, second):
    if second.health or first.health != 0:
        while second.health and first.health > 0:

            if first.dmg > second.health:
                first.dmg = second.health
            first.attack(second)
            print('Офисный крыс: {} получил монитором по ебалу от {} и его здоровье: {}'.format(second.name, first.name, second.health))

            if second.dmg > first.health:
                second.dmg = first.health
            second.attack(first)
            print('Офисный крыс: {} получил монитором по ебалу от {} и его здоровье: {}'.format(first.name, second.name, first.health))


sz = select_zad(warriors)
fight(sz[0], sz[1])

