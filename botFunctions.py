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
            pass
        async def Start(self,server : int,Client : discord.Client()):
            self.Client = Client
            self.server = await Client.fetch_guild(server)
            print(self.server)
            await self.CreateNewBank()
        # async def SaveConfig(self):
        #     with open(f"{self.server}")
        async def CreateNewBank(self):
            direct = f"./Servers/{self.server.name}"
            os.mkdir(direct)
    class TooManyWords(Error):
        def Error(self):
            return "Слишком мало слов я знаю"
    def Message(self,CountMessages : int):
        Lines = []
        with open(f"./Resurses/Words.txt","r") as file:
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
        with open(f"./Stats/Main/{_UserName_}.txt","r") as file:
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
                with open(f"{Resurses}{_UserName_}.png", "wb") as fileTwo:
                    fileTwo.write(logo)
            except Exception:
                pass
    else:
        with open(f"./Stats/Profile/BackGround_{_UserName_}.txt","w") as file:
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
            with open(f"./Stats/Main/{_UserName_}.txt","r") as file:
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
def WriteInventor(**objects):
    """
    Записать в инвентарь.

    `------------------- Обязательные -----------------`

    `username` : ник игрока, чей инвентарь мы изменяем 
    
    `old` : изначальный инвентарь

    `type` : тип предмета

    `Типы предметов` :  `Предмет`  ,  `Оружие`  ,  `Экипировка`  ,  `Ингридиент`

    `name` : имя предмета

    `classItem` : Класс предмета

    `Классы` : Сломанный -> Первоначальный -> Обычный -> Редкий -> Эпический -> Легендарный -> Мифический -> Демонический = Божественный -> Уникальный

    `ID` : это персональный номер у предмета, к которому нужно будет отссылаться, дабы взаимодействовать с ним

    `gold` : Количество золотых, которые нужно потратить, для улучшения предмета

    `------------------- Для предметов ----------------`

    `duration` : длительность эффекта

    `------------------- Для оружия -------------------`

    `armor` : прочность оружия

    `damage` : Урон от оружия

    `------------------- Для экиперовки ---------------`

    `armor` : прочность брони

    `protect` : Уровень защиты
    
    `------------------- Для ингридиентов -------------`

    `count` : количество ингридиентов

    """

    try:
        username = str(objects.pop('username'))
    except: raise Error_CreateItem("username error")


    try:
        old = objects.pop('old')
    except: raise Error_CreateItem("old error")


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

    newItem = {}
    if type_ == "Предмет":
        newItem = {
            "type" : type_,
            "name" : name,
            "classItem" : classItem,
            "ID" : ID,
            "duration" : duration,
            "gold" : gold
        }
    if type_ == "Оружие":
        newItem = {
            "type" : type_,
            "name" : name,
            "classItem" : classItem,
            "ID" : ID,
            "gold" : gold,
            "armor" : armor,
            "damage" : damage
        }
    if type_ == "Экипировка":
        newItem = {
            "type" : type_,
            "name" : name,
            "classItem" : classItem,
            "ID" : ID,
            "gold" : gold,
            "armor" : armor,
            "protect" : protect
        }
    if type_ == "Ингридиент":
        newItem = {
            "type" : type_,
            "name" : name,
            "classItem" : classItem,
            "ID" : ID,
            "gold" : gold,
            "count" : count
        }
    with open(f"./Stats/Inventory/Inventor_{username}.txt","w") as file:
        if str(old) != "":
            file.write(f"{str(old)}\n{str(newItem)}")
        else:
            file.write(f"{str(newItem)}")
    pass
def ReadInventor(_UserName_ : str):
    '''
    Читает инвентарь
    '''
    Inventor = ""
    with open(f"./Stats/Inventory/Inventor_{_UserName_}.txt","r") as file:
        for line in file.readlines():
            Inventor += line
        return Inventor
