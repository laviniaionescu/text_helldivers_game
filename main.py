
import random
import functions


mission_type = ["Search and Destroy, Rescue Operation, Launch ICBM"]
# turn these into dictionary
reinforcements = 5
current_hp = 100
current_ammo = 100


while reinforcements != 0:
    print("Welcome Helldiver! Choose in what way you want to save the world today!")
    for mission in mission_type:
        print(mission)
    mission_pick = input("Press 1, 2 or 3: ")
    while mission_pick not in ["1", "2", "3"]:
        mission_pick = input("Press 1, 2 or 3: ")

    print("You dropped in on the battlefield!")
    obj_explore = input("Do you want to go to the objective, or explore? ")
    while obj_explore.lower() not in ("objective", "explore"):
        obj_explore = input("Do you want to go to the objective, or explore? ")
    if obj_explore.lower() == "objective":
        print("You head to the objective.")

        if functions.event_roll() == 1:
            print("A swarm of Terminids crawl from the sand!")
            fight_flight = input("Do you bravely exterminate the vermin for liberty, "
                                 "or run away like a coward deserter?\n"
                                 "Fight or flight? ")
            while fight_flight.lower() not in ("fight", "flight"):
                fight_flight = input("This is not the time to freeze, Helldiver! Fight or flight!? ")
            if fight_flight == "fight":
                print("You pull out your trusty rifle and proceed to dispense liberty to the freedom-hating Terminids!")
                lost_ammo = functions.ammo_loss()
                if functions.death_prob(current_hp) == 1:
                    reinforcements -= 1
                    print(f"Helldiver down! Sending down reinforcements! Orbital has {reinforcements} Helldivers left!"
                          f" Continue the fight for liberty!")
                dodge = functions.roll_d10()
                if dodge == 1:
                    current_hp = current_hp
                else:
                    current_hp -= functions.hp_loss()
                current_ammo -= lost_ammo
                print(f"The battle is hard, but you fight for freedom and win! The alien scum left you with"
                      f" {current_ammo} ammunition and {current_hp} health.")
            else:
                print("You decide to run like a dishonorable deserter, disappointing Freedom and Liberty both!")
                if functions.death_prob(current_hp) == 1:
                    reinforcements -= 1
                    print(f"The swarm of vermin gave chase and didn't relent, they caught you and killed you! "
                          f"Helldiver down! Sending down reinforcements!\n"
                          f"Orbital has {reinforcements} Helldivers left!"
                          " Continue the fight for liberty!")

        elif functions.event_roll() == 2:
            print("What's that, you came across a Terminid hive! Do you eradicate them all, or proceed to the"
                  "objective by using advanced stealth evasion tactics?")
            kill_evade = input("Destroy, or evade? ")
            while kill_evade.lower() not in ("destroy", "evade"):
                kill_evade = input("Make a decision helldiver! Destroy the pests, or evade?")
            if kill_evade == "kill":
                pass

    else:
        print("You start exploring the area.")

