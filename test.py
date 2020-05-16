import discord
import BazaDate
from discord import user
import urllib
from urllib.request import urlopen
import time
import random
import datetime
import os
from bs4 import BeautifulSoup
import lxml
import requests
import os
from PIL import Image, ImageDraw , ImageFont
import botFunctions
from botFunctions import Gabriel
import asyncio

internetWasOff = True

async def TEST1(parameter_list):
    a = 0
    while a < 100:
        print(parameter_list)
        await asyncio.sleep(0.1)


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
        print(f"Logged on as , {self.user} MODULE : BotTest.py")
        _Gabriel = Gabriel()
        Config = _Gabriel.Config()
        await Config.Start(711132161444675595,self)
    async def on_message(self,message):
        pass



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