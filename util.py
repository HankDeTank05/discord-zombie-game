import os
import pickle
import player as player_module

saves_folder_name = "test_saves"
player_list_path = os.path.join(saves_folder_name, "test_player_list.txt")

emoji_symbols = {
    "level": ":muscle:",
    "health": ":heart:",
    "money": ":dollar:",
    "exp": ":sparkles:"
}


def save_file_name(save_key: str) -> str:
    """
    Constructs the relative path of a player's save file.
    :param save_key:
    The discord tag of the player.
    :return:
    A string representing the relative path of a player's save file.
    """
    return os.path.join(saves_folder_name, save_key + ".pickle")


def new_save_file(save_key: str, data: dict) -> dict:
    """
    Create a new save file for a player. This is done by saving an empty dictionary to a new save file and then
    immediately loading it from that newly created save file.
    :param data:
    A dictionary representing the player's progress.
    :param save_key:
    The discord tag of the player.
    :return:
    A dictionary representing the player's progress.
    """
    try:
        with open(save_file_name(save_key), 'xb') as player_save:
            pickle.dump(data, player_save)
    except FileNotFoundError:
        os.mkdir(saves_folder_name)
        with open(save_file_name(save_key), 'xb') as player_save:
            pickle.dump(data, player_save)

    return data


def save_progress(save_key: str, data: dict):
    """
    Save the player's progress to a file.
    :param save_key:
    The discord tag of the player whose progress should be saved.
    :param data:
    The dictionary representing the player's progress.
    :return:
    """

    if isinstance(data, dict):
        with open(save_file_name(save_key), 'wb') as player_save:
            pickle.dump(data, player_save)
    else:
        print(f"Error attempting to save progress for save_key={save_key}. Data must be a dictionary, but was of type"
              f" {type(data)}!")


def load_progress(save_key: str) -> dict:
    """
    Load a player's progress from a save file.
    :param save_key:
    The discord tag of the player whose progress should be loaded.
    :return:
    The dictionary representing the player's progress.
    """
    with open(save_file_name(save_key), 'rb') as player_save:
        data = pickle.load(player_save)

    return data


def emoji(in_game_name: str) -> str:
    return emoji_symbols[in_game_name]


def rebuild_player_data() -> dict:
    # step 1: get the list of player tags
    player_tags = []

    try:
        with open(player_list_path, 'rt') as player_list_file:
            player_name = player_list_file.readline().strip()

            while player_name != "":
                player_tags.append(player_name)
                player_name = player_list_file.readline()

    except FileNotFoundError:
        pass

    # step 2: load each player's data one by one
    player_data = {}

    if len(player_tags) > 0:
        print("Rebuilding player_data")
        for tag in player_tags:
            player_name, trash = tag.split('#')
            player_data[tag] = player_module.Player(load_progress(player_name))

    return player_data


def save_all_data_and_shut_down(player_data: dict):
    with open(player_list_path, 'a') as player_list_file:
        for save_key in player_data.keys():
            player_id, guild_id = str(save_key).split('@')
            player_name, trash = player_id.split('#')

            player_list_file.write(str(save_key) + "\n")
            print(f"Save key '{save_key}' has been written to the player list.")

            save_progress(player_name, player_data[save_key].make_data_dict())
            print(f"Saved progress of '{player_name}'")

    exit(0)


def print_dict(data: dict, indent: int = 0):
    print("Printing dictionary...")
    for key in data.keys():
        print(f"{key},{type(key)}\t:\t{data[key]},{type(data[key])}")


def make_save_key(guild_id: int, player_id: str) -> str:
    return player_id + '@' + str(guild_id)
