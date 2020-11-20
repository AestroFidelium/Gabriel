import random
import Numbers


class ItemClass():
    def __init__(self,
            Damage      : int = 100,
            Protect     : int = 100,
            Unbreaking  : int = 100,
            Name        : str = "Название класса",
            Description : str = "Описание класса",
            Next              = Ellipsis):

        self.Damage      = Damage
        self.Protect     = Protect
        self.Unbreaking  = Unbreaking
        self.Name        = Name
        self.Description = Description
        self.Next        = Next

        

    def __repr__(self):
        return f"[{self.Name}]            [{self.Description}]\nDamage: [{self.Damage}]            Protect: [{self.Protect}]            Unbreaking: [{self.Unbreaking}]"

class Classes():

    class Отсуствует(ItemClass):
        def __init__(self):
            super().__init__(Name="Название отсутствует",Description="Описание отсутствует")


    class Начальное(ItemClass):
        def __init__(self):
            super().__init__(Name="Начальное",Description="Начальный класс экипировки, его получают все новоприбывшие игроки",Next=Classes.Обычное)
        def __next__(self):
            return Classes.Обычное()

    class Обычное(ItemClass):
        def __init__(self):
            super().__init__(
                Damage     = 500,
                Protect    = 300,
                Unbreaking = 600,
                Name="Обычное",Description="Слегка сильнее чем начальное, других отличий почти нет",Next=Classes.Редкое)
        def __next__(self):
            return Classes.Редкое()
    
    class Редкое(ItemClass):
        def __init__(self):
            super().__init__(
                Damage     = 3200,
                Protect    = 3100,
                Unbreaking = 2200,
                Name="Редкое",Description="Как говорит название класса, получить эту экипировку редкость. Она в разы сильнее обычных",Next=Classes.Эпическое)
        def __next__(self):
            return Classes.Эпическое()
    
    class Эпическое(ItemClass):
        def __init__(self):
            super().__init__(
                Damage     = 12600,
                Protect    = 11900,
                Unbreaking = 6000,
                Name="Эпическое",Description="Экипировка которую используют герои, в своем возвышении",Next=Classes.Легендарное)
        def __next__(self):
            return Classes.Легендарное()
    
    class Легендарное(ItemClass):
        def __init__(self):
            super().__init__(
                Damage     = 65800,
                Protect    = 65300,
                Unbreaking = 50000,
                Name="Легендарное",Description="Легендарная экипировка является существенно сильнее всех остальных",Next=Classes.Мифическое)
        def __next__(self):
            return Classes.Мифическое()
    
    class Мифическое(ItemClass):
        def __init__(self):
            super().__init__(
                Damage     = random.randint(1000,10000000),
                Protect    = random.randint(1000,10000000),
                Unbreaking = random.randint(100,100000),
                Name="Мифическое",Description="Мифическая экипировка не просто названа Мифом. Её нестабильность проявляется в сложности получения хорошего её вида. Ведь её урон, броня, и прочность постоянно меняются",Next=Classes.Мифическое)
        def __next__(self):
            return Classes.Мифическое()

    class СвоеНазвание(ItemClass):
        def __init__(self,
                Damage      : int = 1,
                Protect     : int = 1, 
                Unbreaking  : int = 1,
                Name        : str = "Название класса",
                Description : str = "Описание класса"):
            super().__init__(
                Damage     = Damage,
                Protect    = Protect,
                Unbreaking = Unbreaking,
                Name=Name,Description=Description,Next=Classes.Отсуствует())

