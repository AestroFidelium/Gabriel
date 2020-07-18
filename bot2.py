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
        self.PATH_VERSION = "."
        print(f"Logged on as , {self.user} MODULE : bot2.py")
        randomStatus = random.randint(0,7)
        with codecs.open(f"Ready.txt","r",encoding='utf-8') as file:
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
        self.MiniGame = MiniGame()
        self.Race = self.MiniGame.Race()
        self.Boss = Boss()
        Tasks = list()
        Tasks.append(asyncio.create_task(self.Boss.Respawn()))
        Tasks.append(asyncio.create_task(self.Race.Main(self)))
        for Player in os.listdir(f"{self.PATH_VERSION}/Stats/"):
            Player = Player.split(".txt")[0]
            Player = C_Player(Player)
            try:
                _Talant = Talant(Player,Player.Talants[Player.TalantPicked],Player.TalantPicked)
                Tasks.append(asyncio.create_task(_Talant.Update()))
            except KeyError: pass
        asyncio.gather(*Tasks)
        self.GodsAndCat = await self.fetch_guild(419879599363850251)
        self.Gabriel = Gabriel()
        print("работает все да")
   
    async def Command(self,message):
        """ Команды """

        Channel = await self.fetch_channel(message.channel.id)
        Message = await Channel.fetch_message(message.id)
        
        try:
            Guild = await self.fetch_guild(message.channel.guild.id)
            Guild_Function = C_Guild(self,Guild.name)
        except:
            if message.author != self.user:
                Reference = await self.fetch_channel(623070280973156353)
                GeneralChannel = await self.fetch_channel(419879599363850253)
                GameChannel = await self.fetch_channel(629267102070472714)
                await message.channel.send(f"Добрый день, извините, но я не работаю в личных сообщениях. Если вам нужна помощь то пожалуйста обратитесь за помощью к Гильдии **Боги и Кот**. \n{Reference.mention} : Канал где можно прочитать основную информацию об Гильдии\n{GeneralChannel.mention} : Канал где можно спросить что либо у участников. \n{GameChannel.mention} : Канал где нужно вводить все игровые команды\nУдачного вам дня.")
            return

        IamMember = await Guild.fetch_member(414150542017953793)
        IamUser = await self.fetch_user(414150542017953793)

        Content = str(Message.content)

        Commands = Content.split(" ")

        PlayerName = ""
        for part in str(Message.author.name).split(" "):
            PlayerName += part
        
        PlayerName = PlayerName
        Player = C_Player(PlayerName)

        if Player.Exp >= Player.Level * 500:
            Player.LevelUp(C_Player.mode.one)

        Player.Exp += 1
        Player.Messages += 1
        if Player.Messages >= 5:
            Player.Messages = 0
            Player.Gold += 1
        Player.Edit(
            Edit="Main",
            Exp = Player.Exp,
            Messages = Player.Messages,
            Gold = Player.Gold
            )

        Players = list()
        Players.clear()
        for Player in os.listdir(f"{self.PATH_VERSION}/Stats/Main/"):
            Player = Player.split(".txt")[0]
            Players.append(Player)

        try:
            Member = await Guild.fetch_member(Message.author.id)
            User = await self.fetch_user(Message.author.id)
            await self.DownloadAvatar(Member,Player.Name)
        except discord.errors.NotFound:
            Webhook = await self.fetch_webhook(Message.webhook_id)
            await self.DownloadAvatar(Webhook,Player.Name)

        Player.GetInventor()
        Player.GetTalants()
        Day = datetime.datetime.now().day
        if Commands[0].upper() == "Profile".upper():
            await Message.delete()
            async with Channel.typing():
                try:
                    Player2 = Commands[1]
                except: Player2 = ""
                if Player2 != "":
                    Be = False
                    for Player in self.Players:
                        if Player2.upper() == Player.upper():
                            Player = C_Player(Player)
                            Be = True
                            await Channel.send(" ", file = Player.Profile())
                    if Be == False:
                        raise Error("Такого пользователя не существует")
                else:
                    await self.Channel.send(" ", file = self.Player.Profile())
        elif Commands[0].upper() == "LevelUpMe".upper():
            await Channel.send("Хитро, однако это больше не работает")
        elif Commands[0].upper() == "Attack".upper():
            try:
                Player2 = Commands[1]
            except: 
                raise Error("Нужно указать имя игрока")
                return
            Be = False
            for Player in self.Players:
                if Player.upper() == Player2.upper():
                    Be = True
                    Target = C_Player(Player)
                    AttackStatus = Player.Attack(Target)
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

                    await self.Channel.send(f"`{Player.Name}` вы убили `{Target.Name}`, нанеся {GetDamage}\nСтатистика `{Target.Name}` упала на : \nУровень : {LostLevel}\nЗдоровье : {LostHealth}\nУрон : {LostDamage}\nЛовкость : {LostAgility}\nИнтеллект : {LostIntelligence}\nСила : {LostStrength}")
            else:
                raise Error("Выбранного игрока не существует")
        elif Commands[0].upper() == "Event".upper():
            if Commands[1].upper() == "Profile".upper():
                async with Channel.typing():
                    await Channel.send(" ",file=self.Boss.Profile())
            elif Commands[1].upper() == "Attack".upper():
                GetStats = self.Boss.GetAttack(Player,Player.MaxDamage())
                Status = GetStats[0]
                Embed = GetStats[1]
                if Status == "Dead":
                    async with Channel.typing():
                        await Channel.send(embed=Embed)
            elif Commands[0].upper() == "Bonus".upper():
                async with Channel.typing():
                    if Player.BonusDay != Day:
                        GetGold = random.randint(300,1000)
                        Player.Edit(
                            Edit="Everyday bonus",
                            Day = self.Day,
                            Gold = GetGold)
                        Player.Gold += GetGold
                        Player.Edit(
                            Edit = "Main",
                            Gold = self.Player.Gold
                        )
                        await Channel.send(f"`{Player.Name}` взял(а) ежедневный бонус в размере {GetGold} золотых")
                    else:
                        await Channel.send(f"`{Player.Name}`, Вы уже брали ежедневный бонус в размере {Player.BonusGold} золотых")
        elif Commands[0].upper() == "Inv".upper():
            async with Channel.typing():
                SavedEmbeds = []
                Embed = discord.Embed(title=f"⁯")
                Embed.set_author(name=Player.Name,url=User.avatar_url,icon_url=User.avatar_url)
                Embed.set_footer(text="Страница 1",icon_url=User.avatar_url)
                Count = 0
                CountPapper = 1
                for item in Player.GetInventored:
                    Count += 1
                    AllGold = ReplaceNumber(item.AllGold)
                    Damage = ReplaceNumber(item.Damage)
                    Protect = ReplaceNumber(item.Protect)
                    Armor = ReplaceNumber(item.Armor)
                    AllGold = ReplaceNumber(item.AllGold)
                    Embed.add_field(name=item.Name,value=f"Описание : `{item.Description}`\nУрон : {Damage} / Защита : {Protect}\nПрочность : {Armor}\nЭкипируется : {item.Where}\nЗолота требуется : {item.Gold}/{item.MaxGold}({AllGold})\nКласс : {item.Class} \nМагические свойства : {item.Magic}\nID : {item.ID}",inline=False)
                    if Count == 15:
                        CountPapper += 1
                        Count = 0
                        SavedEmbeds.append(Embed)
                        Embed = discord.Embed(title=f"⁯")
                        Embed.set_author(name=Player.Name,url=User.avatar_url,icon_url=User.avatar_url)
                        Embed.set_footer(text=f"Страница {CountPapper}",icon_url=User.avatar_url)
                if len(SavedEmbeds) > 0:
                    for SavedEmbed in SavedEmbeds:
                        await Channel.send(embed=SavedEmbed)
                else:
                    await Channel.send(embed=Embed)
        elif Commands[0].upper() == "Item".upper():
            async with Channel.typing():
                ID = int(Commands[1])
                item = Item.Find(ID,Player)
                AllGold = ReplaceNumber(item.AllGold)
                await Channel.send(f"```py\nИмя : `{item.Name}`\nОписание : `{item.Description}`\nТип : {item.Type}\nЗолота требуется : {item.Gold}/{item.MaxGold}({AllGold})\nКласс : {item.Class} \nID : {item.ID}```")
        elif Commands[0].upper() == "Upgrade_Item".upper():
            async with Channel.typing():
                ID = int(Commands[1])
                Gold = int(Commands[2])
                item = Item.Find(ID,Player)
                try:
                    item.Upgrade(Gold)
                    AllGold = ReplaceNumber(item.AllGold)
                    await Channel.send(f"```py\nИмя : `{item.Name}`\nОписание : `{item.Description}`\nТип : {item.Type}\nЗолота требуется : {item.Gold}/{item.MaxGold}({AllGold})\nКласс : {item.Class} \nID : {item.ID}```")
                except:
                    await Channel.send(f"Предмет не найден")
        elif Commands[0].upper() == "G".upper():
            async with Channel.typing():
                try:
                    count = int(Commands[1])
                except: count = random.randint(1,35)
                Message = self.Gabriel.Message(count,Guild.name)
                await Channel.send(Message)
        elif Commands[0].upper() == "Talants".upper():
            async with Channel.typing():
                Embed = discord.Embed(title=f"Статистика : {Player.Name}")
                for talant in Player.GetTalanted:
                    Embed.add_field(name=talant.Name,value=f"{talant.Description}\nКаждый уровень : {talant.PerLevel}\nУровень : {talant.Level}/{talant.MaxLevel}\nОпыт : {talant.Exp}/{talant.NeedExp}\nДоступность : {talant.Lock}\n{talant.NeedAt}",inline=False)
                Embed.set_author(name=Player.Name,url=User.avatar_url,icon_url=User.avatar_url)
                Embed.set_footer(text=Player.Name,icon_url=User.avatar_url)
                await Channel.send(embed=Embed)
        elif Commands[0].upper() == "Number".upper():
            await Message.delete()
            Number = ReplaceNumber(int(Commands[1]))
            await Channel.send(Number)
        elif Commands[0].upper() == "Equip".upper():
            async with Channel.typing():
                Player.GetEquipment()
                Headers = ["Head","Body","Legs","Boot","Left_hand","Right_hand","Ring_1"
                ,"Ring_2","Ring_3","Ring_4","Ring_5"]
                count = 0
                Embed = discord.Embed(title=f"Статистика : {Player.Name}")
                for Equip in Player.GetEquipmented:
                    SpaceCenter = " " * 35
                    SpaceLeftCenter = " " * 17
                    Header = Headers[count]
                    Gold = ReplaceNumber(Equip.Gold)
                    MaxGold = ReplaceNumber(Equip.MaxGold)
                    AllGold = ReplaceNumber(Equip.AllGold)
                    Protect = ReplaceNumber(Equip.Protect)
                    Armor = ReplaceNumber(Equip.Armor)
                    Damage = ReplaceNumber(Equip.Damage)
                    Embed.add_field(name=Header,value=f"Название : {Equip.Name}\nОписание : {Equip.Description}\nID : {Equip.ID}\nУрон : {Damage} / Защита : {Protect}\nПрочность : {Armor}\nЗолото : {Gold}/{MaxGold} ({AllGold})\nМагические свойства : {Equip.Magic}",inline=False)
                    count += 1
                await Channel.send(embed=Embed)
        elif Commands[0].upper() == "Gs".upper():
            _ChannelVoice_ = await self.fetch_channel(Message.author.voice.channel.id)
            try:
                if self.VoiceClient.is_connected == False:
                    self.Sounds = os.listdir(f"./Resurses/JoinVoice/")
                    self.VoiceClient = await _ChannelVoice_.connect()
            except:
                self.Sounds = os.listdir(f"./Resurses/JoinVoice/")
                self.VoiceClient = await _ChannelVoice_.connect()
            try:
                RandomInt = random.randint(0,len(self.Sounds) - 1)
            except: 
                self.Sounds = os.listdir(f"./Resurses/JoinVoice/")
                RandomInt = random.randint(0,len(self.Sounds) - 1)
            RandomSound = self.Sounds[RandomInt]
            self.Sounds.remove(RandomSound)
            self.VoiceClient.play(discord.FFmpegPCMAudio(
                executable="C:/ffmpeg/bin/ffmpeg.exe", 
                source=f"./Resurses/JoinVoice/{RandomSound}"))
        elif Commands[0].upper() == "Nev_Avatar".upper():
            async with Channel.typing():
                try:
                    url = Commands[1]
                    DownloadFile = requests.get(url, stream=True)
                    with open(f"./Resurses/{Player.Name}.png","bw") as file:
                        for chunk in DownloadFile.iter_content(12288):
                            file.write(chunk)
                    await Channel.send("Новый аватар поставлен",delete_after=30)
                except:
                    raise Error("Поставить новый аватар не удалось")
        elif Commands[0].upper() == "New_Background".upper():
            async with Channel.typing():
                try:
                    url = Commands[1]
                    DownloadFile = requests.get(url, stream=True)
                    with open(f"./Resurses/BackGround_{Player.Name}.png","bw") as file:
                        for chunk in DownloadFile.iter_content(12288):
                            file.write(chunk)
                    await Channel.send("Новый фон поставлен",delete_after=30)
                except:
                    raise Error("Поставить новый фон не удалось")
        elif Commands[0].upper() == "Shop".upper():
            async with Channel.typing():
                Product = Commands[1]
                Count = int(Commands[2])
                Embed = Shop().Buy(Player,Product,Count)
                Embed.set_author(name=Player.Name,url=User.avatar_url,icon_url=User.avatar_url)
                await Channel.send(embed=Embed)
        elif Commands[0].upper() == "Wiki".upper():
            async with Channel.typing():
                NeedFind = Commands[1]
                Embed = self.Gabriel.SearchInfo(NeedFind)
                Embed.set_author(name=Player.Name,url=User.avatar_url,icon_url=User.avatar_url)
                await Channel.send(embed=Embed)
        elif Commands[0].upper() == "Wear".upper():
            async with Channel.typing():
                try: ID = int(Commands[1])
                except: raise Error("Не указан ID предмета")
                Item_ = Item.Find(ID,Player)
                if Item_.TypeKey.upper() == "Equipment".upper():
                    Player.EquipmentItem(ID,Item_.Where)
                else:
                    try: Where = Commands[2]
                    except: raise Error("Не указано куда следует экипировать предмет")
                    
                    self.Player.EquipmentItem(ID,Where)
                await Channel.send("Вы успешно экипировали предмет")
        elif Commands[0].upper() == "Race".upper():
            async with Channel.typing():
                try: ID = int(Commands[1])
                except: raise Error("Не указана лошадь. От 1 до 5")
                try: Gold = int(Commands[2])
                except: raise Error("Не указана цена")

                Embed = Race.AddRate(Player,ID,Gold)
                
                await Channel.send(embed=Embed)
        elif Message.author == IamUser:
            if Commands[0].upper() == "Admin".upper():
                if Commands[1].upper() == "Debug".upper():
                    async with Channel.typing():
                        Commands.pop(0)
                        Commands.pop(0)
                        Command = ""
                        for _command in Commands:
                            Command += f"{_command} "
                        print(f"Использована команда \n{Command}")
                        Answer = eval(Command)
                        print(f"Получен ответ : \n{Answer}")
                        if Answer == None:
                            Embed = discord.Embed(title="Админ меню",description="Команда выполненна успешно",colour=discord.Colour(9471))
                            await Channel.send(embed=Embed)
                        else:
                            Embed = discord.Embed(title="Админ меню",description=f"Команда вывела : \n{Answer}",colour=discord.Colour(65520))
                            await Channel.send(embed=Embed)
                elif Commands[1].upper() == "Create".upper():
                    async with Channel.typing():
                        Commands.pop(0)
                        Commands.pop(0)
                        Command = ""
                        for _command in Commands:
                            Command += f"{_command} "
                        print(f"Использована команда \n{Command}")
                        Answer = exec(Command)
                        print(f"Получен ответ : \n{Answer}")
                        if Answer == None:
                            Embed = discord.Embed(title="Админ меню",description="Программа выполненна успешно",colour=discord.Colour(9471))
                            await Channel.send(embed=Embed)
                        else:
                            Embed = discord.Embed(title="Админ меню",description=f"Программа вывела : \n{Answer}",colour=discord.Colour(65520))
                            await Channel.send(embed=Embed)
                else:
                    raise Error("Таких команд нет")
        elif Content.count(")") > 0:
            if Message.author != self.user:
                async with Channel.typing():
                    Count = Content.count(")")
                    if Count < 100:
                        await Channel.send(")" * Count)
        else:
            await Guild_Function.CheckMessage()
            self.Gabriel.SaveWords(Content,Guild.name)
    async def DownloadAvatar(self,Downloader,PlayerName):
        try:
            with codecs.open(f"./Resurses/{PlayerName}.png","r"
            ,encoding='utf-8', errors='ignore') as file:
                pass
        except:
            DownloadFile = requests.get(Downloader.avatar_url, stream=True)
            with open(f"./Resurses/{PlayerName}.png","bw") as file:
                for chunk in DownloadFile.iter_content(12288):
                    file.write(chunk)
            print(f"{PlayerName} Не было аватарки, она скачалась")
    
    
    async def on_message(self,message):
        try:
            if message.author != self.user:
                await self.Command(message)
        except OSError:
            Embed = discord.Embed(title="Ошибка",description=f"{message.author.mention} , не могу создать аккаунт под ваше имя",colour=discord.Colour.red())
            await message.Channel.send(embed=Embed,delete_after=60)
        except CommandError as Error:
            Embed = discord.Embed(title="Ошибка",description=f"{Error.Message} \nКоманда : {Error.Command} \nПравильное написание команды : {Error.Correct}",colour=discord.Colour.red())
            await message.Channel.send(embed=Embed,delete_after=60)
        except Warn as Error:
            Embed = discord.Embed(title="Предупреждение",description=f"{Error.Message} \nСлово : {Error.Word} \nКоличество предупреждений {Error.Warns}/{Error.MaxWarns}",colour=discord.Colour.gold())
            await message.Channel.send(embed=Embed,delete_after=60)
        except BaseException as Error:
            Embed = discord.Embed(title="Ошибка",description=str(Error),colour=discord.Colour.red())
            await message.Channel.send(embed=Embed,delete_after=60)
    


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
    
    async def on_member_join(self,Member : discord.member.Member):
        try:
            OurServer = await self.fetch_guild(419879599363850251)
            StartRole = OurServer.get_role(691735620346970123)
            await Member.add_roles(StartRole,reason="Впервые зашел на сервер")
        except: pass

    async def on_guild_channel_update(self,before,after):
        overwrites = before.overwrites
        PermissionsAll = dict()
        Maines = list()
        
        for overwrite in overwrites:
            try:
                permissions = overwrite.permissions
            except AttributeError:
                permissions = overwrite.permissions_in(before)
                
                _Permissions = dict()
                for Permission in permissions:
                    _Permissions.update({Permission[0]:Permission[1]})
                PermissionsAll.update({overwrite.id:_Permissions})
    
                if permissions.manage_channels == True:
                    

                    PlayerName = ""
                    for part in str(overwrite.name).split(" "):
                        PlayerName += part
                    Maines.append(PlayerName)
        for _PlayerName in Maines:
            Player = C_Player(_PlayerName)
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
