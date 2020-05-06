class testword():
    """
    .
    """
    Find = False
    def __init__(self,message : str,target : list):
        self.message = message
        self.target = target
        # self.Start()
    
    def Start(self):
        EveryoneWord = list()
        EveryoneWord.extend(self.message)
        TargetEveryone = list(); TargetEveryone.extend(self.target) 
        self.everyoneWord = EveryoneWord
        self.targetEveryone = TargetEveryone
        # print(self.everyoneWord)
        count = 0
        for word in self.everyoneWord:
            if word == " ":
                count = 0
            else:
                try:
                    if word == TargetEveryone[count]:
                        count += 1
                        # print(f"{word} равно")
                        if count == len(self.target):
                            print(f"`{self.target}` найдено")
                            Find = True
                            return Find
                    elif word != TargetEveryone[count]:
                        count = 0
                        # print(word)
                except IndexError:
                    # print("error")
                    pass
        pass

message = "твоя ава - гачи ты её сам делал? гачи"
target = "гачи"
# message = "я был я ться блять тут сука , 10 ебанных секунд блять назад"
# banWords = ["блять","сука","тут","ничего"]
tw = testword(message,target)
print(tw.Start())