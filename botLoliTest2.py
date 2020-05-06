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

async def CheckingVK(self,Urls : list):
    while True:
        for __url_ in Urls:
            r = requests.get(__url_)
            soup = BeautifulSoup(r.content,"lxml") #html.parser

            div = soup.find_all("div")

            for Getis in div:
                Getting = Getis.get("style")

                if str(Getting) != "None":
                    try:
                        try:
                            url = str(Getting).split("url")[-1]
                            url = url.split("(")[1]
                            url = url.split(")")[0]
                            name = url.split("/")[-1]
                            # print(f"{url} name : {name}")
                            LoliNames = []
                            with open(f"./Resurses/loli/OldLoli.txt","r") as file:
                                for line in file.readlines():
                                    if line != "\n":
                                        LoliNames.append(line)
                                pass
                            if f"{name}\n" not in LoliNames:
                                with open(f"./Resurses/loli/OldLoli.txt","w") as file:
                                    LoliNames.append(name)
                                    for loli in LoliNames:
                                        file.writelines(f"{str(loli)}\n")
                                DownloadFile = requests.get(url, stream=True)
                                # print(f"{name} Скачивается")
                                with open(f"./Resurses/loli/{name}","bw") as file:
                                    for chunk in DownloadFile.iter_content(12288):
                                        file.write(chunk)
                                        pass
                                    pass
                                fileLoli = discord.File(f"./Resurses/loli/{name}",f"./Resurses/loli/{name}")
                                ImageLoli = Image.open(f"./Resurses/loli/{name}")
                                widht,height = ImageLoli.size
                                ResizeImageLoli = ImageLoli.resize(widht * 2,height * 2)
                                # print(f"{widht} x {height}")
                                ResizeImageLoli.save(f"./Resurses/loli/{name}")
                                # channel = self.get_channel(578611164016017408)
                                # await channel.send(" ",file=fileLoli)
                                # os.remove(f"./Resurses/loli/{name}")
                        except: pass
                        
                        
                    except requests.exceptions.InvalidSchema:
                        pass
        time.sleep(600)








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
        urls = [
            "https://vk.com/animelolki",
            "https://vk.com/your.meow",
            "https://vk.com/lolichan",
            "https://vk.com/cute_nekochan",
            "https://vk.com/lolyashii",
            "https://vk.com/lolides",
            "https://vk.com/miyarilove",
            "https://vk.com/lolidro4",
            "https://vk.com/aveloli",
            "https://vk.com/l0lihome",
            "https://vk.com/small09",
            "https://vk.com/lolifox_a",
            "https://vk.com/lolis_shelters",
            "https://vk.com/lolihouse16"
            ]
        await CheckingVK(self,urls)
        # await LoliSend(self)



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