import discord
import BazaDate
from discord import user
import urllib
from urllib.request import urlopen
import time
import random

internetWasOff = True
IntCurExp = 0
IntCurLvl = 0
IntMaxHealth = 0
IntCurHealth = 0
IntMaxDamage = 0
Description = ""
ln = "\n"
FarmExp = ""



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
        print('Logged on as', self.user)
    async def on_message(self, message):
    # don't respond to ourselves
        if message.author == self.user:
            pass
        UserName_ = message.author.name
        ln = "\n"
        IntCurExp = 0
        IntCurLvl = 0
        IntMaxHealth = 0
        IntCurHealth = 0
        IntMaxDamage = 0
        Description = ""
        msg =  message.content
        #print(msg)
        msgSP = msg.split()
        CurCommand = ""

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





        try:
            StatsRd = open("StatsPlayer_" + UserName_ + ".txt","r") #Открывае поток файлов, на чтение
            try:
                CurExp = StatsRd.readline() #Читаем 1 строчку, где храниться опыт
                IntCurExp = int(CurExp)
                CurLvl = StatsRd.readline() #Читаем 2 строчку, где храниться уровень
                IntCurLvl = int(CurLvl)
                _readline = StatsRd.readline() #Читаем 2 строчку, где храниться уровень
                IntMaxHealth = int(_readline)
                _readline = StatsRd.readline() #Читаем 2 строчку, где храниться уровень
                IntCurHealth = int(_readline)
                _readline = StatsRd.readline()
                IntMaxDamage = int(_readline)
                _readline = StatsRd.readline()
                Description = str(_readline)
            except ValueError:
                print("Статистика поврежденна, и сброшена " + UserName_)
                IntCurExp = 0
                IntCurLvl = 0
                IntMaxDamage = 0
                channelSendMyMessage = self.get_channel(627140104988917789) #Получаем ID канала : Разработка-Габриэль
                await channelSendMyMessage.send("Статистика повреждена, и сброшена " + str(message.author.mention)) #Отправляем сообщение, о том, что аккаунт был успешно создан
            

            StatsRd.close() #закрываем поток файлов

            StatsWr = open("StatsPlayer_" + UserName_ + ".txt","w") #Открываем поток файлов, на редактирование
            #print(IntCurExp)
            IntCurExp += int(1) #Добавляем 1 ед. опыта, за каждое сообщение
            if IntCurExp >= IntCurLvl * 5: #Система уровня. Если опыта больше чем уровень * 5, убирают опыт, и дают уровень
                IntCurLvl += 1
                IntMaxHealth += 10
                IntCurHealth += 10
                IntMaxDamage += random.randint(1,35)
                if ((IntCurHealth + 5) < (IntMaxHealth)):
                    IntCurHealth += 5
                else:
                    IntCurHealth = IntMaxHealth
                IntCurExp = 0

            ln = "\n" #Перенос строки
            StatsWr.write(str(IntCurExp) + ln + str(IntCurLvl) + ln + str(IntMaxHealth) + ln + str(IntCurHealth) + ln + str(IntMaxDamage) + ln + Description) #Записываем опыт в 1 строчку, а уровень во 2
            StatsWr.close() #Закрываем поток файлов
        except FileNotFoundError: #Если файл был не найден, значит это первое сообщение пользователя
            print("Создался новый аккаунт с ником : " + UserName_)
            StatsWr = open("StatsPlayer_" + UserName_ + ".txt","w")
            ln = "\n" #Перенос строки
            IntCurExp = 0 #Значения по 0
            IntCurLvl = 0 #Значение по 0
            IntMaxHealth = 0
            IntCurHealth = 0
            IntMaxDamage = 0
            StatsWr.write(str(IntCurExp) + ln + str(IntCurLvl) + ln + str(IntMaxHealth) + ln + str(IntCurHealth) + ln + str(IntMaxDamage) + ln + Description) #Записываем все значения
            StatsWr.close() #Закрываем поток
            channelSendMyMessage = self.get_channel(627140104988917789) #Получаем ID канала : Разработка-Габриэль
            await channelSendMyMessage.send("Успешно создался новый аккаунт, для игрока " + str(UserName_)) #Отправляем сообщение, о том, что аккаунт был успешно создан
            

        if CurCommand == 'Ы':
            await message.channel.send("ЫАЫ")

        if (CurCommand == 'PROFILE') or (CurCommand == 'P') or (CurCommand == 'П') or (CurCommand == 'ПРОФИЛЬ'):
            if CurCommandPlayer == "":
                #Emb = discord.Embed( title = "{}".format(message.author.mention))
                Emb = discord.Embed( title = message.author.name)
                Emb.add_field(name = 'Могущество : ',value = str(IntCurLvl) + " лвл.")
                LevelingSystem = IntCurLvl * 5
                Emb.add_field(name = 'Опыт : ',value = str(IntCurExp) + " ед. / " + str(LevelingSystem) + " ед.",inline = False)
                Emb.add_field(name = 'Здоровье : ',value = str(IntCurHealth) + " ед. / " + str(IntMaxHealth) + " ед.",inline = False)
                Emb.add_field(name = 'Максимальный урон : ',value = str(IntMaxDamage) + " ед.",inline = False)

                if Description != "":
                    if (Description == "God") or (Description == "Divine"):
                        Emb.add_field(name= "Ранг : ",value = "Божественный")
                    elif Description == "Master":
                        Emb.add_field(name= "Ранг : ",value = "Мастер")
                    elif Description == "Boss":
                        Emb.add_field(name= "Ранг : ",value = "Босс")
                    elif Description == "Diamond":
                        Emb.add_field(name= "Ранг : ",value = "Алмаз")
                    elif Description == "Platinum":
                        Emb.add_field(name= "Ранг : ",value = "Платина")
                    elif Description == "Gold":
                        Emb.add_field(name= "Ранг : ",value = "Золото")
                    elif Description == "Silver":
                        Emb.add_field(name= "Ранг : ",value = "Серебро")
                    elif Description == "Bronze":
                        Emb.add_field(name= "Ранг : ",value = "Бронза")


                await message.channel.send(embed = Emb)

        if (CurCommand == "ATTACK") or (CurCommand == "A") or (CurCommand == "А") or (CurCommand == "АТАКА") or (CurCommand == "АТАКОВАТЬ") or (CurCommand == "АТАКУЮ"):
            MyStatsRd = open("StatsPlayer_" + UserName_ + ".txt","r") #Открывае поток файлов, на чтение
            try:
                StatsRd = open("StatsPlayer_" + CurCommandPlayer + ".txt","r") #Открывае поток файлов, на чтение
                try:
                    _readline = StatsRd.readline()
                    IntCurExp = int(_readline)

                    _readline = StatsRd.readline()
                    IntCurLvl = int(_readline)

                    _readline = StatsRd.readline()
                    IntMaxHealth = int(_readline)

                    _readline = StatsRd.readline()
                    IntCurHealth = int(_readline)

                    _readline = StatsRd.readline()
                    IntMaxDamage = int(_readline)

                    _readline = StatsRd.readline()
                    Description = str(_readline)



                    _readline = MyStatsRd.readline()
                    MyIntCurExp = int(_readline)

                    _readline = MyStatsRd.readline()
                    MyIntCurLvl = int(_readline)

                    _readline = MyStatsRd.readline()
                    MyIntMaxHealth = int(_readline)

                    _readline = MyStatsRd.readline()
                    MyIntCurHealth = int(_readline)

                    _readline = MyStatsRd.readline()
                    MyIntMaxDamage = int(_readline)

                    _readline = MyStatsRd.readline()
                    MyDescription = str(_readline)

                    FreeLvlHA = IntCurLvl / 5

                    GetDamage = random.randint(0,MyIntMaxDamage)

                    IntCurHealth -= GetDamage

                    if IntCurHealth <= 0:
                        IntCurHealth = IntMaxHealth
                        IntCurLvl -= int(FreeLvlHA)
                        MyIntCurLvl += int(FreeLvlHA)
                        time.sleep(0.1)
                        #await message.channel.send(UserName_ + " убил " + CurCommandPlayer)


                        Emb = discord.Embed( title = CurCommandPlayer + " убит(а)")
                        Emb.add_field(name = 'Потерял(а) могущество : ',value = str(int(FreeLvlHA)) + " лвл.")
                        if IntCurLvl == 4:
                            Emb.add_field(name = 'Минимальный уровень',value =  "4",inline = True)
                        Emb.add_field(name = 'Здоровье : ',value = str(IntCurHealth) + " ед. / " + str(IntMaxHealth) + " ед.",inline = False)
                        Emb.add_field(name = 'Получил(а) урона : ',value = str(GetDamage) + " ед.",inline = True)
                        #Emb.set_image(url='https://sun9-20.userapi.com/c200720/v200720465/513de/84w3r07gfAI.jpg')

                        await message.channel.send(embed = Emb)

                        MyIntMaxHealth += 10 * int(FreeLvlHA)
                        MyIntCurHealth += 10 * int(FreeLvlHA)
                        MyIntMaxDamage += random.randint(1,35) * int(FreeLvlHA)
                        if ((IntCurHealth + 5 * int(FreeLvlHA)) < (IntMaxHealth)):
                            IntCurHealth += 5 * int(FreeLvlHA)
                        else:
                            IntCurHealth = IntMaxHealth

                    time.sleep(1)
                    StatsRd.close()
                    MyStatsRd.close()

                    MyStatsWr = open("StatsPlayer_" + UserName_ + ".txt","w") #Открывае поток файлов, на чтение
                    StatsWr = open("StatsPlayer_" + CurCommandPlayer + ".txt","w")

                    StatsWr.write(str(IntCurExp) + ln + str(IntCurLvl) + ln + str(IntMaxHealth) + ln + str(IntCurHealth) + ln + str(IntMaxDamage) + ln + Description) #Записываем все значения
                    MyStatsWr.write(str(MyIntCurExp) + ln + str(MyIntCurLvl) + ln + str(MyIntMaxHealth) + ln + str(MyIntCurHealth) + ln + str(MyIntMaxDamage) + ln + MyDescription) #Записываем все значения

                    StatsWr.close()
                    MyStatsWr.close()

                    Emb = discord.Embed( title = CurCommandPlayer)
                    Emb.add_field(name = 'Могущество : ',value = str(IntCurLvl) + " лвл.")
                    LevelingSystem = IntCurLvl * 5
                    Emb.add_field(name = 'После убийства : ',value = str(FreeLvlHA) + " ур.",inline = False)
                    Emb.add_field(name = 'Здоровье : ',value = str(IntCurHealth) + " ед. / " + str(IntMaxHealth) + " ед.",inline = False)
                    Emb.add_field(name = 'Получил урона : ',value = str(GetDamage) + " ед.",inline = True)

                    #await message.channel.send(embed = Emb) #Отправляет сообщение \ во избижаний лагов, лучше убрать

                except ValueError:
                    await message.channel.send("Аккаунт поврежден")
            except FileNotFoundError:
                await message.channel.send("Такого аккаунта не существует.")
        
        if (CurCommand == 'PROFILE') or (CurCommand == 'P') or (CurCommand == 'П') or (CurCommand == 'ПРОФИЛЬ'):

            try:
                StatsRd = open("StatsPlayer_" + CurCommandPlayer + ".txt","r") #Открывае поток файлов, на чтение
                try:
                    CurExp = StatsRd.readline() #Читаем 1 строчку, где храниться опыт
                    IntCurExp = int(CurExp)
                    CurLvl = StatsRd.readline() #Читаем 2 строчку, где храниться уровень
                    IntCurLvl = int(CurLvl)
                    _readline = StatsRd.readline() #Читаем 2 строчку, где храниться уровень
                    IntMaxHealth = int(_readline)
                    _readline = StatsRd.readline() #Читаем 2 строчку, где храниться уровень
                    IntCurHealth = int(_readline)
                    _readline = StatsRd.readline()
                    IntMaxDamage = int(_readline)
                    _readline = StatsRd.readline()
                    Description = str(_readline)
                    StatsRd.close()

                    Emb = discord.Embed( title = CurCommandPlayer)
                    Emb.add_field(name = 'Могущество : ',value = str(IntCurLvl) + " лвл.")
                    LevelingSystem = IntCurLvl * 5
                    Emb.add_field(name = 'Опыт : ',value = str(IntCurExp) + " ед. / " + str(LevelingSystem) + " ед.",inline = False)
                    Emb.add_field(name = 'Здоровье : ',value = str(IntCurHealth) + " ед. / " + str(IntMaxHealth) + " ед.",inline = False)
                    
                    if Description != "":
                        if (Description == "God") or (Description == "Divine"):
                            Emb.add_field(name= "Ранг : ",value = "Божественный")
                        elif Description == "Master":
                            Emb.add_field(name= "Ранг : ",value = "Мастер")
                        elif Description == "Boss":
                            Emb.add_field(name= "Ранг : ",value = "Босс")
                        elif Description == "Diamond":
                            Emb.add_field(name= "Ранг : ",value = "Алмаз")
                        elif Description == "Platinum":
                            Emb.add_field(name= "Ранг : ",value = "Платина")
                        elif Description == "Gold":
                            Emb.add_field(name= "Ранг : ",value = "Золото")
                        elif Description == "Silver":
                            Emb.add_field(name= "Ранг : ",value = "Серебро")
                        elif Description == "Bronze":
                            Emb.add_field(name= "Ранг : ",value = "Бронза")

                    await message.channel.send(embed = Emb)
                except ValueError:
                    await message.channel.send("Статистика аккаунта : '" + CurCommandPlayer + "' повреждена. не была восстановлена")
            except FileNotFoundError:
                if CurCommandPlayer == "":
                    pass
                else:
                    await message.channel.send("Такого аккаунта не существует.")


        if CurCommand == "HOTSPROFILE":
            pass



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