class Weapon:
    def __init__(self, _damage_out, _durability):
        self.damage_out = _damage_out
        self.durability = _durability

    def repair(self):
        pass


class RangedWeapon(Weapon):
    def __init__(self, _damage_out, _durability, _range_min, _range_max, _ammo_capacity, _ammo_type):
        super.__init__(_damage_out, _durability)
        self.range_min = _range_min
        self.range_max = _range_max
        self.ammo_cap = _ammo_capacity

    def reload(self):
        pass


class MeleeWeapon(Weapon):
    def __init__(self, _damage_out, _durability, _range_max):
        super.__init__(_damage_out, _durability)
        self.range_max = _range_max


class Ammo:
    def __init__(self):
        pass


class Healer:
    def __init__(self, _heal_amount):
        self.heal_amt = _heal_amount


class Gun(RangedWeapon):
    def __init__(self, _damage_out, _durability, _range_min, _range_max, _ammo_capacity, _ammo_type):
        pass

class Bullet:
    def __init__(self):
        pass


class Bow:
    def __init__(self):
        pass


class Arrow:
    def __init__(self):
        pass


class Medkit:
    def __init__(self):
        pass