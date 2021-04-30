import items


class GameState:

    def __init__(self):
        self.profiles = {}
        self.base = Base()
        self.storage = Storage()

    def load_guild_state(self, _guild_id):
        pass

    def load_existing(self, _path):
        pass


class Player:
    starting_health = 5

    def __init__(self):
        self.health = 5
        self.armor = 0
        self.weapon = None
        self.ammo = None


class Base:
    upgrades = [
        None,
        {
            "mhealth": 100,
            "mdefense": 25,
            "mupgrade": 1000
        },
        {
            "mhealth": 250,
            "mdefense": 50,
            "mupgrade": 10000
        },
        {
            "mhealth": 500,
            "mdefense": 100,
            "mupgrade": 1000000
        },
        {
            "mhealth": 1000,
            "mdefense": 150,
            "mupgrade": None
        }
    ]

    def __init__(self, _level=1):
        self.level = _level

        self.max_health = Base.upgrades[self.level]["mhealth"]
        self.cur_health = self.max_health

        self.max_defense = Base.upgrades[self.level]["mdefense"]
        self.cur_defense = self.max_defense

        self.upgrade_cost = Base.upgrades[self.level]["mupgrade"]
        self.upgrade_pot = 0

    def upgrade(self):
        if self.upgrade_pot > self.upgrade_cost:
            self.level += 1

            self.max_health = Base.upgrades[self.level]["mhealth"]
            self.cur_health = self.max_health

            self.max_defense = Base.upgrades[self.level]["mdefense"]
            self.cur_defense = self.max_defense

            self.upgrade_cost = Base.upgrades[self.level]["mupgrade"]
            self.upgrade_pot -= self.upgrade_cost


class Storage:

    def __init__(self):
        self.guns = GunStorage(2)
        self.bullets = BulletStorage(100)
        self.bows = BowStorage(3)
        self.arrows = ArrowStorage(15)
        self.medkits = MedkitStorage(10)

    def store(self, _item):
        if isinstance(_item, items.Gun):
            self.guns.store(_item)
        elif isinstance(_item, items.Bullet):
            self.bullets.store(_item)
        elif isinstance(_item, items.Bow):
            self.bows.store(_item)
        elif isinstance(_item, items.Arrow):
            self.arrows.store(_item)
        elif isinstance(_item, items.Medkit):
            self.medkits.store(_item)
        else:
            # _item is of invalid type
            pass

        pass


class StorageUnit:

    def __init__(self, _capacity):
        self.capacity = _capacity
        self.items = []


class GunStorage(StorageUnit):

    def store(self, _item):
        if isinstance(_item, items.Gun) and len(self.items) < self.capacity:
            self.items.append(_item)
        elif not isinstance(_item, items.Gun):
            # item is not a gun
            pass
        elif len(self.items) >= self.capacity:
            # storage unit is full
            pass


class BulletStorage(StorageUnit):

    def store(self, _item):
        if isinstance(_item, items.Bullet) and len(self.items) < self.capacity:
            self.items.append(_item)
        elif not isinstance(_item, items.Gun):
            # item is not a Bullet
            pass
        elif len(self.items) >= self.capacity:
            # storage unit is full
            pass

class BowStorage(StorageUnit):

    def store(self, _item):
        if isinstance(_item, items.Bullet) and len(self.items) < self.capacity:
            self.items.append(_item)
        elif not isinstance(_item, items.Bow):
            # item is not a Bow
            pass
        elif len(self.items) >= self.capacity:
            # storage unit is full
            pass


class ArrowStorage(StorageUnit):

    def store(self, _item):
        if isinstance(_item, items.Arrow) and len(self.items) < self.capacity:
            self.items.append(_item)
        elif not isinstance(_item, items.Arrow):
            # item is not an Arrow
            pass
        elif len(self.items) >= self.capacity:
            # storage unit is full
            pass


class MedkitStorage(StorageUnit):

    def store(self, _item):
        if isinstance(_item, items.Medkit) and len(self.items) < self.capacity:
            self.items.append(_item)
        elif not isinstance(_item, items.Medkit):
            # item is not a Medkit
            pass
        elif len(self.items) >= self.capacity:
            # storage unit is full
            pass