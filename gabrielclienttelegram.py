from gabriel.logic.logic import CommandHelper
from telebot import TeleBot, types
import telebot
from telebot.types import Message
import logging
import time
import datetime
from gabriel.BazeData import telegramm_token as token
import os
import gabriel.logic as GabriLogic
from telebot.types import InlineQueryResultArticle,InputTextMessageContent

from shutil import copyfile

logging.basicConfig(force=True)
Logger = logging.getLogger()
Logger.setLevel(logging.DEBUG)

for pack in ["urllib3"]:
    logging.getLogger(pack).setLevel(logging.CRITICAL)


logging.addLevelName(100, "BUG")
logging.addLevelName(1000, "CRUSHED")
_time = datetime.datetime.now().strftime(r'%d.%m.%y %H;%M')

handler = logging.FileHandler(f'./logs/{_time}.log', 'w', 'utf-8')
handler.setFormatter(logging.Formatter(
    '[%(levelname)s]: [%(message)s] FuncName: [%(funcName)s] Time after start: [%(relativeCreated)d] Secs: [%(msecs)d] Line: [%(lineno)d] [%(name)s] [%(asctime)s]'))
Logger.addHandler(handler)


Bot = TeleBot(token, parse_mode=None)

Gabriel = GabriLogic.Gabriel.Open(False)

Logger.info("Создаются логи")



COMMAND_LIST = [
    CommandHelper("help",
        "Помощь по командам",
        "/help",
        0,
        ["help","profile"]),
    CommandHelper("profile",
        "Открыть профиль игрока",
        "/help profile",
        1),
    CommandHelper("whoiam",
        "Кто я",
        "/help whoiam",
        2),
    CommandHelper("ban",
        "Кто я",
        "/help ban",
        3,
        ["Jesus","Who","SomeOne","Noone","ded"]),
]

