import datetime
from Numbers import ReplaceNumber
from Numbers import To_Int_From_Suffics


class DamageDealer():
    def __init__(self, 
            Player, 
            Value : int):

        self.Player = Player
        self.Value  = Value
    
    def __repr__(self):
        return f"{self.Player.Name} : [{ReplaceNumber(self.Value)}]"

    def __lt__(self, other):
        if other.Value > self.Value:
            return False
        else:
            return True

class Date():
    """ Основной класс босса """

    def __init__(self,
            Name            : str   = "Имя",
            Description     : str   = "Описание",
            Features        : list  = ["Особенности босса"],
            LootDescription : list  = ["Описание дропа из босса"],
            Different       : str   = "Сложность",
            Health          : int   = 1,
            MaxHealth       : int   = 1,
            HealthRegen     : float = 1.0,
            HealthDivision  : int   = 1,
            Mana            : int   = 100,
            MaxMana         : int   = 100,
            ManaRegen       : float = 1.0,
            Protect         : int   = 1,
            Damage          : int   = 1,
            Image           : str   = "Путь к изображению",
            Time_End        : datetime.datetime = datetime.datetime.now()):

        self.Name            = Name
        self.Description     = Description
        self.Features        = Features
        self.LootDescription = LootDescription
        self.Different       = Different
        self.Health          = Health
        self.MaxHealth       = MaxHealth
        self.HealthRegen     = HealthRegen
        self.HealthDivision  = HealthDivision
        self.Mana            = Mana
        self.MaxMana         = MaxMana
        self.ManaRegen       = ManaRegen
        self.Protect         = Protect
        self.Damage          = Damage
        self.Image           = Image
        self.Time_End        = Time_End
        self.Murder          = Ellipsis
        self.Status          = True
        self.Get_Damage_From = []
    
    def GetDamage(self,Value : int,**fields):
        Player = fields['Player']
        if self.Status == False: return 0
        if self.On_GetDamage(Player,Value):
            Value -= self.Protect
            if Value <= 0: Value = 1
            self.DamageRegistration(Player, Value)
            self.Health -= Value
            if self.Health <= 0:
                if self.On_Death():
                    self.Murder = Player
                    self.Death()
        return Value
    
    def DamageRegistration(self, Player, Value : int):
        if Player not in self.Get_Damage_From:
            self.Get_Damage_From.append(Player)
            self.__setattr__(Player.Name,DamageDealer(Player,Value))
        else:
            _DamageDealer = self.__getattribute__(Player.Name)
            _DamageDealer.Value += Value
            self.__setattr__(Player.Name,_DamageDealer)


    
    def Death(self):
        self.Status = False
        self.After_Death()
    

    def On_GetDamage(self,Player, Value : int): return True
    def On_Death(self): return True
    def After_Death(self): pass


    @property
    def TopDealers(self):
        TopDealers = list()
        for Player in self.Get_Damage_From:
            TopDealers.append(self.__getattribute__(Player.Name))
        return sorted(TopDealers)



    @property
    def Now(self):
        return datetime.datetime.now()


    def Create_Timer(self,
            year    : int = datetime.datetime.now().year,
            month   : int = datetime.datetime.now().month,
            day     : int = datetime.datetime.now().day,
            hour    : int = datetime.datetime.now().hour,
            minute  : int = datetime.datetime.now().minute,
            second  : int = datetime.datetime.now().second):
        while second > 59:
            minute += 1
            second -= 59
        while minute > 59:
            hour += 1
            minute -= 59
        while hour > 23:
            day += 1
            hour -= 23
        return datetime.datetime(year=year,month=month,day=day,hour=hour,minute=minute,second=second)

    @property
    def Time(self):
        time = self.Time_End - self.Now
        if self.Now < self.Time_End:
            return time
        else:
            self.Status = False
            return time

    def __repr__(self):
        return f"Boss"

    def __str__(self):
        return f"Имя: [{self.Name}]         Описание: [{self.Description}]         Особенности: [{self.Features}]\nОписание лута: [{self.LootDescription}]         Сложность: [{self.Different}]\nЗдоровье: [{self.Health}/{self.MaxHealth}({self.HealthRegen})/{self.HealthDivision}]\nМана: [{self.Mana}/{self.MaxMana}({self.ManaRegen})]         Защита: [{self.Protect}]         Урон: [{self.Damage}]\nКонец времени: [{self.Time}]"

class Dummy(Date):
    """ Нужен как шаблон для последующих боссов """

    def __init__(self,Guild):
        self.Guild = Guild
        super().__init__(
            Name            = "",
            Description     = "",
            Features        = [""],
            LootDescription = [""],
            Different       = "",
            Health          = 100,
            MaxHealth       = 100,
            HealthRegen     = 1.0,
            HealthDivision  = 2,
            Mana            = 100,
            MaxMana         = 100,
            ManaRegen       = 1.0,
            Protect         = 5,
            Damage          = 5,
            Image           = "",
            Time_End        = self.Create_Timer(minute=self.Now.minute + 5))


class Gnoll(Date):
    def __init__(self,Guild):
        self.Guild = Guild
        super().__init__(
            Name            = "Гнолл Предводитель",
            Description     = "Странствующий гиеноподобный убийца",
            Features        = ["Атакует группой","На последнем дивизионе характеристики повышаются на 1000% / Время на убийство увеличивается на 30 минут","Не получает урона, пока запас маны полон","Получая урон, запас маны истощается","Изначальная мана больше чем максимальная"],
            LootDescription = ["Опыт [500К] каждому в Гильдии","Дополнительная награда:\n1 место по урону: 5К монет, 800К опыта\n2 место по урону: 2К монет, 400К опыта\n3 место по урону: 500 монет, 100К опыта"],
            Different       = "Легко",
            Health          = 10000,
            MaxHealth       = 10000,
            HealthRegen     = 10.0,
            HealthDivision  = 10,
            Mana            = 25,
            MaxMana         = 5,
            ManaRegen       = 0.1,
            Protect         = 900,
            Damage          = 1200,
            Image           = "",
            Time_End        = self.Create_Timer(minute=self.Now.minute + 1))
    
    def On_Death(self):
        if self.HealthDivision > 1:
            self.Health = self.MaxHealth
            self.HealthDivision -= 1
            return False
        elif self.HealthDivision == 1:
            self.Different = "Сложно"
            self.MaxHealth *= 100
            self.Health = self.MaxHealth
            self.HealthDivision -= 1
            self.HealthRegen = 1000.0
            self.ManaRegen = 10.0
            self.Protect *= 100
            self.Damage *= 100
            self.Time_End = self.Create_Timer(minute=self.Time_End.minute + self.Now.minute + 30)
        else:
            self.Status = False
            return True
    
    def After_Death(self):
        TopDealers = self.TopDealers

        TopDealers[0].Player.Gold += 5000
        TopDealers[0].Player.Exp += To_Int_From_Suffics("800K")

        try:
            TopDealers[1].Player.Gold += 2000
            TopDealers[1].Player.Exp += To_Int_From_Suffics("400K")
        except: return
        try:
            TopDealers[2].Player.Gold += 500
            TopDealers[2].Player.Exp += To_Int_From_Suffics("100K")
        except: return


