import urllib
from urllib.request import urlopen
import os
from bs4 import BeautifulSoup
import lxml
import html
import requests

internetWasOff = True

class Parsing():
    def __init__(self):
        pass
    def RepeatURL(self,GetUrl):
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
    def Download(self,Name : str,URL : str):
        """
        Качает лолей
        """
        Lolies = []
        with open(f"./Resurses/loli/OldLoli2.txt","r") as file:
            for line in file.readlines():
                if line != "" and line != " " and line != "\n":
                    NameLoli = str(line).split("\n")[0]
                    Lolies.append(str(NameLoli))
        if Name not in Lolies:
            Lolies.append(Name)    
            with open(f"./Resurses/loli/OldLoli2.txt","w") as file:
                for loli in Lolies:
                    file.writelines(f"{loli}\n")
            DownloadFile = requests.get(URL, stream=True)
            with open(f"./Resurses/loli/{Name}","bw") as file:
                for chunk in DownloadFile.iter_content(30720):
                    file.write(chunk)
                    pass
                pass
    def AnimePicturesNet(self):
        print("AnimePicturesNet activity")
        url = "https://anime-pictures.net/pictures/view_posts/0?search_tag=Loli&order_by=date&ldate=3&lang=ru"
        request = requests.get(url)
        soup = BeautifulSoup(request.content,"html.parser")
        
        items = soup.find_all("img", class_ = "img_cp")

        for item in items:
            GetUrl = item.get("src") ; GetUrl = str(GetUrl)
            fstWord = list() ; fstWord.extend(str(GetUrl))
            URL = f"http://"
            DoIt = True
            for word in fstWord:
                if word == "/" and DoIt == True:
                    pass
                else:
                    URL += word
                    DoIt = False
            Name = str(GetUrl).split("/")[-1]
            self.Download(Name,URL)
        print("AnimePicturesNet not is activity")
    def wallpaper(self):
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
                self.Download(Name,Image)
            # print(url)
        print("wallpaper not is activity")
    
Parser = Parsing()
Parser.AnimePicturesNet()
Parser.wallpaper()