import random
import pickle
import time

import items
from CommandObj import *


class GameState:
    fname = "guild_states.p"

    def __init__(self):
        self.profiles = {}
        self.base = Base()
        self.storage = Storage()

    def new_player(self, _player_name):
        """
        Create a new player profile for this guild's game.
        :param _player_name:
        A player's discord username, a string.
        :return:
        Returns the response to be sent by the calling command, a string.
        """
        if _player_name not in self.profiles.keys():
            self.profiles[_player_name] = Player()
            response = f"Welcome to the zombie apocalypse, {_player_name}!"
            if len(self.profiles.keys()):
                response += " You're the first one here!"
            return response
        else:
            return f"You already started playing, {_player_name}!"

    def get_player(self, _player_name):
        """
        Get the player object with a given name.
        :param _player_name:
        The name of the player whose player object should be returned.
        :return:
        The player object corresponding to _player_name
        """
        return self.profiles[_player_name]

    @staticmethod
    def load_all_guild_states():
        """
        Load guild states from the file of the default filename.
        :return:
        """
        guild_states = {}

        try:
            with open(GameState.fname, 'rb') as guild_file:
                guild_states = pickle.load(guild_file)
        except FileNotFoundError:
            with open(GameState.fname, 'xb') as guild_file:
                pickle.dump(guild_states, guild_file)

        return guild_states

    @staticmethod
    def load_guild_state(guild_id: int) -> dict:
        """
        Load a single guild state from its pickle file.
        :param guild_id:
        The ID of the guild whose save state should be loaded.
        :return:
        Return a dictionary containing
        """

        guild_state = {}

        try:
            # try to open the guild's save state (if it exists)
            with open(str(guild_id) + GameState.fname, 'rb') as guild_file:
                guild_state = pickle.load(guild_file)
        except FileNotFoundError:
            # if the file wasn't found, write an empty dictionary to a new save state and then immediately load it
            with open(str(guild_id) + GameState.fname, 'xb') as guild_file:
                pickle.dump(guild_state, guild_file)
                guild_state = pickle.load(guild_file)

        return guild_state

    @staticmethod
    def save_all_guild_states(_guild_states):
        """
        Save all of the current guild states to a persistent data format.
        :param _guild_states:
        A dictionary whose keys are the guild ID's and whose corresponding value is a GameState object.
        :return:
        """
        if isinstance(_guild_states, dict):
            with open(GameState.fname, 'wb') as guild_file:
                pickle.dump(_guild_states, guild_file)

    @staticmethod
    def save_guild_state(guild_id: int, guild_state: dict) -> None:
        """
        Save a single guild's state to a file.
        :param guild_id:
        The ID of the guild whose state should be saved.
        :param guild_state:
        The dictionary containing the guild's state.
        :return:
        """

        with open(str(guild_id) + GameState.fname, 'wb') as guild_file:
            pickle.dump(guild_state, guild_file)

        pass


