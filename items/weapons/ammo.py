from typing import Union

from items.tagging import Tags
from items.weapon import Weapon


class Ammo(Weapon):
    tags = Weapon.tags + [Tags.ammo, Tags.ammunition]

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


''' SUBCLASSES '''


class Arrow(Ammo):

    name = "Arrow"
    emoji_id = 839627706378879016
    price = 10
    damage_out = 1

    tags = Ammo.tags + ["archery", name.lower()]

    def __init__(self):
        super().__init__(Arrow.name, Arrow.emoji_id, Arrow.damage_out)


class Shell(Ammo):

    name = "Shotgun Shell"
    emoji_id = 839628068448501781
    price = -1
    damage_out = 1

    tags = Ammo.tags + ["mid-range", name.lower()]

    def __init__(self):
        super().__init__(Shell.name, Shell.emoji_id, Shell.damage_out)


class Bullet(Ammo):

    name = "Bullet"
    emoji_id = 839627813254070322
    price = -1
    damage_out = 1

    tags = Ammo.tags + ["mid-range", name.lower()]

    def __init__(self):
        super().__init__(Bullet.name, Bullet.emoji_id, Bullet.damage_out)


class RifleBullet(Ammo):

    name = "Rifle Bullet"
    emoji_id = 839628016929472552
    price = -1
    damage_out = 1

    tags = Ammo.tags + ["long-range", "rifle", name.lower()]

    def __init__(self):
        super().__init__(RifleBullet.name, RifleBullet.emoji_id, RifleBullet.damage_out)
