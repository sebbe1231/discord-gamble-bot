import importlib
from os import environ

import discord
from discord.ext import commands

intents = discord.Intents.all()
intents.presences = True
intents.members = True
intents.guilds = True
intents.members = True
intents.reactions = True
intents.dm_messages = True

bot = commands.Bot(command_prefix="$", intents=intents, help_command=None)

@bot.event
async def on_ready():
    print("Bot is ready!")

bot.run(environ['DISCORD_TOKEN'])