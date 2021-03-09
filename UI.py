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
from gabriel.logic import GabrielUser
from gabriel import GabrielClient
from gabriel.BazeData import token
import asyncio

class MainApp(App):
    def __init__(self,_GabrielClient,**kwargs):
        super().__init__(**kwargs)
        self.Client = _GabrielClient
        
    def build(self):
        self.GabrielPage  = FloatLayout()
        self.EditPage     = FloatLayout()
        self.SettingsPage = FloatLayout()

        self.MainMenu = TabbedPanel(
                        background_color = (1,1,1,1),
                        default_tab_text = 'Габриэль',
                        default_tab_content = self.GabrielPage)
        self.EditMenu = TabbedPanelItem(text='Edit')
        self.SettingsMenu = TabbedPanelItem(text='Settings')

        self.MainMenu.add_widget(self.EditMenu)
        self.MainMenu.add_widget(self.SettingsMenu)


        self.In_GabrielPage()
        self.In_EditPage()
        self.In_SettingsPage()

        return self.MainMenu
    
    def In_GabrielPage(self):
        self.GabrielPage.add_widget(Image(source='./Resurses/main.jpg',color=(1,1,1,0.5)))
        self.GabrielPage.add_widget(Button(text="LOGIN IN",on_press=self.LoginGab,size_hint=(None,None),size=(100,50),pos=(0,0)))
    
    def In_EditPage(self):
        self.EditMenu.add_widget(self.EditPage)

        self.EditPage_InformationMenu = FloatLayout()
        
        self.EditPage.add_widget(self.EditPage_InformationMenu)

        self._SelectUser = Spinner(text='Не выбран',size_hint=(None,None),size=(100,30),pos=(0,1000),on_press=self.find_members,on_text=self.GetInfoUser)

        self.EditPage.add_widget(self._SelectUser)
    
    def In_SettingsPage(self):
        self.SettingsMenu.add_widget(self.SettingsPage)
        self.SettingsPage.add_widget(Label(text="Настройки типа тут будут "))
    
    def LoginGab(self, button):
        self.GabrielPage.remove_widget(button)
        threading.Thread(target=self.Client.run,args=(token,)).start()




    def find_members(self,_Spinner):
            if _Spinner.text == "Не выбран":
                self.Users = []
                for file in os.listdir("./Statictics/"):
                    self.Users.append(GabrielUser.Open(int(file.split(".gabriel")[0]),Save=False))
                
                _Spinner.values = tuple([str(a.Name) for a in self.Users])
                self.GetInfoUser(_Spinner)
            else:
                self.GetInfoUser(_Spinner)
    


    def GetInfoUser(self, _Spinner):
        Layout = GridLayout(cols=5)

        try: User = [user for user in self.Users if user.Name == _Spinner.text][0]
        except: return
        for Varname in User.__dir__():

            value = User.__getattribute__(Varname)
            if type(value) in [str, int, float, bool, list, tuple]:
                ti = TextInput(
                        text=str(value),
                        size_hint=(None,None),
                        size=(300,50),
                        background_color=(.3,1,.6,.7))

                ti.add_widget(Label(text=str(Varname),color=(1,0,0,1)))

                Layout.add_widget(ti)
            
            
        
        self.EditPage_InformationMenu.add_widget(Layout)

# GabrielClient().run(token)
def main():
    _MainApp = MainApp(GabrielClient())
    _MainApp.run()


if __name__ == "__main__":
    main()