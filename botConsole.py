import discord
import urllib
from urllib.request import urlopen
import time

from discord.ext import commands

internetWasOff = True

def ClearTerminal(rang):
    for target_list in range(rang):
        print(" ")
        if target_list < 0:
            print ("ERROR")

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
    client.run("NjU2ODA4MzI3OTU0ODI1MjE2.Xik7NQ.pqnwoAWW_tDg25FVBzm5YLaVVw0")
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
        ClearTerminal(15)
        print(".help = для помощи")
        textInputChannel = "1 = Разработка-Габриэль \n2 = Основной чат \n3 = Справка \n4 = Мини-Игра\n Перевыбрать канал '.ch' \n Текстовой канал : 1/4 : "
        ClearTerminal(3)
        ChannelInput = input(textInputChannel)
        while True:
            channelSendMyMessage = 0 #Разработка-Габриэль
            if(ChannelInput == "1"):
                channelSendMyMessage = self.get_channel(627140104988917789) #Разработка-Габриэль
            elif(ChannelInput == "2"):
                channelSendMyMessage = self.get_channel(419879599363850253) #Основной чат 
            elif(ChannelInput == "3"):
                channelSendMyMessage = self.get_channel(623070280973156353) #Справка
            elif(ChannelInput == "4"):
                channelSendMyMessage = self.get_channel(629267102070472714) #Мини-Игра
            try:
                try:
                    msg = input("Сообщение : ")
                    if(msg == ".ch"):
                        ChannelInput = input(textInputChannel)
                    elif(msg == ".help"):
                        ClearTerminal(50)
                        print("'.help' = Соказывает все команды, и как их использовать. \n'.ch' = Сменить текстовый канал \n'.st' = Сделать красивое меню под текст. \n~Принимает значения : 'Оглавление' = Самая первая надпись. \n'Название' = Вторая надпись, будет чуть меньше обычного текста, и серого цвета. \n'Текст' = Текст, который будет расположен в самом низу. Является обычным текстом, который входит в панель")
                    elif(msg == ".st"):
                        ClearTerminal(10)
                        _title = input("Оглавление : ")
                        ClearTerminal(10)
                        _name = input("Название : ")
                        ClearTerminal(10)
                        _value = input("Текст : ")
                        Emb = discord.Embed( title = _title)
                        Emb.add_field(name = _name,value = _value)

                        await channelSendMyMessage.send(embed = Emb)
                    elif(msg == ".HLP"):
                        Emb = discord.Embed( title = 'Габриэль')

                        nullHA = "‏                 ‫⁯"

                        Emb.add_field(name = "Команда",value = "profile [Ничего/Аттрибуты]")
                        Emb.add_field(name = "Описание",value = "Открывает ваш профиль.")
                        Emb.add_field(name = "Аттрибуты",value = "Не обязательны\nИмя игрока = открывает статистику выбранного игрока. Пример : profile KOT32500 \nСокращения : 'п','p'")

                        Emb.add_field(name = nullHA,value = "Ы")
                        Emb.add_field(name = nullHA,value = "Ы")
                        Emb.add_field(name = nullHA,value = "Нету")

                        Emb.add_field(name = nullHA,value = "attack [Аттрибуты]")
                        Emb.add_field(name = nullHA,value = "С помощью этой команды, вы можете атаковать выбранного вами игрока. После убийства вы получаете часть его опыта.")
                        Emb.add_field(name = nullHA,value = "Обязательны \nИмя игрока = вы атакуете этого игрока. Пример : attack KOT32500 \nСокращения : 'а','атака','атаковать','атакую'")

                        Emb.add_field(name = nullHA,value = "HotsProfile (разрабатывается)")
                        Emb.add_field(name = nullHA,value = "Открывает статистику побед/поражений в своих-играх")
                        Emb.add_field(name = nullHA,value = "Не обязательны \nИмя игрока = открываете статистику выбранного игрока.")

                        Emb.set_thumbnail(url="https://cdn.discordapp.com/icons/419879599363850251/b51c45c480f3e9836c2acc1ab8e66503.jpg")

                        await channelSendMyMessage.send(embed = Emb)
                    elif (msg == ".j"):
                        pass
                    else:
                        await channelSendMyMessage.send(msg)
                except AttributeError:
                    ClearTerminal(50)
                    print("Канал не был выбран")
                    ClearTerminal(5)
                    ChannelInput = input(textInputChannel)
            except discord.errors.HTTPException:
                pass #Сообщение пустое

    async def on_message(self, message):
    # don't respond to ourselves
        if message.author == self.user:
            return
        
        if message.content == 'Ы':
            await message.channel.send("Ы")


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