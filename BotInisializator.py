import discord
# import BazaDate
from discord import user
# import urllib
# from urllib.request import urlopen
import time
import random
import datetime
# import wget
# from PIL import Image, ImageDraw , ImageFont

def Checking():
    with open(f"TimeCount_Activite.txt","r") as file:
        TrueOrFalse = file.readline()
        if TrueOrFalse == "False":
            with open(f"TimeCount_Activite.txt","w") as file:
                file.writelines("True")
            today = datetime.datetime.today()
            secondWait = today.second
            secondWait = 60 - secondWait
            time.sleep(secondWait)
            with open(f"TimeCount_Activite.txt","w") as file:
                file.writelines("False")
            
    pass

async def AttackMessage(CurCommandPlayer : str,IntCurLvl : int,EnIntCurHealth : int,EnIntMaxHealth : int,FreeLvlHA : int,GetDamage : int,CurChannel):
    today = datetime.datetime.today()
    timeThen = str()
    Count = int()
    with open(f"TimeCount.txt","r") as file:
        timeThen = str(file.readline())
        Count = int(file.readline())
        FreeLvl = file.readline()
        TakeDamage = int(file.readline())
        Player = file.readline()
    Count += 1
    FreeLvlEnd = 0
    TakeDamage += GetDamage
    try:
        FreeLvlEnd = int(FreeLvl) + int(FreeLvlHA)
    except ValueError:
        FreeLvlEnd = 0
    
    with open(f"TimeCount.txt","w") as file:
        file.writelines(timeThen)
        file.writelines(f"{Count}")
        file.writelines(f"\n{str(FreeLvlEnd)}")
        file.writelines(f"\n{str(TakeDamage)}")
        file.writelines(f"\n{Player}")
    timeThenSplit = timeThen.split("-")
    # Checking(GoTo)
    if(int(timeThenSplit[4]) == today.minute) and (Player == CurCommandPlayer):
        return
    with open(f"TimeCount.txt","w") as file:
        today = datetime.datetime.today()
        file.writelines(str(today.strftime("%Y-%m-%d-%H-%M-%S")))
        file.writelines(f"\n-1")
        file.writelines(f"\n0")
        file.writelines(f"\n0")
        file.writelines(f"\n{CurCommandPlayer}")
    Emb = discord.Embed( title = f"{Player} убит(а) (x{Count})")
    Emb.add_field(name = 'Потерял(а) могущество : ',value = str(int(FreeLvlEnd)) + " лвл.")
    if IntCurLvl == 4:
        Emb.add_field(name = 'Минимальный уровень',value =  "4",inline = True)
    Emb.add_field(name = 'Здоровье : ',value = str(EnIntCurHealth) + " ед. / " + str(EnIntMaxHealth) + " ед.",inline = False)
    Emb.add_field(name = 'Получил(а) урона : ',value = str(TakeDamage) + " ед.",inline = True)
    #Emb.set_image(url='https://sun9-20.userapi.com/c200720/v200720465/513de/84w3r07gfAI.jpg')

    #return Emb
    await CurChannel.send(embed = Emb)