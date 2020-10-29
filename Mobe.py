import Items
import time
import threading
import random
import datetime

class Loot():
    def __init__(self, Item, Chance : float):
        self.Item   = Item
        self.Chance = Chance

class Mob():
    def __init__(self,
            Name                    : str   = "Имя моба",
            Description             : str   = "Описание моба",
            DropLoot_Description    : str   = "Описание возможного дропа с моба",
            DropLoot                : Loot  = "Вещи выпадаемые с моба",
            Health                  : int   = 1,
            MaxHealth               : int   = 1,
            Damage                  : int   = 1,
            Protect                 : int   = 1,
            Breaks_the_equipment    : bool  = True,
            SpawnRate               : float = 1.0,
            SpawnLimite             : int   = 1,
            NextMob                         = "Следующий моб. Делать не обязательно",
            Level                   : int   = 1,
            LevelRequests           : int   = 1,
            Class                   : str   = "Обычный / Необычный и так далее",
            Information             : str   = "Информация"):

        self.Name                 = Name
        self.Description          = Description
        self.DropLoot_Description = DropLoot_Description
        self.DropLoot             = DropLoot
        self.Health               = Health
        self.MaxHealth            = MaxHealth
        self.Damage               = Damage
        self.Protect              = Protect
        self.Breaks_the_equipment = Breaks_the_equipment
        self.SpawnRate            = SpawnRate
        self.SpawnLimite          = SpawnLimite
        self.DeathList            = 0 # Сколько раз погибал моб
        self.Status               = True # True = живой. False = мертвый
        self.NextMob              = NextMob
        self.Level                = Level
        self.LevelRequests        = LevelRequests
        self.Player               = self.__getattribute__("Player")
        self.Information          = Information
        self.on_spawn()


    def Attack(self):
        """ Атаковать """ 
        self.Player.GetDamage(self.Damage)


    def Hit(self,Damage : int):
        """ Получить урон """
        if self.Status == False:
            if self.SpawnLimite > 0:
                threading.Thread(target=self.Death,args=()).start()
                return "Нельзя атаковать мертвую цель"
            else:
                return "Целей больше нет"
        if self.SpawnLimite < 0: return f"Все цели были зачищены" 
        if self.Player.Level < self.LevelRequests: return "Минимальный уровень моба сильнее вашего максимального"
        self.on_hit(Damage)
        Damage -= self.Protect
        if Damage < 0: Damage = 1
        self.Health -= Damage
        if self.Health < 0: 
            threading.Thread(target=self.Death,args=()).start()
        else: self.Attack()

    def Death(self):
        """ Смерть """ 
        self.on_death()
        self.Status = False
        if self.DeathList == 0:
            self.on_first_death()
        self.DeathList += 1
        self.SpawnLimite -= 1
        time.sleep(self.SpawnRate)
        self.Revive()

    def Revive(self):
        """ Оживление """ 
        self.on_revive()
        self.Health = self.MaxHealth
        self.Status = True


    def on_hit(self,Damage : int): 
        """ Вызывается когда моб собирается получить урон """ 
        pass
    def on_first_death(self): 
        """ Вызывается всего 1 раз. При первой победе над мобом """ 
        pass
    def on_death(self): 
        """ Вызывается когда моб погибает """ 
        pass
    def on_heal(self): 
        """ Вызывается когда моб лечится """ 
        pass
    def on_spawn(self): 
        """ Вызывается только при первом появлении моба """ 
        pass
    def on_revive(self): 
        """ Вызывается каждое появление моба """ 
        pass

    def __repr__(self):
        return f"Name: [{self.Name}]            Description: [{self.Description}]            DropLoot_Description: [{self.DropLoot_Description}]\nDropLoot: [{self.DropLoot}]            Health: [{self.Health}]            MaxHealth: [{self.MaxHealth}]\nDamage: [{self.Damage}]            Protect: [{self.Protect}]            Breaks_the_equipment: [{self.Breaks_the_equipment}]            \nSpawnRate: [{self.SpawnRate}]            SpawnLimite: [{self.SpawnLimite}]            DeathList: [{self.DeathList}]            \nStatus: [{self.Status}]            NextMob: [{self.NextMob}]            Information: [{self.Information}]"



