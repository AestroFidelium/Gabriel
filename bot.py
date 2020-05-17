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
import ast
from bs4 import BeautifulSoup
import lxml
import requests
import datetime
import asyncio
 
#matplotlib

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
    with open(f"./Stats/Clients.txt","r") as file:
        PlayersInStats = int(file.readline())
        for target_list in range(PlayersInStats):
            RDtxt = file.readline()
            lst.append(RDtxt)
            try:
                curPla = lst[target_list].split();curPla = curPla[0]
                try:
                    with open(f"./Stats/Main/{curPla}.txt","r") as fileTo:
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
    #Date = Date.split("-")
    #Year = Date[0]
    txt = str(f"(C) {Who} \n({Date})")
    draw.text(area,txt,font=font,fill=Color)

    nameSave = "Create_quotes.png"
    MainMsage.save(nameSave)
    df = discord.File(nameSave,nameSave)
    return df

def _RemoveMoney(_UserName_,Count):
    with open(f"./Stats/Shop/{str(_UserName_)}.txt","r") as file:
        Msages = int(file.readline())
        Gold = int(file.readline())
    Gold -= Count
    with open(f"./Stats/Shop/{str(_UserName_)}.txt","w") as file:
        file.writelines(f"{Msages}\n")
        file.writelines(f"{Gold}")
def _SetMoney(_UserName_,Count):
    with open(f"./Stats/Shop/{str(_UserName_)}.txt","r") as file:
        Msages = int(file.readline())
        Gold = int(file.readline())
    Gold = Count
    with open(f"./Stats/Shop/{str(_UserName_)}.txt","w") as file:
        file.writelines(f"{Msages}\n")
        file.writelines(f"{Gold}")

def WriteLastMessage(Who : str,Msg : str,Date : str):
    with open(f"./Configs/LastMessage.txt","w") as file:
        file.writelines(Who)
        file.writelines(f"\n{Msg}")
        file.writelines(f"\n{str(Date)}")
def ReadLastMessage():
    with open(f"./Configs/LastMessage.txt","r") as file:
        Who = file.readline()
        Msg = file.readline()
        Date = file.readline()
    return Who , Msg , Date
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
def WriteNewMessage(_UserName_,_Message_,_NowTime_):
    _NowTime_DateWrite = _NowTime_.split(",")
    _OldMessage_ = str()
    try:
        with open(f"./Resurses/Messages/{_NowTime_DateWrite[0]}.txt","r") as file:
            for line in file.readlines():
                _OldMessage_ += line
        pass
    except Exception:
        _OldMessage_ = "Начало нового дня."
    with open(f"./Resurses/Messages/{_NowTime_DateWrite[0]}.txt","w") as file:
        file.writelines(_OldMessage_)
        file.writelines(f"\n{_UserName_}[{_NowTime_DateWrite[1]}] : {_Message_}")
        pass
    pass
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

def Attack(_UserName_ : str,_Target_ : str):
    with open(f"./Stats/Main/{_UserName_}.txt","r") as file:
        IntCurExp = int(file.readline())
        IntCurLvl = int(file.readline())
        IntMaxHealth = int(file.readline())
        IntCurHealth = int(file.readline())
        IntMaxDamage = int(file.readline())
        Description = str(file.readline())
    with open(f"./Stats/Main/{_Target_}.txt","r") as file:
        EnIntCurExp = int(file.readline())
        EnIntCurLvl = int(file.readline())
        EnIntMaxHealth = int(file.readline())
        EnIntCurHealth = int(file.readline())
        EnIntMaxDamage = int(file.readline())
        EnDescription = str(file.readline())
    GetDamage = random.randint(0,IntMaxDamage)

    EnIntCurHealth -= GetDamage

    FreeLvlHA = EnIntCurLvl / 5

    if EnIntCurHealth <= 0:
        EnIntCurHealth = EnIntMaxHealth
        EnIntCurLvl -= int(FreeLvlHA)
        IntCurLvl += int(FreeLvlHA)
        time.sleep(0.1)


        Emb = discord.Embed( title = _Target_ + " убит(а)")
        Emb.add_field(name = 'Потерял(а) могущество : ',value = str(int(FreeLvlHA)) + " лвл.")
        if IntCurLvl == 4:
            Emb.add_field(name = 'Минимальный уровень',value =  "4",inline = True)
        Emb.add_field(name = 'Здоровье : ',value = str(EnIntCurHealth) + " ед. / " + str(EnIntMaxHealth) + " ед.",inline = False)
        Emb.add_field(name = 'Получил(а) урона : ',value = str(GetDamage) + " ед.",inline = True)

        #await message.channel.send(embed = Emb)

        IntMaxHealth += 10 * int(FreeLvlHA)
        IntCurHealth += 10 * int(FreeLvlHA)
        IntMaxDamage += random.randint(1,35) * int(FreeLvlHA)
        if ((IntCurHealth + 5 * int(FreeLvlHA)) < (IntMaxHealth)):
            IntCurHealth += 5 * int(FreeLvlHA)
        else:
            IntCurHealth = IntMaxHealth
        
        EnIntMaxHealth -= 10 * int(FreeLvlHA)
        EnIntMaxDamage -= random.randint(1,35) * int(FreeLvlHA)
        EnIntCurHealth = EnIntMaxHealth
    with open(f"./Stats/Main/{_UserName_}.txt","w") as file:
        file.writelines(str(IntCurExp))
        file.writelines(str(IntCurLvl))
        file.writelines(str(IntMaxHealth))
        file.writelines(str(IntCurHealth))
        file.writelines(str(Description))
    with open(f"./Stats/Main/{_Target_}.txt","w") as file:
        file.writelines(str(EnIntCurExp))
        file.writelines(str(EnIntCurLvl))
        file.writelines(str(EnIntMaxHealth))
        file.writelines(str(EnIntCurHealth))
        file.writelines(str(EnDescription))
    return Emb
    