class Item():
    """ Стандартные настройки всех предметов """

    class Types():
        class Blade()    : pass
        class Equipment(): pass
        class Ring()     : pass
        class Bug()      : pass
    
    class Wheres():
        class Head()  : pass
        class Body()  : pass
        class Legs()  : pass
        class Boots() : pass
        class Weapon(): pass
        class Empty() : pass

    def __init__(self,
            Player,
            ID           : int  = random.randint(1,999999999),
            Name         : str  = "Неизвестно",
            Description  : str  = "Отсутствует",
            Class               = Classes.Отсуствует(),
            Type                = Types.Bug,
            Unbreaking   : int  = 1,
            Damage       : int  = 0,
            Protect      : int  = 0,
            Where               = Wheres.Empty,
            Level        : int  = 0,
            MaxLevel     : int  = 100,
            Exp          : float = 0,
            ExpRequest   : float = 100,
            Information  : str  = "Информация отсуствует"):

        self.ID          = ID
        self.Name        = Name
        self.Description = Description
        self.Type        = Type
        self.Class       = Class
        self._Unbreaking = Unbreaking
        self._Damage     = Damage
        self._Protect    = Protect
        self.Where       = Where
        self.Player      = Player
        self.Type        = Type
        self.Gold        = 0
        self.MaxGold     = 0
        self.AllGold     = 0
        self.Level       = Level
        self.MaxLevel    = MaxLevel
        self.Exp         = Exp
        self.ExpRequest  = ExpRequest
        self.Information = Information

    @property
    def Magic(self):
        return "Отсуствуют"
    
    @property
    def Damage(self):
        return self._Damage
    
    @property
    def Unbreaking(self):
        return self._Unbreaking
    
    @property
    def Protect(self):
        return self._Protect
    
    def Break(self,Value : int):
        """ Повреждение в оружии """
        self._Unbreaking = self.Unbreaking - Value
    
    def Attack(self, Target):
        return Target.GetDamage(random.randint(1,self.Player.MaxDamage()))
          
    def __repr__(self):
        return f"ID: {self.ID}\nName: {self.Name}\nDescription: {self.Description}\nType: {self.Type}\nClass: {self.Class}\nUnbreaking: {self.Unbreaking}\nDamage: {self.Damage}\nProtect: {self.Protect}\nWhere: {self.Where}\nGold: {self.Gold}\nInformation: {self.Information}"

    def __str__(self):
        return f"ID: {self.ID}\nИмя: {self.Name}\nОписание: {self.Description}\nТип: {self.Type}\nКласс: {self.Class}\nПрочность: {self.Unbreaking}\nУрон: {self.Damage}\nЗащита: {self.Protect}\nКуда экипируется: {self.Where}\nЗолото: {self.Gold}\nExp: [{self.Exp}/{self.ExpRequest}]\nLevel: [{self.Level}/{self.MaxLevel}]\nИнформация об предмете: {self.Information}"


    def Upgrade(self,Exp : float):
        self.Exp += Exp
        if self.Exp >= self.ExpRequest:
            if self.Level + 1 >= self.MaxLevel:
                try: self.Class = self.Class.Next()
                except: self.on_upgrade()
            else:
                self.on_upgrade()
            self.Exp = 0
    

    def on_upgrade(self):
        """ Вызывается во время улучшения предмета. """

        if self.Type == self.Types.Blade:
            self._Damage += random.randint(100 + self.Class.Damage,2000 + self.Class.Damage)
        else:
            self._Protect += random.randint(100 + self.Class.Protect,2000 + self.Class.Protect)
        self._Unbreaking += random.randint(100 + self.Class.Unbreaking,3000 + self.Class.Unbreaking)


class Your_first_things(Item):
    """ Начальное снаряжение """
    
    def __init__(self,Player):
        self.Player = Player
    def Blade(self):
        return Item(
            Name=f"Начальный клинок",
            Description=f"Ничем не примечательный клинок. Не обладает никакими свойствами. Был создан специально для ({self.Player.Name})",
            Class=Classes.Начальное(),
            Type=Item.Types.Blade,
            Unbreaking=random.randint(500,700),
            Damage=random.randint(100,3000),
            Player=self.Player)
    def Head(self):
        return Item(
            Name=f"Начальный шлем",
            Description=f"Обычный шлем, с которым начинают все",
            Class=Classes.Начальное(),
            Type=Item.Types.Equipment,
            Unbreaking=random.randint(500,700),
            Protect=random.randint(35,250),
            Where=Item.Wheres.Head,
            Player=self.Player)
    def Body(self):
        return Item(
            Name=f"Начальный нагрудник",
            Description=f"Ничем не примечательный нагрудник.",
            Class=Classes.Начальное(),
            Type=Item.Types.Equipment,
            Unbreaking=random.randint(500,700),
            Protect=random.randint(35,300),
            Where=Item.Wheres.Body,
            Player=self.Player)
    def Legs(self):
        return Item(
            Name=f"Начальные поножи",
            Description=f"Городские поножи. Совсем обычные",
            Class=Classes.Начальное(),
            Type=Item.Types.Equipment,
            Unbreaking=random.randint(500,700),
            Protect=random.randint(35,300),
            Where=Item.Wheres.Legs,
            Player=self.Player)
    
    def Boots(self):
        return Item(
            Name=f"Начальные ботинки",
            Description=f"Городские ботинки. В них довольно приятно ходить",
            Class=Classes.Начальное(),
            Type=Item.Types.Equipment,
            Unbreaking=random.randint(500,700),
            Protect=random.randint(35,200),
            Where=Item.Wheres.Boots,
            Player=self.Player)


