import os

import discord
from discord.ext.commands import command
from dotenv import load_dotenv
from discord.ext import commands
import logging

from items.consumable import Consumable
from items.consumables.health import HealthConsumable
from items.weapons.melee import Knife, Crowbar, BaseballBat, RoadSign, MeleeWeapon
from items.weapons.ranged import Bow, Crossbow, Shotgun, Pistol, HuntingRifle, SniperRifle, RangedWeapon
from items.weapons.ammo import Arrow, Shell, Bullet, RifleBullet
from items.wearables.armor import Armor
from items.wearables.gear import Gear
from shop import Shop
from player import Player, TmpPlayer
import util

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

intents = discord.Intents.default()
intents.members = True

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

description = """A zombie apocalypse discord bot game."""

zombot = commands.Bot(command_prefix='zb ', description=description, intents=intents)

player_data = util.rebuild_player_data()
owner = "HankDeTank05#3890"
start_message = "Please start the game using `zb start` before using this command!"
insufficient_permissions = "You do not have permission to access this command!"

# TODO: organize all the player-visible commands above the permission-locked commands

''' BASIC COMMANDS '''


@zombot.event
async def on_ready():
    print(f'{zombot.user.name} has connected to Discord!')


@zombot.command()
async def start(ctx):
    """
    Start playing the game.
    :param ctx:
    :return:
    """
    success = f"Welcome to the zombie apocalypse, {ctx.author.name}!"
    failure = "You have already started!"

    save_key = util.make_save_key(ctx.guild.id, str(ctx.author))

    if str(ctx.author) not in player_data.keys():
        try:
            player_data[save_key] = Player(ctx.author.name)
        except FileExistsError:
            await ctx.send(failure)
        else:
            await ctx.send(success)


''' COMMON PLAYER COMMANDS '''


@zombot.command()
async def profile(ctx):
    """
    Get information about yourself.
    :param ctx:
    :return:
    """

    # TODO: change the emojis in the output

    save_key = util.make_save_key(ctx.guild.id, str(ctx.author))
    try:
        await ctx.send(player_data[save_key].profile(zombot))
    except KeyError:
        await ctx.send(start_message)


@zombot.command(aliases=["inv"])
async def inventory(ctx, *args):
    grouped_aliases = ["grouped", "grp", "g"]
    group = False
    if len(args) == 1 and (args[0].lower() in grouped_aliases):
        group = True
    save_key = util.make_save_key(ctx.guild.id, str(ctx.author))
    response = player_data[save_key].list_items_in_inventory(group)
    await ctx.send(response)


@zombot.command()
async def fight(ctx):
    """
    Fight some zombies!

    How fighting works:
    ------------------

         knife range     bow range
           0->1        5   ->    10
    Player |-|         |- - - - -|
             1   --->  5
           inter-range size

    * The amount of health you lose when fighting is related to your inter-range size.
        * NOTE: "related to" is not the same as "directly correlated with"!
        * You may not lose the same amount of health each time you fight, even if your inter-range size doesn't change.
        * A smaller inter-range size will cause you to lose less health when fighting, and vice versa.

    * The amount of money you earn from fighting zombies is related to how many of them you kill.
        * NOTE: "related to" is not the same as "directly correlated with"!
        * You may not earn the same amount of money each time you fight, even if your total attack range doesn't change.
        * The larger your total attack range (melee range + distance range), the more zombies you're likely to kill.

    * You earn 3 EXP per kill.
    """
    # TODO: add a check-and-delete for weapons whose durability is zero or lower (see the todo in the USE command for details)
    save_key = util.make_save_key(ctx.guild.id, str(ctx.author))
    response, level_up = player_data[save_key].fight()
    await ctx.send(response)

    if level_up:
        level_up_response = f"You leveled up! You're now level {player_data[save_key].level}!"
        await ctx.send(level_up_response)


@zombot.group()
async def shop(ctx):
    """
    Visit the item shop.
    """
    response = ""

    if ctx.invoked_subcommand is None:
        response = "Use `shop search` or `shop page` to see shop listings."

        await ctx.send(response)


