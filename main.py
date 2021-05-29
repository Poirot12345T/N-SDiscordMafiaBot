import asyncio
import discord
from decouple import config


prefix = config("PREFIX")
client = discord.Client()
info = "nothing special, I'm just a bot :person_shrugging:"

@client.event
async def on_ready():
    print("bot connected")

@client.event
async def on_message(message):
    global prefix
    if message.content.startswith(prefix):
        if message.content.startswith(prefix + "ping"):
            await message.channel.send("pong")
            print('pinged using ping')
        elif message.content.startswith(prefix + "info"):
            await message.channel.send(info)
        else:
            await message.channel.send("unknown command")
        


client.run(config("TOKEN"))