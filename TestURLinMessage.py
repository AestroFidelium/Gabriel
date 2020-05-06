import time

def CheckMessageIn(target,Message):
    a = list()
    a.extend(Message)
    Checking = ""
    curTarget = list() ; curTarget.extend(target)
    for Word in a:
        for _target_list_ in range(len(curTarget)):
            if Word == str(curTarget[_target_list_]):
                Checking += Word
    lst = list()
    lst.extend(Checking)
    truMsg = ""
    Counts = 0
    target_counts = list()
    target_counts.extend (target)
  #  print(len(target_counts))
  #  print(lst)
    Verno = 0
    CurVerno = 0
    for Latter in lst:
        if Latter == curTarget[int(Counts)]:
            Counts += 1
            CurVerno += 1
            Verno = CurVerno
            truMsg += Latter
            #print(truMsg)
        else:
            Verno -= 1
        if Verno == len(target_counts):
            return True
        #print(Verno)
        pass
    if truMsg == target:
        return True
    else:
        return False

msg = "https://sun9-20.userapi.com/4owWlCQerXWzWlNmB8-69jC-OkCI1cGV9m149A/_Fc4pHijhJ0.jpg"



# msg = str.upper(msg)

# _target_ = "gachi"

# _target_ = str.upper(_target_)

# print(CheckMessageIn(_target_,msg))









# for sfa in lst:
#         if sfa == curTarget[int(Counts)]:
#             Counts += 1
#             CountVerno += 1
#             truMsg += sfa
#         print(sfa)
#         if (CountVerno != 0) and (CountVerno != len(target_counts)):
#             #return False
#             print("NO")