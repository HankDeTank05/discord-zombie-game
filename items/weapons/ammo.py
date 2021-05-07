from items.weapons.categories import Ammo


class Arrow(Ammo):

    tags = Ammo.tags + ["archery"]

    def __init__(self):
        super().__init__("Arrow", 839627706378879016, 1)


class Shell(Ammo):

    tags = Ammo.tags + ["mid-range"]

    def __init__(self):
        super().__init__("Shotgun Shell", 839628068448501781, 1)


class Bullet(Ammo):

    tags = Ammo.tags + ["mid-range"]

    def __init__(self):
        super().__init__("Bullet", 839627813254070322, 1)


class RifleBullet(Ammo):

    tags = Ammo.tags + ["long-range", "rifle"]

    def __init__(self):
        super().__init__("Rifle Bullet", 839628016929472552, 1)
