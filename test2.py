test = {
    "main" : {
        "health": 5,
        "maxHealth" : 1,
        "Level" : 5
    },
    "d": {
        "da":"dsa"
    }
}


main = test["main"]
udater = {
    "maxHealth" : 10
}
main.update(udater)
test.update(main)
print(test)