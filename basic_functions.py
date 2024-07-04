import json
import random
import time


remaining_health_symbol = "▒"
lost_health_symbol = "_"
bars = 20


def health_bars(stats):
    remaining_health_bars = round(stats['current_hp'] / stats['max_hp'] * bars)
    lost_health_bars = bars - remaining_health_bars
    print(f"HP remaining: {stats['current_hp']} / {stats['max_hp']}")
    print(f"|{remaining_health_bars * remaining_health_symbol} {lost_health_bars * lost_health_symbol}|")


def get_player_name():
    player_name = input("Welcome, Helldiver! Register your name to start today's operation: ")
    while len(player_name.strip()) < 2:
        player_name = input("Your name can't empty or be less than 2 letters! "
                            "Register your name to start today's operation! ")
    return player_name


def roll_d100():
    return random.randint(1, 100)


def roll_d10():
    return random.randint(1, 10)


def roll_d6():
    return random.randint(1, 6)


def ammo_loss():
    return random.randint(5, 20)


def hp_loss():
    return random.randint(0, 20)


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


def check_game_over(stats):
    if stats['reinforcements'] == 0:
        print("We are out of reinforcements! Mission failed, Orbiter departing!")
        return True
    else:
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
    if prob == 1:
        return True
    else:
        return False


def event_roll():
    pick = random.randint(1, 4)
    if pick == 1:
        return "normal_bug_spawn"
    elif pick == 2:
        return "hive_spawn"
    elif pick == 3:
        return "meteor_shower"
    else:
        return "fire_tornadoes"


def normal_bug_spawn(stats):
    # time.sleep(2)
    print("A swarm of Terminids crawl from the sand!")
    # time.sleep(2)
    fight_flight = input("Do you bravely exterminate the vermin for liberty, "
                         "or run away like a coward deserter?\n"
                         "Fight or flight? ")
    while fight_flight.lower() not in ("fight", "flight"):
        time.sleep(1)
        fight_flight = input("This is not the time to freeze, Helldiver! Fight or flight!? ")
    if fight_flight == "fight":
        time.sleep(1)
        print("You pull out your trusty rifle and proceed to dispense liberty to the freedom-hating Terminids!")
        decrease_stats(stats)
        if death_prob(stats) == 1:
            lost_life(stats)
            if check_game_over(stats):
                exit()
            print(f"Helldiver down! Sending down reinforcements! Orbital has {stats['reinforcements']}"
                  f" Helldivers left! Continue the fight for liberty!")
            reset_hp(stats)
            decrease_stats(stats)
            time.sleep(1)
            print(f"The battle is hard, but you fight for freedom and win! The alien scum left you with"
                  f" {stats['current_ammo']} ammunition and {stats['current_hp']} health.")
        else:
            time.sleep(1)
            print(f"The battle is hard, but you fight for freedom and win! The alien scum left you with"
                  f" {stats['current_ammo']} ammunition and {stats['current_hp']} health.")
    else:
        time.sleep(1)
        print("You decide to run like a dishonorable deserter, disappointing Freedom and Liberty both!")
        if death_prob(stats) == 1:
            lost_life(stats)
            if check_game_over(stats):
                exit()
            reset_hp(stats)
            time.sleep(1)
            print(f"The swarm of vermin gave chase and didn't relent, they caught you and killed you! "
                  f"Helldiver down! Sending down reinforcements!\n"
                  f"Orbital has {stats['reinforcements']} Helldivers left!"
                  " Continue the fight for liberty!")