async def EditAttackDamageTwo(self,Channel : discord.channel.TextChannel,GetDamage : int,_Player : str,_Target : str,CurHealthTarget : int):
    today = datetime.datetime.today()
    try:
        with open(f"./Stats/GetDamageForTime/{_Player}.txt","r") as file:
            Message = int(file.readline())
            Message = await Channel.fetch_message(Message)
            Date = str(file.readline()) ; Date = Date.split("-")
            SumarDamage = int(file.readline())
        SumarDamage += GetDamage
        if int(Date[4]) != today.minute:
            _Message = await Channel.send(content=f"{_Player} нанёс : {GetDamage} ед.\nСумарный урон : {SumarDamage} ед.\nЗдоровье у {_Target} : {CurHealthTarget} ед.")
        else:
            await Message.edit(content=f"{_Player} нанёс : {GetDamage} ед.\nСумарный урон : {SumarDamage} ед.\nЗдоровье у {_Target} : {CurHealthTarget} ед.")
        with open(f"./Stats/GetDamageForTime/{_Player}.txt","w") as file:
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
        with open(f"./Stats/GetDamageForTime/{_Player}.txt","w") as file:
            _Message = await Channel.send(content=f"{_Player} нанёс : {GetDamage} ед.\nСумарный урон : {GetDamage} ед.\nЗдоровье у {_Target} : {CurHealthTarget} ед.")
            writeToday = "%Y-%m-%d-%H-%M-%S"
            file.writelines(f"{_Message.id}")
            file.writelines(f"\n{str(today.strftime(writeToday))}")
            file.writelines(f"\n0")
    

    pass


def CreateNewBoss():
    with open(f"./Stats/EventBoss.txt","w") as file:
        today = datetime.datetime.today()
        MaxHealth = random.randint(50000,100000000)
        CurHealth = MaxHealth
        GetGold = 0
        for ran in range(int(MaxHealth / 1000000)):
            if ran < 0: print("ERROR")
            GetGold += random.randint(300,550)
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
    with open(f"./Stats/EventBoss.txt","r") as file:
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

    with open(f"./Stats/EventBoss.txt","w") as file:
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

def ReadWords(**fields):
    AllWords = str()
    with open(f"./Resurses/Words.txt","r") as file:
        try:
            for line in file.readlines():
                AllWords += line
        except:
            pass
    return AllWords


def SaveWords(msg : str):
    Oldmsg = ReadWords()
    with open(f"./Resurses/Words.txt","w") as file:
        msgSplitLines = msg.split("\n")
        file.write(f"{Oldmsg}")
        for line in msgSplitLines:
            file.writelines(f"\n{line}")


def ClearWords(**fields):
    with open(f"./Resurses/Words.txt","w") as file:
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
        with open(f"./Stats/Inventory/{username}.txt","r") as file:
            Inventor = file.readline()
            Inventor = StrToDict(str=Inventor)
            ArmorId = int(Inventor["Armor"])
            AttackId = int(Inventor["Attack"])
    except FileNotFoundError:
        with open(f"./Stats/Inventory/{username}.txt","w") as file:
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
    with open(f"./Stats/Inventory/{username}.txt","w") as file:
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

    with open(f"./Stats/Inventory/{username}.txt","r") as file:
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

    with open(f"./Stats/Inventory/Inventor_{username}.txt","r") as file:
        for item in file.readlines():
            itemDict = StrToDict(str=item)
            itemID = int(itemDict['ID'])
            if ID == itemID:
                return itemDict


