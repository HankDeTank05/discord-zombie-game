from typing import Union, Type

from items.tagging import Tags
from items.weapon import Weapon
from items.weapons.ammo import Arrow, Shell, Bullet, RifleBullet, Ammo


class RangedWeapon(Weapon):
    tags = Weapon.tags + [Tags.ranged_weapon]

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


''' SUBCLASSES '''


class Bow(RangedWeapon):

    name = "Bow"
    emoji_id = 839627772858990632
    price = 250
    base_durability = 50
    range_min = 5
    range_max = 10
    ammo_type = Arrow

    tags = RangedWeapon.tags + ["archery", name.lower()]
    bonus_additive = 3

    def __init__(self, data: dict = None):
        if isinstance(data, dict) and data["name"] == Bow.name:
            super().__init__(data)
        else:
            super().__init__(Bow.name,
                             Bow.emoji_id,
                             Bow.base_durability,
                             Bow.range_min,
                             Bow.range_max,
                             Bow.ammo_type)


class Crossbow(RangedWeapon):

    name = "Crossbow"
    emoji_id = 839627864123113532
    price = 500
    base_durability = 100
    range_min = 5
    range_max = 15
    ammo_type = Arrow

    tags = RangedWeapon.tags + ["archery", name.lower()]
    bonus_additive = 5

    def __init__(self, data: dict = None):
        if isinstance(data, dict) and data["name"] == Crossbow.name:
            super().__init__(data)
        else:
            super().__init__(Crossbow.name,
                             Crossbow.emoji_id,
                             Crossbow.base_durability,
                             Crossbow.range_min,
                             Crossbow.range_max,
                             Crossbow.ammo_type)


class Shotgun(RangedWeapon):

    name = "Shotgun"
    emoji_id = 839628122935918592
    price = 2000
    base_durability = 250
    range_min = 5
    range_max = 15
    ammo_type = Shell

    tags = RangedWeapon.tags + ["mid-range", name.lower()]
    bonus_additive = 7

    def __init__(self, data: dict = None):
        if isinstance(data, dict) and data["name"] == Shotgun.name:
            super().__init__(data)
        else:
            super().__init__(Shotgun.name,
                             Shotgun.emoji_id,
                             Shotgun.base_durability,
                             Shotgun.range_min,
                             Shotgun.range_max,
                             Shotgun.ammo_type)


class Pistol(RangedWeapon):

    name = "Pistol"
    emoji_id = 839627965049995284
    price = 5000
    base_durability = 250
    range_min = 7
    range_max = 20
    ammo_type = Bullet

    tags = RangedWeapon.tags + ["mid-range" + name.lower()]
    bonus_additive = 9

    def __init__(self, data: dict = None):
        if isinstance(data, dict) and data["name"] == Pistol.name:
            super().__init__(data)
        else:
            super().__init__(Pistol.name,
                             Pistol.emoji_id,
                             Pistol.base_durability,
                             Pistol.range_min,
                             Pistol.range_max,
                             Pistol.ammo_type)


class HuntingRifle(RangedWeapon):

    name = "Hunting Rifle"
    emoji_id = 839627913023324221
    price = 20000
    base_durability = 300
    range_min = 10
    range_max = 30
    ammo_type = RifleBullet

    tags = RangedWeapon.tags + ["long-range", "rifle", name.lower()]
    bonus_additive = 11

    def __init__(self, data: dict = None):
        if isinstance(data, dict) and data["name"] == HuntingRifle.name:
            super().__init__(data)
        else:
            super().__init__(HuntingRifle.name,
                             HuntingRifle.emoji_id,
                             HuntingRifle.base_durability,
                             HuntingRifle.range_min,
                             HuntingRifle.range_max,
                             HuntingRifle.ammo_type)


class SniperRifle(RangedWeapon):

    name = "Sniper Rifle"
    emoji_id = 839628168503885844
    price = 50000
    base_durability = 300
    range_min = 15
    range_max = 45
    ammo_type = RifleBullet

    tags = RangedWeapon.tags + ["long-range", "rifle", name.lower()]
    bonus_additive = 13

    def __init__(self, data: dict = None):
        if isinstance(data, dict) and data["name"] == SniperRifle.name:
            super().__init__(data)
        else:
            super().__init__(SniperRifle.name,
                             SniperRifle.emoji_id,
                             SniperRifle.base_durability,
                             SniperRifle.range_min,
                             SniperRifle.range_max,
                             SniperRifle.ammo_type)
