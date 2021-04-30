from gamestate import Player
from items import Item, Knife


class CommandObj:

    def __init__(self):
        pass

    def execute(self):
        pass


class BuyCommand(CommandObj):

    def __init__(self, _cost: int, _item: Item):
        self.cost = _cost
        self.item = _item

    def execute(self, player: Player):
        player.money -= self.cost
        return self.item.__init__()


class BuyKnifeCmd(BuyCommand):

    def __init__(self, _cost: int):
        super().__init__(_cost, Knife)
