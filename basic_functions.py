import random
import time


def roll_d100():
    return random.randint(1,100)


def roll_d10():
    return random.randint(1,10)


def roll_d6():
    return random.randint(1,6)


def ammo_loss():
    return random.randint(5,20)


# check HERE for later issue if the upper cap is too high
def hp_loss():
    return random.randint(0,20)


def reset_hp(stats):
    stats['current_hp'] = 100


def lost_life(stats):
    stats['reinforcements'] -= 1


def check_death(stats):
    if stats['current_hp'] <= 0:
        stats['reinforcements'] -= 1
        stats['current_hp'] = 100
        stats['current_ammo'] = 200
        return True
    return False


def decrease_stats(stats):
    stats['current_ammo'] -= ammo_loss()
    stats['current_hp'] -= hp_loss()


def death_prob(stats):
    if stats['current_hp'] < 50:
        prob = random.randint(1,5)
    else:
        prob = random.randint(1,10)


def event_roll():
    pick = random.randint(4,4)
    if pick == 1:
        return "normal_bug_spawn"
    elif pick == 2:
        return "hive_spawn"
    elif pick == 3:
        return "meteor_shower"
    else:
        return "fire_tornadoes"


def spawn_miniboss():
    pick = random.randint(1,10)
    if pick == 1:
        return "spawn_charger"
    elif pick == 10:
        return "spawn_titan"


def grenade_bounce():
    return random.randint(1, 5)

