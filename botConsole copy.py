import discord
from discord.ext import commands

TOKEN = "NjU2ODA4MzI3OTU0ODI1MjE2.Xik7NQ.pqnwoAWW_tDg25FVBzm5YLaVVw0"
client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print ('TYT')

@client.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    print(channel)
    print(type(channel))
    #await channel.connect()
    #await channel.connect()

@client.command()
async def leave(ctx):
  await ctx.voice_client.disconnect()
client.run(TOKEN)










