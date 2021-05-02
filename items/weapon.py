from items import item


class Weapon(item.Item):

    def __init__(self, name: str, emoji: str, damage_out: int, durability: int):
        super().__init__(name, emoji)
        self.damage_out = damage_out
        self.durability = durability
