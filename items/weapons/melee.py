from items.weapons.categories import MeleeWeapon


class Knife(MeleeWeapon):

    name = "Knife"
    price = 5

    tags = MeleeWeapon.tags + [name.lower()]
    bonus_additive = 2

    def __init__(self, data: dict = None):
        if isinstance(data, dict) and data["name"] == "Knife":
            super().__init__(data)
        else:
            super().__init__(Knife.name, 840278732866191420, 1, 10, 1)


class Crowbar(MeleeWeapon):

    name = "Crowbar"
    price = -1

    tags = MeleeWeapon.tags + [name.lower()]
    bonus_additive = 4

    def __init__(self, data: dict = None):
        if isinstance(data, dict) and data["name"] == "Crowbar":
            super().__init__(data)
        else:
            super().__init__(Crowbar.name, 840278787068526653, 1, 10, 3)


class BaseballBat(MeleeWeapon):

    name = "Baseball Bat"
    price = -1

    tags = MeleeWeapon.tags + [name.lower()]
    bonus_additive = 6

    def __init__(self, data: dict = None):
        if isinstance(data, dict) and data["name"] == "Baseball Bat":
            super().__init__(data)
        else:
            super().__init__(BaseballBat.name, 840278679791206401, 1, 10, 5)


class RoadSign(MeleeWeapon):

    name = "Road Sign"
    price = -1

    tags = MeleeWeapon.tags = [name.lower()]
    bonus_additive = 8

    def __init__(self, data: dict = None):
        if isinstance(data, dict) and data["name"] == "Road Sign":
            super().__init__(data)
        else:
            super().__init__(RoadSign.name, 840278833353850891, 1, 10, 7)
