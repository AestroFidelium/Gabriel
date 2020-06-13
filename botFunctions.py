import discord
import BazaDate
from discord import user
import urllib
from urllib.request import urlopen
import time
import random
import wget
from PIL import Image, ImageDraw , ImageFont
import BotInisializator
import datetime
import ast
import os
import asyncio
import codecs

Resurses = "./Resurses/"
StandartURL = "https://pbs.twimg.com/profile_images/589387776740593664/24AVkUCB_400x400.jpg"

StandartURLBackGround = "https://sun2.beeline-kz.userapi.com/x9atyMKIrNqaScUzfzQnzSPXI3cJeGKBaMJrCQ/YC2g7RI4jxI.jpg"

internetWasOff = True
IntCurExp = 0
IntCurLvl = 0
IntMaxHealth = 0
IntCurHealth = 0
IntMaxDamage = 0
Description = ""
ln = "\n"
FarmExp = ""

class Error(BaseException):
    pass
class Error_FutureMessageDef(Error):
    pass
class Error_CreateItem(Error):
    pass

class LastItem(Error):
    pass

class Gabriel():
    """
    Габриэль.

    Отвечает за всю настройку Габриэль, на сервере
    """
    def __init__(self):
        pass
    class Config():
        def __init__(self):
            self.Online = "Online"
            self.Offline = "Offline"
        async def ConfigOpen(self,Setting : dict):
            Main = Image.open(f"./Resurses/Configs/Main2.png")
            Okay = Image.open(f"./Resurses/Configs/Okay.png")
            Save = f"./Resurses/Configs/ConfigSettings.png"
            Chat = str(Setting["Chat"])
            Game = str(Setting["Game"])
            Rooms = str(Setting["Rooms"])
            if Chat == "ONLINE":
                area = (648,180)
                Main.paste(Okay.convert('RGB'), area, Okay)
            if Game == "ONLINE":
                area = (648,423)
                Main.paste(Okay.convert('RGB'), area, Okay)
            if Rooms == "ONLINE":
                area = (648,677)
                Main.paste(Okay.convert('RGB'), area, Okay)
            Main = Main.save(Save)
            file = discord.File(Save,Save)
            return file
        class NotOnlineOrOffline(Error):
            pass
        async def Start(self,server : int,Client):
            """
            Прогреть конфиг
            """
            self.Client = Client
            self.server = await Client.fetch_guild(server)
            self.direct = f"./Servers/{self.server.name}"
            try:
                self.CreateServer()
                with codecs.open(f"{self.direct}/ChatConfig.txt","w",encoding='utf-8', errors='ignore') as file:
                # with open(f"{self.direct}/ChatConfig.txt","w") as file:
                    NewDict = {
                        "Activity" : [],
                        "Status" : "PRIVATE"
                    }
                    file.write(str(NewDict))
                with codecs.open(f"{self.direct}/RoomsConfig.txt","w",encoding='utf-8', errors='ignore') as file:
                # with open(f"{self.direct}/RoomsConfig.txt","w") as file:
                    NewDict = {
                        "Activity" : []
                    }
                    file.write(str(NewDict))
                with codecs.open(f"{self.direct}/Words.txt","w",encoding='utf-8', errors='ignore') as file:
                # with open(f"{self.direct}/Words.txt","w") as file:
                    file.write("")
            except FileExistsError:
                pass #Старый сервер
        def Read(self,serverName : str):
            try:
                with codecs.open(f"./Servers/{serverName}/Config.txt","r"
                ,encoding='utf-8', errors='ignore') as file:
                # with open(f"./Servers/{serverName}/Config.txt","r") as file:
                    return StrToDict(str=str(file.readline()))
            except FileNotFoundError:
                Modules = {
                    "CHAT" : "ONLINE",
                    "GAME" : "ONLINE",
                    "ROOMS" : "ONLINE"
                }
                return Modules
        
        def _CheckModule(self,name,fields):
            Possible = ["ONLINE","OFFLINE"]
            try:
                Module = str(fields[name])
                if Module not in Possible:
                    raise self.NotOnlineOrOffline("Не правильный ответ")
                else:
                    return Module
            except KeyError:
                Module = self.Read(self.server.name)
                return str(Module[name])
        
        def Write(self,**fields):
            """
            Записать в конфиг сервера.

            `Chat` : `ONLINE` / `OFFLINE`

            `Game` : `ONLINE` / `OFFLINE`

            `Rooms` : `ONLINE` / `OFFLINE`
            """

            Chat = self._CheckModule("Chat",fields)
            Game = self._CheckModule("Game",fields)
            Rooms = self._CheckModule("Rooms",fields)
            with codecs.open(f"{self.direct}/Config.txt","w"
                ,encoding='utf-8', errors='ignore') as file:
            # with open(f"{self.direct}/Config.txt","w") as file:
                Modules = {
                    "Chat" : Chat,
                    "Game" : Game,
                    "Rooms" : Rooms
                }
                file.write(str(Modules))

        def CreateServer(self):
            os.mkdir(self.direct)
            with codecs.open(f"{self.direct}/ServerConfig.txt","w"
                ,encoding='utf-8', errors='ignore') as file:
            # with open(f"{self.direct}/ServerConfig.txt","w") as file:
                newDict = {
                    "name" : self.server.name,
                    "ID" : self.server.id
                }
                file.write(str(newDict))
            self.Write(Chat="ONLINE",Game="ONLINE",Rooms="ONLINE")
    class Rooms(Config):
        """
        Настройка комнат
        """
        def __init__(self,server,Client):
            self.Client = Client
            self.server = server
            self.direct = f"./Servers/{self.server.name}"
        def SavedRooms(self):
            self.File = True
            try:
                with codecs.open(f"{self.direct}/RoomsConfig.txt","r"
                ,encoding='utf-8', errors='ignore') as file:
                # with open(f"{self.direct}/RoomsConfig.txt","r") as file:
                    return StrToDict(str=str(file.readline()))
            except FileNotFoundError:
                self.File = False
                return 
        
        def LoadRooms(self,Channel : int):
            Rooms = self.SavedRooms()
            if self.File == True:
                Channels = list(Rooms["Activity"])
                NewDict = {
                    "Activity" : [
                        Channel, 
                        *Channels
                    ]
                }
            else:
                NewDict = {
                    "Activity" : [
                        Channel
                    ]
                }
            with codecs.open(f"{self.direct}/RoomsConfig.txt","w"
            ,encoding='utf-8', errors='ignore') as file:
            # with open(f"{self.direct}/RoomsConfig.txt","w") as file:
                file.write(str(NewDict))

        def RemoveRooms(self,Channel : int):
            Rooms = self.SavedRooms()
            if self.File == True:
                ChannelsDelete = list(Rooms["Activity"])
                Channels = list()
                for _Channel in ChannelsDelete:
                    if int(_Channel) != Channel:
                        Channels.append(_Channel)
                NewDict = {
                    "Activity" : [
                        *Channels
                    ]
                }
                with codecs.open(f"{self.direct}/RoomsConfig.txt","w"
                ,encoding='utf-8', errors='ignore') as file:
                # with open(f"{self.direct}/RoomsConfig.txt","w") as file:
                    file.write(str(NewDict))
    class Chat(Config):
        """
        Настройка чата.
        """
        def __init__(self,server,Client):
            self.Client = Client
            self.server = server
            self.direct = f"./Servers/{self.server.name}"
        def SavedChat(self):
            """
            Сохраненные настройки чата

            Activity = каналы

            Status = статус
            """
            self.File = True
            try:
                with codecs.open(f"{self.direct}/ChatConfig.txt","r"
                ,encoding='utf-8', errors='ignore') as file:
                # with open(f"{self.direct}/ChatConfig.txt","r") as file:
                    return StrToDict(str=str(file.readline()))
            except FileNotFoundError:
                self.File = False
                return 
        
        def StatusEdit(self,Status : str):
            """
            Редактировать статус чата
            """
            Chats = self.SavedChat()
            if self.File == True:
                Channels = list(Chats["Activity"])
                NewDict = {
                    "Activity" : [
                        *Channels
                    ],
                    "Status" : Status
                }
            else:
                NewDict = {
                    "Activity" : [],
                    "Status" : "Private"
                }
            with codecs.open(f"{self.direct}/ChatConfig.txt","w"
                ,encoding='utf-8', errors='ignore') as file:
            # with open(f"{self.direct}/ChatConfig.txt","w") as file:
                file.write(str(NewDict))
        def LoadChat(self,Channel : int):
            """
            Загрузить новые настройки чата
            """
            Chats = self.SavedChat()
            if self.File == True:
                Channels = list(Chats["Activity"])
                Status = str(Chats["Status"])
                NewDict = {
                    "Activity" : [
                        Channel, 
                        *Channels
                    ],
                    "Status" : Status
                }
            else:
                NewDict = {
                    "Activity" : [
                        Channel
                    ],
                    "Status" : "Private"
                }
            with codecs.open(f"{self.direct}/ChatConfig.txt","w"
                ,encoding='utf-8', errors='ignore') as file:
            # with open(f"{self.direct}/ChatConfig.txt","w") as file:
                file.write(str(NewDict))

        def RemoveChat(self,Channel : int):
            """
            Удалить настойку чата
            """
            Chats = self.SavedChat()
            if self.File == True:
                ChannelsDelete = list(Chats["Activity"])
                Channels = list()
                for _Channel in ChannelsDelete:
                    if int(_Channel) != Channel:
                        Channels.append(_Channel)
                NewDict = {
                    "Activity" : [
                        *Channels
                    ],
                    "Status" : "Private"
                }
                with codecs.open(f"{self.direct}/ChatConfig.txt","w"
                ,encoding='utf-8', errors='ignore') as file:
                # with open(f"{self.direct}/ChatConfig.txt","w") as file:
                    file.write(str(NewDict))

        
        pass
    
    class TooManyWords(Error):
        def Error(self):
            return "Слишком мало слов я знаю"
    class GENERAL(): pass
    def Message(self,CountMessages : int,ServerName : str,Status : GENERAL):
        Lines = []
        if Status == "GENERAL":
            with codecs.open(f"./Resurses/Words.txt", "r",encoding='utf-8', errors='ignore') as file:
            # with open(f"./Resurses/Words.txt","r") as file:
                for line in file.readlines():
                    line = line.decode("utf-8")
                    Cannot = [' ','','\n']
                    if line not in Cannot:
                        CheckMessage_ = CheckMessage(line,"https://")
                        if CheckMessage_.Start() == None:
                            Lines.append(str(line))
        else:
            with codecs.open(f"./Servers/{ServerName}/Words.txt","r",encoding='utf-8', errors='ignore') as file:
            # with open(f"./Servers/{ServerName}/Words.txt","r") as file:
                for line in file.readlines():
                    Cannot = [' ','','\n']
                    if line not in Cannot:
                        CheckMessage_ = CheckMessage(line,"https://")
                        if CheckMessage_.Start() == None:
                            Lines.append(str(line))
        Message = ""
        Count = 0
        BadWords = [
            '\n'
        ]
        while Count < CountMessages:
            try:
                RandomLine = random.randint(1,len(Lines) - 2)
                MainLine = list()
                Words = Lines.pop(RandomLine)
                MainLine.append(Words.split(" "))
                for word in MainLine[0]:
                    Write = randomBool(0,1,1)
                    if Write == True:
                        URL = CheckMessage(word,"https://")
                        URL = URL.Start()
                        if URL == None:
                            if word not in BadWords:
                                try:
                                    word = word.split("\n")[0]
                                except: pass
                                WordSplit = list(); WordSplit.extend(word)
                                for wordSplit in WordSplit: 
                                    if wordSplit != ")":
                                        Message += wordSplit
                                Message += f" "
                                Count += 1
                                # print(f"{Count} {word}")
                                if Count >= CountMessages:
                                    return Message
                    WriteOtherLine = randomBool(0,1,1)
                    if WriteOtherLine == True:
                        RandomLine = random.randint(1,len(Lines) - 2)
                        OtherLine = list()
                        Words = Lines.pop(RandomLine)
                        OtherLine.append(Words.split(" "))
                        for word2 in OtherLine[0]:
                            Write = randomBool(0,1,1)
                            if Write == True:
                                URL = CheckMessage(word,"https://")
                                URL = URL.Start()
                                if URL == None:
                                    if word2 not in BadWords:
                                        try:
                                            word2 = word2.split("\n")[0]
                                        except: pass
                                        WordSplit = list(); WordSplit.extend(word2)
                                        for wordSplit in WordSplit: 
                                            if wordSplit != ")":
                                                Message += wordSplit
                                        Message += f" "
                                        Count += 1
                                        # print(f"{Count} {word2}")
                                        if Count >= CountMessages:
                                            return Message
            except ValueError:
                raise self.TooManyWords("Слишком мало слов я знаю")

        return Message
    def SaveMessage(self):
        pass



