import basic_functions
import time

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


def generator_boot(seconds, generator_hp, stats):
    while seconds != 0:
        seconds -= 1
        time.sleep(1)
        print(seconds)

        if seconds == 14:
            generator_hp -= basic_functions.hp_loss()
            basic_functions.decrease_stats(stats)
            print(f"14 seconds left! The generator has {generator_hp}% functionality left!")

        elif seconds == 7:
            generator_hp -= basic_functions.hp_loss()
            basic_functions.decrease_stats(stats)
            print(f"7 seconds left! The generator is {generator_hp}% intact, protect it, Helldiver!")

        elif seconds == 1:
            print("almost done")

