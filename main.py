import time
import basic_functions, missions

mission_data = basic_functions.read_mission_data()

mission_type = mission_data["mission_type"]
civilian_status = mission_data['civilian_status']
generator_hp = mission_data['generator_hp']
stats = mission_data['stats']

player_score = mission_data['player_score']


if __name__ == '__main__':
    # get player name from function
    player_name = basic_functions.get_player_name()
    time.sleep(1)

    # choose mission
    print(f"Helldiver {player_name.strip()}, choose in what way you want to save the world today! ")
    mission_pick = basic_functions.mission_choice_function(mission_type)

    # roll and run a random event on the way to the mission
    missions.roll_event(stats)

    # run the selected mission
    match mission_pick:
        case 1:
            missions.rescue_mission(stats, civilian_status, player_score, player_name)
        case 2:
            missions.icbm_mission(stats, generator_hp, player_score, player_name)
        case 3:
            missions.boss_mission(stats, player_score, player_name)

