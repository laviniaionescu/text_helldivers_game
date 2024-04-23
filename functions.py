import random


def roll_d100():
    return random.randint(1,100)


def roll_d10():
    return random.randint(1,10)


def ammo_loss():
    return random.randint(10,30)


def hp_loss():
    return random.randint(0,60)


def reset_hp(stats):
    stats['current_hp'] = 100


def lost_life(stats):
    stats['reinforcements'] -= 1


def decrease_stats(stats):
    stats['current_ammo'] -= ammo_loss()
    stats['current_hp'] -= hp_loss()


def death_prob(current_hp):
    if current_hp < 50:
        prob = random.randint(1,5)
    else:
        prob = random.randint(1,10)
    return prob


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


def spawn_miniboss():
    pick = random.randint(1,10)
    if pick == 1:
        return "spawn_charger"
    elif pick == 10:
        return "spawn_titan"


def grenade_bounce():
    return random.randint(1, 5)