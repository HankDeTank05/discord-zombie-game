from items.item import Item


class Consumable(Item):

    tags = Item.tags + ["consumable"]

    def __init__(self, name: str, emoji_id: int, uses: int):
        super().__init__(name, emoji_id)
        self.uses_remaining = uses

    def use(self):
        pass
