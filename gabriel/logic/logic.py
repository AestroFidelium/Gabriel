import discord
import requests
import bs4
import requests
import random
import codecs
import re
import pickle
from telebot.types import InlineQueryResultArticle, InputTextMessageContent


from kivy.uix.behaviors import button
from kivy.core.window import Window
from types import BuiltinMethodType, FunctionType, MethodType
from kivy.app import App

from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.accordion import Accordion, AccordionItem
from kivy.uix.carousel import Carousel
from kivy.uix.filechooser import FileChooser
from kivy.uix.progressbar import ProgressBar
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.spinner import Spinner
from kivy.uix.switch import Switch
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelHeader, TabbedPanelContent, TabbedPanelItem
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.image import Image

from kivy.clock import Clock
from functools import partial

from datetime import datetime
import os
import ast
import time
import random
from alive_progress import alive_bar
import threading
import requests
import bs4
import pickle


class GabrielUser():
    """Пользователь и вся информация
    """

    def __init__(self, ID: int, Name: str = None) -> None:
        """Создать нового пользователя

        Args:
            ID (int): ID пользователя (дискорда)
            Name (str, optional): Ник пользователя. Defaults to None.
        """
        self.Name = Name
        self.Lolilies = 0
        self.Messages = 0
        self._messages = 0
        self.ID = ID
        self.Rooms = []

        self.likes = 0
        self.dislikes = 0
        self.Posts = []

        self.InfoMessage = None
        self.SettingsMessage = None
        self.GameMessage = None

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
        copy = self.Open(self.ID, Save=True)
        with codecs.open(f"./Statictics/{self.ID}.gabriel", "wb") as file:
            try:
                pickle.dump(self, file)
            except BaseException as ERROR:
                pickle.dump(copy, file)
                raise ERROR(
                    "Не удалось сохранить новую информацию пользователя")

    @staticmethod
    def Open(ID: int, Name: str = None, Save=False) -> "GabrielUser":
        """Открыть информацию пользователя

        Returns:
            User: Пользователь
        """
        try:
            with codecs.open(f"./Statictics/{ID}.gabriel", "rb") as file:
                return pickle.load(file)
        except FileNotFoundError:
            if Save == False:
                print(f"[{Name}] Новый аккаунт")
            return GabrielUser(ID=ID, Name=Name)
        except EOFError:
            if Save == False:
                print(f"[{Name}] пустой аккаунт")
            return GabrielUser(ID=ID, Name=Name)

    def __repr__(self) -> str:
        return self.Name

    class Room():
        def __init__(self, Guild: str, Name: str, Permission) -> None:
            self.Guild = Guild
            self.Name = Name
            self.Permission = Permission


class Gabriel():
    def __init__(self) -> None:
        self.Guilds = list()
        self.Posts = list()

    def Save(self):
        """Сохранить статистику пользователя
        """
        copy = self.Open(Save=True)
        with codecs.open(f"./Statictics/Gabriel.gabriel", "wb") as file:
            try:
                pickle.dump(self, file)
            except BaseException as ERROR:
                pickle.dump(copy, file)
                raise ERROR("Габриэль не смогла сохраниться")

    @staticmethod
    def Open(Save: bool) -> "Gabriel":
        """Открыть профиль Габриэль

        Returns:
            Gabriel: Класс Габриэль
        """
        try:
            with codecs.open(f"./Statictics/Gabriel.gabriel", "rb") as file:
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
    def __init__(self, Author_id, Message) -> None:
        self.Author_id = Author_id
        self.Message = Message

        self.Likes = 0
        self.Dislikes = 0

        self.Likers = []
        self.Dislikers = []

    def __repr__(self) -> str:
        return f"Post#{self.Message.id}"


class GabrielGuild():
    """Габриэль-гильдия
    """

    def __init__(self,
                 ID: int,
                 Name: str) -> None:
        self.ID = ID
        self.Name = Name
        self.Users = list()


class CommandHelper():
    def __init__(self,
                 name: str, description: str, output: str, ID: int, *args) -> None:
        self.name = name
        self.description = description
        self.output = output
        self.args = args
        self.ID = ID

    def __repr__(self) -> str:
        return f'"{self.name}"'

    @property
    def ResultArticle(self) -> InlineQueryResultArticle:
        return InlineQueryResultArticle(
            id=self.ID,
            title=self.name,
            input_message_content=InputTextMessageContent(
                self.output
            ),
            description=self.description
        )

    # @property
    # def ResultArticle_ARGS(self) -> InlineQueryResultArticle:

    #     return InlineQueryResultArticle(
    #         id=self.ID,
    #         title=self.name,
    #         input_message_content=InputTextMessageContent(
    #             self.output
    #         )
    #     )


class Arg():
    def __init__(self, TelegramApi=None, func=lambda arg: [{"n": "", "d": ""}], func_args=(), name: str = "", description: str = "", only_description: bool = False) -> None:
        self.TelegramApi = TelegramApi
        self.func_args = func_args
        self.func = func
        self.name = name
        self.description = description
        self.only_description = only_description

    @property
    def Get(self):
        return self.func(self.TelegramApi, self, self.func_args)

    @staticmethod
    def SS(_list: list, d="") -> list:
        return [{"n": str(a), "d": str(d)} for a in _list]


