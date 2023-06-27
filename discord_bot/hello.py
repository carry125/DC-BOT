#Bot實體建置：
import discord
from discord.ext import commands    #引入discord下的commands模組
import json
import os

with open('setting.json',mode='r',encoding='utf8') as jfile:    #取得setting.json資料
    jdata = json.load(jfile)

intents = discord.Intents.default()    #discord 1.5版本更新(intents)
intents.members=True
bot = commands.Bot(command_prefix="小吉", intents=intents)    #建置Bot實體至變數bot中

#Bot事件設置：
@bot.event    #當Bot準備好時回傳字串
async def on_ready():
    print("Bot ready!")

@bot.event    #當Bot上線時回傳字串
async def on_connect():
    print("Bot connected!")

#Bot指令設置：
@bot.command()    #load檔案至本檔案(hello.py)
async def load(ctx,extension):
    bot.load_extension(f"cmds.{extension}")
    await ctx.send(f"Loaded {extension} done!")

@bot.command()    #unload檔案至主檔案
async def unload(ctx,extension):
    bot.unload_extension(f"cmds.{extension}")
    await ctx.send(f"Unloaded {extension} done!")

@bot.command()    #reload檔案至主檔案
async def reload(ctx,extension):
    bot.reload_extension(f"cmds.{extension}")
    await ctx.send(f"Reloaded {extension} done!")

#在./cmds資料夾下搜尋檔案並load至主檔案
for Filename in os.listdir('./cmds'):
    if Filename.endswith('.py'):
        bot.load_extension(f"cmds.{Filename[:-3]}")

#???
if __name__ == '__main__':
    bot.run(jdata["TOKEN"])    #輸入機器人token以運行