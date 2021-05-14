from items.weapons.categories import RangedWeapon
from items.weapons.ammo import Arrow, Shell, Bullet, RifleBullet


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
        if isinstance(data, dict) and data["name"] == "Bow":
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
    price = -1
    base_durability = 10
    range_min = 5
    range_max = 15
    ammo_type = Arrow

    tags = RangedWeapon.tags + ["archery", name.lower()]
    bonus_additive = 5

    def __init__(self, data: dict = None):
        if isinstance(data, dict) and data["name"] == "Crossbow":
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
    price = -1
    base_durability = 10
    range_min = 5
    range_max = 15
    ammo_type = Shell

    tags = RangedWeapon.tags + ["mid-range", name.lower()]
    bonus_additive = 7

    def __init__(self, data: dict = None):
        if isinstance(data, dict) and data["name"] == "Shotgun":
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
    price = -1
    base_durability = 10
    range_min = 7
    range_max = 20
    ammo_type = Bullet

    tags = RangedWeapon.tags + ["mid-range" + name.lower()]
    bonus_additive = 9

    def __init__(self, data: dict = None):
        if isinstance(data, dict) and data["name"] == "Pistol":
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
    price = -1
    base_durability = 10
    range_min = 10
    range_max = 30
    ammo_type = RifleBullet

    tags = RangedWeapon.tags + ["long-range", "rifle", name.lower()]
    bonus_additive = 11

    def __init__(self, data: dict = None):
        if isinstance(data, dict) and data["name"] == "Hunting Rifle":
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
    price = -1
    base_durability = 10
    range_min = 15
    range_max = 45
    ammo_type = RifleBullet

    tags = RangedWeapon.tags + ["long-range", "rifle", name.lower()]
    bonus_additive = 13

    def __init__(self, data: dict = None):
        if isinstance(data, dict) and data["name"] == "Sniper Rifle":
            super().__init__(data)
        else:
            super().__init__(SniperRifle.name,
                             SniperRifle.emoji_id,
                             SniperRifle.base_durability,
                             SniperRifle.range_min,
                             SniperRifle.range_max,
                             SniperRifle.ammo_type)
