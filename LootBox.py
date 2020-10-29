import Items


class ItemInList():
    def __init__(self,Item, Chance : float):
        self.Item = Item
        self.Chance = Chance

class Box():
    def __init__(self,
            Name : str = "Название коробки",
            ItemsList : list = "Что может выпасть с коробки"):
        self.Name = Name
        self.ItemsList = ItemsList