class Talant():
    def __init__(self,
            Name        : str  = "Неизвестно",
            Description : str  = "Отсутствует",
            PerLevel    : str  =  "Каждый уровень ...",
            Level       : int  = 0,
            MaxLevel    : int  = 1,
            Exp         : int  = 0,
            NeedExp     : int  = 10,
            Lock        : bool = False,
            NeedAt      : list = []):
        self.Name = Name
        self.Description = Description
        self.PerLevel = PerLevel
        self.Level = Level
        self.MaxLevel = MaxLevel
        self.Exp = Exp
        self.NeedExp = NeedExp
        self.Lock = Lock
        self.NeedAt = NeedAt

    def Update(self,Exp : int):
        if self.Level < self.MaxLevel and self.Lock == False:
            self.Exp += Exp
            if self.Exp >= self.NeedExp:
                self.NeedExp *= 2
                self.Level += 1
                self.Updated()
                return True
        elif self.Lock:
            for talant in self.NeedAt:
                if talant.NeedLevel < talant.Stats.Level:
                    if talant.Talant.Update(Exp):
                        break
        else:
            return False

    
    def Updated(self): pass


class TalantNeedAt():
    def __init__(self,Talant,NeedLevel : int):
        self.Stats = Talant
        self.NeedLevel = NeedLevel

class Heroic_Level(Talant):
    def __init__(self,Player):
        super().__init__(
            Name="Героический уровень",
            Description="Увеличивает ваши характеристики.\nТребуется для других талантов",
            PerLevel="Сила += 0.1%\nЛовкость += 0.2%\nИнтеллект += 0.3%\nЗдоровье += 320 ед.\nОпыт += 100 ед.\nУровень += 1",
            Level=0,
            MaxLevel=10000,
            Exp=0,
            NeedExp=100,
            Lock=False,
            NeedAt=[])
        self.Player = Player
    
    def Updated(self):
        self.Player.Strength     += 0.1
        self.Player.Agility      += 0.2
        self.Player.Intelligence += 0.3
        self.Player.Health       += 320
        self.Player.MaxHealth    += 320
        self.Player.Exp          += 100
        self.Player.LevelUp()

class More_Exp():
    def __init__(self,Player):
        super().__init__(
            Name="Больше опыта",
            Description="Больше опыта за сообщения",
            PerLevel="Увеличивает количество получаемого опыта",
            Level=0,
            MaxLevel=100,
            Exp=0,
            NeedExp=10,
            Lock=False,
            NeedAt=[])
        self.Player = Player

class More_Gold():
    def __init__(self,Player):
        super().__init__(
            Name="Больше золота",
            Description="Получение золота требует меньшее количество золота",
            PerLevel="Уменьшает требования на 1 сообщение",
            Level=0,
            MaxLevel=5,
            Exp=0,
            NeedExp=10,
            Lock=False,
            NeedAt=[])
        self.Player = Player

class More_Damage():
    def __init__(self,Player):
        super().__init__(
            Name="Усиленный урон",
            Description="Вы наносите больше урона",
            PerLevel="Увеличивает весь ваш урон на 5%",
            Level=0,
            MaxLevel=10,
            Exp=0,
            NeedExp=100,
            Lock=False,
            NeedAt=[])
        self.Player = Player

class More_Protect():
    def __init__(self,Player):
        super().__init__(
            Name="Броня",
            Description="Вы получаете меньше урона",
            PerLevel="Уменьшает весь получаемый урон на 2.5%",
            Level=0,
            MaxLevel=20,
            Exp=0,
            NeedExp=50,
            Lock=False,
            NeedAt=[])
        self.Player = Player

class Passive_Generator():
    def __init__(self,Player):
        super().__init__(
            Name="Пассивный генератор опыта",
            Description="Генерирует опыт. Стандартное значение 0 ед./час",
            PerLevel="Увеличивает значение на 1 ед. в час",
            Level=0,
            MaxLevel=1,
            Exp=0,
            NeedExp=1000,
            Lock=True,
            NeedAt=[TalantNeedAt(Heroic_Level,3)])
        self.Player = Player

class Updater_Generator_Amount():
    def __init__(self,Player):
        super().__init__(
            Name="Генератор Опыта",
            Description="Усиливает генератор опыта",
            PerLevel="Увеличивает опыт на 10 ед.",
            Level=0,
            MaxLevel=4,
            Exp=0,
            NeedExp=700,
            Lock=True,
            NeedAt=[TalantNeedAt(Passive_Generator,1)])
        self.Player = Player

class Updater_Generator_Speed():
    def __init__(self,Player):
        super().__init__(
            Name="Улучшенный Генератор Опыта",
            Description="Ускоряет генератор опыта",
            PerLevel="Уменьшает время на 1 минуту",
            Level=0,
            MaxLevel=40,
            Exp=0,
            NeedExp=2000,
            Lock=True,
            NeedAt=[TalantNeedAt(Passive_Generator,1)])
        self.Player = Player


class Cheater_Generator():
    def __init__(self,Player):
        super().__init__(
            Name="Не честный генератор опыта",
            Description="ГенЕрАциЯ",
            PerLevel="Увеличивает генерируемый опыт на 0.0001% от нужного вам, до следующего уровня",
            Level=0,
            MaxLevel=100,
            Exp=0,
            NeedExp=353000000000,
            Lock=True,
            NeedAt=[TalantNeedAt(Heroic_Level,10000)])
        self.Player = Player

class Regeneration():
    def __init__(self,Player):
        super().__init__(
            Name="Регенерация",
            Description="Регенерация здоровья \nСтандартная регенерация : 0 ед./мин.",
            PerLevel="Увеличивает значение на 1 ед. в минуту",
            Level=0,
            MaxLevel=1,
            Exp=0,
            NeedExp=300,
            Lock=True,
            NeedAt=[TalantNeedAt(Heroic_Level,5)])
        self.Player = Player

