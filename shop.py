import math

import player
from items.consumables.health import PainKillers, FirstAidKit, Medkit, Antidote
from items.tagging import Tags
from items.weapons.ammo import Arrow, Shell, Bullet, RifleBullet
from items.weapons.melee import Knife, Crowbar, BaseballBat, RoadSign
from items.weapons.ranged import Bow, Crossbow, Shotgun, Pistol, HuntingRifle, SniperRifle
from items.wearables.armor import RiotShield, MetalSleeves, MetalBodyArmor
from items.wearables.gears.buffs.damage import Bayonet, BarbedWireWrap
from items.wearables.gears.buffs.health import Multivitamin, PowerVitamin, SuperVitamin
from items.wearables.gears.buffs.profit import CoinMagnet, BillVacuum
from items.wearables.gears.storage import Backpack, DuffelBag, Quiver, AmmoBelt, AmmoSash


class ItemList:

    categories = [Tags.consumables, Tags.weapons, Tags.wearables]

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
        SniperRifle,

        # consumables category
        PainKillers,
        FirstAidKit,
        Medkit,
        Antidote,

        # armor category
        RiotShield,
        MetalSleeves,
        MetalBodyArmor,

        # buff gear category
        Bayonet,
        BarbedWireWrap,
        Multivitamin,
        PowerVitamin,
        SuperVitamin,
        CoinMagnet,
        BillVacuum,

        # storage gear category
        Backpack,
        DuffelBag,
        Quiver,
        AmmoBelt,
        AmmoSash
    ]


class Shop:

    categories = ItemList.categories
    items_per_page = 10.0
    num_pages = math.ceil(len(ItemList.items)/items_per_page)
    row_format = "`${:>5} | {:<20}`\n"

    @staticmethod
    def list_items(page: int = 1) -> str:
        response = ""
        if 0 < page <= Shop.num_pages:
            stop = int(Shop.items_per_page * page)
            start = stop - 10
            if stop > len(ItemList.items):
                stop = len(ItemList.items)

            header_format = f"Showing items {start} - {stop} of {len(ItemList.items)} items\n"
            footer1_format = f"Page {page} of {Shop.num_pages}\n"
            footer2_format = ":white_large_square: " * (page - 1) + ":white_square_button: " + ":white_large_square: " * (Shop.num_pages - page)

            response += header_format
            for i in range(start, stop):
                response += Shop.row_format.format(ItemList.items[i].price, ItemList.items[i].name)
            response += footer1_format
            response += footer2_format

        else:
            response = "Invalid page number!"

        return response

    @staticmethod
    def buy_item(plr: player.Player, item_name: str) -> bool:
        for shop_item in ItemList.items:
            if shop_item.name.lower() == item_name.lower():
                purchase = shop_item()
                print(f"found {shop_item.name}")
                if len(plr.inventory) < player.Player.max_inventory and 0 <= purchase.price <= plr.money:
                    plr.money -= purchase.price
                    plr.inventory.append(purchase)
                    print(f"bought {shop_item.name}")
                    return True
                break
        return False

    @staticmethod
    def search(search_term: str):
        response = f"Search results for {search_term}:\n"

        for shop_item in ItemList.items:
            term_found_in_tags = False
            for tag in shop_item.tags:
                if search_term in tag:
                    term_found_in_tags = True
                    break
            if search_term.lower() in shop_item.name.lower() or term_found_in_tags:
                response += Shop.row_format.format(shop_item.price, shop_item.name)

        return response

    @staticmethod
    def list_by_category(category: str) -> str:
        if category not in Shop.categories:
            return "Invalid category!"
        else:
            response = ""
            for shop_item in ItemList.items:
                if category in shop_item.tags:
                    response += Shop.row_format.format(shop_item.price, shop_item.name)

            return response
