import ffmpeg
import BazaDate
import urllib
import time

#pylint: disable=unused-wildcard-import
from Functions2 import *


class MyClient(discord.Client):

    async def on_ready(self):
        print(f"Logged on as , {self.user}")
        Activites = [discord.Activity(
                        type=discord.ActivityType.listening, 
                        name="твои истории"),
                    discord.Activity(
                        type=discord.ActivityType.listening, 
                        name="твои проблемы"),
                    discord.Activity(
                        type=discord.ActivityType.watching, 
                        name="в будущее"),
                    discord.Activity(
                        type=discord.ActivityType.watching, 
                        name="в окно"),
                    discord.Activity(
                        type=discord.ActivityType.listening, 
                        name="музыку"),
                    discord.Activity(
                        type=discord.ActivityType.watching, 
                        name="как моляться Богам фпса"),
                    discord.Activity(
                        type=discord.ActivityType.watching, 
                        name="на твою историю браузера ;D"),
                    discord.Activity(
                        type=discord.ActivityType.watching, 
                        name="в даль")]
        
        await self.change_presence(
            activity=Activites[random.randint(0,len(Activites) - 1)])
        
        self.Gabriel = C_Gabriel.Gabriel.Open()

        channel = await self.fetch_channel(623070280973156353)

        # Gabriel_Guild = self.Gabriel.GetGuild(419879599363850251)
        # if Gabriel_Guild == False:
        #     Gabriel_Guild = C_Gabriel.Guild(419879599363850251,"Боги и Кот")
        #     Gabriel_Guild.Save(self.Gabriel)

        # channel = await self.fetch_channel(419879599363850253)
        # index = 0
        # async for message in channel.history(limit=100000):
        #     index += 1
        #     print(index)
        #     if message.author.bot == False:
        #         g_user = C_User.Open(message.author.id,message.author.name)
        #         Gabriel_Guild.Save_Line(C_Gabriel.Message(message.id,message.content,g_user))
        # Gabriel_Guild.Save(self.Gabriel)
        print("работает все да")
    
    async def Command(self,Message : discord.Message, Channel : discord.TextChannel,Guild : discord.Guild,User : discord.User):
        """ Команды """

        # Добавляем монеты и максимальное кол.во сообщений
        G_User = C_User.Open(User.id,User.name)
        G_User.Messages += 1
        G_User.Add()
        G_User.LastMessage = datetime.datetime.now()
        G_User.Save()

        # Получаем информацию об Гильдии
        Gabriel_Guild = self.Gabriel.GetGuild(Guild.id)

        if Gabriel_Guild == False:
            Gabriel_Guild = C_Gabriel.Guild(Guild.id,Guild.name)
            Gabriel_Guild.Save(self.Gabriel)

        # Запись в список всех игроков

        if G_User.ID not in self.Gabriel.Users:
            self.Gabriel.Users.append(G_User.ID)
    

        # Тестовое поле



        # --------------

        IsCommand = Message.content.lower().startswith(Gabriel_Guild.StartsWith.lower())

        if IsCommand:
            _splited = Message.content.split(Gabriel_Guild.StartsWith.lower())[-1].split(" ")
            Command = C_Command(_splited.pop(0),_splited)


            if Command.Name.lower() == "profile":
                embed = discord.Embed(title=G_User.Name,colour=User.colour)
                embed.set_thumbnail(url=User.avatar_url)
                embed.add_field(name="Сообщений",value=ReplaceNumber(G_User.Messages),inline=False)
                embed.add_field(name="Лолилиес",value=ReplaceNumber(G_User.Lolilies),inline=False)
                await Channel.send(" ",embed=embed,delete_after=300)
        elif [True for mention in Message.mentions if mention == self.user] or [True for Reaction_on in Gabriel_Guild.Gabriel_Reaction_on if Message.content.startswith(Reaction_on)]:
            try: 
                await Channel.send(Gabriel_Guild.Answer(random.randint(*Gabriel_Guild.StandartWords),GetMessage=Message.content))
            except: 
                embed = discord.Embed(title="Продолжайте общаться!",description='Извините, мне не удалось сгенерировать сообщение, скорее всего это связанно с тем что вы не общаетесь. Продолжайте общение, и эта ошибка пропадёт')
                embed.set_footer(text="Сообщение удалиться через 35 секунд",icon_url="https://bit.ly/3nyxgx4")
                await Channel.send(embed=embed,delete_after=35)
        else:
            if Gabriel_Guild.Speak:
                if await Gabriel_Guild.CheckMessage(Message,Message.content,User,self) == False:
                    Gabriel_Guild.Save_Line(C_Gabriel.Message(Message.id,Message.content,G_User))
                    Gabriel_Guild.CurMessageEvery -= 1
                    if Gabriel_Guild.CurMessageEvery <= 0:
                        Gabriel_Guild.CurMessageEvery = Gabriel_Guild.MessageEvery
                        try: await Channel.send(Gabriel_Guild.Answer(random.randint(*Gabriel_Guild.StandartWords),GetMessage=Message.content))
                        except: pass
                    Gabriel_Guild.Save(self.Gabriel)
                else:
                    G_User.Remove(1000)


    async def on_message(self,message : discord.Message):
        if message.author != self.user:
            await self.Command(Message=message,
                                    Channel=message.channel,
                                    Guild=message.guild,
                                    User=message.author)
            return
        try:
            if message.author.bot == False:
                await self.Command(Message=message,
                                    Channel=message.channel,
                                    Guild=message.guild,
                                    User=message.author)
        except OverflowError:
            Embed = discord.Embed(title="Ваша статистика бессконечна",description=f"Из за этого ваши действия невозможно реализовывать",colour=discord.Colour.red())
            await message.channel.send(embed=Embed,delete_after=60)
        except OSError:
            Embed = discord.Embed(title="Ошибка / Внимание",description=f"{message.author.mention} , не могу создать аккаунт под ваше имя \nЛибо аккаунт был только что создан",colour=discord.Colour.red())
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
    
    async def on_voice_state_update(self,Member : discord.member.Member, _before : discord.member.VoiceState, _after : discord.member.VoiceState):
        """ Вход и выход в голосовых каналах """

        # Переменные
        User = C_User.Open(Member.id,Member.name)
        before = _before.channel
        after = _after.channel
    
        # Есть следующий голосовой канал
        if after:
            Guild = after.guild

            Gabriel_Guild = self.Gabriel.GetGuild(after.guild.id)
            if Gabriel_Guild == False:
                Gabriel_Guild = C_Gabriel.Guild(after.guild.id,after.guild.name)
                Gabriel_Guild.Save(self.Gabriel)

            if after.name == Gabriel_Guild.Name_rooms_create:
                try:
                    Channel = await self.fetch_channel(User.YourRoom)
                    await Member.move_to(Channel,reason="Вы создаете точно такую же комнату")
                except:
                    RoomName = User.Name
                    Overwrites = None

                    guildRoom = getattr(User,after.guild.name,False)
                    if guildRoom:
                        RoomName = guildRoom.Name
                        Overwrites = guildRoom.Overwrites

                    channel = await Guild.create_voice_channel(RoomName,reason="Новая комната",overwrites=Overwrites)
                    await Member.move_to(channel,reason="Новая комната")
                    User.YourRoom = channel.id
                    User.Save()

        # Есть прошлый голосовой канал
        if before:
            Guild = before.guild
            if len(before.members) <= 0:
                for ID in self.Gabriel.Users:
                    User = C_User.Open(ID)
                    if User.YourRoom == before.id:
                        await before.delete(reason="Комната пустая")

    async def on_guild_channel_update(self,before : discord.channel.VoiceChannel,after : discord.channel.VoiceChannel):
        """ Обновление в голосовых каналах """
        
        # Проверка смены название канала
        if after.name != before.name:
            for ID in self.Gabriel.Users:
                User = C_User.Open(ID)
                if User.YourRoom == before.id:
                    User.__setattr__(before.guild.name,GuildRooms(after.name,after.overwrites))
                    User.Save()
    
    async def on_raw_reaction_add(self,payload):
        Channel = await self.fetch_channel(payload.channel_id)
        Guild = await self.fetch_guild(419879599363850251)
        Member = await Guild.fetch_member(payload.user_id)
        Emoji = payload.emoji
        

        if Member == self.user: return

        # Справка
        if Channel.id == 623070280973156353:
            Message = await Channel.fetch_message(payload.message_id)
            await Message.remove_reaction(Emoji,Member)

            class Role_In_Emodji():
                def __init__(self, Emodji : str, Role : int):
                    self.Emodji = Emodji
                    self.Role   = Role

            LLl = [Role_In_Emodji("black_circle",713477362058002535)]

            URL = str(Emoji.url)
            
            if URL.startswith("http"):
                Emoji_name = str(Emoji.name)
                if Emoji_name not in os.listdir("./Resurses/Colours"):
                    Download_Image(URL,f"./Resurses/Colours/{Emoji_name}.png")
                Emoji_Image = Image.open(f"./Resurses/Colours/{Emoji_name}.png")
                PixelColor = Emoji_Image.getpixel((Emoji_Image.size[0] / 2, Emoji_Image.size[1] / 2))
                Colour = rgbToColor(PixelColor[0],PixelColor[1],PixelColor[2])

                for role in Guild.roles:
                    if role._colour == Colour:
                        Standart = Guild.get_role(610078093260095488)
                        StartRole = Guild.get_role(691735620346970123)
                        await Member.add_roles(Standart,role,reason="Сменил цвет")
                    elif str(role.name).find(" цвет") >= 0 and role._colour != Colour:
                        if role in Member.roles:
                            await Member.remove_roles(role,reason="Сменил цвет")
def main():
    client = MyClient()
    client.run(BazaDate.token)

if __name__ == "__main__":
    main()