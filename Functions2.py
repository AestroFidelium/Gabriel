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
import discord
import datetime
import asyncio
import requests
import json
import time
import ast
from bs4 import BeautifulSoup
import pickle
import re
from sys import platform
import Items
import Talants
import threading
import Mobe
from Numbers import ReplaceNumber
from Numbers import Readable
import Effects

def Readable(n):
    s, *d = str(n).partition(".")
    r = ".".join([s[x-3:x] for x in range(-3, -len(s), -3)][::-1] + [s[-3:]])
    return "".join([r] + d)

def GetFromMessage(message : str,Znak : str):
    """ Получить выбранный объект в знаках 
        `Пример сообщения` : `Talant "Max Bonus"`
        
        `Команда` : `GetFromMessage('Talant "Max Bonus"','"')`
        `Возврат` : `Max Bonus` : `str`
    """

    message = message[message.find(Znak) + 1::]
    message = message[:message.find(Znak):]
    return message

def StrToDict(_str):
    """
    `str` : текст который нужно будет конвентировать в Dict
    """
    NwDict = ast.literal_eval(f'{_str}') ; NwDict = dict(NwDict)
    return NwDict

def SplitURL(URL):
    """ Сократить URL """
    with requests.Session() as Session:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 OPR/68.0.3618.191'
        }
        GetURL = Session.get(f'https://clck.ru/--?json=true&url={URL}',headers=headers)
        Json = GetURL.json()
        return Json[0]
class Error(BaseException):
    """ Ошибка """
    pass
class CommandError(Error):
    """ Ошибка в команде 
    Принимает в себя Сообщение, об ошибке, название команды, и правильное написание команды
    
    """

    def __init__(self,Message : str,Command : str,Correct : str):
        self.Message = Message
        self.Command = Command
        self.Correct = Correct

class Warn(Error):
    """ Предупреждение """
    def __init__(self,Message : str,Word : str,Warns : int,MaxWarns : int):
        self.Message = Message
        self.Word = Word
        self.Warns = Warns
        self.MaxWarns = MaxWarns

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

