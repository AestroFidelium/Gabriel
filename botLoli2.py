import requests
from bs4 import BeautifulSoup
import time
import random
import asyncio
import os
import ast
import discord
import BazaDate
import urllib
from urllib.request import urlopen
import threading
import codecs
from LOLI import *
import datetime

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
    async def on_ready(self):
        print(f"Logged on as , {self.user} MODULE : botLoli2.py")
        LoliCitys = [
                "https://vk.com/animelolki",
                "https://vk.com/animenyanpasu",
                "https://vk.com/lolis_shelters",
                "https://vk.com/lolis_house",
                "https://vk.com/somuzu",
                "https://vk.com/henstorage",
                "https://vk.com/waifuhouse",
                "https://vk.com/laffey_chan",
                "https://vk.com/anime__gifs",
                "https://vk.com/random2d",
                "https://vk.com/islandloli",
                "https://vk.com/anime_nyaski",
                "https://vk.com/loli_clu",
                "https://vk.com/2dfox",
                "https://vk.com/loligirls",
                "https://vk.com/small09",
                "https://vk.com/high_quality_nya",
                "https://vk.com/sleepsempai",
                "https://vk.com/yourloliwaifu",
                "https://vk.com/kingdom_of_imaniti",
                "https://vk.com/lolichan",
                "https://vk.com/animect",
                "https://vk.com/xyi.community",
                "https://vk.com/lolikingdom",
                "https://vk.com/animeartweifu",
                "https://vk.com/loli190732355",
                "https://vk.com/ohota_loli",
                "https://vk.com/club185396253",
                "https://vk.com/smsloli",
                "https://vk.com/kkaammiissaammaa",
                "https://vk.com/lolis_heaven",
                "https://vk.com/pogladloli",
                "https://vk.com/club196074693",
                "https://vk.com/tutloli",
                "https://vk.com/lolyashii",
                "https://vk.com/v_mire_anime",
                "https://vk.com/lolides",
                "https://vk.com/miyarilove",
                "https://vk.com/aveloli",
                "https://vk.com/l0lihome",
                "https://vk.com/asura_arts",
                "https://vk.com/loliland",
                "https://vk.com/your.meow",
                "https://vk.com/cute_nekochan",
                "https://vk.com/lolidro4",
                "https://vk.com/loli_lovely",
                "https://vk.com/loliworld",
                "https://vk.com/lofipiic", 
                "https://vk.com/lolianimeloli",
                "https://vk.com/gikchan"]

        with requests.Session() as Session:
            self.Gelbooru = Gelbooru(Session,FILE=f"./Resurses/loli/Gelbooru.txt")
            self.Gelbooru.Login()
            self.Gelbooru.Load()
            Tags = [
                    [Gelbooru.Tag("flat_chest",True),
                    Gelbooru.Tag("panties",False),
                    Gelbooru.Tag("nude",False),
                    Gelbooru.Tag("underwear",False),
                    Gelbooru.Tag("swimsuit",False),
                    Gelbooru.Tag("string_bikini",False),
                    Gelbooru.Tag("string_panties",False),
                    Gelbooru.Tag("bra",False)],

                    [Gelbooru.Tag("small_breasts",True),
                    Gelbooru.Tag("panties",False),
                    Gelbooru.Tag("nude",False),
                    Gelbooru.Tag("underwear",False),
                    Gelbooru.Tag("swimsuit",False),
                    Gelbooru.Tag("string_bikini",False),
                    Gelbooru.Tag("string_panties",False),
                    Gelbooru.Tag("bra",False)]
                ]
            # for _tags in Tags:
                # threading.Thread(target=self.Gelbooru.Update,args=(_tags,30.0)).start()

        await asyncio.sleep(0.3)
        
        self.LoliChannel = await self.fetch_channel(578611164016017408)
        webhooks = await self.LoliChannel.webhooks()
        self.webhook = webhooks[0]
        Tasks = []
        # Tasks.append(self.loop.create_task(self.GelbooruSending()))
        self.LoliGroup = []
        for LoliCity in LoliCitys:
            _Group = VK.Group(LoliCity)
            threading.Thread(target=_Group.Updater,args=()).start()
            self.LoliGroup.append(_Group)
        await asyncio.sleep(30)
        Tasks.append(self.loop.create_task(self.VKSending()))
        asyncio.gather(*Tasks)
    
    async def on_message(self,message):
        if message.content == "FAJSFKASFLASFKSAJFA":
            pass

    async def GelbooruSending(self):
        WasIn = datetime.datetime.now()
        
        while True:
            Now = datetime.datetime.now()
            try:
                Image = self.Gelbooru.Images[0]
                Embed = discord.Embed(title='⁪',colour=discord.Colour(random.randint(0,16777215)))
                Embed.set_image(Image)
                await self.webhook.send(
                    embed = Embed,
                    content = " ",
                    avatar_url = "https://img2.gelbooru.com/samples/fc/59/sample_fc59e3e36ea3748f51cec4c965b0a44d.jpg",
                    username = "Gelbooru")
                Name = Image.split("/")[-1]
                print(f"{Name} отправлено. Осталось ({len(self.Gelbooru.Images)})")
                self.Gelbooru.Images.remove(Image)
                self.Gelbooru.Save()
                WasIn = datetime.datetime.now()
                await asyncio.sleep(2)
            except: 
                Different = Now - WasIn
                try: os.system("cls")
                except: os.system('clear')
                print(f"Logged on as , {self.user} MODULE : botLoli2.py")
                print(f"Нет изображений уже {Different}")
                await asyncio.sleep(30)

    async def VKSending(self):
        print("Начинаю отправлять")
        while True:
            for Group in self.LoliGroup:
                Embeds = list()
                for Image in Group.Images:
                    Color = random.randint(0,16777215)
                    Embed = discord.Embed(title=' ',colour=discord.Colour(Color))
                    for index,url in enumerate(Image):
                        Embed.set_image(url=url)
                        Embeds.append(Embed)
                        if index < len(Image) - 1:
                            Embed = discord.Embed(title=' ',colour=discord.Colour(Color))
                    Embeds.append(Embed)
                    Group.Images.remove(Image)
                for embed in Embeds:
                    await self.webhook.send(
                        embed = embed,
                        content = " ",
                        avatar_url = Group.Avatar,
                        username = Group.Name)
            await asyncio.sleep(10)
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