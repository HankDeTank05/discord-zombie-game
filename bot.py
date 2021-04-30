import os

import discord
from discord.ext.commands import command
from dotenv import load_dotenv
from discord.ext import commands

from gamestate import GameState

intents = discord.Intents.default()
intents.members = True

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

game_state = GameState()

guild_states = {}


class ZomBot(commands.Bot):

    starting_health = 5

    async def on_ready(self):
        print(f'{self.user.name} has connected to Discord!')
        for guild in self.guilds:
            guild_states[str(guild.id)] = GameState.load_guild_state(guild.id)

    @command(name='start', help='Start playing the zombie game.')
    async def start(self, ctx):
        response = f"Welcome to the zombie apocalypse, {ctx.author}!"
        game_state["profiles"][ctx.author] = self.starting_health
        ctx.send(response)

    @command(name='fight', help='Kill some zombies!')
    async def fight(self, ctx):
        pass


zombot = ZomBot(command_prefix='z!')

zombot.run(TOKEN)