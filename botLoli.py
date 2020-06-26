import requests
from bs4 import BeautifulSoup
import lxml
import time
import random
import asyncio
import os
#pylint: disable=unused-wildcard-import
from myConfg import *
import discord
import BazaDate
import urllib
from urllib.request import urlopen
import wget
internetWasOff = True

def is_internet():
    """
    Query internet using python
    :return:
    """
    try:
        urlopen('https://www.google.com', timeout=1)
        
        return True
    except urllib.error.URLError:
        return False
def InternetActive():
    client = MyClient()
    client.run(BazaDate.token)
class MyClient(discord.Client):
    async def SendLolies(self):
        while True:
            print("Отправляет")
            for image in os.listdir(f"./Resurses/loli/"):
                if image != "OldLolies":
                    try:
                        print(f"{image}")
                        File = discord.File(f"./Resurses/loli/{image}",f"./Resurses/loli/{image}")
                        Message = await self.LoliWebhook.send(
                            content = "", file = File
                            )
                        print(f"{image} отправлено")
                        os.remove(f"./Resurses/loli/{image}")
                        # Message_ = await self.LoliChannel.fetch_message(Message.id)
                        # await Message_.add_reaction('👍')
                        # await Message_.add_reaction('👎')
                    except: print("error in sending")
            await asyncio.sleep(60)
    async def DownloadLoli(self,url):
        headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36 OPR/65.0.3467.48'
            }
        GroupName = url.split("/")[-1]
        while True:
            r = requests.get(url, headers = headers)
            soup = BeautifulSoup(r.content,"lxml") #html.parser
            for div in soup.find_all("div",{"class":"_post_content"}):
                for wall_text in div.find_all('div',{"class":"wall_text"}):
                    for content in wall_text.find_all("div",{"class":"page_post_sized_thumbs"}):
                        for _content in content:
                            onclick = _content.get("onclick")
                            onclick = str(onclick)
                            x = onclick.split('{"temp":')[-1]
                            x = x.split(',"queue":1}')[0]
                            try:
                                x = StrToDict(str=x)
                                x = x['y']
                                Name = x.split("/")[-1]
                                url = ""
                                #pylint: disable=anomalous-backslash-in-string
                                for word in x.split("\/"):
                                    url += f"{word}/"
                                url = url[:-1]
                                DownloadFile = requests.get(url, stream=True)
                                try:
                                    with open(f"./Resurses/loli/OldLolies/{GroupName}_OldLoli.txt","r") as file:
                                        Lolies = list()
                                        for line in file.readlines():
                                            if line != '\n':
                                                line = line.split("\n")[0]
                                                Lolies.append(line)
                                except FileNotFoundError:
                                    with open(f"./Resurses/loli/OldLolies/{GroupName}_OldLoli.txt","w"): pass
                                    Lolies = list()
                                if Name not in Lolies:
                                    print(url)
                                    Lolies.append(Name)
                                    with open(f"./Resurses/loli/{Name}","bw") as file:
                                        for chunk in DownloadFile.iter_content(12288):
                                            file.write(chunk)
                                    with open(f"./Resurses/loli/OldLolies/{GroupName}_OldLoli.txt","w") as file:
                                        for loli in Lolies:
                                            file.write(str(f"{loli}\n"))
                            except: print("error")
                            await asyncio.sleep(0.01)
            await asyncio.sleep(10)
    async def on_ready(self):
        print(f"Logged on as , {self.user} MODULE : botLoli.py")
        # for file in os.listdir("./Resurses/loli/"):
        #     txt = file.split(".")[-1]
        #     if txt != "txt" and file != "OldLolies":
        #         os.remove(f"./Resurses/loli/{file}")
        OurGuild = await self.fetch_guild(419879599363850251)
        self.LoliChannel = await self.fetch_channel(578611164016017408)
        for Webhook in await self.LoliChannel.webhooks():
            if Webhook.name == "Лоля":
                self.LoliWebhook = Webhook
        LoliCity = [
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
        Tasks = list()
        for loliUrl in LoliCity:
            task = asyncio.create_task(self.DownloadLoli(loliUrl))
            Tasks.append(task)
        asyncio.gather(*Tasks)
        await self.SendLolies()


while True:
    if is_internet():
        if(internetWasOff == True):
            print("Internet is active")
            InternetActive()
            internetWasOff = False
    else:
        internetWasOff = True
    time.sleep(1)