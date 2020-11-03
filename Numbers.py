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
