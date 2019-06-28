import discord
import os


client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print('ready')
    game = discord.Game('꼬마유령')
    await client.change_presence(status=discord.Status.online, activity=game)



@client.event
async def on_message(message):
    if message.content.startswith('!안녕'):
        await message.channel.send('안녕')
    if message.content.startswith('!시발'):
        await message.channel.send('욕은나빠')
    if message.content.startswith('!꺼져'):
        await message.channel.send('미안해')
    if message.content.startswith('!사탕먹어'):
        await message.channel.send('좋아~~~')


access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
