from items.weapons.categories import RangedWeapon
from items.weapons.ammo import Arrow, Shell, Bullet, RifleBullet


class Bow(RangedWeapon):

    tags = RangedWeapon.tags + ["archery"]
    bonus_additive = 3

    def __init__(self, data: dict = None):
        if isinstance(data, dict) and data["name"] == "Bow":
            super().__init__(data)
        else:
            super().__init__("Bow", 839627772858990632, 10, 5, 10, Arrow)


class Crossbow(RangedWeapon):

    tags = RangedWeapon.tags + ["archery"]
    bonus_additive = 5

    def __init__(self, data: dict = None):
        if isinstance(data, dict) and data["name"] == "Crossbow":
            super().__init__(data)
        else:
            super().__init__("Crossbow", 839627864123113532, 10, 5, 15, Arrow)


class Shotgun(RangedWeapon):

    tags = RangedWeapon.tags + ["mid-range"]
    bonus_additive = 7

    def __init__(self, data: dict = None):
        if isinstance(data, dict) and data["name"] == "Shotgun":
            super().__init__(data)
        else:
            super().__init__("Shotgun", 839628122935918592, 10, 5, 15, Shell)


class Pistol(RangedWeapon):

    tags = RangedWeapon.tags + ["mid-range"]
    bonus_additive = 9

    def __init__(self, data: dict = None):
        if isinstance(data, dict) and data["name"] == "Pistol":
            super().__init__(data)
        else:
            super().__init__("Pistol", 839627965049995284, 10, 7, 20, Bullet)


class HuntingRifle(RangedWeapon):

    tags = RangedWeapon.tags + ["long-range", "rifle"]
    bonus_additive = 11

    def __init__(self, data: dict = None):
        if isinstance(data, dict) and data["name"] == "Hunting Rifle":
            super().__init__(data)
        else:
            super().__init__("Hunting Rifle", 839627913023324221, 10, 10, 30, RifleBullet)


class SniperRifle(RangedWeapon):

    tags = RangedWeapon.tags + ["long-range", "rifle"]
    bonus_additive = 13

    def __init__(self, data: dict = None):
        if isinstance(data, dict) and data["name"] == "Sniper Rifle":
            super().__init__(data)
        else:
            super().__init__("Sniper Rifle", 839628168503885844, 10, 15, 45, RifleBullet)