class C_Player():
    """ Игрок """
    class C_Everyday_bonus():
        def __init__(self):
            self.Day = 0
            self.Gold = 0
    def __init__(self,ID : int,Name : str):
        self.PATH_VERSION = "."
        self.ID = ID
        self.Name = Name
        
        self.Health       = 35
        self.MaxHealth    = 35
        
        self.Shield       = 0
        self.MaxShield    = 100

        self.Mana         = 100
        self.MaxMana      = 100
        
        self.Exp          = 0
        self.ExpRequest   = 500   # ExpRequest * Level = сколько требуется опыта для уровня
        self.Level        = 1
        self.MaxLevel     = 100
        self.Plus         = 1
        self.Damage       = 5
        self.WasMaxLevel  = 1
        self.LosedLevels  = 0    # Возможность набирать опыт дальше, но он не будет засчитыватся и куда либо использоватся, если не применить нужные вещи
        
        self.Gold        = 0
        self.Messages     = 1
        self.MaxGold      = 10000

        self.Strength     = 1.0
        self.Agility      = 1.0
        self.Intelligence = 1.0

        self.Class           = Ellipsis
        self.Room            = Room(self,0,Name)

        self.Everyday_bonus  = self.C_Everyday_bonus()

        self.Inventor        = []

        Your_first_things = Items.Your_first_things(self)

        self.Head = Your_first_things.Head()
        self.Body = Your_first_things.Body()
        self.Legs = Your_first_things.Legs()
        self.Boot = Your_first_things.Boots()
        self.Left_hand = Ellipsis
        self.Right_hand = Your_first_things.Blade()
        self.Ring_1 = Ellipsis
        self.Ring_2 = Ellipsis
        self.Ring_3 = Ellipsis
        self.Ring_4 = Ellipsis
        self.Ring_5 = Ellipsis

        self.Quests = []

        self.Talants = []
        self.TalantPicked = Ellipsis

        self.Heroic_Level             = Talants.Heroic_Level(self)
        self.More_Exp                 = Talants.More_Exp(self)
        self.More_Gold                = Talants.More_Gold(self)
        self.More_Damage              = Talants.More_Damage(self)
        self.More_Protect             = Talants.More_Protect(self)
        self.Passive_Generator        = Talants.Passive_Generator(self)
        self.Updater_Generator_Amount = Talants.Updater_Generator_Amount(self)
        self.Updater_Generator_Speed  = Talants.Updater_Generator_Speed(self)
        self.Cheater_Generator        = Talants.Cheater_Generator(self)
        self.Regeneration             = Talants.Regeneration(self)
        self.Regeneration_Amount      = Talants.Regeneration_Amount(self)
        self.Regeneration_Speed       = Talants.Regeneration_Speed(self)
        self.Cheater_Regeneration     = Talants.Cheater_Regeneration(self)
        self.Blacksmith               = Talants.Blacksmith(self)
        self.Immunity                 = Talants.Immunity(self)
        self.Immunity_from_poison     = Talants.Immunity_from_poison(self)
        self.Bonus                    = Talants.Bonus(self)
        self.Max_Bonus                = Talants.Max_Bonus(self)
        self.Spells                   = Talants.Spells(self)
        self.Berserk                  = Talants.Berserk(self)
        self.Invincible               = Talants.Invincible(self)
        self.Annihilator              = Talants.Annihilator(self)
        self.Repair                   = Talants.Repair(self)
        self.Both_hands_first         = Talants.Both_hands_first(self)
        self.Both_hands_two           = Talants.Both_hands_two(self)
        self.Both_hands_three         = Talants.Both_hands_three(self)
        self.Both_hands_master        = Talants.Both_hands_master(self)



        self.Mobe                     = Mobe.Training_dummy(self)


        self.Effects = list()
        





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
                "About me" : None,
                "ID" : None
            }
        }

        with open(f"./Stats/{self.ID}.txt","wb") as file:
            pickle.dump(self,file)
    

    def Update(self):
        pass


    def _Update(self):
        while True:
            self.Update()
            time.sleep(1)

    def Start(self):

        for Effect in self.Effects:
            Effect.Start()

        threading.Thread(target=self._Update,args=()).start()


    @staticmethod
    def Open(ID : int):
        """ Прочитать информацию об игроке """
        try:
            with open(f"./Stats/{ID}.txt","rb") as file:
                return pickle.load(file)
        except: raise FileExistsError("Пользователь не найден.")
    
    def Save(self):
        """ Сохранить информацию игрока """
        copy = self.Open(self.ID)
        try:
            with open(f"./Stats/{self.ID}.txt","wb") as file:
                pickle.dump(self,file)
        except BaseException as Err: 
            with open(f"./Stats/{self.ID}.txt","wb") as file:
                pickle.dump(copy,file)
            print(f"Не удалось сохранить \n [{Err}]")
    
        
    def GetTalants(self):
        """Получить таланты. Использовать всего 1 раз"""
        self.GetTalanted = list()
        for _Talant_ in self.Talants:
            _Talant = self.Talants[_Talant_]
            self.GetTalanted.append(Talant(self,_Talant,_Talant_))

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
                    raise CommandError(
                                Message="Не правильно указано куда именно следовало экипировать предмет",
                                Command = "Wear",
                                Correct = "Wear ID Where"
                                )
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
    def PickTalant(self,TalantName):
        try:
            self.Talants[TalantName]
            self.Edit(TalantPicked=TalantName)
        except:
            raise Error("Такого таланта не существует")
    def LevelUp(self,count : int = 1):
        """ Получить уровень. 
        Моды : (mode)
            mode.one : 
                Один уровень

            mode.multiply :
                Множество уровней
                требуется : count 
        """
        PlanCount = count
        if self.Level + count > self.MaxLevel: count = self.MaxLevel - self.Level
        if count <= 0: 
            self.LosedLevels += PlanCount
            return "Повысить уровень не удалось"

        self.Health += random.randint(55,100) * count
        self.MaxHealth += random.randint(55,100) * count
        if self.Health > self.MaxHealth:
            self.Health = self.MaxHealth
        self.Damage += random.randint(8,35) * count
        self.Level += 1 * count
        self.Exp = 0
        if self.Level > self.MaxLevel :
            self.Plus += self.Level - self.MaxLevel
            self.MaxLevel = self.Level
        self.Strength += 0.001 * count
        self.Agility += 0.002 * count
        self.Intelligence += 0.005 * count
    def LostLevel(self,count):
        """ Потерять уровень. """
        lostHealth = random.randint(55,100) * count
        self.MaxHealth -= lostHealth
        self.Health = self.MaxHealth
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
        self.Save()
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


        def WriteInCenter(content,Position : tuple,Draw : ImageDraw,Font,Fill):
            offset = Draw.textsize(str(content),font=Font)
            Draw.text(
                (Position[0] - (offset[0] / 2), 
                Position[1] - (offset[1] / 2)), 
                str(content),fill=Fill,font=Font)

        Main = Image.open("./Resurses/System/Profile.jpg")
        Draw = ImageDraw.Draw(Main)


        Font_Path = "./Resurses/System/FONT.otf"

        Font = ImageFont.truetype(Font_Path,72)
        

        Draw.text((86,31),self.Name,font=Font,fill=(138,166,255))



        Line = Image.open("./Resurses/System/Line.png")



        Procent = float((self.Exp * 100) / (self.ExpRequest * self.Level)) / 100
        EndPoint = 1015 * Procent
        if Procent < 0.1: EndPoint = 88
        Draw.line((83,276,EndPoint,276),fill=(255,248,149),width=48)

        Procent = float((self.Gold * 100) / self.MaxGold) / 100
        EndPoint = 645 * Procent
        if Procent < 0.1: EndPoint = 88
        Draw.line((88,451,EndPoint,451),fill=(255,248,149),width=29)






        WriteInCenter(round(self.Strength),(400,554),Draw,Font,(255,255,255))

        WriteInCenter(round(self.Agility),(571,650),Draw,Font,(255,255,255))

        WriteInCenter(round(self.Intelligence),(577,794),Draw,Font,(255,255,255))

        
        WriteInCenter(round(self.Level),(822,627),Draw,ImageFont.truetype(Font_Path,200),(255,255,255))

        WriteInCenter(round(self.Health),(177,1275),Draw,ImageFont.truetype(Font_Path,125),(255,255,255))

        WriteInCenter(round(self.Mana),(521,1275),Draw,ImageFont.truetype(Font_Path,125),(255,255,255))

        WriteInCenter(round(self.Damage),(869,1275),Draw,ImageFont.truetype(Font_Path,125),(255,255,255))
        
        WriteInCenter(f"{ReplaceNumber(self.Gold)} / {ReplaceNumber(self.MaxGold)}",(365, 451),Draw,ImageFont.truetype(Font_Path,50),(0,255,255))
        WriteInCenter(f"{ReplaceNumber(self.Exp)} / {ReplaceNumber(self.ExpRequest * self.Level)}",(549, 278),Draw,ImageFont.truetype(Font_Path,50),(0,255,255))


        Protect = self.MaxProtect()
        
        WriteInCenter(f"{ReplaceNumber(Protect)}",(265, 1051),Draw,ImageFont.truetype(Font_Path,50),(0,255,255))




        Main.save("StatsPl.png")
        df = discord.File("StatsPl.png","StatsPl.png")

        return df
    def GetInventor(self):
        """ Получить инвентарь в class Item """
        self.GetInventored = list()
        for item in self.Inventor:
            item = Item(self,item)
            self.GetInventored.append(item)
    def Attack(self,Target):
        """Атаковать указанную цель"""

        Count = int(Target.Level * 5)

        try: L_Damage = self.Left_hand.Attack(Target)
        except: L_Damage = None


        try: R_Damage = self.Right_hand.Attack(Target)
        except: R_Damage = None

        
        if Target.Health <= 0:
            self.Level_UP_From_Kill(Target)
        Target.Save()
        self.Save()
        return L_Damage , R_Damage
    def CheckEquipItem(self,Where):
        for item in self.GetInventored:
            if item.ID == self.Left_hand.ID:
                self.EquipmentItem(self.Left_hand.ID,Where)
    def RewriteItem(self,_Item):
        try:
            self.RemoveInventor(_Item.ID)
            self.AddInventor(
                Type=_Item.Type,
                Name=Item.CreateName(_Item.Name,_Item.Description),
                Class=_Item.Class,
                ID=_Item.ID,
                Gold=_Item.Gold,
                MaxGold=_Item.MaxGold,
                AllGold=_Item.AllGold,
                Magic=_Item.Magic
                )
        except: raise Error("Нет предмета")
    def MaxDamage(self, Target = None):
        """ Урон который наносит герой. """

        GetDamage = 1 + self.Damage
        # try: GetDamage += self.Left_hand.Attack(Target)
        # except: pass
        # GetDamage += self.Right_hand.Attack(Target)
        
        # GetDamage += GetDamage * ((5 * self.More_Damage.Level) / 100)

        # GetDamage *= self.Strength

        # GetDamage = round(GetDamage)
        
        # if random.randint(0,1000) <= self.Annihilator.Level:
        #     GetDamage *= 5

        # Procent = (self.Health * 100) / self.MaxHealth
        # Procent -= 100
        # Procent *= -1
        # GetDamage += GetDamage * ((Procent * self.Berserk.Level) / 100)


        return round(GetDamage)
    def MaxProtect(self):
        Protect = self.Head.Protect
        Protect += self.Body.Protect
        Protect += self.Legs.Protect
        Protect += self.Boot.Protect
        return round(Protect)
    def AddHealth(self,Amount : int):
        self.Health += Amount
        if self.Health > self.MaxHealth:
            self.Health = self.MaxHealth

        self.Edit(Edit="Main",Health=self.Health)
    def GetDamage(self,Amount : int):
        if getattr(self,"Invulnerability",None) is not None:
            if self.Invulnerability.Status:
                return 0
            
        Amount -= self.MaxProtect()
        if Amount < 0: Amount = 1
    
        self.Health -= Amount
        
        if self.Health <= 0:
            self.Death()

        try:
            self.Head.Break(1)
        except: pass
        try:
            self.Body.Break(1)
        except: pass
        try:
            self.Legs.Break(1)
        except: pass
        try:
            self.Boot.Break(1)
        except: pass

        self.Save()
        return Amount
    def Death(self):
        Count = int(self.Level / 5)
        self.LostLevel(Count)
    def GetExp(self,Amount : int):
        self.Exp += Amount
        if self.Exp >= self.Level * 500:
            self.LevelUp()
    def PlusUpgrade(self,Count : int, Name : str):
        if Name == "Сила":
            self.Plus -= Count
            Plus = 0.001 * Count
            self.Strength += Plus
            Answer = discord.Embed(
                title="Поинты талантов",
                description=f"Количество : {Count}\nУлучшается на : {Plus}\nТекущая Сила : {self.Strength}",
                colour=discord.Colour(14378289))
            self.Edit(
                Edit="Main",
                Strength=self.Strength,
                Plus=self.Plus)
        elif Name == "Ловкость":
            self.Plus -= Count
            Plus = 0.002 * Count
            self.Agility += Plus
            Answer = discord.Embed(
                title="Поинты талантов",
                description=f"Количество : {Count}\nУлучшается на : {Plus}\nТекущая Ловкость : {self.Agility}",
                colour=discord.Colour(8055946))
            self.Edit(
                Edit="Main",
                Agility=self.Agility,
                Plus=self.Plus)
        elif Name == "Интеллект":
            self.Plus -= Count
            Plus = 0.005 * Count
            self.Intelligence += Plus
            Answer = discord.Embed(
                title="Поинты талантов",
                description=f"Количество : {Count}\nУлучшается на : {Plus}\nТекущий Интеллект : {self.Intelligence}",
                colour=discord.Colour(8052972))
            self.Edit(
                Edit="Main",
                Intelligence=self.Intelligence,
                Plus=self.Plus)
        else:
            raise CommandError("Ошибка в команде","Talant Point","Talant Point Сила(Ловкость или Интеллект) Количество поинтов")
        return Answer
    async def Regeneration(self):
        while True:
            SpeedTalant = self.GetTalant('Regeneration Speed')
            AmountTalant = self.GetTalant('Regeneration Amount')
            Speed = 60 - SpeedTalant.Level
            Amount = 10 * AmountTalant.Level
            self.AddHealth(Amount)
            await asyncio.sleep(Speed)
    async def GeneratorExp(self):
        while True:
            Generator = self.GetTalant('Passive Generator')
            SpeedTalant = self.GetTalant('Updater Generator Amount')
            AmountTalant = self.GetTalant('Updater Generator Speed')
            Speed = 3600 - (60 * SpeedTalant.Level)
            Amount = 10 * AmountTalant.Level
            if Generator.Ready:
                self.GetExp(Amount)
            await asyncio.sleep(Speed)
    async def Repair(self):
        while True:
            Repair = self.GetTalant("Repair")

            try:
                self.Left_hand.ArmorEdit(self.Left_hand.Armor + 3 * Repair.Level)
                self.RewriteItem(self.Left_hand)
                self.EquipmentItem(self.Left_hand.ID,"Left_hand")
            except: pass
            try:
                self.Right_hand.ArmorEdit(self.Right_hand.Armor + 3 * Repair.Level)
                self.RewriteItem(self.Right_hand)
                self.EquipmentItem(self.Right_hand.ID,"Right_hand")
            except: pass
            try:
                self.Head.ArmorEdit(self.Head.Armor + 3 * Repair.Level)
                self.RewriteItem(self.Head)
                self.EquipmentItem(self.Head.ID,"Head")
            except: pass
            try:
                self.Body.ArmorEdit(self.Body.Armor + 3 * Repair.Level)
                self.RewriteItem(self.Body)
                self.EquipmentItem(self.Body.ID,"Body")
            except: pass
            try:
                self.Legs.ArmorEdit(self.Legs.Armor + 3 * Repair.Level)
                self.RewriteItem(self.Legs)
                self.EquipmentItem(self.Legs.ID,"Legs")
            except: pass
            try:
                self.Boot.ArmorEdit(self.Boot.Armor + 3 * Repair.Level)
                self.RewriteItem(self.Boot)
                self.EquipmentItem(self.Boot.ID,"Boot")
            except: pass

            await asyncio.sleep(600)
    def TalantUpdater(self):
        if self.TalantPicked is not Ellipsis:
            self.TalantPicked.Update(self,int(self.Intelligence))
    def Gold_Add(self,value : int):
        if self.Gold + value > self.MaxGold: self.Gold = self.MaxGold
        else: self.Gold += value
    def Exp_Add(self,value : int):
        if self.Exp + value >= self.ExpRequest * self.Level: self.LevelUp()
        else: self.Exp += value
    def Level_UP_From_Kill(self,Target):
        Value = round(Target.Level / 5)
        if Value > 0:
            self.LevelUp(Value)
    def __repr__(self):
        return f"""ID: {self.ID}        Name: `{self.Name}`\nStatictics:\nHealth: `{self.Health}`         MaxHealth: `{self.MaxHealth}`         Shield: `{self.Shield}`         MaxShield: `{self.MaxShield}`       Mana: `{self.Mana}`         MaxMana: `{self.MaxMana}`       Damage: `{self.Damage}`\nLeveling:\nLevel: `{self.Level}`           MaxLevel: `{self.MaxLevel}`         Exp: `{self.Exp}`           Plus: `{self.Plus}`\nEconomy:\nGold: `{self.Gold}`            Messages: `{self.Messages}`\nStatictics v2:\nStrength: `{self.Strength}`          Agility: `{self.Agility}`           Intelligence: `{self.Intelligence}`\nEquip:\nHead:[{self.Head}]\nBody:[{self.Body}]\nLegs:[{self.Legs}]\nBoots:[{self.Boot}]\nLeft hand:[{self.Left_hand}]\nRight hand:[{self.Right_hand}]\nRings:\n...1:[{self.Ring_1}]\n..2:[{self.Ring_2}]\n..3:[{self.Ring_3}]\n..4:[{self.Ring_4}]\n..5:[{self.Ring_5}]\nOther:\nQuests: `{self.Quests}`\nTalants: `{self.Talants}`\nTalant picked: `{self.TalantPicked}`\n\n"""


