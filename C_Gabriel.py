import pickle
import discord


class Gabriel():

    def __init__(self):
        print("Создания класса Габриэль")

        self.Guilds = list()


        with open(f"./Resurses/System/Gabriel_Config.txt","wb") as file:
                pickle.dump(self,file)

    @staticmethod
    def Open():
        """ Открыть сохраненный класс Габриэль """
        try:
            with open(f"./Resurses/System/Gabriel_Config.txt","rb") as file:
                return pickle.load(file)
        except: raise FileNotFoundError("Габриэль не нашла свою сохраненную версию")
    
    def Save(self):
        """ Сохранить класс Габриэль """

        copy = self.Open()
        try:
            with open(f"./Resurses/System/Gabriel_Config.txt","wb") as file:
                pickle.dump(self,file)
        except BaseException as Err: 
            with open(f"./Resurses/System/Gabriel_Config.txt","wb") as file:
                pickle.dump(copy,file)
            print(f"Не удалось сохранить \n [{Err}]")

class Message():
    def __init__(self,
            ID          : int,
            Content     : str,
            Player):
        self.ID          = ID
        self.Content     = Content
        self.Player      = Player

class Guild():
    def __init__(self,
            ID   : int, 
            Name : str):

        self.ID                = ID
        self.Name              = Name

        self.Words             = list()
        self.Blocked_Words     = list()
        self.Blocked_Members   = list()
        self.Channels          = list()
        self.Channels_Ignoted  = list()

        self.Channel_Main      = Ellipsis
        self.Channel_Command   = Ellipsis

        self.Name_rooms_create = "Создать комнату"
        self.StandartWords     = (3,6)
        self.ChanceSays        = 35
        self.IgnoreMembers     = list()
        self.Speak             = True
        self.EveryTime         = 300

        self.Members           = list()

        self.Boss              = Ellipsis
    
    def __repr__(self):
        return f"[{self.Name}]"
    

    async def CheckMessage(self,Message : discord.Message,Content : str,Member : discord.Member,Client):
        """ Проверяет сообщения """

        
        Be = False
        for words in self.Blocked_Words:
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
                try:
                    WebhookThisChannel = await Message.channel.webhooks()
                    WebhookThisChannel = WebhookThisChannel[0]

                    await WebhookThisChannel.send(
                        content = Content,
                        username = Member.display_name,
                        avatar_url = Message.author.avatar_url)
                except: raise BaseException("Не могу создать вебхук для корректной работы")
            await Message.delete()


    def Message(self,CountMessages : int,Mode : "Usual or D / B",GetMessage : str = None):
        """ Сгенерировать сообщение """
        pass
        # ReturnMessage = ""
        # if CountMessages == 0: CountMessages = 1
        
        # if Mode == "Usual":
        #     while len(ReturnMessage.split(" ")) < CountMessages:
        #         try:
        #             message = self.Words.pop(random.randint(0,len(self.GotMessages) - 1))
        #         except: raise Error("Габриэль знает слишко мало слов")
        #         for content in message.Content.split(" "):
        #             if random.randint(0,1) == 1:
        #                 ReturnMessage += f"{content} "
        #             elif random.randint(0,1) == 1:
        #                 message = self.GotMessages.pop(random.randint(0,len(self.GotMessages) - 1))
        #                 for content in message.Content.split(" "):
        #                     if random.randint(0,1) == 1:
        #                         ReturnMessage += f"{content} "
        #     return ReturnMessage.capitalize()
        # elif Mode == "D":
        #     try:
        #         Title = ""
        #         while len(Title) <= random.randint(10,30):
        #             Message = self.GotMessages.pop(random.randint(0,len(self.GotMessages) - 1))
        #             _count = 0
                    
        #             for content in Message.Content.split(" "):
        #                 if random.randint(0,3) != 1 or _count < 3:
        #                     if content != "" and content != " ":
        #                         Title += f"{content} "
        #                         _count += 1
        #                         _preCount = 0
        #                         if random.randint(0,3) != 1:
        #                             Message = self.GotMessages.pop(random.randint(0,len(self.GotMessages) - 1))
        #                             for content in Message.Content.split(" "):
        #                                 if random.randint(0,3) != 1 or _preCount < 3:
        #                                     if content != "" and content != " ":
        #                                         content = SoMuchSpaces(re.sub(r"[^А-я]"," ",content))
        #                                         Title += f"{content} "
        #                                         _preCount += 1

        #         ReturnMessage += Title.capitalize()
                
        #         # Поиск участников диалога

        #         Players = list()
        #         _count = 100
        #         while len(Players) < random.randint(2,5):
        #             Message = self.GotMessages[random.randint(0,len(self.GotMessages) - 1)]
        #             author = Message.Author
        #             if len(author) >= 10: 
        #                 author = author[:10:]
        #                 author += "…"
        #             if author not in Players:
        #                 Players.append(author)
        #             _count -= 1
        #             if _count <= 0: break
        #         OldSay = None
        #         NowSay = None
        #         for _ in range(CountMessages):
        #             while OldSay == NowSay:
        #                 NowSay = Players[random.randint(0,len(Players) - 1)]
        #             ReturnMessage += f"\n• {NowSay}: "
        #             _count = 0
        #             Content = ""
        #             while len(Content) <= random.randint(10,30):
        #                 Message = self.GotMessages.pop(random.randint(0,len(self.GotMessages) - 1))
        #                 for content in Message.Content.split(" "):
        #                     if random.randint(0,3) != 1 or _count < 3:
        #                         if content != "" and content != " ":
        #                             Content += f"{content} "
        #                             _count += 1
        #                             _preCount = 0
        #                             if random.randint(0,3) != 1:
        #                                 Message = self.GotMessages.pop(random.randint(0,len(self.GotMessages) - 1))
        #                                 for content in Message.Content.split(" "):
        #                                     if random.randint(0,3) != 1 or _preCount < 3:
        #                                         if content != "" and content != " ":
        #                                             Content += f"{content} "
        #                                             _preCount += 1
        #             Content = SoMuchSpaces(re.sub(r"[^А-я]"," ",Content))
        #             ReturnMessage += Content.capitalize()
        #             OldSay = NowSay
        #     except ValueError: 
        #         return ReturnMessage
        #     return ReturnMessage
        # elif Mode == "A":
        #     if GetMessage:
        #         FoundList = list()
        #         SpliedList = list()

        #         class Message():
        #             def __init__(self,Quest,Answer):
        #                 self.Quest = Quest
        #                 self.Answer = Answer
        #             def __repr__(self):
        #                 rr = f"1: {self.Quest.Content}\n2: {self.Answer.Content}\n"
        #                 ll = "-" * len(rr)
        #                 return f"{rr}\n{ll}"
                
        #         def Search(message,GotMessages,index):
        #             next_message = Ellipsis
        #             for index2 in range(10):
        #                 try:
        #                     next_message = GotMessages[index + 1 + index2]
        #                 except: return next_message
        #                 if message.Author != next_message.Author:
        #                     return next_message
                
        #         for splied in GetMessage.split(" "):
        #             if len(splied) >= 3:
        #                 SpliedList.append(splied)
        #         for index, message in enumerate(self.GotMessages):
        #             for splied in SpliedList:
        #                 next_message = Search(message,self.GotMessages,index)
        #                 if message.Content.lower().find(splied.lower()) >= 0:
        #                     FoundList.append(Message(message,next_message))
        #         found = FoundList[random.randint(0,len(FoundList) - 1)]

        #         Main = ""
        #         for word in found.Answer.Content.split(" "):
        #             if random.randint(1,3) == 3:
        #                 Main += f"{word} "
        #             if random.randint(1,2) == 2:
        #                 new_line = self.GotMessages.pop(random.randint(0,len(self.GotMessages) - 1))
        #                 for word2 in new_line.Content.split(" "):
        #                     if random.randint(1,2) == 2:
        #                         Main += f"{word2} "
        #             if len(Main.split(" ")) >= CountMessages: return Main.capitalize()
        #         while len(Main.split(" ")) < CountMessages:
        #             try:
        #                 for word in Main.split(" "):
        #                     if random.randint(1,3) == 3:
        #                         new_line = self.GotMessages.pop(random.randint(0,len(self.GotMessages) - 1))
        #                         for word2 in new_line.Content.split(" "):
        #                             if random.randint(1,2) == 2:
        #                                 Main += f"{word2} "
        #                             if len(Main.split(" ")) >= CountMessages: return Main.capitalize()
        #                     if random.randint(1,2) == 2:
        #                         new_line = self.GotMessages.pop(random.randint(0,len(self.GotMessages) - 1))
        #                         if random.randint(1,3) == 3:
        #                             Main += f"{word2} "
        #                         if len(Main.split(" ")) >= CountMessages: return Main.capitalize()
        #             except: return Main.capitalize()
        #         return Main.capitalize()
        # elif Mode == "C":
        #     message = self.GotMessages.pop(random.randint(0,len(self.GotMessages) - 1))
        #     author = f'"{message.Author}"'
        #     ReturnMessage = self.Message(CountMessages,ServerName,"Usual")
        #     return f'"{ReturnMessage}"\nСказал **{author}**'
        


if __name__ == "__main__":
    Ga = Gabriel.Open()