from typing import Union

from items.tagging import Tags
from items.weapon import Weapon


class MeleeWeapon(Weapon):
    tags = Weapon.tags + [Tags.melee_weapon]

    def __init__(self, name: Union[str, dict],
                 emoji_id: int = None,
                 damage_out: int = None,
                 durability: int = None,
                 range_max: int = None):
        if isinstance(name, str) \
                and emoji_id is not None \
                and damage_out is not None \
                and durability is not None \
                and range_max is not None:
            super().__init__(name, emoji_id, damage_out, durability)
            self.range_max = range_max
        elif isinstance(name, dict):
            super().__init__(name["name"], name["icon"], name["damage_out"], name["durability"])
            self.range_max = name["range_max"]

    def make_data_dict(self) -> dict:
        data = {
            "item_type": "melee",
            "name": self.name,
            "icon": self.icon,
            "damage_out": self.damage_out,
            "durability": self.durability,
            "range_max": self.range_max
        }
        return data

    def range_size(self) -> int:
        return self.range_max


''' SUBCLASSES '''


class Knife(MeleeWeapon):

    name = "Knife"
    emoji_id = 840278732866191420
    price = 150
    damage_out = 1
    base_durability = 50
    range_max = 1

    tags = MeleeWeapon.tags + [name.lower()]
    bonus_additive = 2

    def __init__(self, data: dict = None):
        if isinstance(data, dict) and data["name"] == Knife.name:
            super().__init__(data)
        else:
            super().__init__(Knife.name, Knife.emoji_id, Knife.damage_out, Knife.base_durability, Knife.range_max)


class Crowbar(MeleeWeapon):

    name = "Crowbar"
    emoji_id = 840278787068526653
    price = 300
    damage_out = 1
    base_durability = 100
    range_max = 3

    tags = MeleeWeapon.tags + [name.lower()]
    bonus_additive = 4

    def __init__(self, data: dict = None):
        if isinstance(data, dict) and data["name"] == Crowbar.name:
            super().__init__(data)
        else:
            super().__init__(Crowbar.name, Crowbar.emoji_id, Crowbar.damage_out, Crowbar.base_durability, Crowbar.range_max)


class BaseballBat(MeleeWeapon):

    name = "Baseball Bat"
    emoji_id = 840278679791206401
    price = 900
    damage_out = 1
    base_durability = 75
    range_max = 5

    tags = MeleeWeapon.tags + [name.lower()]
    bonus_additive = 6

    def __init__(self, data: dict = None):
        if isinstance(data, dict) and data["name"] == BaseballBat.name:
            super().__init__(data)
        else:
            super().__init__(BaseballBat.name, BaseballBat.emoji_id, BaseballBat.damage_out, BaseballBat.base_durability, BaseballBat.range_max)


class RoadSign(MeleeWeapon):

    name = "Road Sign"
    emoji_id = 840278833353850891
    price = 1200
    damage_out = 1
    base_durability = 175
    range_max = 7

    tags = MeleeWeapon.tags = [name.lower()]
    bonus_additive = 8

    def __init__(self, data: dict = None):
        if isinstance(data, dict) and data["name"] == RoadSign.name:
            super().__init__(data)
        else:
            super().__init__(RoadSign.name, RoadSign.emoji_id, RoadSign.damage_out, RoadSign.base_durability, RoadSign.range_max)
