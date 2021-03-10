import discord
import requests
import bs4
import requests
import random
import codecs
import re
import pickle







class GabrielUser():
    """Пользователь и вся информация
    """

    def __init__(self, ID : int ,Name : str = None) -> None:
        """Создать нового пользователя

        Args:
            ID (int): ID пользователя (дискорда)
            Name (str, optional): Ник пользователя. Defaults to None.
        """
        self.Name      = Name
        self.Lolilies  = 0
        self.Messages  = 0
        self._messages = 0
        self.ID        = ID
        self.Rooms     = []

        self.likes     = 0
        self.dislikes  = 0
        self.Posts     = []
    
    def NewMessage(self):
        """Новое сообщение
        """
        self.Messages += 1
        self._messages += 1
        if self._messages >= 10:
            self.Lolilies += 1
            self._messages = 0
    
    def Save(self):
        """Сохранить статистику пользователя
        """
        copy = self.Open(self.ID,Save=True)
        with codecs.open(f"./Statictics/{self.ID}.gabriel","wb") as file:
            try: pickle.dump(self,file)
            except BaseException as ERROR: 
                pickle.dump(copy,file)
                raise ERROR("Не удалось сохранить новую информацию пользователя")

    @staticmethod
    def Open(ID : int, Name : str = None, Save = False) -> "GabrielUser":
        """Открыть информацию пользователя

        Returns:
            User: Пользователь
        """
        try:
            with codecs.open(f"./Statictics/{ID}.gabriel","rb") as file:
                return pickle.load(file)
        except FileNotFoundError:
            if Save == False:
                print(f"[{Name}] Новый аккаунт")
            return GabrielUser(ID=ID,Name=Name)
        except EOFError:
            if Save == False:
                print(f"[{Name}] пустой аккаунт")
            return GabrielUser(ID=ID,Name=Name)

    class Room():
        def __init__(self, Guild : str, Name : str, Permission) -> None:
            self.Guild = Guild
            self.Name  = Name
            self.Permission = Permission

class Gabriel():
    def __init__(self) -> None:
        self.Guilds = list()


    def Save(self):
        """Сохранить статистику пользователя
        """
        copy = self.Open(Save=True)
        with codecs.open(f"./Statictics/Gabriel.gabriel","wb") as file:
            try: pickle.dump(self,file)
            except BaseException as ERROR: 
                pickle.dump(copy,file)
                raise ERROR("Габриэль не смогла сохраниться")

    @staticmethod
    def Open(Save : bool) -> "Gabriel":
        """Открыть профиль Габриэль

        Returns:
            Gabriel: Класс Габриэль
        """
        try:
            with codecs.open(f"./Statictics/Gabriel.gabriel","rb") as file:
                return pickle.load(file)
        except FileNotFoundError:
            if Save == False:
                print(f"Габриэль была заново инициализированна")
            return Gabriel()
        except EOFError:
            if Save == False:
                print(f"Габриэль не удалось прочитать пустой файл")
            return GabrielUser()


class Post():
    def __init__(self, ID : int) -> None:
        self.ID = ID


        self.Likes = 0
        self.Dislikes = 0

        self.Likers = []
        self.Dislikers = []
    
    def __repr__(self) -> str:
        return f"Post#{self.ID}"

class GabrielGuild():
    """Габриэль-гильдия
    """

    def __init__(self,
                ID : int,
                Name : str) -> None:
        self.ID = ID
        self.Name = Name
        self.Users = list()