from items import *


class CommandObj:

    def __init__(self):
        pass

    def execute(self):
        pass


class BuyCommand(CommandObj):

    def __init__(self, _cost: int, _item: Item):
        self.cost = _cost
        self.item = _item

    def execute(self, player):
        player.money -= self.cost
        return self.item.__init__()


class BuyKnifeCmd(BuyCommand):

    def __init__(self, _cost: int):
        super().__init__(_cost, Knife)


class BuySwordCmd(BuyCommand):

    def __init__(self, _cost: int):
        super().__init__(_cost, Sword)


class BuyBowCmd(BuyCommand):

    def __init__(self, _cost: int):
        super().__init__(_cost, Bow)


class BuyArrowCmd(BuyCommand):

    def __init__(self, _cost: int):
        super().__init__(_cost, Arrow)


class BuyPistolCmd(BuyCommand):

    def __init__(self, _cost: int):
        super().__init__(_cost, Pistol)


class BuyBulletCmd(BuyCommand):

    def __init__(self, _cost: int):
        super().__init__(_cost, Bullet)


class BuyShotgunCmd(BuyCommand):

    def __init__(self, _cost: int):
        super().__init__(_cost, Shotgun)


class BuyShellCmd(BuyCommand):

    def __init__(self, _cost: int):
        super().__init__(_cost, Shell)


class BuyFlamethrowerCmd(BuyCommand):

    def __init__(self, _cost: int):
        super().__init__(_cost, Flamethrower)
