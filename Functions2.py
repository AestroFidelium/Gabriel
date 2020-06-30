"""
Функции для Габриэль
Содержат всю логику
Нужны для того чтобы не загружать основной код
Тут нет порядка написания фукнции, то есть может быть все налепленно
Все фукнции храняться здесь
"""
from PIL import Image, ImageDraw , ImageFont
import os
import codecs
import random
from myConfg import * 

class Error(BaseException):
    pass


class C_Player():
    def __init__(self,Name):
        self.PATH_VERSION = "./Version 6"
        self.Name = Name
        self.StartStats = {
            "Main" : {
                    "Health" : 35,
                    "MaxHealth" : 35,
                    "Exp" : 0,
                    "Level" : 1,
                    "Damage" : 5,
                    "Description" : None,
                    "Gold" : 0,
                    "Messages" : 1,
                    "MaxLevel" : 1,
                    "Strength" : 1.0,
                    "Agility" : 1.0,
                    "Intelligence" : 1.0,
                    "Plus" : 0,
                    "Class" : None
                },
            "Room" : self.Name,
            "Everyday bonus" : {
                    "Time" : None,
                    "Gold" : None
                }
        }
        try:
            with codecs.open(f"{self.PATH_VERSION}/Stats/{self.Name}.txt","r",encoding="utf-8") as file:
                self.Stats = StrToDict(file.readline())
        except FileNotFoundError:
            with codecs.open(f"{self.PATH_VERSION}/Stats/{self.Name}.txt","w",encoding="utf-8") as file:
                file.write(str(self.StartStats))
                self.Stats = self.StartStats
        self._selfStats()
    def _selfStats(self):
        self.Stats_main = self.Stats["Main"]
        self.Stats_Room = self.Stats["Room"]
        self.Stats_Everydaybonus = self.Stats["Everyday bonus"]

        self.Health = int(self.Stats_main["Health"])
        self.MaxHealth = int(self.Stats_main["MaxHealth"])
        self.Exp = int(self.Stats_main["Exp"])
        self.Level = int(self.Stats_main["Level"])
        self.Damage = int(self.Stats_main["Damage"])
        self.Description = str(self.Stats_main["Description"])
        self.Gold = int(self.Stats_main["Gold"])
        self.Messages = int(self.Stats_main["Messages"])
        self.MaxLevel = int(self.Stats_main["MaxLevel"])
        self.Strength = float(self.Stats_main["Strength"])
        self.Agility = float(self.Stats_main["Agility"])
        self.Intelligence = float(self.Stats_main["Intelligence"])
        self.Plus = int(self.Stats_main["Plus"])
        self.Class = str(self.Stats_main["Class"])

    def Edit(self,**fields):
        Edit = str(fields.pop("Edit"))
        
        EditStats = self.Stats[Edit]
        EditStats.update(fields)

        self.Stats.update(EditStats)
        
        with codecs.open(f"{self.PATH_VERSION}/Stats/{self.Name}.txt","w",encoding="utf-8") as file:
            file.write(str(self.Stats))
        
        self._selfStats()
    
    class mode():
        class ErrorNoClass(Error): pass
        class one(): pass
        class multiply(): 
            class ErrorNoCount(Error): pass
    
    def LevelUp(self,**mode):
        """
        Моды : (mode)
            mode.one : 
                Один уровень

            mode.multiply :
                Множество уровней
                требуется : count 
        """
        count = 1
        try:
            Mode = mode['mode']
        except ValueError: 
            raise self.mode.ErrorNoClass("Требуется указать модификацию")
        if Mode == self.mode.multiply:
            try:
                count = int(mode["count"])
            except KeyError: 
                raise self.mode.multiply.ErrorNoCount("Требуется указать count")
        
        self.Health += random.randint(55,100) * count
        self.MaxHealth += random.randint(55,100) * count
        if self.Health > self.MaxHealth:
            self.Health = self.MaxHealth
        self.Damage += random.randint(8,35) * count
        self.Level += 1 * count
        self.Exp = 0
        if self.Level > self.MaxLevel:
            self.Plus += self.Level - self.MaxLevel
            self.MaxLevel = self.Level
        self.Strength += random.random() / 10
        self.Agility += random.random() / 9
        self.Intelligence += random.random() / 6
        self.Edit(
            Edit="Main",
            Health = self.Health,
            MaxHealth = self.MaxHealth,
            Damage = self.Damage,
            Level = self.Level,
            Exp = self.Exp,
            Plus = self.Plus,
            Strength = self.Strength,
            Agility = self.Agility,
            Intelligence = self.Intelligence
        )
    def _writeInPicture(self,area,content,font,draw,color):
        draw.text(area,content,font=font,fill=color)
    def Profile(self):
        BackGroud = Image(f"./Resurses/BackGround_{self.Name}.png")
        Main = Image(f"./Resurses/Main.png")
        Ava = Image.open(f"./Resurses/{self.Name}.png")
        Ava.resize((264,264))
        draw = ImageDraw.Draw(Main)
        Main.save("StatsPl.png")
        df = discord.File("StatsPl.png","StatsPl.png")
        return df

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









if __name__ == "__main__":
    pass