def AllMVPs():
    """
    Выводит всю рейтингвую информацию

    _allMvps = AllMVPs()
    OnlyNicks = list()
    OnlyNicks.append(_allMvps[1])

    PlayerList = list()
    PlayerList.append(OnlyNicks[0][0])
    _Level__ = _allMvps[0]

    alreadyChecked = list()

    PositionRange = 0
    for _UserName_ in OnlyNicks[0]:
        Position += 1
        if Position > 5:
            break
        PositionRange = 0
        for _Level_ in _Level__:
            PositionRange += 1
            with open(f"./Stats/Main/{_UserName_}.txt","r") as file:
                CurLvl = int(file.readline())
                CurLvl = int(file.readline())
                if (CurLvl == _Level_) and (_UserName_ not in alreadyChecked):
                    pass

    """
    #me = "KOT32500"
    PlayersInStats = 0
    PlayerList = list()
    LvlMvpList = list()
    lst = list()
    with codecs.open(f"./Stats/Clients.txt","r"
    ,encoding='utf-8', errors='ignore') as file:
    # with open(f"./Stats/Clients.txt","r") as file:
        PlayersInStats = int(file.readline())
        for target_list in range(PlayersInStats):
            RDtxt = file.readline()
            lst.append(RDtxt)
            try:
                curPla = lst[target_list].split();curPla = curPla[0]
                try:
                    with codecs.open(f"./Stats/Main/{curPla}.txt","r"
                    ,encoding='utf-8', errors='ignore') as file:
                    # with open(f"./Stats/Main/{curPla}.txt","r") as fileTo:
                        rdExp = fileTo.readline() ; rdExp.split() ; rdExp = rdExp[0]
                        rdLvl = fileTo.readline() ; rdLvl.split()# ; rdLvl = rdLvl[0]
                        Numbers = int(rdLvl)
                        LvlMvpList.append(int(Numbers))
                        PlayerList.append(curPla)
                except FileNotFoundError:
                    pass
            except IndexError:
                pass
    sortPlayers = sorted(LvlMvpList,reverse=True)

   # print(f"{lst} лист игроков")

    # for _Players_ in PlayerList:
    #     for _Level_ in LvlMvpList:
    #        # print(f"{_Level_} уровень")
    #         with open(f"./Stats/Main/{_Players_}.txt","r") as file:
    #             CurExp = int(file.readline())
    #             CurLvl = int(file.readline())
    #             if CurLvl == _Level_:
    #                 print(f"{_Level_} у {_Players_}")
    
   # lst.clear()
   # LvlMvpList.clear()
    return sortPlayers , PlayerList , LvlMvpList

def Attack(_UserName_ : str,_Target_ : str,Damage):
    pass
    # Player = ReadMainParametrs(username=_UserName_)
    # Target = ReadMainParametrs(username=_Target_)
    # TargetHealth = int(Target["curHealth"])
    # GetDamage = random.randint(1,Damage)

    # TargetHealth -= GetDamage

    # FreeLvlHA = EnIntCurLvl / 5

    # if TargetHealth <= 0:
    #     TargetHealth = EnIntMaxHealth
    #     TargetHealth -= int(FreeLvlHA)
    #     IntCurLvl += int(FreeLvlHA)
    #     time.sleep(0.1)

    #     IntMaxHealth += 10 * int(FreeLvlHA)
    #     IntCurHealth += 10 * int(FreeLvlHA)
    #     IntMaxDamage += random.randint(1,35) * int(FreeLvlHA)
    #     if ((IntCurHealth + 5 * int(FreeLvlHA)) < (IntMaxHealth)):
    #         IntCurHealth += 5 * int(FreeLvlHA)
    #     else:
    #         IntCurHealth = IntMaxHealth
        
    #     EnIntMaxHealth -= 10 * int(FreeLvlHA)
    #     EnIntMaxDamage -= random.randint(1,35) * int(FreeLvlHA)
    #     EnIntCurHealth = EnIntMaxHealth
    # with open(f"./Stats/Main/{_UserName_}.txt","w") as file:
    #     file.writelines(str(IntCurExp))
    #     file.writelines(str(IntCurLvl))
    #     file.writelines(str(IntMaxHealth))
    #     file.writelines(str(IntCurHealth))
    #     file.writelines(str(Description))
    # with open(f"./Stats/Main/{_Target_}.txt","w") as file:
    #     file.writelines(str(EnIntCurExp))
    #     file.writelines(str(EnIntCurLvl))
    #     file.writelines(str(EnIntMaxHealth))
    #     file.writelines(str(EnIntCurHealth))
    #     file.writelines(str(EnDescription))
    # return Emb
    

def nullWrite(_UserName_,new_Client : bool):
    """
    Обнуление статистики.

    Или её создание

    Вход : 
        _UserName_ = Имя игрока. Str Формат
    """
    f = open("./Stats/Main/" + _UserName_ + ".txt","w")
    f.writelines("0") # IntCurExp 0
    f.writelines("\n0") # IntCurLvl 1
    f.writelines("\n0") # IntMaxHealth 2
    f.writelines("\n0") # IntCurHealth 3
    f.writelines("\n0") # IntMaxDamage 4
    Description_Randoms = ("Всем привет!","Мргл. мргл.","Информация пуста",".","Остуствует что либо")
    rnd = random.randint(1,int(len(Description_Randoms)))
    try:
        f.writelines(f"\n{Description_Randoms[rnd]}")
    except Exception:
        f.writelines(f"\n ")
     # Description 5
    #f.writelines("\nS") # Description 5
    f.close()
    with codecs.open(f"./Stats/Shop/{_UserName_}.txt","w"
    ,encoding='utf-8', errors='ignore') as file:
    # with open(f"./Stats/Shop/{_UserName_}.txt","w") as file:
        file.writelines("0")
        file.writelines("\n0")
    lstClients = list()
    if new_Client == True:
        with codecs.open(f"./Stats/Clients.txt","r"
        ,encoding='utf-8', errors='ignore') as file:
        # with open(f"./Stats/Clients.txt","r") as file:
            for lines in file.readlines():
                lstClients.append(lines)
        with codecs.open(f"./Stats/Clients.txt","w"
        ,encoding='utf-8', errors='ignore') as file:
        # with open(f"./Stats/Clients.txt","w") as file:
            for lines in range(len(lstClients)):
                if lines != 0:
                    
                    file.writelines(lstClients[lines])
                else:
                    first_line = lstClients[0]
                    first_line.split() ; first_line = first_line[0]
                    first_line = int(first_line)
                    first_line += 1
                    file.writelines(str(first_line) + "\n")
            try:
                file.writelines(f"\n{_UserName_}")
            except UnicodeEncodeError:
                pass
            
    #print(lstClients)

    _AgentWrite(_UserName_,StandartURL,False) ; _AgentWrite(_UserName_,StandartURLBackGround,True)

def _readStats(_UserName_):
    """
    Прочитать статистику.

    Прочитывает статистику игрока.

    Вход : 
        _UserName_ = Имя игрока. Str Формат
    Выход : 
        IntCurExp = 0 (STR)
        IntCurLvl = 1 (STR)
        IntMaxHealth = 2 (STR)
        IntCurHealth = 3 (STR)
        IntMaxDamage = 4 (STR)
        Description = 5 (STR)
    """
    try:
        with codecs.open(f"./Stats/Main/{_UserName_}.txt","r"
        ,encoding='utf-8', errors='ignore') as file:
        # with open(f"./Stats/Main/{_UserName_}.txt","r") as file:
            IntCurExp = file.readline()
            IntCurLvl = file.readline()
            IntMaxHealth = file.readline()
            IntCurHealth = file.readline()
            IntMaxDamage = file.readline()
            Description = file.readline()
        return IntCurExp ,IntCurLvl,IntMaxHealth,IntCurHealth,IntMaxDamage,Description
    except FileNotFoundError:
        raise FileNotFoundError("Этого аккаунта, не существует")

def _writeStats(_UserName_,*arg):
    """
    Записать в статистику

    Записывает в статистику

    Вход : 
        _UserName_ = Имя игрока. Str Формат
        *arg = Принимает в себя все строчки, которые нужно сохранить
    """
    f = open("./Stats/Main/" + _UserName_ + ".txt","w")
    for target_list in range(len(arg)):
        if target_list != range(len(arg)):
            f.writelines(str(arg[target_list]+ "\n"))
        else:
            f.writelines(str(arg[target_list]))
    f.close()

def _AgentRead(_UserName_,BackGround : bool):
    """
    Агент чтения.

    Прочитывает профиль игрока (URL)

    Вход : 
        _UserName_ = Имя игрока. Str Формат
    Выход : 
        _url = URL. Str Формат
    """
    if BackGround == False:
        with codecs.open(f"./Stats/Profile/{_UserName_}.txt","r"
        ,encoding='utf-8', errors='ignore') as file:
        # with open(f"./Stats/Profile/{_UserName_}.txt","r") as file:
            _url = file.readline()
            return _url
    else:
        with codecs.open(f"./Stats/Profile/BackGround_{_UserName_}.txt","r"
        ,encoding='utf-8', errors='ignore') as file:
        # with open(f"./Stats/Profile/BackGround_{_UserName_}.txt","r") as file:
            _url = file.readline()
            return _url

def _AgentWrite(_UserName_,__url__,BackGround : bool):
    """
    Агент записи. 
    
    Записывает в url в профиль игрока
    
    Вход : 
        _UserName_ = Имя игрока. Str формат
    """
    if BackGround == False:
        with codecs.open("./Stats/Profile/" + _UserName_ + ".txt","w"
        ,encoding='utf-8', errors='ignore') as file:
        # with open("./Stats/Profile/" + _UserName_ + ".txt","w") as file:
            file.writelines(__url__)

            logo = StandartURL

            try:
                logo = urllib.request.urlopen(__url__).read()
                
                with open(f"{Resurses}{_UserName_}.png", "wb") as fileTwo:
                    fileTwo.write(logo)
            except Exception:
                pass
    else:
        with codecs.open(f"./Stats/Profile/BackGround_{_UserName_}.txt","w"
        ,encoding='utf-8', errors='ignore') as file:
        # with open(f"./Stats/Profile/BackGround_{_UserName_}.txt","w") as file:
            file.writelines(__url__)

            logo = StandartURLBackGround

            try:
                logo = urllib.request.urlopen(__url__).read()
                with open(f"{Resurses}BackGround_{_UserName_}.png", "wb") as fileTwo:
                    fileTwo.write(logo)
            except Exception:
                pass
        pass

def _ShopAgentRead(_UserName_):
    """
    Прочитать статистику агента по Магазину

    Вход : 
        _UserName_ = Имя игрока. Str Формат
    Выход : 
        Messages = Количество сообщений
        Gold = Количество Золота
        Формат = tuple
    """
    f = open("./Stats/Shop/" + str(_UserName_) + ".txt","r")
    Messages = f.readline()
    Gold = f.readline() 
    f.close()
    return Messages , Gold

