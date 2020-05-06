import discord
import BazaDate
from discord import user
import urllib
from urllib.request import urlopen
import time
import random

import TestURLinMessage as TestURL


ln = "\n"
Space = " "
FutureMessage = ""

def FutureMessageDef(wordsAll,Strok):
    try:
        try:
            try:
                NewMsg = ""
                #print(len(wordsAll))
                RandInt = random.randint(1,len(wordsAll))
                #RandIntTwo = random.randint(1,RandInt)
                RandIntTwo = RandInt
                RandIntTwo /= Strok
                if int(RandIntTwo) < 1:
                    RandIntTwo = 1

                while (NewMsg == ""):
                    for target_list in range(int(RandIntTwo)):
                        RandInt = random.randint(0,len(wordsAll))
                        NewMsg += wordsAll[RandInt] + " "
                        if target_list == "EMPTY ERROR ESHI":
                            print("чот не то")
                return NewMsg
            except ZeroDivisionError:
                return "Неверный аргумент. Аргумент не должен быть равен 0"
        except ValueError:
            return "Недостаточно слов"
    except IndexError:
        FutureMessageDef(wordsAll,Strok)

def SaveWords(msg):
    bool_Test = TestURL.CheckMessageIn("https://.",msg)
    if bool_Test == False:
        try:
            with open('WORDS.txt') as file:
                lst = list()
                for line in file.readlines(): 
                    lst.extend(line.rstrip().split(' '))
            SaveWordw = open("WORDS.txt","w")
            
            for target_list in lst:
                SaveWordw.writelines(target_list + "\n")
            if msg != "G":
                SaveWordw.writelines(msg)
                SaveWordw.close()
            return lst
        except FileNotFoundError:
            SaveWordw = open("WORDS.txt","w")
            SaveWordw.close()
            SaveWords(msg)
    else:
        return msg


def is_internet():
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
            return
        bool_Test = TestURL.CheckMessageIn("https://.",message.content)
        _Channel_ = None
        _Message_ = None
        try:
            _Channel_ = await self.fetch_channel(message.channel.id)
            _Message_ = await _Channel_.fetch_message(message.id)
        except:
            pass
        if bool_Test == True:
            await _Message_.delete()

        
        
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
        UserName_ = message.author.name
       # UserName_ = message.author.name
        UserName_ = str.split(UserName_)
        UserName__ = str()
        for word in UserName_:
            UserName__ += word
        UserName_ = str(UserName__)

        gachi = TestURL.CheckMessageIn(str.upper("gachi"),str.upper(msg))

        #HttpsCheck = TestURL.CheckMessageIn(str.upper("https://."),str.upper(msg))

        try:
            CurCommandPlayer = msgSP[1]
            pass
        except IndexError:
            pass
        if (gachi == True):
            await message.channel.send(f"a {UserName_}")
        #print(message.author.name)
        RandomChat = random.randint(1,11)
        try:
            if (CurCommand == "G") and (int(CurCommandPlayer) >= 999):
                await message.channel.send("Ошибка : Число не должно быть больше чем 999.",delete_after=2)
                return
        except ValueError:
            await message.channel.send("Ошибка : Неверный аргумент",delete_after=2)
            return
        

        try:
            if RandomChat == 4:
                try:
                    try:
                        try:
                            FutureMessages = FutureMessageDef(SaveWords(msg),100)
                            await message.channel.send(FutureMessages)
                        except UnicodeEncodeError:
                            pass
                    except UnicodeEncodeError:
                        pass
                except discord.errors.HTTPException:
                    pass
            if CurCommand == "G":
                await _Message_.delete()
                try:
                    try:
                        try:
                            try:
                                FutureMessages = FutureMessageDef(SaveWords(msg),int(CurCommandPlayer))
                                await message.channel.send(FutureMessages)
                            except UnicodeEncodeError:
                                pass
                        except UnicodeEncodeError:
                            pass
                        except ValueError:
                            await message.channel.send("Ошибка : Вы указали неверный аргумент.",delete_after=2)
                    except discord.errors.HTTPException:
                        await message.channel.send("Я пыталась сгенерировать сообщение, но у меня ничего не получилось",delete_after=2)
                    pass
                except IndexError:
                    try:
                        try:
                            try:
                                FutureMessages = FutureMessageDef(SaveWords(msg),int(CurCommandPlayer))
                                await message.channel.send(FutureMessages)
                            except UnicodeEncodeError:
                                pass
                        except ValueError:
                            await message.channel.send("Ошибка : Вы указали неверный аргумент.",delete_after=2)
                    except discord.errors.HTTPException:
                        await message.channel.send("Я пыталась сгенерировать сообщение, но у меня ничего не получилось",delete_after=2)
                    pass
            else:
                SaveWords(msg)
        except discord.errors.HTTPException:
            if RandomChat == 4:
                try:
                    FutureMessages = FutureMessageDef(SaveWords(msg),100)
                    await message.channel.send(FutureMessages)
                except UnicodeEncodeError:
                    pass
            if CurCommand == "G":
                await _Message_.delete()
                try:
                    try:
                        try:
                            FutureMessages = FutureMessageDef(SaveWords(msg),int(CurCommandPlayer))
                            await message.channel.send(FutureMessages)
                        except UnicodeEncodeError:
                            pass
                    except ValueError:
                        await message.channel.send("Ошибка : Вы указали неверный аргумент.",delete_after=2)
                    pass
                except IndexError:
                    try:
                        try:
                            FutureMessages = FutureMessageDef(SaveWords(msg),int(CurCommandPlayer))
                            await message.channel.send(FutureMessages)
                        except UnicodeEncodeError:
                            pass
                    except ValueError:
                        await message.channel.send("Ошибка : Вы указали неверный аргумент.",delete_after=2)
                    pass
            else:
                
                SaveWords(msg)

        #Команды Администрации
        if message.author.name == "KOT32500":
            if CurCommand == "GDDF": #Gabriel Delete Data File
                await _Message_.delete()
                Emb = discord.Embed( title = 'Стирание сохраненных слов')
                Emb.add_field(name = "Все сообщения, которые могла использовать Габриэль",value = "Были стёрты")
                await message.channel.send(embed = Emb,delete_after=10)
                w = open("WORDS.txt","w")
                w.close()

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