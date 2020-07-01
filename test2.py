stats = {
    "main":{
        "fs":312,
        "ewq":15
    },
    "qwe":{
        "da":5
    },
    "Inventor":["ItemDada","122"]
}


Inventor = stats['Inventor']
Inventor.append("Item113")
stats.update({"Inventor":Inventor})
print(stats)