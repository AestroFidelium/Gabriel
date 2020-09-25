import requests
from bs4 import BeautifulSoup
from bs4 import Tag
import codecs
import ast
import time
import random

def StrToDict(_str):
    NwDict = ast.literal_eval(f'{_str}') ; NwDict = dict(NwDict)
    return NwDict
class VK():
    class Group():
        def __init__(self,URL : str):
            self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36 OPR/65.0.3467.48'}
            self._Name = "..."
            self._Avatar = "..."
            self._Images = list()
            self.OldImages = list()
            self.URLName = URL.split('/')[-1]
            self.URL = URL

        @property
        def Images(self):
            return self._Images
        
        @property
        def Name(self):
            return self._Name
        
        @property
        def Avatar(self):
            return self._Avatar

        def __Load(self):
            try:
                with codecs.open(f"./Resurses/loli/{self.URLName}.txt","r",encoding='utf-8') as file:
                    OldImages = StrToDict(str(file.readline()))
                    self.OldImages = OldImages["Images"]
            except:
                self.OldImages = []
            
        def __Save(self):
            with codecs.open(f"./Resurses/loli/{self.URLName}.txt","w",encoding='utf-8') as file:
                file.write(str({"Images":self.OldImages}))
        
        def fetch_city(self):
            self.__Load()
            City = requests.get(self.URL,headers=self.headers)
            Soup = BeautifulSoup(City.content,"lxml")
            self._Name = Soup.find('h1',{'class':"page_name"})
            self._Avatar = Soup.find('img',{"class":"post_img"})
            PostsList = Soup.find("div",{"class":"wall_posts own mark_top"})
            for _Post in PostsList.find_all("div",{"class":"post"}):
                Images = list()
                WallInfo = _Post.find('div',{'class':'wall_text'})
                for Post in WallInfo.find_all('a',{"class":"page_post_thumb_wrap"}):
                    Image = str(Post.get('onclick'))
                    Image = Image.split(',"z":"')[-1].split('"')[0].replace('\/',"/")
                    Name = Image.split('/')[-1]
                    if Name.find('return') == -1: 
                        if Name not in self.OldImages:
                            self.OldImages.append(Name)
                            Images.append(Image)
                if len(Images) > 0:
                    self._Images.append(Images)
            self.__Save()

        def Updater(self):
            while True:
                time.sleep(1 + random.randint(1,25))
                self.__Load()
                City = requests.get(self.URL,headers=self.headers)
                Soup = BeautifulSoup(City.content,"lxml")
                self._Name = str(Soup.find('h1',{'class':"page_name"}).text)
                print(f"`{self._Name}`  : стартовал")
                self._Avatar = str(Soup.find('img',{"class":"post_img"}).get('src'))
                PostsList = Soup.find("div",{"class":"wall_posts own mark_top"})
                if isinstance(PostsList,Tag):
                    try:
                        for _Post in PostsList.find_all("div",{"class":"post"}):
                            Images = list()
                            WallInfo = _Post.find('div',{'class':'wall_text'})
                            for Post in WallInfo.find_all('a',{"class":"page_post_thumb_wrap"}):
                                Image = str(Post.get('onclick'))
                                Image = Image.split(',"z":"')[-1].split('"')[0].replace('\/',"/")
                                Name = Image.split('/')[-1]
                                if Name.find('return') == -1: 
                                    if Name not in self.OldImages:
                                        self.OldImages.append(Name)
                                        Images.append(Image)
                            if len(Images) > 0:
                                self._Images.append(Images)
                        self.__Save()
                    except BaseException as Error:
                        print(f"`{self._Name}`  : вызвал ошибку : {Error}")
                time.sleep(300 + random.randint(50,100))