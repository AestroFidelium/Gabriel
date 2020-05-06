import discord
import BazaDate
from discord import user
import urllib
from urllib.request import urlopen
import time
import random
import wget
import botFunctions as Functions
from PIL import Image, ImageDraw , ImageFont

Resurses = "./Resurses/"

internetWasOff = True

def is_internet():
    """
    Query internet using python
    :return:
    """
    
    try:
        urlopen('https://www.google.com', timeout=1)
        
        return True
    except urllib.error.URLError as Error:
        print(Error)
        return False
def InternetActive():
    client = MyClient()
    client.run(BazaDate.token)
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
        # await Functions.GetPermissions(self)
        _channel = await self.fetch_channel(691750825030320218)
        Banner = discord.File('./Resurses/WelcomeFrst.png',"Banner.png")
        Welcome = discord.File('./Resurses/Welcome.png',"Welcome.png")
        await _channel.send(" ",file=Banner)
        await _channel.send(" ",file=Welcome)
    async def on_message(self, message):
    # don't respond to ourselves
        if message.author == self.user:
            pass
        print(message.content)
        


InternetActive()

while True:
    time.sleep(1)
    if is_internet():
        if(internetWasOff == True):
            print("Internet is active")
            InternetActive()
            internetWasOff = False
    else:
        print("Internet disconnected")
        internetWasOff = True