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


"""
Below are the weapons that can be bought at the shop. They include...
- Knife
- Sword
- Bow
    - Arrow
- Pistol
    - Bullet
- Shotgun
    - Shell
- Flamethrower
"""


class Knife(MeleeWeapon):

    def __init__(self):
        """
        Damage: random [1, 3]
        Durability: random [20, 40]
        Name: "Knife"
        Range: 1
        """
        super().__init__(random.randrange(1, 4), random.randrange(20, 41), "Knife", 1)


class Sword(MeleeWeapon):

    def __init__(self):
        """
        Damage: random [3, 5]
        Durability: random [40, 60]
        Name: "Sword"
        Range: 3
        """
        super().__init__(random.randrange(3, 6), random.randrange(40, 61), "Sword", 3)


class Bow(RangedWeapon):

    def __init__(self):
        """
        Damage: random [10, 15]
        Durability: random [60, 80]
        Name: "Bow"
        Range (minimum): 5
        Range (maximum): 25
        Ammo capacity: 1 (this can be increased to 10 when wearing a quiver)
        Ammo type: Arrow
        """
        super().__init__(random.randrange(10, 16), random.randrange(60, 81), "Bow", 5, 25, 1, Arrow)


class Arrow(Ammo):

    def __init__(self):
        super().__init__()


class Pistol(Gun):

    def __init__(self):
        """
        Damage: random [18, 20]
        Durability: random [80, 100]
        Name: "Pistol"
        Range (minimum): 5
        Range (maximum): 20
        Ammo capacity: 8 (this can be increased to 50 when wearing an ammo backpack)
        Ammo type: Bullet
        """
        super().__init__(random.randrange(18, 21), random.randrange(80, 101), "Pistol", 5, 20, 8, Bullet)


class Bullet(Ammo):

    def __init__(self):
        super().__init__()


class Shotgun(Gun):

    def __init__(self):
        """
        Damage: random [40, 50]
        Durability: random [80, 100]
        Name: "Shotgun"
        Range (minimum): 4
        Range (maximum): 10
        Ammo capacity: 2 (this can be increased to 50 when wearing an ammo backpack)
        Ammo type: Shell
        """
        super().__init__(random.randrange(40, 51), random.randrange(80, 101), "Shotgun", 4, 10, 2, Shell)


class Shell(Ammo):

    def __init__(self):
        super().__init__()


class Flamethrower(MeleeWeapon):

    def __init__(self):
        super().__init__(random.randrange(100, 151), random.randrange(80, 101), "Flamethrower", 5)


class Medkit(Healer):

    def __init__(self):
        pass