def fetch_players(TelegramApi, arg, *args):
    return Arg.SS(["JesusPilatus", "AestroFidelium", "anbok", "Zeus", "Pres", "Savage"], "Пользователь")


def WhatDo(TelegramApi, arg, *args):
    return Arg.SS(["Show", "help", "Statistics", "Kill", "Delete"], "цыганские фокусы")


def _timeban(TelegramApi, arg, *args):
    return [
        dict(
            n="1-min",
            d="Забанить на 1 минуту"
        ),
        dict(
            n="10-mins",
            d="Забанить на 10 минут"
        ),
        dict(
            n="1-hour",
            d="Забанить на 1 час"
        ),
        dict(
            n="2-hours",
            d="Забанить на 2 часа"
        ),
        dict(
            n="5-hours",
            d="Забанить на 5 часов"
        ),
        dict(
            n="12-hours",
            d="Забанить на 12 часов"
        )
    ]


def _reasonban(TelegramApi, arg, *args):
    return Arg.SS([""], "напишите причину блокировки")


COMMAND_LIST = [
    CommandHelper("profile", "Открыть профиль игрока", "/help profile", 1,
                  Arg(
                      func=fetch_players,
                      name="*user_name",
                      description="Имя игрока"),
                  Arg(
                      func=WhatDo,
                      name="*do",
                      description="шо делать")
                  ),


    CommandHelper('ban', "Забанить что либо", "/help ban", 2,

                  Arg(
                      func=fetch_players,
                      name="*user_name",
                      description="Пользователь которому следует выдать бан"
                  ),

                  Arg(
                      func=_timeban,
                      name="*ban_time",
                      description="На сколько следует забанить пользователя"
                  ),

                  Arg(
                      func=_reasonban,
                      name="*reason",
                      description="Причина бана пользователя"
                  )

                  )

]


class myButton(Button):
    def __init__(self, Input, command, **kwargs):
        self.Input = Input
        self.command = command
        super(myButton, self).__init__(**kwargs)

    def on_press(self):
        if isinstance(self.command, CommandHelper):
            self.Input.text += f"{self.command.name} "
        else:
            arg_name = self.command["n"]
            self.Input.text += f"{arg_name} "
        return super().on_press()


class TeleGrammTypa(App):
    def build(self):
        self.MainScreen = FloatLayout()
        self.ArgShow = FloatLayout()
        self.MainScreen.add_widget(self.ArgShow)
        self.INPUT = TextInput(size_hint=(None, None), size=(
            200, 50), pos=(Window.width / 2 - 100, Window.height / 2))
        self.MainScreen.add_widget(self.INPUT)
        self.Helper = GridLayout(cols=4, size_hint=(
            None, None), size=(200, 200), pos=(100, 75))
        self.MainScreen.add_widget(self.Helper)
        Clock.schedule_interval(self.CommandHelper, 0.1)
        return self.MainScreen

    def CommandHelper(self, clock):
        Message = str(self.INPUT.text)
        self.Helper.clear_widgets()
        self.ArgShow.clear_widgets()
        # Ничего не написано
        if Message == "":
            for command in COMMAND_LIST:
                self.Helper.add_widget(myButton(
                    self.INPUT, command, text=f"               {command.name}\n{command.description}", size_hint=(None, None), size=(150, 50)))
        # Начал писать что то либо
        else:
            Commands = Message.lower().split(" ")
            SeemIt = [command for command in COMMAND_LIST if command.name.lower(
            ).startswith(Commands[0])]

            # Проверяет закончилась ли название команды
            if len(SeemIt) == 1 and SeemIt[0].name == Commands[0]:

                command = SeemIt[0]

                for LEN in range(0, len(Commands) - 1, 1):
                    self.Helper.clear_widgets()
                    self.ArgShow.clear_widgets()
                    # Первый параметр
                    try:
                        ArgSeemLike = [arg for arg in command.args[LEN].Get if arg["n"].lower(
                        ).startswith(Commands[LEN + 1])]

                        self.ArgShow.add_widget(Label(text=command.args[LEN].name, size_hint=(
                            None, None), size=(50, 50), pos=(300, 350)))
                        self.ArgShow.add_widget(Label(text=command.args[LEN].description, size_hint=(
                            None, None), size=(100, 100), pos=(300, 400)))
                        for arg in ArgSeemLike:
                            n = arg["n"]
                            d = arg['d']
                            self.Helper.add_widget(myButton(
                                self.INPUT, arg, text=f"{n}\n{d}", size_hint=(None, None), size=(150, 50)))
                    except IndexError:
                        self.ArgShow.add_widget(
                            Label(text="Команда завершена", size_hint=(None, None), size=(500, 350)))
            # Нет не закончилось так что продолжает показывать правильное написание команды
            else:
                for command in SeemIt:
                    self.Helper.add_widget(myButton(
                        self.INPUT, command, text=f"               {command.name}\n{command.description}", size_hint=(None, None), size=(150, 50)))


TeleGrammTypa().run()
