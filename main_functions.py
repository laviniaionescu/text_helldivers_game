import basic_functions
import time
import classes
import weapons



def extraction(seconds: int, stats: dict):
    """Extraction with countdown where the player has to defend themselves until the time is up"""
    time.sleep(3)
    print("Orbital shuttle deployed! Make your way to the extraction beacon, and keep the bugs off your back!")
    time.sleep(3)
    # countdown
    while seconds != 1:
        seconds -= 1
        time.sleep(1)
        print(seconds)

        if seconds == 20:
            # fight, lose hp and ammo
            basic_functions.decrease_stats(stats)
            # if you die, check how many lives left, if none, game over. if some, refill hp and ammo and lose life with
            # check death function
            if basic_functions.check_death(stats):
                if basic_functions.check_game_over(stats):
                    exit()
                print(f"Helldiver down! Sending down reinforcements! Orbital has {stats['reinforcements']} "
                      "Helldivers left! Pick up and bring back anything that Helldiver dropped!")
            else:
                print("Pelican shuttle touchdown in twenty seconds! Keep running, Helldiver! "
                      f"{stats['current_hp']} health and {stats['current_ammo']} ammo left!")

        elif seconds == 10:
            # keep fighting, lose hp and ammo
            basic_functions.decrease_stats(stats)
            # check for death, check for game over, if dead refill stats and lose life
            if basic_functions.check_death(stats):
                if basic_functions.check_game_over(stats):
                    exit()
                print(f"Helldiver down! Sending down reinforcements! Orbital has {stats['reinforcements']} "
                      "Helldivers left! Pick up and bring back anything that Helldiver dropped!")
            else:
                print("Ten seconds to landing, you're almost there! "
                      f"{stats['current_hp']} health and {stats['current_ammo']} ammo left!")

        elif seconds == 1:
            print("Shuttle touchdown commencing, keep away from the Pelican's landing thrusters!")
            time.sleep(3)

            # chance to die by staying too close to the shuttle's thrusters, mission accomplished coz helldivers are
            # expendable
            if basic_functions.roll_d6() == 1:
                time.sleep(3)
                print("I said keep away from the shuttle's thrus- Helldiver down! But objective is completed!\n"
                      "Mission accomplished!")
            else:
                print("Extraction successful! Mission accomplished, great job, Helldiver!")


# first mission
def rescue_operation(stats: dict, civilian_status: dict) -> str:
    """Rescue mission that fails if 3 or more civilians die during it"""
    time.sleep(2)
    print("We have civilians to rescue, Helldiver! Open the bunker doors and escort them safely to the ship!")
    time.sleep(5)
    print("Terminids incoming! Open fire! Protect those civilians at all cost, Helldiver! Too many casualties "
          "and it's over!")
    time.sleep(5)
    for i in range(5):
        # for 5 civs, lose hp & ammo, check for death and game over
        time.sleep(3)
        basic_functions.decrease_stats(stats)
        if basic_functions.check_death(stats):
            if basic_functions.check_game_over(stats):
                exit()
            print("You fight bravely, but give your life for the citizens of Super Earth! Helldiver down! "
                  "Sending down reinforcements!\n"
                  f"Orbital has {stats['reinforcements']} Helldivers left!")
            time.sleep(5)
        if basic_functions.roll_d6() == 1:
            civilian_status['dead'] += 1
            print("Civilian down!")
            time.sleep(1)
        else:
            print("Civilian rescued!")
            civilian_status['rescued'] += 1
            time.sleep(1)
    if civilian_status['dead'] >= 3:
        print("We lost too many civilians, the mission is a failure! Train harder, Helldiver!")
        time.sleep(4)
        return "mission failed"
    else:
        print("Objective complete, good work, Helldiver! Now head over to extraction!")
        time.sleep(4)
        return "mission successful"


# second mission
def generator_boot(seconds: int, generator_hp: int, stats: dict):
    """Part 1 of the second mission where the player has to defend a generator that loses HP"""
    time.sleep(3)
    print("The ICBM needs fuel, turn on that pump generator!")
    time.sleep(4)
    print("The sound of the generator activating is attracting Terminids! They're attacking the generator, "
          "protect it while it boots up, and destroy the pests!")
    time.sleep(5)
    while seconds > 1:
        seconds -= 1
        time.sleep(1)
        print(seconds)

        if seconds == 14:
            generator_hp -= basic_functions.hp_loss()
            basic_functions.decrease_stats(stats)
            print(f"Fourteen seconds left! The generator has {generator_hp}% functionality left!")

        elif seconds == 7:
            generator_hp -= basic_functions.hp_loss()
            basic_functions.decrease_stats(stats)
            print(f"Seven seconds left! The generator is {generator_hp}% intact, protect it, Helldiver!")

        elif seconds == 1:
            print("The generator is operational!")


