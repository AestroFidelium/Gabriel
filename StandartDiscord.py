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
    pass
    async def on_ready(self):
        print(f"Logged on as , {self.user} MODULE : BotTest.py")
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