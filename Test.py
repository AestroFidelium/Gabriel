# from PIL import Image, ImageDraw , ImageFont
# import botFunctions as Functions
# Resurses = "./Resurses/"
# def profileEdit(_UserName_):
#     """
#     Меняет профиль игрока. Относиться к команде Profile


#     Вход :
#         _UserName_ = Имя игрока. Str формат
#     Выход :
#         Файл = Discord.File
#     """
#     # MainStats = _readStats(_UserName_)
#     MainStats = Functions.ReadMainParametrs(username=_UserName_)
#     IntCurExp = int(MainStats.pop("exp"))
#     IntCurLvl = int(MainStats.pop("lvl"))
#     IntMaxHealth = int(MainStats.pop("maxHealth"))
#     IntCurHealth = int(MainStats.pop("curHealth"))
#     IntMaxDamage = int(MainStats.pop("damage"))
#     Description = str(MainStats.pop("description"))
#     DescriptionSplit = Description.split()
#     Description = ""
#     for target_list in DescriptionSplit:
#         ABM = str.upper(target_list)
#         if ABM != "ABOUT_ME":
#             Description += target_list + " "
    
#     AllLatters = list()
#     AllLatters.extend(Description)
#     Description = ""
#     countLatter = 0
#     for Latter in AllLatters:
#         countLatter += 1
#         if countLatter == 32:
#             countLatter = 0
#             Description += f"\n{Latter}"
#         else:
#             Description += Latter
    
#     ShopAgent = Functions.ReadMainParametrs(username=_UserName_)
#     Messages = int(ShopAgent.pop("messages"))
#     Gold = int(ShopAgent.pop("money"))
#     try:
#         BackGround = Image.open(f"{Resurses}BackGround_{_UserName_}.webp")
#     except: BackGround = Image.open(f"{Resurses}BackGround_StandartBackGround.webp")

#     img = Image.open(Resurses + "Main.webp")
#     try:
#         N_Ava = Image.open(Resurses + _UserName_ + ".webp")
#     except:
#         raise ErrorAvatar("Отсустует аватарка")

#     Ava = N_Ava.resize((264,264)) #76 76

#     draw = ImageDraw.Draw(img)
#     count = 10
#     counts = 0
#     ElseCount = 0
#     Scaling = 50
#     for target_list in range(int(IntCurLvl)):
#         if target_list < -5:
#             print("ERROR")
#         counts += 1
#         if counts >= int(count):
#             count = str(count) + "0"
#             counts = 0
#             ElseCount += 5
#             Scaling -= 1

#     areaT = (163 - ElseCount,309) #121 153
#     font = ImageFont.truetype("arial.ttf",Scaling)
#     draw.text(areaT,str(IntCurLvl),font=font,fill="black")



#     #AgentConfig = _AgentReadConfig(_UserName_)

#     area = (370,155)
#     Color = (200,210,255)
#     # Color = AgentConfig
#     font = ImageFont.truetype("arial.ttf",100)
#     draw.text(area,_UserName_,font=font,fill=Color)
#     try:
#         Item_ID = Functions.ReadEquipment(username=_UserName_,type="Экипировка")
#         ItemProtect = Functions.CheckParametrsEquipment(username=_UserName_,ID=Item_ID)
#         protect = ItemProtect["protect"]
#         area = (570 - 20,289 - 13)
#         Color = (0,0,0)
#         font = ImageFont.truetype("arial.ttf",35)
#         txt = str(f"Здоровье : {str(IntCurHealth)} ед./ {str(IntMaxHealth)} ({protect})")
#         draw.text(area,txt,font=font,fill=Color)
#     except:
#         area = (570 - 20,289 - 13)
#         Color = (0,0,0)
#         font = ImageFont.truetype("arial.ttf",35)
#         txt = str(f"Здоровье : {str(IntCurHealth)} ед./ {str(IntMaxHealth)}")
#         draw.text(area,txt,font=font,fill=Color)

#     area = (570 - 20,341 - 13)
#     Color = (0,0,0)
#     font = ImageFont.truetype("arial.ttf",35)
#     try:
#         DmgItemID = Functions.ReadEquipment(username=_UserName_,type="Оружие")
#         Item = Functions.CheckParametrsEquipment(username=_UserName_,ID=DmgItemID)
#         DamageItem = Item.pop('damage')
#     except:
#         DamageItem = 0
    