def fuel_icbm(stats: dict):
    """Part 2 of the second mission where the player fights the enemy while fuel is being pumped"""
    time.sleep(3)
    print("It's time to put it to good use! Start pumping that fuel to the missile, and destroy the remaining "
          "bugs!")
    time.sleep(1)
    fuel = 0
    while fuel != 100:
        fuel += 25
        time.sleep(5)
        basic_functions.decrease_stats(stats)
        if basic_functions.check_death(stats):
            if basic_functions.check_game_over(stats):
                exit()
            print(f"Helldiver down! Sending down reinforcements! Orbital has {stats['reinforcements']}"
                  "Helldivers left! Continue the fight for liberty!")
            time.sleep(3)
        else:
            if fuel == 25:
                print(f"ICBM fuel 25%! Keep them off of you! "
                      f"{stats['current_hp']} health and {stats['current_ammo']} ammo left!")
                time.sleep(2)

            elif fuel == 50:
                basic_functions.decrease_stats(stats)
                print("Fuel halfway through! Keep fighting! "
                      f"{stats['current_hp']} health and {stats['current_ammo']} ammo left!")
                time.sleep(2)
                if basic_functions.check_death(stats):
                    if basic_functions.check_game_over(stats):
                        exit()
                    print(f"Helldiver down! Sending down reinforcements! Orbital has {stats['reinforcements']}"
                          "Helldivers left! Continue the fight for liberty!")
                    time.sleep(3)

            elif fuel == 75:
                print("Almost done, hang in there!")
            else:
                print("Fueling complete! Head up to the console and launch hell on them!")


def launch_icbm(seconds: int, stats: dict):
    """Part 3 of the second mission where the player fights off the enemy and defends the console"""
    time.sleep(5)
    print("Launch codes operational! Hit the button, protect the console, and stay the hell away from the missile's!"
          "ignition radius!")
    time.sleep(5)
    while seconds > 1:
        seconds -= 1
        time.sleep(1)
        print(seconds)

        if seconds == 14:
            basic_functions.decrease_stats(stats)
            if basic_functions.check_death(stats):
                time.sleep(3)
                if basic_functions.check_game_over(stats):
                    exit()
                print(f"Helldiver down! Sending down reinforcements! Orbital has {stats['reinforcements']}"
                      " Helldivers left! Continue the fight for liberty!")
            else:
                print("Fourteen seconds left! Ignition commencing! Keep those Terminids off of the console! "
                      f"{stats['current_hp']} health and {stats['current_ammo']} ammo left!")

        elif seconds == 7:
            basic_functions.decrease_stats(stats)
            if basic_functions.check_death(stats):
                time.sleep(3)
                if basic_functions.check_game_over(stats):
                    exit()
                print(f"Helldiver down! Sending down reinforcements! Orbital has {stats['reinforcements']}"
                      " Helldivers left! Continue the fight for liberty!")
            else:
                print("Seven seconds left! Protect that console with your life! "
                      f"{stats['current_hp']} health and {stats['current_ammo']} ammo left!")
            # roll a d6 to check if player is too close to the rocket launch
            if basic_functions.roll_d6() == 1:
                basic_functions.lost_life(stats)
                basic_functions.reset_hp(stats)
                print("You're too close to the blast radius! Back away, before you're burnt to a crisp- Ah, too late! "
                      "Helldiver down! Sending down reinforcements!\n"
                      f"Orbital has {stats['reinforcements']} Helldivers left!"
                      " Continue the fight for liberty!")
                time.sleep(7)
                if basic_functions.check_game_over(stats):
                    exit()
        elif seconds == 1:
            print("We have liftoff! Good work, Helldiver, eliminate the rest of those vermin and head to extraction!"
                  " The missile will do the rest!")
            time.sleep(5)


# third mission
player = classes.Helldiver(name="Helldiver", health=100)
boss = classes.Boss(name="The Bile Titan", health=100, weapon=weapons.titan_attack)


def boss_fight(stats) -> str:
    """Boss fight using classes where the player picks a weapon and a fight occurs until either the player or the boss
    are out of HP"""
    time.sleep(2)
    print("There it is, the massive beast! Listen up, Helldiver! An emergency situation demanded we redirect your "
          "reinforcements towards an urgent side objective!")
    time.sleep(6)
    print("This means you're alone in this one! To make up for it, "
          "Orbital is sending down a medical supply package, as well as a weapon of your choice!")
    time.sleep(6)
    print("Heal up, and transmit what weapon you want to use against this fiend!")
    player_choice = input(weapons.WEAPONS)
    while player_choice not in ["1", "2", "3"]:
        print("Pick a weapon, Helldiver!")
        player_choice = input(weapons.WEAPONS)
    if player_choice == "1":
        player.equip(weapons.auto_cannon)
    elif player_choice == "2":
        player.equip(weapons.anti_tank)
    else:
        player.equip(weapons.railgun)

    while boss.health != 0 and player.health != 0:
        player.attack(boss)
        boss.attack(player)
        print(f"{player.name} health left: {player.health}")
        print(f"Health of {boss.name}: {boss.health}\n*****")
        time.sleep(4)
    if boss.health <= 0:
        print("The vile beast has been felled! Great job, Helldiver, that will put a dent in their plans!")
        time.sleep(4)
        print("Dropping down the last medical field kit and some ammo, heal up so you can make it to extraction, go!")
        basic_functions.reset_hp(stats)
        time.sleep(4)
        return "mission successful"
    else:
        print("You were our last hope! Mission failed, Orbiter departing!")
        return "mission failed"