def StrToDict(**fields):
    """
    `str` : текст который нужно будет конвентировать в Dict
    """
    _str = str(fields.pop('str'))
    NwDict = ast.literal_eval(f'{_str}') ; NwDict = dict(NwDict)
    return NwDict
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
    with open(f"./Stats/Shop/{_UserName_}.txt","w") as file:
        file.writelines("0")
        file.writelines("\n0")
    lstClients = list()
    if new_Client == True:
        with open(f"./Stats/Clients.txt","r") as file:
            for lines in file.readlines():
                lstClients.append(lines)
        with open(f"./Stats/Clients.txt","w") as file:
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
        with open(f"./Stats/Profile/{_UserName_}.txt","r") as file:
            _url = file.readline()
            return _url
    else:
        with open(f"./Stats/Profile/BackGround_{_UserName_}.txt","r") as file:
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
        with open("./Stats/Profile/" + _UserName_ + ".txt","w") as file:
            file.writelines(__url__)

            logo = StandartURL

            try:
                logo = urllib.request.urlopen(__url__).read()
                with open(f"{Resurses}{_UserName_}.webp", "wb") as fileTwo:
                    fileTwo.write(logo)
            except Exception:
                pass
    else:
        with open(f"./Stats/Profile/BackGround_{_UserName_}.txt","w") as file:
            file.writelines(__url__)

            logo = StandartURLBackGround

            try:
                logo = urllib.request.urlopen(__url__).read()
                with open(f"{Resurses}BackGround_{_UserName_}.webp", "wb") as fileTwo:
                    fileTwo.write(logo)
            except Exception:
                pass
        pass

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
        BackGround = Image.open(f"{Resurses}BackGround_{_UserName_}.webp")
    except: BackGround = Image.open(f"{Resurses}BackGround_StandartBackGround.webp")

    img = Image.open(Resurses + "Main.webp")
    try:
        N_Ava = Image.open(Resurses + _UserName_ + ".webp")
    except:
        raise ErrorAvatar("Отсустует аватарка")

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
    try:
        Item_ID = Functions.ReadEquipment(username=_UserName_,type="Экипировка")
        ItemProtect = Functions.CheckParametrsEquipment(username=_UserName_,ID=Item_ID)
        protect = ItemProtect["protect"]
        area = (161,143)
        Color = (0,0,0)
        font = ImageFont.truetype("arial.ttf",8)
        txt = str(f"Здоровье : {str(IntCurHealth)} ед./ {str(IntMaxHealth)} ({protect})")
        draw.text(area,txt,font=font,fill=Color)
    except FileNotFoundError:
        area = (161,143)
        Color = (0,0,0)
        font = ImageFont.truetype("arial.ttf",8)
        txt = str(f"Здоровье : {str(IntCurHealth)} ед./ {str(IntMaxHealth)}")
        draw.text(area,txt,font=font,fill=Color)

    area = (161,158)
    Color = (0,0,0)
    font = ImageFont.truetype("arial.ttf",8)
    try:
        DmgItemID = Functions.ReadEquipment(username=_UserName_,type="Оружие")
        Item = Functions.CheckParametrsEquipment(username=_UserName_,ID=DmgItemID)
        DamageItem = Item.pop('damage')
    except:
        DamageItem = 0
    
    txt = str(f"Урон : {str(IntMaxDamage)} +({DamageItem}) ед.")
    draw.text(area,txt,font=font,fill=Color)
    
    area = (110,280)
    Color = (0,0,0)
    try:
        Procent = (IntCurExp * 100) / (IntCurLvl * 5)
    except: Procent = 0
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
    draw.text(area,txt,font=font,fill=Color)

    Main_characteristics = Functions.ReadMainParametrs(username=_UserName_)

    strength = float(Main_characteristics.pop("strength"))
    agility = float(Main_characteristics.pop("agility"))
    intelligence = float(Main_characteristics.pop("intelligence"))
    plus = int(Main_characteristics.pop("plus"))
    if plus > 0:
        area = (210,280)
        Color = (100,110,90)
        font = ImageFont.truetype("arial.ttf",10)
        txt = str(f"Талант очки : {plus}")
        draw.text(area,txt,font=font,fill=Color)


    Color = (255,100,0)
    area = (15,175)
    font = ImageFont.truetype("arial.ttf",12)
    txt = str(f"Сила : \n{strength}")
    draw.text(area,txt,font=font,fill=Color)
    # draw.line((25 - 5,195,100 - 5,195),fill=Color,width=5)

    Color = (0,255,0)
    area = (15,200 + 10)
    font = ImageFont.truetype("arial.ttf",12)
    txt = str(f"Ловкость : \n{agility}")
    draw.text(area,txt,font=font,fill=Color)

    Color = (0,255,255)
    area = (15,225 + 20)
    font = ImageFont.truetype("arial.ttf",12)
    txt = str(f"Интеллект : \n{intelligence}")
    draw.text(area,txt,font=font,fill=Color)

    
            
    

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
    nameSave = "StatsPl.webp"
    #img.save(nameSave)
    BackGround = BackGround.resize((300,400)) #(358,481)
    area = (0,100) #(25,175)
    
    BackGround.paste(img.convert('RGB'), area, img)
    BackGround.save(nameSave)

    sf = discord.File(nameSave,nameSave)
    #await message.channel.send(" ",file=sf)
    pass
    return sf