class Training_dummy(Mob):
    def __init__(self,Player):
        self.Player = Player
        super().__init__(
            Name                    = "Тренировочный манекен",
            Description             = "На нём вы можете проверить свою экипировку",
            DropLoot_Description    = "С этого моба ничего не выпадает",
            DropLoot                = None,
            Health                  = 3250000,
            MaxHealth               = 3250000,
            Damage                  = 0,
            Protect                 = 9999999999999999,
            Breaks_the_equipment    = False,
            SpawnRate               = 1.0,
            SpawnLimite             = 1,
            NextMob                 = "Неизвестно",
            Level                   = 1,
            LevelRequests           = 1,
            Class                   = "Тренировка")

    def Attack(self):
        # Этот моб не может атаковать
        pass


class Slime(Mob):
    def __init__(self,Player):
        self.Player = Player
        super().__init__(
            Name                    = "Слизь",
            Description             = "Живая слизь. Статус: безобидная",
            DropLoot_Description    = "2 золотых / 300 ед. опыта",
            DropLoot                = None,
            Health                  = 1000,
            MaxHealth               = 1000,
            Damage                  = 5,
            Protect                 = 100,
            Breaks_the_equipment    = False,
            SpawnRate               = 1.0,
            SpawnLimite             = 15,
            NextMob                 = Goblin,
            Level                   = 1,
            LevelRequests           = 1,
            Class                   = "Безобидная")
    
    def on_death(self):
        self.Player.Exp_Add(300)
        self.Player.Gold_Add(2)


class Goblin(Mob):
    def __init__(self,Player):
        self.Player = Player
        super().__init__(
            Name                    = "Гоблин",
            Description             = "Гоблины крайне слабы по одиночке. однако в группах могут представить серьёзную опастность",
            DropLoot_Description    = "Уровень / Награбленные вещи гоблинов с 5% шансом",
            DropLoot                = None,
            Health                  = 3500,
            MaxHealth               = 3500,
            Damage                  = 100,
            Protect                 = 200,
            Breaks_the_equipment    = False,
            SpawnRate               = 1.0,
            SpawnLimite             = 15,
            NextMob                 = Wolf,
            Level                   = 5,
            LevelRequests           = 5,
            Class                   = "Слабая",
            Information             = "Каждый Гоблин атакует.\nГоблины наносят не всегда свой 100% урон.")
    
    def on_death(self):
        self.Player.LevelUp(self.Player.mode.one)
        if random.randint(1,100) <= 5:
            self.Player.Inventor.append(Items.ItemFromGoblin(self.Player))

    def Attack(self):
        for _ in range(self.SpawnLimite):
            self.Player.GetDamage(random.randint(1,self.Damage))


class Wolf(Mob):
    def __init__(self,Player):
        self.Player = Player
        super().__init__(
            Name                    = "Волк",
            Description             = "Сильный противник. Следует быть подготовленным к сражению против него",
            DropLoot_Description    = "100 золотых / 500 опыта / 1% на шанс выпадения клыка",
            DropLoot                = None,
            Health                  = 8000,
            MaxHealth               = 8000,
            Damage                  = 5000,
            Protect                 = 1000,
            Breaks_the_equipment    = False,
            SpawnRate               = 1.0,
            SpawnLimite             = 5,
            NextMob                 = "Неизвестно",
            Level                   = 30,
            LevelRequests           = 15,
            Class                   = "Опасный",
            Information             = "Прокусывает броню(Игнорирует 50% всей брони)\nВолки охотятся ночью, из за чего при попытки напасть на них, призовётся стая. Стая: все волки наносят урон, + от 5 до 10 волков")
        self.Flock = True

    def on_death(self):
        self.Player.Gold_Add(100)
        self.Player.Exp_Add(500)
        if random.randint(1,100) <= 1:
            self.Player.Inventor.append(Items.Fang(self.Player))

    def Attack(self):
        if datetime.datetime.now().hour < 8 and self.Flock:
            self.Flock = False
            self.SpawnLimite += random.randint(5,10)
        if self.Flock == False:
            for _ in range(self.SpawnLimite):
                self.Player.GetDamage(random.randint(1 + round(self.Player.Protect / 0.5),self.Damage + round(self.Player.Protect / 0.5)))
        else:
            self.Player.GetDamage(random.randint(1 + round(self.Player.Protect / 0.5),self.Damage + round(self.Player.Protect / 0.5)))


