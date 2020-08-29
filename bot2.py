import ffmpeg
import BazaDate
import urllib
import time
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
        Tasks = list()
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
        for emodji in self.emojis:
            if emodji.id == 745998760361852999:
                self.VoteOkay = emodji
            elif emodji.id == 745997811518275595:
                self.VoteBad = emodji
        self.MiniGame = MiniGame()
        self.Race = self.MiniGame.Race()
        self.Boss = Boss()
        self.Messages = list()
        self.BanList = list()
        self.AgainTheMessage = dict()
        
        Tasks.append(asyncio.create_task(self.Boss.Respawn()))
        Tasks.append(asyncio.create_task(self.Race.Main(self)))
        for Player in os.listdir(f"./Stats/"):
            Player = Player.split(".txt")[0]
            Player = C_Player(Player)
            try:
                _Talant = Talant(Player,Player.Talants[Player.TalantPicked],Player.TalantPicked)
                Tasks.append(asyncio.create_task(_Talant.Update()))
            except KeyError: pass
        Tasks.append(asyncio.create_task(self.MembersBanned()))
        asyncio.gather(*Tasks)
        self.GodsAndCat = await self.fetch_guild(419879599363850251)
        self.Gabriel = Gabriel()
        print("работает все да")
    
    async def MembersBanned(self):
        Count = 1
        while True:
            for _Member in self.BanList:
                MemberID = _Member["Member"]
                Time = _Member["Time"]
                Time -= Count
                NewMember = {"Member":MemberID,"Time":Time}
                self.BanList.remove(_Member)
                if Time > 0:
                    self.BanList.append(NewMember)
                print(NewMember)
            await asyncio.sleep(Count)
    
    def isBanned(self,MemberID):
        class Return():
            def __init__(self,Ban : bool):
                self.Ban = Ban
            def __bool__(self):
                return self.Ban
        try:
            for _Member in self.BanList:
                _MemberID = _Member["Member"]
                if MemberID == _MemberID:
                    return Return(True)
        except:
            return Return(False)
        

    async def Command(self,message):
        """ Команды """

        Channel = await self.fetch_channel(message.channel.id)
        Message = await Channel.fetch_message(message.id)

        # print()
        
        if str(Channel.type) != "private":
            Guild = await self.fetch_guild(message.channel.guild.id)
            Guild_Function = C_Guild(self,Guild.name)
        else:
            if message.author != self.user:
                Reference = await self.fetch_channel(623070280973156353)
                GeneralChannel = await self.fetch_channel(419879599363850253)
                GameChannel = await self.fetch_channel(629267102070472714)
                await message.channel.send(f"Добрый день, извините, но я не работаю в личных сообщениях. Если вам нужна помощь то пожалуйста обратитесь за помощью к Гильдии **Боги и Кот**. \n{Reference.mention} : Канал где можно прочитать основную информацию об Гильдии\n{GeneralChannel.mention} : Канал где можно спросить что либо у участников. \n{GameChannel.mention} : Канал где нужно вводить все игровые команды\nУдачного вам дня.")
            return

        # IamMember = await Guild.fetch_member(414150542017953793)
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
        for _Player in os.listdir(f"./Stats/"):
            _Player = _Player.split(".txt")[0]
            Players.append(_Player)
        Admin = False
        MUTE = False
        try:
            Member = await Guild.fetch_member(Message.author.id)
            User = await self.fetch_user(Message.author.id)
            await self.DownloadAvatar(Member,Player.Name)
            for role in Member.roles:
                if role.permissions.administrator == True:
                    Admin = True
                if str(role) == "Мут на команды для Габриэль":
                    MUTE = True
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
                    for Player in Players:
                        if Player2.upper() == Player.upper():
                            Player = C_Player(Player)
                            Be = True
                            await Channel.send(" ", file = Player.Profile())
                    if Be == False:
                        raise Error("Такого пользователя не существует")
                else:
                    await Channel.send(" ", file = Player.Profile())
        elif Commands[0].upper() == "Attack".upper():
            await Message.delete()
            try:
                Player2 = Commands[1]
            except: 
                raise Error("Нужно указать имя игрока")
                return
            Be = False
            for _Player in Players:
                if _Player.upper() == Player2.upper():
                    Be = True
                    Target = C_Player(_Player)
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

                    await Channel.send(f"`{Player.Name}` вы убили `{Target.Name}`, нанеся {GetDamage}\nСтатистика `{Target.Name}` упала на : \nУровень : {LostLevel}\nЗдоровье : {LostHealth}\nУрон : {LostDamage}\nЛовкость : {LostAgility}\nИнтеллект : {LostIntelligence}\nСила : {LostStrength}")
            else:
                raise Error(f"{Player2} не существует")
        elif Commands[0].upper() == "Event".upper():
            await Message.delete()
            if Commands[1].upper() == "Profile".upper():
                async with Channel.typing():
                    await Channel.send(" ",file=self.Boss.Profile())
            elif Commands[1].upper() == "Attack".upper():
                GetStats = self.Boss.GetAttack(Player,random.randint(1,Player.MaxDamage()))
                Status = GetStats[0]
                Embed = GetStats[1]
                if Status == "Dead":
                    async with Channel.typing():
                        await Channel.send(embed=Embed)
            elif Commands[1].upper() == "Bonus".upper():
                async with Channel.typing():
                    if Player.BonusDay != Day:
                        GetGold = random.randint(300,1000 + (1250 * Player.GetTalant("Max Bonus").Level))
                        GetGold += 300 * Player.GetTalant("Bonus").Level
                        Player.Edit(
                            Edit="Everyday bonus",
                            Day = Day,
                            Gold = GetGold)
                        Player.Gold += GetGold
                        Player.Edit(
                            Edit = "Main",
                            Gold = Player.Gold
                        )
                        await Channel.send(f"`{Player.Name}` взял(а) ежедневный бонус в размере {GetGold} золотых")
                    else:
                        await Channel.send(f"`{Player.Name}`, Вы уже брали ежедневный бонус в размере {Player.BonusGold} золотых")
            else:
                if Message.author == IamUser:
                    if Commands[1].upper() == "Create".upper():
                        async with Channel.typing():
                            self.Boss.Create()
                            await Channel.send(f"Создан новый босс")
                    else:
                        raise Error("Команды не существует")
                else:
                    raise Error("Команды не существует")
        elif Commands[0].upper() == "Inv".upper():
            await Message.delete()
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
            await Message.delete()
            async with Channel.typing():
                try:
                    ID = Commands[1]
                    item = Item.Find(int(ID),Player)
                    AllGold = ReplaceNumber(item.AllGold)
                    await Channel.send(f"```py\nИмя : `{item.Name}`\nОписание : `{item.Description}`\nТип : {item.Type}\nЗолота требуется : {item.Gold}/{item.MaxGold}({AllGold})\nКласс : {item.Class} \nID : {item.ID}```")
                except IndexError:
                    raise CommandError("Нужно указать ID предмета","Item","Item ID")
                except ValueError:
                    raise CommandError(f"{Debuger(ID,int)}\nНужно передавать ID предмета","Item","Item ID")
                except:
                    raise Error("Этот предмет сломан, либо его не существует")
        elif Commands[0].upper() == "Upgrade_Item".upper():
            await Message.delete()
            async with Channel.typing():
                try:
                    ID = Commands[1]
                    Gold = Commands[2]
                    item = Item.Find(int(ID),Player)
                    try:
                        item.Upgrade(int(Gold))
                        AllGold = ReplaceNumber(item.AllGold)
                        await Channel.send(f"```py\nИмя : `{item.Name}`\nОписание : `{item.Description}`\nТип : {item.Type}\nЗолота требуется : {item.Gold}/{item.MaxGold}({AllGold})\nКласс : {item.Class} \nID : {item.ID}```")
                    except:
                        await Channel.send(f"Предмет не найден")
                except IndexError:
                    raise CommandError("Пропущен обязательный аргумент","Upgrade_Item","Upgrade_Item ID Монеты")
                except ValueError:
                    raise Error(f"Оба аргумента должны быть в 'int'")
        elif Commands[0].upper() == "G".upper():
            await Message.delete()
            if MUTE == True: return
            async with Channel.typing():
                try:
                    if Commands[1].upper() == "S".upper():
                        try: Count = int(Commands[2])
                        except: Count = random.randint(1,35)
                        _Message = self.Gabriel.Message(Count,Guild.name,"Usual")
                        await Channel.send(_Message)
                    elif Commands[1].upper() == "D".upper():
                        try: Count = int(Commands[2])
                        except: Count = random.randint(3,7)
                        _Message = self.Gabriel.Message(Count,Guild.name,"D")
                        await Channel.send(_Message)
                    elif Commands[1].upper() == "B".upper():
                        try: Count = int(Commands[2])
                        except: Count = random.randint(3,7)
                        _Message = self.Gabriel.Message(Count,Guild.name,"B")
                        await Channel.send(_Message)
                    else:
                        Types = ["Usual","D","B"]
                        try: Count = int(Commands[2])
                        except: Count = random.randint(3,7)
                        _Message = self.Gabriel.Message(Count,Guild.name,Types[random.randint(0,2)])
                        await Channel.send(_Message)
                except:
                    Types = ["Usual","D","B"]
                    try: Count = int(Commands[2])
                    except: Count = random.randint(3,7)
                    _Message = self.Gabriel.Message(Count,Guild.name,Types[random.randint(0,2)])
                    await Channel.send(_Message)
        elif Commands[0].upper() == "Talants".upper():
            await Message.delete()
            async with Channel.typing():
                Embeds = list()
                Embed = discord.Embed(title=f"Статистика : {Player.Name}")
                Embed.set_author(name=Player.Name,url=User.avatar_url,icon_url=User.avatar_url)
                Embed.set_footer(text=f"Страница 1",icon_url=User.avatar_url)
                Count = 5
                Latter = 1
                for talant in Player.GetTalanted:
                    Count -= 1
                    if Count <= 0:
                        Latter += 1
                        Count = 5
                        Embeds.append(Embed)
                        Embed = discord.Embed(title=f"⁯")
                        Embed.set_footer(text=f"Страница {Latter}",icon_url=User.avatar_url)
                    Embed.add_field(name=f"{talant.Name} ({talant.MainName})",value=f"{talant.Description}\nКаждый уровень : {talant.PerLevel}\nУровень : {talant.Level}/{talant.MaxLevel}\nОпыт : {talant.Exp}/{talant.NeedExp}\nДоступность : {talant.Lock}\n{talant.NeedAt}",inline=False)
                Embeds.append(Embed)
                for _Embed in Embeds:
                    await Channel.send(embed=_Embed)
        elif Commands[0].upper() == "Talant".upper():
            await Message.delete()
            async with Channel.typing():
                if Content.find('"') == -1:
                    TalantName = Commands[1]
                    Player.PickTalant(TalantName)
                    await Channel.send(f"{TalantName} талант успешно поставлен")
                else:
                    TalantName = GetFromMessage(Content,'"')
                    Player.PickTalant(TalantName)
                    await Channel.send(f"{TalantName} талант успешно поставлен")
        elif Commands[0].upper() == "Number".upper():
            await Message.delete()
            try:
                Count = Commands[1]
                Number = ReplaceNumber(int(Count))
                await Channel.send(Number)
            except IndexError:
                raise CommandError("2 обязательный аргумент является целое число","Number","Number число")
            except ValueError:
                raise Error(Debuger(Count,int))
        elif Commands[0].upper() == "Equip".upper():
            await Message.delete()
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
            await Message.delete()
            try: 
                _channel = int(Commands[1])
                _ChannelVoice_ = await self.fetch_channel(_channel)
            except: _ChannelVoice_ = await self.fetch_channel(Message.author.voice.channel.id)
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
            print(f"Сыграла {RandomSound} трек")
            self.VoiceClient.play(discord.FFmpegPCMAudio(
                executable="C:/ffmpeg/bin/ffmpeg.exe", 
                source=f"./Resurses/JoinVoice/{RandomSound}"))
        elif Commands[0].upper() == "Nev_Avatar".upper():
            await Message.delete()
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
            await Message.delete()
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
            await Message.delete()
            async with Channel.typing():
                try:
                    Product = Commands[1]
                    Count = Commands[2]
                    Embed = Shop().Buy(Player,Product,int(Count))
                    Embed.set_author(name=Player.Name,url=User.avatar_url,icon_url=User.avatar_url)
                    await Channel.send(embed=Embed)
                except IndexError:
                    raise CommandError("Пропущен обязательный аргумент","Shop","Shop Товар Количество")
                except ValueError:
                    raise Error(f"2 Аргумент {Debuger(Count,int)}")
        elif Commands[0].upper() == "Wiki".upper():
            await Message.delete()
            async with Channel.typing():
                if Content.find('"') == -1:
                    NeedFind = Commands[1]
                else:
                    NeedFind = GetFromMessage(Content,'"')
                Embed = self.Gabriel.SearchInfo(NeedFind)
                Embed.set_author(name=Player.Name,url=User.avatar_url,icon_url=User.avatar_url)
                await Channel.send(embed=Embed)
        elif Commands[0].upper() == "Wear".upper():
            await Message.delete()
            async with Channel.typing():
                try: ID = int(Commands[1])
                except: raise Error("Не указан ID предмета")
                Item_ = Item.Find(ID,Player)
                if Item_.TypeKey.upper() == "Equipment".upper():
                    Player.EquipmentItem(ID,Item_.Where)
                else:
                    try: Where = Commands[2]
                    except: raise Error("Не указано куда следует экипировать предмет")
                    
                    Player.EquipmentItem(ID,Where)
                await Channel.send("Вы успешно экипировали предмет")
        elif Commands[0].upper() == "Race".upper():
            await Message.delete()
            async with Channel.typing():
                try: ID = int(Commands[1])
                except: raise Error("Не указана лошадь. От 1 до 5")
                try: Gold = int(Commands[2])
                except: raise Error("Не указана цена")

                Embed = self.Race.AddRate(Player,ID,Gold)
                
                await Channel.send(embed=Embed)
        elif Commands[0].upper() == "Vote".upper():
            replaces = list()
            replaces.append(Commands[0])
            Title = GetFromMessage(Content,'"')
            replaces.append(f'"{Title}"')

            _Content = MessageReplaces(Content,replaces)
            try:
                Description = GetFromMessage(_Content,'"')
                replaces.append(f'"{Description}"')
                Embed = discord.Embed(title=Title,description=Description)
            except: Embed = discord.Embed(title=Title)

            Embed.set_author(name=Member.name,icon_url=User.avatar_url)
            Embed.set_footer(text="Для выбора ответа, нажмите на реакцию")
            _Content = MessageReplaces(Content,replaces)
            try:
                Image = GetFromMessage(_Content,'"')
                if Image.find("https://") == -1:
                    raise Error("Ожидалась ссылка")
                Embed.set_image(url=Image)
            except: pass
            await Message.delete()
            _Message = await Channel.send(embed=Embed)
            await _Message.add_reaction(self.VoteOkay)
            await _Message.add_reaction(self.VoteBad)
        else:
            if Message.author.bot == False:
                if Admin == True:
                    if Commands[0].upper() == "Delete".upper():
                        await Message.delete()
                        async with Channel.typing():
                            Count = int(Commands[1])
                            Embed = self.Gabriel.Delete(Count,Guild.name)
                            await Channel.send(embed=Embed,delete_after=1)
                    elif Commands[0].upper() == "BanWord".upper():
                        await Message.delete()
                        async with Channel.typing():
                            Word = Commands[1]
                            Guild_Function.AddWord(Word)
                            Embed = discord.Embed(title=f"{Guild.name}",description=f"Отныне слово {Word} шифруется")
                            await Channel.send(embed=Embed)
                    elif Commands[0].upper() == "UnBanWord".upper():
                        await Message.delete()
                        async with Channel.typing():
                            Word = Commands[1]
                            Guild_Function.RemoveWord(Word)
                            Embed = discord.Embed(title=f"{Guild.name}",description=f"Отныне слово {Word} перестает шифроватся")
                            await Channel.send(embed=Embed)
                    elif Commands[0].upper() == "BannedWords".upper():
                        await Message.delete()
                        async with Channel.typing():
                            await Channel.send(Guild_Function.BadWords)
                    else:
                        if Message.author != self.user:
                            await Guild_Function.CheckMessage(Message,Content,Member)
                            self.Gabriel.Save(Content,Player.Name,Guild.name)
                else:
                    if Message.author != self.user:
                        await Guild_Function.CheckMessage(Message,Content,Member)
                        self.Gabriel.Save(Content,Player.Name,Guild.name)
        if Message.author == IamUser:
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
            elif Commands[0].upper() == "LevelUpMe".upper():
                Level = int(Commands[1])
                Player.LevelUp(C_Player.mode.multiply,count=Level)
                R_Level = ReplaceNumber(Level)
                await Channel.send(embed=discord.Embed(title="Поздравляем",description=f"Вы получили {R_Level} уровней",colour=discord.Colour(6655214)))
            elif Commands[0].upper() == "Develop".upper():
                Title = GetFromMessage(Content,'"')
                await self.change_presence(
                    status=discord.Status.dnd,
                    activity=discord.Activity(
                        type=discord.ActivityType.playing, 
                        name=Title))
            elif Commands[0].upper() == "Work".upper():
                await self.change_presence(
                    activity=discord.Activity(
                        type=discord.ActivityType.watching, 
                        name="новое обновление"))
        
        if Content.count(")") > 0:
            if Message.author != self.user:
                async with Channel.typing():
                    Count = Content.count(")")
                    if Count < 100:
                        await Channel.send(")" * Count)
    
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
        # print(bool(self.isBanned(message.author.id)))
        Saved = {"Member":message.author.id,"Message":message.content}
        if Saved not in self.Messages:
            self.Messages.append(Saved)
            self.AgainTheMessage.update({message.author.id:{"Member":message.author.id,"Count":3,"Time":NowTime()}})
        else:
            Old = self.AgainTheMessage[message.author.id]
            Time = int(Old["Time"])
            if Time >= NowTime() - 15:
                print("СЛИШКОМ БЫСТРААА")
                Count = Old["Count"]
                Count -= 1
                self.AgainTheMessage.update({message.author.id:{"Member":message.author.id,"Count":Count,"Time":NowTime()}})
                if Count <= 0:
                    NewBan = {"Member":message.author.id,"Time":300}
                    if NewBan not in self.BanList:
                        self.BanList.append(NewBan)
        # if message.author != self.user:
        #     await self.Command(message)
        try:
            if message.author != self.user:
                await self.Command(message)
        except OverflowError:
            Embed = discord.Embed(title="Ваша статистика бессконечна",description=f"Из за этого ваши действия невозможно сканировать",colour=discord.Colour.red())
            
            await message.channel.send(embed=Embed,delete_after=60)

        except OSError:
            Embed = discord.Embed(title="Ошибка",description=f"{message.author.mention} , не могу создать аккаунт под ваше имя",colour=discord.Colour.red())
            await message.channel.send(embed=Embed,delete_after=60)
        except CommandError as Error:
            Embed = discord.Embed(title="Ошибка",description=f"{Error.Message} \nКоманда : {Error.Command} \nПравильное написание команды : {Error.Correct}",colour=discord.Colour.red())
            await message.channel.send(embed=Embed,delete_after=60)
        except Warn as Error:
            Embed = discord.Embed(title="Предупреждение",description=f"{Error.Message} \nСлово : {Error.Word} \nКоличество предупреждений {Error.Warns}/{Error.MaxWarns}",colour=discord.Colour.gold())
            await message.channel.send(embed=Embed,delete_after=60)
        except BaseException as Error:
            if str(Error) != "404 Not Found (error code: 10008): Unknown Message":
                Embed = discord.Embed(title="Ошибка",description=str(Error),colour=discord.Colour.red())
                await message.channel.send(embed=Embed,delete_after=60)
    
    async def on_message_edit(self,before,after):
        try:
            content = before.content
            author = before.author.name
            server = before.channel.guild.name
            Delete = {author:content}
            self.Gabriel.DeleteCur(Delete,server)
            content = after.content
            author = after.author.name
            server = after.channel.guild.name
            self.Gabriel.Save(content,author,server)
        except: pass
    async def on_message_delete(self,message):
        try:
            content = message.content
            author = message.author.name
            server = message.channel.guild.name
            Delete = {author:content}
            self.Gabriel.DeleteCur(Delete,server)
        except: pass
        # self.Gabriel.

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
        MessageRoles = [714080637648240690,737503063409033247]
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
            elif str(Emoji.name) == "Laim_circle": 
                Role = Guild.get_role(716928278988062831)
                await Member.add_roles(Standart,Role,reason="Прошел регистацию")
                await Member.remove_roles(StartRole,reason="Прошел регистрацию")
            elif str(Emoji.name) == "Green_circle": 
                Role = Guild.get_role(716928278988062831)
                await Member.add_roles(Standart,Role,reason="Прошел регистацию")
                await Member.remove_roles(StartRole,reason="Прошел регистрацию")
            elif str(Emoji.name) == "Grass_circle": 
                Role = Guild.get_role(716928284453109772)
                await Member.add_roles(Standart,Role,reason="Прошел регистацию")
                await Member.remove_roles(StartRole,reason="Прошел регистрацию")
            elif str(Emoji.name) == "DarkGreen_circle": 
                Role = Guild.get_role(716928283123384382)
                await Member.add_roles(Standart,Role,reason="Прошел регистацию")
                await Member.remove_roles(StartRole,reason="Прошел регистрацию")
            elif str(Emoji.name) == "Untitled_circle": 
                Role = Guild.get_role(716928281747914792)
                await Member.add_roles(Standart,Role,reason="Прошел регистацию")
                await Member.remove_roles(StartRole,reason="Прошел регистрацию")
            elif str(Emoji.name) == "DarkBlue_circle": 
                Role = Guild.get_role(716928284641853461)
                await Member.add_roles(Standart,Role,reason="Прошел регистацию")
                await Member.remove_roles(StartRole,reason="Прошел регистрацию")
            elif str(Emoji.name) == "LightRed_circle": 
                Role = Guild.get_role(716928286759845899)
                await Member.add_roles(Standart,Role,reason="Прошел регистацию")
                await Member.remove_roles(StartRole,reason="Прошел регистрацию")
            elif str(Emoji.name) == "LightPink_circle": 
                Role = Guild.get_role(716928283089829951)
                await Member.add_roles(Standart,Role,reason="Прошел регистацию")
                await Member.remove_roles(StartRole,reason="Прошел регистрацию")
            elif str(Emoji.name) == "DarkRed_circle": 
                Role = Guild.get_role(716928286776754178)
                await Member.add_roles(Standart,Role,reason="Прошел регистацию")
                await Member.remove_roles(StartRole,reason="Прошел регистрацию")
            elif str(Emoji.name) == "LightBlue_circle": 
                Role = Guild.get_role(716928278988062831)
                await Member.add_roles(Standart,Role,reason="Прошел регистацию")
                await Member.remove_roles(StartRole,reason="Прошел регистрацию")
            elif str(Emoji.name) == "Orange_circle": 
                Role = Guild.get_role(716928283542945792)
                await Member.add_roles(Standart,Role,reason="Прошел регистацию")
                await Member.remove_roles(StartRole,reason="Прошел регистрацию")
            elif str(Emoji.name) == "Cyan_circle": 
                Role = Guild.get_role(716928286097408040)
                await Member.add_roles(Standart,Role,reason="Прошел регистацию")
                await Member.remove_roles(StartRole,reason="Прошел регистрацию")
            elif str(Emoji.name) == "Untitled1_circle": 
                Role = Guild.get_role(716928281966018631)
                await Member.add_roles(Standart,Role,reason="Прошел регистацию")
                await Member.remove_roles(StartRole,reason="Прошел регистрацию")
            elif str(Emoji.name) == "LightPurpure_circle": 
                Role = Guild.get_role(716928284830728262)
                await Member.add_roles(Standart,Role,reason="Прошел регистацию")
                await Member.remove_roles(StartRole,reason="Прошел регистрацию")
            elif str(Emoji.name) == "Untitled3_circle": 
                Role = Guild.get_role(716391509502722060)
                await Member.add_roles(Standart,Role,reason="Прошел регистацию")
                await Member.remove_roles(StartRole,reason="Прошел регистрацию")
            elif str(Emoji.name) == "DarkGreen2_circle": 
                Role = Guild.get_role(716928278988062831)
                await Member.add_roles(Standart,Role,reason="Прошел регистацию")
                await Member.remove_roles(StartRole,reason="Прошел регистрацию")
            elif str(Emoji.name) == "Blue2_circle": 
                Role = Guild.get_role(716928286965498007)
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
        elif Message.id in MessageRoles:
            if Player == self.user:
                return
            await Message.remove_reaction(Emoji,Player)
            
            RolesID = [
                713477210446757900, 713477362058002535, 713477364977500220,
                713477367061938180, 713477369045712932, 713477376910032897,
                713477377644167288, 713477378214592603, 713681425056006154,
                716391511708794951, 716390741475196969, 716391516137848863,
                716391507980189726, 716391501772488748, 716391505425858641,
                716390742012199024, 716391505073274920,

                716928278988062831, 716928279751295076, 716928280153817178,
                716928281630474261, 716928281747914792, 716928281798246470,
                716928281966018631, 716928283089829951, 716928283123384382,
                716928283542945792, 716928284453109772, 716928284641853461,
                716928284830728262, 716928286097408040, 716928286759845899,
                716928286776754178, 716928286965498007

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

            elif str(Emoji.name) == "Green_circle": await self.AddOneRole(716928278988062831,Member,Guild,RolesID)                              
            elif str(Emoji.name) == "Laim_circle": await self.AddOneRole(716928278988062831,Member,Guild,RolesID)
            elif str(Emoji.name) == "Grass_circle": await self.AddOneRole(716928284453109772,Member,Guild,RolesID)
            elif str(Emoji.name) == "DarkGreen_circle": await self.AddOneRole(716928283123384382,Member,Guild,RolesID)
            elif str(Emoji.name) == "Untitled_circle": await self.AddOneRole(716928281747914792,Member,Guild,RolesID)
            elif str(Emoji.name) == "DarkBlue_circle": await self.AddOneRole(716928284641853461,Member,Guild,RolesID)
            elif str(Emoji.name) == "LightRed_circle": await self.AddOneRole(716928286759845899,Member,Guild,RolesID)
            elif str(Emoji.name) == "LightPink_circle": await self.AddOneRole(716928283089829951,Member,Guild,RolesID)
            elif str(Emoji.name) == "DarkRed_circle": await self.AddOneRole(716928286776754178,Member,Guild,RolesID)
            elif str(Emoji.name) == "LightBlue_circle": await self.AddOneRole(716928278988062831,Member,Guild,RolesID)
            elif str(Emoji.name) == "Orange_circle": await self.AddOneRole(716928283542945792,Member,Guild,RolesID)
            elif str(Emoji.name) == "Cyan_circle": await self.AddOneRole(716928286097408040,Member,Guild,RolesID)
            elif str(Emoji.name) == "Untitled1_circle": await self.AddOneRole(716928281966018631,Member,Guild,RolesID)
            elif str(Emoji.name) == "LightPurpure_circle": await self.AddOneRole(716928284830728262,Member,Guild,RolesID)
            elif str(Emoji.name) == "Untitled3_circle": await self.AddOneRole(716391509502722060,Member,Guild,RolesID)
            elif str(Emoji.name) == "DarkGreen2_circle": await self.AddOneRole(716928278988062831,Member,Guild,RolesID)
            elif str(Emoji.name) == "Blue2_circle": await self.AddOneRole(716928286965498007,Member,Guild,RolesID)
        elif Emoji == self.VoteOkay:
            if Player != self.user:
                await Message.remove_reaction(self.VoteBad,Member)
        elif Emoji == self.VoteBad:
            if Player != self.user:
                await Message.remove_reaction(self.VoteOkay,Member)

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
