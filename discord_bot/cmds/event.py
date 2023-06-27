# test
import discord
from discord.ext import commands
from cog.classes import Cog_Extension
import json

with open('setting.json',mode='r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Event(Cog_Extension):

    @commands.Cog.listener()    #當成員加入伺服器時回應
    async def on_member_join(self,member):
        print(f"{member} join!")    #單引號會出錯,暫時先用雙引號
        channel = self.bot.get_channel(int(jdata["test_01_channel"]))
        await channel.send(f"{member} join!")

    @commands.Cog.listener()    #當成員離開伺服器時回應
    async def on_member_remove(self,member):
        print(f"{member} leave!")
        channel = self.bot.get_channel(int(jdata["test_01_channel"]))
        await channel.send(f"{member} leave!")

    @commands.Cog.listener()    #對特定msg回應
    async def on_message(self,msg):
        keyword = jdata["keyword"]
        selfbotmsg = (msg.author != self.bot.user)    #Bot不會回應自己的訊息
        if msg.content in keyword and selfbotmsg:
            await msg.channel.send("我看你是很懂喔")
        # elif '\u4e00' <= msg.content[-1] <= '\u9fff' and selfbotmsg:    #無差別攻擊
        #     await msg.channel.send(f"{msg.content[-1]}你媽")

def setup(bot):
    bot.add_cog(Event(bot))