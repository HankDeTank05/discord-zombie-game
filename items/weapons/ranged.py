from items.weapons.categories import RangedWeapon
from items.weapons.ammo import Arrow, Shell, Bullet, RifleBullet


class Bow(RangedWeapon):

    name = "Bow"
    price = -1

    tags = RangedWeapon.tags + ["archery", name.lower()]
    bonus_additive = 3

    def __init__(self, data: dict = None):
        if isinstance(data, dict) and data["name"] == "Bow":
            super().__init__(data)
        else:
            super().__init__(Bow.name, 839627772858990632, 10, 5, 10, Arrow)


class Crossbow(RangedWeapon):

    name = "Crossbow"
    price = -1

    tags = RangedWeapon.tags + ["archery", name.lower()]
    bonus_additive = 5

    def __init__(self, data: dict = None):
        if isinstance(data, dict) and data["name"] == "Crossbow":
            super().__init__(data)
        else:
            super().__init__(Crossbow.name, 839627864123113532, 10, 5, 15, Arrow)


class Shotgun(RangedWeapon):

    name = "Shotgun"
    price = -1

    tags = RangedWeapon.tags + ["mid-range", name.lower()]
    bonus_additive = 7

    def __init__(self, data: dict = None):
        if isinstance(data, dict) and data["name"] == "Shotgun":
            super().__init__(data)
        else:
            super().__init__(Shotgun.name, 839628122935918592, 10, 5, 15, Shell)


class Pistol(RangedWeapon):

    name = "Pistol"
    price = -1

    tags = RangedWeapon.tags + ["mid-range" + name.lower()]
    bonus_additive = 9

    def __init__(self, data: dict = None):
        if isinstance(data, dict) and data["name"] == "Pistol":
            super().__init__(data)
        else:
            super().__init__(Pistol.name, 839627965049995284, 10, 7, 20, Bullet)


class HuntingRifle(RangedWeapon):

    name = "Hunting Rifle"
    price = -1

    tags = RangedWeapon.tags + ["long-range", "rifle", name.lower()]
    bonus_additive = 11

    def __init__(self, data: dict = None):
        if isinstance(data, dict) and data["name"] == "Hunting Rifle":
            super().__init__(data)
        else:
            super().__init__(HuntingRifle.name, 839627913023324221, 10, 10, 30, RifleBullet)


class SniperRifle(RangedWeapon):

    name = "Sniper Rifle"
    price = -1

    tags = RangedWeapon.tags + ["long-range", "rifle", name.lower()]
    bonus_additive = 13

    def __init__(self, data: dict = None):
        if isinstance(data, dict) and data["name"] == "Sniper Rifle":
            super().__init__(data)
        else:
            super().__init__(SniperRifle.name, 839628168503885844, 10, 15, 45, RifleBullet)
