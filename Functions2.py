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
import asyncio
import requests
import json
import time

def SplitURL(URL):
    with requests.Session() as Session:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 OPR/68.0.3618.191'
        }
        GetURL = Session.get(f'https://clck.ru/--?json=true&url={URL}',headers=headers)
        Json = GetURL.json()
        return Json[0]
class Error(BaseException):
    pass
class CommandError(Error):
    def __init__(self,Message,Command):
        self.Message = Message
        self.Command = Command

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
def ReplaceNumber(Number : int):
    """
    Показывает цифры более компактно
    
    Пример : 
        100 000 = 100К
        1 000 000 = 1М
        1 000 000 000 = 1B
        1 000 000 000 000 = 1T
        1 000 000 000 000 000 = 1P
        1 000 000 000 000 000 000 = 1E
        1 000 000 000 000 000 000 000 = 1Z
        1 000 000 000 000 000 000 000 000 = 1Y
        ----------------------
        -100 000 = -100К
        -1 000 000 = -1М
        -1 000 000 000 = -1B
        -1 000 000 000 000 = -1T
        -1 000 000 000 000 000 = -1P
        -1 000 000 000 000 000 000 = -1E
        -1 000 000 000 000 000 000 000 = -1Z
        -1 000 000 000 000 000 000 000 000 = -1Y
    """
    Minus = False
    if Number < 0:
        Minus = True
        Number *= -1
    if Number >= 1000000000000000000000000:
        NumberSplit = Number / 1000000000000000000000000
        Number = int(NumberSplit)
        if Minus == True:
            Number = f"-{Number}Y"
        else:
            Number = f"{Number}Y"
    elif Number >= 1000000000000000000000:
        NumberSplit = Number / 1000000000000000000000
        Number = int(NumberSplit)
        if Minus == True:
            Number = f"-{Number}z"
        else:
            Number = f"{Number}z"
    elif Number >= 1000000000000000000:
        NumberSplit = Number / 1000000000000000000
        Number = int(NumberSplit)
        if Minus == True:
            Number = f"-{Number}E"
        else:
            Number = f"{Number}E"
    elif Number >= 1000000000000000:
        NumberSplit = Number / 1000000000000000
        Number = int(NumberSplit)
        if Minus == True:
            Number = f"-{Number}P"
        else:
            Number = f"{Number}P"
    elif Number >= 1000000000000:
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
    """ Игрок """

    def __init__(self,Name):
        self.PATH_VERSION = "./Version 6"
        self.Name = Name
        
        self.StartStats = {
            "Main" : {
                    "Health" : 35,
                    "MaxHealth" : 35,
                    "Shield" : 0,
                    "MaxShield" : 0,
                    "Mana" : 1,
                    "MaxMana" : 1,
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
            "Room" : {},
            "Everyday bonus" : {
                    "Day" : None,
                    "Gold" : None
                },
            "Inventor" : [],
            "Equipped" : {
                "Head" : None,
                "Body" : None,
                "Legs" : None,
                "Boot" : None,
                "Left_hand" : None,
                "Right_hand" : None,
                "Ring_1" : None,
                "Ring_2" : None,
                "Ring_3" : None,
                "Ring_4" : None,
                "Ring_5" : None,
                },
            "Quests" : {},
            "Talants" : {
                "Heroic Level":{
                    "Name" : "Героический уровень",
                    "Description" : "Увеличивает ваши характеристики.\nТребуется для других талантов",
                    "PerLevel" : "Сила += 0.1%\nЛовкость += 0.2%\nИнтеллект += 0.3%\nЗдоровье += 320 ед.\nОпыт += 100 ед.\nУровень += 1",
                    "Level" : 0,
                    "MaxLevel" : 100,
                    "Exp" : 0,
                    "NeedExp" : 1000,
                    "Lock" : 0,
                    "NeedAt" : []
                    },
                "More Exp" : {
                    "Name" : "Больше опыта",
                    "Description" : "Больше опыта за сообщения",
                    "PerLevel" : "Увеличивает количество получаемого опыта",
                    "Level" : 0,
                    "MaxLevel" : 100,
                    "Exp" : 0,
                    "NeedExp" : 10,
                    "Lock" : 0,
                    "NeedAt" : []
                    },
                "More Gold" : {
                        "Name" : "Больше золота",
                        "Description" : "Получение золота требует меньшее количество золота",
                        "PerLevel" : "Уменьшает требования на 1 сообщение",
                        "Level" : 0,
                        "MaxLevel" : 5,
                        "Exp" : 0,
                        "NeedExp" : 10,
                        "Lock" : 0,
                        "NeedAt" : []
                        },
                "More Damage" : {
                        "Name" : "Усиленный урон",
                        "Description" : "Вы наносите больше урона",
                        "PerLevel" : "Увеличивает урон на 5%",
                        "Level" : 0,
                        "MaxLevel" : 10,
                        "Exp" : 0,
                        "NeedExp" : 100,
                        "Lock" : 0,
                        "NeedAt" : []
                        },
                "More Protect" : {
                            "Name" : "Броня",
                            "Description" : "Вы получаете меньше урона",
                            "PerLevel" : "Уменьшает получаемый урон на 2.5%",
                            "Level" : 0,
                            "MaxLevel" : 20,
                            "Exp" : 0,
                            "NeedExp" : 50,
                            "Lock" : 0,
                            "NeedAt" : []
                            },
                "Passive Generator" : {
                        "Name" : "Пассивный генератор опыта",
                        "Description" : "Персонаж получает возможность пассивно набирать опыт. Стандартное значение 1 ед./час.",
                        "PerLevel" : "",
                        "Level" : 0,
                        "MaxLevel" : 1,
                        "Exp" : 0,
                        "NeedExp" : 1000,
                        "Lock" : 1,
                        "NeedAt" : [{"Heroic Level":{"Name":"Героический уровень","Level":3}}]
                        },
                "Updater Generator Amount" : {
                        "Name" : "Генератор Опыта",
                        "Description" : "Усиливает генератор опыта",
                        "PerLevel" : "Увеличивает опыт на 10 ед.",
                        "Level" : 0,
                        "MaxLevel" : 4,
                        "Exp" : 0,
                        "NeedExp" : 700,
                        "Lock" : 1,
                        "NeedAt" : [{"Passive Generator":{"Name":"Пассивный генератор опыта","Level":1}}]
                        },
                "Updater Generator Speed" : {
                        "Name" : "Улучшенный Генератор Опыта",
                        "Description" : "Ускоряет генератор опыта",
                        "PerLevel" : "Уменьшает время на 1 минуту",
                        "Level" : 0,
                        "MaxLevel" : 40,
                        "Exp" : 0,
                        "NeedExp" : 2000,
                        "Lock" : 1,
                        "NeedAt" : [{"Passive Generator":{"Name":"Пассивный генератор опыта","Level":1}}]
                        },
                "Regeneration" : {
                        "Name" : "Регенерация",
                        "Description" : "Открывает навыки регенерации \nСтандартная регенерация : 0 ед./мин.",
                        "PerLevel" : "",
                        "Level" : 0,
                        "MaxLevel" : 1,
                        "Exp" : 0,
                        "NeedExp" : 300,
                        "Lock" : 1,
                        "NeedAt" : {"Heroic Level":{"Name":"Героический уровень","Level":5}}
                        },
                "Regeneration Amount" : {
                        "Name" : "Усиленная Регенерация",
                        "Description" : "Усиливает регенерацию здоровья",
                        "PerLevel" : "Увеличивает на 10 ед. регенерацию",
                        "Level" : 0,
                        "MaxLevel" : 100,
                        "Exp" : 0,
                        "NeedExp" : 300,
                        "Lock" : 1,
                        "NeedAt" : [{"Regeneration":{"Name":"Регенерация","Level":1}}]
                        },
                "Regeneration Speed" : {
                        "Name" : "Ускоренная Регенерация",
                        "Description" : "Ускоряет получение регенерации здоровья",
                        "PerLevel" : "Уменьшает время получение регенерации на 1 секунду",
                        "Level" : 0,
                        "MaxLevel" : 30,
                        "Exp" : 0,
                        "NeedExp" : 600,
                        "Lock" : 1,
                        "NeedAt" : [{"Regeneration":{"Name":"Регенерация","Level":1}}]
                        },
                "Blacksmith" : {
                        "Name" : "Кузнец",
                        "Description" : "Сила предметов становиться сильнее",
                        "PerLevel" : "Увеличивает силу у будущих предметов на 2%",
                        "Level" : 0,
                        "MaxLevel" : 20,
                        "Exp" : 0,
                        "NeedExp" : 600,
                        "Lock" : 0,
                        "NeedAt" : []
                        },
                "Immunity" : {
                        "Name" : "Иммунитет",
                        "Description" : "Развить иммунитет \nПосле развития откроются следующие навыки : \nИммунитет от Яда",
                        "PerLevel" : "",
                        "Level" : 0,
                        "MaxLevel" : 1,
                        "Exp" : 0,
                        "NeedExp" : 25,
                        "Lock" : 0,
                        "NeedAt" : []
                        },
                "Immunity from poison" : {
                        "Name" : "Иммунитет От Яда",
                        "Description" : "Вы получаете меньше урона от яда",
                        "PerLevel" : "Уменьшает получаемый урон от яда на 2%",
                        "Level" : 0,
                        "MaxLevel" : 50,
                        "Exp" : 0,
                        "NeedExp" : 100,
                        "Lock" : 1,
                        "NeedAt" : [{"Immunity":{"Name":"Иммунитет","Level":1}}]
                        },
                "Bonus" : {
                        "Name" : "Бонусы",
                        "Description" : "Увеличивает ежедневную награду",
                        "PerLevel" : "Увеличивает ежедневную награду на 300 золотых",
                        "Level" : 0,
                        "MaxLevel" : 10,
                        "Exp" : 0,
                        "NeedExp" : 100,
                        "Lock" : 0,
                        "NeedAt" : []
                        },
                "Max Bonus" : {
                        "Name" : "Бонусы",
                        "Description" : "Увеличивает максимальную ежедневную награду",
                        "PerLevel" : "Увеличивает максимальную ежедневную награду на 1250 золотых",
                        "Level" : 0,
                        "MaxLevel" : 10,
                        "Exp" : 0,
                        "NeedExp" : 1000,
                        "Lock" : 1,
                        "NeedAt" : [{"Bonus":{"Name":"Бонусы","Level":10}}]
                        },
                "Spells" : {
                        "Name" : "Способности",
                        "Description" : "Открывает возможность получить способности",
                        "PerLevel" : "Открывает более сильные таланты",
                        "Level" : 0,
                        "MaxLevel" : 5,
                        "Exp" : 0,
                        "NeedExp" : 3000,
                        "Lock" : 1,
                        "NeedAt" : [{"Heroic Level":{"Name":"Героический уровень","Level":4}}]
                        },
                "Berserk" : {
                        "Name" : "Берсерк",
                        "Description" : "Чем меньше количество здоровья, тем больше наносите урона",
                        "PerLevel" : "Увеличивает урон на 1%",
                        "Level" : 0,
                        "MaxLevel" : 10,
                        "Exp" : 0,
                        "NeedExp" : 1000,
                        "Lock" : 1,
                        "NeedAt" : [{"Spells":{"Name":"Способности","Level":1}}]
                        },
                "Invincible" : {
                        "Name" : "Непобедимый",
                        "Description" : """При фатальном ударе, вы не погибаете, вместо этого количество количество здоровья станоситься 50 ед.\nФатальный урон : Урон, из за которого вы должны были погибнуть. (Он должен быть больше чем здоровья которое вы получаете от исциления с помощью этого навыка)""",
                        "PerLevel" : "Увеличивает исцеление после навыка на 500 ед.",
                        "Level" : 0,
                        "MaxLevel" : 5,
                        "Exp" : 0,
                        "NeedExp" : 3000,
                        "Lock" : 1,
                        "NeedAt" : [{"Spells":{"Name":"Способности","Level":2}}]
                        },
                "Annihilator" : {
                        "Name" : "Уничтожитель",
                        "Description" : "Шанс нанести (х5) кратный урон",
                        "PerLevel" : "Увеличивает шанс на 0.1%",
                        "Level" : 0,
                        "MaxLevel" : 50,
                        "Exp" : 0,
                        "NeedExp" : 5000,
                        "Lock" : 1,
                        "NeedAt" : [{"Spells":{"Name":"Способности","Level":3}}]
                        },
                "Repair" : {
                        "Name" : "Починка",
                        "Description" : "Предметы которые экипированные, начинают чиниться со временем. (Каждые 10 минут)",
                        "PerLevel" : "Увеличивает получаемую прочность на 3 ед.",
                        "Level" : 0,
                        "MaxLevel" : 6,
                        "Exp" : 0,
                        "NeedExp" : 1300,
                        "Lock" : 1,
                        "NeedAt" : [{"Spells":{"Name":"Способности","Level":4}},{"Blacksmith":{"Name:":"Кузнец","Level":20}}]
                        },
                "Determination" : {
                        "Name" : "Решимость",
                        "Description" : "Вы наполняетесь решимостью, из за чего большая часть характеристик увеличивается, однако вы теряете возможность получения очков навыков\nУвеличивает : \nУрон на 100%\nБроню на 100%\nПолучаемое исциление на 100%",
                        "PerLevel" : "",
                        "Level" : 0,
                        "MaxLevel" : 1,
                        "Exp" : 0,
                        "NeedExp" : 100000,
                        "Lock" : 1,
                        "NeedAt" : [{"Spells":{"Name":"Способности","Level":5}},{"Heroic Level":{"Name:":"Героический уровень","Level":100}},{"More Damage":{"Name":"Усиленный урон",'Level':10}},{"More Protect":{"Name":"Броня","Level":20}}]
                        },
                },
            "TalantPicked": "Талант не выбран",
            "Effects" : {},
            "FunStats" : {
                "Viewing Loli" : 0,
                "Likes of Loli" : 0,
                "Dislikes of Loli" : 0,
                "Total messages" : 0
            },
            "Profile": {
                "Age" : None,
                "Gender" : None,
                "Activity" : None,
                "About me" : None
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
    def Read(self):
        """ Прочитать информацию снова """
        with codecs.open(f"{self.PATH_VERSION}/Stats/{self.Name}.txt","r",encoding="utf-8") as file:
            self.Stats = StrToDict(file.readline())
        self._selfStats()
    def _selfStats(self):
        self.Stats_main = self.Stats["Main"]
        self.Stats_Room = self.Stats["Room"]
        self.Stats_Everydaybonus = self.Stats["Everyday bonus"]
        self.Equipped = self.Stats['Equipped']
        self.Talants = self.Stats['Talants']
        self.TalantPicked = self.Stats["TalantPicked"]

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

        self.Shield = int(self.Stats_main["Shield"])
        self.MaxShield = int(self.Stats_main["MaxShield"])
        self.Mana = int(self.Stats_main["Mana"])
        self.MaxMana = int(self.Stats_main["MaxMana"])

        self.Inventor = self.Stats["Inventor"]

        self.Head = Item(self,self.Equipped["Head"])
        self.Body = Item(self,self.Equipped["Body"])
        self.Legs = Item(self,self.Equipped["Legs"])
        self.Boot = Item(self,self.Equipped["Boot"])

        self.Left_hand = Item(self,self.Equipped["Left_hand"])
        self.Right_hand = Item(self,self.Equipped["Right_hand"])
        
        self.Ring_1 = Item(self,self.Equipped["Ring_1"])
        self.Ring_2 = Item(self,self.Equipped["Ring_2"])
        self.Ring_3 = Item(self,self.Equipped["Ring_3"])
        self.Ring_4 = Item(self,self.Equipped["Ring_4"])
        self.Ring_5 = Item(self,self.Equipped["Ring_5"])

        self.BonusGold = self.Stats_Everydaybonus["Gold"]
        self.BonusDay = self.Stats_Everydaybonus["Day"]

        if int(self.Gold) < 0: self.Gold = 0
        
    def GetTalants(self):
        """Получить таланты. Использовать всего 1 раз"""
        self.GetTalanted = list()
        for _Talant_ in self.Talants:
            _Talant = self.Talants[_Talant_]
            self.GetTalanted.append(Talant(self,_Talant,_Talant_))

    def AddInventor(self,**fields):
        """
            Записать в инвентарь.

            `------------------- Обязательные -----------------`

            `Type` : тип предмета  (TypeItem.$)

            `Name` : имя предмета

            `Class` : Класс предмета

            `Классы` : Сломанный -> Первоначальный -> Обычный -> Редкий -> Эпический -> Легендарный -> Мифический -> Демонический = Божественный -> Уникальный -> Реликвия -> Запретный

            `ID` : это персональный номер у предмета, к которому нужно будет отссылаться, дабы взаимодействовать с ним

            `Gold` : Количество золотых, которые нужно потратить, для улучшения предмета

            'MaxGold' : Максимальное количество золотых

            `------------------- Для предметов ----------------`

            `Duration` : длительность эффекта

            `Magic` : особое свойство

            `------------------- Для оружия -------------------`

            `Armor` : прочность оружия

            `Damage` : Урон от оружия

            `Magic` : особое свойство

            `------------------- Для экиперовки ---------------`

            `Armor` : прочность брони

            `Protect` : Уровень защиты

            `Magic` : особое свойство
            
            """
        self.Inventor.append(fields)
        self.Edit(
            Inventor=self.Inventor
        )
        return fields
    def RemoveInventor(self,ID : int):
        """ Удалить вещь из инвентаря """
        for item in self.Inventor:
            itemid = int(item["ID"])
            if itemid == ID:
                self.Inventor.remove(item)
        self.Edit(
            Inventor = self.Inventor
        )
    class NotStandartEquip(Error): pass
    def EquipmentItem(self,ID,Where):
        """
        Экипировать вещь
        Доступно : 
            "Head" : None,
            "Body" : None,
            "Legs" : None,
            "Boot" : None,
            "Left_hand" : None,
            "Right_hand" : None,
            "Ring_1" : None,
            "Ring_2" : None,
            "Ring_3" : None,
            "Ring_4" : None,
            "Ring_5" : None,
        """
        for item in self.Inventor:
            itemID = int(item["ID"])
            if itemID == ID:
                if Where == "Head":self.Edit(Edit = "Equipped",Head = item)
                elif Where == "Body":self.Edit(Edit = "Equipped",Body = item)
                elif Where == "Legs":self.Edit(Edit = "Equipped",Legs = item)
                elif Where == "Boot":self.Edit(Edit = "Equipped",Boot = item)
                elif Where == "Left_hand":self.Edit(Edit = "Equipped",Left_hand = item)
                elif Where == "Right_hand":self.Edit(Edit = "Equipped",Right_hand = item)
                elif Where == "Ring_1":self.Edit(Edit = "Equipped",Ring_1 = item)
                elif Where == "Ring_2":self.Edit(Edit = "Equipped",Ring_2 = item)
                elif Where == "Ring_3":self.Edit(Edit = "Equipped",Ring_3 = item)
                elif Where == "Ring_4":self.Edit(Edit = "Equipped",Ring_4 = item)
                elif Where == "Ring_5":self.Edit(Edit = "Equipped",Ring_5 = item)
                else:
                    raise Error("Не правильно указано куда именно следовало экипировать предмет")
        self._selfStats()

    def Edit(self,**fields):
        """ Редактировать статистику. Edit = "Main" , "Room" , "Everyday bonus" """
        
        try:
            Edit = str(fields.pop("Edit"))
            EditStats = self.Stats[Edit]
            EditStats.update(fields)
        except:
            self.Stats.update(fields)
        
        with codecs.open(f"{self.PATH_VERSION}/Stats/{self.Name}.txt","w",encoding="utf-8") as file:
            file.write(str(self.Stats))
        
        self._selfStats()
    def Edit2(self,Edit,fields):
        """ Редактировать статистику. Edit = "Main" , "Room" , "Everyday bonus" """
        try:
            EditStats = self.Stats[Edit]
            EditStats.update(fields)
        except:
            self.Stats.update(fields)
        with codecs.open(f"{self.PATH_VERSION}/Stats/{self.Name}.txt","w",encoding="utf-8") as file:
            file.write(str(self.Stats))
        self._selfStats()
    def UpdateTalant(self,**fields):
        Updater = self.Talants[self.TalantPicked]
        Updater.update(fields)
        with codecs.open(f"{self.PATH_VERSION}/Stats/{self.Name}.txt","w",encoding="utf-8") as file:
            file.write(str(self.Stats))
        self._selfStats()
    class mode():
        class one(): pass
        class multiply(): 
            class ErrorNoCount(Error): pass
    def GetGuild(self,Guild):
        """ Получить информацию исходя из Гильдии """

        try:
            Stats = self.Stats_Room[Guild]
            self.RoomName = Stats["Name"]
            self.RoomPermissions = Stats["Permissions"]
        except:
            self.RoomName = self.Name
            self.RoomPermissions = None
            self.Stats_Room.update({Guild:{"Name":self.Name,"Permissions":None}})
            with codecs.open(f"{self.PATH_VERSION}/Stats/{self.Name}.txt","w",encoding="utf-8") as file:
                file.write(str(self.Stats))
    def SaveRoom(self,Guild,Name,Permissions):
        """ Сохранить статистику комнаты """

        self.RoomName = Name
        self.RoomPermissions = Permissions
        self.Stats_Room.update({Guild:{"Name":self.RoomName,"Permissions":self.RoomPermissions}})
        with codecs.open(f"{self.PATH_VERSION}/Stats/{self.Name}.txt","w",encoding="utf-8") as file:
            file.write(str(self.Stats))
    def GetTalant(self,TalantName):
        """ Получить статистику о таланте. """

        return Talant(self,self.Talants[TalantName],TalantName)
    
    def LevelUp(self,mode,**fields):
        """ Получить уровень. 
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
        """ Потерять уровень. """
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
        """ Показать профиль игрока """
        try:
            BackGround = Image.open(f"./Resurses/BackGround_{self.Name}.png")
        except: BackGround = Image.open(f"./Resurses/BackGround_StandartBackGround.png")
        Main = Image.open(f"./Resurses/Main.png")
        Ava = Image.open(f"./Resurses/{self.Name}.png")
        Ava = Ava.resize((264,264))
        draw = ImageDraw.Draw(Main)
        
        font = ImageFont.truetype("arial.ttf",50)
        Level = ReplaceNumber(self.Level)
        _writeInPicture((163,309),Level,font,draw,"black")

        font = ImageFont.truetype("arial.ttf",100)
        _writeInPicture((370,155),self.Name,font,draw,(200,210,255))

        font = ImageFont.truetype("arial.ttf",35)
        Health = ReplaceNumber(self.Health)
        MaxHealth = ReplaceNumber(self.MaxHealth)
        Protect = self.MaxProtect()
        Protect = ReplaceNumber(Protect)
        _writeInPicture((550,276),f"Здоровье : {Health} ед./ {MaxHealth} ({Protect})",font,draw,"black")

        font = ImageFont.truetype("arial.ttf",35)
        Damage = ReplaceNumber(self.Damage)
        _writeInPicture((550,328),f"Урон : {Damage}",font,draw,"black")

        font = ImageFont.truetype("arial.ttf",35)
        LevelNeed = self.Level * 500
        LevelNeed = ReplaceNumber(LevelNeed)
        _writeInPicture((380,743),f"Опыт : {self.Exp} / {LevelNeed}",font,draw,"black")

        font = ImageFont.truetype("arial.ttf",30)
        Plus = ReplaceNumber(self.Plus)
        _writeInPicture((700,700),f"Талант очки : {Plus}",font,draw,"black")

        font = ImageFont.truetype("arial.ttf",50)
        Strength = round(self.Strength)
        Strength = ReplaceNumber(Strength)
        _writeInPicture((38,393),f"Сила : \n{Strength}",font,draw,(255,100,0))

        font = ImageFont.truetype("arial.ttf",50)
        Agility = round(self.Agility)
        Agility = ReplaceNumber(Agility)
        _writeInPicture((38,471),f"Ловкость : \n{Agility}",font,draw,(0,255,0))

        font = ImageFont.truetype("arial.ttf",50)
        Intelligence = round(self.Intelligence)
        Intelligence = ReplaceNumber(Intelligence)
        _writeInPicture((38,570),f"Интеллект : \n{Intelligence}",font,draw,(0,255,255))

        font = ImageFont.truetype("arial.ttf",35)
        Gold = ReplaceNumber(self.Gold)
        _writeInPicture((550,380),f"Золота : {Gold} / {self.Messages}",font,draw,"black")

        font = ImageFont.truetype("arial.ttf",60)
        _writeInPicture((380,500),self.Description,font,draw,"black")

        font = ImageFont.truetype("arial.ttf",35)
        _writeInPicture((380,470),"О себе : \n",font,draw,"black")

        Main.paste(Ava,(46,8))
        BackGround = BackGround.resize((1000,1450))
        BackGround.paste(Main.convert("RGB"),(0,550),Main)
        



        BackGround.save("StatsPl.png")
        df = discord.File("StatsPl.png","StatsPl.png")

        return df
    def GetInventor(self):
        """ Получить инвентарь в class Item """
        self.GetInventored = list()
        for item in self.Inventor:
            item = Item(self,item)
            self.GetInventored.append(item)
    def GetEquipment(self):
        self.GetEquipmented = list()
        for item in self.Equipped:
            ItemEquipped = self.Equipped[item]
            item = Item(self,ItemEquipped)
            self.GetEquipmented.append(item)
    def Attack(self,Target):
        """Атаковать указанную цель"""
        GetDamage = self.MaxDamage()
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
    def CheckEquipItem(self,Where):
        for item in self.GetInventored:
            if item.ID == self.Left_hand.ID:
                self.EquipmentItem(self.Left_hand.ID,Where)
    def MaxDamage(self):
        """ Урон который наносит герой. """

        GetDamage = random.randint(1,self.Damage + self.Left_hand.Damage + self.Right_hand.Damage)

        MoreDamage = self.GetTalant("More Damage")
        GetDamage += (5 * MoreDamage.Level) / 100

        GetDamage *= self.Strength

        return GetDamage
    def MaxProtect(self):
        Protect = self.Head.Protect
        Protect += self.Body.Protect
        Protect += self.Legs.Protect
        Protect += self.Boot.Protect
        return Protect
class Item():
    """
    Предмет
    """
    def __init__(self,Player : C_Player,Stats):
        self.Player = Player
        self.Stats = Stats
        self.Damage = 0
        self.Protect = 0
        self.Armor = 0
        self.Where = "Неопознано"
        
        try:
            _Name = self.Stats["Name"]
            self.Name = str(_Name["Name"])
            self.Description = str(_Name["Description"])
        except:
            self.Name = "Неопознанный"
            self.Description = "Отсуствует"
        
        try: self.Magic = self.Stats["Magic"]
        except: self.Magic = None
        
        try: self.Class = str(self.Stats["Class"])
        except: self.Class = "Отсуствует"

        try: self.ID = int(self.Stats["ID"])
        except: self.ID = 0

        try: self.Gold = int(self.Stats["Gold"])
        except: self.Gold = 0

        try: self.MaxGold = int(self.Stats["MaxGold"])
        except: self.MaxGold = 1

        
        try: self.AllGold = int(self.Stats["AllGold"])
        except: self.AllGold = 0

        try:
            self.Type = self.Stats["Type"]

            Keys = self.Type.keys()
            self.TypeKey = "None"
            for key in Keys:
                self.TypeKey = key
                if key == "Weapon":
                    Stats = self.Type[key]
                    self.Damage = Stats["Damage"]
                    self.Armor = Stats["Armor"]
                    self.Magic = Stats["Magic"]
                    self.Where = "Left_hand / Right_hand"
                elif key == "Equipment":
                    Stats = self.Type[key]
                    self.Protect = Stats["Protect"]
                    self.Armor = Stats["Armor"]
                    self.Magic = Stats["Magic"]
                    self.Where = Stats["Where"]
                elif key == "Ring":
                    Stats = self.Type[key]
                    self.Magic = Stats["Magic"]
                    self.Where = "Ring_"
        except TypeError:
            pass
    
    def Upgrade(self,Gold):
        self.Player.Gold -= Gold
        if self.Player.Gold < 0: 
            self.Player.Gold == 0
        else:
            self.Gold += Gold
            self.AllGold += Gold
            if self.Gold >= self.MaxGold:
                self.Gold = 0
                if self.Class == self.Classes.Первоначальный():
                    self.Damage += random.randint(2000,5000)
                    self.Protect += random.randint(2200,4800)
                    self.Armor += random.randint(400,1000)
                    self.MaxGold += random.randint(100,1000)
                    self.Class = self.Classes.Редкий()
                elif self.Class == self.Classes.Редкий():
                    self.Damage += random.randint(6000,10000)
                    self.Protect += random.randint(6000,9000)
                    self.Armor += random.randint(2000,4000)
                    self.MaxGold += random.randint(2000,3000)
                    self.Class = self.Classes.Эпический()
                elif self.Class == self.Classes.Эпический():
                    self.Damage += random.randint(25000,35000)
                    self.Protect += random.randint(20000,40000)
                    self.Armor += random.randint(6000,8000)
                    self.MaxGold += random.randint(6000,9000)
                    self.Class = self.Classes.Легендарный()
                elif self.Class == self.Classes.Легендарный():
                    self.Damage += random.randint(50000,80000)
                    self.Protect += random.randint(50000,100000)
                    self.Armor += random.randint(8000,9000)
                    self.MaxGold += random.randint(15000,35000)
                    self.Class = self.Classes.Мифический()
                elif self.Class == self.Classes.Мифический():
                    self.Damage = random.randint(10,13180000)
                    self.Protect = random.randint(10,131800000)
                    self.Armor = random.randint(10,900000)
                    self.MaxGold += random.randint(990000,2990000)
                elif self.Class == self.Classes.Демонический():
                    self.Damage += random.randint(5000000,9000000)
                    self.Protect += random.randint(1000000,4000000)
                    self.Armor += random.randint(7000,9000)
                    self.MaxGold += 10000000000000
                elif self.Class == self.Classes.Божественный():
                    self.Damage += random.randint(7000000,8350000)
                    self.Protect += random.randint(2000000,3350000)
                    self.Armor += random.randint(8000,8500)
                    self.MaxGold += 10000000000000
                else:
                    self.MaxGold = 10000000000000000
                if self.TypeKey == "Weapon":
                    self.Type = self.Types.Weapon(self.Damage,self.Armor,self.Magic)
                elif self.TypeKey == "Equipment":
                    self.Type = self.Types.Equipment(self.Protect,self.Armor,self.Magic)
            self.Player.RemoveInventor(self.ID)
            self.Player.AddInventor(
                Type=self.Type,
                Name = self.CreateName(self.Name,self.Description),
                Class = self.Class,
                ID = self.ID,
                Gold = self.Gold,
                MaxGold = self.MaxGold,
                AllGold = self.AllGold
                )
            self.Player.CheckEquipItem("Left_hand")
            self.Player.CheckEquipItem("Right_hand")
        self.Player.Edit(Edit="Main",Gold=self.Player.Gold)
    
    def Return(self):
        return 
    @staticmethod
    def Find(ID : int,Player : C_Player):
        Player.GetInventor()
        for _Item in Player.Inventor:
            _ItemID = _Item["ID"]
            if _ItemID == ID:
                return Item(Player,_Item)


    @staticmethod
    def CreateName(Name,Description): return {"Name":Name,"Description":Description}
    class Types():
        @staticmethod
        def Item(): return "Item"

        @staticmethod
        def Ring(Magic): return {"Ring":{"Magic":Magic}}

        @staticmethod
        def Weapon(Damage : int,Armor : int,Magic):
            """Оружие"""
            return {"Weapon":{"Damage":Damage,"Armor":Armor,"Magic":Magic}}

        @staticmethod
        def Equipment(Protect : int,Armor : int,Where : str,Magic):
            """Экипировка"""
            return {"Equipment":{"Where":Where,"Protect":Protect,"Armor":Armor,"Magic":Magic}}

        @staticmethod
        def Ingredient(): return "Ingredient"
    class Classes():

        @staticmethod
        def Сломанный(): return "Сломанный"
        
        @staticmethod
        def Первоначальный(): return "Первоначальный"
        
        @staticmethod
        def Обычный(): return "Обычный"
        
        @staticmethod
        def Редкий(): return "Редкий"
        
        @staticmethod
        def Эпический(): return "Эпический"
        
        @staticmethod
        def Легендарный(): return "Легендарный"
        
        @staticmethod
        def Мифический(): return "Мифический"
        
        @staticmethod
        def Демонический(): return "Демонический"
        
        @staticmethod
        def Божественный(): return "Божественный"
        
        @staticmethod
        def Уникальный(): return "Уникальный"
        
        @staticmethod
        def Реликвия(): return "Реликвия"

        @staticmethod
        def Запретный(): return "Запретный"

        @staticmethod
        def GetList():
            List = [
                "Сломанный","Первоначальный","Обычный","Сломанный",
                "Редкий","Эпический","Легендарный","Мифический",
                "Демонический","Божественный","Уникальный","Реликвия",
                "Запретный"]
            return List

class Gabriel():
    """ Габриэль """

    def __init__(self):
        pass
    class TooManyWords(Error): pass
    def Message(self,CountMessages : int,ServerName : str):
        """ Сообщение """

        Lines = []
        with codecs.open(f"./Servers/{ServerName}/Words.txt","r",encoding='utf-8', errors='ignore') as file:
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
        BadSymvol = ["""""", "\n"]
        while Count < CountMessages:
            try:
                RandomLine = random.randint(1,len(Lines) - 2)
                MainLine = list()
                Words = Lines.pop(RandomLine)
                MainLine.append(Words.split(" "))
                for word in MainLine[0]:
                    Write = randomBool(0,3,1)
                    if Write == False:
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
                                        if str(wordSplit) not in BadSymvol:
                                            Message += wordSplit
                                Message += f" "
                                Count += 1
                                if Count >= CountMessages:
                                    return Message
                    WriteOtherLine = randomBool(0,2,1)
                    if WriteOtherLine == True:
                        RandomLine = random.randint(1,len(Lines) - 2)
                        OtherLine = list()
                        Words = Lines.pop(RandomLine)
                        OtherLine.append(Words.split(" "))
                        for word2 in OtherLine[0]:
                            Write = randomBool(0,3,1)
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
                                                if str(wordSplit) not in BadSymvol:
                                                    Message += wordSplit
                                        Message += f" "
                                        Count += 1
                                        if Count >= CountMessages:
                                            return Message
            except ValueError:
                raise self.TooManyWords("Слишком мало слов я знаю")
    def ReadWords(self,Server : str):
        """ Прочитать все сохраненные слова """

        AllWords = str()
        with codecs.open(f"./Servers/{Server}/Words.txt","r"
        ,encoding='utf-8', errors='ignore') as file:
            try:
                for line in file.readlines():
                    AllWords += line
            except:
                pass
        return AllWords
    def SaveWords(self,msg : str,Server : str):
        """Сохранить слова"""
        Oldmsg = self.ReadWords(Server)
        with codecs.open(f"./Servers/{Server}/Words.txt","w"
        ,encoding='utf-8', errors='ignore') as file:
            msgSplitLines = msg.split("\n")
            file.write(f"{Oldmsg}")
            for line in msgSplitLines:
                file.writelines(f"\n{line}")

    def SearchInfo(self,GetRequest : str):
        Request = "https://ru.wikipedia.org/wiki/"
        Search = "https://ru.wikipedia.org/w/index.php?search="
        
        for Message in GetRequest.split(" "):
            Request += f"{Message}_"
            Search += f"{Message}+"
        Request = Request[:-1]
        Search = Search[:-1]
        with requests.Session() as Session:
            headers = {
                'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 OPR/68.0.3618.191'
            }
            MainCity = Session.get(Request,headers=headers)

            soup = BeautifulSoup(MainCity.content,'lxml')
            
            try:
                main = soup.find('div',{"class":"mw-parser-output"})
                
                RussianLanguage = [
                    "й","ц","у","к","е","н","г","ш","щ","з","х","ъ","ф","ы","в","а","п","р","о","л",
                    "д","ж","э","я","ч","с","м","и","т","ь","б","ю",".",",","ё","?","!",'-'," "
                ]
                Pages = 6
                description = ""
                
                for P in main.find_all("p"):
                    Message = ""
                    Count = 200
                    Be = False
                    for latter in str(P.text):
                        if latter.lower() in RussianLanguage:
                            if Count > 0:
                                description += latter
                            elif Count <= 0: Be = True
                            Count -= 1
                    if Be == True: 
                        description += "..."
                        Pages -= 1
                    if Pages < 0: break

                
                return discord.Embed(title=GetRequest,url=Request,description=f"Согласно википедии\n{description}")
                
            
            except BaseException as Error:
                if str(Error) == "'NoneType' object has no attribute 'find_all'":
                    #Этой статьи нет
                    Embed = discord.Embed(title=GetRequest,description="Этой статьи нет, возможно вы имели что то другое?")
                    MainCity = Session.get(Search,headers=headers)

                    soup = BeautifulSoup(MainCity.content,'lxml')
                    main = soup.find("ul",{"class":"mw-search-results"})

                    for li in main.find_all('li',{"class":"mw-search-result"}):
                        a = li.find('a')
                        Link = f"https://ru.wikipedia.org{str(a.get('href'))}"
                        Link = SplitURL(Link)
                        Title = str(a.text)
                        Embed.add_field(name=Title,value=Link)
                    return Embed
        

def _writeInPicture(area,content,font,draw,color):
    """ Рисовать что либо на холсте """
    draw.text(area,str(content),font=font,fill=color)

class Boss():
    """ Боссы """
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
        """ Создать нового босса """

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
                    "Status" : "Life",
                    "LastGetDamage" : 0,
                    "GetItem" : None
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
                    "Status" : "Life",
                    "LastGetDamage" : 0,
                    "GetItem" : None
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
                    "Status" : "Life",
                    "LastGetDamage" : 0,
                    "GetItem" : None
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
                    "Status" : "Life",
                    "LastGetDamage" : 0,
                    "GetItem" : None
                }
            file.write(str(self.Stats))
    
    def Read(self):
        """ Прочитать сохраненную информацию о боссе """

        try:
            with open(f"{self.PATH_VERSION}/Boss/Boss.txt","r") as file:
                self.Stats = StrToDict(str(file.readline()))
        except: self.Create()
        self._selfStats()

    def Edit(self,**fields):
        """ Редактировать информацию о боссе """
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
        self.Time = str(self.Stats["Time"])
        self.Murder = self.Stats["Murder"]
        self.Status = self.Stats["Status"]
        self.GetItem = self.Stats["GetItem"]

        self.LastGetDamage = self.Stats["LastGetDamage"]

        Timer = self.Time.split(":")

        self.TimeHour = int(Timer[0])
        self.TimeMinute = int(Timer[1])
        self.TimeSecond = int(Timer[2])
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
        """ Показать профиль босса """

        self.Read()
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
            Procent = (self.Health * 100) / self.MaxHealth
            WithOutProcent = 100 - Procent
            Red = 2.55
            Green = 255
            Blue = 80
            Red *= WithOutProcent
            Green -= Red
            ColorSlider = ( round(Red) , round(Green) , Blue )
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

        font = ImageFont.truetype("arial.ttf",60)
        _writeInPicture((150,500),f"Сложность : {self.Different}",font,draw,(100,5,9))

        font = ImageFont.truetype("arial.ttf",35)
        Damage = ReplaceNumber(self.Damage)
        _writeInPicture((150,550),f"Урон : {Damage}",font,draw,(255,127,127))

        font = ImageFont.truetype("arial.ttf",35)
        Armor = ReplaceNumber(self.Armor)
        _writeInPicture((400,550),f"Броня : {Armor}",font,draw,(127,127,255))
        
        BackGround.save("TheBoss.png")

        df = discord.File("TheBoss.png","TheBoss.png")

        return df

        pass
    def GetAttack(self,Player : C_Player,Damage : int):
        """ Получить атаку от босса """
        Embed = discord.Embed(
            title="Убийство босса",
            colour=discord.Colour(11653695)
        )
        if self.Status == "Life":
            Damage -= self.Armor
            self.Health -= Damage
            if self.Health <= 0:
                self.Status = "Dead"
                self.LastGetDamage = Damage
                self.Murder = Player.Name
                Player.Gold += self.Gold
                Player.Edit(
                    Edit = "Main",
                    Gold = Player.Gold
                )
                if self.Different == "Easy":
                    TypeItem = randomBool(0,1,1)
                    if TypeItem == True:
                        Names = [
                            Item.CreateName("Медное копье","Не крепкое, легко ломаемое копье, не наносит серьезного урона"),
                            Item.CreateName("Медный лук","Мягкий лук, из за чего не может нанести существенных повреждений"),
                            Item.CreateName("Медный кинжал","Слабое оружие, не наносит существенного повреждения"),
                            Item.CreateName("Медный нож","Слабое оружие, не наносит существенного повреждения"),
                            Item.CreateName("Медная рапира","Оружие средний дистанции, однако сделано из меди, и не наносит существенного повреждения"),
                        ]
                        self.GetItem = Player.AddInventor(
                            Type = Item.Types.Weapon(random.randint(500,3000),random.randint(300,700),None),
                            Name = Names[random.randint(0,len(Names) - 1)],
                            Class = Item.Classes.Первоначальный(),
                            ID=random.randint(1,9999999999),
                            Gold=0,
                            MaxGold = random.randint(1000,5000),
                            AllGold = 0)
                    else:
                        PossibleEquipment = ["Head","Body","Legs","Boot"]
                        RandomEquipment = PossibleEquipment[random.randint(0,len(PossibleEquipment) - 1)]
                        if RandomEquipment == "Head":
                            Names = [
                                Item.CreateName("Шляпа путешественика","Шляпа которая раньше пренадлежала путешественнику"),
                                Item.CreateName("Кепка","Защищает голову от солнца"),
                                Item.CreateName("Кожанный шлем","Защищает голову от незначительный повреждений"),
                                Item.CreateName("Колпак","Обычный колпак"),
                                Item.CreateName("Медный шлем","Легкий шлем, особо не защищает"),
                            ]
                            self.GetItem = Player.AddInventor(
                                Type = Item.Types.Equipment(random.randint(100,350),random.randint(75,100),RandomEquipment,None),
                                Name = Names[random.randint(0,len(Names) - 1)],
                                Class = Item.Classes.Первоначальный(),
                                ID=random.randint(1,9999999999),
                                Gold=0,
                                MaxGold = random.randint(400,1000),
                                AllGold = 0)
                        elif RandomEquipment == "Body":
                            Names = [
                                Item.CreateName("Кожанная кираса","Кираса которая защищает тело от слабых повреждений"),
                                Item.CreateName("Одежда путешественника","Одежда которая раньше пренадлежала путешественнику"),
                                Item.CreateName("Гражданская кофта","Кофта которую носят гражданские"),
                                Item.CreateName("Медная кираса","Легкая кираса, особо не защищает"),
                                Item.CreateName("Майка охотника","Майка которую носят все охотники"),
                            ]
                            self.GetItem = Player.AddInventor(
                                Type = Item.Types.Equipment(random.randint(800,1200),random.randint(300,350),RandomEquipment,None),
                                Name = Names[random.randint(0,len(Names) - 1)],
                                Class = Item.Classes.Первоначальный(),
                                ID=random.randint(1,9999999999),
                                Gold=0,
                                MaxGold = random.randint(600,1200),
                                AllGold = 0)
                        elif RandomEquipment == "Legs":
                            Names = [
                                Item.CreateName("Кожанные поножи","Тёплые поножи, не замедляющие движение"),
                                Item.CreateName("Брюки путешественника","Брюки которые пренадлежат путешественникам"),
                                Item.CreateName("Гражданские брюки","Брюки которые носят все гражданские"),
                                Item.CreateName("Медные поножи","Лёгкие поножи, не сковывающие движение"),
                            ]
                            self.GetItem = Player.AddInventor(
                                Type = Item.Types.Equipment(random.randint(600,1000),random.randint(300,350),RandomEquipment,None),
                                Name = Names[random.randint(0,len(Names) - 1)],
                                Class = Item.Classes.Первоначальный(),
                                ID=random.randint(1,9999999999),
                                Gold=0,
                                MaxGold = random.randint(550,1100),
                                AllGold = 0)
                        elif RandomEquipment == "Boot":
                            Names = [
                                Item.CreateName("Кожанные ботинки","Тёплые ботинки, не замедляющие движение"),
                                Item.CreateName("Сабатоны путешественника","Сабатоны которые пренадлежат путешественникам"),
                                Item.CreateName("Гражданские ботинки","Ботинки которые носят все гражданские"),
                                Item.CreateName("Медные ботинки","Лёгкие ботинки, не сковывающие движение"),
                            ]
                            self.GetItem = Player.AddInventor(
                                Type = Item.Types.Equipment(random.randint(300,500),random.randint(250,300),RandomEquipment,None),
                                Name = Names[random.randint(0,len(Names) - 1)],
                                Class = Item.Classes.Первоначальный(),
                                ID=random.randint(1,9999999999),
                                Gold=0,
                                MaxGold = random.randint(200,350),
                                AllGold = 0)
                elif self.Different == "Medium":
                    TypeItem = randomBool(0,1,1)
                    if TypeItem == True:
                        Names = [
                            Item.CreateName("Железное копье","Крепкое железное копье, такое есть у каждого умелого бойца"),
                            Item.CreateName("Лук","Ничем не примечательный лук"),
                            Item.CreateName("Железный кинжал","Кинжал который крайне популярен среди охотников"),
                            Item.CreateName("Железный меч","Среднестатистический клинок, не наносит колосального урона."),
                            Item.CreateName("Железный топор","Обычный топор, который можно взять в руки как оружие")
                        ]
                        self.GetItem = Player.AddInventor(
                            Type = Item.Types.Weapon(random.randint(5000,30000),random.randint(1000,3000),None),
                            Name = Names[random.randint(0,len(Names) - 1)],
                            Class = Item.Classes.Обычный(),
                            ID=random.randint(1,9999999999),
                            Gold=0,
                            MaxGold = random.randint(5000,15000),
                            AllGold = 0)
                    else:
                        Ring_ = randomBool(0,5,1)
                        if Ring == False:
                            PossibleEquipment = ["Head","Body","Legs","Boot"]
                            RandomEquipment = PossibleEquipment[random.randint(0,len(PossibleEquipment) - 1)]
                            if RandomEquipment == "Head":
                                Names = [
                                    Item.CreateName("Железный шлем","Шлем который защищает голову"),
                                    Item.CreateName("Защитный шлем","Защищает голову от прямых ударов"),
                                    Item.CreateName("Шлем стражника","Шлем который носят стражники")
                                ]
                                self.GetItem = Player.AddInventor(
                                    Type = Item.Types.Equipment(random.randint(1800,2200),random.randint(1000,2000),RandomEquipment,None),
                                    Name = Names[random.randint(0,len(Names) - 1)],
                                    Class = Item.Classes.Обычный(),
                                    ID=random.randint(1,9999999999),
                                    Gold=0,
                                    MaxGold = random.randint(2000,3000),
                                    AllGold = 0)
                            elif RandomEquipment == "Body":
                                Names = [
                                    Item.CreateName("Железная кираса","Кираса которая защищает тело от повреждений"),
                                    Item.CreateName("Защитная кираса","Кираса защищает тело от прямых попаданий"),
                                    Item.CreateName("Кираса стражника","Кираса которую носят все стражники"),
                                    Item.CreateName("Кольчуга","Легкая кольчуга, защищает от повреждений"),
                                    Item.CreateName("Мантия","Мантия которую носили волшебники"),
                                ]
                                self.GetItem = Player.AddInventor(
                                    Type = Item.Types.Equipment(random.randint(3000,4000),random.randint(2000,2500),RandomEquipment,None),
                                    Name = Names[random.randint(0,len(Names) - 1)],
                                    Class = Item.Classes.Обычный(),
                                    ID=random.randint(1,9999999999),
                                    Gold=0,
                                    MaxGold = random.randint(5000,8000),
                                    AllGold = 0)
                            elif RandomEquipment == "Legs":
                                Names = [
                                    Item.CreateName("Железные поножи","Железные поножи, которые защищают ноги"),
                                    Item.CreateName("Защитные поножи","Защитные поножи защищающие ноги от прямых попаданий"),
                                    Item.CreateName("Поножи стражника","Поножи которые носят все стражники"),
                                ]
                                self.GetItem = Player.AddInventor(
                                    Type = Item.Types.Equipment(random.randint(1000,1800),random.randint(900,1500),RandomEquipment,None),
                                    Name = Names[random.randint(0,len(Names) - 1)],
                                    Class = Item.Classes.Обычный(),
                                    ID=random.randint(1,9999999999),
                                    Gold=0,
                                    MaxGold = random.randint(4500,6000),
                                    AllGold = 0)
                            elif RandomEquipment == "Boot":
                                Names = [
                                    Item.CreateName("Железные сабатоны","Незначительно защитные сабатоны"),
                                    Item.CreateName("Защитные сабатоны","Значительно защитные сабатоны"),
                                    Item.CreateName("Сабатоны стражника","Сабатоны которые носят все стражники"),
                                    Item.CreateName("Ботинки мага","Лёгкие ботинки, которые носили маги"),
                                ]
                                self.GetItem = Player.AddInventor(
                                    Type = Item.Types.Equipment(random.randint(850,1000),random.randint(600,800),RandomEquipment,None),
                                    Name = Names[random.randint(0,len(Names) - 1)],
                                    Class = Item.Classes.Обычный(),
                                    ID=random.randint(1,9999999999),
                                    Gold=0,
                                    MaxGold = random.randint(3500,5000),
                                    AllGold = 0)
                        else:
                            Magic = [
                                {"Healing":{"Name":"Лечение","Description":"Каждая ваша атака исцеляет вас на 1% от максимального количества здоровья","PerLevel":"Лечение увеличивается на 1%","Level":random.randint(1,3)}},
                                {"Damage":{"Name":"Усиленный урон","Description":"Ваши удары наносят усиленный урон на 10%","PerLevel":"Урон увеличивается на 10%","Level":random.randint(1,3)}},
                                {"Shield":{"Name":"Поднять щиты","Description":"По вам приходит на 2% меньше урона","PerLevel":"Уменьшает получаемый урон на 2%","Level":random.randint(1,3)}},
                                {"BloodDust":{"Name":"Зажда крови","Description":"После убийства босса вы наносите на 5% больше урона. (Максимальная сила = 500%)","PerLevel":"Увеличивает урон на 5%","Level":random.randint(1,3)}},
                                {"Pacifist":{"Name":"Удар пацифиста","Description":"Каждые 10 минут урон увеличивается на 10%. Пропадает после атаки.","PerLevel":"Увеличивает прирост урона на 5%","Level":random.randint(1,3)}}
                                ]
                            self.GetItem = Player.AddInventor(
                                Type = Item.Types.Ring(Magic[random.randint(0,len(Magic) - 1)]),
                                Name = Item.CreateName("Магическое кольцо","Если экипировать то дает магический эффект"),
                                Class = Item.Classes.Обычный(),
                                ID=random.randint(1,9999999999),
                                Gold=0,
                                MaxGold = random.randint(50000000,500000000),
                                AllGold = 0)
                elif self.Different == "Hard":
                    TypeItem = randomBool(0,1,1)
                    if TypeItem == True:
                        Names = [
                            Item.CreateName("Платиновое копье","Копье которое обычно носит королевская стража"),
                            Item.CreateName("Эльфийский лук","Лук который был собран Эльфами"),
                            Item.CreateName("Кинжал тени","Кинжал который выдают войнам тени, за их подвиги"),
                            Item.CreateName("Секира","Оружие которое наносит ужасающий урон"),
                            Item.CreateName("Сияющий меч","На столько хорошо выкован, что слепит своим сиянием"),
                            Item.CreateName("Посох","Среднестатистический посох"),
                            Item.CreateName("Платиновый меч","Меч которое обычно экипированы герои")
                        ]
                        self.GetItem = Player.AddInventor(
                            Type = Item.Types.Weapon(random.randint(53000,80000),random.randint(7000,13000),None),
                            Name = Names[random.randint(0,len(Names) - 1)],
                            Class = Item.Classes.Редкий(),
                            ID=random.randint(1,9999999999),
                            Gold=0,
                            MaxGold = random.randint(80000,150000),
                            AllGold = 0)
                    else:
                        Ring_ = randomBool(0,5,1)
                        if Ring == False:
                            PossibleEquipment = ["Head","Body","Legs","Boot"]
                            RandomEquipment = PossibleEquipment[random.randint(0,len(PossibleEquipment) - 1)]
                            if RandomEquipment == "Head":
                                Names = [
                                    Item.CreateName("Платиновый шлем","Шлем сделаный из платины, отлично защищает голову"),
                                    Item.CreateName("Эльфийский шлем","Шлем выкованный Эльфами, отлично защищает голову"),
                                    Item.CreateName("Шлем тени","Шлем который выдают войнам тени, за их подвиги"),
                                    Item.CreateName("Шлем мага","Шлем который носят маги")
                                ]
                                self.GetItem = Player.AddInventor(
                                    Type = Item.Types.Equipment(random.randint(20000,30000),random.randint(10000,20000),RandomEquipment,None),
                                    Name = Names[random.randint(0,len(Names) - 1)],
                                    Class = Item.Classes.Редкий(),
                                    ID=random.randint(1,9999999999),
                                    Gold=0,
                                    MaxGold = random.randint(10000,20000),
                                    AllGold = 0)
                            elif RandomEquipment == "Body":
                                Names = [
                                    Item.CreateName("Платиновая кираса","Кираса сделаная из платины, отлично защищает тело"),
                                    Item.CreateName("Эльфийская кираса","Кираса выкованная Эльфами, отлично защищает тело"),
                                    Item.CreateName("Кираса тени","Кираса которую выдают войнам тени, за их подвиги"),
                                    Item.CreateName("Мантия мага","Мантия которую носят маги")
                                ]
                                self.GetItem = Player.AddInventor(
                                    Type = Item.Types.Equipment(random.randint(50000,150000),random.randint(30000,50000),RandomEquipment,None),
                                    Name = Names[random.randint(0,len(Names) - 1)],
                                    Class = Item.Classes.Редкий(),
                                    ID=random.randint(1,9999999999),
                                    Gold=0,
                                    MaxGold = random.randint(350000,500000),
                                    AllGold = 0)
                            elif RandomEquipment == "Legs":
                                Names = [
                                    Item.CreateName("Платиновые поножи","Поножи сделаные из платины, отлично защищают ноги"),
                                    Item.CreateName("Эльфийские поножи","Поножи выкованные Эльфами, отлично защищают ноги"),
                                    Item.CreateName("Поножи тени","Поножи которые выдают войнам тени, за их подвиги"),
                                ]
                                self.GetItem = Player.AddInventor(
                                    Type = Item.Types.Equipment(random.randint(35000,50000),random.randint(25000,30000),RandomEquipment,None),
                                    Name = Names[random.randint(0,len(Names) - 1)],
                                    Class = Item.Classes.Редкий(),
                                    ID=random.randint(1,9999999999),
                                    Gold=0,
                                    MaxGold = random.randint(350000,400000),
                                    AllGold = 0)
                            elif RandomEquipment == "Boot":
                                Names = [
                                    Item.CreateName("Платиновые сабатоны","Сабатоны сделаные из платины, отлично защищают ноги"),
                                    Item.CreateName("Эльфийские сабатоны","Сабатоны выкованные Эльфами, отлично защищают ноги"),
                                    Item.CreateName("Сабатоны тени","Сабатоны которые выдают войнам тени, за их подвиги")
                                ]
                                self.GetItem = Player.AddInventor(
                                    Type = Item.Types.Equipment(random.randint(30000,40000),random.randint(20000,25000),RandomEquipment,None),
                                    Name = Names[random.randint(0,len(Names) - 1)],
                                    Class = Item.Classes.Редкий(),
                                    ID=random.randint(1,9999999999),
                                    Gold=0,
                                    MaxGold = random.randint(300000,350000),
                                    AllGold = 0)
                        else:
                            Magic = [
                                {"Healing":{"Name":"Лечение","Description":"Каждая ваша атака исцеляет вас на 1% от максимального количества здоровья","PerLevel":"Лечение увеличивается на 1%","Level":random.randint(4,9)}},
                                {"Damage":{"Name":"Усиленный урон","Description":"Ваши удары наносят усиленный урон на 10%","PerLevel":"Урон увеличивается на 10%","Level":random.randint(4,9)}},
                                {"Shield":{"Name":"Поднять щиты","Description":"По вам приходит на 2% меньше урона","PerLevel":"Уменьшает получаемый урон на 2%","Level":random.randint(4,9)}},
                                {"BloodDust":{"Name":"Зажда крови","Description":"После убийства босса вы наносите на 5% больше урона. (Максимальная сила = 500%)","PerLevel":"Увеличивает урон на 5%","Level":random.randint(4,9)}},
                                {"Pacifist":{"Name":"Удар пацифиста","Description":"Каждые 10 минут урон увеличивается на 10%. Пропадает после атаки.","PerLevel":"Увеличивает прирост урона на 5%","Level":random.randint(4,9)}}
                                ]
                            self.GetItem = Player.AddInventor(
                                Type = Item.Types.Ring(Magic[random.randint(0,len(Magic) - 1)]),
                                Name = Item.CreateName("Магическое кольцо","Если экипировать то дает магический эффект"),
                                Class = Item.Classes.Редкий(),
                                ID=random.randint(1,9999999999),
                                Gold=0,
                                MaxGold = random.randint(50000000,500000000),
                                AllGold = 0)
                elif self.Different == "Hard+":
                    TypeItem = randomBool(0,1,1)
                    if TypeItem == True:
                        Names = [
                            Item.CreateName("Героическое копье","Копье которым пользуются герои. Наносит колосальные повреждения"),
                            Item.CreateName("Механический арбалет","Арболет который способен автоматически перезаряжаться."),
                            Item.CreateName("Кровопийца","Клинок который одним касанием способен вызвать кровотичение у жертвы"),
                            Item.CreateName("Гроза Драконов","Клинок который способен убить дракона"),
                            Item.CreateName("Пылающий Феникс","Клинок который словно окутывает свои жертвы пламенем"),
                            Item.CreateName("Жало","Клинок который светиться при орках"),
                            Item.CreateName("Убийца Мурлоков","Клинок который заколенный в боях против мурлоков")
                        ]
                        self.GetItem = Player.AddInventor(
                            Type = Item.Types.Weapon(random.randint(800000,9000000),random.randint(9000,33000),None),
                            Name = Names[random.randint(0,len(Names) - 1)],
                            Class = Item.Classes.Эпический(),
                            ID=random.randint(1,9999999999),
                            Gold=0,
                            MaxGold = random.randint(900000,9900000),
                            AllGold = 0)
                    else:
                        Ring_ = randomBool(0,5,1)
                        if Ring == False:
                            PossibleEquipment = ["Head","Body","Legs","Boot"]
                            RandomEquipment = PossibleEquipment[random.randint(0,len(PossibleEquipment) - 1)]
                            if RandomEquipment == "Head":
                                Names = [
                                    Item.CreateName("Героический шлем","Шлем которые носят все герои"),
                                    Item.CreateName("Магический шлем","Магический шлем, который неосязаем для своего владельца"),
                                    Item.CreateName("Шлем Хранителя","Шлем который носили прошлые Хранители"),
                                    Item.CreateName("Драконий Шлем","Шлем выкованный из Драконией чешуи")
                                ]
                                self.GetItem = Player.AddInventor(
                                    Type = Item.Types.Equipment(random.randint(1000000,2000000),random.randint(33000,50000),RandomEquipment,None),
                                    Name = Names[random.randint(0,len(Names) - 1)],
                                    Class = Item.Classes.Эпический(),
                                    ID=random.randint(1,9999999999),
                                    Gold=0,
                                    MaxGold = random.randint(900000,9900000),
                                    AllGold = 0)
                            elif RandomEquipment == "Body":
                                Names = [
                                    Item.CreateName("Героическая кираса","Кираса которую носят все герои"),
                                    Item.CreateName("Магическая кираса","Магическая Кираса, которая неосязаема для своего владельца"),
                                    Item.CreateName("Кираса Хранителя","Кираса которую носили прошлые Хранители"),
                                    Item.CreateName("Драконья кираса","Кираса выкованная из Драконией чешуи")
                                ]
                                self.GetItem = Player.AddInventor(
                                    Type = Item.Types.Equipment(random.randint(5000000,55000000),random.randint(300000,500000),RandomEquipment,None),
                                    Name = Names[random.randint(0,len(Names) - 1)],
                                    Class = Item.Classes.Эпический(),
                                    ID=random.randint(1,9999999999),
                                    Gold=0,
                                    MaxGold = random.randint(900000,9900000),
                                    AllGold = 0)
                            elif RandomEquipment == "Legs":
                                Names = [
                                    Item.CreateName("Героические поножи","Поножи которые носят все герои"),
                                    Item.CreateName("Магические поножи","Магические поножи, которые неосязаемы для своего владельца"),
                                    Item.CreateName("Поножи Хранителя","Поножи которые носили прошлые Хранители"),
                                    Item.CreateName("Драконье Поножи","Поножи выкованные из Драконией чешуи")
                                ]
                                self.GetItem = Player.AddInventor(
                                    Type = Item.Types.Equipment(random.randint(1000000,2000000),random.randint(33000,50000),RandomEquipment,None),
                                    Name = Names[random.randint(0,len(Names) - 1)],
                                    Class = Item.Classes.Эпический(),
                                    ID=random.randint(1,9999999999),
                                    Gold=0,
                                    MaxGold = random.randint(900000,9900000),
                                    AllGold = 0)
                            elif RandomEquipment == "Boot":
                                Names = [
                                    Item.CreateName("Героические сабатоны","Сабатоны которые носят все герои"),
                                    Item.CreateName("Магические сабатоны","Магические сабатоны, которые неосязаемы для своего владельца"),
                                    Item.CreateName("Сабатоны Хранителя","Сабатоны которые носили прошлые Хранители"),
                                    Item.CreateName("Драконье сабатоны","Сабатоны выкованные из Драконией чешуи")
                                ]
                                self.GetItem = Player.AddInventor(
                                    Type = Item.Types.Equipment(random.randint(800000,1000000),random.randint(33000,50000),RandomEquipment,None),
                                    Name = Names[random.randint(0,len(Names) - 1)],
                                    Class = Item.Classes.Эпический(),
                                    ID=random.randint(1,9999999999),
                                    Gold=0,
                                    MaxGold = random.randint(900000,9900000),
                                    AllGold = 0)
                        else:
                            Magic = [
                                {"Healing":{"Name":"Лечение","Description":"Каждая ваша атака исцеляет вас на 1% от максимального количества здоровья","PerLevel":"Лечение увеличивается на 1%","Level":random.randint(9,14)}},
                                {"Damage":{"Name":"Усиленный урон","Description":"Ваши удары наносят усиленный урон на 10%","PerLevel":"Урон увеличивается на 10%","Level":random.randint(9,14)}},
                                {"Shield":{"Name":"Поднять щиты","Description":"По вам приходит на 2% меньше урона","PerLevel":"Уменьшает получаемый урон на 2%","Level":random.randint(9,14)}},
                                {"BloodDust":{"Name":"Зажда крови","Description":"После убийства босса вы наносите на 5% больше урона. (Максимальная сила = 500%)","PerLevel":"Увеличивает урон на 5%","Level":random.randint(9,14)}},
                                {"Pacifist":{"Name":"Удар пацифиста","Description":"Каждые 10 минут урон увеличивается на 10%. Пропадает после атаки.","PerLevel":"Увеличивает прирост урона на 5%","Level":random.randint(9,14)}}
                                ]
                            self.GetItem = Player.AddInventor(
                                Type = Item.Types.Ring(Magic[random.randint(0,len(Magic) - 1)]),
                                Name = Item.CreateName("Магическое кольцо","Если экипировать то дает магический эффект"),
                                Class = Item.Classes.Эпический(),
                                ID=random.randint(1,9999999999),
                                Gold=0,
                                MaxGold = random.randint(50000000,500000000),
                                AllGold = 0)
                self.Edit(GetItem=self.GetItem)
            self.Edit(
                Health = self.Health,
                Status = self.Status,
                Murder = self.Murder,
                LastGetDamage = self.LastGetDamage,
                GetItem=self.GetItem
            )
        LastGetDamageReplace = ReplaceNumber(self.LastGetDamage)
        Gold = ReplaceNumber(self.Gold)
        Embed.add_field(
            name="Последний урон",
            value=LastGetDamageReplace,
            inline=False)
        Embed.add_field(
            name="Убийца",
            value=self.Murder,
            inline=False)
        Embed.add_field(
            name="Получено золотых",
            value=Gold,
            inline=False)
        Embed.add_field(
            name="Предмет",
            value=self.GetItem['Name']['Name'],
            inline=False)
        return self.Status, Embed
    async def Respawn(self):
        """ Респавнить босса """
        while True:
            self.Read()
            self.TimeMinute -= 5
            Creater = False
            if self.TimeMinute <= 0:
                if self.TimeHour > 0:
                    self.TimeHour -= 1
                    self.TimeMinute = 60
                elif self.TimeHour <= 0:
                    Creater = True
                    print("New")
                    self.Create()
            if Creater == False:
                self.Time = f"{self.TimeHour}:{self.TimeMinute}:{self.TimeSecond}"
                self.Edit(
                    Time=self.Time)
            await asyncio.sleep(300)

class Talant():
    """ Таланты """
    def __init__(self,Player : C_Player,Talant,MainName):
        self.MainName = MainName
        self.Name = Talant["Name"]
        self.Description = Talant["Description"]
        self.PerLevel = Talant["PerLevel"]

        self.Level = Talant["Level"]
        self.MaxLevel = Talant["MaxLevel"]

        self.Exp = Talant["Exp"]
        self.NeedExp = Talant["NeedExp"]

        self.Player = Player

        if self.Level >= self.MaxLevel:
            self.Ready = True
        else:
            self.Ready = False


        self.Lock = Talant["Lock"]

        self.NeedAt = Talant["NeedAt"]

    def UpgradeTalant(self):
        if self.MainName == "Heroic Level":
            self.Player.LevelUp(C_Player.mode.one)
            self.Player.Edit(
                Edit="Main",
                Strength = self.Player.Strength + 0.1,
                Agility = self.Player.Agility + 0.2,
                Intelligence = self.Player.Intelligence + 0.3,
                MaxHealth = self.Player.MaxHealth + 320,
                Exp = self.Player.Exp + 100)
    
    async def Update(self):
        while True:
            self.Player.Read()
            if self.Lock == 0:
                self.Exp += 60 + round(self.Player.Intelligence)
                if self.MainName != self.Player.TalantPicked: break
                if self.Exp >= self.NeedExp:
                    self.Exp -= self.NeedExp
                    if self.Level < self.MaxLevel:
                        self.Level += 1
                        UpgradeTalant()
                    else: break
                self.Player.UpdateTalant(Exp=self.Exp,Level=self.Level)
                await asyncio.sleep(0.1)
            else:
                Be = False
                for NeedAt in self.NeedAt:
                    for key in NeedAt.keys():
                        Requester = NeedAt[key]
                        NeedLevel = Requester["Level"]
                        Talant_ = self.Player.GetTalant(key)
                        if Talant_.Level < NeedLevel and Be == False:
                            Be = True

                            self.MainName = Talant_.MainName
                            self.Name = Talant_.Name
                            self.Description = Talant_.Description
                            self.PerLevel = Talant_.PerLevel

                            self.Level = Talant_.Level
                            self.MaxLevel = Talant_. MaxLevel

                            self.Exp = Talant_.Exp
                            self.NeedExp = Talant_.NeedExp

                            if self.Level >= Talant_.MaxLevel:
                                self.Ready = True
                            else:
                                self.Ready = False


                            self.Lock = Talant_.Lock

                            self.NeedAt = Talant_.NeedAt
                            print(f"{key} - не хватает уровня, берём этот талант")

                            self.Player.Edit(TalantPicked=key)

class Shop():
    """ Магазин """

    def __init__(self):
        pass
    def Buy(self,Player : C_Player,Product : str,Count : int):
        BuyCount = ReplaceNumber(Count)
        Embed = discord.Embed(
            title="Покупка предметов",
            description=f"Куплено {BuyCount} раз",
            colour=discord.Colour(8207801))
        
        if Product.upper() == "Лечение".upper():
            Cost = 15 * Count
            if int(Player.Gold) >= int(Cost):
                Heal = 3000 * Count
                Player.Gold -= Cost
                Player.Health += Heal
                if Player.Health > Player.MaxHealth: Player.Health = Player.MaxHealth
                Player.Edit(
                    Edit="Main",
                    Health=Player.Health,
                    Gold=Player.Gold)

                Gold = ReplaceNumber(Player.Gold)
                CostReplace = ReplaceNumber(Cost)
                HealReplace = ReplaceNumber(Heal)

                Embed.add_field(name="Золота осталось",value=Gold)
                Embed.add_field(name="Стоимость",value=f"{CostReplace} золотых")
                Embed.add_field(name="Лечение на ",value=f"{HealReplace} ед.",inline=False)
                return Embed
            else: raise Error("Не достаточно золота чтобы купить")
        elif Product.upper() == "Здоровье".upper():
            Cost = 100 * Count
            if int(Player.Gold) >= int(Cost):
                Max = 35 * Count
                Player.Gold -= Cost
                Player.MaxHealth += Max
                Player.Edit(
                    Edit="Main",
                    MaxHealth=Player.MaxHealth,
                    Gold=Player.Gold)
                Gold = ReplaceNumber(Player.Gold)
                CostReplace = ReplaceNumber(Cost)
                MaxReplace = ReplaceNumber(Max)
                Embed.add_field(name="Золота осталось",value=Gold)
                Embed.add_field(name="Стоимость",value=f"{CostReplace} золотых")
                Embed.add_field(name="Здоровье увеличино на ",value=f"{MaxReplace} ед.",inline=False)
                return Embed
            else: raise Error("Не достаточно золота чтобы купить")
        elif Product.upper() == "Урон".upper():
            Cost = 50 * Count
            if int(Player.Gold) >= int(Cost):
                Damage = 50 * Count
                Player.Gold -= Cost
                Player.Damage += Damage
                Player.Edit(
                    Edit="Main",
                    Damage=Player.Damage,
                    Gold=Player.Gold)
                Gold = ReplaceNumber(Player.Gold)
                CostReplace = ReplaceNumber(Cost)
                DamageReplace = ReplaceNumber(Damage)
                Embed.add_field(name="Золота осталось",value=Gold)
                Embed.add_field(name="Стоимость",value=f"{CostReplace} золотых")
                Embed.add_field(name="Урон увеличен на ",value=f"{DamageReplace} ед.",inline=False)
                return Embed
            else: raise Error("Не достаточно золота чтобы купить")
        elif Product.upper() == "Уровень".upper():
            Cost = 300 * Count
            if int(Player.Gold) >= int(Cost):
                Player.Gold -= Cost
                Player.LevelUp(Player.mode.multiply,count=Count)
                Gold = ReplaceNumber(Player.Gold)
                CostReplace = ReplaceNumber(Cost)
                Embed.add_field(name="Золота осталось",value=Gold)
                Embed.add_field(name="Стоимость",value=f"{CostReplace} золотых",inline=False)
                return Embed
            else: raise Error("Не достаточно золота чтобы купить")
        else: raise Error("Такого предмета нет")

if __name__ == "__main__":
    Iam = C_Player("KOT32500")

    # Iam.GetInventor()
    Gabriel_ = Gabriel()
    # Gabriel_.SearchInfo('убить')
    # for Items in range(15):
    #     Names = [
    #         Item.CreateName("Героическое копье","Копье которым пользуются герои. Наносит колосальные повреждения"),
    #         Item.CreateName("Механический арбалет","Арболет который способен автоматически перезаряжаться."),
    #         Item.CreateName("Кровопийца","Клинок который одним касанием способен вызвать кровотичение у жертвы"),
    #         Item.CreateName("Гроза Драконов","Клинок который способен убить дракона"),
    #         Item.CreateName("Пылающий Феникс","Клинок который словно окутывает свои жертвы пламенем"),
    #         Item.CreateName("Жало","Клинок который светиться при орках"),
    #         Item.CreateName("Убийца Мурлоков","Клинок который заколенный в боях против мурлоков")
    #     ]
    #     Iam.AddInventor(
    #         Type = Item.Types.Weapon(random.randint(800000,9000000),random.randint(9000,33000),None),
    #         Name = Names[random.randint(0,len(Names) - 1)],
    #         Class = Item.Classes.Эпический(),
    #         ID=random.randint(1,9999999999),
    #         Gold=0,
    #         MaxGold = random.randint(900000,9900000),
    #         AllGold = 0)






    pass