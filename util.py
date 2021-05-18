import os
import pickle
from typing import Type

import player as player_module
# from commands.creations.item import CreateKnifeCmd, CreateCrowbarCmd, CreateBaseballBatCmd, CreateRoadSignCmd, \
#     CreateBowCmd, CreateCrossbowCmd, CreateShotgunCmd, CreatePistolCmd, CreateHuntingRifleCmd, CreateSniperRifleCmd
import items.weapons.melee as MeleeWeapon_module
import items.weapons.ranged as RangedWeapon_module
import items.weapons.ammo as Ammo_module
import items.consumables.health as HealthConsumable_module

saves_folder_name = "test_saves"
player_list_path = os.path.join(saves_folder_name, "test_player_list.txt")

emoji_symbols = {
    "level": ":muscle:",
    "health": ":heart:",
    "money": ":moneybag:",
    "melee": ":boxing_glove:",
    "range": ":flying_disc:",
    "exp": ":sparkles:",
    "gear": ":school_satchel:",
    "armor": ":military_helmet:",
    "diamond": ":gem:",
    "?": ":grey_question:"
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
    # step 1: get the list of save_keys
    save_keys = []

    try:
        with open(player_list_path, 'rt') as player_list_file:
            save_key = player_list_file.readline().strip()

            while save_key.strip() != "" and save_key not in save_keys:
                save_keys.append(save_key.strip())
                save_key = player_list_file.readline()

    except FileNotFoundError:
        pass

    # step 2: load each player's data one by one
    player_data = {}

    if len(save_keys) > 0:
        print("Rebuilding player_data...", end=" ")
        for save_key in save_keys:
            player_id, guild_id = str(save_key).split('@')
            player_name, trash = player_id.split('#')
            player_data[save_key] = player_module.Player(load_progress(player_name))
    print("Done!")
    return player_data


def save_all_data_and_shut_down(player_data: dict):
    with open(player_list_path, 'w') as player_list_file:
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


def dict_to_proper_item_type(item_dict: dict):
    if isinstance(item_dict, dict):
        item_name = item_dict["name"]
        # special case
        if item_name == "none":
            return None

        # melee weapons
        elif item_name == MeleeWeapon_module.Knife.name:
            return MeleeWeapon_module.Knife(item_dict)
        elif item_name == MeleeWeapon_module.Crowbar.name:
            return MeleeWeapon_module.Crowbar(item_dict)
        elif item_name == MeleeWeapon_module.BaseballBat.name:
            return MeleeWeapon_module.BaseballBat(item_dict)
        elif item_name == MeleeWeapon_module.RoadSign.name:
            return MeleeWeapon_module.RoadSign(item_dict)

        # archery stuff
        elif item_name == Ammo_module.Arrow.name:
            return Ammo_module.Arrow()
        elif item_name == RangedWeapon_module.Bow.name:
            return RangedWeapon_module.Bow(item_dict)
        elif item_name == RangedWeapon_module.Crossbow.name:
            return RangedWeapon_module.Crossbow(item_dict)

        # shotgun stuff
        elif item_name == Ammo_module.Shell.name:
            return Ammo_module.Shell()
        elif item_name == RangedWeapon_module.Shotgun.name:
            return RangedWeapon_module.Shotgun(item_dict)

        # pistol stuff
        elif item_name == Ammo_module.Bullet.name:
            return Ammo_module.Bullet()
        elif item_name == RangedWeapon_module.Pistol.name:
            return RangedWeapon_module.Pistol(item_dict)

        # rifle stuff
        elif item_name == Ammo_module.RifleBullet.name:
            return Ammo_module.RifleBullet()
        elif item_name == RangedWeapon_module.HuntingRifle.name:
            return RangedWeapon_module.HuntingRifle(item_dict)
        elif item_name == RangedWeapon_module.SniperRifle.name:
            return RangedWeapon_module.SniperRifle(item_dict)

        # health consumables
        elif item_name == HealthConsumable_module.PainKillers.name:
            return HealthConsumable_module.PainKillers(item_dict)
        elif item_name == HealthConsumable_module.FirstAidKit.name:
            return HealthConsumable_module.FirstAidKit(item_dict)
        elif item_name == HealthConsumable_module.Medkit.name:
            return HealthConsumable_module.Medkit(item_dict)
        elif item_name == HealthConsumable_module.Antidote.name:
            return HealthConsumable_module.Antidote(item_dict)

        # armor

        # buff gear

        # storage gear

        # if name is not found
        else:
            print(f"ERROR: {item_dict['name']} has not been added to dict_to_proper_item_type(item_dict) function!!!")
