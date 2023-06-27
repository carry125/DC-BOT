import discord
from discord.ext import commands
from discord.ext.commands.core import command
from cog.classes import Cog_Extension
import datetime

class Main(Cog_Extension):
    
    @commands.command()    #回傳Bot回應時間
    async def ping(self,ctx):    #所有()中要新增self參數
        await ctx.send(f"{round(self.bot.latency*1000)} (ms)")

    @commands.command()    #回傳指定字串
    async def hi(self,ctx):
        await ctx.send("new comment")

    @commands.command()    #Embed.....?
    async def em(self,ctx):
        embed=discord.Embed(title="About", url="https://pcredivewiki.tw/", description="About the bot",
                            color=0x0affb6, timestamp=datetime.datetime.utcnow())
        embed.set_author(name="meow", url="https://www.plurk.com/m/p/niqe60",
                        icon_url="https://emos.plurk.com/954caca90194e66e83f44620db34d0c2_w48_h48.gif")
        embed.set_thumbnail(url="https://emos.plurk.com/a1578c12d8b09eaca03be79d78cc12cb_w48_h47.gif")
        embed.add_field(name="1", value="0", inline=False)
        embed.add_field(name="2", value="22", inline=True)
        embed.add_field(name="3", value="33", inline=True)
        embed.add_field(name="4", value="44", inline=True)
        embed.add_field(name="5", value="55", inline=True)
        embed.set_footer(text="uiliuhlkbytlkhk")
        await ctx.send(embed=embed)
    
    # @commands.command()    #刪除我所說的訊息
    # async def sayed(self,ctx,*,msg):
    #     await ctx.message.delete()
    #     await ctx.send(msg)

    # @commands.command()    #刪除指定數量訊息
    # async def clean(self,ctx,num:int):
    #     await ctx.channel.purge(limit=num,before=datetime.datetime.utcnow())    #刪除指令之前的訊息
    #     await ctx.send(f"已刪除{num}條訊息")

def setup(bot):
    bot.add_cog(Main(bot))