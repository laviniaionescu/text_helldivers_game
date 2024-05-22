import random
import basic_functions
import time
import classes
import weapons

objective_complete = False

remaining_health_symbol = "X"
lost_health_symbol = "_"
bars = 20


def health_bars(stats):
    remaining_health_bars = round(stats['current_hp'] / stats['max_hp'] * bars)
    lost_health_bars = bars - remaining_health_bars
    print(f"HEALTH: {stats['current_hp']} / {stats['max_hp']}")
    print(f"|{remaining_health_bars * remaining_health_symbol} {lost_health_bars * lost_health_symbol}|")


def rescue_operation(stats, civilian_status):
    print("We have civilians to rescue, Helldiver! Open the doors and escort them safely to the ship!")
    print("Terminids incoming! Open fire! Protect those civilians at all cost, Helldiver! Too many casualties "
          "and it's over!")
    # we need 5 rescued civilians, if 3 die, it's mission failed
    for i in range(5):
        basic_functions.decrease_stats(stats)
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
            civilian_status['rescued'] += 1
    # print(f"rescued civs {civilian_status['rescued']}")
    # print(f"dead civs {civilian_status['dead']}")
    if civilian_status['dead'] == 3:
        print("We lost too many civilians, the mission is a failure! Train harder, Helldiver!")
        exit()
    else:
        print("Objective complete, good work, Helldiver! Now head over to extraction!")
        objective_complete = True


def generator_boot(seconds, generator_hp, stats):
    print("The ICBM needs fuel, turn on those pump generators!")
    # time.sleep(2)
    print("The sound of the generators activating is attracting Terminids! They're attacking the generators, "
          "protect them while they boot up and destroy the pests!")
    while seconds != 0:
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


def fuel_icbm(fuel, stats):
    print("It's time to put them to good use! Start pumping that fuel to the missile, and destroy the remaining "
          "vermin!")
    fuel = 0
    while fuel != 100:
        fuel += 25
        time.sleep(5)
        basic_functions.decrease_stats(stats)
        if basic_functions.check_death(stats):
            print(f"Helldiver down! Sending down reinforcements! Orbital has {stats['reinforcements']}"
                  "Helldivers left! Continue the fight for liberty!")
        else:
            if fuel == 25:
                print(f"ICBM fuel 25%! Keep them off of you! "
                      f"{stats['current_hp']} health and {stats['current_ammo']} ammo left!")
            elif fuel == 50:
                print("Fuel halfway through! Keep fighting! "
                      f"{stats['current_hp']} health and {stats['current_ammo']} ammo left!")
                basic_functions.decrease_stats(stats)
                if basic_functions.check_death(stats):
                    print(f"Helldiver down! Sending down reinforcements! Orbital has {stats['reinforcements']}"
                          "Helldivers left! Continue the fight for liberty!")
            elif fuel == 75:
                print("Almost done, hang in there! "
                      f"{stats['current_hp']} health and {stats['current_ammo']} ammo left!")
            else:
                print("Fueling complete! Head up to the console and launch hell on them!")


def launch_icbm(seconds, stats):
    print("Launch codes operational! Hit the button, protect the console, and stay the hell away from the missile!")
    while seconds != 1:
        seconds -= 1
        time.sleep(1)
        print(seconds)
        if seconds == 14:
            basic_functions.decrease_stats(stats)
            if basic_functions.check_death(stats):
                print(f"Helldiver down! Sending down reinforcements! Orbital has {stats['reinforcements']}"
                      "Helldivers left! Continue the fight for liberty!")
            else:
                print("Fourteen seconds left! Ignition commencing! Keep those Terminids off of the console!"
                      f"{stats['current_hp']} health and {stats['current_ammo']} ammo left!")
        elif seconds == 7:
            basic_functions.decrease_stats(stats)
            if basic_functions.check_death(stats):
                print(f"Helldiver down! Sending down reinforcements! Orbital has {stats['reinforcements']}"
                      "Helldivers left! Continue the fight for liberty!")
            else:
                print("Seven seconds left! Protect that console with your life! "
                      f"{stats['current_hp']} health and {stats['current_ammo']} ammo left!")
            if basic_functions.roll_d6() == 1:
                basic_functions.lost_life(stats)
                print("You're too close to the blast radius! Back away, before you're burnt to a crisp- Ah, too late! "
                      "Helldiver down! Sending down reinforcements!\n"
                      f"Orbital has {stats['reinforcements']} Helldivers left!"
                      " Continue the fight for liberty!")
        elif seconds == 1:
            print("We have liftoff! Good work, Helldiver, eliminate the rest of those vermin and head to extraction!"
                  "The missile will do the rest!")
            objective_complete = True


def extraction(seconds, stats, objective_complete):
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
                health_bars(stats)

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
            if basic_functions.roll_d6() == 1 and objective_complete:
                print("I said keep away from the shuttle's thrus- Helldiver down! But objective is completed!\n"
                      "Mission accomplished!")


player = classes.Helldiver(name="The Helldiver", health=100)
boss = classes.Boss(name="The Bile Titan", health=100, weapon=weapons.titan_attack)


def boss_fight():
    global objective_complete
    print("There it is, the massive beast! Listen up, Helldiver! An emergency situation demanded we redirect your "
          "reinforcements towards an urgent side objective, this means you're alone in this one! To make up for it, "
          "Orbital is sending down a medical supply package, as well as a weapon of your choice! Heal up, and transmit "
          "what weapon you want to use against this fiend!")
    player_choice = int(input(weapons.WEAPONS))
    match player_choice:
        case 1:
            player.equip(weapons.auto_cannon)
        case 2:
            player.equip(weapons.anti_tank)
        case 3:
            player.equip(weapons.railgun)

    while boss.health != 0 and player.health != 0:
        player.attack(boss)
        boss.attack(player)
        print(f"hp of {player.name}: {player.health}")
        print(f"hp of {boss.name}: {boss.health}")
        input()
    if boss.health <= 0:
        print("The vile beast has been felled! Great job, Helldiver, that will put a dent in their plans! Now head to "
              "extraction!")
        objective_complete = True
    else:
        print("mission failed")
        objective_complete = False