class Regeneration_Amount():
    def __init__(self,Player):
        super().__init__(
            Name="Усиленная Регенерация",
            Description="Усиливает регенерацию здоровья",
            PerLevel="Увеличивает на 10 ед. регенерацию",
            Level=0,
            MaxLevel=100,
            Exp=0,
            NeedExp=300,
            Lock=True,
            NeedAt=[TalantNeedAt(Regeneration,1)])
        self.Player = Player

class Regeneration_Speed():
    def __init__(self,Player):
        super().__init__(
            Name="Ускоренная Регенерация",
            Description="Ускоряет получение регенерации здоровья",
            PerLevel="Уменьшает время получение регенерации на 1 секунду",
            Level=0,
            MaxLevel=30,
            Exp=0,
            NeedExp=600,
            Lock=True,
            NeedAt=[TalantNeedAt(Regeneration,1)])
        self.Player = Player

class Cheater_Regeneration():
    def __init__(self,Player):
        super().__init__(
            Name="Сверх реген",
            Description="Заживает даже отрубленная рука",
            PerLevel="Увеличивает регенерацию на 0.5% от максимального здоровья",
            Level=0,
            MaxLevel=5,
            Exp=0,
            NeedExp=5333333333,
            Lock=True,
            NeedAt=[TalantNeedAt(Regeneration,1),TalantNeedAt(Heroic_Level,5000)])
        self.Player = Player

class Blacksmith():
    def __init__(self,Player):
        super().__init__(
            Name="Кузнец",
            Description="Сила предметов становиться сильнее",
            PerLevel="Увеличивает силу у будущих предметов на 2%",
            Level=0,
            MaxLevel=20,
            Exp=0,
            NeedExp=600,
            Lock=False,
            NeedAt=[])
        self.Player = Player

class Immunity():
    def __init__(self,Player):
        super().__init__(
            Name="Иммунитет",
            Description="Развить иммунитет",
            PerLevel="",
            Level=0,
            MaxLevel=1,
            Exp=0,
            NeedExp=25,
            Lock=False,
            NeedAt=[])
        self.Player = Player

class Immunity_from_poison():
    def __init__(self,Player):
        super().__init__(
            Name="Иммунитет От Яда",
            Description="Вы получаете меньше урона от яда",
            PerLevel="Уменьшает получаемый урон от яда на 1.5%",
            Level=0,
            MaxLevel=50,
            Exp=0,
            NeedExp=100,
            Lock=True,
            NeedAt=[TalantNeedAt(Immunity,1)])
        self.Player = Player

class Bonus():
    def __init__(self,Player):
        super().__init__(
            Name="Бонусы",
            Description="Увеличивает ежедневную награду",
            PerLevel="Увеличивает ежедневную награду на 300 золотых",
            Level=0,
            MaxLevel=10,
            Exp=0,
            NeedExp=100,
            Lock=False,
            NeedAt=[])
        self.Player = Player

class Max_Bonus():
    def __init__(self,Player):
        super().__init__(
            Name="Бонусы",
            Description="Увеличивает максимальную ежедневную награду",
            PerLevel="Увеличивает максимальную ежедневную награду на 1250 золотых",
            Level=0,
            MaxLevel=10,
            Exp=0,
            NeedExp=1000,
            Lock=True,
            NeedAt=[TalantNeedAt(Bonus,10)])
        self.Player = Player

class Spells():
    def __init__(self,Player):
        super().__init__(
            Name="Способности",
            Description="Открывает возможность получить способности",
            PerLevel="Открывает более сильные таланты",
            Level=0,
            MaxLevel=5,
            Exp=0,
            NeedExp=3000,
            Lock=True,
            NeedAt=[TalantNeedAt(Heroic_Level,10)])
        self.Player = Player

class Berserk():
    def __init__(self,Player):
        super().__init__(
            Name="Берсерк",
            Description="За каждый недостающий 1% здоровья увеличивает урон на (1 + уровень таланта)%",
            PerLevel="Увеличивает урон на 1%",
            Level=0,
            MaxLevel=10,
            Exp=0,
            NeedExp=1000,
            Lock=True,
            NeedAt=[TalantNeedAt(Spells,1)])
        self.Player = Player


class Invincible():
    def __init__(self,Player):
        super().__init__(
            Name="Непобедимый",
            Description="При смерти: Если урон был выше чем исциление с помощью этого навыка, вы не погибаете. Но здоровье фиксируется используя талант",
            PerLevel="Увеличивает исцеление после навыка на 500 ед.",
            Level=0,
            MaxLevel=5,
            Exp=0,
            NeedExp=3000,
            Lock=True,
            NeedAt=[TalantNeedAt(Spells,2)])
        self.Player = Player


class Annihilator():
    def __init__(self,Player):
        super().__init__(
            Name="Уничтожитель",
            Description="Шанс нанести (х5) кратный урон",
            PerLevel="Увеличивает шанс на 0.1%",
            Level=0,
            MaxLevel=50,
            Exp=0,
            NeedExp=5000,
            Lock=True,
            NeedAt=[TalantNeedAt(Spells,3)])
        self.Player = Player


class Repair():
    def __init__(self,Player):
        super().__init__(
            Name="Починка",
            Description="Предметы которые экипированные, начинают чиниться со временем. (Каждые 10 минут)",
            PerLevel="Увеличивает получаемую прочность на 3 ед.",
            Level=0,
            MaxLevel=6,
            Exp=0,
            NeedExp=1300,
            Lock=True,
            NeedAt=[TalantNeedAt(Spells,4),TalantNeedAt(Blacksmith,20)])
        self.Player = Player