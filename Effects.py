import random
import Numbers
import datetime
import threading
import time

class Simple_Effect():
    """ Главный эффект """

    def __init__(self,
            Player,
            Name            : str               = "Название Эффекта",
            Description     : str               = "Описание Эффекта",
            Do              : str               = "Что делает эффект",
            Time_Start      : datetime.datetime = datetime.datetime.now(),
            Time_End        : datetime.datetime = datetime.datetime.now()):

        self.Player      = Player
        self.Name        = Name
        self.Description = Description
        self.Do          = Do
        self.Time_Start  = Time_Start
        self.Time_End    = Time_End
        self.Status      = True

    @property
    def Now(self):
        return datetime.datetime.now()
    

    @property
    def Timer(self):
        return self.Time_End - self.Time_Start
    
    def __repr__(self):
        return f"({self.Name} [{self.Timer}])"

    def Start(self):
        threading.Thread(target=self._Update,args=()).start()
    
    def _Update(self):
        while True:
            self.Update()
            time.sleep(1)
            if self.Status == False:
                break

    def Update(self):
        if self.Status:
            self.Time_Start = self.Now
            if self.Time_Start > self.Time_End:
                self.Status = False

    def __str__(self):
        return f"Имя Эффекта: [{self.Name}]          Описание Эффекта: [{self.Description}]          Что Делает: [{self.Do}]\nНачинается с: [{self.Time_Start}]          Коней Таймера в: [{self.Time_End}]          Заканчивается через: [{self.Timer}]"

class Invulnerability(Simple_Effect):
    def __init__(self,Player):
        Now = self.Now

        Time_End = datetime.datetime(
            Now.year,
            Now.month,
            Now.day,
            Now.hour,
            Now.minute + 1,
            Now.second)

        super().__init__(Player,
            Name        = "Неуязвимость",
            Description = "Действует сразу после получения, до 5 минут",
            Do          = "Вы течении действия эффекта, цель не получает урона",
            Time_Start  = datetime.datetime.now(),
            Time_End    = Time_End)