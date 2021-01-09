import pickle
import discord
import random
from collections import Counter
import re
import time




class Message():
    def __init__(self,
            ID          : int,
            Content     : str,
            Player):
        self.ID          = ID
        
        self.Content     = re.sub("[^А-я\s]","",Content)
        self.Player      = Player
    
    def __repr__(self):
        return f"[{self.Content}]"
    def __gt__(self, message):
        if message.Content.split(" ") > self.Content.split(" "):
            return True
        else:
            return False




class Guild():
    def __init__(self,
            ID   : int, 
            Name : str):

        # Номер и название Гильдии
        self.ID                = ID
        self.Name              = Name

        # Чат-модерация
        self.Chat_Moderation   = True
        self.Blocked_Words     = ['gachi']

        # Чат-разговоры
        self.Speak             = True
        self.Words             = list()
        self.StandartWords     = (3,6)
        self.MessageEvery      = 25
        self.CurMessageEvery   = 0
        self.Channel_Main      = Ellipsis

        # Команды и прочее
        self.StartsWith        = "G?"
        self.Name_rooms_create = "Создать комнату"

        # Юзеры и их настройки
        self.Users             = list()
        self.Gabriel_Reaction_on = ["Габ"]

    
    def __repr__(self):
        return f"[{self.Name}]"
    

    async def CheckMessage(self,Message : discord.Message,Content : str,Member : discord.Member,Client):
        """ Проверяет сообщения """

        
        Be = False
        for words in self.Blocked_Words:
            if Content.upper().find(words.upper()) >= 0:
                Content = Content.upper().replace(words.upper(),":bread:")
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
        return Be

    def AdvancedAnswer(self, GetMessage : str, CountMessages : int = 5):
        """ Продвинутый ответ """

        class FoundMessage():
            def __init__(self, message : Message, index : int):
                self.Message = message
                self.Index = index
            def __repr__(self):
                return f"{self.Message}{self.Index}"

        # Находим сообщения в которых есть встречаются предложения из GetMessage
        FoundedMessages = list()
        for index, message in enumerate(self.Words):
            for Splited in GetMessage.lower().split(" "):
                if message.Content.lower().find(f" {Splited} ") >= 0:
                    FoundedMessages.append(FoundMessage(message,index))
        if len(FoundedMessages) > 1:
            PickMessage = FoundedMessages[random.randint(0,len(FoundedMessages) - 1)]
        elif FoundedMessages == []:
            raise BaseException("Не удалось найти ответ")
        else:
            PickMessage = FoundedMessages[0]

        # Следующее сообщение
        next_message = [self.Words[index] for index in range(PickMessage.Index - 1,len(self.Words),1)]
        
        # Ответ на сообщение
        Answer_On_The_Message = [message for message in next_message if message.Player.Name != PickMessage.Message.Player.Name and len(re.sub(r"/s","",message.Content)) >= 3]
        
        def Message_In_Split(Message):
            Answer = ""
            for position in Message.Content.split(" "):
                if random.randint(0,1) == 1:
                    Answer += f" {position}"
                elif random.randint(0,1) == 1:
                    Answer += Message_In_Split(sorted_Messages[random.randint(0,len(sorted_Messages) - 1)])
            return Answer
        
        def random_sorted(key):
            if random.randint(0,1) == 1:
                return True
            else:
                return False

        sorted_Messages = sorted(Answer_On_The_Message, key=random_sorted)

        found = sorted_Messages[random.randint(0,len(sorted_Messages) - 1)]
        Main = ""
        try:
            for word in found.Content.split(" "):
                if random.randint(1,3) == 3:
                    Main += f"{word} "
                if random.randint(1,2) == 2:
                    new_line = self.Words[random.randint(0,len(self.Words) - 1)]
                    for word2 in new_line.Content.split(" "):
                        if random.randint(1,2) == 2:
                            Main += f"{word2} "
                if len(Main.split(" ")) >= CountMessages: return Main.capitalize()
            while len(Main.split(" ")) < CountMessages:
                try:
                    for word in Main.split(" "):
                        if random.randint(1,3) == 3:
                            new_line = self.Words[random.randint(0,len(self.Words) - 1)]
                            for word2 in new_line.Content.split(" "):
                                if random.randint(1,2) == 2:
                                    Main += f"{word2} "
                                if len(Main.split(" ")) >= CountMessages: return Main.capitalize()
                        if random.randint(1,2) == 2:
                            new_line = self.Words[random.randint(0,len(self.Words) - 1)]
                            if random.randint(1,3) == 3:
                                Main += f"{word2} "
                            if len(Main.split(" ")) >= CountMessages: return Main.capitalize()
                except: return Main.capitalize()
            return Main.capitalize()
        except BaseException as Error:
            raise BaseException(f"Не смогла сгенерировать сообщение\nКод ошибки: \n{Error}")


    def Answer(self,CountMessages : int,GetMessage : str = None):
        """ Сгенерировать сообщение """

        ReturnMessage = ""
        FoundList = list()
        SpliedList = list()

        class __Message():
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
                if message.Player != next_message.Player:
                    return next_message
        
        for splied in GetMessage.split(" "):
            if len(splied) >= 3:
                SpliedList.append(splied)
        for index, message in enumerate(self.Words):
            for splied in SpliedList:
                next_message = Search(message,self.Words,index)
                if message.Content.lower().find(splied.lower()) >= 0:
                    FoundList.append(__Message(message,next_message))
        found = FoundList[random.randint(0,len(FoundList) - 1)]

        Main = ""
        try:
            for word in found.Answer.Content.split(" "):
                if random.randint(1,3) == 3:
                    Main += f"{word} "
                if random.randint(1,2) == 2:
                    new_line = self.Words[random.randint(0,len(self.Words) - 1)]
                    for word2 in new_line.Content.split(" "):
                        if random.randint(1,2) == 2:
                            Main += f"{word2} "
                if len(Main.split(" ")) >= CountMessages: return Main.capitalize()
            while len(Main.split(" ")) < CountMessages:
                try:
                    for word in Main.split(" "):
                        if random.randint(1,3) == 3:
                            new_line = self.Words[random.randint(0,len(self.Words) - 1)]
                            for word2 in new_line.Content.split(" "):
                                if random.randint(1,2) == 2:
                                    Main += f"{word2} "
                                if len(Main.split(" ")) >= CountMessages: return Main.capitalize()
                        if random.randint(1,2) == 2:
                            new_line = self.Words[random.randint(0,len(self.Words) - 1)]
                            if random.randint(1,3) == 3:
                                Main += f"{word2} "
                            if len(Main.split(" ")) >= CountMessages: return Main.capitalize()
                except: return Main.capitalize()
            return Main.capitalize()
        except BaseException as Error:
            raise BaseException(f"Не смогла сгенерировать сообщение\nКод ошибки: \n{Error}")

    def Save_Line(self, _Message : Message):
        if len(_Message.Content) >= 3:
            self.Words.append(_Message)
    
    def Save(self, _Gabriel):
        _Gabriel.__setattr__(str(self.ID),self)
        _Gabriel.Guilds.append(self)
        _Gabriel.Save()









