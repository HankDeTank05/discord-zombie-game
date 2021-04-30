import random
import pickle
import time
import math

import items


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
    def load_guild_states():
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
    def save_guild_states(_guild_states):
        """
        Save the current guild states to a persistent data format.
        :param _guild_states:
        A dictionary whose keys are the guild ID's and whose corresponding value is a GameState object.
        :return:
        """
        if isinstance(_guild_states, dict):
            with open(GameState.fname, 'wb') as guild_file:
                pickle.dump(_guild_states, guild_file)


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

    def upgrade(self):
        if self.upgrade_pot > self.upgrade_cost:
            self.level += 1

            self.max_health = Base.upgrades[self.level]["mhealth"]
            self.cur_health = self.max_health

            self.max_defense = Base.upgrades[self.level]["mdefense"]
            self.cur_defense = self.max_defense

            self.upgrade_cost = Base.upgrades[self.level]["mupgrade"]
            self.upgrade_pot -= self.upgrade_cost


class Storage:

    def __init__(self):
        self.guns = GunStorage(2)
        self.bullets = BulletStorage(100)
        self.bows = BowStorage(3)
        self.arrows = ArrowStorage(15)
        self.medkits = MedkitStorage(10)

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

    def __init__(self, _capacity):
        self.capacity = _capacity
        self.items = []


class GunStorage(StorageUnit):

    def store(self, _item):
        if isinstance(_item, items.Gun) and len(self.items) < self.capacity:
            self.items.append(_item)
        elif not isinstance(_item, items.Gun):
            # item is not a gun
            pass
        elif len(self.items) >= self.capacity:
            # storage unit is full
            pass


class BulletStorage(StorageUnit):

    def store(self, _item):
        if isinstance(_item, items.Bullet) and len(self.items) < self.capacity:
            self.items.append(_item)
        elif not isinstance(_item, items.Gun):
            # item is not a Bullet
            pass
        elif len(self.items) >= self.capacity:
            # storage unit is full
            pass


class BowStorage(StorageUnit):

    def store(self, _item):
        if isinstance(_item, items.Bullet) and len(self.items) < self.capacity:
            self.items.append(_item)
        elif not isinstance(_item, items.Bow):
            # item is not a Bow
            pass
        elif len(self.items) >= self.capacity:
            # storage unit is full
            pass


class ArrowStorage(StorageUnit):

    def store(self, _item):
        if isinstance(_item, items.Arrow) and len(self.items) < self.capacity:
            self.items.append(_item)
        elif not isinstance(_item, items.Arrow):
            # item is not an Arrow
            pass
        elif len(self.items) >= self.capacity:
            # storage unit is full
            pass


class MedkitStorage(StorageUnit):

    def store(self, _item):
        if isinstance(_item, items.Medkit) and len(self.items) < self.capacity:
            self.items.append(_item)
        elif not isinstance(_item, items.Medkit):
            # item is not a Medkit
            pass
        elif len(self.items) >= self.capacity:
            # storage unit is full
            pass
