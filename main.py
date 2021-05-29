import asyncio
import discord
from decouple import config

client = discord.Client()

@client.event
async def on_ready():
    print("bot connected")


client.run(config("TOKEN"))