import discord
import ffmpeg
import BazaDate
import urllib
import time
import random
import wget
import PIL
import os
import ast
from bs4 import BeautifulSoup
import requests
import datetime
import asyncio
import codecs
from myConfg import *
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
   
    async def Command(self):
        if self.Commands[0].upper() == "2Profile".upper():
            # await self.Message.delete()
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
            self.Player.LevelUp(C_Player.mode.multiply,count=1000000000)
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
            await self.Channel.send(" ",file=self.Boss.Profile())
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
        self.Guild = await self.fetch_guild(message.channel.guild.id)

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
        
        self.Boss = Boss()

        await self.DownloadAvatar()
        await self.Command()
        

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
