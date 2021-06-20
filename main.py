import discord
from discord.ext import commands
from dotenv import load_dotenv
from os import getenv

client = commands.Bot(command_prefix='!', intents=discord.Intents.all())


@client.event
async def on_ready():
    print("Ready!")


client.load_extension('discord_commands')

load_dotenv()
token = getenv("TOKEN")
client.run(token)
