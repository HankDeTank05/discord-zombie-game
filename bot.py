import os

import discord
from discord.ext.commands import command
from dotenv import load_dotenv
from discord.ext import commands
import logging
from player import Player
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

    if str(ctx.author) not in player_data.keys():
        try:
            player_data[str(ctx.author)] = Player(ctx.author.name)
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
    try:
        await ctx.send(player_data[str(ctx.author)].profile())
    except KeyError:
        await ctx.send(start_message)


@zombot.command()
async def fight(ctx):
    pass


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



zombot.run(TOKEN)
