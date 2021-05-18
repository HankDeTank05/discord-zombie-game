import random
from typing import Union, Type, Tuple

from discord.ext import commands

import util
from items.consumable import Consumable
from items.item import Item, NoneDict
from items.weapon import Weapon
from items.weapons.melee import Knife
from items.weapons.ranged import Bow, SniperRifle
from items.wearables.gears.buff import ProfitBuff


class Player:

    # max level = largest valid index in max_health list
    max_level = 100

    # max health for level L = value at index L
    # value at index L = 100 + (L-1) * 5
    start_health = 100
    health_increase_delta = 5
    max_health = [0] + [hp for hp in range(start_health, (start_health+(max_level-1)*health_increase_delta) + 1, health_increase_delta)]

    # max exp for level L = 50 + (L-1) * 150
    start_max_exp = 500
    max_exp_increase_delta = 500
    max_exp = [0] + [exp for exp in range(start_max_exp, (start_max_exp+(max_level-1)*max_exp_increase_delta) + 1, max_exp_increase_delta)]

    max_inventory = 30

    def __init__(self, player: Union[str, dict]):
        if isinstance(player, dict):
            self.id = player["id"]
            self.level = player["level"]
            self.health = player["health"]
            self.money = player["money"]

            # update weapon_melee
            try:
                self.weapon_melee = util.dict_to_proper_item_type(player["weapon_melee"])
            except KeyError:
                self.weapon_melee = Knife()

            # update weapon_ranged
            try:
                self.weapon_ranged = util.dict_to_proper_item_type(player["weapon_ranged"])
            except KeyError:
                self.weapon_ranged = None

            # update inventory
            self.inventory = []
            for key in player["inventory"].keys():
                self.inventory.append(util.dict_to_proper_item_type(player["inventory"][key]))

            # update experience
            try:
                self.exp = player["exp"]
            except KeyError:
                self.exp = 0

            # update gear
            try:
                self.gear_a = player["gear_a"]
            except KeyError:
                self.gear_a = None
            else:
                if self.gear_a == NoneDict:
                    self.gear_a = None

            try:
                self.gear_b = player["gear_b"]
            except KeyError:
                self.gear_b = None
            else:
                if self.gear_b == NoneDict:
                    self.gear_b = None

            # update armor
            try:
                self.armor_a = player["armor_a"]
            except KeyError:
                self.armor_a = None
            else:
                if self.armor_a == NoneDict:
                    self.armor_a = None

            try:
                self.armor_b = player["armor_b"]
            except KeyError:
                self.armor_b = None
            else:
                if self.armor_b == NoneDict:
                    self.armor_b = None

        elif isinstance(player, str):
            self.id = player
            self.level = 1
            self.health = Player.max_health[self.level]
            self.money = 0
            self.weapon_melee = Knife()
            self.weapon_ranged = None
            self.inventory = []
            self.exp = 0
            self.gear_a = None
            self.gear_b = None
            self.armor_a = None
            self.armor_b = None
            # TODO: add an instance variable for the time they're able to fight next

            util.new_save_file(player, self.make_data_dict())
            print(f"Making a new file for {player}")

    def make_data_dict(self) -> dict:
        inventory_dict = {}
        for i in range(len(self.inventory)):
            item = self.inventory[i]
            inventory_dict[str(i) + item.name] = item.make_data_dict()
        data = {}
        data["id"] = self.id
        data["level"] = self.level
        data["health"] = self.health
        data["money"] = self.money

        if self.weapon_melee is None:
            data["weapon_melee"] = NoneDict
        else:
            data["weapon_melee"] = self.weapon_melee.make_data_dict()

        if self.weapon_ranged is None:
            data["weapon_ranged"] = NoneDict
        else:
            data["weapon_ranged"] = self.weapon_ranged.make_data_dict()

        data["inventory"] = inventory_dict
        data["exp"] = self.exp

        if self.gear_a is None:
            data["gear_a"] = NoneDict
        else:
            data["gear_a"] = self.gear_a.make_data_dict()

        if self.gear_b is None:
            data["gear_b"] = NoneDict
        else:
            data["gear_b"] = self.gear_b.make_data_dict()

        if self.armor_a is None:
            data["armor_a"] = NoneDict
        else:
            data["armor_a"] = self.armor_a.make_data_dict()

        if self.armor_b is None:
            data["armor_b"] = NoneDict
        else:
            data["armor_b"] = self.armor_b.make_data_dict()

        return data

    def profile(self, bot):
        # TODO: change this so that it uses standard string table formatting
        ammo_amt = 0
        ammo_type = None
        if self.weapon_ranged is not None:
            ammo_type = self.weapon_ranged.ammo_type
            for inv_item in self.inventory:
                if isinstance(inv_item, ammo_type):
                    ammo_amt += 1

        output = f"__**{self.id}'s profile**__\n" \
                 f"`Level            `{util.emoji('level')} {self.level}\n" \
                 f"`Experience       `{util.emoji('exp')} {self.exp}/{Player.max_exp[self.level]}\n" \
                 f"`Health           `{util.emoji('health')} {self.health}/{Player.max_health[self.level]}\n" \
                 f"`Money            `{util.emoji('money')} ${self.money}\n" \
                 f"`Equipped (melee) `{util.emoji('melee')} {self.weapon_melee}\n" \
                 f"`Equipped (range) `{util.emoji('range')} {self.weapon_ranged}"

        if ammo_type is not None:
            output += f"({bot.get_emoji(ammo_type.emoji_id)}{ammo_amt})"
        output += "\n"

        output +=f"`Gear A           `{util.emoji('gear')} {self.gear_a}\n" \
                 f"`Gear B           `{util.emoji('gear')} {self.gear_b}\n" \
                 f"`Armor A          `{util.emoji('armor')} {self.armor_a}\n" \
                 f"`Armor B          `{util.emoji('armor')} {self.armor_b}\n"
        return output

    def earn_exp(self, exp_earned: int) -> Tuple[bool, int]:
        level_up = False
        self.exp += exp_earned
        if self.exp >= Player.max_exp[self.level]:
            self.exp -= Player.max_exp[self.level]
            self.level += 1
            level_up = True
        return level_up, exp_earned

    def save(self):
        util.save_progress(self.id, self.make_data_dict())

    def inter_range_size(self) -> int:
        inter_range_size = None

        if self.weapon_melee is not None and self.weapon_ranged is not None:
            inter_range_size = max(self.weapon_ranged.range_size(), self.weapon_melee.range_size()) \
                               - min(self.weapon_ranged.range_size(), self.weapon_melee.range_size())
        elif self.weapon_ranged is not None:
            inter_range_size = self.weapon_ranged.range_size()
        elif self.weapon_melee is not None:
            inter_range_size = SniperRifle.range_max - self.weapon_melee.range_max

        irs = max(0, inter_range_size)
        print(f"inter_range_size = {irs}")
        return irs

    def armor_total(self) -> int:
        armor_total = 0
        if self.armor_a is not None:
            armor_total += self.armor_a.protection
        if self.armor_b is not None:
            armor_total += self.armor_b.protection
        return armor_total

    def fight(self):

        # TODO: add code to earn experience when fighting zombies (probably num. kills/2)

        level_up = False

        if self.weapon_melee is not None or self.weapon_ranged is not None:

            # TODO: make them wait one minute before fighting again

            ''' HEALTH / ARMOR '''

            # health
            irs = self.inter_range_size()
            health_difference = -self.armor_total()
            if self.weapon_melee is not None and self.weapon_ranged is not None:
                health_difference += irs + random.randrange(0, self.inter_range_size())
            else:
                health_difference += irs//8

            # lose health
            self.health -= health_difference

            # degrade armor durability
            if self.armor_a is not None:
                self.armor_a.durability -= 1
            if self.armor_b is not None:
                self.armor_b.durability -= 1

            ''' KILLS / PROFIT '''

            # kills
            zombies_killed = random.randrange(0, 5)
            melee_weapon_broke = False
            melee_weapon_name = ""
            ranged_weapon_broke = False
            ranged_weapon_name = ""
            if self.weapon_melee is not None:
                zombies_killed += self.weapon_melee.range_size()
                self.weapon_melee.durability -= 1
                if self.weapon_melee.durability <= 0:
                    melee_weapon_name = self.weapon_melee.name
                    self.weapon_melee = None
                    melee_weapon_broke = True
            if self.weapon_ranged is not None:
                zombies_killed += self.weapon_ranged.range_size()
                self.weapon_ranged.durability -= 1
                if self.weapon_ranged.durability <= 0:
                    ranged_weapon_name = self.weapon_ranged.name
                    self.weapon_ranged = None
                    ranged_weapon_broke = True

            # calculate bonus additive
            total_bonus_additive = health_difference * 4
            if self.weapon_melee is not None:
                total_bonus_additive += self.weapon_melee.bonus_additive
            if self.weapon_ranged is not None:
                total_bonus_additive += self.weapon_ranged.bonus_additive

            level_up, exp_earned = self.earn_exp(zombies_killed * 3)

            # bonus additive is doubled when both melee and ranged weapons are equipped
            if self.weapon_melee is not None and self.weapon_ranged is not None:
                total_bonus_additive *= 2
            money_gained = zombies_killed + random.randrange(0, total_bonus_additive + 1)

            # calculate total profit multiplier from gear
            profit_multiplier = 1.0
            if isinstance(self.gear_a, ProfitBuff):
                profit_multiplier += self.gear_a.profit_multiplier
            if isinstance(self.gear_b, ProfitBuff):
                profit_multiplier += self.gear_b.profit_multiplier

            # earn profit from kills
            old_money = self.money
            self.money += money_gained

            output = f"__**Fighting Zombies**__\n" \
                     f"You lost {health_difference} health fighting zombies...\n" \
                     f"Your health is now {util.emoji('health')}{self.health}/{Player.max_health[self.level]}\n" \
                     f"You killed {zombies_killed} zombies!\n" \
                     f"On the bright side, you earned {util.emoji('money')} ${money_gained} from it! ({util.emoji('money')}{old_money} --> {util.emoji('money')}{self.money})\n" \
                     f"You earned {util.emoji('exp')}{exp_earned} EXP from fighting"

            if level_up:
                output += f" and leveled up! You are now level {self.level}"
            output += ".\n"

            if melee_weapon_broke:
                output += f"Your {melee_weapon_name} broke!\n"
            if ranged_weapon_broke:
                output += f"Your {ranged_weapon_name} broke!\n"

        else:
            output = "You cannot fight without weapons equipped!"

        return output, level_up

    def store_in_inventory(self, _item: Item) -> bool:
        if isinstance(_item, Item) and len(self.inventory) < Player.max_inventory:
            self.inventory.append(_item)
            return True
        else:
            return False

    def remove_from_inventory(self, _item: Item):
        for inv_item in self.inventory:
            if _item is inv_item:
                self.inventory.remove(inv_item)
                break

    def list_items_in_inventory(self, grouped: bool = False) -> str:
        inv_str = ""
        if not grouped:
            headers = ["Item", "Durability", "Uses Remaining"]
            row_header_format = "{:^15}   " * len(headers)
            row_header_format = row_header_format.strip()
            row_format = "{:<15} | {:>15} | {:>15}"

            inv_str += "`" + row_header_format.format(*headers) + "`\n"

            for item in self.inventory:
                if isinstance(item, Weapon):
                    durability = item.durability
                    uses_remaining = "--"
                elif isinstance(item, Consumable):
                    durability = "--"
                    uses_remaining = item.uses_remaining
                else:
                    durability = "--"
                    uses_remaining = "--"
                inv_str += "`" + row_format.format(item.name, durability, uses_remaining) + "`\n"
        else:
            headers = ["Item", "Amount"]
            row_header_format = "{:^15}" * len(headers)
            row_format = "{:<15}{:>15}"

            inv_str += "`" + row_header_format.format(*headers) + "`\n"

            inv_dict = {}

            for item in self.inventory:
                if item.name not in inv_dict.keys():
                    inv_dict[item.name] = 1
                else:
                    inv_dict[item.name] += 1

            for item_name in inv_dict.keys():
                inv_str += "`" + row_format.format(item_name, inv_dict[item_name]) + "`\n"

        return inv_str


class TmpPlayer(Player):

    def __init__(self, player: str):
        self.id = player
        self.level = 1
        self.health = Player.max_health[self.level]
        self.money = 0
        self.weapon_melee = Knife()
        self.weapon_ranged = Bow()
        self.inventory = []
