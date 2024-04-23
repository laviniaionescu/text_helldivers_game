
import functions


mission_type = ["1. Search and Destroy", "2. Rescue Operation", "3. Launch ICBM"]

stats = {"reinforcements": 5, "current_hp": 100, "current_ammo": 100}


while stats['reinforcements'] != 0:
    print("Welcome Helldiver! Choose in what way you want to save the world today!")
    for mission in mission_type:
        print(mission)
    mission_pick = input("Press 1, 2 or 3: ")
    while mission_pick not in ["1", "2", "3"]:
        mission_pick = input("Press 1, 2 or 3: ")

    print("You dropped in on the battlefield!")
    obj_explore = input("Do you want to go to the objective, or explore? ")
    while obj_explore.lower() not in ("objective", "explore"):
        obj_explore = input("Time is Liberty, Helldiver! Do you want to go to the objective, or explore? ")

########################################
    if obj_explore.lower() == "explore":
        print("You start exploring the area.")
########################################
    else:
        print("You head to the objective.")

        if functions.event_roll() == "normal_bug_spawn":
            print("A swarm of Terminids crawl from the sand!")
            fight_flight = input("Do you bravely exterminate the vermin for liberty, "
                                 "or run away like a coward deserter?\n"
                                 "Fight or flight? ")
            while fight_flight.lower() not in ("fight", "flight"):
                fight_flight = input("This is not the time to freeze, Helldiver! Fight or flight!? ")
            if fight_flight == "fight":
                print("You pull out your trusty rifle and proceed to dispense liberty to the freedom-hating Terminids!")

                # you lose ammo and hp fighting them
                functions.decrease_stats(stats)

                # if their hp is low enough, they can die in the rest of the fight
                if functions.death_prob(stats["current_hp"]) == 1:
                    functions.lost_life(stats)
                    print(f"Helldiver down! Sending down reinforcements! Orbital has {stats['reinforcements']} "
                          f"Helldivers left! Continue the fight for liberty!")
                    # if they die, the hp is reset
                    functions.reset_hp(stats)
                    # they lose ammo and hp again
                    functions.decrease_stats(stats)
                    print(f"The battle is hard, but you fight for freedom and win! The alien scum left you with"
                          f" {stats['current_ammo']} ammunition and {stats['current_hp']} health.")
                else:
                    # they don't die, only take dmg and ammo loss
                    print(f"The battle is hard, but you fight for freedom and win! The alien scum left you with"
                          f" {stats['current_ammo']} ammunition and {stats['current_hp']} health.")
            else:
                print("You decide to run like a dishonorable deserter, disappointing Freedom and Liberty both!")
                # if they run, they can get caught up and killed
                if functions.death_prob(stats['current_hp']) == 1:
                    functions.lost_life(stats)
                    functions.reset_hp(stats)
                    print(f"The swarm of vermin gave chase and didn't relent, they caught you and killed you! "
                          f"Helldiver down! Sending down reinforcements!\n"
                          f"Orbital has {stats['reinforcements']} Helldivers left!"
                          " Continue the fight for liberty!")

        elif functions.event_roll() == "hive_spawn":
            print("What's that, you came across a Terminid hive! Do you eradicate them all, or proceed to the"
                  " objective by using advanced stealth evasion tactics?")
            kill_evade = input("Destroy, or evade? ")
            while kill_evade.lower() not in ("destroy", "evade"):
                kill_evade = input("Make a decision helldiver! Destroy the pests, or evade?")
            if kill_evade == "destroy":
                # throwing a grenade in the hole can bounce off an enemy
                if functions.grenade_bounce() == 1:
                    print("You open fire on the hive, decimating the vermin protecting it! You begin tossing grenades "
                          " in the holes to shut the pests in when one of them crawls out just as you throw the grenade!"
                          " It bounces right off the giant insect's hard shell and flies back into your arms!")
                    functions.lost_life(stats)
                    functions.reset_hp(stats)
                    print(f"Helldiver down! Sending down reinforcements!\n"
                          f"Orbital has {stats['reinforcements']} Helldivers left!"
                          "Tossing the last grenade in finishes the job and destroys the hive!")
                else:
                    print("You open fire on the hive, decimating the vermin protecting it, then tossing grenades in the"
                          "hive openings to shut the rest of them in! Hive destroyed!")
                    functions.decrease_stats(stats)
                    print(f"The battle is hard, but you fight for freedom and win! The alien scum left you with"
                          f" {stats['current_ammo']} ammunition and {stats['current_hp']} health.")
            else:
                if functions.death_prob(stats['current_hp']) == 1:
                    functions.lost_life(stats)
                    functions.reset_hp(stats)
                    print(f"You begin tactically avoiding the hive, but an unsuspecting sneeze alerts the enemy to your"
                          " presence! You start emergency evasive maneuvers, but the faster ones catch up to you!\n"
                          "Helldiver down! Sending down reinforcements!\n"
                          f"Orbital has {stats['reinforcements']} Helldivers left!")
                else:
                    print("You let the vermin live another day, ensuring they'll be a deadly issue to the next unlucky"
                          " Helldiver who saves the world in this area!")

        elif functions.event_roll() == "meteor_shower":
            # getting hit by a meteor is an instant death
            print("The skies turn dark, you look up and see a rain of meteors about to commence! Dodge, Helldiver!")
            if functions.roll_d6() == 1:
                functions.lost_life(stats)
                functions.reset_hp(stats)
                print("Just as you thought the rock shower was about to end, one of the giant boulders lands right on"
                      " top of you!\n"
                      "Helldiver down! Sending down reinforcements!\n"
                      f"Orbital has {stats['reinforcements']} Helldivers left!")
            else:
                print("You emerge in one piece through the shower of boulders! Carry on, Helldiver!")

        elif functions.event_roll() == "fire_tornadoes":
            print("The skies turn red, you look up and see the twisting fires above connecting to the ones below! "
                  "Avoid the fire tornadoes at all cost!")
            # a d6 chance to get caught in the fire tornado
            if functions.roll_d6() == 1:
                # if they get touched by it, it does more damage than usual
                functions.hp_loss() * 2
                print("You've stumbled right into one of them! Drop and roll, Helldiver!")
                # they have a chance of dying, higher if lost more hp
                if functions.death_prob(stats) == 1:
                    print("It's too late! Helldiver down! Sending down reinforcements!\n"
                          f"Orbital has {stats['reinforcements']} Helldivers left!")
                else:
                    print(f"You've made it through with {stats['current_hp']} left! Carry on, Helldiver!")

        # print("You made it to the objective!")