import requests
from bs4 import BeautifulSoup
import lxml
import time
import random
import asyncio
import os
import ast
import discord
import BazaDate
import urllib
from urllib.request import urlopen
import wget
internetWasOff = True

def StrToDict(**fields):
    """
    `str` : текст который нужно будет конвентировать в Dict
    """
    _str = str(fields.pop('str'))
    NwDict = ast.literal_eval(f'{_str}') ; NwDict = dict(NwDict)
    return NwDict

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
    async def DownloadLoli(self,url):
        headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36 OPR/65.0.3467.48'
            }
        GroupName = url.split("/")[-1]
        r = requests.get(url, headers = headers)
        soup = BeautifulSoup(r.content,"lxml") #html.parser
        try:
            page_cover_info = soup.find('div',{"class":"page_cover_info"})
            page_cover_image = page_cover_info.find('a',{"class":"page_cover_image"})
            page_top = page_cover_info.find("div",{"class":"page_top"})
            page_name = page_top.find("h1",{"class":"page_name"})
            NameWebHook = str(page_name.text)
            onclick = str(page_cover_image.get("onclick"))
            # print(onclick,end="\n\n\n")
            W = onclick.split(',"y":"')[-1]
            W = W.split('","')[0]
            Avatar_URL = ""
            for a in W.split("\/"):
                Avatar_URL += f"{a}/"
            Avatar_URL = Avatar_URL[:-1]
        except AttributeError: pass
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
                                File = discord.File(f"./Resurses/loli/{Name}",f"./Resurses/loli/{Name}")
                                Message = await self.LoliWebhook.send(
                                    content = "",
                                    file = File,
                                    username = NameWebHook,
                                    avatar_url = Avatar_URL
                                    )
                                os.remove(f"./Resurses/loli/{Name}")
                        except: 
                            print("error")
        print(f"Скачивание закончено ({GroupName})")
    async def on_ready(self):
        print(f"Logged on as , {self.user} MODULE : botLoli.py")
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
            "https://vk.com/loliland",
            "https://vk.com/lolianimeloli",
            "https://vk.com/tutloli",
            "https://vk.com/smsloli",
            "https://vk.com/kkaammiissaammaa",
            "https://vk.com/sleepsempai"
            ]
        Tasks = list()
        self.LoliChannel = await self.fetch_channel(578611164016017408)
        for Webhook in await self.LoliChannel.webhooks():
            if Webhook.name == "Лоля":
                self.LoliWebhook = Webhook
        while True:
            for image in os.listdir(f"./Resurses/loli/"):
                if image != "OldLolies":
                    self.WaitSending = True
                    File = discord.File(f"./Resurses/loli/{image}",f"./Resurses/loli/{image}")
                    await self.LoliWebhook.send(
                        content = " ",
                        file = File
                        )
                    print(f"{image} отправлено")
                    os.remove(f"./Resurses/loli/{image}")
            print("Скачивание лолей")
            for loliUrl in LoliCity:
                await self.DownloadLoli(loliUrl)
        
        async def on_message(self,message):
            if message.content == "EOQWIEOUWOJfasjfksafjaskljKLEJKLWEJQ":
                print("da")


while True:
    if is_internet():
        if(internetWasOff == True):
            print("Internet is active")
            InternetActive()
            internetWasOff = False
    else:
        internetWasOff = True
    time.sleep(1)