class Zombie(Mob):
    def __init__(self,Player):
        self.Player = Player
        super().__init__(
            Name                    = "Зомби",
            Description             = "Ходячий мертвец, способный жить только под инстинктами",
            DropLoot_Description    = "??? **??? означает что чтобы открыть что из него выпадает, нужно его убить**",
            DropLoot                = None,
            Health                  = 90000,
            MaxHealth               = 90000,
            Damage                  = 15000,
            Protect                 = 1000,
            Breaks_the_equipment    = False,
            SpawnRate               = 1.0,
            SpawnLimite             = 1,
            NextMob                 = "Неизвестно",
            Level                   = 60,
            LevelRequests           = 55,
            Class                   = "Смертельный",
            Information             = "50% шанс пережить смертельную атаку, и востановиться / Каждая атака покрывает ядом(500 ед./3с.) **Яд игнорирует броню, и наносит урон постепенно**")
        self.Flock = True

    def on_first_death(self):
        self.DropLoot_Description = "Выпадает всего 1 раз: Мешок для увелечение максимального количество золота на 30к / 15к золотых\nВыпадает всегда: 1к золотых / 2 уровня (если уровень игрока выше 100. заменяется на 2к золотых)"
        self.Player.MaxGold += 30000
        self.Player.Gold += 15000


    def Death(self):
        """ Смерть """ 
        if random.randint(1,100) <= 50:
            self.Revive()
            return
        self.on_death()
        self.Status = False
        if self.DeathList == 0:
            self.on_first_death()
        self.DeathList += 1
        self.SpawnLimite -= 1
        time.sleep(self.SpawnRate)
        self.Revive()


    def on_death(self):
        if self.Player.Level < 100:
            self.Player.LevelUp(2)
        self.Player.Gold_Add(1000)


class SlimeOfKing(Mob):
    def __init__(self,Player):
        self.Player = Player
        super().__init__(
            Name                    = "Король Слаймов",
            Description             = "Его величество Король Слаймов. Является стражем 100 уровня. После его смерти, вам будет доступен новый этаж",
            DropLoot_Description    = "Выпадает всего 1 раз: Повышение лимита на уровень",
            DropLoot                = None,
            Health                  = 55000000,
            MaxHealth               = 55000000,
            Damage                  = 3900000,
            Protect                 = 500000,
            Breaks_the_equipment    = False,
            SpawnRate               = 1.0,
            SpawnLimite             = 1,
            NextMob                 = "Неизвестно",
            Level                   = 120,
            LevelRequests           = 100,
            Class                   = "Королевская особь",
            Information             = "После смерти распадается на свою копию, только слабее(в х2 раза). вплоть до полного уничтожения")
        self.Flock = True

    def on_first_death(self):
        self.Player.MaxLevel += 200


    def Death(self):
        """ Смерть """ 
        if self.MaxHealth > 100:
            self.MaxHealth /= 2
            self.Damage /= 2
            self.Protect /= 2
            if self.Damage <= 0: self.Damage = 1
            if self.Protect <= 0: self.Protect = 1
            self.Health = self.MaxHealth
            return
        self.on_death()
        self.Status = False
        if self.DeathList == 0:
            self.on_first_death()
        self.DeathList += 1
        self.SpawnLimite -= 1
        time.sleep(self.SpawnRate)
        self.Revive()
    


    def on_death(self):
        if self.Player.Level < 100:
            self.Player.LevelUp(2)
        self.Player.Gold_Add(1000)