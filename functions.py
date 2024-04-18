import random


def roll_d100():
    return random.randint(1,100)


def roll_d10():
    return random.randint(1,10)


def ammo_loss():
    return random.randint(10,30)


def death_prob(current_hp):
    if current_hp < 50:
        prob = random.randint(1,5)
    else:
        prob = random.randint(1,10)
    return prob


def hp_loss():
    return random.randint(10,30)


def event_roll():
    pick = random.randint(2,2)
    if pick == 1:
        return "normal_bug_spawn"
    elif pick == 2:
        return "hive_spawn"
    elif pick == 3:
        return "meteor_shower"
    else:
        return "fire_tornado"


