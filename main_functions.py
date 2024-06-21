import basic_functions
import time
import classes
import weapons


player_score = 0


def extraction(seconds, stats):
    time.sleep(2)
    print("Orbital shuttle deployed! Make your way to the extraction beacon, and keep the bugs off your back!")
    while seconds != 1:
        seconds -= 1
        time.sleep(1)
        print(seconds)
        if seconds == 20:
            basic_functions.decrease_stats(stats)
            if basic_functions.check_death(stats):
                print(f"Helldiver down! Sending down reinforcements! Orbital has {stats['reinforcements']}"
                      "Helldivers left! Continue the fight for liberty!")
            else:
                print("Pelican shuttle touchdown in twenty seconds! Keep running, Helldiver!"
                      f"{stats['current_hp']} health and {stats['current_ammo']} ammo left!")
                basic_functions.health_bars(stats)

        elif seconds == 10:
            basic_functions.decrease_stats(stats)
            if basic_functions.check_death(stats):
                print(f"Helldiver down! Sending down reinforcements! Orbital has {stats['reinforcements']}"
                      "Helldivers left! Continue the fight for liberty!")
            else:
                print("Ten seconds to landing, you're almost there!"
                      f"{stats['current_hp']} health and {stats['current_ammo']} ammo left!")
        elif seconds == 1:
            basic_functions.decrease_stats(stats)
            print("Shuttle touchdown commencing, keep away from the Pelican's landing thrusters!")
            time.sleep(1)
            print("Extraction successful! Mission accomplished, great job, Helldiver!")

            if basic_functions.roll_d6() == 1:
                time.sleep(1)
                print("I said keep away from the shuttle's thrus- Helldiver down! But objective is completed!\n"
                      "Mission accomplished!")


# first mission
def rescue_operation(stats, civilian_status):
    time.sleep(2)
    print("We have civilians to rescue, Helldiver! Open the doors and escort them safely to the ship!")
    time.sleep(2)
    print("Terminids incoming! Open fire! Protect those civilians at all cost, Helldiver! Too many casualties "
          "and it's over!")
    for i in range(5):
        time.sleep(3)
        basic_functions.decrease_stats(stats)
        # print(stats)
        if basic_functions.check_death(stats):
            basic_functions.lost_life(stats)
            basic_functions.reset_hp(stats)
            print("You fight bravely, but give your life for the citizens of Super Earth! Helldiver down! "
                  "Sending down reinforcements!\n"
                  f"Orbital has {stats['reinforcements']} Helldivers left!")
        if basic_functions.roll_d6() == 1:
            civilian_status['dead'] += 1
            print("Civilian down!")
        else:
            print("Civilian rescued!")
            civilian_status['rescued'] += 1
    # print(f"rescued civs {civilian_status['rescued']}")
    # print(f"dead civs {civilian_status['dead']}")
    if civilian_status['dead'] >= 3:
        time.sleep(1)
        print("We lost too many civilians, the mission is a failure! Train harder, Helldiver!")
        return "mission failed"
    else:
        time.sleep(2)
        print("Objective complete, good work, Helldiver! Now head over to extraction!")


# second mission
def generator_boot(seconds, generator_hp, stats):
    print("The ICBM needs fuel, turn on those pump generators!")
    time.sleep(2)
    print("The sound of the generators activating is attracting Terminids! They're attacking the generators, "
          "protect them while they boot up and destroy the pests!")
    time.sleep(2)
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
            time.sleep(2)


