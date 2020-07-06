import ffmpeg
import BazaDate
import urllib
import time
import wget
import PIL
import ast
from bs4 import BeautifulSoup
import requests
from Functions2 import *

def is_internet():
    """
    Query internet using python
    :return:
    """
    
    try:
        urllib.request.urlopen('https://www.google.com', timeout=1)
        
        return True
    except urllib.error.URLError:
        return False

def InternetActive():
    client = MyClient()
    client.run(BazaDate.token)


class MyClient(discord.Client):
    async def on_ready(self):
        
        self.PATH_VERSION = "./Version 6"
        print(f"Logged on as , {self.user} MODULE : bot2.py")
        randomStatus = random.randint(0,7)
        with open(f"Ready.txt","r") as file:
            Working = str(file.readline())
        if Working == "-":
            if randomStatus == 0:
                await self.change_presence(
                    activity=discord.Activity(
                        type=discord.ActivityType.listening, 
                        name="твои истории"))
            elif randomStatus == 1:
                await self.change_presence(
                    activity=discord.Activity(
                        type=discord.ActivityType.listening, 
                        name="твои проблемы"))
            elif randomStatus == 2:
                await self.change_presence(
                    activity=discord.Activity(
                        type=discord.ActivityType.watching, 
                        name="в будущее"))
            elif randomStatus == 3:
                await self.change_presence(
                    activity=discord.Activity(
                        type=discord.ActivityType.watching, 
                        name="в окно"))
            elif randomStatus == 4:
                await self.change_presence(
                    activity=discord.Activity(
                        type=discord.ActivityType.listening, 
                        name="музыку"))
            elif randomStatus == 5:
                await self.change_presence(
                    activity=discord.Activity(
                        type=discord.ActivityType.watching, 
                        name="как моляться Богам фпса"))
            elif randomStatus == 6:
                await self.change_presence(
                    activity=discord.Activity(
                        type=discord.ActivityType.watching, 
                        name="на твою историю браузера ;D"))
            elif randomStatus == 7:
                await self.change_presence(
                    activity=discord.Activity(
                        type=discord.ActivityType.watching, 
                        name="в даль"))
        else:
            await self.change_presence(
                status=discord.Status.dnd,
                activity=discord.Activity(
                    type=discord.ActivityType.playing, 
                    name="технические работы"))
        
        self.Boss = Boss()
        Tasks = list()
        Tasks.append(asyncio.create_task(self.Boss.Respawn()))
        for Player in os.listdir(f"{self.PATH_VERSION}/Stats/"):
            Player = Player.split(".txt")[0]
            Player = C_Player(Player)
            try:
                _Talant = Talant(Player,Player.Talants[Player.TalantPicked],Player.TalantPicked)
                Tasks.append(asyncio.create_task(_Talant.Update()))
            except KeyError: pass
        asyncio.gather(*Tasks)
        print("работает все да")
   
    async def Command(self):
        self.Player.GetInventor()
        self.Player.GetTalants()
        if self.Commands[0].upper() == "2Profile".upper():
            await self.Message.delete()
            async with self.Channel.typing():
                try:
                    Player2 = self.Commands[1]
                except: Player2 = ""
                if Player2 != "":
                    Be = False
                    for Player in self.Players:
                        if Player2.upper() == Player.upper():
                            Player = C_Player(Player)
                            Be = True
                            await self.Channel.send(" ", file = Player.Profile())
                    if Be == False:
                        await self.Channel.send("Такого пользователя не существует")
                else:
                    await self.Channel.send(" ", file = self.Player.Profile())
        elif self.Commands[0].upper() == "LevelUpMe".upper():
            self.Player.LevelUp(C_Player.mode.multiply,count=999999999999)
            await self.Channel.send("Вы успешно получили уровни")
        elif self.Commands[0].upper() == "2Attack".upper():
            try:
                Player2 = self.Commands[1]
            except: 
                await self.Channel.send("Нужно указать имя игрока")
                return
            Be = False
            for Player in self.Players:
                if Player.upper() == Player2.upper():
                    Be = True
                    Target = C_Player(Player)
                    AttackStatus = self.Player.Attack(Target)
            if Be == True:
                if AttackStatus["Status"] == "Dead":
                    LostLevel = AttackStatus["Level"]
                    LostLevel = ReplaceNumber(LostLevel)

                    LostHealth = AttackStatus["Health"]
                    LostHealth = ReplaceNumber(LostHealth)

                    LostDamage = AttackStatus["Damage"]
                    LostDamage = ReplaceNumber(LostDamage)

                    LostAgility = AttackStatus["Agility"]
                    LostAgility = ReplaceNumber(LostAgility)

                    LostIntelligence = AttackStatus["Intelligence"]
                    LostIntelligence = ReplaceNumber(LostIntelligence)

                    LostStrength = AttackStatus["Strength"]
                    LostStrength = ReplaceNumber(LostStrength)

                    GetDamage = AttackStatus["GetDamage"]
                    GetDamage = ReplaceNumber(GetDamage)

                    await self.Channel.send(f"`{self.PlayerName}` вы убили `{Target.Name}`, нанеся {GetDamage}\nСтатистика `{Target.Name}` упала на : \nУровень : {LostLevel}\nЗдоровье : {LostHealth}\nУрон : {LostDamage}\nЛовкость : {LostAgility}\nИнтеллект : {LostIntelligence}\nСила : {LostStrength}")
            else:
                await self.Channel.send("Выбранного игрока не существует")
        elif self.Commands[0].upper() == "2B".upper():
            self.Boss.Create()
        elif self.Commands[0].upper() == "2Bp".upper():
            async with self.Channel.typing():
                await self.Channel.send(" ",file=self.Boss.Profile())
        elif self.Commands[0].upper() == "2Ba".upper():
            GetAttack_Stats = self.Boss.GetAttack(self.Player,self.Player.MaxDamage())
            if GetAttack_Stats.Status == "Dead":
                async with self.Channel.typing():
                    Damage = ReplaceNumber(GetAttack_Stats.Damage)
                    GetAttack_StatsGold = ReplaceNumber(GetAttack_Stats.Gold)
                    try:
                        ItemName = GetAttack_Stats.GetItem.Name
                    except AttributeError: ItemName = ""
                    await self.Channel.send(f"`{self.Player.Name}` нанёс последние {Damage} ед. урона, и убив Босса, получил с него : \n{GetAttack_StatsGold} золотых. \n{ItemName}")
        elif self.Commands[0].upper() == "2inv".upper():
            async with self.Channel.typing():
                for item in self.Player.GetInventored:
                    await self.Channel.send(f"```py\nИмя : `{item.Name}`\nОписание : `{item.Description}`\nТип : {item.Type}\nЗолота требуется : {item.Gold}/{item.MaxGold}\nКласс : {item.Class} \nID : {item.ID}```")
        elif self.Commands[0].upper() == "2item".upper():
            async with self.Channel.typing():
                ID = int(self.Commands[1])
                item = Item.Find(ID,self.Player)
                await self.Channel.send(f"```py\nИмя : `{item.Name}`\nОписание : `{item.Description}`\nТип : {item.Type}\nЗолота требуется : {item.Gold}/{item.MaxGold}\nКласс : {item.Class} \nID : {item.ID}```")
        elif self.Commands[0].upper() == "2u".upper():
            async with self.Channel.typing():
                ID = int(self.Commands[1])
                Gold = int(self.Commands[2])
                item = Item.Find(ID,self.Player)
                try:
                    item.Upgrade(Gold)
                    await self.Channel.send(f"```py\nИмя : `{item.Name}`\nОписание : `{item.Description}`\nТип : {item.Type}\nЗолота требуется : {item.Gold}/{item.MaxGold}\nКласс : {item.Class} \nID : {item.ID}```")
                except:
                    await self.Channel.send(f"Предмет не найден")
        elif self.Commands[0].upper() == "2G".upper():
            async with self.Channel.typing():
                try:
                    count = int(self.Commands[1])
                except: count = random.randint(1,35)
                Message = self.Gabriel.Message(count,self.Guild.name)
                await self.Channel.send(Message)
        # elif self.Commands[0].upper() == "2Talants".upper():
            # async with self.Channel.typing():
                # for talant in self.Player.GetTalanted:
                    # await self.Channel.send(f"```{talant.Name}\n{talant.}\n{}\n{}\n{}\n{}\n{}")
        else:
            self.Gabriel.SaveWords(self.Content,self.Guild.name)
    async def DownloadAvatar(self):
        try:
            with codecs.open(f"./Resurses/{self.PlayerName}.png","r"
            ,encoding='utf-8', errors='ignore') as file:
                pass
        except:
            try:
                DownloadFile = requests.get(self.Member.avatar_url, stream=True)
            except: DownloadFile = requests.get(self.Webhook.avatar_url, stream=True)
            with open(f"./Resurses/{self.PlayerName}.png","bw") as file:
                for chunk in DownloadFile.iter_content(12288):
                    file.write(chunk)
            print(f"{self.PlayerName} Не было аватарки, она скачалась")
    
    
    async def on_message(self,message):
        self.Content = str(message.content)
        self.Channel = await self.fetch_channel(message.channel.id)
        self.Message = await self.Channel.fetch_message(message.id)
        self.GodsAndCat = await self.fetch_guild(419879599363850251)
        self.Gabriel = Gabriel()
        try:
            self.Guild = await self.fetch_guild(message.channel.guild.id)
        except:
            if message.author != self.user:
                Reference = await self.fetch_channel(623070280973156353)
                GeneralChannel = await self.fetch_channel(419879599363850253)
                GameChannel = await self.fetch_channel(629267102070472714)
                await message.channel.send(f"Добрый день, извините, но я не работаю в личных сообщениях. Если вам нужна помощь то пожалуйста обратитесь за помощью к Гильдии **Боги и Кот**. \n{Reference.mention} : Канал где можно прочитать основную информацию об Гильдии\n{GeneralChannel.mention} : Канал где можно спросить что либо у участников. \n{GameChannel.mention} : Канал где нужно вводить все игровые команды\nУдачного вам дня.")
            return

        try:
            self.Member = await self.Guild.fetch_member(self.Message.author.id)
        except discord.errors.NotFound:
            self.Webhook = await self.fetch_webhook(self.Message.webhook_id)

        self.Commands = self.Content.split(" ")
        PlayerName = ""
        for part in str(message.author.name).split(" "):
            PlayerName += part
        
        self.PlayerName = PlayerName
        self.Player = C_Player(PlayerName)

        if self.Player.Exp >= self.Player.Level * 500:
            self.Player.LevelUp(C_Player.mode.one)

        self.Player.Exp += 1
        self.Player.Messages += 1
        if self.Player.Messages >= 5:
            self.Player.Messages = 0
            self.Player.Gold += 1
        self.Player.Edit(
            Edit="Main",
            Exp = self.Player.Exp,
            Messages = self.Player.Messages,
            Gold = self.Player.Gold
            )

        self.Players = list()
        self.Players.clear()
        for Player in os.listdir(f"{self.PATH_VERSION}/Stats/"):
            Player = Player.split(".txt")[0]
            self.Players.append(Player)

        await self.DownloadAvatar()
        await self.Command()
    


    async def on_voice_state_update(self,_Player_ : discord.member.Member, before : discord.member.VoiceState, after : discord.member.VoiceState):
        OurServer = await self.fetch_guild(_Player_.guild.id)
        EveryOne = OurServer.roles[0]
        Roles = OurServer.get_role(623063847497891840)
        PlayerName = ""
        for part in str(_Player_.name).split(" "):
            PlayerName += part
        Player = C_Player(PlayerName)
        try:
            Player.GetGuild(after.channel.guild.id)
            if after.channel.name == "Создать комнату":
                try:
                    if Player.RoomPermissions == None:
                        overwrites = {
                            _Player_: discord.PermissionOverwrite(manage_channels=True,move_members=True,manage_roles=True)
                        }
                    else:
                        SavedOverwrites = Player.RoomPermissions
                        overwrites = dict()
                        for overwrite in SavedOverwrites:
                            _Member = await OurServer.fetch_member(overwrite)
                            overwrite = SavedOverwrites[overwrite]
                            overwrites.update({_Member : discord.PermissionOverwrite(**overwrite)})

                    NewGroup = await OurServer.create_voice_channel(f"{Player.RoomName}",reason="Новая комната", overwrites=overwrites)
                    
                    await _Player_.move_to(NewGroup,reason="Новая комната")
                except:
                    NewGroup = await OurServer.create_voice_channel(f"{Player.RoomName}",reason="Новая комната")
                    
                    await _Player_.move_to(NewGroup,reason="Новая комната")
            elif after.channel.name == "Создать комнату (Истинный чат)":
                try:
                    if Player.RoomPermissions == None:
                        overwrites = {
                            _Player_ : discord.PermissionOverwrite(manage_channels=True,move_members=True,manage_roles=True),
                            Roles : discord.PermissionOverwrite(connect=True),
                            EveryOne : discord.PermissionOverwrite(connect=False)
                        }
                    else:
                        SavedOverwrites = Player.RoomPermissions
                        overwrites = dict()
                        for overwrite in SavedOverwrites:
                            _Member = await OurServer.fetch_member(overwrite)
                            overwrite = SavedOverwrites[overwrite]
                            overwrites.update({_Member : discord.PermissionOverwrite(**overwrite)})
                    overwrites.update({Roles : discord.PermissionOverwrite(connect=True)})
                    NewGroup = await OurServer.create_voice_channel(f"{Player.RoomName}",overwrites=overwrites,reason="Новая комната")
                    await _Player_.move_to(NewGroup,reason="Новая комната")
                except:
                    NewGroup = await OurServer.create_voice_channel(f"{Player.RoomName}",reason="Новая комната")
                    await _Player_.move_to(NewGroup,reason="Новая комната")
        except Exception: pass
        try:
            CurGroup = await self.fetch_channel(before.channel.id)
            Members = CurGroup.members
            NotDeleteChannels = ["Создать комнату","Резерв","Музыка","Создать комнату (Истинный чат)"]
            if len(Members) == 0 and str(CurGroup.name) not in NotDeleteChannels:
                await CurGroup.delete(reason="В комнате никого нет")
        except Exception: pass


    async def on_guild_channel_update(self,before,after):
        overwrites = before.overwrites
        PermissionsAll = dict()
        Maines = list()
        for overwrite in overwrites:
            try:
                permissions = overwrite.permissions
            except AttributeError:
                permissions = overwrite.permissions_in(before)
    
                if permissions.manage_channels == True:
                    _Permissions = dict()

                    for Permission in permissions:
                        _Permissions.update({Permission[0]:Permission[1]})
                    PermissionsAll.update({overwrite.id:_Permissions})

                    PlayerName = ""
                    for part in str(overwrite.name).split(" "):
                        PlayerName += part
                    Maines.append(PlayerName)
        for _PlayerName in Maines:
            Player = C_Player(_PlayerName)
            print(after.guild.id)
            Player.SaveRoom(after.guild.id,after.name,PermissionsAll)
    
    async def on_raw_reaction_add(self,payload):   
        Channel = await self.fetch_channel(payload.channel_id)
        Message = await Channel.fetch_message(payload.message_id)
        Guild = await self.fetch_guild(Message.channel.guild.id)
        Player = await self.fetch_user(payload.user_id)
        Member = await Guild.fetch_member(Player.id)
        UserName_ = ""
        for part in str(Player.name).split(" "):
            UserName_ += part
        DevelopGabriel = await self.fetch_guild(716945063351156736)
        EmodjsInDevelop = await DevelopGabriel.fetch_emojis()
        Emoji = payload.emoji
        print(Emoji)
        if Message.id == 713880721709727754:
            if Player == self.user:
                return
            await Message.remove_reaction(Emoji,Player)
            Standart = Guild.get_role(610078093260095488)
            StartRole = Guild.get_role(691735620346970123)
            MainChannel = self.get_channel(419879599363850253)
            await MainChannel.send(f"{Player.mention} присоединился на сервер")
            if str(Emoji.name) == "⚫":
                Role = Guild.get_role(713477362058002535)
                await Member.add_roles(Standart,Role,reason="Прошел регистацию")
                await Member.remove_roles(StartRole,reason="Прошел регистрацию")
            elif str(Emoji.name) == "🔵": 
                Role = Guild.get_role(713477367061938180)
                await Member.add_roles(Standart,Role,reason="Прошел регистацию")
                await Member.remove_roles(StartRole,reason="Прошел регистрацию")
            elif str(Emoji.name) == "🟤": 
                Role = Guild.get_role(713681425056006154)
                await Member.add_roles(Standart,Role,reason="Прошел регистацию")
                await Member.remove_roles(StartRole,reason="Прошел регистрацию")
            elif str(Emoji.name) == "🟢": 
                Role = Guild.get_role(713477377644167288)
                await Member.add_roles(Standart,Role,reason="Прошел регистацию")
                await Member.remove_roles(StartRole,reason="Прошел регистрацию")
            elif str(Emoji.name) == "🟠": 
                Role = Guild.get_role(713477369045712932)
                await Member.add_roles(Standart,Role,reason="Прошел регистацию")
                await Member.remove_roles(StartRole,reason="Прошел регистрацию")
            elif str(Emoji.name) == "🟣": 
                Role = Guild.get_role(713477376910032897)
                await Member.add_roles(Standart,Role,reason="Прошел регистацию")
                await Member.remove_roles(StartRole,reason="Прошел регистрацию")
            elif str(Emoji.name) == "🔴": 
                Role = Guild.get_role(713477364977500220)
                await Member.add_roles(Standart,Role,reason="Прошел регистацию")
                await Member.remove_roles(StartRole,reason="Прошел регистрацию")
            elif str(Emoji.name) == "⚪": 
                Role = Guild.get_role(713477210446757900)
                await Member.add_roles(Standart,Role,reason="Прошел регистацию")
                await Member.remove_roles(StartRole,reason="Прошел регистрацию")
            elif str(Emoji.name) == "🟡": 
                Role = Guild.get_role(713477378214592603)
                await Member.add_roles(Standart,Role,reason="Прошел регистацию")
                await Member.remove_roles(StartRole,reason="Прошел регистрацию")
            Msg = f"""```fix\nПоздравляю.``````\nВы успешно присоединились на сервер!\nТеперь вам доступен ранее недоступный контент.\nСоветую пройти обучение, оно поможет ознакомиться с сервером, \nИ стать полноценным участником, покажет и поможет в начале.\nНо прежде чем ты пойдешь его проходить, спешу сообщить о том, что время\nНа выполнения обучения ограничено часом, этого вполне хватит чтобы прочитать\nА после это меню автоматически уберёться, и не будет мешать вам быть \nПолноценным участником сервера!```
                """
            await Member.send(Msg)
            Channels = [721150391445749882,721150111320899586]
            Tasks = list()
            for Channel in Channels:
                Channel = await self.fetch_channel(Channel)
                overwrite = discord.PermissionOverwrite()
                overwrite.send_messages = True
                overwrite.read_messages = True
                overwrite.read_message_history = True
                Task = asyncio.create_task(Channel.set_permissions(Member,overwrite=overwrite))
                Task2 = asyncio.create_task(self._TimeShow(Member,Channel))
                Tasks.append(Task)
                Tasks.append(Task2)
            asyncio.gather(*Tasks)
        # -----------
        #Роли
        if Message.id == 714080637648240690:
            if Player == self.user:
                return
            await Message.remove_reaction(Emoji,Player)
            
            RolesID = [
                713477210446757900, 713477362058002535, 713477364977500220,
                713477367061938180, 713477369045712932, 713477376910032897,
                713477377644167288, 713477378214592603, 713681425056006154,
                716391511708794951, 716390741475196969, 716391516137848863,
                716391507980189726, 716391501772488748, 716391505425858641,
                716390742012199024, 716391505073274920

                    ]
            RoleList = list()
            for Role in RolesID:
                RoleList.append(Guild.get_role(Role))
            if str(Emoji.name) == "⚫": await self.AddOneRole(713477362058002535,Member,Guild,RolesID)
            elif str(Emoji.name) == "🔵": await self.AddOneRole(713477367061938180,Member,Guild,RolesID)
            elif str(Emoji.name) == "🟤": await self.AddOneRole(713681425056006154,Member,Guild,RolesID)
            elif str(Emoji.name) == "🟢": await self.AddOneRole(713477377644167288,Member,Guild,RolesID)
            elif str(Emoji.name) == "🟠": await self.AddOneRole(713477369045712932,Member,Guild,RolesID)
            elif str(Emoji.name) == "🟣": await self.AddOneRole(713477376910032897,Member,Guild,RolesID)
            elif str(Emoji.name) == "🔴": await self.AddOneRole(713477364977500220,Member,Guild,RolesID)
            elif str(Emoji.name) == "⚪": await self.AddOneRole(713477210446757900,Member,Guild,RolesID)
            elif str(Emoji.name) == "🟡": await self.AddOneRole(713477378214592603,Member,Guild,RolesID)
            elif str(Emoji.name) == "Turquoise_circle": await self.AddOneRole(716391511708794951,Member,Guild,RolesID)
            elif str(Emoji.name) == "Darkpurple_circle": await self.AddOneRole(716390741475196969,Member,Guild,RolesID)
            elif str(Emoji.name) == "Darkgreen_circle": await self.AddOneRole(716391516137848863,Member,Guild,RolesID)
            elif str(Emoji.name) == "Brown_circle": await self.AddOneRole(716391507980189726,Member,Guild,RolesID)
            elif str(Emoji.name) == "Blue_circle": await self.AddOneRole(716391501772488748,Member,Guild,RolesID)
            elif str(Emoji.name) == "Pink_circle": await self.AddOneRole(716390742012199024,Member,Guild,RolesID)
            elif str(Emoji.name) == "Scarlet_circle": await self.AddOneRole(716391505425858641,Member,Guild,RolesID)
            elif str(Emoji.name) == "Golden_circle": await self.AddOneRole(716391505073274920,Member,Guild,RolesID)
        #----
    async def AddOneRole(self,ID,Member,Guild,RolesID):
        Role = Guild.get_role(ID)
        await Member.add_roles(Role,reason="Выбрал роль")
        for role in Member.roles:
            if role.id in RolesID and role != Role:
                await Member.remove_roles(role,reason="Убрана старая роль")


    async def _TimeShow(self,Member,Channel):
        await asyncio.sleep(5000)
        overwrite = discord.PermissionOverwrite()
        overwrite.send_messages = False
        overwrite.read_messages = False
        overwrite.read_message_history = False
        await Channel.set_permissions(Member,overwrite=overwrite)
def main():
    internetWasOff = True
    while True:
        if is_internet():
            if(internetWasOff == True):
                print("Internet is active")
                InternetActive()
                internetWasOff = False
        else:
            internetWasOff = True
        time.sleep(1)

if __name__ == "__main__":
    main()
