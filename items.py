import random


class Item:

    def __init__(self):
        self.icon = ""


class Weapon(Item):

    def __init__(self, _damage_out, _durability, _name):
        super().__init__()
        self.damage_out = _damage_out
        self.durability = _durability
        self.name = _name

    def repair(self):
        pass


class RangedWeapon(Weapon):

    def __init__(self, _damage_out, _durability, _name, _range_min, _range_max, _ammo_capacity, _ammo_type):
        super().__init__(_damage_out, _durability, _name)
        self.range_min = _range_min
        self.range_max = _range_max
        self.ammo_cap = _ammo_capacity

    def reload(self):
        pass


class MeleeWeapon(Weapon):

    def __init__(self, _damage_out, _durability, _name, _range_max):
        super().__init__(_damage_out, _durability, _name)
        self.range_max = _range_max


class Ammo(Item):

    def __init__(self):
        super().__init__()


class Healer(Item):

    def __init__(self, _heal_amount):
        super().__init__()
        self.heal_amt = _heal_amount


class Gun(RangedWeapon):

    def __init__(self, _damage_out, _durability, _name, _range_min, _range_max, _ammo_capacity, _ammo_type):
        super().__init__(_damage_out, _durability, _name, _range_min, _range_max, _ammo_capacity, _ammo_type)
        pass


class Bullet(Ammo):

    def __init__(self):
        pass


class Bow(RangedWeapon):

    def __init__(self):
        pass


class Arrow(Ammo):

    def __init__(self):
        pass


class Knife(MeleeWeapon):

    def __init__(self):
        """
        Damage: random [1,3]
        Durability: random [80,100]
        Name: "Knife"
        Range: 1
        """
        super().__init__(random.randrange(1, 3), random.randrange(80, 100), "Knife", 1)


class Medkit(Healer):

    def __init__(self):
        pass