class ItemFromGoblin(Item):
    def __init__(self,Player):
        self.Player = Player
        super().__init__(
            Name=f"Зазубренный клинок",
            Description=f"Оружие изъятое от гоблинов",
            Class=Classes.Обычное(),
            Type=Item.Types.Blade,
            Unbreaking=random.randint(100,200),
            Damage=random.randint(1000,1500),
            Player=self.Player,
            Information="Есть 10% шанс что вы атакуете 3-4 раза")
    
    @property
    def Damage(self):
        if random.randint(1,100) < 10:
            return self._Damage * random.randint(3,4)
        return self._Damage
    


class Fang(Item):
    def __init__(self,Player):
        self.Player = Player
        self.DamageLimit = 320000
        self.DamageInfo = Numbers.ReplaceNumber("320.000")
        super().__init__(
            Name=f"Клык",
            Description=f"Клык который вы взяли как трофей. Однако из него может выйти неплохое оружие",
            Class=Classes.СвоеНазвание(Damage=10000,Name="Магическое оружие",Description="Это оружие не стандартное, оно пропитано магией"),
            Type=Item.Types.Blade,
            Unbreaking=1,
            Damage=100,
            Player=self.Player,
            Information=f"Нерушимое оружие / После каждой атаки его урон увеличивается на (1 + (Прочность оружия))% / Не может нанести больше {self.DamageInfo} урона / Прокачивание оружие увеличивают его максимальный придел урона",
            MaxLevel=1)
    

    

    @property
    def Damage(self):
        if self._Damage < self.DamageLimit:
            self._Damage += round(self._Damage * (0.01 + (self.Unbreaking / 100)))
        elif self._Damage > self.DamageLimit: self._Damage = self.DamageLimit
        return self._Damage

    def Break(self,Value): pass

    def __str__(self):
        return f"ID: {self.ID}\nИмя: {self.Name}\nОписание: {self.Description}\nТип: {self.Type}\nКласс: {self.Class}\nУрон: [{self._Damage}/{self.DamageLimit}]\nОпыт: [{self.Exp}/{self.ExpRequest}]\nУровень: [{self.Level}/{self.MaxLevel}]\nИнформация об предмете: {self.Information}"


    def on_upgrade(self):
        self.DamageLimit += self.Class.Damage
        self.DamageInfo = Numbers.ReplaceNumber(self.DamageLimit)
        self.Information = f"Нерушимое оружие / После каждой атаки его урон увеличивается на (1 + (Прочность оружия))% / Не может нанести больше {self.DamageInfo} урона / Прокачивание оружие увеличивают его максимальный придел урона"
        self.Level += 1
        self.MaxLevel = self.Level + 1




class Sword_Of_The_Cosmos(Item):
    def __init__(self,Player):
        self.Player = Player
        super().__init__(
            Name=f"Sword Of The Cosmos",
            Description=f"Оружие впитавшее энергию сверхновы",
            Class=Classes.СвоеНазвание(Damage="Бесконечность",Protect="Бесконечность",Unbreaking="Бесконечность",Name="КОСМИЧЕСКАЯ СИЛА",Description="Оружие по силе космоса"),
            Type=Item.Types.Blade,
            Unbreaking=1,
            Damage=1,
            Player=self.Player,
            Information=f"Отсутствует",
            MaxLevel=1)
        self.Gold = "Бесконечность"
    

    def Attack(self, Target):
        self.Player.Level_UP_From_Kill(Target)
        Target.Death()
        Target.Save()
        return Numbers.ReplaceNumber(Target.MaxHealth)

    @property
    def Damage(self):
        return "Бесконечность"
    
    @property
    def Unbreaking(self):
        return "Бесконечность"

    def Break(self,Value): pass

    def Upgrade(self,Exp : float): pass