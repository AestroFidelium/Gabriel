import ffmpeg
import BazaDate
import urllib
import time

#pylint: disable=unused-wildcard-import
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
            elif emodji.id == 751489305020596326:
                self.EmodjiGame = emodji
            elif emodji.id == 751490563316121693:
                self.EmodjiShop = emodji
            elif emodji.id == 751489305696010260:
                self.EmodjiReference = emodji
        self.MiniGame = MiniGame()
        self.Race = self.MiniGame.Race()
        self.Boss = Boss()
        self.Players = list()

        for player in os.listdir("./Stats/"):
            if player.endswith(".txt"):
                self.Players.append(C_Player.Open(player.replace(".txt","")))
        

        # Tasks.append(asyncio.create_task(self.Boss.Respawn()))
        # Tasks.append(asyncio.create_task(self.Race.Main(self)))
        # for Player in os.listdir(f"./Stats/"):
        #     try:
        #         Player = Player.split(".txt")[0]
        #         Player = C_Player(Player)
        #         try:
        #             try:
        #                 _Talant = Talant(Player,Player.Talants[Player.TalantPicked],Player.TalantPicked)
        #                 Tasks.append(asyncio.create_task(_Talant.Update()))
        #             except: pass
        #             Tasks.append(asyncio.create_task(Player.Regeneration()))
        #             Tasks.append(asyncio.create_task(Player.Repair()))
        #             Tasks.append(asyncio.create_task(Player.GeneratorExp()))
        #         except: print(f"{Player.Name} Error with corutines")
        #     except KeyError: pass
        #     except Error as error:
        #         print(error)
        # Tasks.append(asyncio.create_task(self.MembersBanned()))
        # asyncio.gather(*Tasks)
        self.GodsAndCat = await self.fetch_guild(419879599363850251)
        self.DevelopGuild = await self.fetch_guild(716945063351156736)
        self.Gabriel = Gabriel()
        self.C_Guilds = list()
        # for GuildName in os.listdir(f"./Servers"):
        #     with codecs.open(f"./Servers/{GuildName}/Main.txt","r",encoding='utf-8') as file:
        #         Stats = StrToDict(str(file.readline()))
        #         GuildID = Stats['ID']
        #         Guild = C_Guild(self,GuildID,GuildName)
        #         self.C_Guilds.append(Guild)
        #         Tasks.append(asyncio.create_task(self.WannaSpeak(Guild)))
        #         print(f"{GuildName} загружена")
        
        # print("работает все да")
    async def CreateColor(self,Color : tuple,Name : str):
        _Color = C_Color(Color)
        Emodji = _Color.Create()
        image = Emodji.save("Delete.png")
        with open("Delete.png", "rb") as image:
            f = image.read()
            b = bytearray(f)

        Emodji = await self.DevelopGuild.create_custom_emoji(name=Name,image=b,reason="Создаем новую цветную роль")

        Role = await self.GodsAndCat.create_role(name="⁯⁬⁬⁫⁫⁫⁫⁫⁫⁫⁫⁪⁪⁪⁪⁪⁪⁪⁪⁪⁪ ‫‫‫‫‪",colour=discord.Colour(rgbToColor(*Color)))
        
        return (Emodji.name, Role.id)

    
    async def WannaSpeak(self,Guild : C_Guild):
        while True:
            try:
                if Guild.Speak == True:
                    rand = len(Guild.ChannelsForSaveWords)
                    rand -= 1
                    ChannelID = Guild.ChannelsForSaveWords[rand]
                    Channel = await self.fetch_channel(ChannelID)
                    
                    history = await Channel.history(limit=1).flatten()
                    history = history[0]
                    if history.author.bot == False:
                        Message = self.Gabriel.Message(random.randint(Guild.StandartWords[0],Guild.StandartWords[1]),Guild.Name,"Usual")
                        BadList = ['<@!',"<@&","1","2","3","4","5","6","7","8","9","0",'<#>',"@"]
                        async with Channel.typing():
                            for bd in BadList: Message = Message.replace(bd,"")
                            await Channel.send(Message)
            except BaseException as Error:
                print(f"{Error}\n({Guild.Name})\n\n")
            await asyncio.sleep(Guild.EveryTime)
    async def Command(self,message):
        """ Команды """

        Channel = await self.fetch_channel(message.channel.id)
        Message = await Channel.fetch_message(message.id)
        
        if str(Channel.type) != "private":
            Guild = await self.fetch_guild(message.channel.guild.id)
            Guild_Function = C_Guild(self,Guild.id,Guild.name)
            if Guild_Function.New == True:
                self.C_Guilds.append(Guild_Function)
                print(f"`{Guild_Function.Name}` Новая Гильдия загружена в список Гильдий")
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
        try:
            Player = C_Player.Open(Message.author.id)
        except: Player = C_Player(Message.author.id,Message.author.name)

        if Player.Exp >= Player.Level * 500:
            Player.LevelUp()

        Player.Exp += 1 + Player.More_Exp.Level
        Player.Messages += 1
        if Player.Messages >= 5 - Player.More_Gold.Level:
            Player.Messages = 0
            Player.Gold += 1
        Player.Save()

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

        try:
            if Message.raw_mentions[0] == self.user.id:
                _Gabriel = Gabriel()
                
                try: _Message = _Gabriel.Message(random.randint(*Guild_Function.StandartWords),Guild.name,"A",Content.replace("<@!656808327954825216>",""))
                except: _Message = _Gabriel.Message(random.randint(*Guild_Function.StandartWords),Guild.name,"Usual")
                await Channel.send(f"> {Content}\n{Message.author.mention}, {_Message}")
                return
        except: pass
        

        if Commands[0].upper() == "Profile".upper():
            await Message.delete()
            async with Channel.typing():
                try:
                    Player2 = Commands[1]
                    if Player2.isnumeric():
                        Player = C_Player.Open(Player2)
                    else:
                        NickName = Content.upper().replace("PROFILE ","")
                        FoundList = list()
                        for player in self.Players:
                            if player.Name.upper() == NickName:
                                Player = player
                                FoundList.append(player)
                        if len(FoundList) > 1:
                            await Channel.send(f"Было найдено ({len(FoundList)}) игроков с таким же ником", file = Player.Profile())
                            return
                    await Channel.send(" ", file = Player.Profile())
                except (IndexError,ValueError):
                    await Channel.send(" ", file = Player.Profile())
                except:
                    raise BaseException("Такого пользователя не существует")
        elif Commands[0].upper() == "Attack".upper():
            await Message.delete()

            try: Player2 = Commands[1]
            except: raise BaseException("Нужно указать имя игрока")

            if Player2.isnumeric():
                Player2 = C_Player.Open(Player2)
                AttackStatus = Player.Attack(Player2)
            else:
                Targets = self.Fetch_Players(Content)
                if len(Targets) > 1:
                    await Channel.send(f"Было найдено ({len(Targets)}) игроков с таким же ником. Используйте лучше ID вместо ника")
                    AttackStatus = Player.Attack(Targets[0])
                elif len(Targets) == 0:
                    raise BaseException(f"{Player2} не существует")

                # if AttackStatus["Status"] == "Dead":
                #     LostLevel = AttackStatus["Level"]
                #     LostLevel = ReplaceNumber(LostLevel)

                #     LostHealth = AttackStatus["Health"]
                #     LostHealth = ReplaceNumber(LostHealth)

                #     LostDamage = AttackStatus["Damage"]
                #     LostDamage = ReplaceNumber(LostDamage)

                #     LostAgility = AttackStatus["Agility"]
                #     LostAgility = ReplaceNumber(LostAgility)

                #     LostIntelligence = AttackStatus["Intelligence"]
                #     LostIntelligence = ReplaceNumber(LostIntelligence)

                #     LostStrength = AttackStatus["Strength"]
                #     LostStrength = ReplaceNumber(LostStrength)

                #     GetDamage = AttackStatus["GetDamage"]
                #     GetDamage = ReplaceNumber(GetDamage)

                #     await Channel.send(f"`{Player.Name}` вы убили `{Target.Name}`, нанеся {GetDamage}\nСтатистика `{Target.Name}` упала на : \nУровень : {LostLevel}\nЗдоровье : {LostHealth}\nУрон : {LostDamage}\nЛовкость : {LostAgility}\nИнтеллект : {LostIntelligence}\nСила : {LostStrength}")
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
                        GetGold = random.randint(300,1000 + (1250 * Player.Max_Bonus.Level))
                        GetGold += 300 * Player.Bonus.Level
                        Player.Everyday_bonus.Day = Day
                        Player.Everyday_bonus.Gold = GetGold
                        Player.Gold += GetGold
                        Player.Save()
                        await Channel.send(f"`{Player.Name}` взял(а) ежедневный бонус в размере {GetGold} золотых")
                    else:
                        await Channel.send(f"`{Player.Name}`, Вы уже брали ежедневный бонус в размере {Player.BonusGold} золотых")
            else:
                if Message.author == IamUser:
                    if Commands[1].upper() == "Create".upper():
                        async with Channel.typing():
                            self.Boss.Create(Commands[2])
                            await Channel.send(f"Создан новый босс")
                    else:
                        raise BaseException("Команды не существует")
                else:
                    raise BaseException("Команды не существует")
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
            try:
                async with Channel.typing():
                    if Commands[1].upper() == "Sell".upper():
                        ID = Commands[2]
                        item = Item.Find(int(ID),Player)
                        await Channel.send(item.Sell())
                    else:
                            ID = Commands[1]
                            item = Item.Find(int(ID),Player)
                            await Channel.send(file=item.Profile())
            except:
                raise CommandError("Отсуствует ID и/или режим выбран неправильно.","Item","Item (ID предмета) \nItem Sell (ID предмета)")
        elif Commands[0].upper() == "Upgrade_Item".upper():
            await Message.delete()
            async with Channel.typing():
                try:
                    ID = Commands[1]
                    Gold = Commands[2]
                    item = Item.Find(int(ID),Player)
                    try:
                        await item.Upgrade(int(Gold),self,self.GodsAndCat,Member.id)
                        AllGold = ReplaceNumber(item.AllGold)
                        await Channel.send(file=item.Profile())
                    except BaseException as Error:
                        await Channel.send(f"Ошибка в предмете. \nErrorOutput : {Error}")
                except IndexError:
                    raise CommandError("Пропущен обязательный аргумент","Upgrade_Item","Upgrade_Item ID Монеты")
                except ValueError:
                    raise BaseException(f"Оба аргумента должны быть в 'int'")
        elif Commands[0].upper() == "G".upper():
            await Message.delete()
            if MUTE == True: return
            async with Channel.typing():
                try:
                    if Commands[1].upper() == "S".upper():
                        try: Count = int(Commands[2])
                        except: Count = random.randint(Guild_Function.StandartWords[0],Guild_Function.StandartWords[1])
                        _Message = self.Gabriel.Message(Count,Guild.name,"Usual")
                        await Channel.send(_Message)
                    elif Commands[1].upper() == "D".upper():
                        try: Count = int(Commands[2])
                        except: Count = random.randint(3,7)
                        _Message = self.Gabriel.Message(Count,Guild.name,"D")
                        await Channel.send(_Message)
                    elif Commands[1].upper() == "C".upper():
                        try: Count = int(Commands[2])
                        except: Count = random.randint(3,7)
                        _Message = self.Gabriel.Message(Count,Guild.name,"C")
                        await Channel.send(_Message)
                    else:
                        Types = ["Usual","D","C"]
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
            if Commands[1].upper() == "Point".upper():
                await Message.delete()
                async with Channel.typing():
                    Name = str(Commands[2]).capitalize()
                    Count = int(Commands[3])
                    if Count > Player.Plus:
                        Count = Player.Plus
                    Answer = Player.PlusUpgrade(Count,Name)
                    await Channel.send(embed=Answer)
            else:
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
                raise BaseException(Debuger(Count,int))
        elif Commands[0].upper() == "Equip".upper():
            await Message.delete()
            async with Channel.typing():
                Headers = ["Head","Body","Legs","Boot","Left_hand","Right_hand","Ring_1"
                ,"Ring_2","Ring_3","Ring_4","Ring_5"]
                Embed = discord.Embed(title=f"Инвентарь : {Player.Name}")
                List = [Player.Head,Player.Body,Player.Legs,Player.Boot,Player.Left_hand,Player.Right_hand,Player.Ring_1,Player.Ring_2,Player.Ring_3,Player.Ring_4,Player.Ring_5]
                for index,Equip in enumerate(List):
                    Header = Headers[index]
                    try:
                        Gold = ReplaceNumber(Equip.Gold)
                        MaxGold = ReplaceNumber(Equip.MaxGold)
                        AllGold = ReplaceNumber(Equip.AllGold)
                        Protect = ReplaceNumber(Equip.Protect)
                        Armor = ReplaceNumber(Equip.Unbreaking)
                        Damage = ReplaceNumber(Equip.Damage)
                        Embed.add_field(name=Header,value=f"Название : {Equip.Name}\nОписание : {Equip.Description}\nID : {Equip.ID}\nУрон : {Damage} / Защита : {Protect}\nПрочность : {Armor}\nЗолото : {Gold}/{MaxGold} ({AllGold})\nМагические свойства : {Equip.Magic}",inline=False)
                    except: Embed.add_field(name=Header,value="Ничего не экипировано",inline=False)
                    
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
                    raise BaseException("Поставить новый аватар не удалось")
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
                    raise BaseException("Поставить новый фон не удалось")
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
                    raise BaseException(f"2 Аргумент {Debuger(Count,int)}")
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
                except: raise BaseException("Не указан ID предмета")
                Item_ = Item.Find(ID,Player)
                if Item_.TypeKey.upper() == "Equipment".upper():
                    Player.EquipmentItem(ID,Item_.Where)
                else:
                    try: Where = Commands[2]
                    except: raise BaseException("Не указано куда следует экипировать предмет")
                    
                    Player.EquipmentItem(ID,Where)
                await Channel.send("Вы успешно экипировали предмет")
        elif Commands[0].upper() == "Race".upper():
            await Message.delete()
            async with Channel.typing():
                try: ID = int(Commands[1])
                except: raise BaseException("Не указана лошадь. От 1 до 5")
                try: Gold = int(Commands[2])
                except: raise BaseException("Не указана цена")

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
                    raise BaseException("Ожидалась ссылка")
                Embed.set_image(url=Image)
            except: pass
            await Message.delete()
            _Message = await Channel.send(embed=Embed)
            await _Message.add_reaction(self.VoteOkay)
            await _Message.add_reaction(self.VoteBad)
        elif Commands[0].upper() == "Help".upper():
            Embed = discord.Embed(title="Габриэль помощь",colour=discord.Colour(6828997))
            Embed.set_image(url="https://media.discordapp.net/attachments/730683862836838430/751463545903906816/HelpINFO.png")
            _Message = await Channel.send(embed=Embed)
            await _Message.add_reaction(self.EmodjiGame)
            await _Message.add_reaction(self.EmodjiReference)
            await _Message.add_reaction(self.EmodjiShop)
        else:
            if Message.author.bot == False:
                if random.randint(1,100) <= Guild_Function.ChanceSays:
                    try:
                        Count = random.randint(*Guild_Function.StandartWords)
                        _Message = self.Gabriel.Message(Count,Guild.name,"A",Content)
                        await Channel.send(_Message)
                    except: pass
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
                    elif Commands[0].upper() == "Gabriel".upper():
                        if Commands[1].upper() == "Setup".upper():
                            await Guild_Function.Setup(Channel)
                        elif Commands[1].upper() == "AddChannel".upper():
                            Guild_Function.AddChannel(Channel.id)
                            Guild_Function.SaveStats()
                            await Channel.send(f"Добавлен канал, где я общаюсь с вами `{Channel.id}`")
                        elif Commands[1].upper() == "RemoveChannel".upper():
                            try:
                                Guild_Function.ChannelsForSaveWords.remove(Channel.id)
                                Guild_Function.SaveStats()
                                await Channel.send(f"Убран канал, где я общаюсь с вами `{Channel.id}`")
                            except: raise BaseException("Канал не найден")
                        elif Commands[1].upper() == "BanAddChannel".upper():
                            try:
                                ChannelID = int(Commands[2])
                                if ChannelID not in Guild_Function.ChannelWithIgnoreCommand:
                                    Guild_Function.ChannelWithIgnoreCommand.append(ChannelID)
                                    Guild_Function.SaveStats()
                                    await Channel.send(f"Этот канал стал быть противным `{ChannelID}`")
                                else:
                                    await Channel.send(f"Этот канал и так противен мне`{ChannelID}`")
                            except: raise BaseException("Канал не найден")
                        elif Commands[1].upper() == "BanRemoveChannel".upper():
                            try:
                                ChannelID = int(Commands[2])
                                Guild_Function.ChannelWithIgnoreCommand.remove(ChannelID)
                                Guild_Function.SaveStats()
                                await Channel.send(f"Этот канал перестал быть противным `{ChannelID}`")
                            except: raise BaseException("Канал не найден")
                        elif Commands[1].upper() == "Channels".upper():
                            Embed = discord.Embed(title='Каналы')
                            Embed.add_field(
                                name="Каналы где я общаюсь с вами",
                                value=f"{Guild_Function.ChannelsForSaveWords}",
                                inline=False)
                            Embed.add_field(
                                name="Каналы где меня нет",
                                value=f"{Guild_Function.ChannelWithIgnoreCommand}",
                                inline=False)
                            await Channel.send(embed=Embed)
                        elif Commands[1].upper() == "Info".upper():
                            Embed = discord.Embed(title='Информация о Гильдии')
                            Embed.add_field(
                                name="Каналы где я могу разговаривать",
                                value=f"{Guild_Function.ChannelsForSaveWords}",
                                inline=False)
                            Embed.add_field(
                                name="Каналы которые мне не интересны",
                                value=f"{Guild_Function.ChannelWithIgnoreCommand}",
                                inline=False)
                            Embed.add_field(
                                name="С каким шансом мне стоит отвечать?",
                                value=f"{Guild_Function.ChanceSays}%",
                                inline=False)
                            Embed.add_field(
                                name="Сколько слов я могу использовать? от мин. до макс.",
                                value=f"{Guild_Function.StandartWords}",
                                inline=False)
                            Embed.add_field(
                                name="Эти личности мне не интересны",
                                value=f"{Guild_Function.IngoreMember}",
                                inline=False)
                            Embed.add_field(
                                name="Главный канал",
                                value=f"{Guild_Function.MainChannel}",
                                inline=False)
                            Embed.add_field(
                                name="Канал который я создала",
                                value=f"{Guild_Function.CreatedChannel}",
                                inline=False)
                            Embed.add_field(
                                name="Могу ли я сама разговаривать?",
                                value=f"{Guild_Function.Speak} \nИмеется ввиду, что если каналы настроены верно, то каждые {Guild_Function.EveryTime} секунд, она будет писать, если последнее сообщение не от лица бота",
                                inline=False)
                            Embed.add_field(
                                name="Как часто я могу разговаривать?",
                                value=f"{Guild_Function.EveryTime}с.",
                                inline=False)
                                                       
                            await Channel.send(embed=Embed)
                        elif Commands[1].upper() == "Chance".upper():
                            try: 
                                Count = Commands[2]
                                Count = int(Count)
                            except: raise BaseException(Debuger(Count,int))

                            if Count > 75:
                                Count = 75
                                await Channel.send("Не могу установить шанс больше чем `75%`")

                            Guild_Function.ChanceSays = Count
                            Guild_Function.SaveStats()
                            await Channel.send(f"Теперь я реагирую в `{Count}%`")
                        elif Commands[1].upper() == "Words".upper():
                            try: 
                                Count1 = Commands[2]
                                Count1 = int(Count1)
                            except: raise BaseException(Debuger(Count1,int))

                            try: 
                                Count2 = Commands[3]
                                Count2 = int(Count2)
                            except: raise BaseException(Debuger(Count2,int))


                            if Count1 <= 0:
                                Count1 = 1
                                await Channel.send("Не могу установить минимальное количество слов меньше 1")
                            if Count2 <= 0:
                                Count2 = 1
                                await Channel.send("Не могу установить максимальное количество слов меньше 0")
                            if Count1 >= Count2:
                                Count1 = Count2 - 1
                                await Channel.send("Не могу установить количество слов, больше чем максимальное")
                            if Count2 > 500:
                                Count2 = 500
                                await Channel.send("Не могу установить количество слов больше 500")
                            
                            Guild_Function.Edit(StandartWords=(Count1,Count2))
                            await Channel.send(f"Теперь я использую с {Count1} слов до {Count2}")
                        elif Commands[1].upper() == "Speak".upper():
                            try:
                                Say = bool(int(Commands[2]))
                                Guild_Function.Speak = Say
                                Guild_Function.SaveStats()
                                if Say:
                                    await Channel.send(f"Спасибо что разрешаете мне разговаривать")
                                else:
                                    await Channel.send(f":C")
                            except: raise CommandError("Следует отправлять в аргументе 1 либо 0","Gabriel Speak","Gabriel Speak 1")
                        elif Commands[1].upper() == "EveryTime".upper():
                            Count = Commands[2]
                            try: Count = int(Count)
                            except: raise BaseException(Debuger(Count,int))
                            if Count < 30:
                                Count = 30
                                await Channel.send("Не могу установить скорость ниже 30 секунд.")
                            Guild_Function.EveryTime = Count
                            Guild_Function.SaveStats()
                            await Channel.send(f"Теперь я разговариваю сама, каждые {Count}с.")
                        elif Commands[1].upper() == "Help".upper():
                            Embed = discord.Embed(title='Команды для Габриэль',description="Для того чтобы ими воспользоваться, вам нужны права админа")
                            Embed.add_field(
                                name="Setup",
                                value=f"Устанавливает этот канал главным. А так же создает голосовой канал `{Guild_Function.NameToCreateRoom}`",
                                inline=False)
                            Embed.add_field(
                                name="AddChannel",
                                value=f"Добавить канал в список общения",
                                inline=False)
                            Embed.add_field(
                                name="RemoveChannel",
                                value=f"Убрать канал из списка общения",
                                inline=False)
                            Embed.add_field(
                                name="BanAddChannel",
                                value=f"Буду игнорировать канал",
                                inline=False)
                            Embed.add_field(
                                name="BanRemoveChannel",
                                value=f"Не буду игнорировать канал",
                                inline=False)
                            Embed.add_field(
                                name="Chance",
                                value=f"Изменить шанс, при котором я общаюсь с вами",
                                inline=False)
                            Embed.add_field(
                                name="Words",
                                value=f"Изменить минимальное и максимальное количество слов, которые я использую",
                                inline=False)
                            Embed.add_field(
                                name="Speak",
                                value=f"Разрешить мне общаться без команд",
                                inline=False)
                            Embed.add_field(
                                name="EveryTime",
                                value=f"Каждые {Guild_Function.EveryTime} секунд я буду общаться с вами",
                                inline=False)
                            Embed.add_field(
                                name="Help",
                                value=f"Помощь по этому списку команд",
                                inline=False)
                            Embed.add_field(
                                name="Info",
                                value=f"Узнать текущую информацию об Гильдии",
                                inline=False)
                            await Channel.send(embed=Embed)
                        else:
                            Embed = discord.Embed(title='Команды для Габриэль',description="Вероятно вы где то ошиблись, попробуйте прочитать `Gabriel Help`")
                            
                            await Channel.send(embed=Embed)
                    elif Commands[0].upper() == "ReadMessages".upper():
                        Count = int(Commands[1])
                        if Count > 700:
                            Count = 700
                        try:
                            ChannelID = int(Commands[2])
                            Channel = await self.fetch_channel(ChannelID)
                        except: pass
                        async for message in Channel.history(limit=Count):
                            if message.author != self.user:
                                Content = message.content
                                PlayerName = message.author.name
                                Content = Content.replace('░',"")
                                self.Gabriel.Save(Content,PlayerName,Guild.name)
                    else:
                        if Message.author != self.user:
                            await Guild_Function.CheckMessage(Message,Content,Member)
                            if Channel.id in Guild_Function.ChannelsForSaveWords:
                                self.Gabriel.Save(Content,Player.Name,Guild.name)
                else:
                    if Message.author != self.user:
                        await Guild_Function.CheckMessage(Message,Content,Member)
                        if Channel.id in Guild_Function.ChannelsForSaveWords:
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
                    raise BaseException("Таких команд нет")
            elif Commands[0].upper() == "LevelUpMe".upper():
                Level = int(Commands[1])
                Player.LevelUp(Level)
                R_Level = ReplaceNumber(Level)
                await Channel.send(embed=discord.Embed(title="Поздравляем",description=f"Вы получили {R_Level} уровней",colour=discord.Colour(6655214)))
            elif Commands[0].upper() == "Develop".upper():
                Title = GetFromMessage(Content.replace(Commands[0],""),'"')
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
        # if message.author != self.user:
        #     await self.Command(message)
        #     return
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

    async def on_voice_state_update(self,Member : discord.member.Member, before : discord.member.VoiceState, after : discord.member.VoiceState):
        try: Player = C_Player.Open(Member._user.id)
        except: Player = C_Player(Member._user.id, Member._user.name)

        if after.channel.name == "Создать комнату":
            Guild = after.channel.guild
            if Player.Room.Overwrites is Ellipsis:
                Player.Room.Overwrites = {Member._user.id: discord.PermissionOverwrite(manage_channels=True,move_members=True,manage_roles=True)}

            try: 
                Channel = await self.fetch_channel(Player.Room.Channel)
                await Member.move_to(Channel,reason="Вы создаете точно такую же комнату")
            except:
                try:
                    overwrites = {}
                    for ID in Player.Room.Overwrites:
                        overwrite = Player.Room.Overwrites[ID]
                        User = await Guild.fetch_member(ID)
                        overwrites.update({User:overwrite})
                except: 
                    overwrites = {Member._user.id: discord.PermissionOverwrite(manage_channels=True,move_members=True,manage_roles=True)}
                    Player.Room.Overwrites = overwrites
                NewChannel = await Guild.create_voice_channel(f"{Player.Room.Name}",reason="Новая комната", overwrites=overwrites)
                Player.Room.Channel = int(NewChannel.id)
                await Member.move_to(NewChannel,reason="Новая комната")
        else:
            for _Player in self.Players:
                if before.channel.name == _Player.Room.Name:
                    if len(before.channel.members) <= 0:
                        await before.channel.delete(reason="Комната пустая")
        Player.Save()

        # OurServer = await self.fetch_guild(_Player_.guild.id)
        # EveryOne = OurServer.roles[0]
        # Roles = OurServer.get_role(623063847497891840)
        # return
        # PlayerName = ""
        # for part in str(_Player_.name).split(" "):
        #     PlayerName += part
        # Player = C_Player(PlayerName)
        # try:
        #     Player.GetGuild(after.channel.guild.id)
        #     if after.channel.name == "Создать комнату":
        #         try:
        #             if Player.RoomPermissions == None:
        #                 overwrites = {
        #                     _Player_: discord.PermissionOverwrite(manage_channels=True,move_members=True,manage_roles=True)
        #                 }
        #             else:
        #                 SavedOverwrites = Player.RoomPermissions
        #                 overwrites = dict()
        #                 for overwrite in SavedOverwrites:
        #                     _Member = await OurServer.fetch_member(overwrite)
        #                     overwrite = SavedOverwrites[overwrite]
        #                     overwrites.update({_Member : discord.PermissionOverwrite(**overwrite)})

        #             NewGroup = await OurServer.create_voice_channel(f"{Player.RoomName}",reason="Новая комната", overwrites=overwrites)
                    
        #             await _Player_.move_to(NewGroup,reason="Новая комната")
        #         except:
        #             NewGroup = await OurServer.create_voice_channel(f"{Player.RoomName}",reason="Новая комната")
                    
        #             await _Player_.move_to(NewGroup,reason="Новая комната")
        #     elif after.channel.name == "Создать комнату (Истинный чат)":
        #         try:
        #             if Player.RoomPermissions == None:
        #                 overwrites = {
        #                     _Player_ : discord.PermissionOverwrite(manage_channels=True,move_members=True,manage_roles=True),
        #                     Roles : discord.PermissionOverwrite(connect=True),
        #                     EveryOne : discord.PermissionOverwrite(connect=False)
        #                 }
        #             else:
        #                 SavedOverwrites = Player.RoomPermissions
        #                 overwrites = dict()
        #                 for overwrite in SavedOverwrites:
        #                     _Member = await OurServer.fetch_member(overwrite)
        #                     overwrite = SavedOverwrites[overwrite]
        #                     overwrites.update({_Member : discord.PermissionOverwrite(**overwrite)})
        #             overwrites.update({Roles : discord.PermissionOverwrite(connect=True)})
        #             NewGroup = await OurServer.create_voice_channel(f"{Player.RoomName}",overwrites=overwrites,reason="Новая комната")
        #             await _Player_.move_to(NewGroup,reason="Новая комната")
        #         except:
        #             NewGroup = await OurServer.create_voice_channel(f"{Player.RoomName}",reason="Новая комната")
        #             await _Player_.move_to(NewGroup,reason="Новая комната")
        # except Exception: pass
        # try:
        #     CurGroup = await self.fetch_channel(before.channel.id)
        #     Members = CurGroup.members
        #     NotDeleteChannels = ["Создать комнату","Резерв","Музыка","Создать комнату (Истинный чат)"]
        #     if len(Members) == 0 and str(CurGroup.name) not in NotDeleteChannels:
        #         await CurGroup.delete(reason="В комнате никого нет")
        # except Exception: pass
    
    async def on_member_join(self,Member : discord.member.Member):
        try:
            OurServer = await self.fetch_guild(419879599363850251)
            StartRole = OurServer.get_role(691735620346970123)
            await Member.add_roles(StartRole,reason="Впервые зашел на сервер")
        except: pass

    async def on_guild_channel_update(self,before,after):

        for Player in self.Players:
            if Player.Room.Name == before.name:
                Player.Room.Name = str(after.name)
                overwrites = after.overwrites
                for member in overwrites:
                    Permissions = overwrites[member]
                    Player.Room.Overwrites.update({member.id:Permissions})
                print(overwrites)
                print(Player.Room.Overwrites)
                Player.Save()


        # overwrites = before.overwrites
        # PermissionsAll = dict()
        # Maines = list()
        
        # for overwrite in overwrites:
        #     try:
        #         permissions = overwrite.permissions
        #     except AttributeError:
        #         permissions = overwrite.permissions_in(before)
                
        #         _Permissions = dict()
        #         for Permission in permissions:
        #             _Permissions.update({Permission[0]:Permission[1]})
        #         PermissionsAll.update({overwrite.id:_Permissions})
    
        #         if permissions.manage_channels == True:
                    
        #             PlayerName = ""
        #             for part in str(overwrite.name).split(" "):
        #                 PlayerName += part
        #             Maines.append(PlayerName)
        # for _PlayerName in Maines:
            # Player = C_Player(_PlayerName)
            # Player.SaveRoom(after.guild.id,after.name,PermissionsAll)
    
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
        # EmodjsInDevelop = await DevelopGabriel.fetch_emojis()
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
        elif Emoji == self.VoteBad:
            if Player != self.user:
                await Message.remove_reaction(self.VoteOkay,Member)
        elif Emoji == self.EmodjiGame:
            if Player != self.user:
                await Message.clear_reactions()
                Embed = discord.Embed(
                    title="Габриэль помощь по игре",
                    description="Ниже указаны все команды связанные о игре. и их краткое содержание",
                    colour=discord.Colour(5086956))
                Embed.add_field(
                    name="Profile (и/или ник другого игрока)",
                    value="Открытие вашего(или другого игрока) профиля",
                    inline=False
                )
                Embed.add_field(
                    name="Attack (Имя игрока)",
                    value="Вы атакуете выбранного вами игрока",
                    inline=False
                )
                Embed.add_field(
                    name="Event",
                    value="Не является полноценной командой. Подробнее ниже",
                    inline=False
                )
                Embed.add_field(
                    name="Event Profile",
                    value="Открыть профиль Босса",
                    inline=False
                )
                Embed.add_field(
                    name="Event Attack",
                    value="Атаковать Босса",
                    inline=False
                )
                Embed.add_field(
                    name="Event Bonus",
                    value="Взять ежедневную награду",
                    inline=False
                )
                Embed.add_field(
                    name="Event Create (Команда Администрации)",
                    value="Создать босса. Аргумент : Сложность Босса",
                    inline=False
                )
                Embed.add_field(
                    name="Inv",
                    value="Открытие вашего инвентаря",
                    inline=False
                )
                Embed.add_field(
                    name="Item (ID предмета)",
                    value="Узнать информацию о предмете",
                    inline=False
                )
                Embed.add_field(
                    name="Upgrade_Item (ID предмета) (Золотых)",
                    value="Прокачать предмет",
                    inline=False
                )
                Embed.add_field(
                    name="Talants",
                    value="Открытие списка ваших талантов",
                    inline=False
                )
                Embed.add_field(
                    name='Talant "(Англ. название таланта)"',
                    value="Поставить талант на прокачку",
                    inline=False
                )
                Embed.add_field(
                    name="Talant Point (Сила, Ловкость, Интеллект)",
                    value="Потратить очки навыков на (см. выше)",
                    inline=False
                )
                Embed.add_field(
                    name="Number (Число)",
                    value="Не является полноценной командой. Нужна чтобы сокращать цифры. Пример : Number 10000. Будет 10K",
                    inline=False
                )
                Embed.add_field(
                    name="Equip",
                    value="Узнать что на вас сейчас экипированно",
                    inline=False
                )
                Embed.add_field(
                    name="Nev_Avatar (ссылка на аватар)",
                    value="Изменить аватар в профиле",
                    inline=False
                )
                Embed.add_field(
                    name="New_Background (ссылка на фон)",
                    value="Изменить фон в профиле",
                    inline=False
                )
                Embed.add_field(
                    name="Wear (ID предмета) (Куда следует экипировать. Не обязательно для самой экипировки. Англ название. Пример : Left_hand)",
                    value="Экипируете выбранный предмет, получая его характеристики, и/или дополнительные свойства",
                    inline=False
                )
                Embed.add_field(
                    name="Race (лошадь от 1 до 5) (ставка)",
                    value="Поставить на X лошадь. в Случае победы ставка возрастет",
                    inline=False
                )
                Embed.add_field(
                    name="Item Sell (ID предмета)",
                    value="Продать выбранный предмет",
                    inline=False
                )
                Embed.set_image(url="https://media.discordapp.net/attachments/730683862836838430/751463545903906816/HelpINFO.png")
                await Message.edit(embed=Embed)
                await Message.add_reaction(self.EmodjiGame)
                await Message.add_reaction(self.EmodjiReference)
                await Message.add_reaction(self.EmodjiShop)
        elif Emoji == self.EmodjiShop:
            if Player != self.user:
                await Message.clear_reactions()
                Embed = discord.Embed(
                    title="Габриэль помощь по магазину",
                    description="Ниже указаны все ценники, и использование команды магазина",
                    colour=discord.Colour(15394144))
                Embed.add_field(
                    name="Shop (Товар) (Количество)",
                    value="Товары указаны ниже. И их стоимость",
                    inline=False
                    )
                Embed.add_field(
                    name="Лечение (15 золотых за штуку)",
                    value="Лечит вашего персонажа на 3К за штуку",
                    inline=False
                    )
                Embed.add_field(
                    name="Здоровье (100 золотых за штуку)",
                    value="Увеличивает вашему персонажу здоровье на 35 ед. за штуку",
                    inline=False
                    )
                Embed.add_field(
                    name="Урон (50 золотых за штуку)",
                    value="Увеличивает урон от кулаков на 50 ед. за штуку",
                    inline=False
                    )
                Embed.add_field(
                    name="Уровень (300 золотых за штуку)",
                    value="Увеличивает уровень вашего персонажа на 1 за штуку. (Является полноценным получением уровня. Означает вы получаете 100% из этого уровня)",
                    inline=False
                    )
                Embed.set_image(url="https://media.discordapp.net/attachments/730683862836838430/751463545903906816/HelpINFO.png")
                await Message.edit(embed=Embed)
                await Message.add_reaction(self.EmodjiGame)
                await Message.add_reaction(self.EmodjiReference)
                await Message.add_reaction(self.EmodjiShop)
        elif Emoji == self.EmodjiReference:
            if Player != self.user:
                await Message.clear_reactions()
                Embed = discord.Embed(
                    title="Габриэль справка",
                    description="Справка по Габриэль. И все оставшиеся команды",
                    colour=discord.Colour(15394144))
                Embed.add_field(
                    name="G (S/D/B - не обязательны) (Число - не обязательно)",
                    value="Габриэль скажет что либо. Для того чтобы она говорила (см. ниже)",
                    inline=False)
                Embed.add_field(
                    name="Gs (ID голосовой комнаты - не обязательно, если вы подключаете её в ту же комнату, где и вы)",
                    value="Заставляет Габриэль зайти в вашу голосовую комнату, и произвести одно из заранее подготовленных аудио (Внимание, временно не работает)",
                    inline=False)
                Embed.add_field(
                    name='Wiki "(Что следует найти в Википедии)"',
                    value="Габриэль найдет это в Википедии. Если же нет, то покажет похожие",
                    inline=False)
                Embed.add_field(
                    name='Vote "(Название)" "(Описание. Не обязательный аргумент)" "(URL картинка. Не обязательный аргумент)"',
                    value="Запускает голосование, где вы выбираете название, описание, и картинку",
                    inline=False)
                Embed.add_field(
                    name="Gabriel Help",
                    value=f"Следующий список команд. Находиться в отдельном списке, так как он нужен для Администрации `{Guild.name}`",
                    inline=False)
                Embed.add_field(
                    name="Вопросы и ответы",
                    value="Далее ответ - вопрос",
                    inline=False)
                Embed.add_field(
                    name="Почему Габриэль постоянно улыбается?",
                    value="Габриэль поддерживает актив. Из за чего когда вы улыбаетесь, она улыбается тоже!",
                    inline=False)
                Embed.add_field(
                    name="Почему Габриэль молчит?",
                    value="Видимо установка прошла мимо вас. Чтобы исправить это, необходимо её установить. (см. команду Gabriel Help)",
                    inline=False)
                Embed.add_field(
                    name="Почему Габриэль разговаривает сама по себе?",
                    value="Изначально если Габриэль видит что последнее сообщение не от лица бота, она понимает что актив упал. И возможно если она напишет что либо, актив вернется. \n`Чтобы это убрать, смотрите команду Gabriel Help`",
                    inline=False)
                
                Embed.set_image(url="https://media.discordapp.net/attachments/730683862836838430/751463545903906816/HelpINFO.png")
                await Message.edit(embed=Embed)
                await Message.add_reaction(self.EmodjiGame)
                await Message.add_reaction(self.EmodjiReference)
                await Message.add_reaction(self.EmodjiShop)

    async def AddOneRole(self,ID,Member,Guild,RolesID):
        Role = Guild.get_role(ID)
        await Member.add_roles(Role,reason="Выбрал роль")
        for role in Member.roles:
            if role.id in RolesID and role != Role:
                await Member.remove_roles(role,reason="Убрана старая роль")

    def Fetch_Players(self,Content : str):
        """ Найти имя в тексте """
        f = Content.split(" ")[0]
        NickName = Content.replace(f"{f} ","").upper()
        FoundList = list()
        for player in self.Players:
            if player.Name.upper() == NickName:
                Player = player
                FoundList.append(player)
        return FoundList

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
