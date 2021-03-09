from gabriel.gabrielclient import RunDiscord
from gabrielclienttelegram import BotApp


if __name__ == "__main__":
    answer = input("Telegram/Discord (T/D): ").lower()
    if answer == "d":
        RunDiscord()
    else:
        BotApp()