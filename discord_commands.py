import discord
from discord.ext import commands
import datetime
import dateutil.parser
import string


class Commands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command('ping')
    async def ping(self, ctx: commands.Context):
        await ctx.send(f'Pong! {self.bot.latency * 1000:.0f}')

    @commands.command('poll')
    async def poll(self, ctx: commands.Context, title: str, question: str, end_time: str = None, *args):
        letters = '🇦 🇧 🇨 🇩 🇪 🇫 🇬 🇭 🇮 🇯 🇰 🇱 🇲 🇳 🇴 🇵 🇶 🇷 🇸 🇹 🇺 🇻 🇼 🇽 🇾 🇿'.split()

        embed = discord.Embed(
            title=title,
            description=f'{question}\n'
                        f'{"═" * 25}\n'
                        f'{chr(10).join((f"{emoji} {answer}"for answer, emoji in zip(args, letters)))}\n'
                        f'{"═" * 25}\n'
                        f'Vote on the poll by reacting, or add\n'
                        f'another option with `!add your-option-here`'
        )

        message = await ctx.send(embed=embed)
        for emoji, _ in zip(letters, args):
            await message.add_reaction(emoji)


def setup(bot: commands.Bot):
    bot.add_cog(Commands(bot))