class Player:

    starting_health = 20

    def __init__(self):
        self.level = 1
        self.exp = 0

        self.max_health = Player.starting_health
        self.health = self.max_health
        self.armor = 0

        self.weapon = items.Knife()

        self.ammo = None

        self.inventory = []
        self.inventory_cap = 30

        self.money = 0

        self.cooldowns = {
            "fight": -1
        }

    def profile(self):
        """
        Get the player's profile information.
        :return:
        A string containing the player's profile information.
        """
        response = f":heart: Health: {self.health}/{self.max_health}\n" \
                   f":dollar: Money: ${self.money}\n"

        if self.weapon is not None:
            response += f":crossed_swords: Weapon: {self.weapon.name}\n" \
                        f":gem: Weapon Durability: {self.weapon.durability}\n"

        response += f":shield: Armor: {self.armor}\n" \
                    f":toolbox: Inventory: {len(self.inventory)}/{self.inventory_cap}\n"

        return response

    def equip(self, item):
        """
        Equip some item from your inventory.
        :param item:
        :return:
        """
        pass

    def fight(self):
        """
        Fight zombies using whatever you have equipped.

        Loose 10-20% of your health each time.
        Gain between 2-4x the damage output of your weapon in money.
        Loose one point of durability each time you fight.

        :return:
        """
        response = ""
        if time.time() > self.cooldowns["fight"] or self.cooldowns["fight"] == -1:
            lost_hp = random.randrange(self.max_health//10, self.max_health//5)
            self.health -= lost_hp
            gained_money = random.randrange(self.weapon.damage_out*2, self.weapon.damage_out*4)
            self.weapon.durability -= 1
            self.money += gained_money
            response += f"You fought some zombies with your {self.weapon.name}!\n" \
                        f"You lost {lost_hp} HP, but you earned ${gained_money}!\n" \
                        f"Current health: {self.health}.\n" \
                        f"Current money: {self.money}"

            self.cooldowns["fight"] = time.time() + 60
        else:
            response += f"You must wait {round(self.cooldowns['fight'] - time.time())} seconds before fighting again!"

        return response

    def pick_up(self, _item):
        if issubclass(_item, items.Item):
            self.inventory.append(_item)


class Base:
    upgrades = [
        None,
        {
            "mhealth": 100,
            "mdefense": 25,
            "mupgrade": 1000
        },
        {
            "mhealth": 250,
            "mdefense": 50,
            "mupgrade": 10000
        },
        {
            "mhealth": 500,
            "mdefense": 100,
            "mupgrade": 1000000
        },
        {
            "mhealth": 1000,
            "mdefense": 150,
            "mupgrade": None
        }
    ]

    def __init__(self, _level=1):
        self.level = _level

        self.max_health = Base.upgrades[self.level]["mhealth"]
        self.cur_health = self.max_health

        self.max_defense = Base.upgrades[self.level]["mdefense"]
        self.cur_defense = self.max_defense

        self.upgrade_cost = Base.upgrades[self.level]["mupgrade"]
        self.upgrade_pot = 0

        self.shop = {
            "Knife": {
                "base level": 1,
                "player level": 1,
                "cost": 100,
                "buy command": BuyKnifeCmd(100)
            },
            "Sword": {
                "base level": 2,
                "player level": 5,
                "cost": 250,
                "buy command": BuySwordCmd(250)
            },
            "Bow": {
                "base level": 3,
                "player level": 10,
                "cost": 500,
                "buy command": BuyBowCmd(500)
            },
            "Arrow": {
                "base level": 3,
                "player level": 10,
                "cost": 25,
                "buy command": BuyArrowCmd(25)
            },
            "Pistol": {
                "base level": 4,
                "player level": 15,
                "cost": 2000,
                "buy command": BuyPistolCmd(2000)
            },
            "Bullet": {
                "base level": 4,
                "player level": 15,
                "cost": 50,
                "buy command": BuyBulletCmd(50)
            },
            "Shotgun": {
                "base level": 5,
                "player level": 25,
                "cost": 5000,
                "buy command": BuyShotgunCmd(5000)
            },
            "Shell": {
                "base level": 5,
                "player level": 25,
                "cost": 75,
                "buy command": BuyShellCmd(75)
            },
            "Flamethrower": {
                "base level": 10,
                "player level": 50,
                "cost": 50000,
                "buy command": BuyFlamethrowerCmd(50000)
            }
        }

    def status(self):
        response = ""

        response += f":heart: Base Health: {self.cur_health}/{self.max_health}\n" \
                    f":shield: Base Defense: {self.max_defense}/{self.cur_defense}\n" \
                    f":dollar: Upgrade pot: {self.upgrade_pot}\n" \
                    f":arrow_up: Next upgrade: {self.upgrade_cost}\n"

        return response

    def upgrade(self):
        if self.upgrade_pot > self.upgrade_cost:
            self.level += 1

            self.max_health = Base.upgrades[self.level]["mhealth"]
            self.cur_health = self.max_health

            self.max_defense = Base.upgrades[self.level]["mdefense"]
            self.cur_defense = self.max_defense

            self.upgrade_cost = Base.upgrades[self.level]["mupgrade"]
            self.upgrade_pot -= self.upgrade_cost

            if self.level >= 2:
                pass

    def shop(self):
        response = ""

        return response


class Storage:

    def __init__(self):
        self.weapons = WeaponStorage(10)
        self.ammo = AmmoStorage(50)
        self.healers = HealerStorage(100)

    def status(self):
        response = ""

        response += ""

        return response

    def store(self, _item):
        if isinstance(_item, items.Gun):
            self.guns.store(_item)
        elif isinstance(_item, items.Bullet):
            self.bullets.store(_item)
        elif isinstance(_item, items.Bow):
            self.bows.store(_item)
        elif isinstance(_item, items.Arrow):
            self.arrows.store(_item)
        elif isinstance(_item, items.Medkit):
            self.medkits.store(_item)
        else:
            # _item is of invalid type
            pass

        pass


class StorageUnit:

    def __init__(self, _capacity: int, _type):
        self.capacity = _capacity
        self.type = _type
        self.items = []

    def store(self, _item):
        if issubclass(_item, self.type) and len(self.items) < self.capacity:
            self.items.append(_item)
        elif not issubclass(_item, self.type):
            # item is not of the unit's storage type
            pass
        elif len(self.items) >= self.capacity:
            # storage unit is full
            pass

    def upgrade_capacity(self, _new_capacity: int):
        self.capacity = _new_capacity


class WeaponStorage(StorageUnit):

    def __init__(self, _capacity: int):
        super().__init__(_capacity, Weapon)


class AmmoStorage(StorageUnit):

    def __init__(self, _capacity: int):
        super().__init__(_capacity, Ammo)


class HealerStorage(StorageUnit):

    def __init__(self, _capacity: int):
        super().__init__(_capacity, Healer)