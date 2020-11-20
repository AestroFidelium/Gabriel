import pickle

class Gabriel():

    def __init__(self):
        print("Создания класса Габриэль")

        self.Guilds = list()

    @staticmethod
    def Open():
        """ Открыть сохраненный класс Габриэль """
        try:
            with open(f"./Resurses/System/Gabriel_Config.txt","rb") as file:
                return pickle.load(file)
        except: return Gabriel()
    
    def Save(self):
        """ Сохранить класс Габриэль """

        copy = self.Open()
        try:
            with open(f"./Resurses/System/Gabriel_Config.txt","wb") as file:
                pickle.dump(self,file)
        except BaseException as Err: 
            with open(f"./Resurses/System/Gabriel_Config.txt","wb") as file:
                pickle.dump(copy,file)
            print(f"Не удалось сохранить \n [{Err}]")

class Guild():
    def __init__(self,test):
        self.test = test

if __name__ == "__main__":
    Ga = Gabriel.Open()