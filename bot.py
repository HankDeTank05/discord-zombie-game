import os

import discord
from discord.ext.commands import command
from dotenv import load_dotenv
from discord.ext import commands
import logging

from items.weapons.melee import *
from items.weapons.ranged import *
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


@zombot.command()
async def profile(ctx):
    """
    Get information about yourself.
    :param ctx:
    :return:
    """
    save_key = util.make_save_key(ctx.guild.id, str(ctx.author))
    await ctx.send(player_data[save_key].profile())


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
    """
    save_key = util.make_save_key(ctx.guild.id, str(ctx.author))
    await ctx.send(player_data[save_key].fight())


@zombot.command()
async def shop(ctx):
    """
    Visit the item shop.
    """
    await ctx.send(":x:shop command")


@zombot.command(hidden=True)
async def simulatecombat(ctx, melee: str = "knife", ranged: str = "bow", times: int = 1):
    temp_player = TmpPlayer("temp")

    valid_melee = True
    melee = melee.lower()
    if melee == "knife":
        temp_player.weapon_melee = Knife()
    elif melee == "crowbar":
        temp_player.weapon_melee = Crowbar()
    elif melee == "baseball_bat":
        temp_player.weapon_melee = BaseballBat()
    elif melee == "road_sign":
        temp_player.weapon_melee = RoadSign()
    else:
        valid_melee = False

    valid_ranged = True
    ranged = ranged.lower()
    if ranged == "bow":
        temp_player.weapon_ranged = Bow()
    elif ranged == "crossbow":
        temp_player.weapon_ranged = Crossbow()
    elif ranged == "shotgun":
        temp_player.weapon_ranged = Shotgun()
    elif ranged == "pistol":
        temp_player.weapon_ranged = Pistol()
    elif ranged == "hunting_rifle":
        temp_player.weapon_ranged = HuntingRifle()
    elif ranged == "sniper_rifle":
        temp_player.weapon_ranged = SniperRifle()
    else:
        valid_ranged = False

    valid_times = 1 <= times < 999999999

    if valid_melee and valid_ranged and valid_times:
        data = []
        prev_money = 0

        for i in range(times):
            temp_player.fight()
            data.append(temp_player.money - prev_money)
            prev_money = temp_player.money
            temp_player.health = Player.max_health[1]

        report = f"__**combat simulation report**__\n" \
                 f"**melee weapon**: {melee}\n" \
                 f"**ranged weapon**: {ranged}\n" \
                 f"**rounds simulated**: {times}\n" \
                 f"**average money gained per round of combat**: {sum(data)/len(data)}\n" \
                 f"**total money earned from combat**: {sum(data)}" \

        await ctx.send(report)
    else:
        error_message = "__**ERROR!**__\n"
        if not valid_melee:
            error_message += f"invalid melee: {melee}\n"

        if not valid_ranged:
            error_message += f"invalid ranged: {ranged}"

        if not valid_times:
            error_message += f"invalid times: {times}"

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
async def printplayerinfo(ctx):
    if str(ctx.author) == owner:
        output = "Check stdout"
        util.print_dict(player_data)
    else:
        output = insufficient_permissions

    await ctx.send(output)


@zombot.group()
async def info(ctx):
    """
    Get information about aspects of the game.
    """

    if ctx.invoked_subcommand is None:
        response = ":x:info command"
        await ctx.send(response)


@info.group(name="weapons", aliases=["weapon", "w"])
async def _weapons(ctx):
    """
    Get information about how weapons work.
    """

    if ctx.invoked_subcommand is None:
        response = ":x:info weapons command"
        await ctx.send(response)


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

    for weapon in melee:
        response += f"{zombot.get_emoji(weapon.icon)} {weapon.name}\n"

    await ctx.send(response)


@_weapons.command(name="ranged")
async def _ranged(ctx):
    """
    Get information about how ranged weapons work.
    """

    response = ""

    ranged = [Bow(), Crossbow(), Shotgun(), Pistol(), HuntingRifle(), SniperRifle()]

    for weapon in ranged:
        response += f"{zombot.get_emoji(weapon.icon)} {weapon.name}\n"

    await ctx.send(response)


@zombot.group(hidden=True)
async def emoji(ctx):

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


zombot.run(TOKEN)