def profileEdit(_UserName_):
    """
    Меняет профиль игрока. Относиться к команде Profile


    Вход :
        _UserName_ = Имя игрока. Str формат
    Выход :
        Файл = Discord.File
    """
    try:
        MainStats = _readStats(_UserName_)
        IntCurExp = int(MainStats[0])
        IntCurLvl = int(MainStats[1])
        IntMaxHealth = int(MainStats[2])
        IntCurHealth = int(MainStats[3])
        IntMaxDamage = int(MainStats[4])
        Description = str(MainStats[5])
        DescriptionSplit = Description.split()
        Description = ""
        for target_list in DescriptionSplit:
            ABM = str.upper(target_list)
            if ABM != "ABOUT_ME":
                Description += target_list + " "
        
        AllLatters = list()
        AllLatters.extend(Description)
        Description = ""
        countLatter = 0
        for Latter in AllLatters:
            countLatter += 1
            if countLatter == 32:
                countLatter = 0
                Description += f"\n{Latter}"
            else:
                Description += Latter
        
        ShopAgent = _ShopAgentRead(_UserName_)
        Messages = int(ShopAgent[0])
        Gold = int(ShopAgent[1])
        import urllib.request
        try:
            # logo = urllib.request.urlopen(_AgentRead(_UserName_)).read()
            # f = open(Resurses + _UserName_ + ".png", "wb")
            # f.write(logo)
            # f.close()

            BackGround = Image.open(f"{Resurses}BackGround_{_UserName_}.png")

            img = Image.open(Resurses + "Main.png")
            #N_Ava = Image.open(Resurses + "Ava.png")
            N_Ava = Image.open(Resurses + _UserName_ + ".png")
            Ava = N_Ava.resize((74,74)) #76 76

            draw = ImageDraw.Draw(img)
            count = 10
            counts = 0
            ElseCount = 0
            Scaling = 20
            for target_list in range(int(IntCurLvl)):
                if target_list < -5:
                    print("ERROR")
                counts += 1
                if counts >= int(count):
                    count = str(count) + "0"
                    counts = 0
                    ElseCount += 5
                    Scaling -= 1

            areaT = (54 - ElseCount,145) #121 153
            font = ImageFont.truetype("arial.ttf",Scaling)
            draw.text(areaT,str(IntCurLvl),font=font,fill="black")



            #AgentConfig = _AgentReadConfig(_UserName_)

            area = (101,108)
            Color = (200,210,255)
           # Color = AgentConfig
            font = ImageFont.truetype("arial.ttf",25)
            draw.text(area,_UserName_,font=font,fill=Color)

            area = (161,143)
            Color = (0,0,0)
            font = ImageFont.truetype("arial.ttf",8)
            txt = str("Здоровье : " + str(IntCurHealth) + " ед./ " + str(IntMaxHealth))
            draw.text(area,txt,font=font,fill=Color)

            area = (161,158)
            Color = (0,0,0)
            font = ImageFont.truetype("arial.ttf",8)
            txt = str("Урон : " + str(IntMaxDamage) + " ед.")
            draw.text(area,txt,font=font,fill=Color)

            area = (110,280)
            Color = (0,0,0)

            Procent = (IntCurExp * 100) / (IntCurLvl * 5)

           # print(Procent)
           # print(int(Procent))

            #ProcentDel = int(Procent / 100)



            xPos = int((200 - 100) + Procent) ; yPos = 289
            Start_X_Pixel = 100; Start_Y_Pixel = 279
            #MathXPos = xPos - 100 # 183
            RedColor = random.randint(50,205)
            GreenColor = random.randint(50,205)
            BlueColor = random.randint(50,205)
            ColorCur = (RedColor,GreenColor,BlueColor)
            for x in range(int((xPos - Start_X_Pixel))):
                Start_X_Pixel += 1
                Cur_Y_Pixel = Start_Y_Pixel
                for y in range(yPos - Start_Y_Pixel):
                    Start_Y_Pixel += 1
                    #ColorCur = (85,233,156)
                    img.putpixel((Start_X_Pixel,Start_Y_Pixel),ColorCur)
                    if (x) and (y) == -1: pass
                Start_Y_Pixel = Cur_Y_Pixel
            
            font = ImageFont.truetype("arial.ttf",8)
            txt = str(f"Опыт : {IntCurExp} / {IntCurLvl * 5}")
            draw.text(area,txt,font=font,fill=Color) #█ exp
            
                    
            

            area = (161,173)
            Color = (0,0,0)
            font = ImageFont.truetype("arial.ttf",8)
            txt = str("Золота : " + str(Gold) + " / " + str(Messages))
            draw.text(area,txt,font=font,fill=Color)

            Color = (0,0,0)
            The_number_of_letters = list()
            Scaling = 0
            The_number_of_letters.extend(Description)
            countLetter = 0
            Offset = 0
            for Letter in The_number_of_letters:
                if (Letter == "ERROR"): pass
                countLetter += 1
               # print(f"{Letter} текущая буква")
                if (countLetter == 4):
                    Scaling -= 1
                    countLetter = 0
                    Offset += 2
                    #print(f"{Letter} текущая строчка ({countLetter})")
           # print(f"{The_number_of_letters} \n {Scaling}")
            The_number_of_letters.clear()

            Scaling = (18 + Scaling)
            if Scaling < 0:
                Scaling = 0
            area = (110,200 + Offset)
            font = ImageFont.truetype("arial.ttf",1 + Scaling)
            txt = str(Description)
            draw.text(area,txt,font=font,fill=Color)

            area = (108,185)
            font = ImageFont.truetype("arial.ttf",17)
            txt = str("О себе : \n")
            draw.text(area,txt,font=font,fill=Color)

            areaAva = (19,68)

            img.paste(Ava,areaAva)
            nameSave = "StatsPl.png"
            #img.save(nameSave)
            BackGround = BackGround.resize((300,400)) #(358,481)
            area = (0,100) #(25,175)
            
            BackGround.paste(img.convert('RGB'), area, img)
            BackGround.save(nameSave)

            sf = discord.File(nameSave,nameSave)
            #await message.channel.send(" ",file=sf)
            pass
            return sf
        except ValueError:
            #profileEdit(_UserName_)
            pass
    except Exception:
        pass

def StrToDict(**fields):
    """
    `str` : текст который нужно будет конвентировать в Dict
    """
    _str = str(fields.pop('str'))
    NwDict = ast.literal_eval(f'{_str}') ; NwDict = dict(NwDict)
    return NwDict

def RatingSystem():
    Positions = 0
    MainPicture = Image.open(Resurses + "rating statistics.png")
    Position = 0

    _allMvps = AllMVPs()
    OnlyNicks = list()
    OnlyNicks.append(_allMvps[1])

    PlayerList = list()
    PlayerList.append(OnlyNicks[0][0])
    _Level__ = _allMvps[0]

    alreadyChecked = list()

    PositionRange = 0
    for _UserName_ in OnlyNicks[0]:
        Position += 1
        if Position > 5:
            break
        PositionRange = 0
        for _Level_ in _Level__:
            PositionRange += 1
            with codecs.open(f"./Stats/Main/{_UserName_}.txt","r"
            ,encoding='utf-8', errors='ignore') as file:
            # with open(f"./Stats/Main/{_UserName_}.txt","r") as file:
                CurLvl = int(file.readline())
                CurLvl = int(file.readline())
                if (CurLvl == _Level_) and (_UserName_ not in alreadyChecked):

                    alreadyChecked.append(_UserName_)

                    Positions = (500 * (PositionRange - 1))

                    Picture = Image.open(Resurses + "a Place.png")
                    PictureDraw = ImageDraw.Draw(Picture)

                    Ava = Image.open(Resurses + _UserName_ + ".png")
                    Ava = Ava.resize((391,481))
                    area = (0,0)
                    Picture.paste(Ava,area)

                    areaT = (550,200)
                    font = ImageFont.truetype("arial.ttf",75)
                    PictureDraw.text(areaT,str(_UserName_),font=font,fill="black")

                    areaT = (2150,125)
                    font = ImageFont.truetype("arial.ttf",200)
                    PictureDraw.text(areaT,str(PositionRange),font=font,fill="black")


                    area = (218,222 + Positions)
                    MainPicture.paste(Picture,area)
                    nameSave = "RatingSystem.png"

    MainPicture.save(nameSave)
    sf = discord.File(nameSave,nameSave)

    alreadyChecked.clear()
    PlayerList.clear()
    OnlyNicks.clear()
    

    return sf

async def EditAttackDamageTwo(self,Channel : discord.channel.TextChannel,GetDamage : int,_Player : str,_Target : str,CurHealthTarget : int):
    today = datetime.datetime.today()
    try:
        with codecs.open(f"./Stats/GetDamageForTime/{_Player}.txt","r"
        ,encoding='utf-8', errors='ignore') as file:
        # with open(f"./Stats/GetDamageForTime/{_Player}.txt","r") as file:
            Message = int(file.readline())
            Message = await Channel.fetch_message(Message)
            Date = str(file.readline()) ; Date = Date.split("-")
            SumarDamage = int(file.readline())
        SumarDamage += GetDamage
        if int(Date[4]) != today.minute:
            _Message = await Channel.send(content=f"{_Player} нанёс : {GetDamage} ед.\nСумарный урон : {SumarDamage} ед.\nЗдоровье у {_Target} : {CurHealthTarget} ед.")
        else:
            await Message.edit(content=f"{_Player} нанёс : {GetDamage} ед.\nСумарный урон : {SumarDamage} ед.\nЗдоровье у {_Target} : {CurHealthTarget} ед.")
        with codecs.open(f"./Stats/GetDamageForTime/{_Player}.txt","w"
        ,encoding='utf-8', errors='ignore') as file:
        # with open(f"./Stats/GetDamageForTime/{_Player}.txt","w") as file:
            writeToday = "%Y-%m-%d-%H-%M-%S"
            if int(Date[4]) != today.minute:
                file.writelines(f"{_Message.id}")
                file.writelines(f"\n{str(today.strftime(writeToday))}")
                file.writelines(f"\n0")
            else:
                file.writelines(f"{Message.id}")
                file.writelines(f"\n{str(today.strftime(writeToday))}")
                file.writelines(f"\n{SumarDamage}")
    except:
        with codecs.open(f"./Stats/GetDamageForTime/{_Player}.txt","w"
        ,encoding='utf-8', errors='ignore') as file:
        # with open(f"./Stats/GetDamageForTime/{_Player}.txt","w") as file:
            _Message = await Channel.send(content=f"{_Player} нанёс : {GetDamage} ед.\nСумарный урон : {GetDamage} ед.\nЗдоровье у {_Target} : {CurHealthTarget} ед.")
            writeToday = "%Y-%m-%d-%H-%M-%S"
            file.writelines(f"{_Message.id}")
            file.writelines(f"\n{str(today.strftime(writeToday))}")
            file.writelines(f"\n0")
    

    pass


def CreateNewBoss():
    with codecs.open(f"./Stats/EventBoss.txt","w"
    ,encoding='utf-8', errors='ignore') as file:
    # with open(f"./Stats/EventBoss.txt","w") as file:
        today = datetime.datetime.today()
        MaxHealth = random.randint(10000,50000)
        CurHealth = MaxHealth
        GetGold = 0
        for ran in range(int(MaxHealth / 1000)):
            if ran < 0: print("ERROR")
            GetGold += random.randint(5,50)
            pass
        Dead = "No"
        NameFile = random.randint(1,32)
        NameFile = f"Boss{NameFile}"
        NewDict = {
            "data": str(today.strftime("%Y-%m-%d-%H-%M-%S")) ,
            "maxHealth":str(MaxHealth),
            "curHealth":str(CurHealth),
            "getGold":str(GetGold),
            "dead":str(Dead),
            "nameFile":NameFile,
            "killer":"none"
        }
        file.writelines(f"{str(NewDict)}")

def ReadBossStats():
    """
    Прочитать статистику босса

    `data`

    `maxHealth`

    `curHealth`

    `getGold`

    `dead`

    `nameFile`
    
    `killer`

    """
    with codecs.open(f"./Stats/EventBoss.txt","r"
    ,encoding='utf-8', errors='ignore') as file:
    # with open(f"./Stats/EventBoss.txt","r") as file:
        stats = str(file.readline())
        stats = StrToDict(str=stats)
        pass
    return stats

def WriteBossStats(**fields):
    """
    Записать в статистику

    `data`

    `maxHealth`

    `curHealth`

    `getGold`

    `dead`

    `nameFile`

    `killer`

    """

    try:
        data = fields.pop("data")
    except:
        try:
            RBS = ReadBossStats() ; data = RBS.pop("data")
        except: pass

    try:
        maxHealth = fields.pop("maxHealth")
    except:
        try:
            RBS = ReadBossStats() ; maxHealth = RBS.pop("maxHealth")
        except: pass

    try:
        curHealth = fields.pop("curHealth")
    except:
        try:
            RBS = ReadBossStats() ; curHealth = RBS.pop("curHealth")
        except: pass

    try:
        getGold = fields.pop("getGold")
    except:
        try:
            RBS = ReadBossStats() ; getGold = RBS.pop("getGold")
        except: pass

    try:
        dead = fields.pop("dead")
    except:
        try:
            RBS = ReadBossStats() ; dead = RBS.pop("dead")
        except: pass

    try:
        nameFile = fields.pop("nameFile")
    except:
        try:
            RBS = ReadBossStats() ; nameFile = RBS.pop("nameFile")
        except: pass

    try:
        killer = fields.pop("killer")
    except:
        try:
            RBS = ReadBossStats() ; killer = RBS.pop("killer")
        except: pass


    NewDict = {
        "data": data ,
        "maxHealth":maxHealth,
        "curHealth":curHealth,
        "getGold":getGold,
        "dead":dead,
        "nameFile":nameFile,
        "killer":killer
    }
    with codecs.open(f"./Stats/EventBoss.txt","w"
    ,encoding='utf-8', errors='ignore') as file:
    # with open(f"./Stats/EventBoss.txt","w") as file:
        file.write(str(NewDict))

    



    pass

