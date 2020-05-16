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

async def Download(self,Name : str,URL : str):
    """
    Качает лолей
    """
    Lolies = []
    with open(f"./Resurses/loli/OldLoli.txt","r") as file:
        for line in file.readlines():
            if line != "" and line != " " and line != "\n":
                NameLoli = str(line).split("\n")[0]
                Lolies.append(str(NameLoli))
    if Name not in Lolies:
        Lolies.append(Name)    
        with open(f"./Resurses/loli/OldLoli.txt","w") as file:
            for loli in Lolies:
                file.writelines(f"{loli}\n")
        DownloadFile = requests.get(URL, stream=True)
        with open(f"./Resurses/loli/{Name}","bw") as file:
            for chunk in DownloadFile.iter_content(30720):
                file.write(chunk)
                pass
            pass
        channel = self.get_channel(578611164016017408)
        fileLoli = discord.File(f"./Resurses/loli/{Name}",f"./Resurses/loli/{Name}")
        loliMessage = await channel.send(" ",file=fileLoli)
        await loliMessage.add_reaction("👍")
        await loliMessage.add_reaction("👎")
        os.remove(f"./Resurses/loli/{Name}")

def RepeatURL(GetUrl):
    URL = f"http://"
    DoIt = True
    fstWord = list() ; fstWord.extend(str(GetUrl))
    for word in fstWord:
        if word == "/" and DoIt == True:
            pass
        else:
            URL += word
            DoIt = False
    return URL
    
async def AnimePicturesNet(self):
    print("AnimePicturesNet activity")
    url = "https://anime-pictures.net/pictures/view_posts/0?search_tag=Loli&order_by=date&ldate=3&lang=ru"
    request = requests.get(url)
    soup = BeautifulSoup(request.content,"html.parser")
    
    items = soup.find_all("img", class_ = "img_cp")

    for item in items:
        GetUrl = item.get("src") ; GetUrl = str(GetUrl)
        fstWord = list() ; fstWord.extend(str(GetUrl))
        AnimePicturesNet_URL = f"http://"
        DoIt = True
        for word in fstWord:
            if word == "/" and DoIt == True:
                pass
            else:
                AnimePicturesNet_URL += word
                DoIt = False
        Name = str(GetUrl).split("/")[-1]
        await Download(self,Name,AnimePicturesNet_URL)
    print("AnimePicturesNet not is activity")

async def wallpaper(self):
    print("wallpaper activity")
    WallpaperUrl = "https://www.wallpaperflare.com/search?wallpaper=loli"
    request = requests.get(WallpaperUrl)
    soup = BeautifulSoup(request.content,"html.parser")
    
    items = soup.find_all("li")
    for item in items:
        url = item.find_all("img", class_ = "lazy")
        for URL in url:
            Image = URL.get("data-src")
            Name = str(Image).split("/")[-1]
            await Download(self,Name,Image)
        # print(url)
    print("wallpaper not is activity")


async def CheckingVK(self,Urls : list):
    while True:
        await AnimePicturesNet(self)
        await wallpaper(self)
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
        print(f"Logged on as , {self.user} MODULE : botLoli.py")
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