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
    def __init__(self,_Group : Group):
        Thread.__init__(self)
        self.Posts = list()
        self.Group = _Group
        self.Posts = list()
        Replaces = ['/',"|","Ɛ",":"]
        self.MainName = self.Group.Name
        for replace in Replaces:
            self.MainName = self.MainName.replace(replace,"")
        self.NewLolies = 0
        try:
            with codecs.open(f"./Resurses/loli/OldLolies/{self.MainName}.txt","r",encoding='utf-8') as file:
                self.OldLolies = StrToDict(str(file.readline()))
                self.OldLolies = self.OldLolies['list']
        except: 
            with codecs.open(f"./Resurses/loli/OldLolies/{self.MainName}.txt","w",encoding='utf-8') as file:
                file.write(str({'list':[]}))
            self.OldLolies = []
        print(f"[{self.Group.Name}] готова")
        self.start()
    def run(self):
        be = False
        try:
            headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36 OPR/65.0.3467.48'
                }

            MainCity = requests.get(self.Group.URL,headers = headers)
            soup = BeautifulSoup(MainCity.content,"lxml")

            PostsList = soup.find("div",{"class":"wall_posts own mark_top"})
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
                        be = True
                        self.Posts.append(_Post)
                        self.OldLolies.append(str(_Post))
                        self.NewLolies += 1
                except: pass
            if be == True: print(f"{self.Group.Name} новых постов ({self.NewLolies})")
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
        await self._Start2()

    
    async def _Start2(self):
        LoliCitys = [
            Group(
                Name="Empire of Loli (Аниме / Anime)",
                URL="https://vk.com/animelolki",
                Avatar="https://sun9-60.userapi.com/c841338/v841338031/4b30c/HTdH8Nh-efw.jpg"),
            Group(
                Name="Nyanpasu",
                URL="https://vk.com/animenyanpasu",
                Avatar="https://sun9-73.userapi.com/c834203/v834203245/edfe4/WfJX21y_Imw.jpg"),
            Group(
                Name="Kawaii Carnival",
                URL="https://sun9-73.userapi.com/c834203/v834203245/edfe4/WfJX21y_Imw.jpg",
                Avatar="https://sun9-38.userapi.com/c836227/v836227624/69092/3GuZeuLCGOk.jpg"),
            Group(
                Name="Loli's Shelters | Приют Лолей",
                URL="https://vk.com/lolis_shelters",
                Avatar="https://sun9-24.userapi.com/7Bv3vXr5fc9B9iGZePemJuS0CCbd-tpT3UsKcw/YwUpUNfbL4s.jpg"),
            Group(
                Name="Лолин дом",
                URL="https://vk.com/lolis_house",
                Avatar="https://sun9-51.userapi.com/c836333/v836333479/50b9c/ZK7H7qb2Fbg.jpg"),
            Group(
                Name="Ɛ: Zusomu :3",
                URL="https://vk.com/somuzu",
                Avatar="https://sun9-47.userapi.com/nF90X3ia_NBv25-n1HFVYsUvRfr6iR2DAiDiIA/LgYzes8CJt8.jpg"),
            Group(
                Name="ХХранилище | Внешнее",
                URL="https://vk.com/henstorage",
                Avatar="https://sun9-4.userapi.com/c830308/v830308116/163749/LcwwiQSUe-E.jpg"),
            Group(
                Name="Waifu House",
                URL="https://vk.com/waifuhouse",
                Avatar="https://sun9-62.userapi.com/c855616/v855616264/55ae0/hBEItTl8MtQ.jpg"),
            Group(
                Name="Laffey-chan (◕‿◕)",
                URL="https://vk.com/laffey_chan",
                Avatar="https://sun9-35.userapi.com/c856020/v856020456/236cf6/cnw0zfdehow.jpg"),
            Group(
                Name="Denforz",
                URL="https://vk.com/anime__gifs",
                Avatar="https://sun9-66.userapi.com/c857020/v857020273/10eda5/4lWbGOmfbng.jpg"),
            Group(
                Name="2D Random",
                URL="https://vk.com/random2d",
                Avatar="https://sun9-58.userapi.com/c854428/v854428179/1e2375/y5S1Cal-zIs.jpg"),
            Group(
                Name="Loli Island",
                URL="https://vk.com/islandloli",
                Avatar="https://sun9-20.userapi.com/hSWjmaKGts5eQixoSyf0NLUXA1xwH_b_cpBgiQ/vf0iszs2Kss.jpg"),
            Group(
                Name="Аниме Няшки",
                URL="https://vk.com/anime_nyaski",
                Avatar="https://sun9-17.userapi.com/c637916/v637916387/335ae/DnEE0eWtJas.jpg"),
            Group(
                Name="Loli club",
                URL="https://vk.com/loli_clu",
                Avatar="https://sun9-64.userapi.com/c857016/v857016428/1e2207/dub-d_06xk0.jpg"),
            Group(
                Name="2DFox",
                URL="https://vk.com/2dfox",
                Avatar="https://sun9-42.userapi.com/c841328/v841328160/74dac/bweCoIFIcPE.jpg"),
            Group(
                Name="LoliGirls",
                URL="https://vk.com/loligirls",
                Avatar="https://sun9-42.userapi.com/3qHzVlsX0CGzJ0KhgO5yQ4ZBBEGrnlj4qtrnbQ/gPdumPCTRmw.jpg"),
            Group(
                Name="LoliCity",
                URL="https://vk.com/small09",
                Avatar="https://sun9-52.userapi.com/KhLAzSFdAy2BAEfBnY6iVobExcEWv3S1T5V-Kw/c_8HFsU4O1Q.jpg"),
            Group(
                Name="Качественный контент ня :3",
                URL="https://vk.com/high_quality_nya",
                Avatar="https://sun9-60.userapi.com/Z6Wf64FjBWzq6kUULrm4N_3WQsGHC63_Gbzh9g/sBWjiT_9GuY.jpg"),
            Group(
                Name="комнатка твоих снов",
                URL="https://vk.com/sleepsempai",
                Avatar="https://sun9-4.userapi.com/H5JNdh9scPbRQPwTOchOfHt1Pa5NGTcIVdl1Vg/glMwaK0dR7Y.jpg"),
            Group(
                Name="Роскомлоли",
                URL="https://vk.com/yourloliwaifu",
                Avatar="https://sun9-29.userapi.com/c857228/v857228899/148023/8iajyi5JKy8.jpg"),
            Group(
                Name="Kingdom of Imaniti (KOI)",
                URL="https://vk.com/kingdom_of_imaniti",
                Avatar="https://sun1.beeline-kz.userapi.com/c857032/v857032131/1f53ec/2oebOsbQhcw.jpg"),
            Group(
                Name="Lolichan",
                URL="https://vk.com/lolichan",
                Avatar="https://sun1.beeline-kz.userapi.com/c841131/v841131185/26d88/pubIFCompgs.jpg"),
            Group(
                Name="Аnime aesthetics /аниме эстетика",
                URL="https://vk.com/animect",
                Avatar="https://sun9-73.userapi.com/GYXaBwHcGkGblEy4Ba8qM7LdamVmYzWKEJRQ-Q/H6-KfTQ_ilw.jpg"),
            Group(
                Name="XYI",
                URL="https://vk.com/xyi.community",
                Avatar="https://sun9-53.userapi.com/c856524/v856524299/1b0ce9/k9OMFlKZS00.jpg"),
            Group(
                Name="Милые аниме девочки",
                URL="https://vk.com/lolikingdom",
                Avatar="https://sun9-52.userapi.com/fwhao-U08FN7HCW6l4DojEqimxGCh51YNFphnw/VqjEDmNrgpA.jpg"),
            Group(
                Name="Domik Weifu | Anime Arts",
                URL="https://vk.com/animeartweifu",
                Avatar="https://sun9-43.userapi.com/tC097eqvdfYFUiOGhm3qoy31x-DXo2iEjRd-Pg/-v5HsHdz2rA.jpg"),
            Group(
                Name="loli",
                URL="https://vk.com/loli190732355",
                Avatar="https://sun9-7.userapi.com/p4EMsKlCgRsjI92alCElDZZ5s9ya7FOhlxr8Zg/rzKlGOWsuUM.jpg"),
            Group(
                Name="2D девочки",
                URL="https://vk.com/ohota_loli",
                Avatar="https://sun9-22.userapi.com/c857132/v857132579/6fc7c/FTiWjDbgkP0.jpg"),
            Group(
                Name="Anime Kawaii",
                URL="https://vk.com/club185396253",
                Avatar="https://sun9-76.userapi.com/HpzzxLfjmq9yFLZ6pWlevuMRgQecg1I5_nRoQQ/mbpsuSLAwHg.jpg"),
            Group(
                Name="Милые лольки онлайн без смс",
                URL="https://vk.com/smsloli",
                Avatar="https://sun9-52.userapi.com/c857328/v857328600/b0339/VElz8DxeHd4.jpg"),
            Group(
                Name="Я счастлив, А ещё я лжец..",
                URL="https://vk.com/kkaammiissaammaa",
                Avatar="Я счастлив, А ещё я лжец.."),
            Group(
                Name="Loli's heaven",
                URL="https://vk.com/lolis_heaven",
                Avatar="https://sun9-18.userapi.com/c853520/v853520957/333ef/p2qDOzuZeXU.jpg"),
            Group(
                Name="Погладь лолю",
                URL="https://vk.com/pogladloli",
                Avatar="https://sun9-45.userapi.com/1i9Y1xeIikfQu4jPJKTgePtV2Jj27fAosTxRlQ/N75lPm76HFw.jpg"),
            Group(
                Name="Loli",
                URL="https://vk.com/club196074693",
                Avatar="https://sun9-17.userapi.com/J8NfEEqrb3Z3ijrM8aYa-kwdOxaePB7mt_AjNw/s-WioD7g-ME.jpg"),
            Group(
                Name="братик, тут лоли",
                URL="https://vk.com/tutloli",
                Avatar="https://sun9-61.userapi.com/uk_dLYc2M-RxK1UM_uosdMSjT01iC9J2b2jURQ/s0cxGEaBd-Y.jpg"),
            Group(
                Name="Lolicon",
                URL="https://vk.com/lolyashii",
                Avatar="https://sun9-71.userapi.com/c848520/v848520580/2e106/o-z0TIWzIHs.jpg"),
            Group(
                Name="ANIME WORLD",
                URL="https://vk.com/v_mire_anime",
                Avatar="https://sun9-75.userapi.com/c850520/v850520093/1ab040/Bt_5GJrr24Y.jpg"),
            Group(
                Name="loli desu",
                URL="https://vk.com/lolides",
                Avatar="https://sun9-35.userapi.com/c857216/v857216026/50d03/V6GGWKFlh-E.jpg"),
            Group(
                Name="nekochan",
                URL="https://vk.com/miyarilove",
                Avatar="https://sun9-70.userapi.com/Ea01t_KlFee3foTA1QrI3pKMUC80QQmIV7lzSA/DzgURMSYtNQ.jpg"),
            Group(
                Name="AVE LOLI",
                URL="https://vk.com/aveloli",
                Avatar="https://sun9-33.userapi.com/c851024/v851024988/16b58b/WbCxdOZCmIc.jpg"),
            Group(
                Name="Loli home",
                URL="https://vk.com/l0lihome",
                Avatar="https://sun9-32.userapi.com/c853424/v853424959/111017/gJ5Q11w0u1g.jpg"),
            Group(
                Name="Asura Arts",
                URL="https://vk.com/asura_arts",
                Avatar="https://sun9-1.userapi.com/c853424/v853424411/10b5f6/cuQ1JFTLB-M.jpg"),
            Group(
                Name="Loliland",
                URL="https://vk.com/loliland",
                Avatar="https://sun9-43.userapi.com/c206716/v206716745/8fcfc/msDb2AyshkI.jpg"),
            Group(
                Name="meowchan",
                URL="https://vk.com/your.meow",
                Avatar="https://sun9-49.userapi.com/c850628/v850628303/1db221/4chfsBbOWGc.jpg"),
            Group(
                Name="Cute Neko",
                URL="https://vk.com/cute_nekochan",
                Avatar="https://sun9-39.userapi.com/c854020/v854020826/23409a/1aBGXZkjZAk.jpg"),
            Group(
                Name="Доски для твоего забора",
                URL="https://vk.com/lolidro4",
                Avatar="https://sun9-64.userapi.com/c853524/v853524410/a3931/6jCauPFi8Tc.jpg"),
            Group(
                Name="Lovely Loli | Милые Лоли",
                URL="https://vk.com/loli_lovely",
                Avatar="https://sun9-54.userapi.com/c845418/v845418314/1b50fd/-LHfu5x2m2o.jpg"),
            Group(
                Name="LoliWorld",
                URL="https://vk.com/loliworld",
                Avatar="https://sun9-51.userapi.com/c851336/v851336168/18c6cd/iFo2i-qBTM8.jpg"),
            Group(
                Name="lo-fi pic",
                URL="https://vk.com/lofipiic",
                Avatar="https://sun9-17.userapi.com/ApVCbJe9NOhKEkztx61f_sWRwDwoVSQltgzKCA/W-BPpRSutkQ.jpg"),
            Group(
                Name="Anime | Loli",
                URL="https://vk.com/lolianimeloli",
                Avatar="https://sun9-32.userapi.com/c206824/v206824792/c7a3/8gPMG07VcmE.jpg"),
            Group(
                Name="GIK-CHan",
                URL="https://vk.com/gikchan",
                Avatar="https://sun9-19.userapi.com/c856016/v856016129/1de287/r6IkqHDYxyU.jpg")
            ]
        Groups = list()
        self.LoliChannel = await self.fetch_channel(578611164016017408)
        webhooks = await self.LoliChannel.webhooks()
        webhook = webhooks[0]
        
        while True:
            try:
                for group in LoliCitys:
                    Groups.append(fetch_group(group))
                    DeleteLolies = list()
                for group in Groups:
                    for post in group.Posts:
                        RandomColor = random.randint(0,16777215)
                        Embeds = list()
                        TagsStr = ""
                        for tag in post.Tags:
                            TagsStr += f"{tag} "
                        for image in post.Images:
                            embed = discord.Embed(title="⁪",colour=discord.Colour(RandomColor))
                            embed.set_image(url=image)
                            embed.set_footer(text=TagsStr)
                            Embeds.append(embed)
                        if len(Embeds) > 0:
                            await webhook.send(
                                embeds = Embeds,
                                content = post.Content,
                                avatar_url = group.Group.Avatar,
                                username = group.Group.Name
                            )
                            group.Posts.remove(post)
                await asyncio.sleep(10)
            except:
                await asyncio.sleep(30)

    
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
            try:
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
                
                await asyncio.sleep(100)
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
                await asyncio.sleep(10)
            except: pass


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