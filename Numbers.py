import re


def Readable(n):
    s, *d = str(n).partition(".")
    r = ".".join([s[x-3:x] for x in range(-3, -len(s), -3)][::-1] + [s[-3:]])
    return "".join([r] + d)

def ReplaceNumber(index):
    Types = ["K","M","B",'T','P','E','Z','Y']
    if type(index) is str:
        err = False
        Index = re.split("\.",index)
        try:
            Type = Types[len(Index) - 2] 
        except:
            err = True
        counter = 2
        try:
            if int(Index[1][2:3]) > 5:
                counter += 1
            Index = f"{Index[0]}.{Index[1][:counter]}"
            if err:
                Count = str(re.sub("\.","",index))[26::].count("0")
                Count = round(Count / 3) + 1
                
                Index = f"{str(Index[:5])}YY"
                Index = f"{Index}{Count}"
                return Index
            return f"{Index}{Type}"
        except: return Index[0]
    if type(index) is int:
        return ReplaceNumber(Readable(index))
    else: raise ValueError("Ожидалось получить int")


def To_Int_From_Suffics(Value : str):
    """ Пример 
    Value == "100K" 
    Выход == 100000 """

    Suffics = re.sub(r"\d","",Value)[0::]
    Numbers = int(Value.split(Suffics)[0])
    
    class _type():
        def __init__(self,Suffics : str,Counter : int):
            self.Suffics = Suffics
            self.Counter = Counter

    Types = [
            _type("K",10 ** 3),
            _type("M",10 ** 6),
            _type("B",10 ** 9),
            _type('T',10 ** 12),
            _type('P',10 ** 15),
            _type('E',10 ** 18),
            _type('Z',10 ** 21),
            _type('Y',10 ** 24)]

    
    try: Numbers *= [i for i in Types if i.Suffics == Suffics][0].Counter
    except: 
        if Suffics == ".YY":
            Counter = int(Value.split("YY")[-1])
            Numbers = int(Value.split("YY")[0].replace(".",""))
            Multiple = 10 ** (26 + (3 * Counter))

            return Numbers * Multiple
        else:
            return Numbers
    return Numbers
