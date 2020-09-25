import requests
from bs4 import BeautifulSoup
import asyncio
import time
import codecs
import ast

def StrToDict(_str):
    NwDict = ast.literal_eval(f'{_str}') ; NwDict = dict(NwDict)
    return NwDict

class Gelbooru():
    """ ы """

    def __init__(self,
            Session : requests.Session,
            loop : asyncio.AbstractEventLoop = asyncio.get_event_loop(),
            FILE : str="Gelbooru.txt"):
        self.Session = Session
        self.headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36'}
        self.loop = loop
        self.Images = list()
        self.OldImages = list()
        self.FILE = FILE

    def Load(self):
        try:
            with codecs.open(self.FILE,"r",encoding='utf-8') as file:
                OldImages = StrToDict(str(file.readline()))
                self.OldImages = OldImages["Images"]
        except:
            self.OldImages = []

    def Save(self):
        with codecs.open(self.FILE,"w",encoding='utf-8') as file:
            file.write(str({"Images":self.OldImages}))

    class Tag():
        """ False = удалять если присуствует. True = искать """
        def __init__(self,Name : str, FindOrBan : bool):
            self.Name = Name
            self.Find = FindOrBan

    def Get(self,Function):
        while True:
            try:
                Image = self.Images[0]
                Function(Image)
                self.Images.remove(Image)
            except: pass
            time.sleep(0.5)
    def Login(self,UpdateData : dict = None):
        Options = "https://gelbooru.com/index.php?page=account&s=options"
        self.Session.get("https://gelbooru.com",headers=self.headers)
        data = {
            "tags": "",
            "cthreshold": "0",
            "pthreshold": "0",
            "my_tags": "",
            "safe_only": "on",
            "ad_type[]": "1",
            "ad_type[]": "3",
            "show_comments": "on",
            "searchPostView": "on",
            "submit": "Save Settings"}
        if isinstance(UpdateData,dict):
            data.update(UpdateData)
        self.Session.post(Options,data=data,headers=self.headers)
    
    def Fetch_Image(self,ID : int,Mode : "bytes or url"="url"):
        City = self.Session.get(f"http://gelbooru.com/index.php?page=post&s=view&id={ID}",headers=self.headers)
        Soup = BeautifulSoup(City.content,"lxml")
        try:
            Post = Soup.find("div",{"id":"note-container"}).next.next
        except: return
        Image = Post.get('src')
        if Mode.lower() == "url":
            self.Images.append(Image)
        elif Mode.lower() == "bytes":
            _Image = self.Session.get(f"http://gelbooru.com/index.php?page=post&s=view&id={ID}",headers=self.headers)
            self.Images.append(_Image.content)
    def __GetCity(self,City : requests.Response,BadTag : list):
        Soup = BeautifulSoup(City.content,"lxml")
        container = Soup.find('div',{"class":"thumbnail-container"})
        for Preview in container.find_all("div",{"class":"thumbnail-preview poopC"}):
            poopC = Preview.find("img",{"class":"poopC thumbnail-preview"})
            Tags = str(poopC.get("title")).split(" ")
            Clear = True
            for Tag in Tags:
                if Tag in BadTag:
                    Clear = False
            if Clear:
                ImageID = str(Preview.find('a').get('href')).split('&id=')[-1].split("&")[0]
                if ImageID not in self.OldImages:
                    self.OldImages.append(ImageID)
                    self.Fetch_Image(ImageID,"url")
    def Fetch_List(self,Tags : list,Count : int):
        FindTags = ""
        BadTag = []
        for tag in Tags:
            if tag.Find == True:
                FindTags += f"{tag.Name}+"
            else:
                BadTag.append(tag.Name)
        FindTags = FindTags[:-1:]
        for pid in range(Count):
            pid *= 42
            City = self.Session.get(f"https://gelbooru.com/index.php?page=post&s=list&tags={FindTags}&pid={pid}")
            self.__GetCity(City,BadTag)

    def __repr__(self):

        return f"Gelbooru > Count Loli = [{len(self.Images)}]"
        
    def Update(self,Tags : list,CheckEvery : float):
        FindTags = ""
        BadTag = []
        for tag in Tags:
            if tag.Find == True:
                FindTags += f"{tag.Name}+"
            else:
                BadTag.append(tag.Name)
        FindTags = FindTags[:-1:]
        while True:
            City = self.Session.get(f"https://gelbooru.com/index.php?page=post&s=list&tags={FindTags}&pid=0")
            self.__GetCity(City,BadTag)
            time.sleep(CheckEvery)