class Room():
    def __init__(self,
            Player     : C_Player,
            ID         : int, 
            Name       : str,
            Overwrites = Ellipsis):
        self.ID         = ID
        self.Name       = Name
        self.Overwrites = Overwrites
        self.Channel    = Ellipsis


class Gabriel():
    """ Габриэль """

    def __init__(self):
        self.Standart = {
            "Words" : []
        }

    class _Message():
        def __init__(self,Content : dict):
            self.Main = Content
            for key in Content.keys():
                self.Author = str(key)
            self.Content = self.ConvertToSimpleText(str(Content[self.Author]))

        def ConvertToSimpleText(self,Text : str) -> str:
            return str(SoMuchSpaces(re.sub(r"[^А-я]"," ",Text)))

    def ConvertToSimpleText(self,Text : str) -> str:
        return str(SoMuchSpaces(re.sub(r"[^А-я]"," ",Text)))


    def Message(self,CountMessages : int,ServerName : str,Mode : "Usual or D / B",GetMessage : str = None):
        """ Сообщение """
        ReturnMessage = ""
        self.GetMessages(ServerName)
        if CountMessages == 0: CountMessages = 1
        
        if Mode == "Usual":
            while len(ReturnMessage.split(" ")) < CountMessages:
                try:
                    message = self.GotMessages.pop(random.randint(0,len(self.GotMessages) - 1))
                except: raise Error("Габриэль знает слишко мало слов")
                for content in message.Content.split(" "):
                    if random.randint(0,1) == 1:
                        ReturnMessage += f"{content} "
                    elif random.randint(0,1) == 1:
                        message = self.GotMessages.pop(random.randint(0,len(self.GotMessages) - 1))
                        for content in message.Content.split(" "):
                            if random.randint(0,1) == 1:
                                ReturnMessage += f"{content} "
            return ReturnMessage.capitalize()
        elif Mode == "D":
            try:
                Title = ""
                while len(Title) <= random.randint(10,30):
                    Message = self.GotMessages.pop(random.randint(0,len(self.GotMessages) - 1))
                    _count = 0
                    
                    for content in Message.Content.split(" "):
                        if random.randint(0,3) != 1 or _count < 3:
                            if content != "" and content != " ":
                                Title += f"{content} "
                                _count += 1
                                _preCount = 0
                                if random.randint(0,3) != 1:
                                    Message = self.GotMessages.pop(random.randint(0,len(self.GotMessages) - 1))
                                    for content in Message.Content.split(" "):
                                        if random.randint(0,3) != 1 or _preCount < 3:
                                            if content != "" and content != " ":
                                                content = SoMuchSpaces(re.sub(r"[^А-я]"," ",content))
                                                Title += f"{content} "
                                                _preCount += 1

                ReturnMessage += Title.capitalize()
                
                # Поиск участников диалога

                Players = list()
                _count = 100
                while len(Players) < random.randint(2,5):
                    Message = self.GotMessages[random.randint(0,len(self.GotMessages) - 1)]
                    author = Message.Author
                    if len(author) >= 10: 
                        author = author[:10:]
                        author += "…"
                    if author not in Players:
                        Players.append(author)
                    _count -= 1
                    if _count <= 0: break
                OldSay = None
                NowSay = None
                for _ in range(CountMessages):
                    while OldSay == NowSay:
                        NowSay = Players[random.randint(0,len(Players) - 1)]
                    ReturnMessage += f"\n• {NowSay}: "
                    _count = 0
                    Content = ""
                    while len(Content) <= random.randint(10,30):
                        Message = self.GotMessages.pop(random.randint(0,len(self.GotMessages) - 1))
                        for content in Message.Content.split(" "):
                            if random.randint(0,3) != 1 or _count < 3:
                                if content != "" and content != " ":
                                    Content += f"{content} "
                                    _count += 1
                                    _preCount = 0
                                    if random.randint(0,3) != 1:
                                        Message = self.GotMessages.pop(random.randint(0,len(self.GotMessages) - 1))
                                        for content in Message.Content.split(" "):
                                            if random.randint(0,3) != 1 or _preCount < 3:
                                                if content != "" and content != " ":
                                                    Content += f"{content} "
                                                    _preCount += 1
                    Content = SoMuchSpaces(re.sub(r"[^А-я]"," ",Content))
                    ReturnMessage += Content.capitalize()
                    OldSay = NowSay
            except ValueError: 
                return ReturnMessage
            return ReturnMessage
        elif Mode == "A":
            if GetMessage:
                FoundList = list()
                SpliedList = list()

                class Message():
                    def __init__(self,Quest,Answer):
                        self.Quest = Quest
                        self.Answer = Answer
                    def __repr__(self):
                        rr = f"1: {self.Quest.Content}\n2: {self.Answer.Content}\n"
                        ll = "-" * len(rr)
                        return f"{rr}\n{ll}"
                
                def Search(message,GotMessages,index):
                    next_message = Ellipsis
                    for index2 in range(10):
                        try:
                            next_message = GotMessages[index + 1 + index2]
                        except: return next_message
                        if message.Author != next_message.Author:
                            return next_message
                
                for splied in GetMessage.split(" "):
                    if len(splied) >= 3:
                        SpliedList.append(splied)
                for index, message in enumerate(self.GotMessages):
                    for splied in SpliedList:
                        next_message = Search(message,self.GotMessages,index)
                        if message.Content.lower().find(splied.lower()) >= 0:
                            FoundList.append(Message(message,next_message))
                found = FoundList[random.randint(0,len(FoundList) - 1)]

                Main = ""
                for word in found.Answer.Content.split(" "):
                    if random.randint(1,3) == 3:
                        Main += f"{word} "
                    if random.randint(1,2) == 2:
                        new_line = self.GotMessages.pop(random.randint(0,len(self.GotMessages) - 1))
                        for word2 in new_line.Content.split(" "):
                            if random.randint(1,2) == 2:
                                Main += f"{word2} "
                    if len(Main.split(" ")) >= CountMessages: return Main.capitalize()
                while len(Main.split(" ")) < CountMessages:
                    try:
                        for word in Main.split(" "):
                            if random.randint(1,3) == 3:
                                new_line = self.GotMessages.pop(random.randint(0,len(self.GotMessages) - 1))
                                for word2 in new_line.Content.split(" "):
                                    if random.randint(1,2) == 2:
                                        Main += f"{word2} "
                                    if len(Main.split(" ")) >= CountMessages: return Main.capitalize()
                            if random.randint(1,2) == 2:
                                new_line = self.GotMessages.pop(random.randint(0,len(self.GotMessages) - 1))
                                if random.randint(1,3) == 3:
                                    Main += f"{word2} "
                                if len(Main.split(" ")) >= CountMessages: return Main.capitalize()
                    except: return Main.capitalize()
                return Main.capitalize()
        elif Mode == "C":
            message = self.GotMessages.pop(random.randint(0,len(self.GotMessages) - 1))
            author = f'"{message.Author}"'
            ReturnMessage = self.Message(CountMessages,ServerName,"Usual")
            return f'"{ReturnMessage}"\nСказал **{author}**'


    def Delete(self,Count : int,Server : str):
        self.Read(Server)
        try:
            for _ in range(Count):
                self.Words.remove(self.Words[-1])
            self.Stats.update({"Words":self.Words})
            with codecs.open(f"./Servers/{Server}/Words.txt","w",encoding='utf-8') as file:
                file.write(str(self.Stats))
            return discord.Embed(title="Амнезия",description=f"Габриэль забыла последние ({Count}) строчки")
        except:
            self.Stats.update({"Words":self.Words})
            with codecs.open(f"./Servers/{Server}/Words.txt","w",encoding='utf-8') as file:
                file.write(str(self.Stats))
            return discord.Embed(title="Амнезия",description=f"Габриэль забыла все сохраненные строчки в Гильдии: **{Server}**")

    def DeleteCur(self,Content,Server : str):
        self.Read(Server)
        self.Words.remove(Content)
        self.Stats.update({"Words":self.Words})
        with codecs.open(f"./Servers/{Server}/Words.txt","w",encoding='utf-8') as file:
                file.write(str(self.Stats))


    def Save(self,Content : str,Who : str,Server : str):
        """ Сохранить слова """
        self.Read(Server)
        if Content.find("http") == -1:
            appen = {Who:Content}
            if appen not in self.Words:
                self.Words.append(appen)
                self.Stats.update({"Words":self.Words})
                with codecs.open(f"./Servers/{Server}/Words.txt","w",encoding='utf-8') as file:
                    file.write(str(self.Stats))
    
    def Read(self,Server : str):
        """ Прочитать слова """
        
        try:
            with codecs.open(f"./Servers/{Server}/Words.txt","r",encoding='utf-8') as file:
                self.Stats = StrToDict(str(file.readline()))
                self.Words = self.Stats["Words"]
        except:
            with codecs.open(f"./Servers/{Server}/Words.txt","w",encoding='utf-8') as file:
                self.Stats = self.Standart
                self.Words = self.Stats["Words"]
                file.write(str(self.Stats))
    def GetMessages(self,Server : str):
        self.Read(Server)
        self.GotMessages = list()
        for Word in self.Words:
            self.GotMessages.append(self._Message(Word))
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