@shop.command(name="page", aliases=["pg", "p"])
async def _page(ctx, page: int = 1):

    # TODO: finish making the item shop
    # TODO: add weapon prices
    # TODO: add ammo prices
    # TODO: add health consumable prices

    response = Shop.list_items(page)

    await ctx.send(response)


@shop.command(name="search")
async def _search(ctx, *args):

    search_term = ""
    for arg in args:
        search_term += arg + " "
    search_term = search_term.strip()

    response = Shop.search(search_term)

    await ctx.send(response)


@zombot.command()
async def buy(ctx, *args):
    """
    Buy an item from the shop.
    """

    item_name = ""
    for arg in args:
        item_name += arg + " "
    item_name = item_name.strip()

    plr = player_data[util.make_save_key(ctx.guild.id, str(ctx.author))]

    shop_success = Shop.buy_item(plr, item_name)
    if shop_success:
        response = f"You purchased a {plr.inventory[-1].name} for ${plr.inventory[-1].price}."
    else:
        response = f"There was an error purchasing this item. Either it is not available for purchase or you do not " \
                   f"have enough money to purchase it. "

    await ctx.send(response)


@zombot.command()
async def use(ctx, *args):
    """
    Use an item in your inventory.
    """
    item_to_use = ""
    for arg in args:
        item_to_use += arg + " "
    item_to_use = item_to_use.strip()

    item_name_capitalized = ""

    item_used = False
    item_found = False
    item_found_tags = []
    item_out_of_uses = False
    item_cannot_use = False

    save_key = util.make_save_key(ctx.guild.id, str(ctx.author))
    plr = player_data[save_key]

    response = ""

    for inv_item in plr.inventory:
        if inv_item.name.lower() == item_to_use.lower():
            item_found = True
            item_name_capitalized = inv_item.name
            item_found_tags = inv_item.tags
            if "usable" in inv_item.tags:
                if isinstance(inv_item, HealthConsumable):
                    if plr.health < plr.max_health[plr.level]:
                        pre_use_health = plr.health
                        inv_item.use(plr)
                        response = f"{util.emoji('health')}{pre_use_health}/{plr.max_health[plr.level]} --> " \
                                   f"{util.emoji('health')}{plr.health}/{plr.max_health[plr.level]}\n"
                    else:
                        response = f"Your health is already maxed out at {util.emoji('health')}{plr.health}!\n"
                        item_cannot_use = True
                elif isinstance(inv_item, Consumable):
                    inv_item.use()

                item_used = True

                # TODO: add a similar check-and-deletion for weapons whose durability is zero
                if isinstance(inv_item, Consumable) and inv_item.uses_remaining <= 0:
                    plr.remove_from_inventory(inv_item)
                    item_out_of_uses = True

                break

    if item_found:
        if item_used:
            if item_out_of_uses:
                response += f"You used the rest of the {item_name_capitalized}!"
            elif item_cannot_use:
                pass
            else:
                response += f"You used your {item_name_capitalized}!"
        else:
            response += f"You cannot use your {item_name_capitalized} with the `use` command!"
            if "weapon" in item_found_tags:
                response += f"\nNOTE: Weapons, such as your {item_name_capitalized}, can be used by equipping it " \
                            f"with `zb equip` and then fighting zombies with `zb fight`."
    else:
        response += f"No item named '{item_to_use}' was found in your inventory!"

    await ctx.send(response)


