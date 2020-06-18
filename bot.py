import discord
from discord import Permissions as _Permission_
from discord import AudioSource as _AudioSource
from discord import FFmpegPCMAudio
import ffmpeg
import BazaDate
from discord import user
import urllib
from urllib.request import urlopen
import time
import random
import wget
from PIL import Image, ImageDraw , ImageFont
import BotInisializator
import pycparser , cffi , pyasn1
import youtube_dl
import os
from os import path
import botFunctions as Functions
from botFunctions import PlayerInventor
from botFunctions import BossForMoney
from botFunctions import PlayerClass
from botFunctions import CheckMessage
import ast
from bs4 import BeautifulSoup
import lxml
import requests
import datetime
import asyncio
from PIL import Image, ImageDraw , ImageFont
import botFunctions as Functions
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
lst = list()
LvlMvpList = list()


class Error():
    pass
class ErrorInAvatar(Error):
    pass
class ErrorAvatar(BaseException):
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

def Create_quotes(Who : str,Msg : str,Date : str):
    MainMsage = Image.new(mode="RGB",size = (2000 , 1000),color = (0,0,0))

    draw = ImageDraw.Draw(MainMsage)
    
    Avatar = Image.open(f"./Resurses/{Who}.png")
    Avatar = Avatar.resize((500,500))
    area = (100,300)
    MainMsage.paste(Avatar,area)

    area = (700,200)
    Color = (255,255,255)
    font = ImageFont.truetype("arial.ttf",72)
    txt = str(f"{Msg}")
    Latters = list() ; Latters.extend(txt)
    txt = ""
    counts = 0
    #NoIt = ["-","_","=","+","[","]","{","}","'",";",",",".","/",'"']
    countsAll = 0
    for Latt in Latters:
        counts += 1
        if countsAll != 5:
            if counts == 35:
                txt += f"\n{Latt}"
                counts = 0
                countsAll += 1
            else:
                txt += f"{Latt}"
        else:
            txt += f"."
        

    draw.text(area,txt,font=font,fill=Color)
    area = (800,800)
    Color = (255,255,255)
    font = ImageFont.truetype("arial.ttf",72)
    txt = str(f"(C) {Who} \n({Date})")
    draw.text(area,txt,font=font,fill=Color)

    nameSave = "Create_quotes.png"
    MainMsage.save(nameSave)
    df = discord.File(nameSave,nameSave)
    return df

def ProfileBoss(*Stats):
    NowTime = datetime.datetime.today()
    today = Stats[0]
    Boss_MaxHealth = Stats[1]
    Boss_CurHealth = Stats[2]
    Boss_GetGold = Stats[3]
    Boss_Dead = str(Stats[4])
   # print(Boss_Dead)
   # Boss_DeadSplit = Boss_Dead.split()
   # print(Boss_DeadSplit)
   # print(Boss_DeadSplit[0])
    today = today.split("-")

    Time_between_dates_day = int(today[2])
    Time_between_dates_hour = int(today[3])
    Time_between_dates_mins = int(today[4])

    Time_between_dates_day -= NowTime.day
    Time_between_dates_hour -= NowTime.hour
    Time_between_dates_mins -= NowTime.minute

    Time_between_dates_mins *= -1
    Time_between_dates_mins = 20 - Time_between_dates_mins

    StatsBoss = Functions.ReadBossStats()
    NameBoss = StatsBoss.pop("nameFile")
    BackGround = Image.open(f"./Resurses/Bosses/{NameBoss}.png")
    BackGround = BackGround.resize((800,600))
    BackGroundDraw = ImageDraw.Draw(BackGround)

    nameSave = "TheBoss.png"


    if Boss_Dead == "No":
        area = (270,230)
        font = ImageFont.truetype("arial.ttf",35)
        Color = (42,0,0)
        BackGroundDraw.text(area,f"{str(Boss_GetGold)} золотых",font=font,fill=Color)

        StartX = 100
        StartY = 275

        EndX = (((Boss_CurHealth * 100) / Boss_MaxHealth) * 7)
        EndY = 374
        RedRand = random.randint(0,255)
        GreenRand = random.randint(0,255)
        BlueRand = random.randint(0,255)
        ColorSlider = ( RedRand , GreenRand , BlueRand )
        for XPos in range(int(EndX - StartX)):
            for YPos in range(int(EndY - StartY)):
                BackGround.putpixel((StartX + XPos,StartY + YPos),ColorSlider)

        area = (105,300)
        font = ImageFont.truetype("arial.ttf",40)
        Color = (42,0,0)
        BackGroundDraw.text(area,f"{str(Boss_CurHealth)} / {str(Boss_MaxHealth)} ед. здоровья",font=font,fill=Color)
        Color = (0,0,0)
        area = [(99,274),(701,274)]
        BackGroundDraw.line(area,fill=Color,width=1)
        area = [(701,274),((701,375))]
        BackGroundDraw.line(area,fill=Color,width=1)
        area = [(701,375),((99,375))]
        BackGroundDraw.line(area,fill=Color,width=1)
        area = [(99,375),((99,274))]
        BackGroundDraw.line(area,fill=Color,width=1)

        pass


    if Boss_Dead == "Yes":
        area = (50,280)
        font = ImageFont.truetype("arial.ttf",80)
        Color = (84,0,0)
        BackGroundDraw.text(area,f"БОСС ПОВЕРЖЕН",font=font,fill=Color)

        area = (100,230)
        font = ImageFont.truetype("arial.ttf",35)
        Color = (42,0,0)
        killer = StatsBoss.pop("killer")
        BackGroundDraw.text(area,f"{str(killer)} нанёс последний удар",font=font,fill=Color)

    area = (500,400)
    font = ImageFont.truetype("arial.ttf",20)
    Color = (115,100,150)
    BackGroundDraw.text(area,f"Осталось : {Time_between_dates_day}D:{Time_between_dates_hour}H:{Time_between_dates_mins}M",font=font,fill=Color)


    BackGround.save(nameSave)

    discordFile = discord.File(nameSave,nameSave)

    return discordFile
def _WriteMainStats(_UserName_,*age):
    f = open("./Stats/Main/" + _UserName_ + ".txt","w")
    for target_list in range(len(age)):
        f.writelines(str(age[target_list] + "\n"))
    f.close()

def FixText(text):
    """
    Фиксирует текст
    """
    return f"```fix\n{text}\n```"
    
def StrToDict(**fields):
    """
    `str` : текст который нужно будет конвентировать в Dict
    """
    _str = str(fields.pop('str'))
    NwDict = ast.literal_eval(f'{_str}') ; NwDict = dict(NwDict)
    return NwDict

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


Resurses = "./Resurses/"
def profileEdit(_UserName_):
    """
    Меняет профиль игрока. Относиться к команде Profile


    Вход :
        _UserName_ = Имя игрока. Str формат
    Выход :
        Файл = Discord.File
    """
    # MainStats = _readStats(_UserName_)
    MainStats = Functions.ReadMainParametrs(username=_UserName_)
    IntCurExp = int(MainStats.pop("exp"))
    IntCurLvl = int(MainStats.pop("lvl"))
    IntMaxHealth = int(MainStats.pop("maxHealth"))
    IntCurHealth = int(MainStats.pop("curHealth"))
    IntMaxDamage = int(MainStats.pop("damage"))
    Description = str(MainStats.pop("description"))
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
    
    ShopAgent = Functions.ReadMainParametrs(username=_UserName_)
    Messages = int(ShopAgent.pop("messages"))
    Gold = int(ShopAgent.pop("money"))
    try:
        BackGround = Image.open(f"{Resurses}BackGround_{_UserName_}.png")
    except: BackGround = Image.open(f"{Resurses}BackGround_StandartBackGround.png")

    img = Image.open(Resurses + "Main.png")
    try:
        N_Ava = Image.open(Resurses + _UserName_ + ".png")
    except:
        raise ErrorAvatar("Отсустует аватарка")

    Ava = N_Ava.resize((264,264)) #76 76

    draw = ImageDraw.Draw(img)
    count = 10
    counts = 0
    ElseCount = 0
    Scaling = 50
    for target_list in range(int(IntCurLvl)):
        if target_list < -5:
            print("ERROR")
        counts += 1
        if counts >= int(count):
            count = str(count) + "0"
            counts = 0
            ElseCount += 5
            Scaling -= 1

    areaT = (163 - ElseCount,309) #121 153
    font = ImageFont.truetype("arial.ttf",Scaling)
    draw.text(areaT,str(IntCurLvl),font=font,fill="black")



    #AgentConfig = _AgentReadConfig(_UserName_)

    area = (370,155)
    Color = (200,210,255)
    # Color = AgentConfig
    font = ImageFont.truetype("arial.ttf",100)
    draw.text(area,_UserName_,font=font,fill=Color)
    try:
        Item_ID = Functions.ReadEquipment(username=_UserName_,type="Экипировка")
        ItemProtect = Functions.CheckParametrsEquipment(username=_UserName_,ID=Item_ID)
        protect = ItemProtect["protect"]
        area = (570 - 20,289 - 13)
        Color = (0,0,0)
        font = ImageFont.truetype("arial.ttf",35)
        txt = str(f"Здоровье : {str(IntCurHealth)} ед./ {str(IntMaxHealth)} ({protect})")
        draw.text(area,txt,font=font,fill=Color)
    except:
        area = (570 - 20,289 - 13)
        Color = (0,0,0)
        font = ImageFont.truetype("arial.ttf",35)
        txt = str(f"Здоровье : {str(IntCurHealth)} ед./ {str(IntMaxHealth)}")
        draw.text(area,txt,font=font,fill=Color)

    area = (570 - 20,341 - 13)
    Color = (0,0,0)
    font = ImageFont.truetype("arial.ttf",35)
    try:
        DmgItemID = Functions.ReadEquipment(username=_UserName_,type="Оружие")
        Item = Functions.CheckParametrsEquipment(username=_UserName_,ID=DmgItemID)
        DamageItem = Item.pop('damage')
    except:
        DamageItem = 0
    
    txt = str(f"Урон : {str(IntMaxDamage)} +({DamageItem}) ед.")
    draw.text(area,txt,font=font,fill=Color)


    #Slider Exp
    # 686 = 100%
    # 342 = 0%
    # 35% 
    # 500 = 35%
    EndPoint = 686 - 342
    EndPoint /= 100
    Procent = IntCurExp * 100
    Procent /= IntCurLvl * 5
    EndPoint *= Procent
    EndPoint += 342
    fstPoints = (342,761,EndPoint,761)
    # EndPoints = (686,743,686,780)
    
    Color = (255,0,255)
    draw.line(fstPoints,fill=Color,width=37)
    #Slider Exp
    
    area = (380,743)
    Color = (0,0,0)

    font = ImageFont.truetype("arial.ttf",35)
    txt = str(f"Опыт : {IntCurExp} / {IntCurLvl * 5}")
    draw.text(area,txt,font=font,fill=Color)

    Main_characteristics = Functions.ReadMainParametrs(username=_UserName_)

    strength = float(Main_characteristics.pop("strength"))
    agility = float(Main_characteristics.pop("agility"))
    intelligence = float(Main_characteristics.pop("intelligence"))
    plus = int(Main_characteristics.pop("plus"))
    if plus > 0:
        area = (700,700)
        Color = (100,110,90)
        font = ImageFont.truetype("arial.ttf",30)
        txt = str(f"Талант очки : {plus}")
        draw.text(area,txt,font=font,fill=Color)


    Color = (255,100,0)
    area = (38,393)
    font = ImageFont.truetype("arial.ttf",50)
    txt = str(f"Сила : \n{strength}")
    draw.text(area,txt,font=font,fill=Color)
    # draw.line((25 - 5,195,100 - 5,195),fill=Color,width=5)

    Color = (0,255,0)
    area = (38,471)
    font = ImageFont.truetype("arial.ttf",50)
    txt = str(f"Ловкость : \n{agility}")
    draw.text(area,txt,font=font,fill=Color)

    Color = (0,255,255)
    area = (38,570)
    font = ImageFont.truetype("arial.ttf",50)
    txt = str(f"Интеллект : \n{intelligence}")
    draw.text(area,txt,font=font,fill=Color)

    
            
    

    area = (570 - 20,393 - 13)
    Color = (0,0,0)
    font = ImageFont.truetype("arial.ttf",35)
    txt = str("Золота : " + str(Gold) + " / " + str(Messages))
    draw.text(area,txt,font=font,fill=Color)

    Color = (0,0,0)
    The_number_of_letters = list()

    area = (380,500)
    font = ImageFont.truetype("arial.ttf",10 + 50)
    txt = str(Description)
    draw.text(area,txt,font=font,fill=Color)

    area = (380,470)
    font = ImageFont.truetype("arial.ttf",35)
    txt = str("О себе : \n")
    draw.text(area,txt,font=font,fill=Color)

    areaAva = (46,8)

    img.paste(Ava,areaAva)
    nameSave = "StatsPl.png"
    BackGround = BackGround.resize((1000,1450)) #(358,481)
    area = (0,550)
    
    BackGround.paste(img.convert('RGB'), area, img)
    BackGround.save(nameSave)

    sf = discord.File(nameSave,nameSave)
    return sf

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

def _BuyItem(_Cost_,_CurGold_,_Count_):
    """
    Покупаем предмет
    
        Вход :
            _Cost_ = Стоимость предмета
            _CurGold_ = Текущее количество золота, у игрока
            _Count_ = Количество предметов, которых нужно купить
        Выход :
            Количество покупок
            Сообщение в str форме. Разрез делать по (^)
            Текущее количество золота.
    """
    CountBuy = 0
    returnStr = ""
    for target_list in range(int(_Count_)):
        if _CurGold_ >= _Cost_:
            CountBuy += 1
            _CurGold_ -= _Cost_
        if target_list < 0:
            returnStr += ("Количество не может быть меньше 1")
    if _CurGold_ < _Cost_:
        returnStr += ("У вас недостаточно золота. \nВсего количесто предметов : " + str(CountBuy))
    else:
        returnStr += ("Все предметы, были успешно куплены")
    return CountBuy , returnStr , _CurGold_

_VoiceClient = None
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
    try:
        client.run(BazaDate.token)
    except: 
        print("Нет подключения к интернету")
