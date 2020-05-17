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

async def ConfigOpen(self,Setting : dict):
    Main = Image.open(f"./Resurses/Configs/Main2.png")
    Okay = Image.open(f"./Resurses/Configs/Okay.png")
    Save = f"./Resurses/Configs/ConfigSettings.png"
    Chat = str(Setting["Chat"])
    Game = str(Setting["Game"])
    Rooms = str(Setting["Rooms"])
    if Chat == "ONLINE":
        area = (648,180)
        Main.paste(Okay.convert('RGB'), area, Okay)
    if Game == "ONLINE":
        area = (648,423)
        Main.paste(Okay.convert('RGB'), area, Okay)
    if Rooms == "ONLINE":
        area = (648,677)
        Main.paste(Okay.convert('RGB'), area, Okay)
    Main = Main.save(Save)
    file = discord.File(Save,Save)
    return file

async def OnMessage(self,message):
    print(message)

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
        print(f"Logged on as , {self.user} MODULE : test.py")

    async def on_message(self,message):
        if message.author == self.user:
            return
        task1 = asyncio.create_task(OnMessage(self,message))
        task2 = asyncio.create_task(TEST1("ara"))
        asyncio.gather(task1,task2)



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