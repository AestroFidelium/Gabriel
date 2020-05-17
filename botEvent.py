import discord
import BazaDate
from discord import user
from discord import voice_client
import urllib
from urllib.request import urlopen
import time
import random
import datetime
import os
import wget
from PIL import Image, ImageDraw , ImageFont
import botFunctions as Functions
from botFunctions import Gabriel

MiniGameID = 629267102070472714 


internetWasOff = True
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

def is_internet():
    """
    Query internet using python
    :return:
    """
    
    try:
        urlopen('https://www.google.com', timeout=1)
        
        return True
    except urllib.error.URLError as Error:
        print(Error)
        return False
def InternetActive():
    client = MyClient()
    client.run(BazaDate.token)
class MyClient(discord.Client):
    async def on_ready(self):
        print(f"Logged on as , {self.user} MODULE : botEvent.py")
        # Functions.CreateNewBoss()
    # async def on_member_join(self,member):
    #     print("DA")
    #     print(self)
    #     print(member)
    async def on_message(self, message):
        MiniGame = self.get_channel(MiniGameID)
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

    async def on_voice_state_update(self,_Player_ : discord.member.Member, before : discord.member.VoiceState, after : discord.member.VoiceState):
        #msg = self.get_channel(627140104988917789)
        _Gabriel = Gabriel()
        Confige = _Gabriel.Config()
        await Confige.Start(_Player_.guild.id,self)
        Modules = Confige.Read()

        print(Modules)
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