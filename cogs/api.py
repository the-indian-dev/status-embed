from discord.ext import commands
import discord

import lib.api_lib as api_lib

from json import dumps


class ApiCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def api(self, ctx, *, member: discord.Member):
        res = await api_lib.api(member)
        await ctx.reply(dumps(res))

    @commands.command()
    async def info(self, ctx, user: discord.Member):
        res = await api_lib.api(member=user)
        await api_lib.image_gen_1(res)
        await ctx.send(file=discord.File("temp/gen.png"))


def setup(bot):
    bot.add_cog(ApiCog(bot))
    print("[INFO] LOADED COG API")
