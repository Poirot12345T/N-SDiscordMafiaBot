import discord
from discord.ext import commands
import datetime
import re


class Commands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command('ping')
    async def ping(self, ctx: commands.Context):
        await ctx.send(f'Pong! {self.bot.latency * 1000:.0f}')

    @commands.command('poll')
    async def poll(self, ctx: commands.Context, title: str, end_time: str):

        embed = discord.Embed(title=title)
        await ctx.send(embed=embed)


def setup(bot: commands.Context):
    bot.add_cog(Commands(bot))
