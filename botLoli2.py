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
from threading import Thread
import codecs

internetWasOff = True



class Group():
    def __init__(self,Name : str,URL : str,Avatar : str):
        self.Name = Name
        self.URL = URL
        self.Avatar = Avatar

class Post():
    def __init__(self,Content : str,Images : list,Tags : list):
        self.Content = f"{Content} "
        bad = ['discord.gg/',"https://"]
        for _ban in bad:
            self.Content = self.Content.replace(_ban,'')

        self.Images = Images
        self.Tags = Tags
    def __str__(self):
        return f"{self.Content} {self.Tags} {self.Images}"
class fetch_group(Thread):
    def __init__(self,URL : str,Webhook):
        Thread.__init__(self)
        self.Posts = list()
        self.URL = URL
        self.MainName = self.URL.split("/")[-1]
        try:
            with codecs.open(f"./Resurses/loli/OldLolies/{self.MainName}.txt","r",encoding='utf-8') as file:
                self.OldLolies = StrToDict(str(file.readline()))
                self.OldLolies = self.OldLolies['list']
        except: 
            with codecs.open(f"./Resurses/loli/OldLolies/{self.MainName}.txt","w",encoding='utf-8') as file:
                file.write(str({'list':[]}))
            self.OldLolies = []
        self.start()
    
    def run(self):
        try:
            headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36 OPR/65.0.3467.48'
                }

            MainCity = requests.get(self.URL,headers = headers)
            soup = BeautifulSoup(MainCity.content,"lxml")

            try: Title = soup.find('h1',{"class":"page_name"}).text
            except: Title = "Лоля"
            try: Informtion = soup.find('div',{"class":"line_value"}).text
            except: Informtion = "Отсуствует"
            page_cover_info = soup.find('div',{"class":"page_cover_info"})
            page_cover_image = page_cover_info.find('a',{"class":"page_cover_image"})
            onclick = str(page_cover_image.get("onclick"))
            W = onclick.split(',"y":"')[-1]
            W = W.split('","')[0]
            Avatar_URL = ""
            for a in W.split("\/"):
                Avatar_URL += f"{a}/"
            Avatar_URL = Avatar_URL[:-1]
            self.Group = Group(Title,Informtion,Avatar_URL)
 
            PostsList = soup.find("div",{"class":"wall_posts own mark_top"})
            self.Posts = list()
            for post in PostsList.find_all("div",{"class":"_post"}):
                try:
                    Tags = list()
                    try:
                        _Tags = post.find("div",{"class":"wall_post_text"})
                        for tag in _Tags.find_all("a"):
                            Tags.append(str(tag.text))
                    except: pass
                    try:
                        content = str(post.find("div",{"class":"wall_post_text"}).text)
                    except: content = ""

                    imagesList = list()
                    for images in post.find_all("div",{"class":"page_post_sized_thumbs"}):
                        for image in images.find_all('a'):
                            onclick = image.get("onclick")
                            onclick = str(onclick)
                            image = onclick.split(',"y":"')[-1]
                            image = image.split('"')[0]
                            # pylint: disable=anomalous-backslash-in-string
                            image = image.replace('\/',"/")
                            if str(image).find("https://") >= 0:
                                imagesList.append(image)
                    _Post = Post(content,imagesList,Tags)
                    if str(_Post) not in self.OldLolies:
                        self.Posts.append(_Post)
                        self.OldLolies.append(str(_Post))
                        for image in _Post.Images:
                            if str(image).find("https://") >= 0:
                                Name = image.split('/')[-1]
                                DownloadFile = requests.get(image, stream=True)
                                with open(f"./Resurses/loli/{Name}","bw") as file:
                                    for chunk in DownloadFile.iter_content(12288):
                                        file.write(chunk)
                        print(f"{self.Group.Name} новый пост")
                except: pass
            with codecs.open(f"./Resurses/loli/OldLolies/{self.MainName}.txt","w",encoding='utf-8') as file:
                file.write(str({"list":self.OldLolies}))
        except: pass






