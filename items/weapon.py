import util
from items.item import Item
from items.tagging import Tags


class Weapon(Item):

    tags = Item.tags + [Tags.weapons, Tags.weapon, Tags.equippable]

    def __init__(self, name: str, emoji_id: int, damage_out: int, durability: int):
        super().__init__(name, emoji_id)
        self.damage_out = damage_out
        self.durability = durability

    def __str__(self):
        return f"{self.name} ({util.emoji('diamond')}{self.durability})"
