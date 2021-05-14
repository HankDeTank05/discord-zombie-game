import math
from typing import Type

import player
from items import item
from items.weapons.ammo import Arrow, Shell, Bullet, RifleBullet
from items.weapons.melee import Knife, Crowbar, BaseballBat, RoadSign
from items.weapons.ranged import Bow, Crossbow, Shotgun, Pistol, HuntingRifle, SniperRifle


class Shop:

    items_per_page = 10.0

    def __init__(self):
        self.items = List.items

    @staticmethod
    def list_items(page: int = 1) -> str:
        response = ""
        if 0 < page <= math.ceil(len(List.items)/Shop.items_per_page):
            stop = int(Shop.items_per_page * page)
            start = stop - 10
            if stop > len(List.items):
                stop = len(List.items)
            for i in range(start, stop):
                num = i+1
                if num < 10:
                    response += "` "
                else:
                    response += "`"
                response += f"{num}. ${List.items[i].price}\t`{List.items[i].name}\n"
        else:
            response = "Invalid page number!"

        return response

    @staticmethod
    def buy_item(plr: player.Player, item_index: int) -> bool:
        item_index -= 1
        purchase = List.items[item_index]()
        if len(plr.inventory) < player.Player.max_inventory and 0 <= purchase.price <= plr.money:
            plr.money -= purchase.price
            plr.inventory.append(purchase)
            return True
        else:
            return False


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

        # consumables category

    ]