def FutureMessageDef(**fields):
    """
    Готовое сообщение

    `message` : сообщение

    `step` : количество сообщений
    
    """

    try:
        message = fields.pop('message')
    except KeyError:
        raise Error_FutureMessageDef("Отсуствует параметр сообщения")

    try:
        step = int(fields.pop('step'))
    except:
        raise Error_FutureMessageDef("Отсуствует параметр количеств или указана не цифра") 


    NewMessage = str()
    MessageSplit_LN = message.split("\n")
    MessageSplit = message.split()
    RandomLine = random.randint(0,len(MessageSplit_LN) - 1)
    WordInJump = [',','.',' ','/','"',"'",'%','$','-','=','_','+','`']
    Count = step
    WordNotInJump = ""
    RandomSayOrNo = 0
    CountWordsLen = 0
    FrstWord = True
    for word in MessageSplit_LN[RandomLine]:
        if Count > 0:
            if word not in WordInJump:
                wordUpgrade = word
                if FrstWord == False:
                    wordUpgrade = str.lower(word)
                if FrstWord == True:
                    wordUpgrade = str.upper(word)
                    FrstWord = False
                if RandomSayOrNo == 0:
                    RandomSayOrNo = random.randint(1,5)
                if (RandomSayOrNo != 1) or (Count == step):
                    WordNotInJump += wordUpgrade
            else:
                CountWordsLen += 1
                NewMessage += WordNotInJump
                WordNotInJump = ""
                RandomSayOrNo = 0
                Count -= 1
                RandomSayOrNo = random.randint(0,4)
                if RandomSayOrNo == 1:
                    RandomWordInt = random.randint(0,len(MessageSplit) - 1)
                    RandomWord = MessageSplit[RandomWordInt]
                    NewMessage += f" {RandomWord} "
                else:
                    NewMessage += " "
        else:
            break
        pass

    return NewMessage

def ReadWords(Server : str,Status : str):
    AllWords = str()
    if Status != "PRIVATE":
        with codecs.open(f"./Resurses/Words.txt","r"
        ,encoding='utf-8', errors='ignore') as file:
        # with open(f"./Resurses/Words.txt","r") as file:
            try:
                for line in file.readlines():
                    AllWords += line
            except:
                pass
        return AllWords
    else:
        with codecs.open(f"./Servers/{Server}/Words.txt","r"
        ,encoding='utf-8', errors='ignore') as file:
        # with open(f"./Servers/{Server}/Words.txt","r") as file:
            try:
                for line in file.readlines():
                    AllWords += line
            except:
                pass
        return AllWords


def SaveWords(msg : str,Server : str,Status : str):
    if Status != "PRIVATE":
        Oldmsg = ReadWords(Server,Status)
        with codecs.open(f"./Resurses/Words.txt","w"
        ,encoding='utf-8', errors='ignore') as file:
        # with open(f"./Resurses/Words.txt","w") as file:
            msgSplitLines = msg.split("\n")
            file.write(f"{Oldmsg}")
            for line in msgSplitLines:
                file.writelines(f"\n{line}")
    else:
        Oldmsg = ReadWords(Server,Status)
        with codecs.open(f"./Servers/{Server}/Words.txt","w"
        ,encoding='utf-8', errors='ignore') as file:
        # with open(f"./Servers/{Server}/Words.txt","w") as file:
            msgSplitLines = msg.split("\n")
            file.write(f"{Oldmsg}")
            for line in msgSplitLines:
                file.writelines(f"\n{line}")


def ClearWords(**fields):
    with codecs.open(f"./Resurses/Words.txt","w"
    ,encoding='utf-8', errors='ignore') as file:
    # with open(f"./Resurses/Words.txt","w") as file:
        file.write("")
    pass  

def WriteEquipment(**fields): 
    """
    Одеть предмет

    `username` : имя игрока

    `type` : тип предмета

    `бывают типы` : Оружие , Броня 

    `ID` : Индекс предмета.

    `1(0)` = `Броня`

    `2(1)` = `Оружие`

    """
    username = fields.pop('username')
    type_ = fields.pop('type')
    ID = int(fields.pop('ID'))

    try:
        with codecs.open(f"./Stats/Inventory/{username}.txt","r"
        ,encoding='utf-8', errors='ignore') as file:
        # with open(f"./Stats/Inventory/{username}.txt","r") as file:
            Inventor = file.readline()
            Inventor = StrToDict(str=Inventor)
            ArmorId = int(Inventor["Armor"])
            AttackId = int(Inventor["Attack"])
    except FileNotFoundError:
        with codecs.open(f"./Stats/Inventory/{username}.txt","w"
        ,encoding='utf-8', errors='ignore') as file:
        # with open(f"./Stats/Inventory/{username}.txt","w") as file:
            NewDict = {
            "Armor" : 0,
            "Attack" : 0
            }
            file.write(str(NewDict))
            AttackId = 0
            ArmorId = 0
            pass

    if type_ == "Оружие":
        AttackId = ID
    if type_ == "Экипировка":
        ArmorId = ID
    with codecs.open(f"./Stats/Inventory/{username}.txt","w"
    ,encoding='utf-8', errors='ignore') as file:
    # with open(f"./Stats/Inventory/{username}.txt","w") as file:
        NewDict = {
            "Armor" : int(ArmorId),
            "Attack" : int(AttackId)
        }
        file.write(str(NewDict))
    
    pass

def ReadEquipment(**fields):
    """
    Прочитать что одето на игрока

    `username` : Имя игрока

    `type` : Оружие , Экипировка

    """

    type_ = fields.pop('type')
    username = fields.pop('username')
    with codecs.open(f"./Stats/Inventory/{username}.txt","r"
    ,encoding='utf-8', errors='ignore') as file:
    # with open(f"./Stats/Inventory/{username}.txt","r") as file:
        Stats = file.readline()
        Stats = StrToDict(str=Stats)
        if type_ == "Экипировка":
            return int(Stats["Armor"])
        if type_ == "Оружие":
            return int(Stats["Attack"])
        

def CheckParametrsEquipment(**fields):
    """
    Вывести параметры предмета

    `username` : имя игрока

    `ID` : Индекс предмета.

    """

    username = fields.pop("username")

    ID = fields.pop("ID")
    with codecs.open(f"./Stats/Inventory/Inventor_{username}.txt","r"
    ,encoding='utf-8', errors='ignore') as file:
    # with open(f"./Stats/Inventory/Inventor_{username}.txt","r") as file:
        for item in file.readlines():
            itemDict = StrToDict(str=item)
            itemID = int(itemDict['ID'])
            if ID == itemID:
                return itemDict


def _Gold(**fields):
    """
    Взаимодействия с золотом

    `username` : Имя игрока

    `do` : Убавить / Добавить / Разузнать

    `count` : Количество

    """

    username = fields.pop("username")
    do = fields.pop("do")
    try:
        count = int(fields.pop("count"))
    except:
        pass

    Parametrs = ReadMainParametrs(username=username)
    Gold = int(Parametrs.pop("money"))
    if do == "Убавить":
        Gold -= count
        WriteMainParametrs(username=username,money=Gold)
    if do == "Добавить":
        Gold += count
        WriteMainParametrs(username=username,money=Gold)
    if do == "Разузнать":
        return Gold
    


def BalansList(**fields):
    """
    Создает рандомные параметры, исходя из класса предмета

    `---------------- ОБЯЗАТЕЛЬНЫЕ ----------------`

    `type` : Тип предмета

    `classItem` : Класс предмета 
    
    `Сломанный` -> `Первоначальный` -> `Обычный` -> `Редкий` -> `Эпический` -> `Легендарный` -> `Мифический` -> `Демонический` = `Божественный` -> `Уникальный`
    
    `---------------- ОБЯЗАТЕЛЬНЫЕ ----------------`

    `------------------- ОРУЖИЕ -------------------`

    `Первоначальный` = от `1` до `5`

    `Обычный` = от `10` до `30`

    `Редкий` = от `45` до `100`

    `Эпический` = от `125` до `300`

    `Легендарный` = от `500` до `700`

    `Мифический` = от `10` до `2000`

    `Демонический` = от `2500` до `4000`

    `Божественный` = от `2000` до `4500`

    `------------------- ОРУЖИЕ -------------------`
    
    `----------------- ЭКИПИРОВКА -----------------`

    `Первоначальный` = от `1` до `5`

    `Обычный` = от `10` до `25`

    `Редкий` = от `40` до `90`

    `Эпический` = от `100` до `250`

    `Легендарный` = от `500` до `600`

    `Мифический` = от `10` до `1700`

    `Демонический` = от `2350` до `3700`

    `Божественный` = от `2000` до `4000`

    `----------------- ЭКИПИРОВКА -----------------`

    `----------------- СТОИМОСТЬ ------------------`
    
    `Первоначальный` = от `35` до `50`

    `Обычный` = от `45` до `100`

    `Редкий` = от `110` до `170`

    `Эпический` = от `300` до `1000`

    `Легендарный` = от `1300` до `3000`

    `Мифический` = от `5000` до `10000`

    `Демонический` = от `9500` до `10000`

    `Божественный` = от `10000` до `15000`

    `----------------- СТОИМОСТЬ ------------------`

    `----------------- ПРОЧНОСТЬ ------------------`

    `----------------- ПРОЧНОСТЬ ------------------`

    """

    type_ = fields.pop("type")

    classItem = fields.pop("classItem")

    if type_ == "Оружие":
        Damage = 0
        Gold = 0
        Stability = 0
        if classItem == "Первоначальный":
            Damage = random.randint(1,5)
            Gold = random.randint(35,50)
            Stability = random.randint(100,200)

        if classItem == "Обычный":
            Damage = random.randint(10,30)
            Gold = random.randint(45,100)
            Stability = random.randint(150,300)

        if classItem == "Редкий":
            Damage = random.randint(45,100)
            Gold = random.randint(110,170)
            Stability = random.randint(250,450)

        if classItem == "Эпический":
            Damage = random.randint(125,300)
            Gold = random.randint(300,1000)
            Stability = random.randint(600,1000)

        if (classItem == "Легендарный") or (classItem == "Ћегендарный"):
            Damage = random.randint(500,700)
            Gold = random.randint(1300,3000)
            Stability = random.randint(32000,100000)

        if classItem == "Мифический":
            Damage = random.randint(10,2000)
            Gold = random.randint(5000,10000)
            Stability = random.randint(100,10000000)

        if classItem == "Демонический":
            Damage = random.randint(2500,4000)
            Gold = random.randint(9500,10000)
            Stability = 100000000

        if classItem == "Божественный":
            Damage = random.randint(2000,4500)
            Gold = random.randint(10000,15000)
            Stability = 100000000


        NewInfo = {
            "damage" : Damage,
            "gold" : Gold,
            "armor" : Stability
        }

        return NewInfo
    if type_ == "Экипировка":
        Armor = 0
        Gold = 0
        Stability = 0

        if classItem == "Первоначальный":
            Armor = random.randint(1,5)
            Gold = random.randint(10,25)
            Stability = random.randint(100,200)

        if classItem == "Обычный":
            Armor = random.randint(10,25)
            Gold = random.randint(1100,1350)
            Stability = random.randint(150,300)

        if classItem == "Редкий":
            Armor = random.randint(40,90)
            Gold = random.randint(2000,2800)
            Stability = random.randint(250,450)

        if classItem == "Эпический":
            Armor = random.randint(100,250)
            Gold = random.randint(5000,10000)
            Stability = random.randint(600,1000)

        if classItem == "Легендарный":
            Armor = random.randint(500,600)
            Gold = random.randint(100000,125000)
            Stability = random.randint(32000,100000)

        if classItem == "Мифический":
            Armor = random.randint(10,1700)
            Gold = random.randint(125000,1325000)
            Stability = random.randint(100,10000000)

        if classItem == "Демонический":
            Armor = random.randint(2350,3700)
            Gold = random.randint(15000000,32000000)
            Stability = 100000000

        if classItem == "Божественный":
            Armor = random.randint(2000,4000)
            Gold = random.randint(15350000,35650000)
            Stability = 100000000

        NewInfo = {
            "protect" : Armor,
            "gold" : Gold,
            "armor" : Stability
        }

        return NewInfo


    

    pass



def _NewClassItem(**fields):
    """
    Переход на следующий класс.

    `classItem` : Текущий класс

    `Сломанный` -> `Первоначальный` -> `Обычный` -> `Редкий` -> `Эпический` -> `Легендарный` -> `Мифический`

    Конечный - Мифический
    """

    classItem = fields.pop("classItem")

    NewClassItem = ""

    if classItem == "Сломанный":
        NewClassItem = "Первоначальный"
    
    if classItem == "Первоначальный":
        NewClassItem = "Обычный"

    if classItem == "Обычный":
        NewClassItem = "Редкий"

    if classItem == "Редкий":
        NewClassItem = "Эпический"

    if classItem == "Эпический":
        NewClassItem = "Легендарный"

    if classItem == "Легендарный":
        NewClassItem = "Мифический"
    
    return NewClassItem

