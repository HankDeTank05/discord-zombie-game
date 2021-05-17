from items.wearables.gears.buff import ProfitBuff


class CoinMagnet(ProfitBuff):

    name = "Coin Magnet"
    emoji_id = -1
    price = -1
    multiplier = 0.1

    tags = ProfitBuff.tags + [name.lower()]

    def __init__(self):
        super().__init__(CoinMagnet.name, CoinMagnet.emoji_id, CoinMagnet.multiplier)


class BillVacuum(ProfitBuff):

    name = "Bill Vacuum"
    emoji_id = -1
    price = -1
    multiplier = 0.3

    tags = ProfitBuff.tags + [name.lower()]

    def __init__(self):
        super().__init__(BillVacuum.name, BillVacuum.emoji_id, BillVacuum.multiplier)
