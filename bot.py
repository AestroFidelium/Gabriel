import discord



class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
        print("$Help = для помощи")
        textInputChannel = "Пустота или 1 = Разработка-Габриэль \n2 = Основной чат \n3 = Справка\n Перевыбрать канал $Ch \n Текстовой канал : 1/3 : "
        ChannelInput = input(textInputChannel)
        while True:
            channelSendMyMessage = 0 #Разработка-Габриэль
            if(ChannelInput == "1"):
                channelSendMyMessage = self.get_channel(627140104988917789) #Разработка-Габриэль
            elif(ChannelInput == "2"):
                channelSendMyMessage = self.get_channel(419879599363850253) #Основной чат
            elif(ChannelInput == "3"):
                channelSendMyMessage = self.get_channel(623070280973156353) #Справка
            else:
                channelSendMyMessage = self.get_channel(627140104988917789) #Разработка-Габриэль
            msg = input("Message : ")
            if(msg == "$Ch"):
                ChannelInput = input(textInputChannel)
            elif(msg == "$Help"):
                print("'$Help' = Соказывает все команды, и как их использовать. \n'$Ch = Сменить текстовый канал \n'$St' = Сделать красивое меню под текст. \n~Принимает значения : 'Оглавление' = Самая первая надпись. \n'Название' = Вторая надпись, будет чуть меньше обычного текста, и серого цвета. \n'Текст' = Текст, который будет расположен в самом низу. Является обычным текстом, который входит в панель")
            elif(msg == "$St"):
                _title = input("Оглавление : ")
                _name = input("Название : ")
                _value = input("Текст : ")
                Emb = discord.Embed( title = _title)
                Emb.add_field(name = _name,value = _value)

                await channelSendMyMessage.send(embed = Emb)
                
            else:
                await channelSendMyMessage.send(msg)


    async def on_message(self, message):
    # don't respond to ourselves
        if message.author == self.user:
            return
        
        if message.content == 'Ы':
            await message.channel.send("Ы")


client = MyClient()
client.run("NjU2ODA4MzI3OTU0ODI1MjE2.Xik7NQ.pqnwoAWW_tDg25FVBzm5YLaVVw0")