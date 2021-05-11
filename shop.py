import math

import player
from items import item
from items.weapons.ammo import Arrow, Shell, Bullet, RifleBullet
from items.weapons.melee import Knife, Crowbar, BaseballBat, RoadSign
from items.weapons.ranged import Bow, Crossbow, Shotgun, Pistol, HuntingRifle, SniperRifle


class Shop:

    items_per_page = 10.0

    def __init__(self):
        self.items = List.items

    def list_items(self, page: int = 1) -> str:
        response = ""
        if 0 < page <= math.ceil(len(self.items)/Shop.items_per_page):
            stop = int(Shop.items_per_page * page)
            start = stop - 10
            if stop > len(self.items):
                stop = len(self.items)
            for i in range(start, stop):
                num = i+1
                if num < 10:
                    response += "` "
                else:
                    response += "`"
                response += f"{num}. ${self.items[i].cost}\t`{self.items[i].name}\n"
        else:
            response = "Invalid page number!"

        return response

    def buy_item(player: player.Player, item_index: int) -> Type[item.Item]:
        pass


class List:

    items = [
        # weapons category
        Arrow,
        Shell,
        Bullet,
        RifleBullet,

        Knife,
        Crowbar,
        BaseballBat,
        RoadSign,
        
        Bow,
        Crossbow,
        Shotgun,
        Pistol,
        HuntingRifle,
        SniperRifle
    ]