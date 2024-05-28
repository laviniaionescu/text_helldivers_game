import random
import time


remaining_health_symbol = "▒"
lost_health_symbol = "_"
bars = 20


def get_player_name():
    player_name = input("Welcome, Helldiver! Register your name to start today's operation: ")
    while len(player_name) < 3:
        player_name = input("Your name can't empty or be less than 3 letters! "
                            "Register your name to start today's operation! ")
    return player_name


def health_bars(stats):
    remaining_health_bars = round(stats['current_hp'] / stats['max_hp'] * bars)
    lost_health_bars = bars - remaining_health_bars
    print(f"HP remaining: {stats['current_hp']} / {stats['max_hp']}")
    print(f"|{remaining_health_bars * remaining_health_symbol} {lost_health_bars * lost_health_symbol}|")


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
    health_bars(stats)


def death_prob(stats: dict):
    if stats['current_hp'] < 50:
        prob = random.randint(1,5)
    else:
        prob = random.randint(1,10)


def event_roll():
    pick = random.randint(1,1)
    if pick == 1:
        return "normal_bug_spawn"
    elif pick == 2:
        return "hive_spawn"
    elif pick == 3:
        return "meteor_shower"
    else:
        return "fire_tornadoes"


def grenade_bounce():
    return random.randint(1, 5)


def coin_flip():
    return random.randint(1, 2)



