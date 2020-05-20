# newDict = {
#     "Vampirism" : {
#         "Name" : "Вампиризм",
#         "Descript" : "Ага да"
#     },
#     "Posion" : {
#         "Name" : "Яд",
#         "Descript" : "АЫАФЫ"
#     }
# }
# Keys = newDict.keys()
# Keys = list(Keys)
# print(Keys[0])
# print(newDict[Keys[0]])

from botFunctions import CheckParametrsEquipment


ThisItem = CheckParametrsEquipment(username="KOT32500",ID=1)

_magic = ThisItem["magic"]
_magic = _magic['Parametrs']
_magic = _magic[0]
Keys = _magic.keys()
for key in Keys:
    key = str(key)
    Spell = _magic[key]
    Name = Spell.pop('name') #Description
    Description = Spell.pop('Description')
    KeysSpell = Spell.keys()
    Txt = f"{Name} "
    for Key in KeysSpell:
        key = str(Key)
        Stat = Spell[key]
        Txt += f"{Stat}"
    Txt += "\n"
    print(Txt)