def RatingSystem():
    Positions = 0
    MainPicture = Image.open(Resurses + "rating statistics.webp")
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
            with open(f"./Stats/Main/{_UserName_}.txt","r") as file:
                CurLvl = int(file.readline())
                CurLvl = int(file.readline())
                if (CurLvl == _Level_) and (_UserName_ not in alreadyChecked):

                    alreadyChecked.append(_UserName_)

                    Positions = (500 * (PositionRange - 1))

                    Picture = Image.open(Resurses + "a Place.webp")
                    PictureDraw = ImageDraw.Draw(Picture)

                    Ava = Image.open(Resurses + _UserName_ + ".webp")
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
                    nameSave = "RatingSystem.webp"

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
    client.run(BazaDate.token)
class MyClient(discord.Client):
    _VoiceClient = None
    async def Dialog(self,message):

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

        if RandomSaying == 1:
            messages = Functions.ReadWords()
            try:
                Step = int(CurCommandPlayer)
                await message.channel.send(Functions.FutureMessageDef(message=messages,step=Step))
            except:
                pass

        if CurCommand == "G":
            await _Message_.delete()
            # messages = Functions.ReadWords()
            Step = int(CurCommandPlayer)
            # msg = Functions.FutureMessageDef(message=messages,step=Step)
            Gabriel = Functions.Gabriel()
            try:
                msg = Gabriel.Message(Step)
            except Gabriel.TooManyWords:
                await message.channel.send("Столько слов я не знаю ;c",delete_after=5)
                return
            # print(f"message : {msg} \nreadWords : {messages}")
            try:
                await message.channel.send(msg)
            except discord.errors.HTTPException:
                await message.channel.send(f"Столько слов я не могу отправить ;c",delete_after=5)
            
        else:
            ChannelPossible = [696928662045458452,419879599363850253,686553674394239053]
            if _Channel_.id in ChannelPossible:
                Commands = ['PROFILE','ПРОФИЛЬ','P','П',
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
                'G','GABRIELE',
                'ГАБРИЭЛЬ',
                'КУПИТЬ','BUY','К','B',
                'TALANT',"ТАЛАНТ",
                "SELL_ITEM","S_I",
                "EVENT","E","Е","ИВЕНТ",
                "AU","AUCTION","АУКЦИОН",
                "Gabriel_Config"]
                if CurCommand not in Commands:
                    Functions.SaveWords(msg)
        #Команды Администрации
        if message.author.name == "KOT32500":
            if CurCommand == "GDDF": #Gabriel Delete Data File
                await _Message_.delete()
                Emb = discord.Embed( title = 'Стирание сохраненных слов')
                Emb.add_field(name = "Все сообщения, которые могла использовать Габриэль",value = "Были стёрты")
                await message.channel.send(embed = Emb,delete_after=10)
                Functions.ClearWords()
    async def on_ready(self):
        print(f"Logged on as , {self.user} MODULE : bot.py")
        randomStatus = random.randint(0,6)
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

        _ReadLastMessage = ReadLastMessage()


        WriteNewMessage(UserName_,msg,NowTime.strftime("%Y-%m-%d,%H:%M:%S"))



        if (Time_between_dates_mins <= -20) or (Time_between_dates_hour <= -1) or (Time_between_dates_day <= -1):
                Functions.CreateNewBoss()
                Boss_Dead = "No"
                await MiniGame.send("Создан новый босс")
                return

                # SplitToDay = today.split("-")

                # Time_between_dates_day = int(SplitToDay[2])
                # Time_between_dates_hour = int(SplitToDay[3])
                # Time_between_dates_mins = int(SplitToDay[4])

                # Time_between_dates_day -= NowTime.day
                # Time_between_dates_hour -= NowTime.hour
                # Time_between_dates_mins -= NowTime.minute
        if (CurCommand == "EVENT") or (CurCommand == "E") or (CurCommand == "Е"):
            await _Message_.delete()
            if (CurCommandEvent == "A") or (CurCommandEvent == "А") or (CurCommandEvent == "ATTACK"):
                try:
                    DmgItemID = Functions.ReadEquipment(username=UserName_,type="Оружие")
                    Item = Functions.CheckParametrsEquipment(username=UserName_,ID=DmgItemID)
                    DamageItem = Item.pop('damage')
                except:
                    DamageItem = 0
                try:
                    Inventores = Functions.ReadInventor(UserName_)
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
                    Functions.EditItem(username=UserName_,ID=DmgItemID,armor=armorItem,type="Оружие",damage=damageOld,classItem="Сломанный")
                    if armorItem == 0:
                        await message.channel.send(f"{UserName_} предмет [{NameItem}] сломался")
                        Functions.WriteEquipment(username=UserName_,type="Оружие",ID=0)
                except:
                    pass
                YourDamage = random.randint(1,IntMaxDamage + DamageItem)

                Boss_CurHealth -= YourDamage

                if (Boss_CurHealth <= 0) and (Boss_Dead == "No"):
                    await message.channel.send(f"{UserName_} убил босса, и получил {Boss_GetGold} зототых")
                    Inventor = Functions.ReadInventor(UserName_)
                    RandomID = random.randint(1,999999)
                    Classes = ['Обычный','Редкий','Эпический','Первоначальный']
                    randomClasses = random.randint(0,3)
                    Classes = Classes[randomClasses]

                    Boss_Dead = "Yes"
                    with open(f"./Stats/EventBoss.txt","w") as file:
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
                        TypeTheItem = "Оружие"
                        NameForItem = ['Медное копье','Медный лук','Медный кинжал','Медный нож','Медная рапира']
                        NameForItem = NameForItem[random.randint(0,len(NameForItem) - 1)]
                        BalansListItem = Functions.BalansList(type=TypeTheItem,classItem=Classes)
                        BalansListDamageItem = BalansListItem.pop('damage')
                        BalansListGoldItem = BalansListItem.pop('gold')
                        Functions.WriteInventor(username=UserName_,old=Inventor,type="Оружие",name=NameForItem,classItem=Classes,ID=RandomID,armor=100,damage=BalansListDamageItem,gold=BalansListGoldItem)
                    if Classes == "Редкий":
                        TypeTheItem = "Оружие"
                        NameForItem = ['Редкое железное копье','Редкий лук','Редкий железный кинжал','Редкий железный нож','Редкая железная рапира','Редкий железный меч.']
                        NameForItem = NameForItem[random.randint(0,len(NameForItem) - 1)]
                        BalansListItem = Functions.BalansList(type=TypeTheItem,classItem=Classes)
                        BalansListDamageItem = BalansListItem.pop('damage')
                        BalansListGoldItem = BalansListItem.pop('gold')
                        Functions.WriteInventor(username=UserName_,old=Inventor,type="Оружие",name=NameForItem,classItem=Classes,ID=RandomID,armor=100,damage=BalansListDamageItem,gold=BalansListGoldItem)
                    if Classes == "Эпический":
                        TypeTheItem = "Оружие"
                        NameForItem = ['Эпическое копье','Эльфийский лук','Кинжал тени','Два топора','Секира',"Сияющий меч","Посох","Платиновый меч","Длинный меч"]
                        NameForItem = NameForItem[random.randint(0,len(NameForItem) - 1)]
                        BalansListItem = Functions.BalansList(type=TypeTheItem,classItem=Classes)
                        BalansListDamageItem = BalansListItem.pop('damage')
                        BalansListGoldItem = BalansListItem.pop('gold')
                        Functions.WriteInventor(username=UserName_,old=Inventor,type="Оружие",name=NameForItem,classItem=Classes,ID=RandomID,armor=100,damage=BalansListDamageItem,gold=BalansListGoldItem)
                    if Classes == "Первоначальный":
                        TypeTheItem = "Оружие"
                        NameForItem = ['Палка','Дубинка','Перчатки','Тяжелая палка','Острый камень']
                        NameForItem = NameForItem[random.randint(0,len(NameForItem) - 1)]
                        BalansListItem = Functions.BalansList(type=TypeTheItem,classItem=Classes)
                        BalansListDamageItem = BalansListItem.pop('damage')
                        BalansListGoldItem = BalansListItem.pop('gold')
                        Functions.WriteInventor(username=UserName_,old=Inventor,type="Оружие",name=NameForItem,classItem=Classes,ID=RandomID,armor=100,damage=BalansListDamageItem,gold=BalansListGoldItem)
                    

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
                            GoldPlayer += RandomAddMoney
                            Functions.WriteMainParametrs(username=UserName_,money=GoldPlayer)
                            await message.channel.send(f"{UserName_} взял(а) ежедневный бонус, в {RandomAddMoney}:moneybag:")
                            with open(f"./Stats/EveryDay/{UserName_}.txt","w") as fileTwo:
                                fileTwo.writelines(str(NowTime.day))
                                fileTwo.writelines(f"\n{str(RandomAddMoney)}")
                        else:
                            await message.channel.send(f"{UserName_}, вы уже брали ежедневный бонус в размере {EarlierTakeGem}:moneybag:")
                        
                except FileNotFoundError:
                    with open(f"./Stats/EveryDay/{UserName_}.txt","w") as file:
                        file.writelines(str(NowTime.day))
                        RandomAddMoney = random.randint(5,100)
                        file.writelines(f"\n{str(RandomAddMoney)}")
                        GoldPlayer += RandomAddMoney
                        Functions.WriteMainParametrs(username=UserName_,money=GoldPlayer)
                        await message.channel.send(f"{UserName_} взял(а) ежедневный бонус, в {RandomAddMoney}:moneybag:")
            time.sleep(0.01)
            if (CurCommandEvent == "CASINO") or (CurCommandEvent == "C"):
                MainStats = Functions.ReadMainParametrs(username=UserName_)
                Money = MainStats.pop("money")
                try:
                    CurCountForCasino = int(CurCountForCasino)
                except ValueError:
                    await message.channel.send(f":negative_squared_cross_mark:`Нужно указать число` :negative_squared_cross_mark:")
                    return
                
                try:
                   # oldMoney = Money
                    if CurCountForCasino > Money:
                        CurCountForCasino = Money
                    if CurCountForCasino < 0:
                        await message.channel.send(f"Нельзя указать < 0")
                        return
                    Money -= CurCountForCasino

                   # GetMoney = int(CurCountForCasino * (random.random() * 2))
                    rnd = random.random()
                    rnd *= 2
                    GetMoney = int(CurCountForCasino * rnd)
                    Money += GetMoney
                   # GetMoney = 1
                    #GetMoney
                   # print(GetMoney)
                    await message.channel.send(f"Коэффициент : {rnd}%. \nСтавка : {CurCountForCasino} золотых.\nПолученно золотых : {GetMoney}.\nТекущее количество золотых : {Money} золотых.")

                    #_AddMoney(UserName_,GetMoney)
                    # _SetMoney(UserName_,Money)
                    Functions.WriteMainParametrs(username=UserName_,money=Money)



                    pass
                except ValueError:
                    await message.channel.send(f"Ошибка : проверьте правильность написания команды")
                


            if (CurCommandEvent == "P") or (CurCommandEvent == "П") or (CurCommandEvent == "Р") or (CurCommandEvent == "ПРОФИЛЬ") or (CurCommandEvent == "PROFILE"):
                await message.channel.send(f" ",file = ProfileBoss(today,Boss_MaxHealth,Boss_CurHealth,Boss_GetGold,Boss_Dead))
        if (CurCommand == "ЦИТАТА"):
            await _Message_.delete()
            NickNameLastMessage = _ReadLastMessage[0] ; NickNameLastMessage = NickNameLastMessage.split() ; NickNameLastMessage = NickNameLastMessage[0]
            await message.channel.send(f" ",file=Create_quotes(NickNameLastMessage,_ReadLastMessage[1],_ReadLastMessage[2]))
        
        Year = NowTime.strftime("%Y-%m-%d,%H:%M")
        WriteLastMessage(UserName_,msg,Year)
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
        _Channel_ = None
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
        # print(_Player_.avatar_url)
        # DownloadFile = requests.get(_Player_.avatar_url, stream=True)
        # with open("AVATAR ME.webp","bw") as file:
        #     for chunk in DownloadFile.iter_content(15360):
        #         file.write(chunk)
        #         pass
        #     pass
        # sf = discord.File("AVATAR ME.webp","AVATAR ME.webp")
        # await message.channel.send(" ",file=sf)

        Message = message.content
        _Gabriel = Functions.Gabriel()
        self.Config = _Gabriel.Config()
        await self.Config.Start(message.guild.id,self)
        Setting = self.Config.Read()
        Guild = await self.fetch_guild(message.guild.id)
        Member = await Guild.fetch_member(message.author.id)
        Administrator = False
        for role in Member.roles:
            RolePermission = role.permissions
            if RolePermission.administrator == True:
                Administrator = True
        Command = str(Message).split(" ")[0].upper()
        if Administrator == True:
            if Command == "GABRIEL_CONFIG":
                file = await _Gabriel.Config.ConfigOpen(self,Setting)
                await message.channel.send(f" ",file=file)
            if Command == "Gabriel_Config_Edit".upper():
                Config = str(Message).split(" ")[1].upper()
                if Config == "Chat".upper():
                    OnlineOrOffline = str(Message).split(" ")[2].upper()
                    try:
                        self.Config.Write(Chat=OnlineOrOffline)
                        await message.channel.send(f"Текущее состояние : {OnlineOrOffline}")
                    except Functions.Gabriel.Config.NotOnlineOrOffline:
                        AddOrRemove = str(Message).split(" ")[2].upper()
                        Possibles = ['ADD','REMOVE',"CHANNELS","GENERAL","PRIVATE"]
                        Chat = _Gabriel.Chat(self.Config.server,self.Config.Client)
                        if AddOrRemove in Possibles:
                            if AddOrRemove == "ADD".upper():
                                Index = str(Message).split(" ")[3] ; Index = int(Index)
                                try:
                                    GetChannel = await self.fetch_channel(Index)
                                    Chat.LoadChat(Index)
                                    await message.channel.send(f"{GetChannel.name}, добавлен.")
                                except discord.errors.NotFound:
                                    await message.channel.send(f"Канал не может быть добавлен, так как его не существует")
                            if AddOrRemove == "REMOVE".upper():
                                Index = str(Message).split(" ")[3] ; Index = int(Index)
                                try:
                                    GetChannel = await self.fetch_channel(Index)
                                    Chat.RemoveChat(Index)
                                    await message.channel.send(f"{GetChannel.name}, убран")
                                except discord.errors.NotFound:
                                    await message.channel.send(f"Канал не может быть убран, так как его уже не существует")
                            if AddOrRemove == "CHANNELS".upper():
                                Channels = Chat.SavedChat()
                                Answer = "Сохраненные каналы : "
                                ChannelsList = Channels["Activity"]
                                for _Channel in ChannelsList:
                                    GetChannel = await self.fetch_channel(_Channel)
                                    Answer += f"\n{GetChannel.name} ({_Channel})"
                                await message.channel.send(f"{Answer}")
                            if AddOrRemove == "GENERAL".upper():
                                
                                pass

                        else:
                            await message.channel.send(f"Доступные вариатны ответа : \nOnline / Offline \nADD ID/ REMOVE ID \nGeneral / Private")
                
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
                        Rooms = _Gabriel.Rooms(self.Config.server,self.Config.Client)
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
        
        if _Channel_.id == 691750825030320218 and message.author != self.user:
            MessageContent = message.content
            MessageContent = str.lower(MessageContent)
            try:
                await _Message_.delete()
            except:
                pass
            Agree = ["Yes","Agree","Да","Согласен","Конечно","Хорошо","Ок","Ok","Okay","Okey","Ог"]
            not_agree = ["No","No agree","Нет","Не","Неа","Нет уж"]
            if MessageContent in str(not_agree).lower():
                await message.channel.send("Ничего страшного. Зайти на сервер, вы можете когда вам угодно.",delete_after=2)
            elif MessageContent in str(Agree).lower():
                StartRole = OurServer.get_role(691735620346970123)
                TimeRole = OurServer.get_role(610078093260095488)

                await Member_Player.add_roles(TimeRole,reason="Прошел проверку")
                await Member_Player.remove_roles(StartRole,reason="Прошел проверку")

                StandartChannel = await self.fetch_channel(419879599363850253)
                await StandartChannel.send(f"{message.author.mention} присоединился на сервер",delete_after=300)
            
            if MessageContent not in str(not_agree).lower() and MessageContent not in str(Agree).lower():
                await message.channel.send("Это не похоже на ответ. Пожалуйста, следуйте указаниям",delete_after=2)
            return
        
        YourProfilParamerts = Functions.ReadMainParametrs(username=UserName_)
        IntCurExp = int(YourProfilParamerts.pop("exp"))
        Level = int(YourProfilParamerts.pop("lvl"))
        IntMaxHealth = int(YourProfilParamerts.pop("maxHealth"))
        IntCurHealth = int(YourProfilParamerts.pop("curHealth"))
        IntMaxDamage = int(YourProfilParamerts.pop("damage"))
        IntCurExp += 1
        Functions.WriteMainParametrs(username=UserName_,exp=IntCurExp)
        if IntCurExp > Level * 5:
            Level += 1
            maxLevel = int(YourProfilParamerts.pop("maxLevel"))
            plus = int(YourProfilParamerts.pop("plus"))
            if maxLevel < Level:
                maxLevel = Level
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
            with open(f"{Resurses}{UserName_}.webp","r"): pass
        except:
            DownloadFile = requests.get(_Player_.avatar_url, stream=True)
            with open(f"{Resurses}{UserName_}.webp","bw") as file:
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
            await _Message_.add_reaction("🇵") ; await _Message_.add_reaction("🇷") ; await _Message_.add_reaction("🇦") ; await _Message_.add_reaction("🇮") ; await _Message_.add_reaction("🇸") ; await _Message_.add_reaction("🇪")
            pass
        if CurCommand == "GS":
            try:
                await _Message_.delete()
            except:
                pass
            
            _ChannelVoice_ = await self.fetch_channel(message.author.voice.channel.id)
            InVoice = False
            for member in _ChannelVoice_.members:
                if member == _Gabriele_:
                    InVoice = True
            if InVoice == False:
                _VoiceClient = await _ChannelVoice_.connect()
                RandomInt = random.randint(1,36)
                RandomSound = f"JoinVoice ({RandomInt}).mp3"
                _VoiceClient.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source=f"./Resurses/JoinVoice/{RandomSound}"))
            else:
                await message.channel.send(f"Не могу проиграть звук",delete_after=1)


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
                    with open(f"{Resurses}{UserName_}.webp","bw") as file:
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
                    Inventores = Functions.ReadInventor(UserName_)
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
                    Functions.EditItem(username=UserName_,ID=DmgItemID,armor=armorItem,type="Оружие",damage=damageOld,classItem="Сломанный")
                    if armorItem == 0:
                        await message.channel.send(f"{UserName_} предмет [{NameItem}] сломался")
                        Functions.WriteEquipment(username=UserName_,type="Оружие",ID=0)
                except:
                    pass
                GetDamage = random.randint(0,IntMaxDamage + int(DamageItem))
                strength = Functions.ReadMainParametrs(username=UserName_) ; strength = float(strength.pop("strength"))
                GetDamage *= strength

                Item_ID = Functions.ReadEquipment(username=CurCommandPlayer,type="Экипировка")
                ItemProtect = Functions.CheckParametrsEquipment(username=CurCommandPlayer,ID=Item_ID)
                protect = int(ItemProtect["protect"])

                GetDamage -= protect

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
                        plus += 1 * (IntCurLvl - maxLevel)
                        maxLevel = IntCurLvl


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
                await message.channel.send(":warning: `Профиль не найден, или этого ирока просто не существует` :warning:",delete_after=2)
        if (CurCommand == 'PROFILE'):
            
            if CurCommandPlayer != "":
                try:
                    try:
                        await message.channel.send(" ",file=profileEdit(CurCommandPlayer))
                    except:
                        await message.channel.send(":warning: `Профиль не найден, или этого ирока просто не существует` :warning:",delete_after=2)
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
                nullWrite(UserName_,False)
                await message.channel.send(":tools: `Вы успешно сбросили собственный аккаунт` :tools:",delete_after=2)
                return
            else:
                if UserName_ != "KOT32500":
                    await message.channel.send(":no_entry: `У вас нет прав на это` :lock:",delete_after=2)
                else:
                    nullWrite(CurCommandPlayer,False)
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
                old = Functions.ReadInventor(UserName_)
                oldList = old.split("\n")
                ItemList = list()
                for line in oldList:
                    NwDict = ast.literal_eval(f'{line}') ; NwDict = dict(NwDict)
                    ItemList.append(str(NwDict))
            except:
                IDrandom = random.randint(1,99999999)
                Functions.WriteInventor(username=UserName_,old="",type="Оружие",name="Ржавый сломанный ножик",classItem="Первоначальный",ID=IDrandom,armor=1000,damage=5,gold=100)
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

                # if type_ == "Предмет":
                    # SendInfo += f"Имя предмета : {name}\nТип предмета : {type_} \nКласс предмета : {classItem} \nID предмета : {ID}\nЗолотых для улучшения : {gold}\nДлительность : {duration}\n\n"
                if type_ == "Оружие":
                    # SendInfo += f"Имя предмета : {name}\nТип предмета : {type_} \nКласс предмета : {classItem} \nID предмета : {ID}\nЗолотых для улучшения : {gold}\nПрочность : {armor}\nУрон : {damage}\n\n"
                    ImageInventor = Functions.CreateImageInventor(username=UserName_,typeItem=type_,name=name,classItem=classItem,ID=ID,gold=gold,armor=armor,damage=damage)
                if type_ == "Экипировка":
                    # SendInfo += f"Имя предмета : {name}\nТип предмета : {type_} \nКласс предмета : {classItem} \nID предмета : {ID}\nЗолотых для улучшения : {gold}\nПрочность : {armor}\nЗащита : {protect}\n\n"
                    ImageInventor = Functions.CreateImageInventor(username=UserName_,typeItem=type_,name=name,classItem=classItem,ID=ID,gold=gold,armor=armor,protect=protect)
                # if type_ == "Ингридиент":
                #     SendInfo += f"Имя предмета : {name}\nТип предмета : {type_} \nКласс предмета : {classItem} \nID предмета : {ID}\nЗолотых для улучшения : {gold}\nКоличество : {count}\n\n"
                await message.channel.send(f"ID : {ID}",file=ImageInventor)
            pass
        if CurCommand == "WEAR":
            await _Message_.delete()
            old = Functions.ReadInventor(UserName_)
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
            Inventore = Functions.ReadInventor(UserName_)
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
                            Functions.EditItem(username=UserName_,ID=itemID,type=type_,classItem=NewClassItem,armor=NewArmor,gold=NewGold,damage=NewDamage)
                            Functions._Gold(username=UserName_,do="Убавить",count=GoldSell)
                            return
                        if (type_ == "Экипировка"):
                            NewProtect = NewUpgrade.pop('protect')
                            NewArmor = NewUpgrade.pop('armor')
                            NewGold = NewUpgrade.pop('gold')
                            Functions.EditItem(
                                username=UserName_,
                                ID=itemID,
                                type=type_,
                                classItem=NewClassItem,
                                armor=NewArmor,
                                gold=NewGold,
                                protect=NewProtect
                                )
                            Functions._Gold(username=UserName_,do="Убавить",count=GoldSell)
                            return

                    Functions._Gold(username=UserName_,do="Убавить",count=GoldSell)
                    if (type_ == "Оружие"):
                        damage = itemDict['damage']
                        armor = itemDict['armor']
                        Functions.EditItem(username=UserName_,ID=itemID,type=type_,classItem=classItem,armor=armor,damage=damage,gold=gold)
                    elif type_ == "Экипировка":
                        protect = itemDict['protect']
                        armor = itemDict['armor']
                        Functions.EditItem(
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
            Inventore = Functions.ReadInventor(UserName_)
            for item in Inventore.split("\n"):
                itemDict = Functions.StrToDict(str=item)
                itemID = itemDict.pop('ID')
                if itemID == IDitem:
                    name = itemDict.pop("name")
                    try:
                        MoneyEnd = Functions.SellItem(username=UserName_,ID=IDitem)
                        await message.channel.send(f"Вы продаете предмет : {name} \nЗа {MoneyEnd} золотых")
                    except Functions.LastItem:
                        await message.channel.send(f"Вы не можете продать единственный предмет, в инвентаре")
                    
            pass

    
        # if CurCommand == "ROLE":
        #     try:
        #         RoleMentions = _Message_.raw_role_mentions[0]
        #         RoleMentions = OurServer.get_role(RoleMentions)
        #         MentionPlayer = await OurServer.fetch_member(_Mention_.id)

        #         Can = [578514082252980234,626028536305811487,578514024782626837,691209621968519188,692917601076248657,688482228962983968,578517475042394113,610078093260095488,622412934391267378,625966754769928202,632180542070325248,686553299641827331,688015318396043317,691735620346970123,623063847497891840,419879599363850251]

        #         if RoleMentions.id not in Can:
        #             await MentionPlayer.add_roles(RoleMentions)
        #             # print(f"{MentionPlayer} {type(MentionPlayer)} {_Mention_.id} {_Mention_.name}")
        #             await message.channel.send(f"{_Mention_.mention} повысили до {RoleMentions.mention}")
        #         else:
        #             await message.channel.send(f"{_Mention_.mention} нельзя повысить до {RoleMentions.mention}")
                
        #         pass
        #     except:
        #         await message.channel.send(f"Ошибка в команде",delete_after=5)


        # if CurCommand == "GUILD":
        #     EveryOne = OurServer.get_role(419879599363850251)
        #     CreatorGuild = OurServer.get_role(692917601076248657)
        #     Member = await OurServer.fetch_member(message.author.id)
        #     await Member.add_roles(CreatorGuild)
        #     # await Functions.GetPermissions(self)
        #     perms = discord.Permissions(267910976)
        #     color = discord.colour.Colour(2123412)
        #     Guard = await OurServer.create_role(name=f"Стража Гильдии ({UserName_})",permissions=perms,colour=color)
        #     Permissions = {
        #         EveryOne: discord.PermissionOverwrite(read_messages=False,send_messages=False,read_message_history=False),
        #         Guard: discord.PermissionOverwrite(read_messages=True,send_messages=True,read_message_history=True),
        #         message.author: discord.PermissionOverwrite(read_messages=True,send_messages=True,read_message_history=True,manage_channels=True)
        #     }
        #     newGuild = await OurServer.create_category(name="Гильдия",overwrites=Permissions)
        #     Info = await OurServer.create_text_channel(name="Информация",category=newGuild,overwrites=Permissions)
        #     pass
        
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
                    strength += float(0.01 * Number)
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
                    agility += (0.025 * Number)
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
                    intelligence += (0.03 * Number)
                    plus -= Number
                    Functions.WriteMainParametrs(username=UserName_,intelligence=intelligence,plus=plus)
                    await message.channel.send(f"Вы успешно повысили интеллект, на {Number} ед.",delete_after=5)
                pass
            pass
        
        
        if CurCommand == "AU":
            Auction = Functions.Auction()
            CurCommandPlayer = str(CurCommandPlayer).upper()
            if CurCommandPlayer == "ADD":
                ItemID = int(msgSP[2])
                GoldCost = int(msgSP[3])
                if GoldCost < 100: 
                    await message.channel.send("Число не должно быть меньше 100")
                    return
                Auction.AddAuction(username=UserName_,ID=ItemID,goldAuction=GoldCost)
                await message.channel.send(f'{FixText(f"Вы успешно поставили выбранный торг, за {GoldCost}")}')
                # Functions._Gold(username=UserName_,do="Убавить",count=GoldCost)
            if CurCommandPlayer == "BUY":
                AuctionID = int(msgSP[2])
                GoldCost = int(msgSP[3])
                try:
                    Auction.RemoveAuction(username=UserName_,gold=GoldCost,AuctionID=AuctionID)
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
                AllAuctions = Auction.ReadAuction()
                AllAuctions = AllAuctions.split("\n")
                for _Auction in AllAuctions:
                    AuctionDict = Functions.StrToDict(str=_Auction)
                    Owner = str(AuctionDict.pop("username"))
                    ItemID = int(AuctionDict.pop("ID"))
                    goldAuction = int(AuctionDict.pop("goldAuction"))
                    ItemType = str(AuctionDict.pop("type"))
                    ItemName = str(AuctionDict.pop("name"))
                    ClassItem = str(AuctionDict.pop("classItem"))
                    ItemGold = int(AuctionDict.pop("gold"))
                    if ItemType == "Оружие":
                        ItemArmor = int(AuctionDict.pop("armor"))
                        ItemDamage = int(AuctionDict.pop("damage"))
                        await message.channel.send(f"Владелец : {Owner}\nИндекс предмета : {ItemID}\nСтоимость торга : {goldAuction}\nТип предмета : {ItemType}\nИмя предмета : {ItemName}\nКласс предмета : {ClassItem}\nЗолото в предмете : {ItemGold}\nПрочность : {ItemArmor}\nУрон : {ItemDamage}")
                    if ItemType == "Экипировка":
                        ItemArmor = int(AuctionDict.pop("armor"))
                        ItemProtect = int(AuctionDict.pop("protect"))
                        await message.channel.send(f"Владелец : {Owner}\nИндекс предмета : {ItemID}\nСтоимость торга : {goldAuction}\nТип предмета : {ItemType}\nИмя предмета : {ItemName}\nКласс предмета : {ClassItem}\nЗолото в предмете : {ItemGold}\nПрочность : {ItemArmor}\nЗащита : {ItemProtect}")
                    pass
                pass
            
            pass
        

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

        if Msages >= 5:
            Gold += 1
            Msages = 0

        MainStats = Functions.ReadMainParametrs(username=UserName_)
        IntCurExp = int(MainStats.pop("exp"))
        IntCurLvl = int(MainStats.pop("lvl"))
        IntMaxHealth = int(MainStats.pop("maxHealth"))
        IntCurHealth = int(MainStats.pop("curHealth"))
        IntMaxDamage = int(MainStats.pop("damage"))

        if (CurCommand == "BUY") or (CurCommand == "B") or (CurCommand == "Б") or (CurCommand == "КУПИТЬ") or (CurCommand == "К"):
            #Начало
            await _Message_.delete()
            if CurBuyItem == "ЛЕЧЕНИЕ":
                if CurCountBuyItem != "":
                    BuyItem = _BuyItem(5,Gold,CurCountBuyItem)
                    _CountBuy = BuyItem[0]
                    str1 = BuyItem[1]
                    _Gold_ = BuyItem[2]
                    Gold = _Gold_
                    for target_list in range(int(_CountBuy)):
                        IntCurHealth += 500
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
                    BuyItem = _BuyItem(35,Gold,CurCountBuyItem)
                    _CountBuy = BuyItem[0]
                    str1 = BuyItem[1]
                    _Gold_ = BuyItem[2]
                    Gold = _Gold_
                    for target_list in range(int(_CountBuy)):
                        IntMaxDamage += random.randint(5,35)
                        if target_list < 0:
                            print("ERROR")
                    await message.channel.send(str1)
                else:
                    await message.channel.send("Количеств не указано",delete_after=2)
            #Конец
            #Начало
            elif CurBuyItem == "ЗДОРОВЬЕ":
                if CurCountBuyItem != "":
                    BuyItem = _BuyItem(8,Gold,CurCountBuyItem)
                    _CountBuy = BuyItem[0]
                    str1 = BuyItem[1]
                    _Gold_ = BuyItem[2]
                    Gold = _Gold_
                    for target_list in range(int(_CountBuy)):
                        IntMaxHealth += random.randint(50,80)
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
                    BuyItem = _BuyItem(25,Gold,CurCountBuyItem)
                    _CountBuy = BuyItem[0]
                    str1 = BuyItem[1]
                    _Gold_ = BuyItem[2]
                    Gold = _Gold_
                    for target_list in range(int(_CountBuy)):
                        IntCurExp += random.randint(1000,2000)
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
                        if target_list < 0:
                            print("ERROR")
                    await message.channel.send(str1)
                else:
                    await message.channel.send("Количеств не указано",delete_after=2)
            #Конец
            #Начало
            elif CurBuyItem == "УРОВЕНЬ":
                if CurCountBuyItem != "":
                    BuyItem = _BuyItem(50,Gold,CurCountBuyItem)
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
                        if target_list < 0:
                            print("ERROR")
                    await message.channel.send(str1)
                else:
                    await message.channel.send("Количеств не указано",delete_after=2)
            #Конец
            else:
                await message.channel.send("Такого предмета нет",delete_after=2)

        Functions.WriteMainParametrs(username=UserName_,exp=IntCurExp,lvl=IntCurLvl,maxHealth=IntMaxHealth,curHealth=IntCurHealth,damage=IntMaxDamage,money=Gold,messages=Msages)
    async def on_message(self, message):
    # don't respond to ourselves
        Dialog = asyncio.create_task(self.Dialog(message))
        botEvent = asyncio.create_task(self.botEvent(message))
        botStandart = asyncio.create_task(self.botStandart(message))
        botShop = asyncio.create_task(self.botShop(message))
        asyncio.gather(Dialog,botEvent,botStandart,botShop)


    async def on_voice_state_update(self,_Player_ : discord.member.Member, before : discord.member.VoiceState, after : discord.member.VoiceState):
        #msg = self.get_channel(627140104988917789)
        _Gabriel = Functions.Gabriel()
        Confige = _Gabriel.Config()
        await Confige.Start(_Player_.guild.id,self)
        Modules = Confige.Read()

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
        MembersBefore = after.members
        for member in MembersBefore:
            permiss = after.permissions_for(member)
            if permiss.manage_channels == True:
                Room = Functions.Room(member.name)
                Room.Save(after.name)

    async def on_member_join(self,member : discord.member.Member):
        try:
            OurServer = await self.fetch_guild(419879599363850251)
            StartRole = OurServer.get_role(691735620346970123)
            await member.add_roles(StartRole,reason="Впервые зашел на сервер")
        except: pass

InternetActive()

while True:
    time.sleep(1)
    if is_internet():
        if(internetWasOff == True):
            print("Internet is active")
            InternetActive()
            internetWasOff = False
    else:
        print("Internet disconnected")
        internetWasOff = True