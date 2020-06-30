import discord
import ffmpeg
import BazaDate
import urllib
import time
import random
import wget
import PIL
import os
import ast
from bs4 import BeautifulSoup
import requests
import datetime
import asyncio
import codecs
from myConfg import *
from Functions2 import *

def is_internet():
    """
    Query internet using python
    :return:
    """
    
    try:
        urllib.request.urlopen('https://www.google.com', timeout=1)
        
        return True
    except urllib.error.URLError:
        return False

def InternetActive():
    client = MyClient()
    client.run(BazaDate.token)


class MyClient(discord.Client):
    async def on_ready(self):
        print("ready")
    async def on_message(self,message):
        self.Content = str(message.content)
        self.Channel = await self.fetch_channel(message.channel.id)
        self.Message = await self.Channel.fetch_message(message.id)
        self.Words = self.Content.split(" ")
        PlayerName = ""
        for part in str(message.author.name).split(" "):
            PlayerName += part
        
        self.Player = C_Player(PlayerName)
        Profile = self.Player.Profile()
        await self.Channel.send(" ",file=Profile)

def main():
    internetWasOff = True
    while True:
        if is_internet():
            if(internetWasOff == True):
                print("Internet is active")
                InternetActive()
                internetWasOff = False
        else:
            internetWasOff = True
        time.sleep(1)

if __name__ == "__main__":
    main()