class BotApp():
    def __init__(self):
        Logger.info("Бот запустился")
        Bot.polling(True)

    @Bot.message_handler(commands=['start'])
    def Start_command(message: Message):
        if message.chat.type == "private":
            Bot.delete_message(message.chat.id, message.id)
            if str(message.from_user.last_name) == "None":
                last_name = ""
            else:
                last_name = message.message.chat.last_name
            User = GabriLogic.GabrielUser.Open(
                message.from_user.id, f"{message.from_user.first_name}{last_name}")

            markup = types.InlineKeyboardMarkup()
            markup.add(
                types.InlineKeyboardButton(".", callback_data="."),
                types.InlineKeyboardButton("..", callback_data=".."),
                types.InlineKeyboardButton("...", callback_data="..."),
                types.InlineKeyboardButton("....", callback_data="...."),
                types.InlineKeyboardButton(".....", callback_data=".....")
            )
            User.InfoMessage = Bot.send_message(
                message.chat.id, f"{User.Name} Профиль был успешно создан", reply_markup=markup)
            User.GameMessage = Bot.send_message(
                message.chat.id, f"Поле игры типа того", reply_markup=markup)
            User.SettingsMessage = Bot.send_message(
                message.chat.id, f"Настройки и прочее", reply_markup=markup)

            User.Save()

    @Bot.message_handler(content_types='text')
    def on_message(message: Message):
        if message.chat.type == "private":
            # Bot.delete_message(message.chat.id, message.id)
            ...

    @Bot.callback_query_handler(func=lambda call: True)
    def callback_inline(call: types.CallbackQuery):
        try:
            if call.message:
                if str(call.from_user.last_name) == "None":
                    last_name = ""
                else:
                    last_name = call.message.chat.last_name
                User = GabriLogic.GabrielUser.Open(
                    call.from_user.id, f"{call.from_user.first_name}{last_name}")
                if call.data in ['i like it', "i dont like it"]:
                    try:
                        Post = [
                            post for post in Gabriel.Posts if post.Message.id == call.message.id][0]
                    except:
                        msg = "Слишком старое изображение"
                        Bot.answer_callback_query(call.id, msg, True)
                        Logger.info(msg)
                        return
                    keyboard = Post.Message.reply_markup.keyboard[0]
                    like_it = keyboard[0]
                    dislike_it = keyboard[1]

                    if call.data == 'i like it':
                        if User.Name not in Post.Likers:
                            Post.Likers.append(User.Name)
                            Post.Likes += 1
                            like_it.text = f"{Post.Likes} 👍"
                            Logger.debug(f"{User.Name} 👍(+1)")

                            if User.Name in Post.Dislikers:
                                Post.Dislikers.remove(User.Name)
                                Post.Dislikes -= 1
                                dislike_it.text = f"{Post.Dislikes} 👎"

                                Bot.answer_callback_query(call.id, "👎 »»»» 👍")
                            else:
                                Bot.answer_callback_query(call.id, "👍")
                        else:
                            Post.Likers.remove(User.Name)
                            Post.Likes -= 1
                            like_it.text = f"{Post.Likes} 👍"

                            Logger.debug(f"{User.Name} 👍(-1)")
                            Bot.answer_callback_query(call.id, "±")

                    elif call.data == 'i dont like it':
                        if User.Name not in Post.Dislikers:
                            Post.Dislikers.append(User.Name)
                            Post.Dislikes += 1
                            dislike_it.text = f"{Post.Dislikes} 👎"
                            Logger.debug(f"{User.Name} 👎(+1)")

                            if User.Name in Post.Likers:
                                Post.Likers.remove(User.Name)
                                Post.Likes -= 1
                                like_it.text = f"{Post.Likes} 👍"
                                Bot.answer_callback_query(call.id, "👍 »»»»» 👎")
                            else:
                                Bot.answer_callback_query(call.id, "👎")
                        else:
                            Post.Dislikers.remove(User.Name)
                            Post.Dislikes -= 1
                            dislike_it.text = f"{Post.Dislikes} 👎"
                            Bot.answer_callback_query(call.id, "±")
                            Logger.debug(f"{User.Name} 👎(-1)")

                    User.Save()
                    markup = types.InlineKeyboardMarkup()
                    markup.add(like_it, dislike_it, types.InlineKeyboardButton(
                        "✕", callback_data="delete message"))
                    Bot.edit_message_reply_markup(
                        call.message.chat.id, call.message.id, reply_markup=markup)
                elif call.data in ['delete message']:
                    try:
                        post = [
                            post for post in Gabriel.Posts if post.Message.id == call.message.id][0]
                    except:
                        msg = "Слишком старое изображение"
                        Bot.answer_callback_query(call.id, msg, True)
                        Logger.info(msg)
                        return

                    if call.from_user.id == post.Author_id:
                        Bot.answer_callback_query(
                            call.id, "Сообщение было удалено")
                        Bot.delete_message(
                            call.message.chat.id, call.message.id)
                        Logger.debug(f"{User.Name} удалил фото")

                    else:
                        Bot.answer_callback_query(
                            call.id, "Вы должны быть автором этого сообщения")
                else:
                    Bot.answer_callback_query(call.id, "Неизвестная кнопка")
                    Logger.warning(f"[{call.data}] не была использована")

                Gabriel.Save()
        except Exception as error:
            Logger.log(100, error)

    @Bot.message_handler(content_types=['photo'])
    def on_photo(message: Message):
        User = GabriLogic.GabrielUser.Open(
            message.from_user.id, f"{message.from_user.first_name} {message.from_user.last_name}")

        Logger.debug(f"{User.Name} отправил фото")

        markup = types.InlineKeyboardMarkup()

        markup.add(
            types.InlineKeyboardButton("0 👍", callback_data='i like it'),
            types.InlineKeyboardButton("0 👎", callback_data='i dont like it'),
            types.InlineKeyboardButton("✕", callback_data="delete message")
        )
        Message = Bot.send_photo(
            message.chat.id, message.photo[0].file_id, disable_notification=True, reply_markup=markup)

        Gabriel.Posts.append(GabriLogic.Post(message.from_user.id, Message))

        User.Save()
        Gabriel.Save()

        Bot.delete_message(message.chat.id, message.id)













    @Bot.inline_handler(lambda query: True)
    def default_query(inline_query: types.InlineQuery):
        Message = str(inline_query.query)

        def DisplayArgs(args):  
            Return = []
            for value, arg in enumerate(args):
                Return.append(InlineQueryResultArticle(
                        id=value,
                        title=arg,
                        input_message_content=InputTextMessageContent(
                            arg)))
            return Return


        #Ничего не написано
        if Message == "":
            Bot.answer_inline_query(inline_query.id, [command.ResultArticle for command in COMMAND_LIST])
        
        #Начал писать что то либо
        else:
            Commands = Message.lower().split(" ")
            SeemIt = [command for command in COMMAND_LIST if command.name.lower().startswith(Commands[0])]

            #Проверяет закончилась ли название команды
            if len(SeemIt) == 1 and SeemIt[0].name == Commands[0]:
                command = SeemIt[0]

                for LEN in range(0,len(Commands) - 1,1):
                    # Первый параметр
                    try:
                        ArgSeemLike = [arg for arg in command.args[LEN] if arg.lower().startswith(Commands[LEN + 1])]
                        Bot.answer_inline_query(inline_query.id, DisplayArgs(ArgSeemLike))
                    except:
                        Bot.answer_inline_query(inline_query.id, [InlineQueryResultArticle(
                                                                id=0,
                                                                title="Команда завершена",
                                                                input_message_content=InputTextMessageContent(
                                                                    "Отправить команду типа"))])
            
            #Нет не закончилось так что продолжает показывать правильное написание команды
            else:
                Bot.answer_inline_query(inline_query.id, [InlineQueryResultArticle(id=0,title=command.name,input_message_content=InputTextMessageContent(command.output),description=command.description) for command in SeemIt])
        
                











def DeleteHistoryLogs(path_on_logs: str = "./logs/", max_counts: int = 5):
    logers = os.listdir(path_on_logs)
    if len(logers) <= max_counts:
        return
    logers.reverse()

    Logger.info(f"Очищаются старые логи")
    _count = 0
    for will_delete in logers[max_counts::]:
        Logger.warning(f"Лог за {will_delete} был удалён")
        os.remove(f"{path_on_logs}{will_delete}")
        _count += 1

    Logger.info(f"Логи были успешно очищены ({_count})")


def SaveLog():
    try:
        Name = handler.baseFilename.split("\\")[-1]
        copyfile(handler.baseFilename, f"./crush-logs/{Name}")
    except:
        Logger.log(100, "Логи не удается сохранить")
    finally:
        Logger.info("Логи успешно сохранены")


if __name__ == "__main__":
    DeleteHistoryLogs()
    DeleteHistoryLogs("./crush-logs/", 10)
    while True:
        try:
            BotApp()
        except BaseException as ERROR:
            Logger.log(1000, repr(ERROR))
            Logger.info("Сохранение логов")
            SaveLog()
            Logger.info("Происходит перезапуск")