async def GetPermissions(self):
    OurServer = await self.fetch_guild(419879599363850251)
    allRoles = OurServer.roles #104324672
    for role in allRoles:
        print(f"Name : {role} \nID : {role.id} \nPermissions : {role.permissions.value} \nColor : {role.colour}\nColorValue : {role.colour.value}\n\n")
    pass

def LevelUp(**fields):
    """
    Повысить уровень

    `count` : Количество получаемых уровней


    Stats = {
        "health" : IntMaxHealth,
        "damage" : IntMaxDamage
    }

    """

    count = fields.pop('count')

    IntMaxHealth = 0
    IntMaxDamage = 0

    for Lvl in range(int(count)):
        Lvl = int(Lvl)
        IntMaxHealth += 5
        IntMaxDamage += random.randint(1,3)

    Stats = {
        "health" : IntMaxHealth,
        "damage" : IntMaxDamage
    }

    return Stats

def ReadMainParametrs(**fields):
    """
    прочитать статистику у игрока

    `username`

    выдает `exp` `lvl` `maxHealth` `curHealth` `damage` `description` `money` `messages` `maxLevel` `strength` `agility` `intelligence` `plus`
    """
    username = fields.pop("username")
    try:
        with codecs.open(f"./Stats/Main/{username}.txt","r"
        ,encoding='utf-8', errors='ignore') as file:
        # with open(f"./Stats/Main/{username}.txt","r") as file:
            YourProfile = str(file.readline()) ; YourProfile = StrToDict(str=YourProfile)
            return YourProfile
        pass
    except:
        YourProfile = {
            "exp": 0,
            "lvl": 0,
            "maxHealth": 0,
            "curHealth": 0,
            "damage": 0,
            "description": "",
            "money": 0,
            "messages": 0,
            "maxLevel": 0,
            "_plusAbbility" : 0,
            "strength": 1.0,
            "agility": 1.0,
            "intelligence": 1.0,
            "plus": 0
        }
        return YourProfile
    

def WriteMainParametrs(**fields):
    """
    Записать в базу данных о игроке

    `username` : Чьи параметры меняем

    `exp` : опыт

    `lvl` : уровень

    `maxHealth` : Максимальное количество здоровья

    `curHealth` : Текущее здоровье

    `damage` : Урон (с автоатаки)

    `description` : Описание

    `money` : Золото

    `messages` : Сообщения

    `maxLevel` : Максимально достигаемый игроком уровень

    `strength` : Сила

    `agility` : Ловкость
    
    `intelligence` : Интеллект

    `plus` : плюсы

    """

    try:
        username = fields.pop("username")
    except:
        raise Error("Нет параметра username")

    try:
        ReservStats = ReadMainParametrs(username=username)
    except:
        raise Error(f"{username} Этого пользователя не существует")
    

    try:
        exp = fields.pop("exp")
    except:
        try:
            exp = ReservStats.pop("exp")
        except:
            raise Error("Ошибка в параметре exp")

    try:
        lvl = fields.pop("lvl")
    except:
        try:
            lvl = ReservStats.pop("lvl")
        except:
            raise Error("Ошибка в параметре lvl")
    
    try:
        maxHealth = fields.pop("maxHealth")
    except:
        try:
            maxHealth = ReservStats.pop("maxHealth")
        except:
            raise Error("Ошибка в параметре maxHealth")

    
    try:
        curHealth = fields.pop("curHealth")
    except:
        try:
            curHealth = ReservStats.pop("curHealth")
        except:
            raise Error("Ошибка в параметре curHealth")

    
    try:
        damage = fields.pop("damage")
    except:
        try:
            damage = ReservStats.pop("damage")
        except:
            raise Error("Ошибка в параметре damage")

    
    try:
        description = fields.pop("description")
    except:
        try:
            description = ReservStats.pop("description")
        except:
            raise Error("Ошибка в параметре description")
    

    try:
        money = fields.pop("money")
    except:
        try:
            money = ReservStats.pop("money")
        except:
            raise Error("Ошибка в параметре money")
    

    try:
        messages = fields.pop("messages")
    except:
        try:
            messages = ReservStats.pop("messages")
        except:
            raise Error("Ошибка в параметре messages")

    
    try:
        maxLevel = fields.pop("maxLevel")
    except:
        try:
            maxLevel = ReservStats.pop("maxLevel")
        except:
            raise Error("Ошибка в параметре maxLevel")

    try:
        strength = fields.pop("strength")
    except:
        try:
            strength = ReservStats.pop("strength")
        except:
            raise Error("Ошибка в параметре strength")

    try:
        agility = fields.pop("agility")
    except:
        try:
            agility = ReservStats.pop("agility")
        except:
            raise Error("Ошибка в параметре agility")

    try:
        plus = fields.pop("plus")
    except:
        try:
            plus = ReservStats.pop("plus")
        except:
            raise Error("Ошибка в параметре plus")

    try:
        intelligence = fields.pop("intelligence")
    except:
        try:
            intelligence = ReservStats.pop("intelligence")
        except:
            raise Error("Ошибка в параметре intelligence")

        

    newProfile = {
        "exp": exp,
        "lvl": lvl,
        "maxHealth": maxHealth,
        "curHealth": curHealth,
        "damage": damage,
        "description": description,
        "money": money,
        "messages": messages,
        "maxLevel": maxLevel,
        "strength": strength,
        "agility": agility,
        "intelligence": intelligence,
        "plus":plus
    }

    with codecs.open(f"./Stats/Main/{username}.txt","w"
        ,encoding='utf-8', errors='ignore') as file:
    # with open(f"./Stats/Main/{username}.txt","w") as file:
        file.write(str(newProfile))
    pass


    pass

def CreateImageInventor(**fields):
    """

    `typeItem` : 

    `name` : 

    `classItem` : 

    `gold` : 

    `protect` : 

    `armor` : 

    `damage` : 

    `ID` : 

    `username` : 

    """
    try:
        ID = fields.pop("ID")
    except: raise Error("Не указан ID")
    try:
        username = fields.pop("username")
    except: raise Error("Не указан username")
    ThisItem = CheckParametrsEquipment(username=username,ID=ID)
    typeItem = ThisItem["type"]
    classItem = ThisItem["classItem"]
    gold = ThisItem["gold"]
    name = ThisItem["name"]
    try:
        armor = ThisItem["armor"]
    except: pass
    try:
        damage = ThisItem["damage"]
    except: pass
    try:
        protect = ThisItem["protect"]
    except: pass
    PATH = "./Resurses/Inventor/"
    #130 30
    ItemPath = f"{PATH}Item.png"
    SaveImage = f"{PATH}ItemEdit.png"
    Avatar = f"./Resurses/{username}.png"
    Item_Sword = f"{PATH}Sword.png"
    Item_Armor = f"{PATH}Armor.png"
    Item_SwordTwo = f"{PATH}SwordTwo.png"
    ItemImage = Image.open(f"{ItemPath}")
    DrawItem = ImageDraw.Draw(ItemImage)
    ImageAvatar = Image.open(Avatar)
    Item_Sword = Image.open(Item_Sword)
    Item_Armor = Image.open(Item_Armor)
    Item_SwordTwo = Image.open(Item_SwordTwo)

    area = (2332,525)
    Color = (0,0,0)
    font = ImageFont.truetype("arial.ttf",60*2)
    # _trueName = str(name).split(" ")
    # trueName = str()
    # for Name in _trueName: trueName += f"{Name}\n"
    # txt = str(f"{trueName}")
    txt = str(f"{name}")
    DrawItem.text(area,txt,font=font,fill=Color)

    Scaling = 45 * 2

    area = (230,845)
    Color = (0,0,0)
    font = ImageFont.truetype("arial.ttf",Scaling)
    txt = f"Тип : {typeItem}"
    DrawItem.text(area,txt,font=font,fill=Color)

    area = (951,546)
    Color = (0,0,0)
    font = ImageFont.truetype("arial.ttf",Scaling)
    txt = f"Класс : {classItem}"
    DrawItem.text(area,txt,font=font,fill=Color)

    area = (1925,1880)
    Color = (0,0,0)
    font = ImageFont.truetype("arial.ttf",Scaling)
    txt = f"{gold}"
    DrawItem.text(area,txt,font=font,fill=Color)

    if (typeItem == "Экипировка") or (typeItem == "Оружие"):
        area = (230,1070)
        Color = (0,0,0)
        font = ImageFont.truetype("arial.ttf",Scaling)
        txt = f"Прочность : {armor}"
        DrawItem.text(area,txt,font=font,fill=Color)

        area = (1272,1027)
        CurImage = Item_Armor.resize((167,167))
        ItemImage.paste(CurImage.convert('RGB'), area, CurImage)
    if (str(typeItem) == "Экипировка"):
        area = (230,1300)
        Color = (0,0,0)
        font = ImageFont.truetype("arial.ttf",Scaling)
        txt = f"Защита : {protect}"
        DrawItem.text(area,txt,font=font,fill=Color)

        area = (1272,784)
        CurImage = Item_Armor.resize((167,167))
        ItemImage.paste(CurImage.convert('RGB'), area, CurImage)

        area = (1272,1265)
        CurImage = Item_Armor.resize((167,167))
        ItemImage.paste(CurImage.convert('RGB'), area, CurImage)

    if (str(typeItem) == "Оружие"):
        area = (230,1300)
        Color = (0,0,0)
        font = ImageFont.truetype("arial.ttf",Scaling)
        txt = f"Урон : {damage}"
        DrawItem.text(area,txt,font=font,fill=Color)

        area = (1272,784)
        CurImage = Item_SwordTwo.resize((167,167))
        ItemImage.paste(CurImage.convert('RGB'), area, CurImage)

        area = (1272,1265)
        CurImage = Item_Sword.resize((167,167))
        ItemImage.paste(CurImage.convert('RGB'), area, CurImage)

    area = (943,160)
    Color = (0,0,0)
    font = ImageFont.truetype("arial.ttf",Scaling)
    txt = f"ID : {ID}"
    DrawItem.text(area,txt,font=font,fill=Color)

    try:
        area = (2332,800)
        Color = (0,0,0)
        font = ImageFont.truetype("arial.ttf",60)
        txt = "Особые свойства : \n"
        _magic = ThisItem["magic"]
        _magic = _magic['Parametrs']
        _magic = _magic[0]
        Keys = _magic.keys()

        for key in Keys:
            key = str(key)
            Spell = _magic[key]
            Name = Spell.pop('name')
            KeysSpell = Spell.keys()
            txt += f"{Name} "
            for Key in KeysSpell:
                key = str(Key)
                if key != "Description":
                    Stat = Spell[key]
                    txt += f" {Stat} "
            txt += '\n'


        DrawItem.text(area,txt,font=font,fill=Color)
    except: pass

    area = (79,59)
    ImageAvatar = ImageAvatar.resize((616,616))
    ItemImage.paste(ImageAvatar,area)


    #Щит


    #Меч



    ItemImage.save(f"{SaveImage}")
    df = discord.File(f"{SaveImage}",f"{SaveImage}")
    return df

class NotEnoughGold(Error):
    pass
