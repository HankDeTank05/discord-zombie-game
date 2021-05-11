from typing import Type, Union

from items.weapon import Weapon


class Ammo(Weapon):
    tags = Weapon.tags + ["ammo"]

    def __init__(self, name: Union[str, dict],
                 emoji_id: int = None,
                 damage_out: int = None):
        if isinstance(name, str) \
                and emoji_id is not None \
                and damage_out is not None:
            super().__init__(name, emoji_id, damage_out, 1)
        else:
            super().__init__(name["name"], name["icon"], name["damage_out"])

    def make_data_dict(self) -> dict:
        data = {
            "item_type": "ammo",
            "name": self.name,
            "icon": self.icon,
            "damage_out": self.damage_out
        }
        return data


class MeleeWeapon(Weapon):
    tags = Weapon.tags + ["melee weapon"]

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


class RangedWeapon(Weapon):
    tags = Weapon.tags + ["ranged weapon"]

    def __init__(self, name: Union[str, dict],
                 emoji_id: int = None,
                 durability: int = None,
                 range_min: int = None,
                 range_max: int = None,
                 ammo_type: Type[Ammo] = None):
        if isinstance(name, str) \
                and emoji_id is not None \
                and durability is not None \
                and range_min is not None \
                and range_max is not None \
                and ammo_type is not None:
            super().__init__(name, emoji_id, 0, durability)
            self.range_min = range_min
            self.range_max = range_max
            self.ammo_type = ammo_type
        elif isinstance(name, dict):
            super().__init__(name["name"], name["icon"], name["damage_out"], name["durability"])
            self.range_min = name["range_min"]
            self.range_max = name["range_max"]
            self.ammo_type = name["ammo_type"]

    def make_data_dict(self) -> dict:
        data = {
            "item_type": "ranged",
            "name": self.name,
            "icon": self.icon,
            "damage_out": self.damage_out,
            "durability": self.durability,
            "range_min": self.range_min,
            "range_max": self.range_max,
            "ammo_type": self.ammo_type
        }
        return data

    def range_size(self) -> int:
        return self.range_max - self.range_min
