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
                Getting = Getis.find_all("a")
                # try:
                for Gets in Getting:
                    try:
                        UrlNew = str(Gets).split('data-src_big="')[1] #https://sun2.beeline-kz.
                        UrlNew = UrlNew.split("|")[0]
                        name = UrlNew.split("https://")[1] ; name = name.split("/")[-1]
                        # print(f" url {UrlNew} name : {name}")
                    except IndexError: pass
                    LoliNames = []
                    with open(f"./Resurses/loli/OldLoli.txt","r") as file:
                        for line in file.readlines():
                            if line != "\n":
                                LoliNames.append(line)
                        pass
                    # print(f" url {UrlNew} name : {Name}")
                    try:
                        try:
                            if f"{name}\n" not in LoliNames:
                                with open(f"./Resurses/loli/OldLoli.txt","w") as file:
                                    LoliNames.append(name)
                                    for loli in LoliNames:
                                        file.writelines(f"{str(loli)}\n")
                                DownloadFile = requests.get(UrlNew, stream=True)
                                with open(f"./Resurses/loli/{name}","bw") as file:
                                    for chunk in DownloadFile.iter_content(30720):
                                        file.write(chunk)
                                        pass
                                    pass
                                ImageLoli = Image.open(f"./Resurses/loli/{name}")
                                widht,height = ImageLoli.size
                                ResizeImageLoli = ImageLoli.resize((widht * 2,height * 2))
                                ResizeImageLoli.save(f"./Resurses/loli/{name}")
                                fileLoli = discord.File(f"./Resurses/loli/{name}",f"./Resurses/loli/{name}")
                                channel = self.get_channel(578611164016017408)
                                loliMessage = await channel.send(" ",file=fileLoli)
                                await loliMessage.add_reaction("👍")
                                await loliMessage.add_reaction("👎")
                                os.remove(f"./Resurses/loli/{name}")
                        except FileNotFoundError: pass
                    except UnboundLocalError: pass
                # except: pass
        time.sleep(15)

# def test(Ulr : str):
#     response = requests.get(Ulr)
#     soup = BeautifulSoup(response.content, "html.parser")
#     items = soup.findAll('div', class_ = "_post post page_block all own post--with-likes deep_active")
#     print(items)
#     # for item in items:
#     #     Title = item.find('span', class_ = "rel_date rel_date_needs_update").get_text(strip=True)
#     # pass
# print("start")
# test("https://vk.com/your.meow")
# print("end")
#https://www.youtube.com/watch?v=3DF6Zt2-GLw
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
            "https://vk.com/lolihouse16",
            "https://vk.com/loli_lovely",
            "https://vk.com/loliland"
            ]
        await CheckingVK(self,urls)
#         await LoliSend(self)



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