class C_Guild():
    def __init__(self,Client,GuildID : int,GuildName : str):
        self.PATH = f"./Servers/{GuildName}"
        self.Client = Client
        self.StandartStats = {
            "Moderators" : {
                "Bad Words" : ["gachi"],
                "Players with Warns" : {},
                "Max Warns" : 3,
                "Do" : "Say without the words"
            },
            "Rooms" : {
                "Save" : ["Создать комнату","Резерв","Музыка"],
                "General" : []
            },
            "NameToCreateRoom": "Создать комнату",
            "ChannelsForSaveWords" : [],
            "ChannelWithIgnoreCommand": [],
            "ChanceSays" : 35,
            "StandartWords" : (1,35),
            "IngoreMember" : [],
            "ID" : GuildID,
            "Name" : GuildName,
            "MainChannel" : None,
            "CreatedChannel" : None,
            "Speak" : True,
            "EveryTime" : 300
        }
        self.Main()
    
    async def CheckMessage(self,Message : discord.Message,Content : str,Member : discord.Member):
        """ Проверяет сообщения """

        Be = False
        for words in self.BadWords:
            if Content.upper().find(words.upper()) >= 0:
                Content = Content.upper().replace(words.upper(),"░" * int(len(words)))
                Be = True
        if Be == True:
            Content = Content.capitalize()
            try:
                WebhookThisChannel = await Message.channel.webhooks()
                WebhookThisChannel = WebhookThisChannel[0]

                await WebhookThisChannel.send(
                    content = Content,
                    username = Member.display_name,
                    avatar_url = Message.author.avatar_url)
            except:
                Channel = await self.Client.fetch_channel(Message.channel.id)
                avatar = "https://sun9-70.userapi.com/c851528/v851528376/11cba6/qenzOyjqwrU.jpg"
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 OPR/68.0.3618.197'
                    }
                Response = requests.get(avatar,headers=headers)
                WebhookThisChannel = await Channel.create_webhook(
                    name="Габриэль",
                    avatar=Response.content,
                    reason="Для работы с сообщениями, Габриэль нужен вебхук")
                await WebhookThisChannel.send(
                    content = Content,
                    username = Member.display_name,
                    avatar_url = Message.author.avatar_url)
            await Message.delete()
    def AddWord(self,Word):
        self.BadWords.append(Word)
        self.Moderators.update({"Bad Words":self.BadWords})
        self.Stats.update({"Moderators":self.Moderators})
        self.SaveStats()
    def RemoveWord(self,Word):
        try:
            self.BadWords.remove(Word)
            self.Moderators.update({"Bad Words":self.BadWords})
            self.Stats.update({"Moderators":self.Moderators})
            self.SaveStats()
        except:
            raise Error("Это слово и не шифровалось")

    def SaveStats(self):
        with codecs.open(f"{self.PATH}/Main.txt","w",encoding="utf-8") as file:
            file.write(str(self.Stats))
        self._selfStats()

    def _selfStats(self):
        self.Moderators = self.Stats['Moderators']
        self.Rooms = self.Stats['Rooms']
        self.ID = self.Stats["ID"]
        self.NameToCreateRoom = self.Stats["NameToCreateRoom"]
        self.ChannelsForSaveWords = self.Stats["ChannelsForSaveWords"]
        self.ChannelWithIgnoreCommand = self.Stats["ChannelWithIgnoreCommand"]
        self.ChanceSays = self.Stats["ChanceSays"]
        self.StandartWords = self.Stats['StandartWords']
        self.IngoreMember = self.Stats["IngoreMember"]
        self.Name = self.Stats["Name"]
        self.MainChannel = self.Stats["MainChannel"]
        self.CreatedChannel = self.Stats["CreatedChannel"]
        self.Speak = self.Stats['Speak']
        self.EveryTime = self.Stats['EveryTime']

        self.BadWords = self.Moderators['Bad Words']
        self.Players = self.Moderators['Players with Warns']
        self.MaxWarns = self.Moderators['Max Warns']
        self.Do = self.Moderators['Do']

        self.Save = self.Rooms['Save']
        self.General = self.Rooms['General']

    def Edit(self,**fields):
        self.Stats.update(fields)
        self.SaveStats()
        self._selfStats()

    def Main(self):
        try: os.makedirs(self.PATH)
        except: pass
        self.New = False
        try:
            with codecs.open(f"{self.PATH}/Main.txt","r",encoding="utf-8") as file:
                self.Stats = StrToDict(str(file.readline()))
        except:
            with codecs.open(f"{self.PATH}/Main.txt","w",encoding="utf-8") as file:
                self.New = True
                self.Stats = self.StandartStats
                file.write(str(self.Stats))
        self._selfStats()
    def AddChannel(self,ChannelID):
        if ChannelID not in self.ChannelsForSaveWords:
            self.ChannelsForSaveWords.append(ChannelID)
    async def Setup(self,Channel : discord.TextChannel):
        """ Установка Габриэль в Гильдию """
        Guild = await self.Client.fetch_guild(self.ID)
        self.MainChannel = Channel.id
        self.AddChannel(Channel.id)

        await Guild.create_voice_channel(name="Создать комнату")
        await Channel.send(embed=discord.Embed(title="Установка",description=f'`{Channel.name}` - Установлен как основной канал\nБыла создана голосовая комната с именем `Создать комнату`'))
        await Channel.send(embed=discord.Embed(
            title="Текущие настройки",
            description=f'Основной канал : `{self.MainChannel}`\nГолосовую комнату зайду когда будите в : `{self.NameToCreateRoom}`\nКаналы где я могу общаться с вами : `{self.ChannelsForSaveWords}`\nТекстовые каналы которые мне противны : `{self.ChannelWithIgnoreCommand}`\nШанс что я захочу ответить вам : `{self.ChanceSays}% / 100%`\nСколько слов я могу себе позволить? : `{self.StandartWords}`\nУчастники которые мне противны : `{self.IngoreMember}`\nID Гильдии : `{self.ID}`\nМогу я общаться, даже когда вы все молчите? : `{self.Speak}`\nОбщаться буду каждые : `{self.EveryTime} секунд`'))
        self.SaveStats()

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
        class Loli():
            """
            Сильнейший сет в игре
            Выпадает :
                Сет лоли
            Особенности : 
                Атакует. Имеет бронь.
            Время жизни : 0:20:00
            """
            pass
    def __init__(self):
        self.PATH_VERSION = "./Stats"
        self.Read()
        self._selfStats()
    
    def Create(self,
        Different : None = ["Easy","Easy","Easy","Easy","Easy","Medium","Medium","Medium","Medium","Hard","Hard","Hard","Hard+","Hard+"]):
        """ Создать нового босса """
        if isinstance(Different,list):
            Different = Different[random.randint(0,len(Different) - 1)]
        with codecs.open(f"{self.PATH_VERSION}/Boss/Boss.txt","w",encoding="utf-8") as file:
            BossImage = os.listdir(f"./Resurses/Bosses/{Different}/")
            BossImage = BossImage[random.randint(0,len(BossImage) - 1)]
            if Different == "Easy":
                MaxHealth = random.randint(8000000,500000000)
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
                MaxHealth = random.randint(500000000000,500000000000000)
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
                MaxHealth = random.randint(500000000000000000,500000000000000000000)
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
                MaxHealth = random.randint(500000000000000000000000000,500000000000000000000000000000000)
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
            elif Different == "Loli":
                MaxHealth = random.randint(
                    100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000,
                    10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)
                self.Stats = {
                    "Different" : "Loli",
                    "Image" : BossImage,
                    "Health" : MaxHealth,
                    "MaxHealth" : MaxHealth,
                    "Damage" : 1000000000000000000000000000000000000000000000000000000000000000000000000000000000,
                    "Armor" : 1000000000000000000000000000000000000000000000000000000000000000000000000000000000,
                    "Time" : "0:60:00",
                    "Murder" : None,
                    "Status" : "Life",
                    "LastGetDamage" : 0,
                    "GetItem" : None
                }
            file.write(str(self.Stats))
    
    def Read(self):
        """ Прочитать сохраненную информацию о боссе """

        try:
            with codecs.open(f"{self.PATH_VERSION}/Boss/Boss.txt","r",encoding='utf-8') as file:
                self.Stats = StrToDict(str(file.readline()))
        except: self.Create()
        self._selfStats()

    def Edit(self,**fields):
        """ Редактировать информацию о боссе """
        self.Stats.update(fields)
        with codecs.open(f"{self.PATH_VERSION}/Boss/Boss.txt","w",encoding="utf-8") as file:
            file.write(str(self.Stats))
    
    def _selfStats(self):
        self.Different = self.Stats["Different"]
        self.Image = self.Stats["Image"]
        self.Health = int(self.Stats["Health"])
        self.MaxHealth = int(self.Stats["MaxHealth"])
        self.Damage = int(self.Stats["Damage"])
        self.Armor = int(self.Stats["Armor"])
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
        if self.MaxHealth >= 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000:
            count = int(self.MaxHealth / 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)
            self.Gold += 500000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 * count
        elif self.MaxHealth >= 500000000000000000000000000:
            count = int(self.MaxHealth / 10000000000000000000000000)
            self.Gold += 50000000 * count
        elif self.MaxHealth >= 500000000000000000:
            count = int(self.MaxHealth / 10000000000000000)
            self.Gold += 1000000 * count
        elif self.MaxHealth >= 500000000000:
            count = int(self.MaxHealth / 10000000000)
            self.Gold += 100000 * count
        elif self.MaxHealth >= 8000000:
            count = int(self.MaxHealth / 100000)
            self.Gold += 1000 * count

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
    def GetAttack(self,Player : C_Player,Damage : int):
        """ Получить атаку от босса """
        Embed = discord.Embed(
            title="Убийство босса",
            colour=discord.Colour(11653695)
        )
        if self.Status == "Life":
            Damage -= self.Armor
            if Damage < 0: Damage = 1
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
                                Type = Item.Types.Equipment(random.randint(1000000,3500000),random.randint(75,100),RandomEquipment,None),
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
                            Type = Item.Types.Weapon(random.randint(500000000,30000000000),random.randint(1000000,300000),None),
                            Name = Names[random.randint(0,len(Names) - 1)],
                            Class = Item.Classes.Обычный(),
                            ID=random.randint(1,9999999999),
                            Gold=0,
                            MaxGold = random.randint(5000,15000),
                            AllGold = 0)
                    else:
                        Ring_ = randomBool(0,5,1)
                        if Ring_ == False:
                            PossibleEquipment = ["Head","Body","Legs","Boot"]
                            RandomEquipment = PossibleEquipment[random.randint(0,len(PossibleEquipment) - 1)]
                            if RandomEquipment == "Head":
                                Names = [
                                    Item.CreateName("Железный шлем","Шлем который защищает голову"),
                                    Item.CreateName("Защитный шлем","Защищает голову от прямых ударов"),
                                    Item.CreateName("Шлем стражника","Шлем который носят стражники")
                                ]
                                self.GetItem = Player.AddInventor(
                                    Type = Item.Types.Equipment(random.randint(1000800,22000000),random.randint(1000,2000),RandomEquipment,None),
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
                                    Type = Item.Types.Equipment(random.randint(30000000,40000000),random.randint(2000,2500),RandomEquipment,None),
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
                            Type = Item.Types.Weapon(random.randint(53000000000000,80000000000000),random.randint(7000,13000),None),
                            Name = Names[random.randint(0,len(Names) - 1)],
                            Class = Item.Classes.Редкий(),
                            ID=random.randint(1,9999999999),
                            Gold=0,
                            MaxGold = random.randint(80000,150000),
                            AllGold = 0)
                    else:
                        Ring_ = randomBool(0,5,1)
                        if Ring_ == False:
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
                                    Type = Item.Types.Equipment(random.randint(20000000000000,30000000000000),random.randint(10000,20000),RandomEquipment,None),
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
                                    Type = Item.Types.Equipment(random.randint(50000000000,150000000000),random.randint(30000,50000),RandomEquipment,None),
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
                                    Type = Item.Types.Equipment(random.randint(35000000000,50000000000),random.randint(25000,30000),RandomEquipment,None),
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
                                    Type = Item.Types.Equipment(random.randint(30000000000,40000000000),random.randint(20000,25000),RandomEquipment,None),
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
                            Type = Item.Types.Weapon(random.randint(8000000000000000000,90000000000000000000),random.randint(9000,33000),None),
                            Name = Names[random.randint(0,len(Names) - 1)],
                            Class = Item.Classes.Эпический(),
                            ID=random.randint(1,9999999999),
                            Gold=0,
                            MaxGold = random.randint(900000,9900000),
                            AllGold = 0)
                    else:
                        Ring_ = randomBool(0,5,1)
                        if Ring_ == False:
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
                                    Type = Item.Types.Equipment(random.randint(10000000000000000000,20000000000000000000),random.randint(33000,50000),RandomEquipment,None),
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
                                    Type = Item.Types.Equipment(random.randint(50000000000000000000,550000000000000000000),random.randint(300000,500000),RandomEquipment,None),
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
                                    Type = Item.Types.Equipment(random.randint(10000000000000000000,20000000000000000000),random.randint(33000,50000),RandomEquipment,None),
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
                                    Type = Item.Types.Equipment(random.randint(8000000000000000000,10000000000000000000),random.randint(33000,50000),RandomEquipment,None),
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
                elif self.Different == "Loli___offline":
                    Sword = Item.CreateName("Лолирд","Был получен после победы над Лоли")
                    
                    self.GetItem = Player.AddInventor(
                        Type = Item.Types.Weapon(random.randint(
                            10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000,
                            100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
                            ),random.randint(500,900),None),
                        Name = Sword,
                        Class = Item.Classes.Лоли(),
                        ID=random.randint(1,99999999999),
                        Gold=0,
                        MaxGold = random.randint(1,2),
                        AllGold = 0)
                    PossibleEquipment = ["Head","Body","Legs","Boot"]
                    for RE in PossibleEquipment:
                        if RE == "Head":
                            _Item = Item.CreateName("Лолихерд","Шапка Лоли")
                        elif RE == "Body":
                            _Item = Item.CreateName("Лолиберд","Майка Лоли")
                        elif RE == "Legs":
                            _Item = Item.CreateName("Лолиленг","Юбка Лоли")
                        elif RE == "Boot":
                            _Item = Item.CreateName("Лолибуут","Милые ботинки")
                        self.GetItem = Player.AddInventor(
                            Type = Item.Types.Equipment(random.randint(
                                100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000,
                                100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000),random.randint(33000,50000),RandomEquipment,None),
                            Name = _Item,
                            Class = Item.Classes.Лоли(),
                            ID=random.randint(1,9999999999),
                            Gold=0,
                            MaxGold = random.randint(1,2),
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
        try:
            Embed.add_field(
                name="Предмет",
                value=self.GetItem['Name']['Name'],
                inline=False)
        except:
            Embed.add_field(
                name="Предмет",
                value="Босс не убит",
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
        # if self.Name == "Талант не выбран": return
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
            self.Player.LevelUp()
            self.Player.Edit(
                Edit="Main",
                Strength = self.Player.Strength + 0.1,
                Agility = self.Player.Agility + 0.2,
                Intelligence = self.Player.Intelligence + 0.3,
                MaxHealth = self.Player.MaxHealth + 320,
                Exp = self.Player.Exp + 100)
    
    def Edit(self,Talant_):
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
    
    async def Update(self):
        while True:
            try:
                self.Player.Read()
                self.Edit(self.Player.GetTalant(self.Player.TalantPicked))
                if self.Lock == 0:
                    if self.Level < self.MaxLevel:
                        self.Exp += int(round(self.Player.Intelligence) * 60)
                        if self.Exp >= self.NeedExp:
                            self.Exp -= self.NeedExp
                            self.Level += 1
                            self.UpgradeTalant()
                        self.Player.UpdateTalant(Exp=self.Exp,Level=self.Level)
                        await asyncio.sleep(60)
                    else:
                        await asyncio.sleep(5)
                else:
                    
                    Be = False
                    for NeedAt in self.NeedAt:
                        if isinstance(NeedAt,str) == False:
                            for key in NeedAt.keys():
                                Requester = NeedAt[key]
                                NeedLevel = Requester["Level"]
                                Talant_ = self.Player.GetTalant(key)
                                if Talant_.Level < NeedLevel and Be == False:
                                    Be = True

                                    self.Edit(Talant_)

                                    self.Player.Edit(TalantPicked=key)
                        else:
                            Requester = self.NeedAt[NeedAt]
                            NeedLevel = Requester["Level"]
                            Talant_ = self.Player.GetTalant(NeedAt)
                            if Talant_.Level < NeedLevel and Be == False:
                                Be = True

                                self.Edit(Talant_)

                                self.Player.Edit(TalantPicked=key)
                    if Be == False:
                        self.Player.UpdateTalant(Lock=0)
                    await asyncio.sleep(1)
            except BaseException as Error:
                await asyncio.sleep(1)
                print(f"{self.Player.Name} ERROR WITH TALANTS \n{Error}")

    def __str__(self):
        dct = {
            "MainName":self.MainName,
            "Name": self.Name,
            "Description": self.Description,
            "PerLevel" : self.PerLevel,
            "Level": self.Level,
            "MaxLevel" : self.MaxLevel,
            "Exp" : self.Exp,
            "NeedExp" : self.NeedExp,
            "Player" : self.Player.Name,
            "Ready" : self.Ready,
            "Lock" : self.Lock,
            "NeedAt" : self.NeedAt
                }
        return str(dct)
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
                Player.Edit(
                    Edit="Main",
                    Gold=Player.Gold)
                Player.LevelUp(Count)
                Gold = ReplaceNumber(Player.Gold)
                CostReplace = ReplaceNumber(Cost)
                Embed.add_field(name="Золота осталось",value=Gold)
                Embed.add_field(name="Стоимость",value=f"{CostReplace} золотых",inline=False)
                return Embed
            else: raise Error("Не достаточно золота чтобы купить")
        else: raise Error("Такого предмета нет")


class MiniGame():
    """ Мини игры """

    class Race():
        """ Скачки """

        def __init__(self):
            # self.Client = Client
            self.Images = list()
            self.StandartStats = {
                "Timer" : "600",
                "Rates" : {
                    1:[],
                    2:[],
                    3:[],
                    4:[],
                    5:[]
                    }
            }
            self.Read()
        
        def Read(self):
            try:
                with codecs.open(f"./Resurses/Race.txt","r",encoding="utf-8") as file:
                    self.Stats = StrToDict(str(file.readline()))
            except:
                with codecs.open(f"./Resurses/Race.txt","w",encoding="utf-8") as file:
                    self.Stats = self.StandartStats
                    file.write(str(self.Stats))
            self._selfStats()
        
        def End(self):
            with codecs.open(f"./Resurses/Race.txt","w",encoding="utf-8") as file:
                self.Stats = self.StandartStats
                file.write(str(self.Stats))
            self._selfStats()

        def Start(self):
            self.Horses = [
                self.Horse(random.randint(10,30),100,1),
                self.Horse(random.randint(10,30),200,2),
                self.Horse(random.randint(10,30),300,3),
                self.Horse(random.randint(10,30),400,4),
                self.Horse(random.randint(10,30),500,5)]

            while True:
                BackGround = Image.new('RGB', (600, 600), (54, 57, 63))
                for horse in self.Horses:
                    horse.Run()
                    BackGround.paste(horse.Image.convert("RGB"),(horse.PositionX,horse.PositionY),horse.Image)
                    self.Images.append(BackGround)
                    if horse.PositionX >= 600: 
                        return
        def Winning(self):
            Embed = discord.Embed(title="Итоги скачек",colour=discord.Colour(10240064))
            
            Positions = {}
            for horses in self.Horses:
                Positions.update({horses.PositionX:horses})

            TOP = 5
            Be = False
            for sort in sorted(Positions):
                horses = Positions[sort]
                horses.TOP = TOP
                for Player in self.Rates[horses.ID]:
                    for PlayerName in Player.keys():
                        Gold = int(Player[PlayerName])
                        if TOP == 1: Multiply = 2.25
                        elif TOP == 2: Multiply = 1.85
                        elif TOP == 3: Multiply = 1.0
                        elif TOP == 4: Multiply = 0.5
                        elif TOP == 5: Multiply = 0.0
                        Player = C_Player(PlayerName)
                        Player.Gold += Gold * Multiply
                        Player.Edit(Edit="Main",Gold=Player.Gold)
                        Be = True
                        Embed.add_field(name=Player.Name,value=f"х{Multiply} за {TOP} место")
                TOP -= 1

            self.Images[0].save(
                f'./Resurses/Race.gif',
                save_all=True,
                append_images=self.Images[1:],
                duration=75,
                loop=0)
            self.End()
            if Be == False:
                return "Nothing"
            return Embed

        def Edit(self,**fields):
            self.Stats.update(fields)
            with codecs.open(f"./Resurses/Race.txt","w",encoding="utf-8") as file:
                file.write(str(self.Stats))
        
        def _selfStats(self):
            self.Timer = self.Stats['Timer']
            self.Rates = self.Stats['Rates']

        def AddRate(self,Player : C_Player,Number : int,Gold : int):
            """ Ставка """
            if Player.Gold >= Gold:
                self.Rates[Number].append({Player.Name:Gold})
                Embed = discord.Embed(title="Ставка",description=f"{Gold} золотых")
                Player.Gold -= Gold
                Player.Edit(Edit="Main",Gold=Player.Gold)
            elif Player.Gold > 0: 
                self.Rates[Number].append({Player.Name:Player.Gold})
                Embed = discord.Embed(title="Ставка",description=f"Не достаточно золота на всю ставку, из за чего поставилось всего \n{Player.Gold} золотых")
                Player.Gold = 0
                Player.Edit(Edit="Main",Gold=Player.Gold)
            else:
                raise Error("У вас недостаточно золота чтобы сделать минимальную ставку в 1 золотую.")
            with codecs.open(f"./Resurses/Race.txt","w",encoding="utf-8") as file:
                file.write(str(self.Stats))
            return Embed
        
        async def Main(self,Client):
            """ Основная функция """

            while True:
                try:
                    Channel = await Client.fetch_channel(629267102070472714)
                    self.Start()
                    Embed = self.Winning()
                    if isinstance(Embed,str) == False:
                        file = discord.File("./Resurses/Race.gif","Race.gif")
                        await Channel.send(file=file,embed = Embed)

                        Embed = discord.Embed(title="Ставки принимаются",description="Скоро начнуться скачки, успейте поставить ставку на победителя!",colour=discord.Colour(5683293))
                        await Channel.send(embed=Embed)
                        self.End()
                except BaseException as Error:
                    print(Error)
                await asyncio.sleep(600)

        class Horse():
            def __init__(self,Speed : int,PositionY,ID):
                self.Speed = Speed
                self.Image = Image.open(f"./Resurses/System/Horse.png")
                self.Image = self.Image.resize((100,100))
                self.PositionX = 0
                self.PositionY = PositionY
                self.ID = ID
                self.TOP = 6
            def Run(self):
                self.PositionX += self.Speed
                self.Speed = random.randint(1,250)


class C_Color():
    def __init__(self,Color : tuple = (0,0,0)):
        self.Color = Color

    def Create(self):
        BackGround = Image.new("RGBA",(1000,1000),(0,0,0,0))
        Draw = ImageDraw.Draw(BackGround)
        Draw.ellipse((0,0,1000,1000),fill=self.Color)
        return BackGround


async def Notification(Function,Timer : int,End : "Loop or off",**fields):
    """ Поставить фунцию на уведомление. Чтобы выключить должен получить с функции слово NoNotification = True """
    
    if End == "Loop":
        while True:
            Function(fields)
            await asyncio.sleep(Timer)
    elif End == "off":
        Function(fields)


async def MemberMuted(Message : discord.Message,Content : str,Member : discord.Member,Client):
    for words in Content:
        Content = Content.replace(words,"░" * int(len(words)))
    Content = Content.capitalize()
    try:
        WebhookThisChannel = await Message.channel.webhooks()
        WebhookThisChannel = WebhookThisChannel[0]

        await WebhookThisChannel.send(
            content = Content,
            username = Member.display_name,
            avatar_url = Message.author.avatar_url)
    except:
        Channel = await Client.fetch_channel(Message.channel.id)
        avatar = "https://sun9-70.userapi.com/c851528/v851528376/11cba6/qenzOyjqwrU.jpg"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 OPR/68.0.3618.197'
            }
        Response = requests.get(avatar,headers=headers)
        WebhookThisChannel = await Channel.create_webhook(
            name="Габриэль",
            avatar=Response.content,
            reason="Для работы с сообщениями, Габриэль нужен вебхук")
        await WebhookThisChannel.send(
            content = Content,
            username = Member.display_name,
            avatar_url = Message.author.avatar_url)
        await Message.delete()

def NowTime():
    Time = int(time.strftime("%H%M%S"))
    return Time

def MessageReplaces(Content : str,replaces : list):
    """ Заменить """
    _Content = Content
    for repl in replaces:
        _Content = _Content.replace(repl,"")
    return _Content


def Debuger(arg,Correct : "Класс ожидаемого объекта"):
    """ Более подробное описание возникновения ошибки и её дальнейшее исправление """
    arg_type = str(type(arg))
    arg_type = arg_type.split("<class")[-1]
    arg_type = arg_type.split(">")[0]

    Correct_type = str(Correct)
    Correct_type = Correct_type.split("<class")[-1]
    Correct_type = Correct_type.split(">")[0]

    if isinstance(arg,Correct) == False:
        return f"Получен неверный аргумент{arg_type}. Ожидался аргумент{Correct_type}"


def rgbToColor(r, g, b):
    return (r << 16) + (g << 8) + b

def colorToRGB(c):
    r = c >> 16
    c -= r * 65536
    g = c / 256
    c -= g * 256
    b = c

    return (round(r), round(g), round(b))

def ClearConsole():
    if platform == "win32":
        os.system('cls')
    elif platform == "linux":
        os.system('clear')

def SoMuchSpaces(Message : str) -> str:
    Return = ""
    for Mess in re.split(r"[\b\s]",Message):
        if Mess != "": Return += f"{Mess} "
    return Return[:-1:]

if __name__ == "__main__":
    ClearConsole()
    lll = "- - - - " * 10
    try:
        Iam = C_Player.Open(414150542017953793)
    except: Iam = C_Player(414150542017953793,"Aestro Fidelium")

    try: Gab = C_Player.Open(656808327954825216)
    except: Gab = C_Player(656808327954825216,"Габриэль")

    Iam.Start()
    Gab.Start()

    print(lll)

    print(Iam.Effects)

    # for _ in range(1000):
    #     ClearConsole()
    #     print(Iam.GetDamage(1000))
    #     print(Iam.Health)
    #     print(Iam.Effects)
    #     time.sleep(1)
    
    


    if getattr(Iam,"Invulnerability",None) is None:
        Ef = Effects.Invulnerability(Iam)
        Iam.Effects.append(Ef)
        Iam.Invulnerability = Ef
    else:
        Iam.__getattribute__("Invulnerability").Status = True
    


    Gab.Save()
    Iam.Save()