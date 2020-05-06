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
        textInputChannel = "1 = Разработка-Габриэль \n2 = Основной чат \n3 = Справка \n4 = Мини-Игра\nКасается Перевыбрать канал '.ch' \nКасается Текстовой канал : 1/4 : "
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
                channelSendMyMessage = self.get_channel(629267102070472714)#Мини-Игра
            try:
                try:
                    msg = input("Сообщение : ")
                    if(msg == ".ch"):
                        ChannelInput = input(textInputChannel)
                    elif(msg == ".help"):
                        ClearTerminal(50)
                        print(f"'.help' = Соказывает все команды, и как их использовать. \n'.ch' = Сменить текстовый канал \nКасается'.st' = Сделать красивое меню под текст. \nКасается~Принимает значения : 'Оглавление' = Самая первая надпись. \nКасается'Название' = Вторая надпись, будет чуть меньше обычного текста, и серого цвета. \nКасается'Текст' = Текст, который будет расположен в самом низу. Является обычным текстом, который входит в панель")
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

                        Emb = discord.Embed( title = 'Габриэль (Правила)')

                        nullHA = "‏                 ‫⁯"

                        Emb.add_field(name = "Правило",value = "18+ запрещён")
                        Emb.add_field(name = "Подробнее",value = "Картинки, видео, GIF , Coub , или любой другой фомарт, запрещен \nЛёгкая эротика разрешена, но только на специальных каналах. Такие как #мими-мишность-catgirl")
                        Emb.add_field(name = "Наказание",value = "Предупреждение, мут на пару часов ,потом кик, а после бан")

                        Emb.add_field(name = nullHA,value = "Чрезвычайная токсичность")
                        Emb.add_field(name = nullHA,value = "После каждого слова мат, и/или оскорбление")
                        Emb.add_field(name = nullHA,value = "Мут на пару часов")

                        Emb.add_field(name = nullHA,value = "Использовать ник игрока, который уже есть на сервере")
                        Emb.add_field(name = nullHA,value = "(Исключение : Это ваш 2 аккаунт)")
                        Emb.add_field(name = nullHA,value = "Предупреждение -> Кик")

                        Emb.add_field(name = nullHA,value = "Использовать 18+ в профиле")
                        Emb.add_field(name = nullHA,value = "Аватарка что в игре, что в вашем личном профиле, не должна содержать 18+ контент. (Опираемся на 1 правило)")
                        Emb.add_field(name = nullHA,value = "Предупреждение -> Кик -> Бан")

                        Emb.add_field(name = nullHA,value = "Оскорблять в статусе")
                        Emb.add_field(name = nullHA,value = "Запрещенно оскорблять в статусе кого либо. \nКасается всех статусов \nИсключение : Вы можете оскорблять самого себя")
                        Emb.add_field(name = nullHA,value = "Предупреждения -> Кик")

                        Emb.add_field(name = nullHA,value = "Присылать смайлики с 18+ контентом")
                        Emb.add_field(name = nullHA,value = ".")
                        Emb.add_field(name = nullHA,value = "Предупреждения -> Кик")

                        Emb.add_field(name = nullHA,value = "Злоупотребления правами")
                        Emb.add_field(name = nullHA,value = "Администрации запрещено удалять сообщения, без причины на то. Исключение : Это ваше сообщение. Это сообщение от бота Габриэль.\nЗапрещено перекидывать участников в голосовые, без причин")
                        Emb.add_field(name = nullHA,value = "Предупреждения -> Лишение прав")

                        Emb.add_field(name = nullHA,value = "Комнатах")
                        Emb.add_field(name = nullHA,value = "Создатель комнаты не должен устанавливать название комнаты, которое содержит оскорбление кого либо. Исключений нет")
                        Emb.add_field(name = nullHA,value = "Предупреждения -> Лишение прав комнаты -> Лишение прав создавать комнату")

                        Emb.set_thumbnail(url="https://cdn.discordapp.com/icons/419879599363850251/b51c45c480f3e9836c2acc1ab8e66503.jpg")

                        await channelSendMyMessage.send(embed = Emb)



                        Emb = discord.Embed( title = 'Габриэль (Команды)')

                        nullHA = "‏                 ‫⁯"

                        Emb.add_field(name = "Команда",value = "profile [Ничего/Аттрибуты]")
                        Emb.add_field(name = "Описание",value = "Открывает ваш профиль.")
                        Emb.add_field(name = "Атрибуты",value = "Не обязательны\nИмя игрока = открывает статистику выбранного игрока. Пример : profile KOT32500 \nСокращения : 'п','p'")

                        Emb.add_field(name = nullHA,value = "Ы")
                        Emb.add_field(name = nullHA,value = "Ы")
                        Emb.add_field(name = nullHA,value = "Атрибуты отсуствуют")

                        Emb.add_field(name = nullHA,value = "attack [Аттрибуты]")
                        Emb.add_field(name = nullHA,value = "С помощью этой команды, вы можете атаковать выбранного вами игрока. После убийства вы получаете часть его опыта.")
                        Emb.add_field(name = nullHA,value = "Обязательны \nИмя игрока = вы атакуете этого игрока. Пример : attack KOT32500 \nСокращения : 'а','атака','атаковать','атакую'")

                        Emb.add_field(name = nullHA,value = "About_Me")
                        Emb.add_field(name = nullHA,value = "Изменяет информацию о себе, которую можно посмотреть в профиле")
                        Emb.add_field(name = nullHA,value = "Обязательный \nТекст, который будет высвечиваться в профиле")

                        Emb.add_field(name = nullHA,value = "New_Avatar")
                        Emb.add_field(name = nullHA,value = "Изменяет текущую аватарку у пользователя, в профиле")
                        Emb.add_field(name = nullHA,value = "Обязательный \nURL на картинку. Если URL не будет поддерживаться, то он не поставиться.")

                        Emb.add_field(name = nullHA,value = "New_BackGround")
                        Emb.add_field(name = nullHA,value = "Изменяет текущий фон у пользователя, в профиле \nКасается(300х400) установиться расширение для фона. Имейте это ввиду, устанавливая собственный фон")
                        Emb.add_field(name = nullHA,value = "Обязательный \nURL на картинку. Если URL не будет поддерживаться, то он не поставиться.")

                        Emb.add_field(name = nullHA,value = "DeleteInfo")
                        Emb.add_field(name = nullHA,value = "Сбрасывает информацию о пользователе")
                        Emb.add_field(name = nullHA,value = "Не обязательный \nИмя игрока = сбрасывает статистику выбранного игрока. `Нужны адм права на это действие`")

                        Emb.add_field(name = nullHA,value = "Top")
                        Emb.add_field(name = nullHA,value = "Показывает топ 5 игроков")
                        Emb.add_field(name = nullHA,value = "Атрибуты отсуствуют")

                        Emb.add_field(name = nullHA,value = "Inv")
                        Emb.add_field(name = nullHA,value = "Показывает инвентарь игрока")
                        Emb.add_field(name = nullHA,value = "Атрибуты отсуствуют")

                        Emb.add_field(name = nullHA,value = "Wear")
                        Emb.add_field(name = nullHA,value = "Экипирует выбранный предмет")
                        Emb.add_field(name = nullHA,value = "ID предмета. Его можно увидить в команде Inv")

                        Emb.add_field(name = nullHA,value = "Upgrade_Item")
                        Emb.add_field(name = nullHA,value = "Улучшить предмет")
                        Emb.add_field(name = nullHA,value = "ID предмета. \nCount = количество золотых, которые вы потратите, на улучшение. Финальная команда выглядит так : Upgrade_Item 1234 5 \nГде 1234 это ID. \nГде 5 это количество золотых, которые мы тратим на улучшение предмета")

                        Emb.add_field(name = nullHA,value = "G")
                        Emb.add_field(name = nullHA,value = "Расшифровка Gabriele. Заставляет Габриэль сказать что-либо")
                        Emb.add_field(name = nullHA,value = "Index : Цифра. Регулирует количество изменяемых сообщений.")

                        Emb.add_field(name = nullHA,value = "G")
                        Emb.add_field(name = nullHA,value = "Расшифровка Gabriele. Заставляет Габриэль сказать что-либо")
                        Emb.add_field(name = nullHA,value = "Index : Цифра. Регулирует количество изменяемых сообщений.")

                        Emb.set_thumbnail(url="https://cdn.discordapp.com/icons/419879599363850251/b51c45c480f3e9836c2acc1ab8e66503.jpg")

                        await channelSendMyMessage.send(embed = Emb)

                        Emb = discord.Embed( title = 'Габриэль (Команды 2)')

                        nullHA = "‏                 ‫⁯"

                        Emb.add_field(name = nullHA,value = "Inv")
                        Emb.add_field(name = nullHA,value = "Показывает инвентарь игрока")
                        Emb.add_field(name = nullHA,value = "Атрибуты отсуствуют")

                        Emb.add_field(name = nullHA,value = "Wear")
                        Emb.add_field(name = nullHA,value = "Экипирует выбранный предмет")
                        Emb.add_field(name = nullHA,value = "ID предмета. Его можно увидить в команде Inv")

                        Emb.add_field(name = nullHA,value = "Upgrade_Item")
                        Emb.add_field(name = nullHA,value = "Улучшить предмет")
                        Emb.add_field(name = nullHA,value = "ID предмета. \nCount = количество золотых, которые вы потратите, на улучшение. Финальная команда выглядит так : Upgrade_Item 1234 5 \nГде 1234 это ID. \nГде 5 это количество золотых, которые мы тратим на улучшение предмета")

                        Emb.add_field(name = nullHA,value = "G")
                        Emb.add_field(name = nullHA,value = "Расшифровка Gabriele. Заставляет Габриэль сказать что-либо")
                        Emb.add_field(name = nullHA,value = "Index : Цифра. Регулирует количество изменяемых сообщений.")

                        Emb.add_field(name = nullHA,value = "G")
                        Emb.add_field(name = nullHA,value = "Расшифровка Gabriele. Заставляет Габриэль сказать что-либо")
                        Emb.add_field(name = nullHA,value = "Index : Цифра. Регулирует количество изменяемых сообщений.")

                        Emb.add_field(name = nullHA,value = "Габриэль")
                        Emb.add_field(name = nullHA,value = "PRAISE")
                        Emb.add_field(name = nullHA,value = "Отсуствуют")

                        Emb.set_thumbnail(url="https://cdn.discordapp.com/icons/419879599363850251/b51c45c480f3e9836c2acc1ab8e66503.jpg")

                        await channelSendMyMessage.send(embed = Emb)

                        Emb = discord.Embed( title = 'Габриэль (Магазин)')

                        nullHA = "‏                 ‫⁯"

                        Emb.add_field(name = "Название",value = "Лечение")
                        Emb.add_field(name = "Описание",value = "За каждый заряд, лечит по 500 ед. здоровья")
                        Emb.add_field(name = "Стоимость",value = "5 золотых на 1 ед.")

                        Emb.add_field(name = nullHA,value = "Урон")
                        Emb.add_field(name = nullHA,value = "За каждый заряд, добавляет от 300 до 1000 ед. к максимальному урону.")
                        Emb.add_field(name = nullHA,value = "35 золотых на 1 ед.")

                        Emb.add_field(name = nullHA,value = "Здоровье")
                        Emb.add_field(name = nullHA,value = "За каждый заряд, добавляет от 100 до 150 ед. к максимальному здоровью")
                        Emb.add_field(name = nullHA,value = "8 золотых на 1 ед.")

                        Emb.add_field(name = nullHA,value = "Опыт")
                        Emb.add_field(name = nullHA,value = "За каждый заряд, добавляет от 1000 до 2000 ед. опыта")
                        Emb.add_field(name = nullHA,value = "25 золотых на 1 ед.")

                        Emb.add_field(name = nullHA,value = "Уровень")
                        Emb.add_field(name = nullHA,value = "За каждый заряд, добавляет от 5 до 15 уровней")
                        Emb.add_field(name = nullHA,value = "50 золотых на 1 ед.")

                        Emb.set_thumbnail(url="https://cdn.discordapp.com/icons/419879599363850251/b51c45c480f3e9836c2acc1ab8e66503.jpg")




                        await channelSendMyMessage.send(embed = Emb)





                        pass

                    elif(msg == ".WELCOME"):
                        channelSendMyMessage = self.get_channel(691750825030320218) #<#623070280973156353>

                        await channelSendMyMessage.send("Привет, новичек. Рада видеть тебя на сервере")

                    elif (msg == ".j"):
                        pass
                    elif msg == ".shop":
                        Emb = discord.Embed( title = 'Габриэль')

                        nullHA = "‏                 ‫⁯"

                        Emb.add_field(name = "Товар",value = "Писать название товара, следует полностью исходя отсюда")
                        Emb.add_field(name = "Описание",value = "Внимание: большинство предметов, активируются сразу же, после покупки.")
                        Emb.add_field(name = "Стоимость",value = "Получить золото можно многими путями. Один из них, это набирать сообщения")

                        Emb.add_field(name = nullHA,value = "HotsProfile (разрабатывается)")
                        Emb.add_field(name = nullHA,value = "Открывает статистику побед/поражений в своих-играх")
                        Emb.add_field(name = nullHA,value = "Не обязательны \nИмя игрока = открываете статистику выбранного игрока.")

                        Emb.set_thumbnail(url="https://cdn.discordapp.com/icons/419879599363850251/b51c45c480f3e9836c2acc1ab8e66503.jpg")

                        await channelSendMyMessage.send(embed = Emb)
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