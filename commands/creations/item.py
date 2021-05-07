from commands.creation import ItemCreationCmd
from items.weapons.ammo import Arrow, Shell, Bullet, RifleBullet
from items.weapons.categories import RangedWeapon, MeleeWeapon, Ammo
from items.weapons.melee import Knife, Crowbar, BaseballBat, RoadSign
from items.weapons.ranged import Bow, Crossbow, Shotgun, Pistol, HuntingRifle, SniperRifle

""" Ranged weapon creations """


class CreateBowCmd(ItemCreationCmd):

    def __init__(self):
        super().__init__(Bow)

    @staticmethod
    def execute(data: dict) -> Bow:
        return Bow(data)


class CreateCrossbowCmd(ItemCreationCmd):

    def __init__(self):
        super().__init__(Crossbow)

    @staticmethod
    def execute(data: dict) -> Crossbow:
        return Crossbow(data)


class CreateShotgunCmd(ItemCreationCmd):

    def __init__(self):
        super().__init__(Shotgun)

    @staticmethod
    def execute(data: dict) -> Shotgun:
        return Shotgun(data)


class CreatePistolCmd(ItemCreationCmd):

    def __init__(self):
        super().__init__(Pistol)

    @staticmethod
    def execute(data: dict) -> Pistol:
        return Pistol(data)


class CreateHuntingRifleCmd(ItemCreationCmd):

    def __init__(self):
        super().__init__(HuntingRifle)

    @staticmethod
    def execute(data: dict) -> HuntingRifle:
        return HuntingRifle(data)


class CreateSniperRifleCmd(ItemCreationCmd):

    def __init__(self):
        super().__init__(SniperRifle)

    @staticmethod
    def execute(data: dict) -> SniperRifle:
        return SniperRifle(data)


""" Melee Weapon Creation Commands """


class CreateKnifeCmd(ItemCreationCmd):

    def __init__(self):
        super().__init__(Knife)

    @staticmethod
    def execute(data: dict) -> Knife:
        return Knife(data)


class CreateCrowbarCmd(ItemCreationCmd):

    def __init__(self):
        super().__init__(Crowbar)

    @staticmethod
    def execute(data: dict) -> Crowbar:
        return Crowbar(data)


class CreateBaseballBatCmd(ItemCreationCmd):

    def __init__(self):
        super().__init__(BaseballBat)

    @staticmethod
    def execute(data: dict) -> BaseballBat:
        return BaseballBat(data)


class CreateRoadSignCmd(ItemCreationCmd):

    def __init__(self):
        super().__init__(RoadSign)

    @staticmethod
    def execute(data: dict) -> RoadSign:
        return RoadSign(data)


""" Ammo Creation Commands """


class CreateArrowCmd(ItemCreationCmd):

    def __init__(self):
        super().__init__(Arrow)

    @staticmethod
    def execute() -> Arrow:
        return Arrow()


class CreateShellCmd(ItemCreationCmd):

    def __init__(self):
        super().__init__(Shell)

    @staticmethod
    def execute() -> Shell:
        return Shell()


class CreateBullet(ItemCreationCmd):

    def __init__(self):
        super().__init__(Bullet)

    @staticmethod
    def execute() -> Bullet:
        return Bullet()


class CreateRifleBullet(ItemCreationCmd):

    def __init__(self):
        super().__init__(RifleBullet)

    @staticmethod
    def execute() -> RifleBullet:
        return RifleBullet()
