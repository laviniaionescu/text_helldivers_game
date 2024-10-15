import basic_functions, main_functions


def roll_event(stats):
    run_event = basic_functions.event_roll()
    if run_event == "normal_bug_spawn":
        basic_functions.normal_bug_spawn(stats)

    elif run_event == "hive_spawn":
        basic_functions.hive_spawn(stats)

    elif run_event == "meteor_shower":
        basic_functions.meteor_shower(stats)

    elif run_event == "fire_tornadoes":
        basic_functions.fire_tornadoes(stats)


def rescue_mission(stats, civilian_status, player_score, player_name):
    rescue_civs = main_functions.rescue_operation(stats, civilian_status)
    if rescue_civs == "mission successful":
        # mission successful, update player score, run extraction, write player score
        player_score = basic_functions.update_player_score(player_score)
        player_score += 10
        main_functions.extraction(30, stats)
        basic_functions.write_player_score(player_name, player_score)
        exit()
    else:
        exit()


def icbm_mission(stats, generator_hp, player_score, player_name):
    # run the 3 stages of the mission then write the score
    main_functions.generator_boot(20, generator_hp, stats)
    main_functions.fuel_icbm(stats)
    main_functions.launch_icbm(20, stats)
    player_score = basic_functions.update_player_score(player_score)
    player_score += 20
    main_functions.extraction(30, stats)
    basic_functions.write_player_score(player_name, player_score)
    exit()


def boss_mission(stats, player_score, player_name):
    boss_fight = main_functions.boss_fight(stats)
    if boss_fight == "mission successful":
        # if mission is successful, update the score, go to extraction, write the score
        player_score = basic_functions.update_player_score(player_score)
        player_score += 30
        main_functions.extraction(30, stats)
        basic_functions.write_player_score(player_name, player_score)
        exit()
    else:
        # if mission failed, exit
        exit()
