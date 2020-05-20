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
from botFunctions import BossForMoney
import asyncio

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

    async def OnMessage(self,message):
        pass
    
    async def AttackTheBoss(self,message):
        Command = str(message.content).split(" ")[0].upper()
        if Command == "SuperBossKill".upper():
            BossStats = self.Bossed.Read()
            Health = int(BossStats["Health"])
        
            Message = await message.channel.send(f"Текущее здоровье босса : (Много)")
            while True:
                BossStats = self.Bossed.Read()
                Health = int(BossStats["Health"])
                Health -= 10000
                await Message.edit(content=f"Текущее здоровье босса : {Health}")
                self.Bossed.Write(Health=Health)
                await asyncio.sleep(0.1)

    async def testSpam(self,Spam):
        a = 0
        while True:
            a += 1
            print(Spam)
            await asyncio.sleep(0.1)

    async def on_ready(self):
        print(f"Logged on as , {self.user} MODULE : test.py")
        Task2 = asyncio.create_task(self.testSpam("DADADADA"))
        asyncio.gather(Task2)

    async def on_message(self,message):
        if message.author == self.user:
            return
        self.Bossed = BossForMoney(message.channel.guild.name)
        # Bossed.Create(1000000)
        task1 = asyncio.create_task(self.OnMessage(message))
        task2 = asyncio.create_task(self.AttackTheBoss(message))
        print("Работает")
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