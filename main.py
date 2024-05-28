import time
import basic_functions
import main_functions


mission_type = ["1. Rescue Operation", "2. Launch ICBM", "3. Exterminate Abomination"]


civilian_status = {"rescued": 0, "dead": 0}
generator_hp = 100


stats = {"reinforcements": 5, "current_hp": 100, "max_hp": 100, "current_ammo": 200}


if __name__ == '__main__':

    while stats['reinforcements'] != 0:
        player_name = basic_functions.get_player_name()
        print(f"Helldiver {player_name}, choose in what way you want to save the world today! ")
        for mission in mission_type:
            print(mission)
        mission_pick = input("Press 1, 2 or 3: ")
        while mission_pick not in ["1", "2", "3"]:
            mission_pick = input("Press 1, 2 or 3: ")
        else:
            print("You dropped in on the battlefield!")
        # time.sleep(2)
        run_event = basic_functions.event_roll()
        if run_event == "normal_bug_spawn":
            basic_functions.normal_bug_spawn(stats)

        elif run_event == "hive_spawn":
            basic_functions.hive_spawn(stats)

        elif run_event == "meteor_shower":
            basic_functions.meteor_shower(stats)

        elif run_event == "fire_tornadoes":
            basic_functions.fire_tornadoes(stats)
    ####################################################################################
        if mission_pick == "1":
            main_functions.rescue_operation(stats, civilian_status)
            exit()
        elif mission_pick == "2":
            main_functions.generator_boot(20, generator_hp, stats)
            main_functions.fuel_icbm(0, stats)
            main_functions.launch_icbm(20, stats)
            exit()
        elif mission_pick == "3":
            main_functions.boss_fight(stats, main_functions.objective_complete)
            exit()


