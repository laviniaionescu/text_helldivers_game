import json
import random
import time


# add try and except
def read_mission_data():
    """Reads necessary info from mission_data json"""
    try:
        with open("mission_data.json", "r", encoding="utf-8") as f:
            mission_data = json.loads(f.read())
        return mission_data
    except FileNotFoundError as e:
        print(f"Cannot read mission data. File not found: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Cannot read mission data. JSON decode error: {e}")
        return None


mission_data = read_mission_data()

remaining_health_symbol = mission_data['remaining_health_symbol']
lost_health_symbol = mission_data['lost_health_symbol']
bars = mission_data['bars']


def health_bars(stats: dict) -> None:
    """Displays HP visually"""
    remaining_health_bars = round(stats['current_hp'] / stats['max_hp'] * bars)
    lost_health_bars = bars - remaining_health_bars
    print(f"HP remaining: {stats['current_hp']} / {stats['max_hp']}")
    print(f"|{remaining_health_bars * remaining_health_symbol} {lost_health_bars * lost_health_symbol}|")


def get_player_name() -> str:
    """Sets player name"""
    player_name = input("Welcome, Helldiver! Register your name to start today's operation: ")
    while len(player_name.strip()) < 2:
        player_name = input("Your name can't empty or be less than 2 letters! "
                            "Register your name to start today's operation! ")
    return player_name


def roll_d6():
    """Rolls a D6 dice"""
    return random.randint(1, 6)


def ammo_loss():
    """Decreases random amount of ammo"""
    return random.randint(5, 20)


def hp_loss():
    """Decreases random amount of HP"""
    return random.randint(0, 20)


def reset_hp(stats: dict):
    """Resets HP and ammo to full"""
    stats['current_hp'] = 100
    stats['current_ammo'] = 300


def lost_life(stats: dict):
    """Decreases lives by 1"""
    stats['reinforcements'] -= 1


def check_death(stats: dict) -> bool:
    """Checks if player has died, if they did die, they lose a life, and HP and ammo are reset to max"""
    if stats['current_hp'] <= 0:
        stats['reinforcements'] -= 1
        stats['current_hp'] = 100
        stats['current_ammo'] = 200
        return True
    return False


def check_game_over(stats: dict) -> bool:
    """Checks if the player has no lives left, if they don't, it's game over"""
    if stats['reinforcements'] == 0:
        print("We are out of reinforcements! Mission failed, Orbiter departing!")
        return True
    else:
        return False


def decrease_stats(stats: dict):
    """Decreases both ammo and HP by a random amount and displays the visual HP bar"""
    stats['current_ammo'] -= ammo_loss()
    stats['current_hp'] -= hp_loss()
    health_bars(stats)


def death_prob(stats: dict) -> bool:
    """Calculates the death probability in an event. If the player has less than 50 HP, the chance of dying is 1 in 5,
    if they have more, it's 1 in 10"""
    if stats['current_hp'] < 50:
        prob = random.randint(1,5)
    else:
        prob = random.randint(1,10)
    if prob == 1:
        return True
    else:
        return False


def event_roll() -> str:
    """Rolls an event out of 4 possible ones"""
    pick = random.randint(1, 4)
    if pick == 1:
        return "normal_bug_spawn"
    elif pick == 2:
        return "hive_spawn"
    elif pick == 3:
        return "meteor_shower"
    else:
        return "fire_tornadoes"


def normal_bug_spawn(stats: dict) -> None:
    """Spawns some simple enemies"""
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


def hive_spawn(stats: dict):
    """Spawns an enemy hive, where the player has to throw grenades to close the hive entrances, and a 1 in 5 chance
    for the tossed grenade to bounce back and kill the player"""
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


def meteor_shower(stats: dict):
    """A meteor shower with a D6 chance to die"""
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


def fire_tornadoes(stats: dict):
    """A fire tornado that the player can get caught in. If they do, they have a chance to die if their HP is too low"""
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


def grenade_bounce() -> int:
    """A 1 in 5 chance for the grenade to bounce back towards the player"""
    return random.randint(1, 5)


def coin_flip_samples() -> int:
    """A coin flip"""
    return random.randint(1, 2)


def find_sample() -> str:
    """Picks a common or rare sample like a coin flip"""
    return random.choice(['common', 'rare'])


def update_player_score(player_score: int) -> int:
    """If the coin flip is successful, it runs the find_sample function, and it adds to the score depending on what
    kind of sample was found"""
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


def write_player_score(player_name: str, player_score: int):
    """Writes the player's name and score to the jsonl file"""
    player_stats = {"Name": player_name, "Score": player_score}
    with open("scores.jsonl", "a") as f:
        f.write(json.dumps(player_stats, indent=4) + "\n")