from items.item import Item


class Weapon(Item):

    tags = Item.tags + ["weapons"]

    def __init__(self, name: str, emoji_id: int, damage_out: int, durability: int):
        super().__init__(name, emoji_id)
        self.damage_out = damage_out
        self.durability = durability
