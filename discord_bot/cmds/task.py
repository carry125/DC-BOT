import discord
from discord.ext import commands
from discord.ext.commands.core import command
from cog.classes import Cog_Extension
import json,asyncio,datetime

class Task(Cog_Extension):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        async def task_start():
            await self.bot.wait_until_ready()
            self.channel = self.bot.get_channel(923234841632329790)
            while not self.bot.is_closed():
                now_time = datetime.datetime.now().strftime('%H%M')
                with open('setting.json',mode='r',encoding='utf8') as jfile:
                    jdata = json.load(jfile)
                if jdata["time"] == now_time:
                    await self.channel.send("Task Working")
                    await asyncio.sleep(1)    #60秒
                else:
                    await asyncio.sleep(1)
                    pass

        self.bg_task = self.bot.loop.create_task(task_start())

    @commands.command()
    async def set_channel(self,ctx,ch:int):
        self.channel = self.bot.get_channel(ch)
        await ctx.send(f"set channel {self.channel.mention}")
    
    @commands.command()    #設定指定時間
    async def set_time(self,ctx,time):
        with open('setting.json',mode='r',encoding='utf8') as jfile:
            jdata = json.load(jfile)
        jdata["time"] = time
        with open('setting.json',mode='w',encoding='utf8') as jfile:
            json.dump(jdata,jfile,indent=4)

        await ctx.send(f"已設置時間{time}")

def setup(bot):
    bot.add_cog(Task(bot))