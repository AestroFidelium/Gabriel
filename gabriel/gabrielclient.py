import discord
import random

from .BazeData import *
from .logic import *




class GabrielClient(discord.Client):
    """Запуск Габриэль происходит инициализацией команды run этого класса

    Args:
        discord (str): Токен бота
    """

    async def on_ready(self):
        print(f"Logged on as , {self.user}")

        listening = discord.ActivityType.listening
        watching = discord.ActivityType.watching
        Activity = discord.Activity

        Activites = [
            Activity(
                type=listening,
                name="твои истории"),
            Activity(
                type=listening,
                name="твои проблемы"),
            Activity(
                type=watching,
                name="в будущее"),
            Activity(
                type=watching,
                name="в окно"),
            Activity(
                type=listening,
                name="музыку"),
            Activity(
                type=watching,
                name="как моляться Богам фпса"),
            Activity(
                type=watching,
                name="на твою историю браузера ;D"),
            Activity(
                type=watching,
                name="в даль"),
            Activity(
                type=listening,
                name="тебя"),
            Activity(
                type=watching,
                name="на звёзды"),
            Activity(
                type=watching,
                name="аниме"),
            Activity(
                type=watching,
                name="на онлайн"),
            Activity(
                type=listening,
                name="Spotify"),
            Activity(
                type=listening,
                name="оправдания")]

        await self.change_presence(
            activity=Activites[random.randint(0, len(Activites) - 1)])

        print("работает все да")

    async def command(self,
                      Message: discord.Message,
                      Channel: discord.TextChannel,
                      Guild: discord.Guild,
                      User: discord.User):
        """

        Args:
            Message: Сообщение
            Channel: Канал
            Guild: Гильдия
            User: Пользователь

        Returns:

        """

        _GabrielUser = GabrielUser.Open(User.id, User.name)

        print(_GabrielUser.Name)

        _GabrielUser.NewMessage()
        _GabrielUser.Save()

    async def on_message(self, message: discord.Message):
        if message.author.bot == False:
            await self.Command(Message=message,
                               Channel=message.channel,
                               Guild=message.guild,
                               User=message.author)



def RunDiscord():
    client = GabrielClient()
    client.run(token)




if __name__ == "__main__":
    RunDiscord()
