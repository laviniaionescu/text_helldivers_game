import time
import basic_functions
import main_functions
import random


mission_type = ["1. Rescue Operation", "2. Launch ICBM", "3. Exterminate Abomination"]
objective_complete = False

civilian_status = {"rescued": 0, "dead": 0}
generator_hp = 100

stats = {"reinforcements": 5, "max_hp": 100, "current_hp": 100, "current_ammo": 200}


while stats['reinforcements'] != 0:
    print("Welcome Helldiver! Choose in what way you want to save the world today!")
    for mission in mission_type:
        print(mission)
    mission_pick = input("Press 1, 2 or 3: ")
    while mission_pick not in ["1", "2", "3"]:
        mission_pick = input("Press 1, 2 or 3: ")
    print("You dropped in on the battlefield!")
    # time.sleep(2)
    obj_explore = input("Do you want to go to the objective, or explore? ")
    while obj_explore.lower() not in ("objective", "explore"):
        obj_explore = input("Time is Liberty, Helldiver! Do you want to go to the objective, or explore? ")

########################################################################################################
    if obj_explore.lower() == "explore":

        print("You start exploring the area.")
########################################################################################################
    else:
        # time.sleep(2)
        print("You head to the objective!")

        if basic_functions.event_roll() == "normal_bug_spawn":
            # time.sleep(2)
            print("A swarm of Terminids crawl from the sand!")
            # time.sleep(2)
            fight_flight = input("Do you bravely exterminate the vermin for liberty, "
                                 "or run away like a coward deserter?\n"
                                 "Fight or flight? ")
            while fight_flight.lower() not in ("fight", "flight"):
                fight_flight = input("This is not the time to freeze, Helldiver! Fight or flight!? ")
            if fight_flight == "fight":
                print("You pull out your trusty rifle and proceed to dispense liberty to the freedom-hating Terminids!")

                # you lose ammo and hp fighting them
                basic_functions.decrease_stats(stats)

                # if their hp is low enough, they can die in the rest of the fight
                if basic_functions.death_prob(stats["current_hp"]) == 1:
                    basic_functions.lost_life(stats)
                    print(f"Helldiver down! Sending down reinforcements! Orbital has {stats['reinforcements']} "
                          f"Helldivers left! Continue the fight for liberty!")
                    # if they die, the hp is reset
                    basic_functions.reset_hp(stats)
                    # they lose ammo and hp again
                    basic_functions.decrease_stats(stats)
                    print(f"The battle is hard, but you fight for freedom and win! The alien scum left you with"
                          f" {stats['current_ammo']} ammunition and {stats['current_hp']} health.")
                else:
                    # they don't die, only take dmg and ammo loss
                    print(f"The battle is hard, but you fight for freedom and win! The alien scum left you with"
                          f" {stats['current_ammo']} ammunition and {stats['current_hp']} health.")
            else:
                print("You decide to run like a dishonorable deserter, disappointing Freedom and Liberty both!")
                # if they run, they can get caught up and killed
                if basic_functions.death_prob(stats['current_hp']) == 1:
                    basic_functions.lost_life(stats)
                    basic_functions.reset_hp(stats)
                    print(f"The swarm of vermin gave chase and didn't relent, they caught you and killed you! "
                          f"Helldiver down! Sending down reinforcements!\n"
                          f"Orbital has {stats['reinforcements']} Helldivers left!"
                          " Continue the fight for liberty!")

        elif basic_functions.event_roll() == "hive_spawn":
            print("What's that, you came across a Terminid hive! Do you eradicate them all, or proceed to the"
                  " objective by using advanced stealth evasion tactics?")
            kill_evade = input("Destroy, or evade? ")
            while kill_evade.lower() not in ("destroy", "evade"):
                kill_evade = input("Make a decision helldiver! Destroy the pests, or evade?")
            if kill_evade == "destroy":
                # throwing a grenade in the hole can bounce off an enemy
                if basic_functions.grenade_bounce() == 1:
                    print("You open fire on the hive, decimating the vermin protecting it! You begin tossing grenades "
                          "in the holes to shut the pests in when one of them crawls out just as you throw the grenade!"
                          " It bounces right off the giant insect's hard shell and flies back into your arms!")
                    basic_functions.lost_life(stats)
                    basic_functions.reset_hp(stats)
                    print(f"Helldiver down! Sending down reinforcements!\n"
                          f"Orbital has {stats['reinforcements']} Helldivers left!"
                          "Tossing the last grenade in finishes the job and destroys the hive!")
                else:
                    print("You open fire on the hive, decimating the vermin protecting it, then tossing grenades in the"
                          "hive openings to shut the rest of them in! Hive destroyed!")
                    basic_functions.decrease_stats(stats)
                    if basic_functions.check_death(stats):
                        print(f"Helldiver down! Sending down reinforcements! Orbital has {stats['reinforcements']}"
                              "Helldivers left! Continue the fight for liberty!")
                    else:
                        print(f"The battle is hard, but you fight for freedom and win! The alien scum left you with"
                              f" {stats['current_ammo']} ammunition and {stats['current_hp']} health.")
            else:
                if basic_functions.death_prob(stats['current_hp']) == 1:
                    basic_functions.lost_life(stats)
                    basic_functions.reset_hp(stats)
                    print(f"You begin tactically avoiding the hive, but an unsuspecting sneeze alerts the enemy to your"
                          " presence! You start emergency evasive maneuvers, but the faster ones catch up to you!\n"
                          "Helldiver down! Sending down reinforcements!\n"
                          f"Orbital has {stats['reinforcements']} Helldivers left!")
                else:
                    print("You let the vermin live another day, ensuring they'll be a deadly issue to the next unlucky"
                          " Helldiver who saves the world in this area!")

        elif basic_functions.event_roll() == "meteor_shower":
            # getting hit by a meteor is an instant death
            print("The skies turn dark, you look up and see a rain of meteors about to commence! Dodge, Helldiver!")
            if basic_functions.roll_d6() == 1:
                basic_functions.lost_life(stats)
                basic_functions.reset_hp(stats)
                print("Just as you thought the rock shower was about to end, one of the giant boulders lands right on"
                      " top of you!\n"
                      "Helldiver down! Sending down reinforcements!\n"
                      f"Orbital has {stats['reinforcements']} Helldivers left!")
            else:
                print("You emerge in one piece through the shower of boulders! Carry on, Helldiver!")

        elif basic_functions.event_roll() == "fire_tornadoes":
            print("The skies turn red, you look up and see the twisting fires above connecting to the ones below! "
                  "Avoid the fire tornadoes at all cost!")
            # a d6 chance to get caught in the fire tornado
            if basic_functions.roll_d6() == 1:
                # if they get touched by it, it does more damage than usual
                basic_functions.hp_loss() * 2
                print("You've stumbled right into one of them! Drop and roll, Helldiver!")
                # they have a chance of dying, higher if lost more hp
                if basic_functions.death_prob(stats) == 1:
                    print("It's too late! Helldiver down! Sending down reinforcements!\n"
                          f"Orbital has {stats['reinforcements']} Helldivers left!")
                    basic_functions.lost_life(stats)
                    basic_functions.reset_hp(stats)
                else:
                    print("You've made it through! Carry on!")
            else:
                print(f"You've made it through! Carry on!")
################################################################################################################
        if mission_pick == "1":
            main_functions.rescue_operation(stats, civilian_status)
            main_functions.extraction(30, stats, objective_complete)

        elif mission_pick == "2":
            main_functions.generator_boot(20, generator_hp, stats)
            main_functions.fuel_icbm(0, stats)
            main_functions.launch_icbm(20, stats)
            main_functions.extraction(30, stats, objective_complete)
        elif mission_pick == "3":
            main_functions.boss_fight()