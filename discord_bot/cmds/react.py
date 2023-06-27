import discord
from discord.ext import commands
from cog.classes import Cog_Extension
import random
import json

with open('setting.json',mode='r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

class React(Cog_Extension):
    
    @commands.command()    #從本機上傳圖片至伺服器
    async def pc_image(self,ctx):    #所有()中要新增self參數
        random_pic = random.choice(jdata["image_01"])
        img = discord.File(random_pic)
        await ctx.send(file=img)

    @commands.command()    #從網路上傳圖片連結至伺服器
    async def web_image(self,ctx):
        random_pic = random.choice(jdata["url_01"])
        await ctx.send(random_pic)

def setup(bot):
    bot.add_cog(React(bot))