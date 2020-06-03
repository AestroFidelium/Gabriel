import discord
import BazaDate
from discord import user
import time
import random

class Error():
    pass

def is_internet():
    """
    Query internet using python
    :return:
    """
    
    try:
        urlopen('https://www.google.com', timeout=1)
        
        return True
    except urllib.error.URLError:
        return False
def InternetActive():
    client = MyClient()
    try:
        client.run(BazaDate.token)
    except: 
        print("Нет подключения к интернету")
class MyClient(discord.Client):

    async def on_ready(self):
        print(f"Loggined")#permissions edit
        # newGuild = await self.create_guild("Прикол да?")
        #716945063351156736
        # GodsAndCat = await self.fetch_guild(419879599363850251)
        # Administrator_Role = GodsAndCat.get_role(578514082252980234)
        # OldSettings = Administrator_Role.colour
        # Guild = await self.fetch_guild(716945063351156736)
        # Me = await Guild.fetch_member(414150542017953793)
        # # await NewGroup.set_permissions(Me,manage_channels=True,move_members=True,manage_roles=True,reason="Новая комната")
        # # Role = await Guild.create_role(name="Кот")
        # Role = Guild.get_role(716947955160186891)
        # await Role.edit(colour=OldSettings)
        # await Me.add_roles(Role)
        # newGuild = await self.fetch_guild(419879599363850251)
        # sfs = discord.Invite(newGuild)
        # print(sfs)
        # RandomChannel = await newGuild.fetch_channels()
        # for channel in RandomChannel:
        #     try:
        #         Invite = await channel.create_invite()
        #         print(Invite)
        #     except: pass
    async def on_typing(self,channel, user, when):
        print(channel)
        print(user)
        print(when)
        pass
InternetActive()

while True:
    time.sleep(1)
    if is_internet():
        if(internetWasOff == True):
            print("Internet is active")
            InternetActive()
            internetWasOff = False
    else:
        internetWasOff = True