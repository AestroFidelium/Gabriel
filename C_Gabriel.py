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
        self.Player = Player

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


        


if __name__ == "__main__":
    Ga = Gabriel.Open()