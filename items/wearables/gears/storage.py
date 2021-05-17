from items.item import Item
from items.tagging import Tags
from items.weapons.ammo import Arrow, Ammo
from items.wearables.gear import StorageGear


class Backpack(StorageGear):

    name = "School Backpack"
    emoji_id = -1
    price = -1
    storage_type = Item
    storage_amount = 5

    tags = StorageGear.tags + [Tags.general_storage, name.lower()]

    def __init__(self):
        super().__init__(Backpack.name, Backpack.emoji_id, Backpack.storage_type, Backpack.storage_amount)


class DuffelBag(StorageGear):

    name = "Duffel Bag"
    emoji_id = -1
    price = -1
    storage_type = Item
    storage_amount = 15

    tags = StorageGear.tags + [Tags.general_storage, name.lower()]

    def __init__(self):
        super().__init__(DuffelBag.name, DuffelBag.emoji_id, DuffelBag.storage_type, DuffelBag.storage_amount)


class Quiver(StorageGear):

    name = "Quiver"
    emoji_id = -1
    price = -1
    storage_type = Arrow
    storage_amount = 20

    tags = StorageGear.tags + [Tags.ammo_storage, name.lower()]

    def __init__(self):
        super().__init__(Quiver.name, Quiver.emoji_id, Quiver.storage_type, Quiver.storage_amount)


class AmmoBelt(StorageGear):

    name = "Ammo Belt"
    emoji_id = -1
    price = -1
    storage_type = Ammo
    storage_amount = 15

    tags = StorageGear.tags + [Tags.ammo_storage, name.lower()]

    def __init__(self):
        super().__init__(AmmoBelt.name, AmmoBelt.emoji_id, AmmoBelt.storage_type, AmmoBelt.storage_amount)


class AmmoSash(StorageGear):

    name = "Ammo Sash"
    emoji_id = -1
    price = -1
    storage_type = Ammo
    storage_amount = 45

    tags = StorageGear.tags + [Tags.ammo_storage, name.lower()]