def fuel_icbm(fuel, stats):
    time.sleep(1)
    print("It's time to put them to good use! Start pumping that fuel to the missile, and destroy the remaining "
          "vermin!")
    fuel = 0
    while fuel != 100:
        fuel += 25
        time.sleep(5)
        basic_functions.decrease_stats(stats)
        if basic_functions.check_death(stats):
            time.sleep(1)
            print(f"Helldiver down! Sending down reinforcements! Orbital has {stats['reinforcements']}"
                  "Helldivers left! Continue the fight for liberty!")
        else:
            if fuel == 25:
                time.sleep(1)
                print(f"ICBM fuel 25%! Keep them off of you! "
                      f"{stats['current_hp']} health and {stats['current_ammo']} ammo left!")
            elif fuel == 50:
                time.sleep(1)
                print("Fuel halfway through! Keep fighting! "
                      f"{stats['current_hp']} health and {stats['current_ammo']} ammo left!")
                basic_functions.decrease_stats(stats)
                if basic_functions.check_death(stats):
                    time.sleep(1)
                    print(f"Helldiver down! Sending down reinforcements! Orbital has {stats['reinforcements']}"
                          "Helldivers left! Continue the fight for liberty!")
            elif fuel == 75:
                time.sleep(1)
                print("Almost done, hang in there! "
                      f"{stats['current_hp']} health and {stats['current_ammo']} ammo left!")
            else:
                time.sleep(1)
                print("Fueling complete! Head up to the console and launch hell on them!")


def launch_icbm(seconds, stats):
    time.sleep(3)
    print("Launch codes operational! Hit the button, protect the console, and stay the hell away from the missile!")
    time.sleep(1)
    while seconds > 1:
        seconds -= 1
        time.sleep(1)
        print(seconds)
        if seconds == 14:
            basic_functions.decrease_stats(stats)
            if basic_functions.check_death(stats):
                time.sleep(1)
                print(f"Helldiver down! Sending down reinforcements! Orbital has {stats['reinforcements']}"
                      "Helldivers left! Continue the fight for liberty!")
            else:
                time.sleep(1)
                print("Fourteen seconds left! Ignition commencing! Keep those Terminids off of the console!"
                      f"{stats['current_hp']} health and {stats['current_ammo']} ammo left!")
        elif seconds == 7:
            basic_functions.decrease_stats(stats)
            if basic_functions.check_death(stats):
                time.sleep(1)
                print(f"Helldiver down! Sending down reinforcements! Orbital has {stats['reinforcements']}"
                      "Helldivers left! Continue the fight for liberty!")
            else:
                time.sleep(1)
                print("Seven seconds left! Protect that console with your life! "
                      f"{stats['current_hp']} health and {stats['current_ammo']} ammo left!")
            if basic_functions.roll_d6() == 1:
                basic_functions.lost_life(stats)
                time.sleep(1)
                print("You're too close to the blast radius! Back away, before you're burnt to a crisp- Ah, too late! "
                      "Helldiver down! Sending down reinforcements!\n"
                      f"Orbital has {stats['reinforcements']} Helldivers left!"
                      " Continue the fight for liberty!")
        elif seconds == 1:
            time.sleep(1)
            print("We have liftoff! Good work, Helldiver, eliminate the rest of those vermin and head to extraction!"
                  " The missile will do the rest!")


# third mission
player = classes.Helldiver(name="Helldiver", health=100)
boss = classes.Boss(name="The Bile Titan", health=100, weapon=weapons.titan_attack)


def boss_fight(stats):
    time.sleep(2)
    print("There it is, the massive beast! Listen up, Helldiver! An emergency situation demanded we redirect your "
          "reinforcements towards an urgent side objective!")
    time.sleep(3)
    print("This means you're alone in this one! To make up for it, "
          "Orbital is sending down a medical supply package, as well as a weapon of your choice!")
    time.sleep(3)
    print("Heal up, and transmit what weapon you want to use against this fiend!")
    time.sleep(3)
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
        print(f"Health of {boss.name}: {boss.health}")
        time.sleep(3)
    if boss.health <= 0:
        time.sleep(2)
        print("The vile beast has been felled! Great job, Helldiver, that will put a dent in their plans! Now head to "
              "extraction!")
        time.sleep(1)
        return "mission successful"
    else:
        time.sleep(1)
        print("You were our last hope! Mission failed, Orbiter departing!")
        return "mission failed"
