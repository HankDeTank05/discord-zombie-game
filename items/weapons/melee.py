from items.weapons.categories import MeleeWeapon


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
        if isinstance(data, dict) and data["name"] == "Knife":
            super().__init__(data)
        else:
            super().__init__(Knife.name, Knife.emoji_id, Knife.damage_out, Knife.base_durability, Knife.range_max)


class Crowbar(MeleeWeapon):

    name = "Crowbar"
    emoji_id = 840278787068526653
    price = -1
    damage_out = 1
    base_durability = 10
    range_max = 3

    tags = MeleeWeapon.tags + [name.lower()]
    bonus_additive = 4

    def __init__(self, data: dict = None):
        if isinstance(data, dict) and data["name"] == "Crowbar":
            super().__init__(data)
        else:
            super().__init__(Crowbar.name, Crowbar.emoji_id, Crowbar.damage_out, Crowbar.base_durability, Crowbar.range_max)


class BaseballBat(MeleeWeapon):

    name = "Baseball Bat"
    emoji_id = 840278679791206401
    price = -1
    damage_out = 1
    base_durability = 10
    range_max = 5

    tags = MeleeWeapon.tags + [name.lower()]
    bonus_additive = 6

    def __init__(self, data: dict = None):
        if isinstance(data, dict) and data["name"] == "Baseball Bat":
            super().__init__(data)
        else:
            super().__init__(BaseballBat.name, BaseballBat.emoji_id, BaseballBat.damage_out, BaseballBat.base_durability, BaseballBat.range_max)


class RoadSign(MeleeWeapon):

    name = "Road Sign"
    emoji_id = 840278833353850891
    price = -1
    damage_out = 1
    base_durability = 10
    range_max = 7

    tags = MeleeWeapon.tags = [name.lower()]
    bonus_additive = 8

    def __init__(self, data: dict = None):
        if isinstance(data, dict) and data["name"] == "Road Sign":
            super().__init__(data)
        else:
            super().__init__(RoadSign.name, RoadSign.emoji_id, RoadSign.damage_out, RoadSign.base_durability, RoadSign.range_max)
