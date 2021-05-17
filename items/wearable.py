from items.item import Item


class Wearable(Item):

    tags = Item.tags + ["wearables", "wearable", "equippable"]

    def __init__(self, name: str, emoji_id: int):
        super().__init__(name, emoji_id)
