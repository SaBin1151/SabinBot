import asyncio
import discord
import datetime
import os

client = discord.Client()

token = "access_token"

@client.event
async def on_ready():
    print("다음으로 로그인합니다 : ")
    print(client.user.name)
    print(client.user.id)
    print("===========")
    game = discord.Game("사비니")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    now = datetime.datetime.now()
    if message.author.bot:
        return None
    if message.content == ("안녕"):
        await message.channel.send("안녕!")
    if message.content == ("S명령어"):
        embed = discord.Embed(title="안녕 난 사빈봇이야!", description="명령어 앞에 S로 시작해!", color=0x00ff00)
        embed.set_footer(
            text=str(now.year) + "년 " + str(now.month) + "월 " + str(now.day) + "일 | " + str(now.hour) + ":" + str(
                now.minute) + ":" + str(now.second))
        embed.set_image(url="https://i.imgur.com/TPXM3me.png")
        await message.channel.send(message.channel, embed=embed)

access_token = os.environ["BOT_TOKEN"]
client.run(token)
