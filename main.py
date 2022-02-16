import os

import discord
from discord.ext import commands
from discord import Embed

from os import environ

import asyncio

from quart import Quart
from quart import jsonify
from quart import send_file

import lib.api_lib


embed_none = "\u200b"
guild_id = int(environ.get("GUILD_ID"))

if environ.get("DISCORD_PREFIX") is None:
    prefix = "!"
else:
    prefix = environ.get("DISCORD_PREFIX")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=prefix, case_insensitive=True, intents=intents)


async def status_task():
    await bot.change_presence(activity=discord.Game(name="Making Embeds"))
    await asyncio.sleep(60)
    await bot.change_presence(activity=discord.Game(name="Made by the_indian_dev#0148"))
    await asyncio.sleep(60)


@bot.event
async def on_ready():
    print("Bot Started")
    bot.loop.create_task(status_task())
    bot.loop.create_task(app.run_task())
    bot.load_extension('cogs.api')
    try:
        os.mkdir('temp/')
    except:
        pass


@bot.command(name='credits', description='Shows Credit')
async def credits_bot(ctx):
    """Shows credit nothing else"""
    embed = Embed(title="Credits", url="https://github.com/the-indian-dev",
                  description="About the developer", color=0x109319)
    embed.add_field(name=embed_none, value="Hi, I am @the-indian-dev aka Ritabrata Das", inline=False)
    embed.add_field(name=embed_none,
                    value="<:github:928249835625250836> [Github Profile](https://github.com/the-indian-dev)",
                    inline=False)
    embed.add_field(name=embed_none, value="<:chrome:928251220529905695> [Website](https://theindiandev.xyz)",
                    inline=False)
    embed.set_image(url="https://cdn.discordapp.com/attachments/927828410120687617/928187062291669002/durga-nft-2.jpg")
    embed.set_footer(text="Programmed By the_indian_dev#0148")
    await ctx.reply(embed=embed, mention_author=False)


app = Quart(__name__)


@app.route('/api/<int:id>')
async def index(member_id):
    guild = bot.get_guild(guild_id)
    member = guild.get_member(member_id)
    res = await lib.api_lib.api(member)
    return jsonify(res)


@app.route('/api/<int:id>.png')
async def img_gen(member_id):
    guild = bot.get_guild(guild_id)
    member = guild.get_member(member_id)
    res = await lib.api_lib.api(member)
    await lib.api_lib.image_gen_1(res)
    return await send_file("temp/gen.png")


@app.errorhandler(404)
def not_found(_):
    return jsonify({"Status": "ERROR",
                    "err": {
                        "code": 404,
                        "Message": "Not Found"}})


bot.run(environ.get("DISCORD_TOKEN"))
