from items.weapons.categories import Ammo


class Arrow(Ammo):

    name = "Arrow"
    price = -1

    tags = Ammo.tags + ["archery", name.lower()]

    def __init__(self):
        super().__init__(Arrow.name, 839627706378879016, 1)


class Shell(Ammo):

    name = "Shotgun Shell"
    price = -1

    tags = Ammo.tags + ["mid-range", name.lower()]

    def __init__(self):
        super().__init__(Shell.name, 839628068448501781, 1)


class Bullet(Ammo):

    name = "Bullet"
    price = -1

    tags = Ammo.tags + ["mid-range", name.lower()]

    def __init__(self):
        super().__init__(Bullet.name, 839627813254070322, 1)


class RifleBullet(Ammo):

    name = "Rifle Bullet"
    price = -1

    tags = Ammo.tags + ["long-range", "rifle", name.lower()]

    def __init__(self):
        super().__init__(RifleBullet.name, 839628016929472552, 1)
