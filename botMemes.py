import requests
from bs4 import BeautifulSoup
import lxml
import time
import random
import asyncio
import urllib
import os
import ast
import discord
import BazaDate
import wget
import json
import codecs
internetWasOff = True

def StrToDict(str):
    """
    `str` : текст который нужно будет конвентировать в Dict
    """
    NwDict = ast.literal_eval(f'{str}') ; NwDict = dict(NwDict)
    return NwDict

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
    
    async def Parser(self):
        token = BazaDate.VKToken
        domain = "the_gates_of_orgrimmar"
        try:
            os.makedirs(f"./Resurses/VK/Memes/{domain}/")
            with codecs.open(f"./Resurses/VK/Memes/{domain}/Main.txt","w",encoding="utf-8") as file:
                _Main = {
                    "Posts" : []
                }
                file.write(str(_Main))
                OldPosts = list()
        except:
            with codecs.open(f"./Resurses/VK/Memes/{domain}/Main.txt","r",encoding="utf-8") as file:
                _OldPosts = StrToDict(str(file.readline()))
                OldPosts = _OldPosts["Posts"]
        
        count = 2
        key = f"https://api.vk.com/method/wall.get?domain={domain}&count={count}&filter=owner&extended=1&access_token={token}&v=5.110"
        Channel = await self.fetch_channel(738275633825710130)
        Webhook = await Channel.webhooks()
        Webhook = Webhook[0]
        with requests.Session() as Session:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36 OPR/65.0.3467.48'
            }
            Response = Session.get(key,headers=headers)
            Json = Response.json()
            Posts = Json['response']
            class Post():
                def __init__(self,text : str,photos : list,Author : str,GroupName : str,GroupAvatar : str):
                    self.text = text[:2048:]
                    self.photos = photos
                    self.Author = Author
                    self.GroupName = GroupName
                    self.GroupAvatar = GroupAvatar
                def __str__(self):
                    return f"{self.text} {self.photos} {self.Author}"
            PostsClass = list()
            for _Post in Posts['items']:
                text = _Post['text']
                attachments = _Post['attachments']
                PhotosURL = list()
                for attachment in attachments:
                    _type = attachment["type"]
                    if str(_type) == "photo":
                        photo = attachment['photo']
                        sizes = photo['sizes']
                        for size in sizes:
                            sizeType = size['type']
                            if str(sizeType) == "w":
                                PhotosURL.append(size["url"])
                profile = Posts["profiles"][0]
                AuthorName = profile['first_name']
                AuthorName += " "
                AuthorName += profile['last_name']
                group = Posts['groups'][0]
                GroupName = group['name']
                GroupAvatar = group["photo_200"]
                C_Post = Post(text,PhotosURL,AuthorName,GroupName,GroupAvatar)
                if C_Post.__str__() not in OldPosts:
                    OldPosts.append(str(C_Post))
                    PostsClass.append(C_Post)
                else:
                    print("Старый пост")
            Iter = iter(PostsClass)
            for Poster in Iter:
                Embeds = list()
                RandomColor = random.randint(0,16777215)
                Embed = discord.Embed(
                    title="Новая запись",
                    description=Poster.text,
                    colour=discord.Colour(RandomColor),
                    url=f"https://vk.com/{domain}")
                URL = Poster.photos[0]
                Embed.set_image(url=URL)
                Poster.photos.remove(URL)
                Embed.set_footer(text=Poster.Author)
                Embeds.append(Embed)
                for URL in Poster.photos:
                    Embed = discord.Embed(
                        title="⁯⁬⁬⁫⁫⁫⁫⁫⁫⁫⁫⁪⁪⁪⁪⁪⁪⁪⁪⁪⁪ ‫‫‫‫‪",
                        colour=discord.Colour(RandomColor))
                    Embed.set_image(url=URL)
                    Embed.set_footer(text=Poster.Author)
                    if len(Embeds) < 10:
                        Embeds.append(Embed)
                await Webhook.send(
                    embeds=Embeds,
                    avatar_url=Poster.GroupAvatar,
                    username = Poster.GroupName
                    )
            with codecs.open(f"./Resurses/VK/Memes/{domain}/Main.txt","w",encoding="utf-8") as file:
                _Main = {
                    "Posts" : OldPosts
                }
                file.write(str(_Main))
    async def on_ready(self):
        MODULE = str(__file__).split("/")[-1]
        print(f"Logged on as , {self.user} MODULE : {MODULE}")
        await self.Parser()
        
        
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