def hive_spawn(stats):
    time.sleep(1)
    print("What's that, you came across a Terminid hive! Do you eradicate them all, or proceed to the"
          " objective by using advanced stealth evasion tactics?")
    kill_evade = input("Destroy, or evade? ")
    while kill_evade.lower() not in ("destroy", "evade"):
        kill_evade = input("Make a decision helldiver! Destroy the pests, or evade?")
    if kill_evade == "destroy":
        if grenade_bounce() == 1:
            time.sleep(1)
            print("You open fire on the hive, decimating the vermin protecting it! You begin tossing grenades "
                  "in the holes to shut the pests in \nwhen one of them crawls out just as you throw the grenade!"
                  " It bounces right off the giant insect's hard shell and flies back into your arms!")
            lost_life(stats)
            if check_game_over(stats):
                exit()
            reset_hp(stats)
            time.sleep(1)
            print(f"Helldiver down! Sending down reinforcements!\n"
                  f"Orbital has {stats['reinforcements']} Helldivers left!"
                  "Tossing the last grenade in finishes the job and destroys the hive!")
        else:
            time.sleep(1)
            print("You open fire on the hive, decimating the vermin protecting it, then tossing grenades in the"
                  " hive openings to shut the rest of them in! Hive destroyed!")
            decrease_stats(stats)
            if check_death(stats):
                time.sleep(1)
                print(f"Helldiver down! Sending down reinforcements! Orbital has {stats['reinforcements']}"
                      "Helldivers left! Continue the fight for liberty!")
            else:
                time.sleep(1)
                print(f"The battle is hard, but you fight for freedom and win! The alien scum left you with"
                      f" {stats['current_ammo']} ammunition and {stats['current_hp']} health.")
    else:
        if death_prob(stats) == 1:
            if check_game_over(stats):
                exit()
            lost_life(stats)
            reset_hp(stats)
            time.sleep(1)
            print(f"You begin tactically avoiding the hive, but an unsuspecting sneeze alerts the enemy to your"
                  " presence! You start emergency evasive maneuvers, but the faster ones catch up to you!\n"
                  "Helldiver down! Sending down reinforcements!\n"
                  f"Orbital has {stats['reinforcements']} Helldivers left!")
        else:
            time.sleep(1)
            print("You let the vermin live another day, ensuring they'll be a deadly issue to the next unlucky"
                  " Helldiver who saves the world in this area!")


def meteor_shower(stats):
    time.sleep(2)
    print("The skies turn dark, you look up and see a rain of meteors about to commence! Dodge, Helldiver!")
    time.sleep(2)
    if roll_d6() == 1:
        if check_game_over(stats):
            exit()
        lost_life(stats)
        reset_hp(stats)
        time.sleep(2)
        print("Just as you thought the rock shower was about to end, one of the giant boulders lands right on"
              " top of you!\n"
              "Helldiver down! Sending down reinforcements!\n"
              f"Orbital has {stats['reinforcements']} Helldivers left!")
    else:
        time.sleep(2)
        print("Lady Liberty herself must've been watching over you, because you emerged in one piece through the "
              "shower of boulders! Carry on, Helldiver!")


def fire_tornadoes(stats):
    time.sleep(2)
    print("The skies turn red, you look up and see the twisting fires above connecting to the ones below! "
          "Avoid the fire tornadoes at all cost!")
    if roll_d6() == 1:
        hp_loss() * 2
        time.sleep(2)
        print("You've stumbled right into one of them! Drop and roll, Helldiver!")
        if death_prob(stats) == 1:
            time.sleep(2)
            print("It's too late! Helldiver down! Sending down reinforcements!\n"
                  f"Orbital has {stats['reinforcements']} Helldivers left!")
            lost_life(stats)
            if check_game_over(stats):
                exit()
            reset_hp(stats)
        else:
            time.sleep(3)
            print("Somehow, you've made it through! Carry on!")
    else:
        time.sleep(2)
        print(f"You've made it through! Carry on!")


def grenade_bounce():
    return random.randint(1, 5)


# def coin_flip():
#     return random.randint(1, 2)


def coin_flip_samples():
    return random.randint(1, 2)


def find_sample():
    return random.choice(['common', 'rare'])


def update_player_score(player_score):
    if coin_flip_samples() == 1:
        sample = find_sample()
        if sample == 'common':
            player_score += 10
            print("Look at that, Helldiver, a common sample! Pick that up, we need it for research.")
        elif sample == 'rare':
            player_score += 20
            print("Rare sample spotted! Pick that up right away!")
    else:
        print("Looks like there are no samples here, shame, carry on.")
    return player_score


def write_player_score(player_name, player_score):
    player_stats = {"Name": player_name, "Score": player_score}
    with open("scores.jsonl", "a") as f:
        f.write(json.dumps(player_stats, indent=4) + "\n")