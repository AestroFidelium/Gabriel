import discord
import BazaDate
from discord import user
from discord import voice_client
import urllib
from urllib.request import urlopen
import time
import random
import datetime
import os
import wget
from PIL import Image, ImageDraw , ImageFont

MiniGameID = 629267102070472714 


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
    async def on_message(self,message):
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