@zombot.command()
async def equip(ctx, *args):
    """
    Equip armor, gear, or a weapon from your inventory.
    """

    # TODO: THIS COMMAND IS BUGGY, NEEDS FIXING

    item_to_equip = ""
    for arg in args:
        item_to_equip += arg + " "
    item_to_equip = item_to_equip.strip()

    item_name_capitalized = ""

    item_equipped = False
    item_found = False
    item_found_tags = []
    item_unequippable = False

    save_key = util.make_save_key(ctx.guild.id, str(ctx.author))
    plr = player_data[save_key]

    for inv_item in plr.inventory:
        if inv_item.name.lower() == item_to_equip.lower():
            item_found = True
            item_name_capitalized = inv_item.name
            item_found_tags = inv_item.tags
            if "equippable" in inv_item.tags:
                if isinstance(inv_item, MeleeWeapon):
                    if plr.weapon_melee is not None:
                        plr.store_in_inventory(plr.weapon_melee)
                    plr.weapon_melee = inv_item
                    item_equipped = True
                elif isinstance(inv_item, RangedWeapon):
                    if plr.weapon_ranged is not None:
                        plr.store_in_inventory(plr.weapon_ranged)
                    plr.weapon_ranged = inv_item
                    item_equipped = True
                elif isinstance(inv_item, Armor):  # TODO: create the wearables.Armor class
                    pass
                elif isinstance(inv_item, Gear):  # TODO: create the wearables.Gear class
                    pass

                if item_equipped:
                    plr.inventory.remove(inv_item)

                break

    response = ""

    if item_found:
        if item_equipped:
            response += f"You equipped your {item_name_capitalized}!"
        else:
            response += f"You cannot equip a {item_name_capitalized}!"
    else:
        response += f"No item named '{item_to_equip}' was found in your inventory!"

    response = ":x:equip command"
    await ctx.send(response)


''' RESTRICTED ACCESS COMMANDS '''


@zombot.command(hidden=True)
async def simulate_combat(ctx, _melee: str = "knife", _ranged: str = "bow", _times: int = 1):
    # TODO: add a permissions check for the simulatecombat command
    temp_player = TmpPlayer("temp")

    valid_melee = True
    _melee = _melee.lower()
    if _melee == "none":
        temp_player.weapon_melee = None
    elif _melee == "knife":
        temp_player.weapon_melee = Knife()
    elif _melee == "crowbar":
        temp_player.weapon_melee = Crowbar()
    elif _melee == "baseball_bat":
        temp_player.weapon_melee = BaseballBat()
    elif _melee == "road_sign":
        temp_player.weapon_melee = RoadSign()
    else:
        valid_melee = False

    valid_ranged = True
    _ranged = _ranged.lower()
    if _ranged == "none":
        temp_player.weapon_melee = None
    elif _ranged == "bow":
        temp_player.weapon_ranged = Bow()
    elif _ranged == "crossbow":
        temp_player.weapon_ranged = Crossbow()
    elif _ranged == "shotgun":
        temp_player.weapon_ranged = Shotgun()
    elif _ranged == "pistol":
        temp_player.weapon_ranged = Pistol()
    elif _ranged == "hunting_rifle":
        temp_player.weapon_ranged = HuntingRifle()
    elif _ranged == "sniper_rifle":
        temp_player.weapon_ranged = SniperRifle()
    else:
        valid_ranged = False

    valid_times = 1 <= _times < 999999999

    if valid_melee and valid_ranged and valid_times:
        data = []
        prev_money = 0

        for i in range(_times):
            temp_player.fight()
            data.append(temp_player.money - prev_money)
            prev_money = temp_player.money
            temp_player.health = Player.max_health[1]

        report = f"__**combat simulation report**__\n" \
                 f"**melee weapon**: {_melee}\n" \
                 f"**ranged weapon**: {_ranged}\n" \
                 f"**rounds simulated**: {_times}\n" \
                 f"**average money gained per round of combat**: {sum(data) / len(data)}\n" \
                 f"**total money earned from combat**: {sum(data)}"
        await ctx.send(report)
    else:
        error_message = "__**ERROR!**__\n"
        if not valid_melee:
            error_message += f"invalid melee: {_melee}\n"

        if not valid_ranged:
            error_message += f"invalid ranged: {_ranged}"

        if not valid_times:
            error_message += f"invalid times: {_times}"

        await ctx.send(error_message)


@zombot.command(hidden=True)
async def shutdown(ctx):
    if str(ctx.author) == owner:
        output = "Saving all player data and shutting down."
    else:
        output = insufficient_permissions
    await ctx.send(output)

    if str(ctx.author) == owner:
        util.save_all_data_and_shut_down(player_data)


@zombot.command(hidden=True)
async def print_player_info(ctx):
    # TODO: add permissions check for printplayerinfo command
    if str(ctx.author) == owner:
        output = "Check stdout"
        util.print_dict(player_data)
    else:
        output = insufficient_permissions

    await ctx.send(output)


