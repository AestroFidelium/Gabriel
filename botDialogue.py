import discord
import BazaDate
from discord import user
import urllib
from urllib.request import urlopen
import time
import random

# import TestURLinMessage as TestURL
import botFunctions as Functions

from collections import Counter


ln = "\n"
Space = " "
FutureMessage = ""


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
messages = Functions.ReadWords()
Step = 3
Functions.FutureMessageDef(message=messages,step=Step)
class MyClient(discord.Client):
    async def on_ready(self):
        print(f"Logged on as , {self.user} MODULE : botDialogue.py")
    async def on_message(self, message):
    # don't respond to ourselves
        if message.author == self.user:
            return
        _Channel_ = discord.channel.TextChannel
        _Message_ = discord.message.Message
        try:
            _Channel_ = await self.fetch_channel(message.channel.id)
            _Message_ = await _Channel_.fetch_message(message.id)
        except:
            pass

        # try:
        #     banWords = ["https","gachi"]
        #     for BanWord in banWords:
        #         BanWordlower = str.lower(BanWord)
        #         Ban_Message = str.lower(_Message_.content)

        #         PossibleZnacks = [',','.','/','-',' ','=','+','_','<','>','?','"',"'",';',':','[',']','{','}','!','@','#','$','%','^','&','*','(',')']

        #         BanWord = False

        #         for Znack in PossibleZnacks:
        #             MessageSplit = Ban_Message.split(Znack)
        #             for _BanWord in MessageSplit:
        #                 if (Counter(_BanWord) == (Counter(BanWordlower))):
        #                     BanWord = True
        #                     await _Message_.delete()
        #                     return
        #                 if (Counter(_BanWord) == (Counter("gachi"))):
        #                     await _Message_.delete()
        #                     await message.channel.send(f"a {message.author.name}",delete_after=3)
        #                     return
                
        # except:
        #     pass
        try:
            messageLower = str(message.contect).lower()
            gachi = Functions.CheckText(messageLower,"gachi")

            if gachi == True:
                await _Message_.delete()
                pass
        except:
            pass
        
        msg =  message.content
        #print(msg)
        msgSP = msg.split()
        CurCommand = ""

        try:
            CurCommand = msgSP[0]
            CurCommand = str.upper(CurCommand)
        except IndexError:
            pass
        
        CurCommandPlayer = "" ; print(CurCommandPlayer,end="")
        UserName_ = message.author.name
       # UserName_ = message.author.name
        UserName_ = str.split(UserName_)
        UserName__ = str()
        for word in UserName_:
            UserName__ += word
        UserName_ = str(UserName__)

        #HttpsCheck = TestURL.CheckMessageIn(str.upper("https://."),str.upper(msg))

        try:
            CurCommandPlayer = msgSP[1]
            pass
        except IndexError:
            pass
        
        #print(message.author.name)

        RandomSaying = random.randint(0,3)

        if RandomSaying == 1:
            messages = Functions.ReadWords()
            try:
                Step = int(CurCommandPlayer)
                await message.channel.send(Functions.FutureMessageDef(message=messages,step=Step))
            except:
                pass

        if CurCommand == "G":
            await _Message_.delete()
            # messages = Functions.ReadWords()
            Step = int(CurCommandPlayer)
            # msg = Functions.FutureMessageDef(message=messages,step=Step)
            Gabriel = Functions.Gabriel()
            try:
                msg = Gabriel.Message(Step)
            except Gabriel.TooManyWords:
                await message.channel.send("Столько слов я не знаю ;c",delete_after=5)
                return
            # print(f"message : {msg} \nreadWords : {messages}")
            try:
                await message.channel.send(msg)
            except discord.errors.HTTPException:
                await message.channel.send(f"Столько слов я не могу отправить ;c",delete_after=5)
            
        else:
            ChannelPossible = [696928662045458452,419879599363850253,686553674394239053]
            if _Channel_.id in ChannelPossible:
                Commands = ['PROFILE','ПРОФИЛЬ','P','П',
                'Ы',
                'ATTACK','A','АТАКА','АТКОВАТЬ','АТАКУЮ',
                'ABOUT_ME',
                'NEW_AVATAR',
                'NEW_BACKGROUND',
                'DELETEINFO',
                'TOP',
                'INV',
                'WEAR',
                'UPGRADE_ITEM',
                'G','GABRIELE',
                'ГАБРИЭЛЬ',
                'КУПИТЬ','BUY','К','B',
                'TALANT',"ТАЛАНТ",
                "SELL_ITEM","S_I",
                "EVENT","E","Е","ИВЕНТ",
                "AU","AUCTION","АУКЦИОН"]
                if CurCommand not in Commands:
                    Functions.SaveWords(msg)
        #Команды Администрации
        if message.author.name == "KOT32500":
            if CurCommand == "GDDF": #Gabriel Delete Data File
                await _Message_.delete()
                Emb = discord.Embed( title = 'Стирание сохраненных слов')
                Emb.add_field(name = "Все сообщения, которые могла использовать Габриэль",value = "Были стёрты")
                await message.channel.send(embed = Emb,delete_after=10)
                Functions.ClearWords()

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