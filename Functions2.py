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
import discord
import datetime

class Error(BaseException):
    pass


def ReplaceNumber(Number):
    """
    Показывает цифры более компактно
    
    Пример : 
        100 000 = 100К
        312 434 = 312К
        1 232 542 = 1М
        1 231 123 153 = 1B
        1 300 000 000 000 = 1T
        ----------------------
        -100 000 = -100К
        -312 434 = -312К
        -1 232 542 = -1М
        -1 231 123 153 = -1B
        -1 300 000 000 000 = -1T
    """
    Minus = False
    if Number < 0:
        Minus = True
        Number *= -1
    if Number >= 1000000000000:
        NumberSplit = Number / 1000000000000
        Number = int(NumberSplit)
        if Minus == True:
            Number = f"-{Number}T"
        else:
            Number = f"{Number}T"
    elif Number >= 1000000000:
        NumberSplit = Number / 1000000000
        Number = int(NumberSplit)
        if Minus == True:
            Number = f"-{Number}B"
        else:
            Number = f"{Number}B"
    elif Number >= 1000000:
        NumberSplit = Number / 1000000
        Number = int(NumberSplit)
        if Minus == True:
            Number = f"-{Number}M"
        else:
            Number = f"{Number}M"
    elif Number >= 10000:
        NumberSplit = Number / 1000
        Number = int(NumberSplit)
        if Minus == True:
            Number = f"-{Number}K"
        else:
            Number = f"{Number}K"
    return Number


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
                },
            "Inventor" : [],
            "Equipped" : {
                "Head" : None,
                "Body" : None,
                "Legs" : None,
                "Boot" : None,
                "Left hand" : None,
                "Right hand" : None,
                "Ring 1" : None,
                "Ring 2" : None,
                "Ring 3" : None,
                "Ring 4" : None,
                "Ring 5" : None,
                },
            "Quests" : [],
            "Talants" : [],
            "Effects" : []
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
        """
        Edit = "Main" , "Room" , "Everyday bonus"
        """
        Edit = str(fields.pop("Edit"))
        
        EditStats = self.Stats[Edit]
        EditStats.update(fields)

        # self.Stats.update(EditStats)
        
        with codecs.open(f"{self.PATH_VERSION}/Stats/{self.Name}.txt","w",encoding="utf-8") as file:
            file.write(str(self.Stats))
        
        self._selfStats()
    
    class mode():
        class one(): pass
        class multiply(): 
            class ErrorNoCount(Error): pass
    
    def LevelUp(self,mode,**fields):
        """
        Моды : (mode)
            mode.one : 
                Один уровень

            mode.multiply :
                Множество уровней
                требуется : count 
        """
        count = 1

        if mode == self.mode.multiply:
            try:
                count = int(fields["count"])
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
        self.Strength += (random.random() / 10) * count
        self.Agility += (random.random() / 9) * count
        self.Intelligence += (random.random() / 6) * count
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
    def LostLevel(self,count):
        lostHealth = random.randint(55,100) * count
        self.Health -= lostHealth
        self.MaxHealth -= lostHealth
        if self.Health <= 0:
            self.Health = 35
        if self.MaxHealth <= 0:
            self.MaxHealth = 35
        lostDamage = random.randint(8,35) * count
        self.Damage -= lostDamage
        if self.Damage <= 0:
            self.Damage = 5
        
        lostLevel = 1 * count
        self.Level -=lostLevel
        if self.Level <= 0:
            self.Level = 0

        self.Exp = 0

        lostStrength = (random.random() / 10) * count
        self.Strength -= lostStrength
        if self.Strength < 1.0:
            self.Strength = 1.0
        
        lostAgility = (random.random() / 9) * count
        self.Agility -= lostAgility
        if self.Agility < 1.0:
            self.Agility = 1.0

        lostIntelligence = (random.random() / 6) * count
        self.Intelligence -= lostIntelligence
        if self.Intelligence < 1.0:
            self.Intelligence = 1.0
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
        LostStatus = {
            "Status" : "Dead",
            "Level" : lostLevel - self.Level,
            "Damage" : lostDamage - self.Damage,
            "Health" : lostHealth - self.Health,
            "Agility" : lostAgility - self.Agility,
            "Intelligence" : lostIntelligence - self.Intelligence,
            "Strength" : lostStrength - self.Strength
        }
        return LostStatus
    def Profile(self):
        try:
            BackGround = Image.open(f"./Resurses/BackGround_{self.Name}.png")
        except: BackGround = Image.open(f"./Resurses/BackGround_StandartBackGround.png")
        Main = Image.open(f"./Resurses/Main.png")
        Ava = Image.open(f"./Resurses/{self.Name}.png")
        Ava = Ava.resize((264,264))
        draw = ImageDraw.Draw(Main)
        
        font = ImageFont.truetype("arial.ttf",50)
        Level = ReplaceNumber(self.Level)
        self._writeInPicture((163,309),Level,font,draw,"black")

        font = ImageFont.truetype("arial.ttf",100)
        self._writeInPicture((370,155),self.Name,font,draw,(200,210,255))

        font = ImageFont.truetype("arial.ttf",35)
        Health = ReplaceNumber(self.Health)
        MaxHealth = ReplaceNumber(self.MaxHealth)
        self._writeInPicture((550,276),f"Здоровье : {Health} ед./ {MaxHealth}",font,draw,"black")

        font = ImageFont.truetype("arial.ttf",35)
        Damage = ReplaceNumber(self.Damage)
        self._writeInPicture((550,328),f"Урон : {Damage}",font,draw,"black")

        font = ImageFont.truetype("arial.ttf",35)
        LevelNeed = self.Level * 500
        LevelNeed = ReplaceNumber(LevelNeed)
        self._writeInPicture((380,743),f"Опыт : {self.Exp} / {LevelNeed}",font,draw,"black")

        font = ImageFont.truetype("arial.ttf",30)
        Plus = ReplaceNumber(self.Plus)
        self._writeInPicture((700,700),f"Талант очки : {Plus}",font,draw,"black")

        font = ImageFont.truetype("arial.ttf",50)
        Strength = round(self.Strength)
        Strength = ReplaceNumber(Strength)
        self._writeInPicture((38,393),f"Сила : \n{Strength}",font,draw,(255,100,0))

        font = ImageFont.truetype("arial.ttf",50)
        Agility = round(self.Agility)
        Agility = ReplaceNumber(Agility)
        self._writeInPicture((38,471),f"Ловкость : \n{Agility}",font,draw,(0,255,0))

        font = ImageFont.truetype("arial.ttf",50)
        Intelligence = round(self.Intelligence)
        Intelligence = ReplaceNumber(Intelligence)
        self._writeInPicture((38,570),f"Интеллект : \n{Intelligence}",font,draw,(0,255,255))

        font = ImageFont.truetype("arial.ttf",35)
        Gold = ReplaceNumber(self.Gold)
        self._writeInPicture((550,380),f"Золота : {Gold} / {self.Messages}",font,draw,"black")

        font = ImageFont.truetype("arial.ttf",60)
        self._writeInPicture((380,500),self.Description,font,draw,"black")

        font = ImageFont.truetype("arial.ttf",35)
        self._writeInPicture((380,470),"О себе : \n",font,draw,"black")

        Main.paste(Ava,(46,8))
        BackGround = BackGround.resize((1000,1450))
        BackGround.paste(Main.convert("RGB"),(0,550),Main)
        



        BackGround.save("StatsPl.png")
        df = discord.File("StatsPl.png","StatsPl.png")

        return df

    def Attack(self,Target):
        """Атаковать указанную цель"""
        GetDamage = random.randint(1,self.Damage)
        Target.Health -= GetDamage
        if Target.Health <= 0:
            Count = int(Target.Level / 5)
            LostStatus = Target.LostLevel(Count)
            self.LevelUp(self.mode.multiply,count=Count)
            LostStatus.update({"GetDamage":GetDamage})
            return LostStatus
        else:
            Target.Edit(
                Edit="Main",
                Health = Target.Health
                )
            AttackStatus = {
                "Status" : "Attack",
                "GetDamage" : GetDamage,
                "Health" : Target.Health
            }
            return AttackStatus