#     txt = str(f"Урон : {str(IntMaxDamage)} +({DamageItem}) ед.")
#     draw.text(area,txt,font=font,fill=Color)


#     #Slider Exp
#     # 686 = 100%
#     # 342 = 0%
#     # 35% 
#     # 500 = 35%
#     EndPoint = 686 - 342
#     EndPoint /= 100
#     EndPoint *= 5
#     EndPoint += 342
#     fstPoints = (342,761,EndPoint,761)
#     # EndPoints = (686,743,686,780)
#     Color = (255,0,255)
#     draw.line(fstPoints,fill=Color,width=37)
#     #Slider Exp
    
#     area = (380,743)
#     Color = (0,0,0)

#     font = ImageFont.truetype("arial.ttf",35)
#     txt = str(f"Опыт : {IntCurExp} / {IntCurLvl * 5}")
#     draw.text(area,txt,font=font,fill=Color)

#     Main_characteristics = Functions.ReadMainParametrs(username=_UserName_)

#     strength = float(Main_characteristics.pop("strength"))
#     agility = float(Main_characteristics.pop("agility"))
#     intelligence = float(Main_characteristics.pop("intelligence"))
#     plus = int(Main_characteristics.pop("plus"))
#     if plus > 0:
#         area = (782,700)
#         Color = (100,110,90)
#         font = ImageFont.truetype("arial.ttf",30)
#         txt = str(f"Талант очки : {plus}")
#         draw.text(area,txt,font=font,fill=Color)


#     Color = (255,100,0)
#     area = (38,393)
#     font = ImageFont.truetype("arial.ttf",35)
#     txt = str(f"Сила : \n{strength}")
#     draw.text(area,txt,font=font,fill=Color)
#     # draw.line((25 - 5,195,100 - 5,195),fill=Color,width=5)

#     Color = (0,255,0)
#     area = (38,471)
#     font = ImageFont.truetype("arial.ttf",35)
#     txt = str(f"Ловкость : \n{agility}")
#     draw.text(area,txt,font=font,fill=Color)

#     Color = (0,255,255)
#     area = (38,570)
#     font = ImageFont.truetype("arial.ttf",35)
#     txt = str(f"Интеллект : \n{intelligence}")
#     draw.text(area,txt,font=font,fill=Color)

    
            
    

#     area = (570 - 20,393 - 13)
#     Color = (0,0,0)
#     font = ImageFont.truetype("arial.ttf",35)
#     txt = str("Золота : " + str(Gold) + " / " + str(Messages))
#     draw.text(area,txt,font=font,fill=Color)

#     Color = (0,0,0)
#     The_number_of_letters = list()
#     Scaling = 0
#     The_number_of_letters.extend(Description)
#     countLetter = 0
#     Offset = 0
#     for Letter in The_number_of_letters:
#         if (Letter == "ERROR"): pass
#         countLetter += 1
#         # print(f"{Letter} текущая буква")
#         if (countLetter == 4):
#             Scaling -= 1
#             countLetter = 0
#             Offset += 2
#             #print(f"{Letter} текущая строчка ({countLetter})")
#     # print(f"{The_number_of_letters} \n {Scaling}")
#     The_number_of_letters.clear()

#     Scaling = (18 + Scaling)
#     if Scaling < 0:
#         Scaling = 0
#     area = (110,200 + Offset)
#     font = ImageFont.truetype("arial.ttf",10 + Scaling)
#     txt = str(Description)
#     draw.text(area,txt,font=font,fill=Color)

#     area = (380,470)
#     font = ImageFont.truetype("arial.ttf",35)
#     txt = str("О себе : \n")
#     draw.text(area,txt,font=font,fill=Color)

#     areaAva = (46,8)

#     img.paste(Ava,areaAva)
#     nameSave = "StatsPl.webp"
#     BackGround = BackGround.resize((1000,1450)) #(358,481)
#     area = (0,550)
    
#     BackGround.paste(img.convert('RGB'), area, img)
#     BackGround.save(nameSave)

#     sf = discord.File(nameSave,nameSave)
#     return sf