def StrToDict(_str : str):
    """
    `str` : текст который нужно будет конвентировать в Dict
    """
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
    async def on_ready(self):
        print(f"Logged on as , {self.user} MODULE : botLoli2.py")
        await self._Start()
    async def _Start(self):
        LoliCitys = [
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
            "https://vk.com/sleepsempai",
            "https://vk.com/somuzu",
            "https://vk.com/henstorage",
            "https://vk.com/waifuhouse",
            "https://vk.com/anime__gifs",
            "https://vk.com/laffey_chan",
            "https://vk.com/random2d",
            "https://vk.com/islandloli",
            "https://vk.com/anime_nyaski",
            "https://vk.com/loli_clu",
            "https://vk.com/2dfox",
            "https://vk.com/loligirls",
            "https://vk.com/loligirls",
            "https://vk.com/high_quality_nya",
            "https://vk.com/kingdom_of_imaniti",
            "https://vk.com/animect",
            "https://vk.com/animeartweifu",
            "https://vk.com/club185396253",
            "https://vk.com/ohota_loli",
            "https://vk.com/lolis_heaven",
            "https://vk.com/pogladloli",
            "https://vk.com/club196074693",
            "https://vk.com/loliworld",
            "https://vk.com/v_mire_anime",
            "https://vk.com/asura_arts",
            "https://vk.com/lofipiic",
            "https://vk.com/lolianimeloli",
            ]
        Tasks = list()
        self.LoliChannel = await self.fetch_channel(578611164016017408)
        webhooks = await self.LoliChannel.webhooks()
        webhook = webhooks[0]
        while True:
            LostedLolies = list()
            LostLoli = os.listdir(f"./Resurses/loli/")
            for Lost in LostLoli:
                if str(Lost) != "OldLolies":
                    LostedLolies.append(f"./Resurses/loli/{str(Lost)}")
            lenLostLolies = 0
            SendLostLolies = list()
            for loli in LostedLolies:
                lenLostLolies += 1
                name = str(loli).split("/")[-1]
                SendLostLolies.append(discord.File(loli,name))
                if lenLostLolies >= 10 and len(LostedLolies) >= 10:
                    lenLostLolies = 0
                    await webhook.send(
                        content = " ",
                        files = SendLostLolies)
                    
                    SendLostLolies.clear()
                elif len(LostedLolies) < 10:
                    try:
                        await webhook.send(
                            content = " ",
                            files = SendLostLolies)
                    except: pass
            for loli in LostedLolies:
                try:
                    os.remove(loli)
                except:
                    print("Лоля занята другим процессом, удаление невозможно")


            Groups = list()
            for url in LoliCitys:
                try:
                    _Group = fetch_group(url,webhook)
                    print(f"{_Group.MainName} все хорошо")
                    Groups.append(_Group)
                except:
                    print(f"{url} плохо")
            
            await asyncio.sleep(30)
            for group in Groups:
                try:
                    print(group.Group.Name)
                    for post in group.Posts:
                        RandomColor = random.randint(0,16777215)
                        Embeds = list()
                        group.Posts.remove(post)
                        TagsStr = ""
                        for tag in post.Tags:
                            TagsStr += f"{tag} "
                        for image in post.Images:
                            embed = discord.Embed(title="⁪",colour=discord.Colour(RandomColor))
                            embed.set_image(url=image)
                            embed.set_footer(text=TagsStr)
                            Name = image.split("/")[-1]
                            os.remove(f"./Resurses/loli/{Name}")
                            Embeds.append(embed)
                        if len(Embeds) > 0:
                            await webhook.send(
                                embeds = Embeds,
                                content = post.Content,
                                avatar_url = group.Group.Avatar,
                                username = group.Group.Name
                            )
                except: pass

        
        async def on_message(self,message):
            if message.content == "EOQWIEOUWOJfasjfksafjaskljKLEJKLWEJQ":
                print("da")

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