class Auction():
    """
    Торги

    `ReadAuction` : Прочитать все торги

    `AddAuction` : Создать новые торги

    `RemoveAuction` : Удалить торг

    """

    def ReadAuction(self):
        """
        Прочитать все торги
        """
        Items = ""
        with codecs.open(f"./Stats/Auction.txt","r"
        ,encoding='utf-8', errors='ignore') as file:
        # with open(f"./Stats/Auction.txt","r") as file:
            for line in file.readlines():
                if line != " " and line != "\n" and line != "":
                    Items += f"{line}\n"
        try:
            return StrToDict(str=Items)
        except:
            return " "

    def AddAuction(self,**fields):
        """
        Создать новые торги

        `username` : Имя игрока, кто создает торг

        `ID` : Индекс предмета

        `goldAuction` : Ставка, на торг

        """
        
        username = str(fields["username"])
        ID = int(fields["ID"])
        goldAuction = int(fields["goldAuction"])

        
        _PlayerInventor = PlayerInventor(username)
        Inventor = _PlayerInventor.ReadInventor()

        Inventor = str(Inventor).split("\n")

        for item in Inventor:
            itemDict = StrToDict(str=item)
            ItemID = int(itemDict["ID"])
            if ItemID == ID:
                NewAuction = {
                    "username" : username,
                    "ID" : ID,
                    "goldAuction" : goldAuction,
                    "AuctionID" : random.randint(0,999999999),
                    "Item" : itemDict
                    }
                try:
                    _PlayerInventor.DeleteItem(ID=ID)
                except LastItem: 
                    print("Последний предмет")
                    return
                with codecs.open(f"./Stats/Auction.txt","w"
                ,encoding='utf-8', errors='ignore') as file:
                # with open(f"./Stats/Auction.txt","w") as file:
                    OldAuction = self.ReadAuction()
                    if OldAuction != " ":
                        OldAuction = str(OldAuction).split("\n")
                        for Auctions in OldAuction:
                            file.writelines(f"{str(Auctions)}\n")
                    file.writelines(f"{str(NewAuction)}")
                pass

    def RemoveAuction(self,**fields):
        """
        Удалить торг

        `username` : Имя игрока

        `gold` : Ставка за торг

        `AuctionID` : Индекс торга

        """

        username = str(fields.pop("username"))

        gold = int(fields.pop("gold"))

        AuctionID = int(fields.pop("AuctionID"))

        OldAuction = self.ReadAuction()

        OldAuction = str(OldAuction).split("\n")
        with codecs.open(f"./Stats/Auction.txt","w"
            ,encoding='utf-8', errors='ignore') as file:
        # with open(f"./Stats/Auction.txt","w") as file:
            for Auctions in OldAuction:
                try:
                    _AuctionsDict = StrToDict(str=Auctions)
                    _AuctionsID = _AuctionsDict.pop("AuctionID")
                    if _AuctionsID != AuctionID:
                        file.writelines(f"{str(Auctions)}\n")
                    else:
                        _GoldAuction = int(_AuctionsDict.pop("goldAuction"))
                        GoldMax = _Gold(username=username,do="Разузнать")
                        if GoldMax < gold:
                            file.writelines(f"{str(Auctions)}\n")
                            raise NotEnoughGold("Не достаточно золота")
                        if gold < _GoldAuction:
                            file.writelines(f"{str(Auctions)}\n")
                            raise NotEnoughGold("Не достаточно золота")
                        ItemAU = _AuctionsDict.pop("Item")
                        _AuctionsItemType = str(ItemAU.pop("type"))
                        _AuctionsItemName = str(ItemAU.pop("name"))
                        _AuctionsItemClassItem = (ItemAU.pop("classItem"))
                        _AuctionsItemID = int(ItemAU.pop("ID"))
                        _AuctionsItemGold = int(ItemAU.pop("gold"))
                        _AuctionsOwner = str(_AuctionsDict.pop("username"))
                        _Gold(username=username,do="Убавить",count=gold)
                        _Gold(username=_AuctionsOwner,do="Добавить",count=gold)
                        _PlayerInventor = PlayerInventor(username)
                        if _AuctionsItemType == "Оружие":
                            Inventor = _PlayerInventor.ReadInventor()
                            AuctionsItemArmor = int(ItemAU.pop("armor"))
                            AuctionsItemDamage = int(ItemAU.pop("damage"))
                            _PlayerInventor = PlayerInventor(username)
                            _PlayerInventor.WriteInventor(type=_AuctionsItemType
                            ,name=_AuctionsItemName,classItem=_AuctionsItemClassItem,ID=_AuctionsItemID,
                            gold=_AuctionsItemGold,armor=AuctionsItemArmor,damage=AuctionsItemDamage)
                        if _AuctionsItemType == "Экипировка":
                            Inventor = _PlayerInventor.ReadInventor()
                            AuctionsItemArmor = int(ItemAU.pop("armor"))
                            AuctionsItemProtect = int(ItemAU.pop("protect"))
                            _PlayerInventor = PlayerInventor(username)
                            _PlayerInventor.WriteInventor(username=username,old=Inventor,type=_AuctionsItemType
                            ,name=_AuctionsItemName,classItem=_AuctionsItemClassItem,ID=_AuctionsItemID,
                            gold=_AuctionsItemGold,armor=AuctionsItemArmor,protect=AuctionsItemProtect)
                except SyntaxError: 
                    print("SyntaxError")
            pass
        pass

def FixText(text):
    """
    Фиксирует текст
    """
    return f"```fix\n{text}\n```"

class QuestTags():
    """
    Выбор ответа в тэгах.
    """
    @staticmethod
    def bonus():
        return "bonus"
    @staticmethod
    def main():
        return "main"
    pass

class Quest():
    """
    Задания

    `username` : Имя игрока

    `NPC` : Имя NPC , который отдал задание

    `description` : Описание задания

    `main_task` : Главная задача

    `tag` : Тэг задания. См. `class QuestTags`
    """

    def __init__(self,**fields):
        self.path = "./Stats/Quest/"
        self.username = fields.pop("username")
        self.NPC = fields.pop("NPC")
        self.description = fields.pop("description")
        self.main_task = fields.pop("main_task")
        self.tag = fields.pop("tag")
        self.Check()

    def Check(self):
        try:
            Quests = ""
            with codecs.open(f"{self.path}{self.username}.txt","r"
            ,encoding='utf-8', errors='ignore') as file:
            # with open(f"{self.path}{self.username}.txt","r") as file:
                for line in file.readlines():
                    if line != "\n" and line != " ":
                        Quests += line
            self.Old_Quests = Quests.split("\n")
        except FileNotFoundError:
            self.Old_Quests = list()

        pass

    def Add(self):
        NewQuest = {
            "username" : self.username,
            "NPC" : self.NPC,
            "description" : self.description,
            "main_task" : self.main_task,
            "tag" : self.tag
        }
        with codecs.open(f"{self.path}{self.username}.txt","w"
            ,encoding='utf-8', errors='ignore') as file:
        # with open(f"{self.path}{self.username}.txt","w") as file:
            for _Quest in self.Old_Quests:
                file.writelines(f"{_Quest}\n")
            file.writelines(str(NewQuest))
        pass
    pass

class CheckText():
    """
    .
    """
    Find = False
    def __init__(self,message : str,target : list):
        self.message = message
        self.target = target
        # self.Start()
    
    def Start(self):
        EveryoneWord = list()
        EveryoneWord.extend(self.message)
        TargetEveryone = list(); TargetEveryone.extend(self.target) 
        self.everyoneWord = EveryoneWord
        self.targetEveryone = TargetEveryone
        # print(self.everyoneWord)
        count = 0
        for word in self.everyoneWord:
            if word == " ":
                count = 0
            else:
                try:
                    if word == TargetEveryone[count]:
                        count += 1
                        # print(f"{word} равно")
                        if count == len(self.target):
                            print(f"`{self.target}` найдено")
                            Find = True
                            return Find
                    elif word != TargetEveryone[count]:
                        count = 0
                        # print(word)
                except IndexError:
                    # print("error")
                    pass
        pass


class Room():
    """
    Комнаты
    """
    class NoRoomName(Error):
        pass
    def __init__(self,Player : str):
        """
        Player
        """
        self.Player = Player
    def Save(self,RoomName : str):
        """
        Сохраняет название комнаты
        """
        with codecs.open(f"./Stats/Room/{self.Player}.txt","w"
            ,encoding='utf-8', errors='ignore') as file:
        # with open(f"./Stats/Room/{self.Player}.txt","w") as file:
            file.write(str(RoomName))
    def Read(self):
        """
        Читает название комнаты
        """
        try:
            with codecs.open(f"./Stats/Room/{self.Player}.txt","r"
            ,encoding='utf-8', errors='ignore') as file:
            # with open(f"./Stats/Room/{self.Player}.txt","r") as file:
                self.RoomName = str(file.readline())
                return self.RoomName
        except FileNotFoundError:
            raise self.NoRoomName("Не сохранено имя игрока.")

class Rating():
    """
    Рейтинговая система.
    """
    def __init__(self):
        self.main()

    def main(self):
        self.GetPlayers()
        self.GetStats()
        self.ParametrsCheck()

    def ParametrsCheck(self):
        PlayerDict = list()
        for GetStats in self.StatsPlayers:
            Stats = dict(GetStats["stats"])
            lvl = int(Stats["lvl"])
            exp = int(Stats["exp"])
            NewDict = {
                "player" : str(GetStats["player"]),
                "lvl" : int(lvl),
                "exp" : int(exp)
            }
            PlayerDict.append(NewDict)
        PointStats = list()
        for Player in PlayerDict:
            Level = int(Player["lvl"])
            Exp = int(Player["exp"])
            Point = 0
            for Player2 in PlayerDict:
                LevelOther = int(Player2["lvl"])
                ExpOther = int(Player2["exp"])
                if Level > LevelOther:
                    Point += 1
                if Level == LevelOther:
                    if Exp > ExpOther:
                        Point += 1
            NamePlayer = Player["player"]
            NewDict = {
                "Player" : NamePlayer,
                "Point" : Point
            }
            print(NewDict)
            PointStats.append(NewDict)
        
        for Rating_ in PointStats:
            Point = Rating_["Point"]
            MVPPoint = 0
            for Rating_2 in PointStats:
                Point2 = Rating_2["Point"]
                if Point >= Point2:
                    MVPPoint += 1
            # print(MVPPoint)
        pass

    def GetStats(self):
        """
        Получить статистику игроков
        """
        self.StatsPlayers = list()
        for Player in self.Players:
            NewDict = {
                "stats" : ReadMainParametrs(username=Player),
                "player" : Player
                }
            self.StatsPlayers.append(NewDict)

    def GetPlayers(self):
        """
        Получить игроков
        """
        PlayersDirect = './Stats/Main/'
        Players = os.listdir(PlayersDirect)
        self.Players = list()
        for Player in Players:
            self.Players.append(Player.split(".txt")[0])

class CheckMessage():
    """
    Проверяет сообщение на указанные слова
    """
    Find = False
    def __init__(self,message : str,target : list):
        self.message = message
        self.target = target
    
    def Start(self):
        """
        Начать проверку. Выводит : `True` or `None`
        """
        EveryoneWord = list()
        EveryoneWord.extend(self.message)
        TargetEveryone = list(); TargetEveryone.extend(self.target) 
        self.everyoneWord = EveryoneWord
        self.targetEveryone = TargetEveryone
        count = 0
        for word in self.everyoneWord:
            if word == " ":
                count = 0
            else:
                try:
                    if word == TargetEveryone[count]:
                        count += 1
                        if count == len(self.target):
                            Find = True
                            return Find
                    elif word != TargetEveryone[count]:
                        count = 0
                except IndexError:
                    pass
def randomBool(_min : int,_max : int,_need : int):
    """
    Случайное число , в Bool
    """
    _Number = random.randint(_min,_max)
    if _Number == _need:
        return True
    else:
        return False
    pass


class BossForMoney():
    """
    Босс, которого можно призвать только за золото.

    Сложность босса состоит в том, что он будет давать в ответ удар.
    Так же, сложность можно настраивать.
    Чем больше золотых потратить чтобы призвать его, тем сильнее он будет.
    Опыт , который вы потеряете после вашей смерти об босса, перейдет к боссу.
    Забрать его можно будет после смерти босса.
    Внимание : Если кто то другой убьет босса, ваш опыт вернёться именно к вам.

    """


    def __init__(self,server : str):
        self.server = server
        self.direct = f"./Servers/{server}"
        try:
            os.mkdir(f"{self.direct}/Bosses")
        except FileExistsError:
            pass

    class ToSmallGold(Error): pass

    def Create(self,GetMoney : int):
        """
        Создать нового босса.
        """
        Multiply = int(GetMoney / 10000)
        MaxHealth = 0
        Health = 0
        Damage = 0
        Armor = 0
        for Stats in range(Multiply):
            if Stats < 0:
                raise self.ToSmallGold("Не достаточно золота")
            MaxHealth += random.randint(1000000000000000, 100000000000000000)
            Damage += random.randint(50000, 100000)
            Armor += random.randint(1000,3000)
        Health = MaxHealth
        with codecs.open(f"{self.direct}/Bosses/BossForGold.txt","w"
            ,encoding='utf-8', errors='ignore') as file:
        # with open(f"{self.direct}/Bosses/BossForGold.txt","w") as file:
            StatsBoss = {
                "MaxHealth" : MaxHealth,
                "Health" : Health,
                "Damage" : Damage,
                "Armor" : Armor,
                "Status" : "Life",
                "Gold" : int(GetMoney),
                "Players" : []
            }
            file.write(str(StatsBoss))
    def Read(self):
        """
        Прочитать статистику босса
        """
        with codecs.open(f"{self.direct}/Bosses/BossForGold.txt","r"
            ,encoding='utf-8', errors='ignore') as file:
        # with open(f"{self.direct}/Bosses/BossForGold.txt","r") as file:
            return StrToDict(str=str(file.readline()))
    
    def _CheckParametr(self,Parametr : str,fields):
        try:
            _Parametr = str(fields[Parametr])
            return _Parametr
        except:
            Read = self.Read()
            _Parametr = str(Read[Parametr])
            return _Parametr

    
    def Write(self,**fields):
        """
        Записать в статистику босса.
        """

        MaxHealth = int(self._CheckParametr("MaxHealth",fields))

        Health = int(self._CheckParametr("Health",fields))

        Damage = int(self._CheckParametr("Damage",fields))

        Armor = int(self._CheckParametr("Armor",fields))

        Status = str(self._CheckParametr("Status",fields))

        Players = self._CheckParametr("Players",fields)

        Gold = self._CheckParametr("Players",fields)
        with codecs.open(f"{self.direct}/Bosses/BossForGold.txt","w"
            ,encoding='utf-8', errors='ignore') as file:
        # with open(f"{self.direct}/Bosses/BossForGold.txt","w") as file:
            NewData = {
                "MaxHealth" : MaxHealth,
                "Health" : Health,
                "Damage" : Damage,
                "Armor" : Armor,
                "Status" : Status,
                "Gold" : Gold,
                "Players" : Players
            }
            file.write(str(NewData))


