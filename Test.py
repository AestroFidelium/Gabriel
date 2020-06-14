import discord
import BazaDate
import time
import random
import asyncio
import aiohttp

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
    async def _TimeShow(self,Member,Channel):
        Timer = 100
        while Timer > 0:
            Timer -= 1
            print(Timer)
        overwrite = discord.PermissionOverwrite()
        overwrite.send_messages = False
        overwrite.read_messages = False
        await Channel.set_permissions(Member,overwrite=overwrite)
        print("Конец")
    async def on_ready(self):
        print(f"Loggined")
        # WebHook = discord.Webhook(721170179010199592,"SecCttffdkCnj7FaCuvWJX3t2KM9rKWSWe3I73ffj6kQjuhadIXTklDMvsXhdndLif9U")
        # WebHook.send("da")
        # async with aiohttp.ClientSession() as session:
        #     webhook = Webhook.from_url('https://discordapp.com/api/webhooks/721170179010199592/SecCttffdkCnj7FaCuvWJX3t2KM9rKWSWe3I73ffj6kQjuhadIXTklDMvsXhdndLif9U', adapter=AsyncWebhookAdapter(session))
        #     await webhook.send('Hello World', username='Foo')

        # Guild = await self.fetch_guild(419879599363850251)
        # print(await Guild.webhooks())
        # Channels = [721150391445749882,721150365361242138,721150111320899586]
        # NewPlayer = await Guild.fetch_member(414150542017953793)
        # Tasks = list()
        # for Channel in Channels:
        #     Members = list()
        #     Channel = await self.fetch_channel(Channel)
        #     for Member in Channel.members:
        #         Permissions = Channel.permissions_for(Member)
        #         if Permissions.administrator == False:
        #             Members.append(Member)
        #     for Member in Members:
        #         task = asyncio.create_task(self._TimeShow(Member,Channel))
        #         Tasks.append(task)
        # asyncio.gather(*Tasks)
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