import discord
from module import *


client = discord.Client()


@client.event
async def on_ready():
    print("준비됐어!")
    await client.get_channel(666455973124374537).send("김고래 접속!")
    game = discord.Game("눈뜨고 힐링")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):

    if message.content.startswith("!학습"):
        msglist = msgdivision(message.content)
        await message.channel.send(study(msglist))

    if message.content.startswith("@"):
        msg = message.content
        msgs = msg[1:]
        msgs.strip()
        await message.channel.send(talk(msgs))

    if message.content.startswith("!비만도"):
        msglist = msgdivision(message.content)
        await message.channel.send(bmi(msglist))

    if message.content.startswith("!검색"):
        a = msgdivision(message.content)
        await message.channel.send(srch(a))

    if message.content.startswith("!비밀암호"):
        user = message.guild.get_member(message.author.id)
        await user.send("서버 채널에 공개핼 암호가 아니라면 이곳에\n !암호 생성 (원하는 문장이나 단어) (2~5정도의 숫자)\n 를 입력해 주세요. \n !암호 해독 (암호문) (생성할 때 사용한 숫자) \n 로 해독 가능합니다.")

    if message.content.startswith("!암호"):
        msglist = msgdivision(message.content)
        await message.channel.send(s_code(msglist))

    if message.content.startswith("!임티"):
        a = msgdivision(message.content)
        await message.channel.send(imti(a[1]))

    if message.content.startswith("!강화"):
        a = msgdivision(message.content)
        b = message.author.id
        await message.channel.send(enhance(a, b))

client.run("NjcwOTU0NzExMjc2NDUzOTA5.Xi15qw.H8Oc1vSwr027Pfh6gLet4haF-Mc")