class MyClient(discord.Client):
    _VoiceClient = None
    async def Dialog(self,message):
        if message.author == self.user:
            return
        _Channel_ = discord.channel.TextChannel
        _Message_ = discord.message.Message
        try:
            _Channel_ = await self.fetch_channel(message.channel.id)
            _Message_ = await _Channel_.fetch_message(message.id)
        except:
            pass

        RandomSaying = random.randint(0,3)

        msg =  message.content
        msgSP = msg.split()
        CurCommand = ""

        try:
            CurCommand = msgSP[0]
            CurCommand = str.upper(CurCommand)
        except IndexError:
            pass
        
        CurCommandPlayer = "" ; print(CurCommandPlayer,end="")
        UserName_ = message.author.name
        UserName_ = str.split(UserName_)
        UserName__ = str()
        for word in UserName_:
            UserName__ += word
        UserName_ = str(UserName__)
        try:
            CurCommandPlayer = msgSP[1]
            pass
        except IndexError:
            pass

        _CheckMessage = CheckMessage(str(msg).upper(),"gachi".upper())

        IsGachi = _CheckMessage.Start()

        if IsGachi == True:
            await message.delete()
            return

        if RandomSaying == 1:
            SavedChat = self.Chat.SavedChat()
            Status = SavedChat["Status"]
            messages = Functions.ReadWords(message.channel.guild.name,Status)
            try:
                Step = int(CurCommandPlayer)
                await message.channel.send(Functions.FutureMessageDef(message=messages,step=Step))
            except:
                pass

        if CurCommand == "G":
            try: await _Message_.delete()
            except: pass
            try:
                Step = int(CurCommandPlayer)
            except: Step = random.randint(1,30)
            try:
                Status = []
                Chat = self.Chat
                SavedChat = Chat.SavedChat()
                Status = SavedChat["Status"]
                msg = self.Gabriel.Message(Step,message.channel.guild.name,Status)
            except self.Gabriel.TooManyWords:
                await message.channel.send("Столько слов я не знаю ;c",delete_after=5)
                return
            try:
                await message.channel.send(msg)
            except discord.errors.HTTPException:
                await message.channel.send(f"Столько слов я не могу отправить ;c",delete_after=5)
            
        else:
            SavedChat = self.Chat.SavedChat()
            ChannelPossible = SavedChat["Activity"]
            if _Channel_.id in ChannelPossible:
                Commands = [
                    'PROFILE','ПРОФИЛЬ','P','П',
                    'Ы',
                    'ATTACK','A','АТАКА','АТКОВАТЬ','АТАКУЮ',
                    'ABOUT_ME',
                    'NEW_AVATAR',
                    'NEW_BACKGROUND',
                    'DELETEINFO',
                    'TOP',
                    'INV',
                    'WEAR',
                    'UPGRADE_ITEM',
                    'G','GABRIELE',"GS",
                    'ГАБРИЭЛЬ',
                    'КУПИТЬ','BUY','К','B',
                    'TALANT',"ТАЛАНТ",
                    "SELL_ITEM","S_I",
                    "EVENT","E","Е","ИВЕНТ",
                    "AU","AUCTION","АУКЦИОН",
                    "GABRIEL_CONFIG","GABRIEL_CONFIG_EDIT",
                    "CREATEHARDBOSS","HARDBOSS_ATTACK","SHOWHARDBOSS"
                ]
                if CurCommand not in Commands:
                    SavedChat = self.Chat.SavedChat()
                    Status = SavedChat["Status"]
                    Functions.SaveWords(msg,message.channel.guild.name,Status)
        #Команды Администрации
        if message.author.name == "KOT32500":
            if CurCommand == "GDDF": #Gabriel Delete Data File
                await _Message_.delete()
                Emb = discord.Embed( title = 'Стирание сохраненных слов')
                Emb.add_field(name = "Все сообщения, которые могла использовать Габриэль",value = "Были стёрты")
                await message.channel.send(embed = Emb,delete_after=10)
                Functions.ClearWords()
    

    

        

        pass
    
    async def on_ready(self):
        print(f"Logged on as , {self.user} MODULE : bot.py")
        Tasks = list()
        randomStatus = random.randint(0,7)
        with open(f"Ready.txt","r") as file:
            Working = str(file.readline())
        if Working == "-":
            if randomStatus == 0:
                await self.change_presence(
                    activity=discord.Activity(
                        type=discord.ActivityType.listening, 
                        name="твои истории"))
            elif randomStatus == 1:
                await self.change_presence(
                    activity=discord.Activity(
                        type=discord.ActivityType.listening, 
                        name="твои проблемы"))
            elif randomStatus == 2:
                await self.change_presence(
                    activity=discord.Activity(
                        type=discord.ActivityType.watching, 
                        name="в будущее"))
            elif randomStatus == 3:
                await self.change_presence(
                    activity=discord.Activity(
                        type=discord.ActivityType.watching, 
                        name="в окно"))
            elif randomStatus == 4:
                await self.change_presence(
                    activity=discord.Activity(
                        type=discord.ActivityType.listening, 
                        name="музыку"))
            elif randomStatus == 5:
                await self.change_presence(
                    activity=discord.Activity(
                        type=discord.ActivityType.watching, 
                        name="как моляться Богам фпса"))
            elif randomStatus == 6:
                await self.change_presence(
                    activity=discord.Activity(
                        type=discord.ActivityType.watching, 
                        name="на твою историю браузера ;D"))
            elif randomStatus == 7:
                await self.change_presence(
                    activity=discord.Activity(
                        type=discord.ActivityType.watching, 
                        name="в даль"))
        else:
            await self.change_presence(
                status=discord.Status.dnd,
                activity=discord.Activity(
                    type=discord.ActivityType.playing, 
                    name="технические работы"))
        # Channel = await self.fetch_channel(691750825030320218)
        # df = discord.File("LogoGuild.png","Логотип Гильдии.png")
        # await Channel.send(" ",file=df)
        # df = discord.File("Трактат правил.png","Трактат правил.png")
        # await Channel.send(" ",file=df)

        Rooms = await self.fetch_channel(717131388867838002)

        for Channel in Rooms.channels:
            if Channel.topic != "Создание текстовой личной комнаты" and Channel.name != "комната":
                Tasks.append(asyncio.create_task(
                    self.NotMessagesInRoom(Channel)))
                Tasks.append(asyncio.create_task(
                    self.CommandInCustomRoom(Channel)))
            

        for Player in os.listdir(f"./Stats/Main/"):
            _Talant = Functions.Talant(str(Player).split(".txt")[0])
            Tasks.append(_Talant._Update())
            Tasks.append(_Talant.Repair())


        self.DevelopGuild = await self.fetch_guild(716945063351156736)
        self.SoundsWas = []
        self.WebHook = await self.fetch_webhook(721168721326112838)
        Tasks.append(asyncio.create_task(self.BossesRegeneration()))
        Channels = [721150391445749882,721150111320899586]
        
        for Channel in Channels:
            Members = list()
            Channel = await self.fetch_channel(Channel)
            for Member in Channel.members:
                Permissions = Channel.permissions_for(Member)
                if Permissions.administrator == False and Permissions.read_messages == True:
                    Members.append(Member)
            for Member in Members:
                task = asyncio.create_task(self._TimeShow(Member,Channel))
                Tasks.append(task)
        asyncio.gather(*Tasks)
    async def botEvent(self,message):
        MiniGame = self.get_channel(629267102070472714 )
        _Channel_ = None
        _Message_ = None
        try:
            _Channel_ = await self.fetch_channel(message.channel.id)
            _Message_ = await _Channel_.fetch_message(message.id)
        except:
            pass
       # _Player_ = await self.fetch_user(message.author.id)
       # OurServer = await self.fetch_guild(419879599363850251)
        #PLAYER = self.get_user(message.author.id)
        if message.author == self.user:
            pass
        msg = message.content
        #print(msg)
        msgSP = str(message.content).split(" ")
        CurCommand = ""
        

        CurCountForCasino = ""

        try:
            CurCommand = msgSP[0]
            CurCommand = str.upper(CurCommand)
        except IndexError:
            pass
        
        CurCommandEvent = ""

        try:
            CurCommandEvent = msgSP[1]
            CurCommandEvent = str.upper(CurCommandEvent)
        except IndexError:
            pass

        try:
            CurCountForCasino = msgSP[2]
            CurCountForCasino = str.upper(CurCountForCasino)
        except IndexError:
            pass

        UserName_ = message.author.name
      #  UserName_ = message.author.name
        UserName_ = str.split(UserName_)
        UserName__ = str()
        for word in UserName_:
            UserName__ += word
        UserName_ = str(UserName__)
        NowTime = datetime.datetime.today()

        MainStats = Functions.ReadMainParametrs(username=UserName_)
        IntMaxDamage = int(MainStats.pop("damage"))
        GoldPlayer = int(MainStats.pop("money"))
        BossStats = Functions.ReadBossStats()
        today = BossStats.pop("data")
        Boss_MaxHealth = int(BossStats.pop("maxHealth"))
        Boss_CurHealth = int(BossStats.pop("curHealth"))
        Boss_GetGold = int(BossStats.pop("getGold"))
        Boss_Dead = BossStats.pop("dead")

        SplitToDay = today.split("-")

        Time_between_dates_day = int(SplitToDay[2])
        Time_between_dates_hour = int(SplitToDay[3])
        Time_between_dates_mins = int(SplitToDay[4])

        Time_between_dates_day -= NowTime.day
        Time_between_dates_hour -= NowTime.hour
        Time_between_dates_mins -= NowTime.minute

        time.sleep(0.02)

        # _ReadLastMessage = ReadLastMessage()

        if (Time_between_dates_mins <= -20) or (Time_between_dates_hour <= -1) or (Time_between_dates_day <= -1):
                Functions.CreateNewBoss()
                Boss_Dead = "No"
                await MiniGame.send("Создан новый босс")
                return
        if (CurCommand == "EVENT") or (CurCommand == "E") or (CurCommand == "Е"):
            # await _Message_.delete()
            if (CurCommandEvent == "A") or (CurCommandEvent == "А") or (CurCommandEvent == "ATTACK"):
                try:
                    DmgItemID = Functions.ReadEquipment(username=UserName_,type="Оружие")
                    Item = Functions.CheckParametrsEquipment(username=UserName_,ID=DmgItemID)
                    DamageItem = Item.pop('damage')
                except:
                    DamageItem = 0
                try:
                    PlayerInventor = Functions.PlayerInventor(UserName_)
                    Inventores = PlayerInventor.ReadInventor()
                    for items in Inventores.split("\n"):
                        itemsDict = Functions.StrToDict(str=items)
                        IDitem = itemsDict.pop("ID")
                        if DmgItemID == IDitem:
                            armorItem = int(itemsDict.pop("armor"))
                            damageOld = int(itemsDict.pop("damage"))
                            NameItem = itemsDict.pop("name")

                    armorItem -= 1
                    if armorItem < 0:
                        armorItem = 0
                        _PlayerInventor = Functions.PlayerInventor(UserName_)
                        _PlayerInventor.EditItem(username=UserName_,ID=DmgItemID,armor=armorItem,type="Оружие",damage=damageOld,classItem="Сломанный")
                    if armorItem == 0:
                        await message.channel.send(f"{UserName_} предмет [{NameItem}] сломался")
                        Functions.WriteEquipment(username=UserName_,type="Оружие",ID=0)
                except:
                    pass
                YourDamage = random.randint(1,IntMaxDamage + DamageItem)

                MoreDamage = self.Talant_.CheckTalantLevel("Усиленный урон")

                Determination = self.Talant_.CheckTalantLevel("Решимость")

                if Determination["Ready"] == True:
                    YourDamage *= 2

                Level = int(MoreDamage["Level"])
                PlusProcentDamage = (5 * Level) / 100
                PlusProcentDamage = YourDamage * PlusProcentDamage
                YourDamage += PlusProcentDamage

                Boss_CurHealth -= YourDamage

                if (Boss_CurHealth <= 0) and (Boss_Dead == "No"):
                    await message.channel.send(f"{UserName_} убил босса, и получил {Boss_GetGold} зототых")
                    PlayerInventor = Functions.PlayerInventor(UserName_)
                    Inventor = PlayerInventor.ReadInventor()
                    RandomID = random.randint(1,999999)
                    Classes = ['Обычный','Редкий','Эпический','Первоначальный']
                    randomClasses = random.randint(0,3)
                    Classes = Classes[randomClasses]

                    Boss_Dead = "Yes"
                    with codecs.open(f"./Stats/EventBoss.txt","w"
                    ,encoding='utf-8', errors='ignore') as file:
                    # with open(f"./Stats/EventBoss.txt","w") as file:
                        NewDict = {
                            "data": str(today),
                            "maxHealth":0,
                            "curHealth":0,
                            "getGold":str(Boss_GetGold),
                            "dead":"Yes",
                            "nameFile":str(BossStats.pop("nameFile")),
                            "killer":str(message.author.name)
                        }
                        file.writelines(f"{str(NewDict)}")


                    GoldPlayer += Boss_GetGold
                    
                    Functions.WriteMainParametrs(username=UserName_,money=GoldPlayer)

                    if Classes == "Обычный":
                        SwordOrShiel = Functions.randomBool(0,1,1)
                        if SwordOrShiel == True:
                            TypeTheItem = "Оружие"
                            NameForItem = ['Медное копье','Медный лук','Медный кинжал','Медный нож','Медная рапира']
                            NameForItem = NameForItem[random.randint(0,len(NameForItem) - 1)]
                            BalansListItem = Functions.BalansList(type=TypeTheItem,classItem=Classes)
                            BalansListDamageItem = BalansListItem.pop('damage')
                            BalansListGoldItem = BalansListItem.pop('gold')
                            PlayerInventor = Functions.PlayerInventor(UserName_)
                            PlayerInventor.WriteInventor(
                                username=UserName_,
                                old=Inventor,
                                type="Оружие",
                                name=NameForItem,
                                classItem=Classes,
                                ID=RandomID,
                                armor=100,
                                damage=BalansListDamageItem,gold=BalansListGoldItem
                                )
                        else:
                            TypeTheItem = "Экипировка"
                            NameForItem = ['Сандали','Порванный носок','Шляпа','Майка','Куртка']
                            NameForItem = NameForItem[random.randint(0,len(NameForItem) - 1)]
                            BalansListItem = Functions.BalansList(type=TypeTheItem,classItem=Classes)
                            BalansListDamageItem = BalansListItem.pop('protect')
                            BalansListGoldItem = BalansListItem.pop('gold')
                            PlayerInventor = Functions.PlayerInventor(UserName_)
                            PlayerInventor.WriteInventor(
                                username=UserName_,
                                old=Inventor,
                                type="Экипировка",
                                name=NameForItem,
                                classItem=Classes,
                                ID=RandomID,
                                armor=100,
                                protect=BalansListDamageItem,gold=BalansListGoldItem
                                )
                    if Classes == "Редкий":
                        SwordOrShiel = Functions.randomBool(0,1,1)
                        if SwordOrShiel == True:
                            TypeTheItem = "Экипировка"
                            NameForItem = ['Кожанная броня','Шляпа путешествинека','Броня стражника','Перчатки']
                            NameForItem = NameForItem[random.randint(0,len(NameForItem) - 1)]
                            BalansListItem = Functions.BalansList(type=TypeTheItem,classItem=Classes)
                            BalansListDamageItem = BalansListItem.pop('damage')
                            BalansListGoldItem = BalansListItem.pop('gold')
                            PlayerInventor = Functions.PlayerInventor(UserName_)
                            PlayerInventor.WriteInventor(username=UserName_,old=Inventor,type="Экипировка",name=NameForItem,classItem=Classes,ID=RandomID,armor=100,damage=BalansListDamageItem,gold=BalansListGoldItem)
                        else:
                            TypeTheItem = "Оружие"
                            NameForItem = ['Редкое железное копье','Редкий лук','Редкий железный кинжал','Редкий железный нож','Редкая железная рапира','Редкий железный меч.']
                            NameForItem = NameForItem[random.randint(0,len(NameForItem) - 1)]
                            BalansListItem = Functions.BalansList(type=TypeTheItem,classItem=Classes)
                            BalansListDamageItem = BalansListItem.pop('protect')
                            BalansListGoldItem = BalansListItem.pop('gold')
                            PlayerInventor = Functions.PlayerInventor(UserName_)
                            PlayerInventor.WriteInventor(username=UserName_,old=Inventor,type="Оружие",name=NameForItem,classItem=Classes,ID=RandomID,armor=100,protect=BalansListDamageItem,gold=BalansListGoldItem)
                    if Classes == "Эпический":
                        SwordOrShiel = Functions.randomBool(0,1,1)
                        if SwordOrShiel == True:
                            TypeTheItem = "Оружие"
                            NameForItem = ['Эпическое копье','Эльфийский лук','Кинжал тени','Два топора','Секира',"Сияющий меч","Посох","Платиновый меч","Длинный меч"]
                            NameForItem = NameForItem[random.randint(0,len(NameForItem) - 1)]
                            BalansListItem = Functions.BalansList(type=TypeTheItem,classItem=Classes)
                            BalansListDamageItem = BalansListItem.pop('damage')
                            BalansListGoldItem = BalansListItem.pop('gold')
                            PlayerInventor = Functions.PlayerInventor(UserName_)
                            PlayerInventor.WriteInventor(username=UserName_,old=Inventor,type="Оружие",name=NameForItem,classItem=Classes,ID=RandomID,armor=100,damage=BalansListDamageItem,gold=BalansListGoldItem)
                        else:
                            TypeTheItem = "Экипировка"
                            NameForItem = ['Кристальный барьер','Броня Героя','Броня из камня','Духовное покровительство','Героическая душа',"Домашние тапочки","Магический барьер","Эльфийские доспехи"]
                            NameForItem = NameForItem[random.randint(0,len(NameForItem) - 1)]
                            BalansListItem = Functions.BalansList(type=TypeTheItem,classItem=Classes)
                            BalansListDamageItem = BalansListItem.pop('protect')
                            BalansListGoldItem = BalansListItem.pop('gold')
                            PlayerInventor = Functions.PlayerInventor(UserName_)
                            PlayerInventor.WriteInventor(
                                username=UserName_,
                                old=Inventor,
                                type="Экипировка",
                                name=NameForItem,
                                classItem=Classes,
                                ID=RandomID,
                                armor=100,
                                protect=BalansListDamageItem,
                                gold=BalansListGoldItem)
                    if Classes == "Первоначальный":
                        TypeTheItem = "Оружие"
                        NameForItem = ['Палка','Дубинка','Перчатки','Тяжелая палка','Острый камень']
                        NameForItem = NameForItem[random.randint(0,len(NameForItem) - 1)]
                        BalansListItem = Functions.BalansList(type=TypeTheItem,classItem=Classes)
                        BalansListDamageItem = BalansListItem.pop('damage')
                        BalansListGoldItem = BalansListItem.pop('gold')
                        PlayerInventor = Functions.PlayerInventor(UserName_)
                        PlayerInventor.WriteInventor(username=UserName_,old=Inventor,type="Оружие",name=NameForItem,classItem=Classes,ID=RandomID,armor=100,damage=BalansListDamageItem,gold=BalansListGoldItem)
                    

                    pass
            if (CurCommandEvent == "C_N_B") and (UserName_ == "KOT32500"):
                Functions.CreateNewBoss()
                await MiniGame.send(f"{UserName_} создал нового босса")
                return
            if (CurCommandEvent == "BONUS") or (CurCommandEvent == "B") or (CurCommandEvent == "Б") or (CurCommandEvent == "БОНУС"):
                try:
                    with open(f"./Stats/EveryDay/{UserName_}.txt","r") as file:
                        NowDayForUser = file.readline()
                        EarlierTakeGem = file.readline()
                        if int(NowDayForUser) != NowTime.day:
                            RandomAddMoney = random.randint(5,100)
                            BonusTalant = self.Talant_.CheckTalantLevel("Бонусы")
                            TalantLevel = int(BonusTalant["Level"])
                            BonusForTalant = 30 * TalantLevel
                            GoldPlayer += RandomAddMoney + BonusForTalant
                            Functions.WriteMainParametrs(username=UserName_,money=GoldPlayer)
                            await message.channel.send(f"{UserName_} взял(а) ежедневный бонус, в {RandomAddMoney}:moneybag: \n(+{BonusForTalant}:moneybag: за {TalantLevel} уровень таланта Бонусы)")
                            with codecs.open(f"./Stats/EveryDay/{UserName_}.txt","w"
                            ,encoding='utf-8', errors='ignore') as fileTwo:
                                fileTwo.writelines(str(NowTime.day))
                                fileTwo.writelines(f"\n{str(RandomAddMoney + BonusForTalant)}")
                        else:
                            await message.channel.send(f"{UserName_}, вы уже брали ежедневный бонус в размере {EarlierTakeGem}:moneybag:")
                        
                except FileNotFoundError:
                    with open(f"./Stats/EveryDay/{UserName_}.txt","w") as file:
                        file.writelines(str(NowTime.day))
                        BonusTalant = self.Talant_.CheckTalantLevel("Бонусы")
                        RandomAddMoney = random.randint(5,100)
                        TalantLevel = int(BonusTalant["Level"])
                        BonusForTalant = 30 * TalantLevel
                        file.writelines(f"\n{str(RandomAddMoney + BonusForTalant)}")
                        GoldPlayer += RandomAddMoney + BonusForTalant
                        Functions.WriteMainParametrs(username=UserName_,money=GoldPlayer)
                        await message.channel.send(f"{UserName_} взял(а) ежедневный бонус, в {RandomAddMoney}:moneybag: \n(+{BonusForTalant}:moneybag: за {TalantLevel} уровень таланта Бонусы)")
            time.sleep(0.01)
            # if (CurCommandEvent == "CASINO") or (CurCommandEvent == "C"):
            #     MainStats = Functions.ReadMainParametrs(username=UserName_)
            #     Money = MainStats.pop("money")
            #     try:
            #         CurCountForCasino = int(CurCountForCasino)
            #     except ValueError:
            #         await message.channel.send(f":negative_squared_cross_mark:`Нужно указать число` :negative_squared_cross_mark:")
            #         return
                
            #     try:
            #        # oldMoney = Money
            #         if CurCountForCasino > Money:
            #             CurCountForCasino = Money
            #         if CurCountForCasino < 0:
            #             await message.channel.send(f"Нельзя указать < 0")
            #             return
            #         Money -= CurCountForCasino

            #        # GetMoney = int(CurCountForCasino * (random.random() * 2))
            #         rnd = random.random()
            #         rnd *= 1.85
            #         GetMoney = int(CurCountForCasino * rnd)
            #         Money += GetMoney
            #        # GetMoney = 1
            #         #GetMoney
            #        # print(GetMoney)
            #         await message.channel.send(f"Коэффициент : {rnd}%. \nСтавка : {CurCountForCasino} золотых.\nПолученно золотых : {GetMoney}.\nТекущее количество золотых : {Money} золотых.",delete_after=100)

            #         #_AddMoney(UserName_,GetMoney)
            #         # _SetMoney(UserName_,Money)
            #         Functions.WriteMainParametrs(username=UserName_,money=Money)



            #         pass
            #     except ValueError:
            #         await message.channel.send(f"Ошибка : проверьте правильность написания команды")
                


            if (CurCommandEvent == "P") or (CurCommandEvent == "П") or (CurCommandEvent == "Р") or (CurCommandEvent == "ПРОФИЛЬ") or (CurCommandEvent == "PROFILE"):
                await message.channel.send(f" ",file = ProfileBoss(today,Boss_MaxHealth,Boss_CurHealth,Boss_GetGold,Boss_Dead))
        if (CurCommand == "ЦИТАТА"):
            await _Message_.delete()
            # NickNameLastMessage = _ReadLastMessage[0] ; NickNameLastMessage = NickNameLastMessage.split() ; NickNameLastMessage = NickNameLastMessage[0]
            # await message.channel.send(f" ",file=Create_quotes(NickNameLastMessage,_ReadLastMessage[1],_ReadLastMessage[2]))
            await message.channel.send(f"(временно не работает)")

        Functions.WriteBossStats(data=today,maxHealth=Boss_MaxHealth,curHealth=Boss_CurHealth,getGold=Boss_GetGold,dead=Boss_Dead)
    async def botStandart(self,message):
        UserName_ = message.author.name
        UserName_ = str.split(UserName_)
        UserName__ = str()
        for word in UserName_:
            UserName__ += word
        UserName_ = str(UserName__)
        _Gabriele_ = await self.fetch_user(656808327954825216)
        OurServer = await self.fetch_guild(message.guild.id)
        # print(message.content)
        _Message_ = discord.message.Message
        _Player_ = discord.user.User
        Member_Player = discord.member.Member
        try:
            _Channel_ = await self.fetch_channel(message.channel.id)
            _Player_ = await self.fetch_user(message.author.id)
            Member_Player = await OurServer.fetch_member(_Player_.id)
            _Message_ = await _Channel_.fetch_message(message.id)
        except:
            pass

        Message = message.content
        Guild = await self.fetch_guild(message.guild.id)
        Member = await Guild.fetch_member(message.author.id)
        Administrator = False
        for role in Member.roles:
            RolePermission = role.permissions
            if RolePermission.administrator == True:
                Administrator = True
        Command = str(Message).split(" ")[0].upper()
        if Administrator == True:
            if Command == "GABRIEL_CONFIG".upper():
                file = await self.Gabriel.Config.ConfigOpen(self,self.Setting)
                await message.channel.send(f" ",file=file)
                await message.delete()
            if Command == "Gabriel_Config_Edit".upper():
                Config = str(Message).split(" ")[1].upper()
                if Config == "Chat".upper():
                    OnlineOrOffline = str(Message).split(" ")[2].upper()
                    try:
                        self.Config.Write(Chat=OnlineOrOffline)
                        await message.channel.send(f"Текущее состояние : {OnlineOrOffline}")
                    except Functions.Gabriel.Config.NotOnlineOrOffline:
                        AddOrRemove = str(Message).split(" ")[2].upper()
                        Possibles = ['ADD','REMOVE',"CHANNELS","GENERAL","PRIVATE","STATUS"]
                        Chat = self.Chat
                        if AddOrRemove in Possibles:
                            if AddOrRemove == "ADD".upper():
                                Index = str(Message).split(" ")[3] ; Index = int(Index)
                                try:
                                    GetChannel = await self.fetch_channel(Index)
                                    Chat.LoadChat(Index)
                                    await message.channel.send(f"{GetChannel.name}, добавлен.")
                                except discord.errors.NotFound:
                                    await message.channel.send(f"Канал не может быть добавлен, так как его не существует")
                            elif AddOrRemove == "REMOVE".upper():
                                Index = str(Message).split(" ")[3] ; Index = int(Index)
                                try:
                                    GetChannel = await self.fetch_channel(Index)
                                    Chat.RemoveChat(Index)
                                    await message.channel.send(f"{GetChannel.name}, убран")
                                except discord.errors.NotFound:
                                    await message.channel.send(f"Канал не может быть убран, так как его уже не существует")
                            elif AddOrRemove == "CHANNELS".upper():
                                Channels = Chat.SavedChat()
                                Answer = "Сохраненные каналы : "
                                ChannelsList = Channels["Activity"]
                                for _Channel in ChannelsList:
                                    GetChannel = await self.fetch_channel(_Channel)
                                    Answer += f"\n{GetChannel.name} ({_Channel})"
                                await message.channel.send(f"{Answer}")
                            elif AddOrRemove == "GENERAL".upper():
                                Chat.StatusEdit("GENERAL".upper())
                                await message.channel.send(f"Теперь чат всеобщий. \nЭто означает, что Габриэль будет брать слова со всех серверов, на которых включен этот режим, и отправлять сообщения.")
                            elif AddOrRemove == "PRIVATE".upper():
                                Chat.StatusEdit("PRIVATE")
                                await message.channel.send(f"Теперь чат частный. \nЭто означает, что Габриэль будет брать слова только с этого сервера, и отправлять сообщения.")
                            elif AddOrRemove == "STATUS".upper():
                                SavedChat = Chat.SavedChat()
                                Status = str(SavedChat["Status"])
                                if Status == "GENERAL":
                                    Description = "Это означает, что Габриэль будет общаться используя словарный запас, со всех серверов, на которых включена данная фукнция"
                                else:
                                    Description = "Это означает, что Габриэль будет общаться, используя словарный запас сервера"
                                await message.channel.send(f"Текущее состояние : {Status} \n{Description}")
                            else:
                                await message.channel.send(f"Для модуля чата, доступные варианты настроек : \nOnline / Offline \nADD ID/ REMOVE ID \nGeneral / Private")

                        else:
                            await message.channel.send(f"Для модуля чата, доступные варианты настроек : \nOnline / Offline \nADD ID/ REMOVE ID \nGeneral / Private")
                
                elif Config == "Game".upper():
                    OnlineOrOffline = str(Message).split(" ")[2].upper()
                    try:
                        self.Config.Write(Game=OnlineOrOffline)
                        await message.channel.send(f"Текущее состояние : {OnlineOrOffline}")
                    except Functions.Gabriel.Config.NotOnlineOrOffline:
                        await message.channel.send(f"Доступные вариатны ответа : Online / Offline")

                elif Config == "Rooms".upper():
                    OnlineOrOffline = str(Message).split(" ")[2].upper()
                    try:
                        self.Config.Write(Rooms=OnlineOrOffline)
                        await message.channel.send(f"Текущее состояние : {OnlineOrOffline}")
                    except Functions.Gabriel.Config.NotOnlineOrOffline:
                        AddOrRemove = str(Message).split(" ")[2].upper()
                        Possibles = ['ADD','REMOVE',"CHANNELS"]
                        Rooms = self.Gabriel.Rooms(self.Config.server,self.Config.Client)
                        if AddOrRemove in Possibles:
                            if AddOrRemove == "ADD".upper():
                                Index = str(Message).split(" ")[3] ; Index = int(Index)
                                try:
                                    GetChannel = await self.fetch_channel(Index)
                                    Rooms.LoadRooms(Index)
                                    await message.channel.send(f"{GetChannel.name}, добавлен.")
                                except discord.errors.NotFound:
                                    await message.channel.send(f"Канал не может быть добавлен, так как его не существует")
                            if AddOrRemove == "REMOVE".upper():
                                    Index = str(Message).split(" ")[3] ; Index = int(Index)
                                    try:
                                        GetChannel = await self.fetch_channel(Index)
                                        Rooms.RemoveRooms(Index)
                                        await message.channel.send(f"{GetChannel.name}, убран")
                                    except discord.errors.NotFound:
                                        await message.channel.send(f"Канал не может быть убран, так как его уже не существует")
                            if AddOrRemove == "CHANNELS".upper():
                                Channels = Rooms.SavedRooms()
                                Answer = "Сохраненные каналы : "
                                ChannelsList = Channels["Activity"]
                                for _Channel in ChannelsList:
                                    GetChannel = await self.fetch_channel(_Channel)
                                    Answer += f"\n{GetChannel.name} ({_Channel})"
                                await message.channel.send(f"{Answer}")
                        else:
                            await message.channel.send(f"Доступные вариатны ответа : \nOnline / Offline \nADD ID/ REMOVE ID")
                await message.delete()
        if _Channel_.id == 691750825030320218 and message.author != self.user:
            MessageContent = message.content
            MessageContent = str.lower(MessageContent)
            try:
                await _Message_.delete()
            except:
                pass
        
        YourProfilParamerts = Functions.ReadMainParametrs(username=UserName_)
        IntCurExp = int(YourProfilParamerts.pop("exp"))
        Level = int(YourProfilParamerts.pop("lvl"))
        IntMaxHealth = int(YourProfilParamerts.pop("maxHealth"))
        IntCurHealth = int(YourProfilParamerts.pop("curHealth"))
        IntMaxDamage = int(YourProfilParamerts.pop("damage"))
        MoreExp = self.Talant_.CheckTalantLevel("Больше опыта")
        IntCurExp += 1 + int(MoreExp["Level"])
        Functions.WriteMainParametrs(username=UserName_,exp=IntCurExp)
        if IntCurExp > Level * 5:
            Level += 1
            maxLevel = int(YourProfilParamerts.pop("maxLevel"))
            plus = int(YourProfilParamerts.pop("plus"))
            if maxLevel < Level:
                maxLevel = Level
                Reshumost = self.Talant_.CheckTalantLevel("Решимость")
                if Reshumost["Ready"] == False:
                    plus += 1
            LevelUp = Functions.LevelUp(count=1)
            health = LevelUp.pop("health")
            damage = LevelUp.pop('damage')
            IntMaxHealth += health
            IntCurHealth += health
            IntMaxDamage += damage #{'exp': 0, 'lvl': 0, 'maxHealth': 0, 'curHealth': 0, 'damage': 0, 'description': '', 'money': 0, 'messages': 0, 'maxLevel': 0, 'strength': 1.0, 'agility': 1.0, 'intelligence': 1.0, '_plus': 0}
            IntCurExp = 0
            Functions.WriteMainParametrs(username=UserName_,exp=IntCurExp,damage=IntMaxDamage,maxHealth=IntMaxHealth,curHealth=IntCurHealth,lvl=Level,maxLevel=maxLevel,plus=plus)

        
        FrstMention = None
        _Mention_ = None
        try:
            RolesPlayer = Member_Player.roles
            _Mentions_ = _Message_.raw_mentions
            FrstMention = _Mentions_[0]
            _Mention_ = await self.fetch_user(FrstMention)
        except:
            pass
        if message.author == self.user:
            pass
        # CurChannel = message.channel
        
        msg =  message.content
        #message.channel.message.reactions(name="LUL")
        #print(msg)
        msgSP = msg.split()
        CurCommand = ""

        # AboutTextThenCommand = ""
        try:
            with codecs.open(f"{Resurses}{UserName_}.png","r"
            ,encoding='utf-8', errors='ignore') as file:
            # with open(f"{Resurses}{UserName_}.png","r"):
                pass
        except:
            DownloadFile = requests.get(_Player_.avatar_url, stream=True)
            with open(f"{Resurses}{UserName_}.png","bw") as file:
                for chunk in DownloadFile.iter_content(12288):
                    file.write(chunk)
                    pass
                pass


        #for target_list in range(len(message)):
            #pass

        try:
            CurCommand = msgSP[0]
            CurCommand = str.upper(CurCommand)
        except IndexError:
            pass
        
        
        CurCommandPlayer = ""
        try:
            CurCommandPlayer = msgSP[1]

        except IndexError:
            pass
        

        # try:
        #     AboutTextThenCommand = msgSP[0]

        #     Commands = ["ABOUT_ME",
        #     "UPGRADE_ITEM","U_I"
        #     "ROLE",
        #     "TALANT",
        #     "SELL_ITEM","S_I",
        #     "AE","AUCTION",
        #     ""," "]

        #     AboutTextThenCommand = str(AboutTextThenCommand).upper()
        #     if AboutTextThenCommand not in Commands:
        #         try:
        #             _AboutTextThenCommand = msgSP[2]
        #             _AboutTextThenCommand = str(_AboutTextThenCommand).upper()
        #         except: 
        #             return
        # except:
        #     pass


        if CurCommand == 'Ы':
            await _Message_.delete()
            await message.channel.send(":poultry_leg: **`ЫАЫ`** :poultry_leg:",delete_after=2)
        if CurCommand == "ГАБРИЭЛЬ":
            for emodji in self.DevelopGuild.emojis:
                Names = ["Letter_A2","Letter_L","Letter_B","Letter_A","Letter_C"]
                if emodji.name in "Letter_A2":
                    Letter_A2 = emodji
                if emodji.name in "Letter_L":
                    Letter_L = emodji
                if emodji.name in "Letter_B":
                    Letter_B = emodji
                if emodji.name in "Letter_A":
                    Letter_A = emodji
                if emodji.name in "Letter_C":
                    Letter_C = emodji
            await _Message_.add_reaction(Letter_C)
            await _Message_.add_reaction(Letter_L)
            await _Message_.add_reaction(Letter_A)
            await _Message_.add_reaction(Letter_B)
            await _Message_.add_reaction(Letter_A2)
        try:
            if CurCommand == "GS":
                try:
                    await _Message_.delete()
                except:
                    pass
                try:
                    _ChannelVoice_ = await self.fetch_channel(int(str(message.content).split()[1]))
                except:
                    _ChannelVoice_ = await self.fetch_channel(message.author.voice.channel.id)
                try:
                    Mode = int(str(message.content).split()[2])
                except:
                    Mode = 0
                InVoice = False
                for member in _ChannelVoice_.members:
                    if member == _Gabriele_:
                        InVoice = True
                if InVoice == False:
                    self._VoiceClient = await _ChannelVoice_.connect()
                    Sounds = os.listdir(f"./Resurses/JoinVoice/")
                    # Sounds.pop(self.SoundsWas)
                    RandomInt = random.randint(0,len(Sounds) - 1)
                    RandomSound = Sounds[RandomInt]
                    self.SoundsWas.append(RandomSound)
                    self._VoiceClient.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source=f"./Resurses/JoinVoice/{RandomSound}"))
                else:
                    # await message.channel.send(f"Не могу проиграть звук",delete_after=1)
                    Sounds = os.listdir(f"./Resurses/JoinVoice/")
                    RandomInt = random.randint(0,len(Sounds) - 1)
                    RandomSound = Sounds[RandomInt]
                    self._VoiceClient.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source=f"./Resurses/JoinVoice/{RandomSound}"))
        except AttributeError:
            pass

        if (CurCommand == 'PROFILE'):
            try:
                await _Message_.delete()
            except:
                pass
            if CurCommandPlayer == "":
                try:
                    await message.channel.send(" ",file=profileEdit(UserName_))
                except ErrorAvatar:
                    DownloadFile = requests.get(_Player_.avatar_url, stream=True)
                    # print(f"новая аватарка в {Resurses}{_Player_.name}")
                    with open(f"{Resurses}{UserName_}.png","bw") as file:
                        for chunk in DownloadFile.iter_content(12288):
                            file.write(chunk)
                            pass
                        pass
        if (CurCommand == "ATTACK"):
            await _Message_.delete()
            if CurCommandPlayer.lower() == UserName_.lower():
                await message.channel.send(":no_entry: `Нельзя выбрать в качестве цели самого себя` :no_entry:",delete_after=2)
                return
            try:
                ThisItem = Functions.ReadEquipment(username=UserName_,type="Оружие")
                ThisItem = Functions.CheckParametrsEquipment(username=UserName_,ID=ThisItem)
                _magic = ThisItem["magic"]
                Damage = int(ThisItem["damage"])
                Player_ = Functions.ReadMainParametrs(username=UserName_)
                Health = int(Player_["curHealth"])
                maxHealth = int(Player_["maxHealth"])
                try:
                    _magic = _magic['Parametrs']
                    _magic = _magic[0]
                    Keys = _magic.keys()
                    for key in Keys:
                        key = str(key)
                        Spell = _magic[key]
                        # KeysSpell = Spell.keys()
                        # print(key)
                        # print(Spell)
                        if key == "Poison":
                            Time = int(Spell["Time"])
                            Damage = int(Spell["Damage"])
                            _PlayerClass = PlayerClass(UserName_,self)
                            await _PlayerClass.Poison(CurCommandPlayer,Time,Damage)
                        if key == "Vampirism":
                            Heal = int(Spell["Heal"])
                            Health += Heal
                            if Health >= maxHealth:
                                Health = 0
                            Functions.WriteMainParametrs(username=UserName_,curHealth=Health)
                        await asyncio.sleep(0.1)
                except: pass
                    
                    # Name = Spell.pop('name')
                    # KeysSpell = Spell.keys()
                    # txt += f"{Name} "
                    # for Key in KeysSpell:
                    #     key = str(Key)
                    #     if key != "Description":
                    #         Stat = Spell[key]
                    #         txt += f"{Stat}"
                    # txt += '\n'

                StatsEnemy = Functions.ReadMainParametrs(username=CurCommandPlayer)
                EnIntCurLvl = int(StatsEnemy.pop("lvl"))
                EnIntMaxHealth = int(StatsEnemy.pop("maxHealth"))
                EnIntCurHealth = int(StatsEnemy.pop("curHealth"))
                EnIntMaxDamage = int(StatsEnemy.pop("damage"))
                EnMaxLevel = int(StatsEnemy.pop("maxLevel"))
                if EnMaxLevel == 0: return


                FreeLvlHA = EnIntCurLvl / 5
                
                try:
                    DmgItemID = Functions.ReadEquipment(username=UserName_,type="Оружие")
                    Item = Functions.CheckParametrsEquipment(username=UserName_,ID=DmgItemID)
                    DamageItem = Item.pop('damage')
                except:
                    DamageItem = 0
                try:
                    PlayerInventor = Functions.PlayerInventor(UserName_)
                    Inventores = PlayerInventor.ReadInventor()
                    for items in Inventores.split("\n"):
                        itemsDict = Functions.StrToDict(str=items)
                        IDitem = itemsDict.pop("ID")
                        if DmgItemID == IDitem:
                            armorItem = int(itemsDict.pop("armor"))
                            damageOld = int(itemsDict.pop("damage"))
                            NameItem = itemsDict.pop("name")

                    armorItem -= 1
                    if armorItem < 0:
                        armorItem = 0
                    _PlayerInventor = Functions.PlayerInventor(UserName_)
                    _PlayerInventor.EditItem(username=UserName_,ID=DmgItemID,armor=armorItem,type="Оружие",damage=damageOld,classItem="Сломанный")
                    if armorItem == 0:
                        await message.channel.send(f"{UserName_} предмет [{NameItem}] сломался")
                        Functions.WriteEquipment(username=UserName_,type="Оружие",ID=0)
                except:
                    pass
                GetDamage = random.randint(0,IntMaxDamage + int(DamageItem))
                strength = Functions.ReadMainParametrs(username=UserName_) ; strength = float(strength.pop("strength"))
                GetDamage *= strength
                try:
                    Item_ID = Functions.ReadEquipment(username=CurCommandPlayer,type="Экипировка")
                    ItemProtect = Functions.CheckParametrsEquipment(username=CurCommandPlayer,ID=Item_ID)
                    protect = int(ItemProtect["protect"])
                    Determination = self.Talant_.CheckTalantLevel("Решимость")
                    if Determination["Ready"] == True:
                        protect *= 2
                    GetDamage -= protect
                except: pass
                if GetDamage <= 0:
                    GetDamage = 1
                
                EnIntCurHealth -= int(GetDamage)
                await Functions.EditAttackDamageTwo(self=self,Channel=_Channel_,GetDamage=int(GetDamage),_Player=UserName_,_Target=CurCommandPlayer,CurHealthTarget=EnIntCurHealth)

                if EnIntCurHealth <= 0:
                    EnIntCurLvl -= int(FreeLvlHA)
                    MainStats = Functions.ReadMainParametrs(username=UserName_)
                    IntCurLvl = int(MainStats.pop("lvl"))
                    IntCurLvl += int(FreeLvlHA)

                    plus = int(MainStats.pop("plus"))
                    maxLevel = int(MainStats.pop("maxLevel"))
                    if IntCurLvl > maxLevel:
                        Reshumost = self.Talant_.CheckTalantLevel("Решимость")
                        if Reshumost["Ready"] == False:
                            plus += maxLevel - IntCurLvl
                            maxLevel = plus


                    # await BotInisializator.AttackMessage(CurCommandPlayer,IntCurLvl,EnIntCurHealth,EnIntMaxHealth,FreeLvlHA,GetDamage,CurChannel)

                    LevelUp = Functions.LevelUp(count=int(FreeLvlHA))

                    health = LevelUp.pop('health')

                    damage = LevelUp.pop('damage')


                    IntMaxHealth += health
                    IntCurHealth += health
                    IntMaxDamage += damage
                    Functions.WriteMainParametrs(username=UserName_,lvl=IntCurLvl,maxHealth=IntMaxHealth,curHealth=IntCurHealth,damage=IntMaxDamage,plus=plus,maxLevel=maxLevel)
                    
                    EnIntMaxHealth -= health
                    if EnIntMaxHealth <= 0: EnIntMaxHealth = 5
                    EnIntMaxDamage -= damage
                    if EnIntMaxDamage <= 0: EnIntMaxDamage = 1
                    EnIntCurHealth = EnIntMaxHealth
                Functions.WriteMainParametrs(username=CurCommandPlayer,lvl=EnIntCurLvl,maxHealth=EnIntMaxHealth,curHealth=EnIntCurHealth,damage=EnIntMaxDamage)
            except FileNotFoundError:
                await message.channel.send(":warning: `Профиль не найден, или этого игрока просто не существует` :warning:",delete_after=2)
        if (CurCommand == 'PROFILE'):
            
            if CurCommandPlayer != "":
                try:
                    try:
                        await message.channel.send(" ",file=profileEdit(CurCommandPlayer))
                    except:
                        await message.channel.send(":warning: `Профиль не найден, или этого игрока просто не существует` :warning:",delete_after=2)
                except ErrorAvatar:
                    await message.channel.send("У пользователя нет аватарки. Это связано с : \n1) Пользователь имеет ошибку в аватарке \n2) Пользователь не открывал свой профиль, ни разу",delete_after=5)


        if CurCommand == "HOTSPROFILE":
            pass
        
        if CurCommand == "NEW_AVATAR":
            await _Message_.delete()
            await message.channel.send(":ballot_box_with_check: `Новая аватарка, поставлена. В случае её ошибки, она будет заменена на обычную` :ballot_box_with_check:",delete_after=2)
            _AgentWrite(UserName_,CurCommandPlayer,False)
        if CurCommand == "NEW_BACKGROUND":
            await _Message_.delete()
            await message.channel.send(":white_check_mark: `Новый фон, поставлен. В случае его ошибки, он будет заменен на обычный` :white_check_mark:",delete_after=2)
            _AgentWrite(UserName_,CurCommandPlayer,True)


        if CurCommand == "ABOUT_ME":
            await _Message_.delete()
            Description = str(message.content)
            Functions.WriteMainParametrs(username=UserName_,description=Description)
            await message.channel.send(":bell: `Вы успешно сменили информацию, о себе` :bell:",delete_after=2)


            pass

        if CurCommand == "DELETEINFO":
            await _Message_.delete()
            if CurCommandPlayer == "":
                await message.channel.send(":tools: `Вы успешно сбросили собственный аккаунт` :tools:",delete_after=2)
                return
            else:
                if UserName_ != "KOT32500":
                    await message.channel.send(":no_entry: `У вас нет прав на это` :lock:",delete_after=2)
                else:
                    await message.channel.send(f":pencil2: {UserName_} `сбросил аккаунт у` {CurCommandPlayer} :pencil2:",delete_after=2)
                    return

        
        if CurCommand == "TOP":
            await _Message_.delete()
            await message.channel.send(":tools: `Процесс пошел.` :tools:",delete_after=5)
            #time.sleep(0.1)
            await message.channel.send(" ",file=RatingSystem())
            time.sleep(1)
            #AllMVPs()            
            pass

        if CurCommand == "MUTE":
            if UserName_ == "KOT32500":
                await _Channel_.set_permissions(_Mention_,send_messages=False,attach_files=False,add_reactions=False)
            await _Message_.delete()
        if CurCommand == "UNMUTE":
            if UserName_ == "KOT32500":
                await _Channel_.set_permissions(_Mention_,send_messages=True,attach_files=True,add_reactions=True)
            await _Message_.delete()
        
        if CurCommand == "INV":
            try:
                PlayerInventor = Functions.PlayerInventor(UserName_)
                old = PlayerInventor.ReadInventor()
                oldList = old.split("\n")
                ItemList = list()
                for line in oldList:
                    NwDict = ast.literal_eval(f'{line}') ; NwDict = dict(NwDict)
                    ItemList.append(str(NwDict))
            except:
                IDrandom = random.randint(1,99999999)
                PlayerInventor = Functions.PlayerInventor(UserName_)
                PlayerInventor.WriteInventor(username=UserName_,old="",type="Оружие",name="Ржавый сломанный ножик",classItem="Первоначальный",ID=IDrandom,armor=1000,damage=5,gold=100)
                StandartImageItem = "./Resurses/Inventor/StandartItem.png"
                DF = discord.File(StandartImageItem,StandartImageItem)
                await message.channel.send(f" ",file=DF)
                return
            
            # SendInfo = ""
            for item in ItemList:
                ItemDict = StrToDict(str=item)
                # typeItem = "None"
                # nameItem = "None"

                try:
                    type_ = str(ItemDict.pop('type'))
                except: raise Functions.Error_CreateItem("type error")


                try:
                    name = str(ItemDict.pop('name'))
                except: raise Functions.Error_CreateItem("name error")


                try:
                    classItem = str(ItemDict.pop('classItem'))
                except: raise Functions.Error_CreateItem("classItem error")


                try:
                    ID = int(ItemDict.pop("ID"))
                except: raise Functions.Error_CreateItem("ID error")

                try:
                    gold = int(ItemDict.pop("gold"))
                except: raise Functions.Error_CreateItem("gold error")


                # try:
                #     duration = int(ItemDict.pop("duration"))
                # except:
                #     if type_ == "Предмет":
                #         raise Functions.Error_CreateItem("duration error")


                try:
                    armor = int(ItemDict.pop("armor"))
                except:
                    if (type_ == "Оружие") or (type_ == "Экипировка"):
                        raise Functions.Error_CreateItem("armor error")

                try:
                    damage = int(ItemDict.pop("damage"))
                except:
                    if type_ == "Оружие":
                        raise Functions.Error_CreateItem("damage error")


                try:
                    protect = int(ItemDict.pop("protect"))
                except:
                    if type_ == "Экипировка":
                        raise Functions.Error_CreateItem("protect error")


                # try:
                #     count = int(ItemDict.pop("count"))
                # except:
                #     if type_ == "Ингридиент":
                #         raise Functions.Error_CreateItem("count error")
                if type_ == "Оружие":
                    ImageInventor = Functions.CreateImageInventor(username=UserName_,typeItem=type_,name=name,classItem=classItem,ID=ID,gold=gold,armor=armor,damage=damage)
                    await message.channel.send(f"ID : {ID}",file=ImageInventor)
                if type_ == "Экипировка":
                    ImageInventor = Functions.CreateImageInventor(username=UserName_,typeItem=type_,name=name,classItem=classItem,ID=ID,gold=gold,armor=armor,protect=protect)
                    await message.channel.send(f"ID : {ID}",file=ImageInventor)
            pass
        if CurCommand == "WEAR":
            await _Message_.delete()
            PlayerInventor = Functions.PlayerInventor(UserName_)
            old = PlayerInventor.ReadInventor()
            oldList = old.split("\n")
            ItemList = list()
            for line in oldList:
                NwDict = ast.literal_eval(f'{line}') ; NwDict = dict(NwDict)
                ItemList.append(str(NwDict))
            for Item in ItemList:
                ItemDict = StrToDict(str=Item)
                ID = ItemDict.pop('ID')
                type_ = ItemDict.pop('type')
                nameItem = ItemDict.pop('name')
                try:
                    IndexItem = int(CurCommandPlayer)
                    Parmetrs = Functions.CheckParametrsEquipment(username=UserName_,ID=IndexItem)
                    ClassItem = Parmetrs.pop('classItem')
                    if (IndexItem == ID) and (ClassItem != "Сломанный"):
                        Functions.WriteEquipment(username=UserName_,type=type_,ID=ID)
                        await message.channel.send(f"{UserName_}, вы успешно экипировали [{nameItem}]")
                    if (IndexItem == ID) and (ClassItem == "Сломанный"):
                        await message.channel.send(f"{UserName_}, вы не можете экипировать [{nameItem}] \nПо скольку он сломанный")
                        pass
                    
                except:
                    pass
                
                

            pass
        if (CurCommand == "UPGRADE_ITEM"):
            await _Message_.delete()
            RolesPlayer = Member_Player.roles
            # try:
            IDitem = int(CurCommandPlayer)
            GoldSell = int(msgSP[2])
            MyGold = Functions._Gold(username=UserName_,do="Разузнать")
            if GoldSell > int(MyGold):
                GoldSell = int(MyGold)
            if GoldSell <= 0:
                await message.channel.send(f"Золото не может быть ниже 1")
                return
            PlayerInventor = Functions.PlayerInventor(UserName_)
            Inventore = PlayerInventor.ReadInventor()
            for item in Inventore.split("\n"):
                itemDict = Functions.StrToDict(str=item)
                itemID = itemDict['ID']
                if itemID == IDitem:
                    type_ = itemDict['type']
                    classItem = itemDict['classItem']
                    gold = int(itemDict['gold'])
                    gold -= GoldSell
                    if gold <= 0:
                        GoldSell -= gold
                        NewClassItem = Functions._NewClassItem(classItem=classItem)
                        RolesPlayer = Member_Player.roles
                        if classItem == "Мифический":
                            for Role in RolesPlayer:
                                # print(f"Name : {Role} \nID : {Role.id} \n\n")
                                if Role.id == 691209621968519188: #Демоны
                                    NewClassItem = "Демонический"
                                elif Role.id == 578514024782626837: #Боги
                                    NewClassItem = "Божественный"
                                else:
                                    await message.channel.send(f"Вы достигли макс. уровня предмета, на ваш ранг")
                        # Pers = await Functions.GetPermissions(self)
                        # print(Pers)
                        print(NewClassItem)
                        NewUpgrade = Functions.BalansList(type=type_,classItem=NewClassItem)
                        if (type_ == "Оружие"):
                            NewDamage = NewUpgrade.pop('damage')
                            NewArmor = NewUpgrade.pop('armor')
                            NewGold = NewUpgrade.pop('gold')
                            _PlayerInventor = Functions.PlayerInventor(UserName_)
                            _PlayerInventor.EditItem(username=UserName_,ID=itemID,type=type_,classItem=NewClassItem,armor=NewArmor,gold=NewGold,damage=NewDamage)
                            Functions._Gold(username=UserName_,do="Убавить",count=GoldSell)
                            await message.channel.send(f"Урон : {NewDamage}\nПрочность : {NewArmor}\nНужно золотых : {NewGold} \nID : {itemID} \nКласс : {NewClassItem}")
                            return
                        if (type_ == "Экипировка"):
                            NewProtect = NewUpgrade.pop('protect')
                            NewArmor = NewUpgrade.pop('armor')
                            NewGold = NewUpgrade.pop('gold')
                            _PlayerInventor = Functions.PlayerInventor(UserName_)

                            _PlayerInventor.EditItem(
                                username=UserName_,
                                ID=itemID,
                                type=type_,
                                classItem=NewClassItem,
                                armor=NewArmor,
                                gold=NewGold,
                                protect=NewProtect
                                )
                            Functions._Gold(username=UserName_,do="Убавить",count=GoldSell)
                            await message.channel.send(f"Защиты : {NewProtect}\nПрочность : {NewArmor}\nНужно золотых : {NewGold} \nID : {itemID}\nКласс : {NewClassItem}")
                            return

                    Functions._Gold(username=UserName_,do="Убавить",count=GoldSell)
                    if (type_ == "Оружие"):
                        damage = itemDict['damage']
                        armor = itemDict['armor']
                        _PlayerInventor = Functions.PlayerInventor(UserName_)
                        _PlayerInventor.EditItem(username=UserName_,ID=itemID,type=type_,classItem=classItem,armor=armor,damage=damage,gold=gold)
                    elif type_ == "Экипировка":
                        protect = itemDict['protect']
                        armor = itemDict['armor']
                        _PlayerInventor = Functions.PlayerInventor(UserName_)
                        _PlayerInventor.EditItem(
                            username=UserName_,
                            ID=itemID,
                            type=type_,
                            classItem=classItem,
                            protect=protect,
                            armor=armor,
                            gold=gold
                            )
                pass
            # except:
            #     await message.channel.send(f"Ошибка в команде")
            

            # Functions.EditItem(username=UserName_)
        if (CurCommand == "SELL_ITEM"):
            await _Message_.delete()
            IDitem = int(CurCommandPlayer)
            PlayerInventor = Functions.PlayerInventor(UserName_)
            Inventore = PlayerInventor.ReadInventor()
            for item in Inventore.split("\n"):
                itemDict = Functions.StrToDict(str=item)
                itemID = itemDict.pop('ID')
                if itemID == IDitem:
                    name = itemDict.pop("name")
                    try:
                        MoneyEnd = PlayerInventor.SellItem(username=UserName_,ID=IDitem)
                        await message.channel.send(f"Вы продаете предмет : {name} \nЗа {MoneyEnd} золотых")
                    except Functions.LastItem:
                        await message.channel.send(f"Вы не можете продать единственный предмет, в инвентаре")
                    
            pass

        time.sleep(0.1)
        if (CurCommand == "TALANT") or (CurCommand == "ТАЛАНТ"):
            CurCommandPlayer = str(CurCommandPlayer).upper()
            if (CurCommandPlayer == "STRENGTH") or (CurCommandPlayer == "СИЛА"):
                MainStatsTalant = Functions.ReadMainParametrs(username=UserName_)
                try:
                    Number = int(str(message.content).split()[-1])
                except: Number = 1
                strength = float(MainStatsTalant.pop("strength"))
                plus = int(MainStatsTalant.pop("plus"))
                time.sleep(0.1)
                if (Number <= plus) and (Number > 0):
                    strength += float(0.0025 * Number)
                    plus -= Number
                    Functions.WriteMainParametrs(username=UserName_,strength=strength,plus=plus)
                    await message.channel.send(f"Вы успешно повысили силу, на {Number} ед.",delete_after=5)
                
                pass
            if (CurCommandPlayer == "AGILITY") or (CurCommandPlayer == "ЛОВКОСТЬ"):
                MainStatsTalant = Functions.ReadMainParametrs(username=UserName_)
                try:
                    Number = int(str(message.content).split()[-1])
                except: Number = 1
                agility = float(MainStatsTalant.pop("agility"))
                plus = int(MainStatsTalant.pop("plus"))
                time.sleep(0.1)
                if (Number <= plus) and (Number > 0):
                    agility += (0.01 * Number)
                    plus -= Number
                    Functions.WriteMainParametrs(username=UserName_,agility=agility,plus=plus)
                    await message.channel.send(f"Вы успешно повысили ловкость, на {Number} ед.",delete_after=5)
                pass
            if (CurCommandPlayer == "INTELLIGENCE") or (CurCommandPlayer == "ИНТЕЛЛЕКТ"):
                MainStatsTalant = Functions.ReadMainParametrs(username=UserName_)
                try:
                    Number = int(str(message.content).split()[-1])
                except: Number = 1
                intelligence = float(MainStatsTalant.pop("intelligence"))
                plus = int(MainStatsTalant.pop("plus"))
                time.sleep(0.1)
                if (Number <= plus) and (Number > 0):
                    intelligence += (0.025 * Number)
                    plus -= Number
                    Functions.WriteMainParametrs(username=UserName_,intelligence=intelligence,plus=plus)
                    await message.channel.send(f"Вы успешно повысили интеллект, на {Number} ед.",delete_after=5)
                pass
            if CurCommandPlayer == "SHOW":
                __Talant__ = Functions.Talant(UserName_)
                Info = __Talant__.Info
                Stats = Info["Stats"]
                Talants = Info["Talants"]
                GetExp = int(Stats["GetExp"])
                Pick = str(Stats["Pick"])
                MessageSend = f"```\nТаланты {message.author.name}\nОпыт : {GetExp}/мин.\nВыбранный навык : {Pick}```"
                Author = message.author
                await Author.send(MessageSend)
                for _Talant in Talants:
                    Talant = Talants[_Talant]

                    Name = str(Talant["Name"])
                    Description = str(Talant["Description"])
                    PerLevel = str(Talant["PerLevel"])

                    Level = int(Talant["Level"])
                    MaxLevel = int(Talant["MaxLevel"])

                    Exp = int(Talant["Exp"])
                    NeedExp = int(Talant["NeedExp"])

                    Lock = int(Talant["Lock"])
                    if Lock == 0:
                        Lock = "Доступно"
                    else:
                        Lock = "Не доступно"
                    Description_Lock = str(Talant["Description_Lock"])
                    MessageSend = f"```\n{Name}\n{Description}\nЗа каждый уровень : \n{PerLevel}\nУровень : {Level}\nМаксимальный уровень : {MaxLevel}\nОпыт : {Exp}/{NeedExp}\nДоступен : {Lock}\n{Description_Lock}```"
                    await Author.send(MessageSend)
            if CurCommandPlayer == "PICK":
                Talant = Functions.Talant(UserName_)
                Text_ = str(message.content).split()[2::]
                Text = ""
                count = int(len(Text_))
                for text in Text_:
                    count -= 1
                    if count > 0:
                        Text += f"{text} "
                    else: Text += text
                Be = False
                Talants = Talant.GetTalants()
                for _Talant_ in Talants:
                    Talants = Talant.Info["Talants"]
                    _Talant = Talants[_Talant_]
                    Name = str(_Talant["Name"])
                    if Name == Text:
                        Be = True
                if Be == True:
                    Talant.PickTalant(Text)
                    await message.channel.send(f"Вы успено поставили '{Text}' в качестве навыков")
                else:
                    await message.channel.send(f"Таланта '{Text}' не существует")
        if CurCommand == "AU":
            _Auction = Functions.Auction()
            CurCommandPlayer = str(CurCommandPlayer).upper()
            if CurCommandPlayer == "ADD":
                ItemID = int(msgSP[2])
                GoldCost = int(msgSP[3])
                if GoldCost < 100: 
                    await message.channel.send("Число не должно быть меньше 100")
                    return
                _Auction.AddAuction(username=UserName_,ID=ItemID,goldAuction=GoldCost)
                await message.channel.send(f'{FixText(f"Вы успешно поставили выбранный торг, за {GoldCost}")}')
                # Functions._Gold(username=UserName_,do="Убавить",count=GoldCost)
            if CurCommandPlayer == "BUY":
                AuctionID = int(msgSP[2])
                GoldCost = int(msgSP[3])
                try:
                    _Auction.RemoveAuction(username=UserName_,gold=GoldCost,AuctionID=AuctionID)
                    await message.channel.send("Покупка торга прошла успешна")
                except Functions.NotEnoughGold:
                    await message.channel.send("Не достаточно золота")
            if CurCommandPlayer == "INFO":
                Text = FixText("                               Аукцион \nЭто место, где вы можете как покупать предметы, так и продавать им другим игрокам.")
                await message.channel.send(f'{Text} ```Если вам нужна подробная информация о аукционе, поищите её в Auction Help```')
            if CurCommandPlayer == "HELP":
                AuctionText = FixText("                               Аукцион ")
                HowWorking = FixText("Как работает аукцион? \nТорговцы выставляют вещи, за определенную сумму (минимальная цена : 100 золотых), покупатели же, покупают эти вещи, отдавая своё золото продавцу")
                CommandAdd = FixText("Auction add = позволяет выставить выбранный вами предмет, на продажу. Делается это так : Auction add ИндексПредмета Цена\nТем самым, другие игроки смогут купить этот предмет, и вы получите деньги. \nВнимание : После этой команды, этот предмет пропадет из вашего инвентаря")
                CommandBuy = FixText("Auction buy = позволяет купить выбранный вами торг. Делается это так : Auction buy ИндексТорга Золото \nВнимание : Устанавливать число больше того, которое просит торг можно, но не обязательно. Установив больше, вы отдадите больше золота, чем просит на это торг")
                CommandShow = FixText("Auction show = позволяет увидеть все торги.")
                await message.channel.send(f'{AuctionText}{HowWorking}{CommandAdd}{CommandBuy}{CommandShow}')

                pass
            if CurCommandPlayer == "SHOW":
                AllAuctions = str(_Auction.ReadAuction())
                AllAuctions = AllAuctions.split("\n")
                for _Auction in AllAuctions:
                    print(_Auction)
                    try:
                        AuctionDict = Functions.StrToDict(str=_Auction)
                        Owner = str(AuctionDict.pop("username"))
                        ItemID = int(AuctionDict.pop("ID"))
                        goldAuction = int(AuctionDict.pop("goldAuction"))
                        AuctionID = int(AuctionDict.pop("AuctionID"))
                        Item = Functions.StrToDict(str=AuctionDict["Item"])
                        ItemType = str(Item.pop("type"))
                        ItemName = str(Item.pop("name"))
                        ClassItem = str(Item.pop("classItem"))

                        ItemGold = int(Item.pop("gold"))
                        if ItemType == "Оружие":
                            ItemArmor = int(Item.pop("armor"))
                            ItemDamage = int(Item.pop("damage"))
                            await message.channel.send(f"Владелец : {Owner}\nИндекс предмета : {ItemID}\nСтоимость торга : {goldAuction}\nИндекс торга : {AuctionID}\nТип предмета : {ItemType}\nИмя предмета : {ItemName}\nКласс предмета : {ClassItem}\nЗолото в предмете : {ItemGold}\nПрочность : {ItemArmor}\nУрон : {ItemDamage}")
                        if ItemType == "Экипировка":
                            ItemArmor = int(Item.pop("armor"))
                            ItemProtect = int(Item.pop("protect"))
                            await message.channel.send(f"Владелец : {Owner}\nИндекс предмета : {ItemID}\nСтоимость торга : {goldAuction}\nИндекс торга : {AuctionID}\nТип предмета : {ItemType}\nИмя предмета : {ItemName}\nКласс предмета : {ClassItem}\nЗолото в предмете : {ItemGold}\nПрочность : {ItemArmor}\nЗащита : {ItemProtect}")
                        pass
                    except SyntaxError:
                        print("SyntaxError")
                pass
            
        if message.channel.topic == "Создание текстовой личной комнаты":
            if message.author != self.user:
                await self._CreateRoom(message.channel,message.author)
        pass
    async def botShop(self,message):
        time.sleep(1)
        if message.author == self.user:
            pass
        _Channel_ = None
        _Message_ = None
        try:
            _Channel_ = await self.fetch_channel(message.channel.id)
            _Message_ = await _Channel_.fetch_message(message.id)
        except:
            pass
        msg =  message.content
        #print(msg)
        msgSP = msg.split()
        CurCommand = ""

        CurCountBuyItem = ""

        try:
            CurCommand = msgSP[0]
            CurCommand = str.upper(CurCommand)
        except IndexError:
            pass
        
        CurBuyItem = ""

        try:
            CurBuyItem = msgSP[1]
            CurBuyItem = str.upper(CurBuyItem)
        except IndexError:
            pass

        try:
            CurCountBuyItem = msgSP[2]
            CurCountBuyItem = str.upper(CurCountBuyItem)
        except IndexError:
            pass

        UserName_ = message.author.name
       # UserName_ = message.author.name
        UserName_ = str.split(UserName_)
        UserName__ = str()
        for word in UserName_:
            UserName__ += word
        UserName_ = str(UserName__)

        MainStats = Functions.ReadMainParametrs(username=UserName_)
        Msages = int(MainStats.pop("messages"))
        Gold = int(MainStats.pop("money"))
        
        Msages += 1

        MoreGold = self.Talant_.CheckTalantLevel("Больше золота")

        if Msages >= 5 - int(MoreGold["Level"]):
            Gold += 1
            Msages = 0

        MainStats = Functions.ReadMainParametrs(username=UserName_)
        IntCurExp = int(MainStats.pop("exp"))
        IntCurLvl = int(MainStats.pop("lvl"))
        IntMaxHealth = int(MainStats.pop("maxHealth"))
        IntCurHealth = int(MainStats.pop("curHealth"))
        IntMaxDamage = int(MainStats.pop("damage"))
        
        Plus = int(MainStats["plus"]) 

        maxLevel = int(MainStats["maxLevel"]) 

        if (CurCommand == "BUY"):
            #Начало
            await _Message_.delete()
            if CurBuyItem == "ЛЕЧЕНИЕ":
                if CurCountBuyItem != "":
                    BuyItem = _BuyItem(2,Gold,CurCountBuyItem)
                    _CountBuy = BuyItem[0]
                    str1 = BuyItem[1]
                    _Gold_ = BuyItem[2]
                    Gold = _Gold_
                    for target_list in range(int(_CountBuy)):
                        IntCurHealth += 35
                        if IntCurHealth > IntMaxHealth:
                            IntCurHealth = IntMaxHealth
                        if target_list < 0:
                            print("ERROR")
                    await message.channel.send(str1)
                else:
                    await message.channel.send("Количеств не указано",delete_after=2)
            #Конец
            #Начало
            elif CurBuyItem == "УРОН":
                if CurCountBuyItem != "":
                    BuyItem = _BuyItem(8,Gold,CurCountBuyItem)
                    _CountBuy = BuyItem[0]
                    str1 = BuyItem[1]
                    _Gold_ = BuyItem[2]
                    Gold = _Gold_
                    for target_list in range(int(_CountBuy)):
                        IntMaxDamage += random.randint(1,5)
                        if target_list < 0:
                            print("ERROR")
                    await message.channel.send(str1)
                else:
                    await message.channel.send("Количеств не указано",delete_after=2)
            #Конец
            #Начало
            elif CurBuyItem == "ЗДОРОВЬЕ":
                if CurCountBuyItem != "":
                    BuyItem = _BuyItem(13,Gold,CurCountBuyItem)
                    _CountBuy = BuyItem[0]
                    str1 = BuyItem[1]
                    _Gold_ = BuyItem[2]
                    Gold = _Gold_
                    for target_list in range(int(_CountBuy)):
                        IntMaxHealth += random.randint(5,10)
                        if target_list < 0:
                            print("ERROR")
                    await message.channel.send(str1)
                else:
                    await message.channel.send("Количеств не указано",delete_after=2)
            #Конец
            #Начало
            elif CurBuyItem == "ОПЫТ":
                if CurCountBuyItem != "":
                    time.sleep(1)
                    BuyItem = _BuyItem(50,Gold,CurCountBuyItem)
                    _CountBuy = BuyItem[0]
                    str1 = BuyItem[1]
                    _Gold_ = BuyItem[2]
                    Gold = _Gold_
                    for target_list in range(int(_CountBuy)):
                        IntCurExp += random.randint(10,200)
                        while IntCurExp >= IntCurLvl * 5:
                            WasExpNeed = IntCurLvl * 5
                            IntCurLvl += 1
                            IntMaxHealth += 10
                            IntCurHealth += 10
                            IntMaxDamage += random.randint(1,35)
                            if ((IntCurHealth + 5) < (IntMaxHealth)):
                                IntCurHealth += 5
                            else:
                                IntCurHealth = IntMaxHealth
                            IntCurExp -= WasExpNeed
                            if maxLevel < IntCurLvl:
                                Reshumost = self.Talant_.CheckTalantLevel("Решимость")
                                if Reshumost["Ready"] == False:
                                    Plus += 1
                        if target_list < 0:
                            print("ERROR")
                    await message.channel.send(str1)
                else:
                    await message.channel.send("Количеств не указано",delete_after=2)
            #Конец
            #Начало
            elif CurBuyItem == "УРОВЕНЬ":
                if CurCountBuyItem != "":
                    BuyItem = _BuyItem(100,Gold,CurCountBuyItem)
                    _CountBuy = BuyItem[0]
                    str1 = BuyItem[1]
                    _Gold_ = BuyItem[2]
                    Gold = _Gold_
                    for target_list in range(int(_CountBuy)):
                        rnd = random.randint(5,15)
                        IntCurLvl += rnd
                        for target_list in range(int(rnd)):
                            IntMaxHealth += 10
                            IntCurHealth += 10
                            IntMaxDamage += random.randint(1,35)
                            if ((IntCurHealth + 5) < (IntMaxHealth)):
                                IntCurHealth += 5
                            else:
                                IntCurHealth = IntMaxHealth
                            if maxLevel < IntCurLvl:
                                Reshumost = self.Talant_.CheckTalantLevel("Решимость")
                                if Reshumost["Ready"] == False:
                                    Plus += 1
                        if target_list < 0:
                            print("ERROR")
                    await message.channel.send(str1)
                else:
                    await message.channel.send("Количеств не указано",delete_after=2)
            #Конец
            else:
                await message.channel.send("Такого предмета нет",delete_after=2)

        Functions.WriteMainParametrs(username=UserName_,exp=IntCurExp,lvl=IntCurLvl,maxHealth=IntMaxHealth,curHealth=IntCurHealth,damage=IntMaxDamage,money=Gold,messages=Msages,plus=Plus)
    async def BossesRegeneration(self):
        Servers = os.listdir("./Servers/")
        AliveBossed = []
        for Server in Servers:
            try:
                Boss = BossForMoney(Server)
                StatsBoss = Boss.Read()
                BossAlive = str(StatsBoss["Status"])
                if BossAlive == "Life":
                    AliveBossed.append(Boss)
            except: pass
        while True:
            for AliveBoss in AliveBossed:
                StatsBoss = AliveBoss.Read()
                Health = int(StatsBoss["Health"])
                Status = StatsBoss["Status"]
                if Status == "Life":
                    Health += random.randint(300000,500000)
                    MaxHealth = int(StatsBoss["MaxHealth"])
                    if Health > MaxHealth:
                        Health = MaxHealth
                    if Health <= 0:
                        Health = 0
                    AliveBoss.Write(Health=Health)
            await asyncio.sleep(0.1) 
        pass
    async def SuperBoss(self,message):
        Command = str(message.content).split(" ")[0].upper()
        Boss = BossForMoney(message.channel.guild.name)
        HaveBoss = False
        try:
            Stats = Boss.Read()
            HaveBoss = True
        except:
            pass
        UserName_ = message.author.name
        UserName_ = str.split(UserName_)
        UserName__ = str()
        for word in UserName_:
            UserName__ += word
        UserName_ = str(UserName__)
        if HaveBoss == True:
            Health = int(Stats["Health"])
            MaxHealth = int(Stats["MaxHealth"])
            Damage = int(Stats["Damage"])
            Armor = int(Stats["Armor"])

            if Command == "CreateHardBoss".upper():
                Index = str(message.content).split(" ")[1].upper()
                await message.delete()
                if int(Index) < 100000:
                    await message.channel.send(f"Меньше чем 100000 золотых, нельзя призывать босса",delete_after=10)
                    return
                curGold = Functions._Gold(username=UserName_,do="Разузнать")
                if curGold < int(Index):
                    await message.channel.send(f"У вас не достаточно золото чтобы призвать босса",delete_after=10)
                    return
                Functions._Gold(username=UserName_,do="Убавить",count=int(Index))
                Boss.Create(int(Index))
                await message.channel.send(f"Босс успешно был призван",delete_after=10)


    async def on_message(self, message):
        self.Gabriel = Functions.Gabriel()
        try:
            Guild = await self.fetch_guild(message.channel.guild.id)
        except:
            if message.author != self.user:
                await message.channel.send(f"Я не работаю, в личных сообщениях. Пожалуйста, обратитесь за помощью на сервер")
            return
        self.Config = self.Gabriel.Config()
        await self.Config.Start(Guild.id,self)
        self.Chat = self.Gabriel.Chat(Guild,self)
        self.Setting = self.Config.Read(message.channel.guild.name)
        self.ThisGuild = await self.fetch_guild(message.channel.guild.id)
        UserName_ = message.author.name
        UserName_ = str.split(UserName_)
        UserName__ = str()
        for word in UserName_:
            UserName__ += word
        UserName_ = str(UserName__)
        self.Talant_ = Functions.Talant(UserName_)
        self.Talants = self.Talant_.GetTalants()
        self.TalantStats = self.Talant_.GetStats()
        Dialog = asyncio.create_task(self.Dialog(message))
        botEvent = asyncio.create_task(self.botEvent(message))
        botStandart = asyncio.create_task(self.botStandart(message))
        botShop = asyncio.create_task(self.botShop(message))
        SuperBoss = asyncio.create_task(self.SuperBoss(message))
        asyncio.gather(Dialog,botEvent,botStandart,botShop,SuperBoss)


    async def on_voice_state_update(self,_Player_ : discord.member.Member, before : discord.member.VoiceState, after : discord.member.VoiceState):
        #msg = self.get_channel(627140104988917789)
        _Gabriel = Functions.Gabriel()
        Confige = _Gabriel.Config()
        await Confige.Start(_Player_.guild.id,self)
        Modules = Confige.Read(_Player_.guild.name)

        RoomModule = Modules["Rooms"]
        if RoomModule != "ONLINE":
            return
        OurServer = await self.fetch_guild(_Player_.guild.id)
        CurVoice = after.channel
        TextCurVoice = str(CurVoice)
        Roles = OurServer.get_role(623063847497891840)
        EveryOne = OurServer.roles[0]
        # print(before)
        # print(after)
        
       # print(Roles)
        if TextCurVoice == "Создать комнату":
            RolesThisPlayer = _Player_.roles
            for role in RolesThisPlayer:
                if role.id == 700036252317122628:
                    # print("Невозможно создать комнату, из за того что на вас весит запрет")
                    try:
                        await _Player_.send("```fix\nВы не можете создать комнату.\n```")
                    except: pass
                    MusicVoice = await self.fetch_channel(688501395779092572)
                    await _Player_.move_to(MusicVoice,reason="Невозможность создать комнату")
                    return
            try:
                Room = Functions.Room(_Player_.name)
                NewGroup = await OurServer.create_voice_channel(f"{Room.Read()}",reason="Новая комната")
            except Room.NoRoomName:
                NewGroup = await OurServer.create_voice_channel(f"{_Player_.name}",reason="Новая комната")
            await NewGroup.set_permissions(_Player_,manage_channels=True,move_members=True,manage_roles=True,reason="Новая комната")
            await _Player_.move_to(NewGroup,reason="Новая комната")
        if TextCurVoice == "Создать комнату (Истинный чат)":
            try:
                Room = Functions.Room(_Player_.name)
                NewGroup = await OurServer.create_voice_channel(f"{Room.Read()}",reason="Новая комната")
            except Room.NoRoomName:
                NewGroup = await OurServer.create_voice_channel(f"{_Player_.name}",reason="Новая комната")
            await NewGroup.set_permissions(_Player_,manage_channels=True,move_members=True,manage_roles=True,reason="Новая комната")
            await NewGroup.set_permissions(Roles,connect=True,reason="Новая комната")
            await NewGroup.set_permissions(EveryOne,connect=False,reason="Новая комната")
            await _Player_.move_to(NewGroup,reason="Новая комната")
        Textbefore = str(before.channel)
        #await msg.send(f"{Textbefore} и {_Player_.name}")

        try:
            CurGroup = await self.fetch_channel(before.channel.id)
            Members = CurGroup.members
            Guild = await self.fetch_guild(before.channel.guild.id)
            Config = _Gabriel.Rooms(Guild,self)
            Saved = Config.SavedRooms()
            #Activity
            SavedID = Saved["Activity"]
            if (len(Members) == 0) and (Textbefore != "Создать комнату") and (Textbefore != "Резерв") and (Textbefore != "Музыка") and (Textbefore != "Создать комнату (Истинный чат)"):
                if CurGroup.id not in SavedID:
                    await CurGroup.delete(reason="В комнате никого нет")
        except Exception:
            pass

    async def on_guild_channel_update(self,before,after):
        overwrites = before.overwrites
        for overwrite in overwrites:
            try:
                permissions = overwrite.permissions
            except AttributeError:
                permissions = overwrite.permissions_in(before)
                if permissions.manage_channels == True:
                    Room = Functions.Room(overwrite.name)
                    Room.Save(after.name)

    async def on_member_join(self,member : discord.member.Member):
        try:
            OurServer = await self.fetch_guild(419879599363850251)
            StartRole = OurServer.get_role(691735620346970123)
            await member.add_roles(StartRole,reason="Впервые зашел на сервер")
        except: pass

    async def on_raw_reaction_add(self,payload):
        Channel = await self.fetch_channel(payload.channel_id)
        Message = await Channel.fetch_message(payload.message_id)
        Guild = await self.fetch_guild(Message.channel.guild.id)
        Player = await self.fetch_user(payload.user_id)
        Member = await Guild.fetch_member(Player.id)
        UserName_ = Player.name
        UserName_ = str.split(UserName_)
        UserName__ = str()
        for word in UserName_:
            UserName__ += word
        UserName_ = str(UserName__)
        DevelopGabriel = await self.fetch_guild(716945063351156736)
        EmodjsInDevelop = await DevelopGabriel.fetch_emojis()
        # for Emodji in EmodjsInDevelop:
        #     await Message.add_reaction(Emodji)
        Emoji = payload.emoji
        # print(Emoji)
        # await Message.add_reaction(Emoji)
        #Босс 2
        if Message.id == 713440081863639130:
            if Player == self.user:
                return
            Boss = BossForMoney(Guild.name)
            Stats = Boss.Read()
            HeroStats = Functions.ReadMainParametrs(username=UserName_)
            HeroStrength = float(HeroStats["strength"])
            PlayerHealth = int(HeroStats["curHealth"])
            await Message.remove_reaction(Emoji,Player)
            Health = int(Stats["Health"])
            MaxHealth = int(Stats["MaxHealth"])
            Damage = int(Stats["Damage"])
            Armor = int(Stats["Armor"])
            BossStatus = str(Stats["Status"])
            if str(Emoji.name) == "Fight":
                Item = Functions.ReadEquipment(username=UserName_,type="Оружие")
                Item = Functions.CheckParametrsEquipment(username=UserName_,ID=Item)
                ItemDamage = int(Item["damage"])
                
                DamageHero = int(HeroStats["damage"])
                GetDamage = random.randint(1,DamageHero + ItemDamage)
                GetDamage -= Armor
                if GetDamage <= 0: GetDamage = 1
                GetDamage = int(GetDamage * HeroStrength)
                Health -= GetDamage
                PlayerHealth -= Damage
                if PlayerHealth <= 0:
                    PlayerMaxHealth = int(HeroStats["maxHealth"])
                    PlayerLevel = int(HeroStats["lvl"])
                    FreeLevel = PlayerLevel / 5
                    PlayerLevel -= FreeLevel
                    LostLevels = Functions.LevelUp(count=FreeLevel)
                    LostHealth = LostLevels["health"]
                    LostDamage = LostLevels["damage"]
                    PlayerMaxHealth -= LostHealth
                    DamageHero -= LostDamage
                    PlayerHealth = PlayerMaxHealth
                    PlayersLostStats = list()
                    Functions.WriteMainParametrs(
                        username = UserName_,
                        lvl = PlayerLevel,
                        curHealth = PlayerHealth,
                        maxHealth = PlayerMaxHealth,
                        damage = DamageHero
                        )
                if Health <= 0:
                    Boss.Write(Health=Health,Status="Dead")
                    if BossStatus == "Life":
                        await Message.edit(
                            content=f"Текущее здоровье : 0\nМаксимальное здоровье : {MaxHealth}\nВозможный урон : {Damage}\nБроня : {Armor}"
                        )
                        Magic = Functions.Magic()
                        Encanteds = Magic.PossibleEnchant()
                        Enchant = Encanteds[random.randint(0,len(Encanteds))]
                        Inventor = Functions.PlayerInventor(UserName_)
                        ReliquaryNames = [
                            "Божественная длань",
                            "Затерянный левый носок",
                            "Деревянная палка",
                            "Драконий посох",
                            "Правосудие",
                            "Испепелитель",
                            "Душа",
                            "Уничтожитель",
                            "Меч из чистой энергии",
                            "Плазменный меч",
                            "Заряженный великой магией посох",
                            "Злобная энергия",
                            "Атомный разборщик",
                            "Тренировочный меч",
                            "Ветвь дерева",
                            "Заточенный острый камень",
                            "Перчатка с шипами",
                            "Укрепленный магией и драконьей душой , позолоченный , кристальный боевой тапок",
                            "Ворованный носок"
                        ]
                        if Enchant == "Vampirism":
                            EncantItem = Magic.Create(
                                Parametrs = {
                                    "Vampirism" : {
                                        "name" : "Вампиризм",
                                        "Description" : "После каждой атаки вы исциляетесь",
                                        "Heal" : random.randint(100,3000),
                                        "type" : "+"
                                    }
                                }
                            )
                        elif Enchant == "More experience":
                            EncantItem = Magic.Create(
                                Parametrs = {
                                    "More experience" : {
                                        "name" : "Больше опыта",
                                        "Description" : "После каждого убийства героя, вы забираете дополнительный опыт",
                                        "Multi" : 2
                                    }
                                }
                            )
                        elif Enchant == "Poison":
                            EncantItem = Magic.Create(
                                Parametrs = {
                                    "Poison" : {
                                        "name" : "Яд",
                                        "Description" : "После каждой атаки, вы наносите дополнительный урон ядом",
                                        "Time" : random.randint(0.1,10),
                                        "Damage" : random.randint(1000,100000)
                                    }
                                }
                            )
                        elif Enchant == "Fury":
                            EncantItem = Magic.Create(
                                Parametrs = {
                                    "Fury" : {
                                        "name" : "Неистовство",
                                        "Description" : "Вы начинаете получать опыт, за убийство боссов.",
                                        "Exp" : random.randint(100,1000)
                                    }
                                }
                            )
                        elif Enchant == "Critical hit":
                            EncantItem = Magic.Create(
                                Parametrs = {
                                    "Critical hit" : {
                                        "name" : "Критический удар",
                                        "Description" : "У вас есть шанс, нанести умноженный урон",
                                        "Multy" : 2
                                    }
                                }
                            )
                        elif Enchant == "Recklessness":
                            EncantItem = Magic.Create(
                                Parametrs = {
                                    "Recklessness" : {
                                        "name" : "Безрассудство",
                                        "Description" : "Ваши удары игнорируют броню, однако прочность предмета снижается на 99%",
                                    }
                                }
                            )
                        elif Enchant == "Execution":
                            EncantItem = Magic.Create(
                                Parametrs = {
                                    "Execution" : {
                                        "name" : "Казнь",
                                        "Description" : "Противники чье хп стало меньше отметки, могут быть убиты с 1 удара",
                                        "MinHealth" : 10
                                    }
                                }
                            )
                        elif Enchant == "Looting":
                            EncantItem = Magic.Create(
                                Parametrs = {
                                    "Looting" : {
                                        "name" : "Грабёж",
                                        "Description" : "С каждой атакой, вы имеете шанс ограбить героя",
                                        "chance" : 10
                                    }
                                }
                            )
                        elif Enchant == "Grace":
                            EncantItem = Magic.Create(
                                Parametrs = {
                                    "Grace" : {
                                        "name" : "Благодать",
                                        "Description" : "После вашей смерти, предмет пропадает, однако дает вам временную неуязвимость, и полностью исциляет вас",
                                        "Time" : 50000
                                    }
                                }
                            )
                        elif Enchant == "Cheating":
                            EncantItem = Magic.Create(
                                Parametrs = {
                                    "Cheating" : {
                                        "name" : "Читерство",
                                        "Description" : "Увеличивает шансы победить , в казино. Внимание : Другие игроки , которые будут вас атаковать, смогут забирать ваши деньги",
                                    }
                                }
                            )
                        elif Enchant == "Dealer":
                            EncantItem = Magic.Create(
                                Parametrs = {
                                    "Dealer" : {
                                        "name" : "Торговец",
                                        "Description" : "Этот предмет стоит в 10 раз дороже",
                                    }
                                }
                            )
                        elif Enchant == "Training":
                            EncantItem = Magic.Create(
                                Parametrs = {
                                    "Training" : {
                                        "name" : "Обучение",
                                        "Description" : "Если вы атакуете кого либо, вы получаете большее количество опыта",
                                        "Exp" : 15
                                    }
                                }
                            )
                        elif Enchant == "Curse":
                            EncantItem = Magic.Create(
                                Parametrs = {
                                    "Curse" : {
                                        "name" : "Проклятье",
                                        "Description" : "Каждое ваше сообщение, убивает вас.",
                                        "Damage" : 15
                                    }
                                }
                            )
                        try:
                            ReliquaryName = ReliquaryNames[random.randint(0,len(ReliquaryNames))]
                        except:
                            ReliquaryName = ReliquaryNames[0]
                        Inventor.WriteInventor(
                            type="Оружие",
                            name=ReliquaryName,
                            classItem="Реликвия",
                            ID=random.randint(0,99999999),
                            gold=9999999999,
                            armor=5000000,
                            damage=random.randint(500650000,1065000000),
                            magic=EncantItem
                        )
                else:
                    Boss.Write(Health=Health,Status="Life")
                    await Message.edit(
                        content=f"Текущее здоровье : {Health}\nМаксимальное здоровье : {MaxHealth}\nВозможный урон : {Damage}\nБроня : {Armor}\n\n{UserName_} : \nЗдоровье : {PlayerHealth}"
                    )    
        # -----
        # Регистрация
        if Message.id == 713880721709727754:
            if Player == self.user:
                return
            await Message.remove_reaction(Emoji,Player)
            Standart = Guild.get_role(610078093260095488)
            StartRole = Guild.get_role(691735620346970123)
            MainChannel = self.get_channel(419879599363850253)
            await MainChannel.send(f"{Player.mention} присоединился на сервер",delete_after=600)
            if str(Emoji.name) == "⚫":
                Role = Guild.get_role(713477362058002535)
                await Member.add_roles(Standart,Role,reason="Прошел регистацию")
                await Member.remove_roles(StartRole,reason="Прошел регистрацию")
            elif str(Emoji.name) == "🔵": 
                Role = Guild.get_role(713477367061938180)
                await Member.add_roles(Standart,Role,reason="Прошел регистацию")
                await Member.remove_roles(StartRole,reason="Прошел регистрацию")
            elif str(Emoji.name) == "🟤": 
                Role = Guild.get_role(713681425056006154)
                await Member.add_roles(Standart,Role,reason="Прошел регистацию")
                await Member.remove_roles(StartRole,reason="Прошел регистрацию")
            elif str(Emoji.name) == "🟢": 
                Role = Guild.get_role(713477377644167288)
                await Member.add_roles(Standart,Role,reason="Прошел регистацию")
                await Member.remove_roles(StartRole,reason="Прошел регистрацию")
            elif str(Emoji.name) == "🟠": 
                Role = Guild.get_role(713477369045712932)
                await Member.add_roles(Standart,Role,reason="Прошел регистацию")
                await Member.remove_roles(StartRole,reason="Прошел регистрацию")
            elif str(Emoji.name) == "🟣": 
                Role = Guild.get_role(713477376910032897)
                await Member.add_roles(Standart,Role,reason="Прошел регистацию")
                await Member.remove_roles(StartRole,reason="Прошел регистрацию")
            elif str(Emoji.name) == "🔴": 
                Role = Guild.get_role(713477364977500220)
                await Member.add_roles(Standart,Role,reason="Прошел регистацию")
                await Member.remove_roles(StartRole,reason="Прошел регистрацию")
            elif str(Emoji.name) == "⚪": 
                Role = Guild.get_role(713477210446757900)
                await Member.add_roles(Standart,Role,reason="Прошел регистацию")
                await Member.remove_roles(StartRole,reason="Прошел регистрацию")
            elif str(Emoji.name) == "🟡": 
                Role = Guild.get_role(713477378214592603)
                await Member.add_roles(Standart,Role,reason="Прошел регистацию")
                await Member.remove_roles(StartRole,reason="Прошел регистрацию")
            Msg = f"""
            ```fix
Поздравляю.
```
```
Вы успешно присоединились на сервер!
Теперь вам доступен ранее недоступный контент.
Советую пройти обучение, оно поможет ознакомиться с сервером, 
И стать полноценным участником, покажет и поможет в начале.
Но прежде чем ты пойдешь его проходить, спешу сообщить о том, что время
На выполнения обучения ограничено часом, этого вполне хватит чтобы прочитать
А после это меню автоматически уберёться, и не будет мешать вам быть 
Полноценным участником сервера!
```
            """
            await Member.send(Msg)
            Channels = [721150391445749882,721150111320899586]
            Tasks = list()
            for Channel in Channels:
                Channel = await self.fetch_channel(Channel)
                overwrite = discord.PermissionOverwrite()
                overwrite.send_messages = True
                overwrite.read_messages = True
                overwrite.read_message_history = True
                Task = asyncio.create_task(Channel.set_permissions(Member,overwrite=overwrite))
                Task2 = asyncio.create_task(self._TimeShow(Member,Channel))
                Tasks.append(Task)
                Tasks.append(Task2)
            asyncio.gather(*Tasks)
        # -----------
        # await Message.add_reaction("⚫")
        # await Message.add_reaction("🔵")
        # await Message.add_reaction("🟤")
        # await Message.add_reaction("🟢")
        # await Message.add_reaction("🟠")
        # await Message.add_reaction("🟣")
        # await Message.add_reaction("🔴")
        # await Message.add_reaction("⚪")
        # await Message.add_reaction("🟡")
        #Роли
        # print(Emoji)
        if Message.id == 714080637648240690:
            # ⚫ - Чёрный
            # 🔵 - Синий
            # 🟤 - Коричневый
            # 🟢 - Зелёный
            # 🟠 - Оранжевый
            # 🟣 - Фиолетовый
            # 🔴 - Красный
            # ⚪ - Белый
            # 🟡 - Жёлтый
            if Player == self.user:
                return
            await Message.remove_reaction(Emoji,Player)
            
            RolesID = [
                713477210446757900, 713477362058002535, 713477364977500220,
                713477367061938180, 713477369045712932, 713477376910032897,
                713477377644167288, 713477378214592603, 713681425056006154,
                716391511708794951, 716390741475196969, 716391516137848863,
                716391507980189726, 716391501772488748, 716391505425858641,
                716390742012199024, 716391505073274920

                    ]
            RoleList = list()
            for Role in RolesID:
                RoleList.append(Guild.get_role(Role))
            if str(Emoji.name) == "⚫": await self.AddOneRole(713477362058002535,Member,Guild,RolesID)
            elif str(Emoji.name) == "🔵": await self.AddOneRole(713477367061938180,Member,Guild,RolesID)
            elif str(Emoji.name) == "🟤": await self.AddOneRole(713681425056006154,Member,Guild,RolesID)
            elif str(Emoji.name) == "🟢": await self.AddOneRole(713477377644167288,Member,Guild,RolesID)
            elif str(Emoji.name) == "🟠": await self.AddOneRole(713477369045712932,Member,Guild,RolesID)
            elif str(Emoji.name) == "🟣": await self.AddOneRole(713477376910032897,Member,Guild,RolesID)
            elif str(Emoji.name) == "🔴": await self.AddOneRole(713477364977500220,Member,Guild,RolesID)
            elif str(Emoji.name) == "⚪": await self.AddOneRole(713477210446757900,Member,Guild,RolesID)
            elif str(Emoji.name) == "🟡": await self.AddOneRole(713477378214592603,Member,Guild,RolesID)
            elif str(Emoji.name) == "Turquoise_circle": await self.AddOneRole(716391511708794951,Member,Guild,RolesID)
            elif str(Emoji.name) == "Darkpurple_circle": await self.AddOneRole(716390741475196969,Member,Guild,RolesID)
            elif str(Emoji.name) == "Darkgreen_circle": await self.AddOneRole(716391516137848863,Member,Guild,RolesID)
            elif str(Emoji.name) == "Brown_circle": await self.AddOneRole(716391507980189726,Member,Guild,RolesID)
            elif str(Emoji.name) == "Blue_circle": await self.AddOneRole(716391501772488748,Member,Guild,RolesID)
            elif str(Emoji.name) == "Pink_circle": await self.AddOneRole(716390742012199024,Member,Guild,RolesID)
            elif str(Emoji.name) == "Scarlet_circle": await self.AddOneRole(716391505425858641,Member,Guild,RolesID)
            elif str(Emoji.name) == "Golden_circle": await self.AddOneRole(716391505073274920,Member,Guild,RolesID)
        #----
    async def AddOneRole(self,ID,Member,Guild,RolesID):
        Role = Guild.get_role(ID)
        await Member.add_roles(Role,reason="Выбрал роль")
        for role in Member.roles:
            if role.id in RolesID and role != Role:
                await Member.remove_roles(role,reason="Убрана старая роль")

    async def _CreateRoom(self,GetChannel, User):
        Guild = await self.fetch_guild(419879599363850251)
        Member = await Guild.fetch_member(User.id)
        # Channel = await self.fetch_channel(717131413828403212)
        # print(GetChannel.topic)
        topic = "Создание текстовой личной комнаты"
        if GetChannel.topic == topic:
            Category = GetChannel.category
            Position = GetChannel.position
            Position -= 1
            # await GetChannel.trigger_typing()
            Guard = Guild.get_role(610078093260095488)
            overwrites = {
                Guard: discord.PermissionOverwrite(read_messages=True,send_messages=True,read_message_history=True)
            }
            NewRoom = await Guild.create_text_channel(
                name = "комната",
                category = Category,
                position = Position,
                topic = topic,
                reason = "Новая комната",
                overwrites=overwrites
                )
            Message = "Написав что либо в эту комнату, вы её создадите"
            NewMessage = await NewRoom.send(Message)
            async for message in GetChannel.history(limit=10):
                if message.author == self.user:
                    if message.content == Message:
                        Message = f"{User.mention}, Вы успешно создали комнату"
                        await message.edit(
                            content=Message,
                            reason = "Уведомление о успешной созданной комнате"
                            )
            # overwrites = {
            #     Guard: discord.PermissionOverwrite(read_messages=False,send_messages=False,read_message_history=False),
            #     User: discord.PermissionOverwrite(read_messages=True,send_messages=True,read_message_history=True)
            # }
            await GetChannel.edit(
                name = f"{User.name}",
                topic = f"Комната игрока {User.name}",
                category = Category,
                reason = "Игрок создал новую комнату",
            )
            overwrite = discord.PermissionOverwrite()
            overwrite.send_messages = False
            overwrite.read_messages = False
            await GetChannel.set_permissions(Guard,overwrite=overwrite)
            overwrite.send_messages = True
            overwrite.read_messages = True
            await GetChannel.set_permissions(Member,overwrite=overwrite)
            task1 = asyncio.create_task(
                self.NotMessagesInRoom(GetChannel))
            task2 = asyncio.create_task(
                self.CommandInCustomRoom(GetChannel))
            asyncio.gather(task1,task2)

    async def on_typing(self,GetChannel, User, When):
        if GetChannel.topic == "Создание текстовой личной комнаты":
            await self._CreateRoom(GetChannel,User)

    async def CommandInCustomRoom(self,Channel : discord.TextChannel):
        historyMessages = list()
        while Channel.topic != "Комната удалена":
            try:
                async for message in Channel.history(limit=10):
                    Message = str(message.content)
                    try:
                        Command = Message.split()[0].upper()
                        Mention = message.mentions
                    except IndexError: pass
                    if Message not in historyMessages: #Команда не повторяется
                        historyMessages.append(Message)
                        if Command == "Add".upper():
                            Members = message.mentions
                            for member in Members:
                                overwrite = discord.PermissionOverwrite()
                                overwrite.send_messages = True
                                overwrite.read_messages = True
                                # overwrite.view_channel = True
                                await message.channel.set_permissions(member,overwrite=overwrite)
                        if Command == "Remove".upper():
                            Members = message.mentions
                            for member in Members:
                                overwrite = discord.PermissionOverwrite()
                                overwrite.send_messages = False
                                overwrite.read_messages = False
                                # overwrite.view_channel = False
                                await message.channel.set_permissions(member,overwrite=overwrite)

                await asyncio.sleep(0.35)
            except discord.errors.NotFound: 
                break

    async def NotMessagesInRoom(self,Channel):
        MaxTime = 900
        Times = MaxTime
        historyMessages = list()
        while Times > 0:
            await asyncio.sleep(10)
            NewMessages = False
            try:
                async for message in Channel.history(limit=100):
                    if str(message.content) not in historyMessages:
                        Times = MaxTime
                        NewMessages = True
                        historyMessages.append(str(message.content))
                if NewMessages == False:
                    Times -= 1
            except discord.errors.NotFound:
                Times = 0
        try:
            await Channel.edit(
                topic = "Комната удалена"
            )
            await Channel.delete(reason="Комната не взаимодейсвует")
        except: pass
    async def _TimeShow(self,Member,Channel):
        Timer = 3600
        while Timer > 0:
            Timer -= 1
            await asyncio.sleep(1)
        overwrite = discord.PermissionOverwrite()
        overwrite.send_messages = False
        overwrite.read_messages = False
        overwrite.read_message_history = False
        await Channel.set_permissions(Member,overwrite=overwrite)
InternetActive()

while True:
    time.sleep(1)
    if is_internet():
        if(internetWasOff == True):
            print("Internet is active")
            InternetActive()
            internetWasOff = False
    else:
        internetWasOff = True