from items.wearables.gears.buff import DamageBuff


class Bayonet(DamageBuff):

    name = "Bayonet"
    emoji_id = -1
    price = -1
    multiplier = 0.05

    tags = DamageBuff.tags + [name.lower()]

    def __init__(self):
        super().__init__(Bayonet.name, Bayonet.emoji_id, Bayonet.multiplier)


class BarbedWireWrap(DamageBuff):

    name = "Barbed Wire Wrap"
    emoji_id = -1
    price = -1
    multiplier = 0.10

    tags = DamageBuff.tags + [name.lower()]

    def __init__(self):
        super().__init__(BarbedWireWrap.name, BarbedWireWrap.emoji_id, BarbedWireWrap.multiplier)
