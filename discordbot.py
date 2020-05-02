import random
import os
import asyncio
import discord
from discord.ext import *

client = discord.Client()
tocken = "your_tocken"


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("당신이 연애할 확률 계산중")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.content.startswith("서버주소"):
        await message.channel.send("Spina.kr")
    if message.content.startswith("스피나봇"):
        await message.channel.send("난 BONI의 따까...아니 봇이에요!")
    if message.content.startswith("안녕하세요"):
        await message.channel.send("반가워요!")
    if message.content.startswith("스피나봇 메뉴는?"):
        await message.channel.send("된장찌개")
        await message.channel.send("김치찌개")
        await message.channel.send("볶음밥")
        await message.channel.send("이거 3개중에 골라요 제가 가장 좋아하는 메뉴에요!")
    if message.content.startswith("직업"):
        await message.channel.send("현재 준비중이에요!!")
    if message.content.startswith("가이드"):
        await message.channel.send("버섯님 카오스님 윤빈님 핫도그님 하롱님 이수터님이 계십니다")
    if message.content.startswith("DM"):
        author = message.guild.get_member(int(message.content[4:22]))
        msg = message.content[23:]
        await author.send(msg)

access token = os.environ["BOT_TOKEN"]
client.run(access_token)