def EditItem(**fields):
    """
    Редактирует предмет

    `username` : Имя игрока

    `ID` : Индекс предмета

    `type` : тип `Оружие` , `Экипировка`

    `armor` : Броня у предмета

    `protect` : защита

    `damage` : урон

    `classItem` : Сломанный -> Первоначальный -> Обычный -> Редкий -> Эпический -> Легендарный -> Мифический -> Демонический = Божественный -> Уникальный

    `gold` : Количество золотых, на улучшение предмета

    """

    username = fields.pop('username')
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
    
    ListItems = list()
    with open(f"./Stats/Inventory/Inventor_{username}.txt","r") as file:
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
                        "damage" : damage
                    }
                if type_ == "Экипировка":
                    newItem = {
                        "type" : type_item,
                        "name" : nameItem,
                        "classItem" : classItem,
                        "ID" : itemID,
                        "gold" : gold,
                        "armor" : armor,
                        "protect" : protect
                    }
                ListItems.append(newItem)
            else:
                ListItems.append(itemDictStandart)
    with open(f"./Stats/Inventory/Inventor_{username}.txt","w") as file:
        Counts = len(ListItems)
        for ItemIn in ListItems:
            Counts -= 1
            if Counts != 0:
                file.writelines(f"{ItemIn}\n")
            else:
                file.writelines(f"{ItemIn}")
        pass
    pass

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

    `Первоначальный` = от `100` до `500`

    `Обычный` = от `350` до `1.000`

    `Редкий` = от `850` до `3.000`

    `Эпический` = от `2.800` до `8.000`

    `Легендарный` = от `10.000` до `325.000`

    `Мифический` = от `100` до `6.352.500`

    `Демонический` = от `60.000.000` до `100.000.000`

    `Божественный` = от `60.350.000` до `100.650.000`

    `------------------- ОРУЖИЕ -------------------`
    
    `----------------- ЭКИПИРОВКА -----------------`

    `Первоначальный` = от `5` до `425`

    `Обычный` = от `425` до `800`

    `Редкий` = от `750` до `2.500`

    `Эпический` = от `2.255` до `7.000`

    `Легендарный` = от `9.000` до `320.000`

    `Мифический` = от `100` до `55.000.000`

    `Демонический` = от `60.000.000` до `85.000.000`

    `Божественный` = от `60.000.000` до `75.000.000`

    `----------------- ЭКИПИРОВКА -----------------`

    `----------------- СТОИМОСТЬ ------------------`
    
    `Первоначальный` = от `5` до `25`

    `Обычный` = от `1.110` до `1.350`

    `Редкий` = от `2.000` до `2.800`

    `Эпический` = от `5.000` до `10.000`

    `Легендарный` = от `100.000` до `125.000`

    `Мифический` = от `125.000` до `1.325.000`

    `Демонический` = от `15.000.000` до `35.000.000`

    `Божественный` = от `15.350.000` до `35.650.000`

    `----------------- СТОИМОСТЬ ------------------`

    `----------------- ПРОЧНОСТЬ ------------------`

    `----------------- ПРОЧНОСТЬ ------------------`

    """

    type_ = fields.pop("type")

    classItem = fields.pop("classItem")

    if type_ == "Оружие":
        Damage = 0
        Gold = 0
        Armored = 0
        if classItem == "Первоначальный":
            Damage = random.randint(100,500)
            Gold = random.randint(5,25)
            Armored = random.randint(100,200)

        if classItem == "Обычный":
            Damage = random.randint(350,1000)
            Gold = random.randint(1100,1350)
            Armored = random.randint(150,300)

        if classItem == "Редкий":
            Damage = random.randint(850,3000)
            Gold = random.randint(2000,2800)
            Armored = random.randint(250,450)

        if classItem == "Эпический":
            Damage = random.randint(2800,8000)
            Gold = random.randint(5000,10000)
            Armored = random.randint(600,1000)

        if (classItem == "Легендарный") or (classItem == "Ћегендарный"):
            Damage = random.randint(10000,325000)
            Gold = random.randint(100000,125000)
            Armored = random.randint(32000,100000)

        if classItem == "Мифический":
            Damage = random.randint(100,6352500)
            Gold = random.randint(125000,1325000)
            Armored = random.randint(100,10000000)

        if classItem == "Демонический":
            Damage = random.randint(60000000,100000000)
            Gold = random.randint(15000000,32000000)
            Armored = 100000000

        if classItem == "Божественный":
            Damage = random.randint(60350000,100650000)
            Gold = random.randint(15350000,35650000)
            Armored = 100000000


        NewInfo = {
            "damage" : Damage,
            "gold" : Gold,
            "armor" : Armored
        }

        return NewInfo
    if type_ == "Экипировка":
        Armor = 0
        Gold = 0
        Armored = 0

        if classItem == "Первоначальный":
            Armor = random.randint(5,425)
            Gold = random.randint(5,25)
            Armored = random.randint(100,200)

        if classItem == "Обычный":
            Armor = random.randint(425,800)
            Gold = random.randint(1100,1350)
            Armored = random.randint(150,300)

        if classItem == "Редкий":
            Armor = random.randint(750,2500)
            Gold = random.randint(2000,2800)
            Armored = random.randint(250,450)

        if classItem == "Эпический":
            Armor = random.randint(2255,7000)
            Gold = random.randint(5000,10000)
            Armored = random.randint(600,1000)

        if classItem == "Легендарный":
            Armor = random.randint(9000,320000)
            Gold = random.randint(100000,125000)
            Armored = random.randint(32000,100000)

        if classItem == "Мифический":
            Armor = random.randint(100,55000000)
            Gold = random.randint(125000,1325000)
            Armored = random.randint(100,10000000)

        if classItem == "Демонический":
            Armor = random.randint(60000000,85000000)
            Gold = random.randint(15000000,32000000)
            Armored = 100000000

        if classItem == "Божественный":
            Armor = random.randint(60000000,75000000)
            Gold = random.randint(15350000,35650000)
            Armored = 100000000

        NewInfo = {
            "protect" : Armor,
            "gold" : Gold,
            "armor" : Armored
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
        with open(f"./Stats/Main/{username}.txt","r") as file:
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


    with open(f"./Stats/Main/{username}.txt","w") as file:
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
        typeItem = fields.pop("typeItem")
    except: raise Error("Не указан typeItem")
    try:
        name = fields.pop("name")
    except: raise Error("Не указан name")
    try:
        classItem = fields.pop("classItem")
    except: raise Error("Не указан classItem")
    try:
        ID = fields.pop("ID")
    except: raise Error("Не указан ID")
    try:
        gold = fields.pop("gold")
    except: raise Error("Не указан gold")
    try:
        protect = 0
        if typeItem == "Экипировка":
            protect = fields.pop("protect")
    except: raise Error("Не указан protect")
    try:
        armor = 0
        if (typeItem == "Экипировка") or (typeItem == "Оружие"):
            armor = fields.pop("armor")
    except: raise Error("Не указан armor")
    try:
        damage = 0
        if typeItem == "Оружие":
            damage = fields.pop("damage")
    except: raise Error("Не указан damage")
    try:
        username = fields.pop("username")
    except: raise Error("Не указан username")
    PATH = "./Resurses/Inventor/"
    #130 30
    ItemPath = f"{PATH}Item.png"
    SaveImage = f"{PATH}ItemEdit.png"
    Avatar = f"./Resurses/{username}.webp"
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

    area = (1925,1846)
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
    if (str(typeItem) == "Экипировка"):
        area = (230,1300)
        Color = (0,0,0)
        font = ImageFont.truetype("arial.ttf",Scaling)
        txt = f"Защита : {protect}"
        DrawItem.text(area,txt,font=font,fill=Color)

        area = (1272,784)
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

    area = (943,160)
    Color = (0,0,0)
    font = ImageFont.truetype("arial.ttf",Scaling)
    txt = f"ID : {ID}"
    DrawItem.text(area,txt,font=font,fill=Color)

    area = (79,59)
    ImageAvatar = ImageAvatar.resize((616,616))
    ItemImage.paste(ImageAvatar,area)


    #Щит
    area = (1272,1027)
    CurImage = Item_Armor.resize((167,167))
    ItemImage.paste(CurImage.convert('RGB'), area, CurImage)


    #Меч
    area = (1272,1265)
    CurImage = Item_Sword.resize((167,167))
    ItemImage.paste(CurImage.convert('RGB'), area, CurImage)



    ItemImage.save(f"{SaveImage}")
    df = discord.File(f"{SaveImage}",f"{SaveImage}")
    return df

def SellItem(**fields):
    """
    Продает предмет

    `username` : Имя игрока

    `ID` : Индекс предмета

    `Сломанный` : с 1 до 15 золотых

    `Первоначальный` : с 5 до 15 золотых

    `Обычный` : с 500 до 700 золотых

    `Редкий` : с 1000 до 1111 золотых

    `Эпический` : с 2000 до 3000 золотых

    `Легендарный` : с 6000 до 10000 золотых

    `Мифический` : с 500 до 100000 золотых

    `Божественный` : с 100000 до 130000 золотых

    `Демонический` : с 59999 до 200000 золотых

    """
    username = str(fields.pop("username"))
    ID = int(fields.pop("ID"))
    Inventor = ReadInventor(username)

    Inventor = Inventor.split("\n")

    NewInventor = list()

    CountItems = len(Inventor)

    for Item in Inventor:
        ItemDict = StrToDict(str=Item)
        ItemID = int(ItemDict.pop("ID"))
        if ItemID == ID:
            if CountItems > 1:
                ClassItem = ItemDict.pop("classItem")

                if ClassItem == "Сломанный":
                    SellMoney = random.randint(1,15)
                    _Gold(username=username,do="Добавить",count=SellMoney)
                elif ClassItem == "Первоначальный":
                    SellMoney = random.randint(5,15)
                    _Gold(username=username,do="Добавить",count=SellMoney)
                elif ClassItem == "Обычный":
                    SellMoney = random.randint(500,700)
                    _Gold(username=username,do="Добавить",count=SellMoney)
                elif ClassItem == "Редкий":
                    SellMoney = random.randint(1000,1111)
                    _Gold(username=username,do="Добавить",count=SellMoney)
                elif ClassItem == "Эпический":
                    SellMoney = random.randint(2000,3000)
                    _Gold(username=username,do="Добавить",count=SellMoney)
                elif ClassItem == "Легендарный":
                    SellMoney = random.randint(6000,10000)
                    _Gold(username=username,do="Добавить",count=SellMoney)
                elif ClassItem == "Мифический":
                    SellMoney = random.randint(500,100000)
                    _Gold(username=username,do="Добавить",count=SellMoney)
                elif ClassItem == "Божественный":
                    SellMoney = random.randint(100000,130000)
                    _Gold(username=username,do="Добавить",count=SellMoney)
                elif ClassItem == "Демонический":
                    SellMoney = random.randint(59999,200000)
                    _Gold(username=username,do="Добавить",count=SellMoney)       
            else:
                raise LastItem("Последний предмет")
        else:
            NewInventor.append(Item)
        pass

    with open(f"./Stats/Inventory/Inventor_{username}.txt","w") as file:
        Counts = len(NewInventor)
        for Item in NewInventor:
            Counts -= 1
            if Counts != 0:
                file.writelines(f"{Item}\n")
            else:
                file.writelines(f"{Item}")

    return SellMoney
class NotEnoughGold(Error):
    pass
class Auction():
    """
    Торги

    `ReadAuction` : Прочитать все торги

    `AddAuction` : Создать новые торги

    `RemoveAuction` : Удалить торг

    """

    @staticmethod
    def ReadAuction(**fields):
        """
        Прочитать все торги
        """
        Items = ""
        with open(f"./Stats/Auction.txt","r") as file:
            for line in file.readlines():
                if (line != "") and (line != "\n"):
                    Items += f"{line}"
        return Items
    
    @staticmethod
    def AddAuction(**fields):
        """
        Создать новые торги

        `username` : Имя игрока, кто создает торг

        `ID` : Индекс предмета

        `goldAuction` : Ставка, на торг

        """
        
        username = fields.pop("username")
        ID = fields.pop("ID")
        goldAuction = fields.pop("goldAuction")

        OldAuction = Auction.ReadAuction()

        OldAuction = str(OldAuction).split("\n")

        Inventor = ReadInventor(username)

        Inventor = str(Inventor).split("\n")

        NewAuction = {
            "username" : username,
            "ID" : ID,
            "goldAuction" : goldAuction,
            "AuctionID" : random.randint(0,999999999)
        }

        NewAuction = str(NewAuction)

        Words = list();Words.extend(NewAuction)
        NewAuction_ = str()
        for Word in Words:
            if Word != "}":
                NewAuction_ += Word
            else:
                NewAuction_ += ","
        

        for item in Inventor:
            itemDict = StrToDict(str=item)
            ItemID = itemDict.pop("ID")
            if ItemID == ID:
                Words = list() ; Words.extend(str(itemDict))
                for word in Words:
                    if word != "{":
                        NewAuction_ += word
                NewAuction = StrToDict(str=NewAuction_)
                try:
                    try:
                        SellItem(username=username,ID=ID)
                    except: 
                        print("Этого предмета нет")
                        return
                except LastItem: 
                    print("Последний предмет")
                    return

                with open(f"./Stats/Auction.txt","w") as file:
                    for Auctions in OldAuction:
                        file.writelines(f"{str(Auctions)}\n")
                    file.writelines(f"{str(NewAuction)}")
                pass
        
    
    @staticmethod
    def RemoveAuction(**fields):
        """
        Удалить торг

        `username` : Имя игрока

        `gold` : Ставка за торг

        `AuctionID` : Индекс торга

        """

        username = str(fields.pop("username"))

        gold = int(fields.pop("gold"))

        AuctionID = fields.pop("AuctionID")

        OldAuction = Auction.ReadAuction()

        OldAuction = str(OldAuction).split("\n")
        
        with open(f"./Stats/Auction.txt","w") as file:
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
                        _AuctionsItemType = str(_AuctionsDict.pop("type"))
                        _AuctionsItemName = str(_AuctionsDict.pop("name"))
                        _AuctionsItemClassItem = (_AuctionsDict.pop("classItem"))
                        _AuctionsItemID = int(_AuctionsDict.pop("ID"))
                        _AuctionsItemGold = int(_AuctionsDict.pop("gold"))
                        _AuctionsOwner = str(_AuctionsDict.pop("username"))
                        _Gold(username=username,do="Убавить",count=gold)
                        _Gold(username=_AuctionsOwner,do="Добавить",count=gold)
                        if _AuctionsItemType == "Оружие":
                            Inventor = ReadInventor(username)
                            AuctionsItemArmor = int(_AuctionsDict.pop("armor"))
                            AuctionsItemDamage = int(_AuctionsDict.pop("damage"))
                            WriteInventor(username=username,old=Inventor,type=_AuctionsItemType
                            ,name=_AuctionsItemName,classItem=_AuctionsItemClassItem,ID=_AuctionsItemID,
                            gold=_AuctionsItemGold,armor=AuctionsItemArmor,damage=AuctionsItemDamage)
                        if _AuctionsItemType == "Экипировка":
                            Inventor = ReadInventor(username)
                            AuctionsItemArmor = int(_AuctionsDict.pop("armor"))
                            AuctionsItemProtect = int(_AuctionsDict.pop("protect"))
                            WriteInventor(username=username,old=Inventor,type=_AuctionsItemType
                            ,name=_AuctionsItemName,classItem=_AuctionsItemClassItem,ID=_AuctionsItemID,
                            gold=_AuctionsItemGold,armor=AuctionsItemArmor,protect=AuctionsItemProtect)
                except SyntaxError: pass
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
            with open(f"{self.path}{self.username}.txt","r") as file:
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
        with open(f"{self.path}{self.username}.txt","w") as file:
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
        with open(f"./Stats/Room/{self.Player}.txt","w") as file:
            file.write(str(RoomName))
    def Read(self):
        """
        Читает название комнаты
        """
        try:
            with open(f"./Stats/Room/{self.Player}.txt","r") as file:
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





if __name__ == "__main__":
    # description = "Проверка описания к заданию"
    # main_task = "Стать аниме-девочкой"
    # tag = QuestTags.main()
    # NewQuest = Quest(username="KOT32500",NPC="Gabriele",
    # description=description,main_task=main_task,tag=tag)
    # NewQuest.Add()
    pass
    