@zombot.group(hidden=True)
async def emoji(ctx):
    # TODO: add permissions check for emoji command
    response = ""

    for available_emoji in zombot.emojis:
        response += f"{zombot.get_emoji(available_emoji.id)}{available_emoji.name}: {str(available_emoji.id)}\n"

    await ctx.send(response)


@emoji.command(name="all")
async def _all(ctx):
    response = ":x:emoji all command"
    await ctx.send(response)


@emoji.command(name="permissions")
async def _permissions(ctx):
    response = "ZomBot "
    if discord.Permissions.manage_emojis:
        response += "can "
    else:
        response += "can't "
    response += "manage emojis"

    await ctx.send(response)


''' INFO COMMANDS '''


@zombot.group()
async def info(ctx):
    """
    Get information about aspects of the game.
    """

    if ctx.invoked_subcommand is None:
        response = ":x:info command"  # TODO: write the "info" command
        await ctx.send(response)
# TODO: add more subcommands


# TODO: write the "info weapons" command
@info.group(name="weapons", aliases=["weapon", "w"])
async def _weapons(ctx):
    """
    Get information about how weapons work.
    """

    if ctx.invoked_subcommand is None:
        response = ":x:info weapons command"
        await ctx.send(response)


# TODO: write the "info consumables" command
@info.group(name="consumables", aliases=["consumable"])
async def _consumables(ctx):
    pass


# TODO: write the "info armor" command
@info.group(name="armor")
async def _armor(ctx):
    pass


# TODO: write the "info gear" command
@info.group(name="gear")
async def _gear(ctx):
    pass


# TODO: add more info here
@_weapons.command(name="ammo")
async def _ammo(ctx):
    """
    Get information about how ammo works.
    """

    response = ""

    ammo = [Arrow(), Shell(), Bullet(), RifleBullet()]

    for ammo_type in ammo:
        response += f"{zombot.get_emoji(ammo_type.icon)} {ammo_type.name}\n"

    await ctx.send(response)


@_weapons.command(name="melee")
async def _melee(ctx):
    """
    Get information about how melee weapons work.
    """

    response = ""

    melee = [Knife(), Crowbar(), BaseballBat(), RoadSign()]
    attributes = ["Name", "Price", "Damage Out", "Base Durability", "Range (max)"]

    row_header_format = "{:^15}" * len(attributes)
    row_format = "{:<15}" + "{:^15}" * (len(attributes) - 1)

    response += "`" + row_header_format.format(*attributes) + "`\n"

    for weapon in melee:
        response += "`" + row_format.format(weapon.name, weapon.price, weapon.damage_out, weapon.base_durability,
                                            weapon.range_max) + "`\n"

    await ctx.send(response)


@_weapons.command(name="ranged")
async def _ranged(ctx):
    """
    Get information about how ranged weapons work.
    """

    response = ""

    ranged = [Bow(), Crossbow(), Shotgun(), Pistol(), HuntingRifle(), SniperRifle()]
    attributes = ["Name", "Price", "Base Durability", "Range (min)", "Range (max)", "Ammo Type", "Ammo Damage"]

    row_header_format = "{:^15}" * len(attributes)
    row_format = "{:<15}" + "{:^15}" * (len(attributes) - 3) + "{:<15}" + "{:^15}"

    response += "`" + row_header_format.format(*attributes) + "`\n"

    for weapon in ranged:
        emoji_string = f"{zombot.get_emoji(weapon.icon)}"
        weapon_string = f"` \t{weapon.name}"
        info_string = f"{weapon.price}\t" \
                      f"{weapon.base_durability}\t" \
                      f"{weapon.range_min}\t" \
                      f"{weapon.range_max}\t`" \
                      f"{zombot.get_emoji(weapon.ammo_type.emoji_id)}\n"
        response += "`" + row_format.format(weapon.name, weapon.price, weapon.base_durability, weapon.range_min,
                                            weapon.range_max, weapon.ammo_type.name,
                                            weapon.ammo_type.damage_out) + "`\n"

    # response += "NOTE: use `info weapons [weapon]` to see more detailed weapon information!"

    await ctx.send(response)


zombot.run(TOKEN)

# my_secret = os.environ['DISCORD_TOKEN']
