import random

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
            Class        : str  = "Неизвестно",
            Type                = Types.Bug,
            Unbreaking   : int  = 1,
            Damage       : int  = 0,
            Protect      : int  = 0,
            Where               = Wheres.Empty,
            Information  : str  = "Информация отсуствует"):
        self.ID = ID
        self.Name = Name
        self.Description = Description
        self.Type = Type
        self.Class = Class
        self._Unbreaking = Unbreaking
        self._Damage = Damage
        self._Protect = Protect
        self.Where = Where
        self.Player = Player
        self.Type = Type
        self.Gold = 0
        self.MaxGold = 0
        self.AllGold = 0
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
          
    def __repr__(self):
        return f"ID: {self.ID}\nName: {self.Name}\nDescription: {self.Description}\nType: {self.Type}\nClass: {self.Class}\nUnbreaking: {self.Unbreaking}\nDamage: {self.Damage}\nProtect: {self.Protect}\nWhere: {self.Where}\nGold: {self.Gold}\nInformation: {self.Information}"

    def __str__(self):
        return f"ID: {self.ID}\nИмя: {self.Name}\nОписание: {self.Description}\nТип: {self.Type}\nКласс: {self.Class}\nПрочность: {self.Unbreaking}\nУран: {self.Damage}\nЗащита: {self.Protect}\nКуда экипируется: {self.Where}\nЗолото: {self.Gold}\nИнформация об предмете: {self.Information}"

class Your_first_things(Item):
    """ Начальное снаряжение """
    
    def __init__(self,Player):
        self.Player = Player
    def Blade(self):
        return Item(
            Name=f"Начальный клинок",
            Description=f"Ничем не примечательный клинок. Не обладает никакими свойствами. Был создан специально для ({self.Player.Name})",
            Class="Первоначальный",
            Type=Item.Types.Blade,
            Unbreaking=random.randint(500,700),
            Damage=random.randint(100,3000),
            Player=self.Player)
    def Head(self):
        return Item(
            Name=f"Начальный шлем",
            Description=f"Обычный шлем, с которым начинают все",
            Class="Первоначальный",
            Type=Item.Types.Equipment,
            Unbreaking=random.randint(500,700),
            Protect=random.randint(35,250),
            Where=Item.Wheres.Head,
            Player=self.Player)
    def Body(self):
        return Item(
            Name=f"Начальный нагрудник",
            Description=f"Ничем не примечательный нагрудник.",
            Class="Первоначальный",
            Type=Item.Types.Equipment,
            Unbreaking=random.randint(500,700),
            Protect=random.randint(35,300),
            Where=Item.Wheres.Body,
            Player=self.Player)
    def Legs(self):
        return Item(
            Name=f"Начальные поножи",
            Description=f"Городские поножи. Совсем обычные",
            Class="Первоначальный",
            Type=Item.Types.Equipment,
            Unbreaking=random.randint(500,700),
            Protect=random.randint(35,300),
            Where=Item.Wheres.Legs,
            Player=self.Player)
    
    def Boots(self):
        return Item(
            Name=f"Начальные ботинки",
            Description=f"Городские ботинки. В них довольно приятно ходить",
            Class="Первоначальный",
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
            Class="Обычное",
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
        super().__init__(
            Name=f"Клык",
            Description=f"Клык который вы взяли как трофей. Однако из него может выйти неплохое оружие",
            Class="Необычное оружие",
            Type=Item.Types.Blade,
            Unbreaking=1,
            Damage=100,
            Player=self.Player,
            Information="Нерушимое оружие / После каждой атаки его урон увеличивается на 1% / Не может нанести больше 32к урона / **Не имеется смысл прокачивать оружие**")
    
    @property
    def Damage(self):
        if self._Damage < 32000:
            self._Damage += self._Damage * 0.01
        elif self._Damage > 32000: self._Damage = 32000
        return self._Damage

    def Break(self,Value): pass

















