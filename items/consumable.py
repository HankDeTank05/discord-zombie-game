from items.item import Item
from items.tagging import Tags


class Consumable(Item):

    tags = Item.tags + [Tags.consumables, Tags.consumable, Tags.usable]

    def __init__(self, name: str, emoji_id: int, uses: int):
        super().__init__(name, emoji_id)
        self.uses_remaining = uses

    def use(self):
        pass
