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
w2 = OfficeWarrior('Nicola', 125, random.randrange(1, 20))
w3 = OfficeWarrior('Lisyj', 100, random.randrange(1, 20))
w4 = OfficeWarrior('Illia', 100, random.randrange(1, 20))

warriors_1 = (w1, w2)
warriors_2 = (w3, w4)


def select_zad(warriors_1, warriors_2):
    first = random.choice(warriors_1)
    second = random.choice(warriors_2)
    return first, second


def fight(first, second):
     
     if second.health or first.health > 1:

        while second.health and first.health > 1:

            if first.health > 1:

                    if second.dmg > first.health:
                        second.dmg = first.health
                    second.attack(first)
                    print('Офисный крыс: {} получил монитором по ебалу от {} и его здоровье: {}'.format(first.name, second.name, first.health))

            if second.health > 1:

                    if first.dmg > second.health:
                        first.dmg = second.health
                    first.attack(second)
                    print('Офисный крыс: {} получил монитором по ебалу от {} и его здоровье: {}'.format(second.name, first.name, second.health))

     else:
         print('GAME OVER')

sz = select_zad(warriors_1, warriors_2)
fight(sz[0], sz[1])