def _writeInPicture(area,content,font,draw,color):
    draw.text(area,str(content),font=font,fill=color)

class Boss():
    class Stady():
        class Easy(): 
            """
            Легкий босс
                Выпадает : 
                    Первоначальное снаряжение, которое отлично подойдет для старта игры
                Особенности : 
                    Не атакует. Не имеет брони.
                Время жизни : 1:00:00
            """
            pass
        class Medium(): 
            """
            Средний босс
                Выпадает : 
                    Среднее снаряжение, которое не тяжело выбить.
                Особенности : 
                    Атакует. Не имеет брони.
                Время жизни : 0:50:00
            """
            pass
        class Hard():
            """
            Сложный босс
                Выпадает : 
                    Одно из лучших снаряжений.
                    Можно выбить кольца.
                Особенности : 
                    Атакует. Имеет бронь.
                Время жизни : 0:40:00
            """ 
            pass
        class HardPlus():
            """
            Сложный босс++
            Выпадает :
                Предпоследний уровень снаряжений.
                Можно выбить кольца.
            Особенности : 
                Атакует. Имеет бронь.
                Имеет регенерацию в 5М за 10с.
            Время жизни : 0:30:00
            """
        class Relic():
            """
            Самый сложный босс
            Выпадает :
                Зачарованное оружие, или же реликвии.
                Можно выбить кольца.
                `Зачарованное оружие` : 
                    Оружие которое наносит сокрушительный урон.
                    А так же, имеет магические свойства.
                    Только оружие этого типа, можно зачаровать.
            Особенности : 
                Атакует. Имеет бронь.
                
                Имеет регенерацию в 500М за 1м.
                
                Каждый удар по боссу, уничтожает прочность предмета на 1%
                    Если прочность упадет ниже 0% предмет полностью пропадает.
                
                Оглушает на 5-10 секунд.
                
                Отражает 5% вашего урона по вам же. ( не может нанести больше 100 млн. )
                
                В случае если по боссу не идет урона в течении минуты
                он пропадает.
            Время жизни : 0:20:00
            """
            pass
    def __init__(self):
        self.PATH_VERSION = "./Version 6"
        self.Read()
        self._selfStats()
    def Create(self):
        Different = ["Easy","Medium","Hard","Hard+"]
        Different = Different[random.randint(0,len(Different) - 1)]
        with open(f"{self.PATH_VERSION}/Boss/Boss.txt","w") as file:
            BossImage = os.listdir(f"./Resurses/Bosses/{Different}/")
            BossImage = BossImage[random.randint(0,len(BossImage) - 1)]
            if Different == "Easy":
                MaxHealth = random.randint(80000,500000)
                self.Stats = {
                    "Different" : "Easy",
                    "Image" : BossImage,
                    "Health" : MaxHealth,
                    "MaxHealth" : MaxHealth,
                    "Damage" : 0,
                    "Armor" : 0,
                    "Time" : "1:00:00",
                    "Murder" : None,
                    "Status" : "Life"
                }
                file.write(str(self.Stats))
            elif Different == "Medium":
                MaxHealth = random.randint(5000000,8000000)
                self.Stats = {
                    "Different" : "Medium",
                    "Image" : BossImage,
                    "Health" : MaxHealth,
                    "MaxHealth" : MaxHealth,
                    "Damage" : random.randint(15000,50000),
                    "Armor" : 0,
                    "Time" : "0:50:00",
                    "Murder" : None,
                    "Status" : "Life"
                }
                file.write(str(self.Stats))
            elif Different == "Hard":
                MaxHealth = random.randint(80000000,999999999)
                self.Stats = {
                    "Different" : "Hard",
                    "Image" : BossImage,
                    "Health" : MaxHealth,
                    "MaxHealth" : MaxHealth,
                    "Damage" : random.randint(4000000,57000000),
                    "Armor" : random.randint(900000,2900000),
                    "Time" : "0:40:00",
                    "Murder" : None,
                    "Status" : "Life"
                }
            elif Different == "Hard+":
                MaxHealth = random.randint(9999999999,9999999999999)
                self.Stats = {
                    "Different" : "Hard+",
                    "Image" : BossImage,
                    "Health" : MaxHealth,
                    "MaxHealth" : MaxHealth,
                    "Damage" : random.randint(5700000000,57000000000),
                    "Armor" : random.randint(90000000,290000000),
                    "Time" : "0:30:00",
                    "Murder" : None,
                    "Status" : "Life"
                }
            file.write(str(self.Stats))
    def Read(self):
        try:
            with open(f"{self.PATH_VERSION}/Boss/Boss.txt","r") as file:
                self.Stats = StrToDict(str(file.readline()))
        except FileNotFoundError: self.Create()
    def Edit(self,**fields):
        self.Stats.update(fields)
        with open(f"{self.PATH_VERSION}/Boss/Boss.txt","w") as file:
            file.write(str(self.Stats))
    
    def _selfStats(self):
        self.Different = self.Stats["Different"]
        self.Image = self.Stats["Image"]
        self.Health = self.Stats["Health"]
        self.MaxHealth = self.Stats["MaxHealth"]
        self.Damage = self.Stats["Damage"]
        self.Armor = self.Stats["Armor"]
        self.Time = self.Stats["Time"]
        self.Murder = self.Stats["Murder"]
        self.Status = self.Stats["Status"]
        self.Gold = 500
        if self.MaxHealth >= 1000000000000:
            for a in range(int(self.MaxHealth / 100000000000)):
                try:
                    self.Gold += random.randint(66666666, 999999999 * a)
                except: pass
        elif self.MaxHealth >= 1000000000:
            for a in range(int(self.MaxHealth / 100000000)):
                try:
                    self.Gold += random.randint(666666, 9999999 * a)
                except: pass
        elif self.MaxHealth >= 1000000:
            for a in range(int(self.MaxHealth / 100000)):
                try:
                    self.Gold += random.randint(6666, 99999 * a)
                except: pass
        elif self.MaxHealth >= 100000:
            for a in range(int(self.MaxHealth / 10000)):
                try:
                    self.Gold += random.randint(666, 9999 * a)
                except: pass
        elif self.MaxHealth >= 1000:
            for a in range(int(self.MaxHealth / 100)):
                try:
                    self.Gold += random.randint(6, 99 * a)
                except: pass

    def Profile(self):
        NowTime = datetime.datetime.today()

        BackGround = Image.open(f"./Resurses/Bosses/{self.Different}/{self.Image}")
        BackGround = BackGround.resize((800,600))
        draw = ImageDraw.Draw(BackGround)
        if self.Status == "Life":
            font = ImageFont.truetype("arial.ttf",35)
            Gold = ReplaceNumber(self.Gold)
            _writeInPicture((270,230),f"{Gold} золотых",font,draw,(42,0,0))

            StartX = 100
            StartY = 275

            EndX = (((self.Health * 100) / self.MaxHealth) * 7)
            EndY = 374
            RedRand = random.randint(0,255)
            GreenRand = random.randint(0,255)
            BlueRand = random.randint(0,255)
            ColorSlider = ( RedRand , GreenRand , BlueRand )
            for XPos in range(int(EndX - StartX)):
                for YPos in range(int(EndY - StartY)):
                    BackGround.putpixel((StartX + XPos,StartY + YPos),ColorSlider)
            
            font = ImageFont.truetype("arial.ttf",40)
            Health = ReplaceNumber(self.Health)
            MaxHealth = ReplaceNumber(self.MaxHealth)
            _writeInPicture((105,300),f"{Health} / {MaxHealth} ед. здоровья",font,draw,(42,0,0))

            Color = (0,0,0)
            area = [(99,274),(701,274)]
            draw.line(area,fill=Color,width=1)
            area = [(701,274),((701,375))]
            draw.line(area,fill=Color,width=1)
            area = [(701,375),((99,375))]
            draw.line(area,fill=Color,width=1)
            area = [(99,375),((99,274))]
            draw.line(area,fill=Color,width=1)
        else:
            font = ImageFont.truetype("arial.ttf",80)
            _writeInPicture((50,280),f"БОСС ПОВЕРЖЕН",font,draw,(84,0,0))


            font = ImageFont.truetype("arial.ttf",35)
            _writeInPicture((100,230),f"{self.Murder} нанёс последний удар",font,draw,(42,0,0))
        
        font = ImageFont.truetype("arial.ttf",45)
        _writeInPicture((200,400),f"Осталось : {self.Time}",font,draw,(200,150,150))
        
        BackGround.save("TheBoss.png")

        df = discord.File("TheBoss.png","TheBoss.png")

        return df

        pass
if __name__ == "__main__":
    pass