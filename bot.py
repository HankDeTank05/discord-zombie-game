import os

import discord
from discord.ext.commands import command
from dotenv import load_dotenv
from discord.ext import commands

from gamestate import *

intents = discord.Intents.default()
intents.members = True

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

zombot = commands.Bot(command_prefix='z!')

guild_states = GameState.load_all_guild_states()


class sc:

    @staticmethod
    def get_current_guild_state(_guild_id):
        return guild_states[str(_guild_id)]

    @staticmethod
    def get_player(ctx):
        return sc.get_current_guild_state(ctx.guild.id).get_player(ctx.author)

    @staticmethod
    def new_player(ctx):
        return sc.get_current_guild_state(ctx.guild.id).new_player(ctx.author)


@zombot.event
async def on_ready():
    print(f'{zombot.user.name} has connected to Discord!')


@zombot.command(name='start', help=' o - Start playing the zombie game.')
async def start(ctx):
    try:
        response = guild_states[str(ctx.guild.id)].new_player(ctx.author)
    except KeyError:
        print(f"Created new game state for this guild (ID: {ctx.guild.id})")
        guild_states[str(ctx.guild.id)] = GameState()
        response = guild_states[str(ctx.guild.id)].new_player(ctx.author)
    await ctx.send(response)


@zombot.command(name='base', help=' o - Check the status of the base.')
async def base(ctx):
    response = guild_states[str(ctx.guild.id)].base.status()
    await ctx.send(response)


@zombot.command(name='storage', help=' x - Check the status of the storage.')
async def storage(ctx):
    response = ":x:storage command"
    await ctx.send(response)


@zombot.command(name='equip', help=" x - Equip a weapon, some ammo, or some clothing gear.")
async def equip(ctx, item=None):
    response = ":x:equip command"
    await ctx.send(response)


@zombot.command(name='inventory', help=" x - Check the items in your inventory")
async def inventory(ctx):
    response = ":x:inventory command"
    await ctx.send(response)


@zombot.command(name='profile', help=" o - Check player data, such as health, money, equipped weapon, etc.")
async def profile(ctx):
    response = sc.get_player(ctx).profile()
    await ctx.send(response)


@zombot.command(name='fight', help=' o - Kill some zombies!', aliases=['f', 'fgt'])
async def fight(ctx):
    response = sc.get_player(ctx).fight()
    await ctx.send(response)


@zombot.command(name='save', help=' x - Save all progress.', hidden=True, enabled=False)
async def save(ctx):
    if ctx.author == "HankDeTank05#3890":
        GameState.save_all_guild_states(guild_states)
        GameState.load_all_guild_states()


zombot.run(TOKEN)
