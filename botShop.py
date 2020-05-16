import discord
import BazaDate
from discord import user
import urllib
from urllib.request import urlopen
import time
import random
import botFunctions as Functions

internetWasOff = True

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
        print(f"Logged on as , {self.user} MODULE : botShop.py")
    async def on_message(self, message):
    # don't respond to ourselves
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