import discord
from discord.ext import commands
from cog.classes import Cog_Extension
import json
import random

with open('setting.json',mode='r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Talk(Cog_Extension):

    @commands.command()
    async def 給我睡(self,ctx):
        # 資料在json中為str型態
        if ctx.message.author.id == int(jdata["My_discord_id"]):
            await ctx.send('<:dog_sleep:961316554300092487>')
            await ctx.bot.close()
        else:
            await ctx.send("睡你媽")

    @commands.command()
    async def 閉嘴(self,ctx):
        await ctx.send('<:dog_angry:878287177652518923>')

    @commands.command()
    async def 操你媽(self,ctx):
        await ctx.send('<:dog_angry:878287177652518923>')

    @commands.command()
    async def dance(self,ctx):
        await ctx.send(file = discord.File('./gif/cat_left.gif'))

    @commands.command()
    async def 晚餐吃什麼(self,ctx):
        await ctx.send(random.choice(jdata["dinner"]))

def setup(bot):
    bot.add_cog(Talk(bot))