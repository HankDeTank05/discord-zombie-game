import random
from typing import Union, Type

import util
from items.item import Item
from items.weapons.melee import Knife
from items.weapons.ranged import Bow


class Player:
    max_health = [
        0,
        100
    ]

    max_inventory = 30

    def __init__(self, player: Union[str, dict]):
        if isinstance(player, dict):
            self.id = player["id"]
            self.level = player["level"]
            self.health = player["health"]
            self.money = player["money"]

            # update weapon_melee
            try:
                self.weapon_melee = util.dict_to_proper_weapon_type(player["weapon_melee"])
            except KeyError:
                self.weapon_melee = Knife()

            # update weapon_ranged
            try:
                self.weapon_ranged = util.dict_to_proper_weapon_type(player["weapon_ranged"])
            except KeyError:
                self.weapon_ranged = Bow()

            # update inventory

        elif isinstance(player, str):
            self.id = player
            self.level = 1
            self.health = Player.max_health[self.level]
            self.money = 0
            self.weapon_melee = Knife()
            self.weapon_ranged = Bow()
            self.inventory = []

            util.new_save_file(player, self.make_data_dict())
            print(f"Making a new file for {player}")

    def make_data_dict(self) -> dict:
        data = {
            "id": self.id,
            "level": self.level,
            "health": self.health,
            "money": self.money,
            "weapon_melee": self.weapon_melee.make_data_dict(),
            "weapon_ranged": self.weapon_ranged.make_data_dict()
        }
        return data

    def profile(self):
        output = f"__**{self.id}'s profile**__\n" \
                 f"`Level            `{util.emoji('level')} {self.level}\n" \
                 f"`Health           `{util.emoji('health')} {self.health}/{Player.max_health[self.level]}\n" \
                 f"`Money            `{util.emoji('money')} ${self.money}\n" \
                 f"`Equipped (melee) `{util.emoji('melee')} {self.weapon_melee.name}\n" \
                 f"`Equipped (range) `{util.emoji('range')} {self.weapon_ranged.name}\n"
        return output

    def save(self):
        util.save_progress(self.id, self.make_data_dict())

    def inter_range_size(self) -> int:
        inter_range_size = max(self.weapon_ranged.range_size(), self.weapon_melee.range_size()) \
                           - min(self.weapon_ranged.range_size(), self.weapon_melee.range_size())
        return max(0, inter_range_size)

    def armor_total(self) -> int:
        return 0

    def fight(self):
        health_difference = self.inter_range_size() + random.randrange(0, self.inter_range_size()) - self.armor_total()
        self.health -= health_difference

        zombies_killed = self.weapon_melee.range_size() \
                         + self.weapon_ranged.range_size() \

        money_gained = zombies_killed \
                       + random.randrange(0, self.weapon_melee.bonus_additive + self.weapon_ranged.bonus_additive)
        self.money += money_gained

        output = f"__**Fighting Zombies**__\n" \
                 f"You lost {health_difference} health fighting zombies...\n" \
                 f"Your health is now {util.emoji('health')} {self.health}/{Player.max_health[self.level]}\n" \
                 f"You killed {zombies_killed} zombies!\n" \
                 f"On the bright side, you earned {util.emoji('money')} ${money_gained} from it!"

        return output

    def store_in_inventory(self, item: Type[Item]):
        if issubclass(item, Item) and len(self.inventory) < Player.max_inventory:
            # store in inventory
            pass
        else:
            # do not store in inventory
            pass

    def list_items_in_inventory(self):
        pass


class TmpPlayer(Player):

    def __init__(self, player: str):
        self.id = player
        self.level = 1
        self.health = Player.max_health[self.level]
        self.money = 0
        self.weapon_melee = Knife()
        self.weapon_ranged = Bow()
        self.inventory = []
