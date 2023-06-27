# 源代碼：https://github.com/noheartino/pcredive_gacha_discordbot
import discord
import random
from discord.ext import commands
from discord.utils import get
from cog.classes import Cog_Extension

arr = ['3star', '2star', '1star']
# 控制機率
rate = [2, 18, 80]
# discord img
img_3star='<:rainbow_card:962029054893129809>'
img_2star='<:gold_card:962029071921995777>'
img_1star='<:silver_card:962029085696082051>'

# discord不能在同一行上傳多張圖片(會分成多行)

def random_index(rate):
    start = 0
    index = 0
    randnum = random.randint(1, sum(rate))

    for index, scope in enumerate(rate):
        start += scope
        if randnum <= start:
            break
    
    return index

def random_card(number):
    card_list = [None]*number
    for i in range(number):
        # 先給定，避免每次if都是不同的
        prob_card=arr[random_index(rate)]
        
        if prob_card == '3star':
            card_list[i] = img_3star
        elif prob_card == '2star':
            card_list[i] = img_2star
        elif prob_card == '1star':
            card_list[i] = img_1star
        else:
            card_list[i] = img_1star
    
    return card_list

class Pcredive_gacha(Cog_Extension):

    @commands.command()
    async def 十連抽(self,ctx):
        card = random_card(10)

        # 保底
        if card.count(img_1star) == 10:
            card[9] = img_2star

        card.insert(5,'\n')
        lol = ''.join('%s' %id for id in card)
        # ctx.message.author.id獲取discord用戶id
        await ctx.send(f'<@{ctx.message.author.id}>')
        await ctx.send(lol)

    @commands.command()
    async def 兩百抽(self,ctx):
        card = random_card(200)

        rainbow = card.count(img_3star)
        gold = card.count(img_2star)
        silver = card.count(img_1star)
        if rainbow == 0:
            rainbow = 1
            silver-=1

        await ctx.send(f'<@{ctx.message.author.id}>')
        await ctx.send(f'{img_3star}x{rainbow}張\n{img_2star}x{gold}張\n{img_1star}x{silver}張')

    @commands.command()
    async def 抽卡機率(self,ctx):
        await ctx.send( "★3.."+'{:>5}'.format(str(rate[0]))+"%\n"
                        "★2.."+'{:>5}'.format(str(rate[1]))+"%\n"
                        "★1.."+'{:>5}'.format(str(rate[2]))+"%\n")

    @commands.command()
    async def 石蓮抽(self,ctx):
        await ctx.send('<:c86:911249576411922432>')

    @commands.command()
    async def 抽卡指令(self,ctx):
        embed = discord.Embed(title="爆射抽卡ㄐ器人 by沒心", description="沒有反應，就只是一個抽卡ㄐ器人，以下是指令", color=0xcc25de)
        embed.add_field(name="小吉十連抽", value="抽10張卡 有保底", inline=False)
        embed.add_field(name="小吉兩百抽", value="抽200張卡 有保底", inline=False)
        embed.add_field(name="小吉抽卡機率", value="顯示當前抽卡機率", inline=False)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Pcredive_gacha(bot))