from weaponTypes import Ammo, RangedWeapon


class Arrow(Ammo):

    def __init__(self):
        super().__init__("Arrow", ":arrow_right:", 1)


class Bow(RangedWeapon):

    def __init__(self):
        super().__init__("Bow", ":bow_and_arrow:", 10, 5, 10, Arrow)


class Crossbow(RangedWeapon):

    def __init__(self):
        super().__init__("Crossbow", ":question:", 10, 5, 15, Arrow)


class Shell(Ammo):

    def __init__(self):
        super().__init__("Shotgun Shell", ":question:", 1)


class Shotgun(RangedWeapon):

    def __init__(self):
        super().__init__("Shotgun", ":question:", 10, 5, 15, Shell)


class Bullet(Ammo):

    def __init__(self):
        super().__init__("Bullet", ":question:", 1)


class Pistol(RangedWeapon):

    def __init__(self):
        super().__init__("Pistol", ":question:", 10, 7, 20, Bullet)


class RifleBullet(Ammo):

    def __init__(self):
        super().__init__("Rifle Bullet", ":question:", 1)


class HuntingRifle(RangedWeapon):

    def __init__(self):
        super().__init__("Hunting Rifle", ":question:", 10, 10, 30, RifleBullet)


class SniperRifle(RangedWeapon):

    def __init__(self):
        super().__init__("Sniper Rifle", ":question:", 10, 15, 45, RifleBullet)
