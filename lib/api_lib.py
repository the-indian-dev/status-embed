import discord
from PIL import Image, ImageDraw, ImageFont


# noinspection PyTypedDict
async def api(member: discord.Member):
    res = {}
    activ = member.activities
    res['member'] = {'username': member.name + "#" + str(member.discriminator),
                     'av': f"https://cdn.discordapp.com/avatars/{member.id}/{member.avatar}.png?size=128",
                     'status': str(member.status)}
    if activ is None or activ == ():
        # noinspection PyTypedDict
        res['presence'] = {'type': None,
                           'image_big': None,
                           'image_small': None,
                           'name': None}
    else:
        try:
            res['presence'] = {'type': str(activ[0].type).split(".")[-1],
                               'image_big': str(activ[0].large_image_url),
                               'image_small': str(activ[0].small_image_url),
                               'name': str(activ[0].name)
                               }
        except AttributeError:
            res['presence'] = {'type': str(activ[0].type).split(".")[-1],
                               'image_big': None,
                               'image_small': None,
                               'name': str(activ[0].name)
                               }

    return res


async def image_gen_1(res: dict):
    img = Image.open("img/embed-2.png")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("font/ReadexPro-Regular.ttf", 100)
    fontbig = ImageFont.truetype("font/ReadexPro-Regular.ttf", 400)
    draw.text((200, 0), "Status", (255, 255, 255), font=fontbig)
    draw.text((50, 500), "Username  {}".format(res['member']['username']), (255, 255, 255),
              font=font)
    draw.text((50, 700), "Status    {}".format(res['member']['status']), (255, 255, 255), font=font)
    draw.text((50, 900), "Presence  {}".format(res['presence']['name']), (255, 255, 255),
              font=font)
    img.save('temp/gen.png')