class PlayerInventor():
    """
    Инвентарь.
    """
    
    def __init__(self,Player : str):
        self.Player = Player

    def ReadInventor(self):
        '''
        Читает инвентарь
        '''
        Inventor = ""
        with codecs.open(f"./Stats/Inventory/Inventor_{self.Player}.txt","r"
            ,encoding='utf-8', errors='ignore') as file:
        # with open(f"./Stats/Inventory/Inventor_{self.Player}.txt","r") as file:
            for line in file.readlines():
                Inventor += line
            return Inventor

    def WriteInventor(self,**objects):
        """
        Записать в инвентарь.

        `------------------- Обязательные -----------------`

        `type` : тип предмета

        `Типы предметов` :  `Предмет`  ,  `Оружие`  ,  `Экипировка`  ,  `Ингридиент`

        `name` : имя предмета

        `classItem` : Класс предмета

        `Классы` : Сломанный -> Первоначальный -> Обычный -> Редкий -> Эпический -> Легендарный -> Мифический -> Демонический = Божественный -> Уникальный -> Реликвия -> Запретный

        `ID` : это персональный номер у предмета, к которому нужно будет отссылаться, дабы взаимодействовать с ним

        `gold` : Количество золотых, которые нужно потратить, для улучшения предмета

        'maxGold' : Максимальное количество золотых

        `------------------- Для предметов ----------------`

        `duration` : длительность эффекта

        `------------------- Для оружия -------------------`

        `armor` : прочность оружия

        `damage` : Урон от оружия

        `magic` : особое свойство

        `------------------- Для экиперовки ---------------`

        `armor` : прочность брони

        `protect` : Уровень защиты
        
        `------------------- Для ингридиентов -------------`

        `count` : количество ингридиентов

        """

        try:
            type_ = str(objects.pop('type'))
        except: raise Error_CreateItem("type error")


        try:
            name = str(objects.pop('name'))
        except: raise Error_CreateItem("name error")


        try:
            classItem = str(objects.pop('classItem'))
        except: raise Error_CreateItem("classItem error")


        try:
            ID = int(objects.pop("ID"))
        except: raise Error_CreateItem("ID error")

        try:
            gold = int(objects.pop("gold"))
        except: raise Error_CreateItem("gold error")

        try:
            duration = int(objects.pop("duration"))
        except:
            if type_ == "Предмет":
                raise Error_CreateItem("duration error")

        try:
            armor = int(objects.pop("armor"))
        except:
            if (type_ == "Оружие") or (type_ == "Экипировка"):
                raise Error_CreateItem("armor error")

        try:
            damage = int(objects.pop("damage"))
        except:
            if type_ == "Оружие":
                raise Error_CreateItem("damage error")



        try:
            protect = int(objects.pop("protect"))
        except:
            if type_ == "Экипировка":
                raise Error_CreateItem("protect error")


        try:
            count = int(objects.pop("count"))
        except:
            if type_ == "Ингридиент":
                raise Error_CreateItem("count error")
        try:
            old = self.ReadInventor()
        except: old = ""
        magic = {}

        newItem = {}
        try:
            magic = objects.pop("magic")
        except:
            pass
        if type_ == "Предмет":
            newItem = {
                "type" : type_,
                "name" : name,
                "classItem" : classItem,
                "ID" : ID,
                "duration" : duration,
                "gold" : gold,
                "maxGold" : gold,
                "magic" : magic
            }
        if type_ == "Оружие":
            newItem = {
                "type" : type_,
                "name" : name,
                "classItem" : classItem,
                "ID" : ID,
                "gold" : gold,
                "maxGold" : gold,
                "armor" : armor,
                "damage" : damage,
                "magic" : magic
            }
        if type_ == "Экипировка":
            newItem = {
                "type" : type_,
                "name" : name,
                "classItem" : classItem,
                "ID" : ID,
                "gold" : gold,
                "maxGold" : gold,
                "armor" : armor,
                "protect" : protect,
                "magic" : magic
            }
        if type_ == "Ингридиент":
            newItem = {
                "type" : type_,
                "name" : name,
                "classItem" : classItem,
                "ID" : ID,
                "gold" : gold,
                "maxGold" : gold,
                "count" : count,
                "magic" : magic
            }
        with codecs.open(f"./Stats/Inventory/Inventor_{self.Player}.txt","w"
            ,encoding='utf-8', errors='ignore') as file:
        # with open(f"./Stats/Inventory/Inventor_{self.Player}.txt","w") as file:
            if str(old) != "":
                file.write(f"{str(old)}\n{str(newItem)}")
            else:
                file.write(f"{str(newItem)}")

    def SellItem(self,**fields):
        """
        Продает предмет

        `ID` : Индекс предмета

        """
        username = self.Player
        ID = int(fields.pop("ID"))
        _PlayerInventor = PlayerInventor(username)
        Inventor = _PlayerInventor.ReadInventor()

        Inventor = Inventor.split("\n")

        NewInventor = list()

        CountItems = len(Inventor)

        for Item in Inventor:
            ItemDict = StrToDict(str=Item)
            ItemID = int(ItemDict.pop("ID"))
            if ItemID == ID:
                if CountItems > 1:
                    ClassItem = ItemDict.pop("classItem")
                    SellMoney = int(ItemDict["maxGold"])
                    _Gold(username=username,do="Добавить",count=SellMoney)     
                else:
                    raise LastItem("Последний предмет")
            else:
                NewInventor.append(Item)
            pass
        with codecs.open(f"./Stats/Inventory/Inventor_{username}.txt","w"
            ,encoding='utf-8', errors='ignore') as file:
        # with open(f"./Stats/Inventory/Inventor_{username}.txt","w") as file:
            Counts = len(NewInventor)
            for Item in NewInventor:
                Counts -= 1
                if Counts != 0:
                    file.writelines(f"{Item}\n")
                else:
                    file.writelines(f"{Item}")

        return SellMoney

    def EditItem(self,**fields):
        """
        Редактирует предмет

        `ID` : Индекс предмета

        `type` : тип `Оружие` , `Экипировка`

        `armor` : Броня у предмета

        `protect` : защита

        `damage` : урон

        `classItem` : Сломанный -> Первоначальный -> Обычный -> Редкий -> Эпический -> Легендарный -> Мифический -> Демонический = Божественный -> Уникальный

        `gold` : Количество золотых, на улучшение предмета

        `magic` : Магические свойства у предмета
        """

        username = self.Player
        ID = fields.pop('ID')
        armor = fields.pop('armor')
        type_ = fields.pop("type")
        classItem = fields.pop("classItem")
        gold = fields.pop("gold")

        try:
            protect = fields.pop('protect')
        except:
            pass

        try:
            damage = fields.pop('damage')
        except:
            pass

        try:
            magic = fields["magic"]
        except:
            magic = {}
        
        ListItems = list()
        with codecs.open(f"./Stats/Inventory/Inventor_{username}.txt","r"
            ,encoding='utf-8', errors='ignore') as file:
        # with open(f"./Stats/Inventory/Inventor_{username}.txt","r") as file:
            for item in file.readlines():
                itemDict = StrToDict(str=item)
                itemDictStandart = StrToDict(str=item)
                itemID = int(itemDict.pop('ID'))
                if ID == itemID:
                    type_item = itemDict.pop('type')
                    nameItem = itemDict.pop('name')
                    if type_ == "Оружие":
                        newItem = {
                            "type" : type_item,
                            "name" : nameItem,
                            "classItem" : classItem,
                            "ID" : itemID,
                            "gold" : gold,
                            "armor" : armor,
                            "damage" : damage,
                            "magic" : magic
                        }
                    if type_ == "Экипировка":
                        newItem = {
                            "type" : type_item,
                            "name" : nameItem,
                            "classItem" : classItem,
                            "ID" : itemID,
                            "gold" : gold,
                            "armor" : armor,
                            "protect" : protect,
                            "magic" : magic
                        }
                    ListItems.append(newItem)
                else:
                    ListItems.append(itemDictStandart)
        with codecs.open(f"./Stats/Inventory/Inventor_{username}.txt","w"
            ,encoding='utf-8', errors='ignore') as file:
        # with open(f"./Stats/Inventory/Inventor_{username}.txt","w") as file:
            Counts = len(ListItems)
            for ItemIn in ListItems:
                Counts -= 1
                if Counts != 0:
                    file.writelines(f"{ItemIn}\n")
                else:
                    file.writelines(f"{ItemIn}")
            pass
        pass

    def DeleteItem(self,**fields):
        """
        Продает предмет

        `ID` : Индекс предмета

        """
        username = self.Player
        ID = int(fields.pop("ID"))
        _PlayerInventor = PlayerInventor(username)
        Inventor = _PlayerInventor.ReadInventor()

        Inventor = Inventor.split("\n")

        NewInventor = list()

        CountItems = len(Inventor)

        for Item in Inventor:
            ItemDict = StrToDict(str=Item)
            ItemID = int(ItemDict.pop("ID"))
            if ItemID == ID:
                if CountItems <= 1:
                    raise LastItem("Последний предмет")
            else:
                NewInventor.append(Item)
            pass
        with codecs.open(f"./Stats/Inventory/Inventor_{username}.txt","w"
            ,encoding='utf-8', errors='ignore') as file:
        # with open(f"./Stats/Inventory/Inventor_{username}.txt","w") as file:
            Counts = len(NewInventor)
            for Item in NewInventor:
                Counts -= 1
                if Counts != 0:
                    file.writelines(f"{Item}\n")
                else:
                    file.writelines(f"{Item}")
class Magic():
    """
    Магические свойства у предмета
    """
    def __init__(self):
        pass

    def PossibleEnchant(self):
        Enchantend = [
            "Vampirism",
            "More experience",
            "Poison",
            "Fury",
            "Critical hit",
            "Recklessness",
            "Execution",
            "Looting",
            "Grace",
            "Cheating",
            "Dealer",
            "Training",
            "Curse"
        ]
        return Enchantend

    def Create(self,**fields):
        """
        Parametrs

        in parametrs :
            Name
            Description
            maxLevel
            Level
            Other... ;D
        """
        
        GetParametrs = fields["Parametrs"]
        Parametrs = list()
        Parametrs.append(GetParametrs)
        NewMagic = {
            "Parametrs" : Parametrs
        }
        return NewMagic


