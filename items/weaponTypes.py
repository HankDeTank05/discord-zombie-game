from typing import Type

import weapon


class Ammo(weapon.Weapon):

    def __init__(self, name: str, emoji: str, damage_out: int):
        super().__init__(name, emoji, damage_out, 1)


class RangedWeapon(weapon.Weapon):

    def __init__(self, name: str, emoji: str, durability: int, range_min: int, range_max: int, ammo_type: Type[Ammo]):
        super().__init__(name, emoji, ammo_type.damage_out, durability)
        self.range_min = range_min
        self.range_max = range_max
        self.ammo_type = ammo_type


class MeleeWeapon(weapon.Weapon):

    def __init__(self, name: str, emoji: str, damage_out: int, durability: int, range_max: int):
        super().__init__(name, emoji, damage_out, durability)
        self.range_max = range_max
