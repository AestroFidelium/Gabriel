import pygame
import asyncio
import time
import discord
import BazaDate
import os
from botFunctions import StrToDict

def printText(screen,message,x,y,color,size):
    """
    Вывести на экран
    """
    font_text = pygame.font.Font("Arial.ttf",size)
    text = font_text.render(message, True,color)
    screen.blit(text,(x,y))

class MyClient(discord.Client):
    async def main(self):
        pygame.init()
        width, height = 1366, 768
        screen = pygame.display.set_mode((width, height),pygame.FULLSCREEN)
        # screen = pygame.display.set_mode((width, height))

        BackGround = pygame.image.load("Main.png").convert_alpha() 

        BackGround = pygame.transform.scale(BackGround, (width, height))
        
        Servers = os.listdir("./Servers/")
        ChannelsAll = list()
        for server in Servers:
            with open(f"./Servers/{server}/ServerConfig.txt","r") as file:
                Config = StrToDict(str=str(file.readline()))
            
            ServerID = int(Config["ID"])
            Server = await self.fetch_guild(ServerID)
            Channels = await Server.fetch_channels()
            for channel in Channels:
                type = channel.type
                type = str(type)
                if type == "text":
                    ChannelsAll.append(channel.id)

        MyMessage = ""
        DeleteMessages = False
        NewSplash = False
        Index = 0
        ID = ChannelsAll[Index]
        Channel = await self.fetch_channel(ID)
        while True:
            await asyncio.sleep(0.01)
            if DeleteMessages == True:
                MyMessage = MyMessage[:-1]
            screen.blit(BackGround, (0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        await Channel.send(MyMessage)
                        MyMessage = ""
                    elif event.key == pygame.K_BACKSPACE:
                        DeleteMessages = True
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit() 
                        return
                    elif event.key == pygame.K_UP:
                        MaxIndex = len(ChannelsAll)
                        Index += 1
                        if Index >= MaxIndex:
                            Index = 0
                        ID = ChannelsAll[Index]
                        Channel = await self.fetch_channel(ID)
                    elif event.key == pygame.K_DOWN:
                        MaxIndex = len(ChannelsAll)
                        Index -= 1
                        if Index < 0:
                            Index = MaxIndex - 1
                        ID = ChannelsAll[Index]
                        Channel = await self.fetch_channel(ID)
                    else:
                        MyMessage += event.unicode
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_BACKSPACE:
                        DeleteMessages = False
            
            if len(MyMessage) > 0:
                printText(screen,MyMessage,57,694,(255,255,255),30)
            printText(screen,Channel.name,1191,64,(255,255,255),30)
            # print(self.Chat)
            Scale = 16
            ChatX = int(45 - Scale)
            ChatY = 3
            Count = 3
            Fst = None
            for Chat in self.Chat:
                Author = Chat["Author"]
                Guild = Chat["Guild"]
                Channel = Chat["Channel"]
                Message = Chat["Message"]
                ChatY += 50
                if Count > 0:
                    MessageShow = f"[{Guild.name}][{Channel.name}] {Author.name} : {Message.content}"
                    printText(screen,MessageShow,ChatX,ChatY,(75,125,170),Scale)
                else:
                    self.Chat.pop(0)
                Count -= 1
            pygame.display.flip()
    async def on_ready(self):
        print("В сети")
        self.Chat = []
        await self.main()
        mainMenu = asyncio.create_task(self.main())
        asyncio.gather(mainMenu)
    async def on_message(self,message):
        if str(message.content) != " ":
            User = await self.fetch_user(message.author.id)
            Guild = await self.fetch_guild(message.channel.guild.id)
            Channel = await self.fetch_channel(message.channel.id)
            NewDict = {
                "Author" : User,
                "Guild" : Guild,
                "Channel" : Channel,
                "Message" : message
            }
            self.Chat.append(NewDict)


def InternetActive():
    client = MyClient()
    client.run(BazaDate.token)

InternetActive()