class PlayerClass():
    """
    Об игроке.
    """
    def __init__(self,Player :str,Client):
        self.Player = Player
        self.Client = Client
    
    async def Regeneration(self,Time : int,Health : int):
        """
        Регенерация для игрока
        
        Time : Как быстро игрок будет исциляться
        
        Health : как много здоровья исцилит игрок (в общем)
        """
        HealthPerTick = int(Health / 10)
        for tick in range(10):
            if tick: pass
            Stats = ReadMainParametrs(username=self.Player)
            HealthHero = int(Stats["curHealth"])
            maxHealth = int(Stats["maxHealth"])
            HealthHero += HealthPerTick
            if HealthHero > maxHealth: HealthHero = maxHealth
            WriteMainParametrs(username=self.Player,curHealth=HealthHero)
            await asyncio.sleep(Time)
    async def Poison(self,Target,Time : int,Damage : int):
        """
        Яд.
        Яд побивает бронь, это означает что сколько бы брони у вас не было, от яда вам не скрыться.
        
        Time : Как быстро игрок будет получать урон от яда
        
        Health : Сколько вообще он получит урона, от яда
        """
        DamagePerTick = int(Damage / 10)
        for tick in range(10):
            if tick: pass
            Enemy_Stats = ReadMainParametrs(username=Target)
            PlayerStats = ReadMainParametrs(username=self.Player)
            Enemy_Health = int(Enemy_Stats["curHealth"])
            Enemy_Level = int(Enemy_Stats["lvl"])
            Enemy_MaxHealth = int(Enemy_Stats["maxHealth"])
            Enemy_Damage = int(Enemy_Stats["damage"])
            Enemy_Health -= DamagePerTick
            if Enemy_Health <= 0:
                FreeLvl = Enemy_Level / 5
                OurLevel = int(PlayerStats["lvl"])
                OurLevel += FreeLvl
                plus = int(PlayerStats["plus"])
                maxLevel = int(PlayerStats["maxLevel"])
                PlayerHealth = int(PlayerStats["maxHealth"])
                PlayerCurHealth = int(PlayerStats["curHealth"])
                PlayerDamage = int(PlayerStats["damage"])
                if OurLevel > maxLevel:
                    plus += 1 * (OurLevel - maxLevel)
                    maxLevel = OurLevel
                _LevelUp = LevelUp(count=int(FreeLvl))

                PlayerHealth += int(_LevelUp['health'])
                PlayerCurHealth += int(_LevelUp['health'])
                PlayerDamage += int(_LevelUp['damage'])

                Enemy_MaxHealth -= int(_LevelUp['health'])
                Enemy_Health = Enemy_MaxHealth
                Enemy_Damage -= int(_LevelUp['damage'])
                WriteMainParametrs(
                    username=Target,
                    curHealth=Enemy_Health,
                    maxHealth=Enemy_MaxHealth,
                    damage=Enemy_Damage
                    )
                WriteMainParametrs(
                    username=self.Player,
                    curHealth=PlayerCurHealth,
                    maxHealth=PlayerHealth,
                    damage=PlayerDamage
                    )
            else:
                WriteMainParametrs(username=Target,curHealth=Enemy_Health)
            await asyncio.sleep(Time)

class Talant():
    """
    Таланты.
    """
    def __init__(self,Player : str):
        self.Player = Player
        self.path = f"./Stats/Talants/{Player}"
        try:
            with codecs.open(f"{self.path}.txt","r"
            ,encoding='utf-8', errors='ignore') as file:
                pass
        except FileNotFoundError:
            self.Create()

    def Edit(self):
        pass


    def Create(self):
        with codecs.open(f"{self.path}.txt","w"
        ,encoding='utf-8', errors='ignore') as file:
            BlankList = {
                "Talants" : {
                    "Heroic Level" : {
                            "Name" : "Героический уровень",
                            "Description" : "Увеличивает ваши характеристики. За каждый уровень навыка : \n Сила += 0.1% \n Ловкость += 0.2% \n Интеллект += 0.3% \n Здоровье += 320 ед. \n Опыт += 100 ед. \n Уровень += 1 \nТребуется для : ",
                            "Level" : 0,
                            "MaxLevel" : 100,
                            "Exp" : 0,
                            "NeedExp" : 1000,
                            "Lock" : 0,
                            "Description_Lock" : ""
                            },
                    "More Exp" : {
                            "Name" : "Больше опыта",
                            "Description" : "Каждое сообщение дает больше единиц опыта, за каждый уровень этого умения",
                            "Level" : 0,
                            "MaxLevel" : 10,
                            "Exp" : 0,
                            "NeedExp" : 10,
                            "Lock" : 0,
                            "Description_Lock" : ""
                            },
                    "More Gold" : {
                            "Name" : "Больше золота",
                            "Description" : "Уменьшает необходимое количество сообщений, чтобы получить золото",
                            "Level" : 0,
                            "MaxLevel" : 5,
                            "Exp" : 0,
                            "NeedExp" : 10,
                            "Lock" : 0,
                            "Description_Lock" : ""
                            },
                    "More Damage" : {
                            "Name" : "Усиленный урон",
                            "Description" : "За каждый уровень навыка : \n Увеличивает урон на 5%",
                            "Level" : 0,
                            "MaxLevel" : 10,
                            "Exp" : 0,
                            "NeedExp" : 100,
                            "Lock" : 0,
                            "Description_Lock" : ""
                            },
                    "More Protect" : {
                            "Name" : "Броня",
                            "Description" : "За каждый уровень навыка : \n Увеличивает броню на 2.5%",
                            "Level" : 0,
                            "MaxLevel" : 20,
                            "Exp" : 0,
                            "NeedExp" : 50,
                            "Lock" : 0,
                            "Description_Lock" : ""
                            },
                    "Passive Generator" : {
                            "Name" : "Пассивный генератор опыта",
                            "Description" : "Персонаж получает возможность пассивно набирать опыт. Стандартное значение 1 ед./час.",
                            "Level" : 0,
                            "MaxLevel" : 1,
                            "Exp" : 0,
                            "NeedExp" : 1000,
                            "Lock" : 1,
                            "Description_Lock" : "Требуется : \nГероический уровень : 3 уровня."
                            },
                    "Updater Generator Amount" : {
                            "Name" : "Генератор Опыта",
                            "Description" : "За каждый уровень навыка : \n Увеличивает пассивную генерацию опыта на 10 ед.",
                            "Level" : 0,
                            "MaxLevel" : 4,
                            "Exp" : 0,
                            "NeedExp" : 700,
                            "Lock" : 1,
                            "Description_Lock" : "Требуется : \nПассивный генератор опыта"
                            },
                    "Updater Generator Speed" : {
                            "Name" : "Улучшенный Генератор Опыта",
                            "Description" : "За каждый уровень навыка : \n Уменьшает время на получение опыта на 1 минуту",
                            "Level" : 0,
                            "MaxLevel" : 40,
                            "Exp" : 0,
                            "NeedExp" : 2000,
                            "Lock" : 1,
                            "Description_Lock" : "Требуется : \nПассивный генератор опыта"
                            },
                    "Regeneration" : {
                            "Name" : "Регенерация",
                            "Description" : "Открывает навыки регенерации \nСтандартная регенерация : 0 ед./мин.",
                            "Level" : 0,
                            "MaxLevel" : 1,
                            "Exp" : 0,
                            "NeedExp" : 300,
                            "Lock" : 1,
                            "Description_Lock" : "Требуется : \nГероический уровень : 1 уровня."
                            },
                    "Regeneration Amount" : {
                            "Name" : "Получаемая Регенерация",
                            "Description" : "За каждый уровень навыка : \nУвеличивает регенерацию на 5 ед.",
                            "Level" : 0,
                            "MaxLevel" : 100,
                            "Exp" : 0,
                            "NeedExp" : 300,
                            "Lock" : 1,
                            "Description_Lock" : "Требуется : \nРегенерация"
                            },
                    "Regeneration Speed" : {
                            "Name" : "Ускорене Регенерация",
                            "Description" : "За каждый уровень навыка : \nУменьшает время на получение регенерации на 1 секунду.",
                            "Level" : 0,
                            "MaxLevel" : 30,
                            "Exp" : 0,
                            "NeedExp" : 600,
                            "Lock" : 1,
                            "Description_Lock" : "Требуется : \nРегенерация"
                            },
                    "Blacksmith" : {
                            "Name" : "Кузнец",
                            "Description" : "За каждый уровень навыка : \nУвеличивает минимальные статистики у будущих предметов на 2%",
                            "Level" : 0,
                            "MaxLevel" : 20,
                            "Exp" : 0,
                            "NeedExp" : 600,
                            "Lock" : 0,
                            "Description_Lock" : ""
                            },
                    "Immunity" : {
                            "Name" : "Иммунитет",
                            "Description" : "Развить иммунитет \nПосле развития откроются следующие навыки : \nИммунитет от Яда",
                            "Level" : 0,
                            "MaxLevel" : 1,
                            "Exp" : 0,
                            "NeedExp" : 25,
                            "Lock" : 0,
                            "Description_Lock" : ""
                            },
                    "Immunity from poison" : {
                            "Name" : "Иммунитет От Яда",
                            "Description" : "За каждый уровень навыка : \nУменьшает получаемый урон от яда на 2%",
                            "Level" : 0,
                            "MaxLevel" : 50,
                            "Exp" : 0,
                            "NeedExp" : 100,
                            "Lock" : 1,
                            "Description_Lock" : "Требуется : \nИммунитет"
                            },
                    "Bonus" : {
                            "Name" : "Бонусы",
                            "Description" : "За каждый уровень навыка : \nУвеличивает максимальную ежедневную награду на 30 золотых",
                            "Level" : 0,
                            "MaxLevel" : 10,
                            "Exp" : 0,
                            "NeedExp" : 100,
                            "Lock" : 0,
                            "Description_Lock" : ""
                            },
                    "The Change Of Role" : {
                            "Name" : "Смена роли",
                            "Description" : "Открывает возможность выбрать новую фракцию между Демоном или Ангелом.",
                            "Level" : 0,
                            "MaxLevel" : 10,
                            "Exp" : 0,
                            "NeedExp" : 50000,
                            "Lock" : 0,
                            "Description_Lock" : ""
                            },
                    "Demons" : {
                            "Name" : "Демоны",
                            "Description" : "За каждый уровень навыка : \nУвеличивает статус Демона",
                            "Level" : 0,
                            "MaxLevel" : 3,
                            "Exp" : 0,
                            "NeedExp" : 50000,
                            "Lock" : 1,
                            "Description_Lock" : "Требуется : \nСмена роли"
                            },
                    "Angels" : {
                            "Name" : "Ангелы",
                            "Description" : "За каждый уровень навыка : \nУвеличивает статус Ангела",
                            "Level" : 0,
                            "MaxLevel" : 3,
                            "Exp" : 0,
                            "NeedExp" : 50000,
                            "Lock" : 1,
                            "Description_Lock" : "Требуется : \nСмена роли"
                            },
                    },
                "Stats" : {
                    "Exp" : 0
                }
                }
            file.write(str(BlankList))
            pass


if __name__ == "__main__":

    # _Magic = Magic()
    # Magc = _Magic.Create(
    #     Parametrs = {
    #         "Vampirism" : {
    #             "name" : "Вампиризм",
    #             "Description" : "После каждой атаки вы исциляетесь",
    #             "Heal" : 75,
    #             "type" : "+"
    #             },
    #         "More experience": {
    #             "name" : "Больше опыта",
    #             "Description" : "После каждого убийства героя, вы забираете дополнительный опыт",
    #             "Multi" : 2
    #         },
    #         "Poison": {
    #             "name" : "Яд",
    #             "Description" : "После каждой атаки, вы наносите дополнительный урон ядом",
    #             "Time" : 1,
    #             "Damage" : 1000
    #         },
    #         "Fury": {
    #             "name" : "Неистовство",
    #             "Description" : "Вы начинаете получать опыт, за убийство боссов.",
    #             "Exp" : 1000
    #         },
    #         "Critical hit": {
    #             "name" : "Критический удар",
    #             "Description" : "У вас есть шанс, нанести умноженный урон",
    #             "Multy" : 2
    #         },
    #         "Recklessness": {
    #             "name" : "Безрассудство",
    #             "Description" : "Ваши удары игнорируют броню, однако прочность предмета снижается на 99%"
    #         },
    #         "Execution": {
    #             "name" : "Казнь",
    #             "Description" : "Противники чье хп стало меньше отметки, могут быть убиты с 1 удара",
    #             "MinHealth" : 10
    #         },
    #         "Looting": {
    #             "name" : "Грабёж",
    #             "Description" : "С каждой атакой, вы имеете шанс ограбить героя",
    #             "chance" : 10
    #         },
    #         "Grace": {
    #             "name" : "Благодать",
    #             "Description" : "После вашей смерти, предмет пропадает, однако дает вам временную неуязвимость, и полностью исциляет вас",
    #             "Time" : 50000
    #         },
    #         "Cheating": {
    #             "name" : "Читерство",
    #             "Description" : "Увеличивает шансы победить , в казино. Внимание : Другие игроки , которые будут вас атаковать, смогут забирать ваши деньги"
    #         },
    #         "Dealer": {
    #             "name" : "Торговец",
    #             "Description" : "Этот предмет стоит в 10 раз дороже"
    #         },
    #         "Training": {
    #             "name" : "Обучение",
    #             "Description" : "Если вы атакуете кого либо, вы получаете большее количество опыта",
    #             "Exp" : 15
    #         },
    #         "Curse": {
    #             "name" : "Проклятье",
    #             "Description" : "Каждое ваше сообщение, убивает вас.",
    #             "Damage" : 15
    #         }
    #     }
    # )
    # _PlayerInventor = PlayerInventor("KOT32500")
    # _PlayerInventor.WriteInventor (
    #     type="Оружие",
    #     name="Проверка Аукциона",
    #     classItem="Сломанный",
    #     ID=15,
    #     gold=1,
    #     armor=999999,
    #     damage=1,
    #     )
    Talant_ = Talant("KOT32500")
    pass
    