import pygame
import asyncio
import time
import discord
import BazaDate
import os
from botFunctions import StrToDict

def printText(screen,message,x,y,color,size):
    font_text = pygame.font.Font("Arial.ttf",size)
    text = font_text.render(message, True,color)
    screen.blit(text,(x,y))


async def main(self):
    pygame.init()
    width, height = 986, 768
    screen = pygame.display.set_mode((width, height),pygame.FULLSCREEN)

    BackGround = pygame.image.load("Main.png").convert_alpha() 

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
            printText(screen,MyMessage,300,650,(255,255,255),30)
        printText(screen,Channel.name,50,700,(255,255,255),30)
        pygame.display.flip()

class MyClient(discord.Client):
    async def on_ready(self):
        print("В сети")
        await main(self)
        # task1 = asyncio.create_task(main(self))
        # asyncio.gather(task1)



def InternetActive():
    client = MyClient()
    client.run(BazaDate.token)

InternetActive()