class Gabriel():

    def __init__(self):
        print("Создания класса Габриэль")

        self.Guilds = list()
        self.Users  = list()

        with open(f"./Resurses/System/Gabriel_Config.txt","wb") as file:
                pickle.dump(self,file)

    @staticmethod
    def Open():
        """ Открыть сохраненный класс Габриэль """
        try:
            with open(f"./Resurses/System/Gabriel_Config.txt","rb") as file:
                return pickle.load(file)
        except:
            print(f"Габриэль: Не была найдена сохранённая копия. Инициализируеться новая")
            return Gabriel()
    
    def Save(self):
        """ Сохранить класс Габриэль """

        copy = self.Open()
        try:
            with open(f"./Resurses/System/Gabriel_Config.txt","wb") as file:
                pickle.dump(self,file)
        except BaseException as Err: 
            with open(f"./Resurses/System/Gabriel_Config.txt","wb") as file:
                pickle.dump(copy,file)
            print(f"Габриэль: Не удалось сохранить данные \n [{Err}]")


    def GetGuild(self, ID : int) -> Guild:
        """ Получить Гильдию """

        return getattr(self,str(ID),False)
    


    def __str__(self):
        content = "Список Гильдий:"
        for guild in self.Guilds:
            content += f"\n{guild}"
        return content


if __name__ == "__main__":
    Ga = Gabriel.Open()
    _Guild = Ga.GetGuild(419879599363850251)