from telebot import TeleBot, types
import telebot
from telebot.types import Message
import logging
import time
import datetime
from gabriel.BazeData import telegramm_token as token
import os
import gabriel.logic as GabriLogic
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
    '[%(levelname)s]: [%(message)s] [%(funcName)s] [%(relativeCreated)d] [%(msecs)d] [%(lineno)d] [%(name)s] [%(asctime)s]'))
Logger.addHandler(handler)


Bot = TeleBot(token, parse_mode=None)

Gabriel = GabriLogic.Gabriel()

Logger.info("Создаются логи")


class BotApp():
    def __init__(self):
        Logger.info("Бот запустился")
        Bot.polling(True)

    @Bot.message_handler(commands=['start'])
    def Start_command(message: Message):
        Logger.debug(
            f"{message.from_user.username} использовал команду {message.text}")
        Bot.send_message(message.chat.id, "Привет чего над сосна")

    @Bot.message_handler(content_types='text')
    def on_message(message: Message):
        Logger.debug(
            f"{message.from_user.username} обратился с {message.text}")

    @Bot.callback_query_handler(func=lambda call: True)
    def callback_inline(call: types.CallbackQuery):
        try:
            if call.message:
                if str(call.message.chat.last_name) == "None":
                    last_name = ""
                else:
                    last_name = call.message.chat.last_name
                User = GabriLogic.GabrielUser.Open(
                    call.message.chat.id, f"{call.message.chat.first_name}{last_name}")
                if call.data in ['i like it', "i dont like it"]:
                    keyboard = call.message.reply_markup.keyboard[0]
                    like_it = keyboard[0]
                    dislike_it = keyboard[1]
                    Post = GabriLogic.Post(call.message.id)

                    oldPost = [
                        post for post in User.Posts if post.ID == Post.ID]
                    if oldPost:
                        Post = oldPost[0]
                    else:
                        User.Posts.append(Post)

                    if call.data == 'i like it':
                        if User.Name not in Post.Likers:
                            Post.Likers.append(User.Name)
                            num = int(like_it.text.split(" ")[0]) + 1
                            like_it.text = f"{num} 👍"
                            Post.Likes = num

                            Logger.debug(f"{User.Name} 👍")

                            if User.Name in Post.Dislikers:
                                Post.Dislikers.remove(User.Name)
                                num = int(dislike_it.text.split(" ")[0]) - 1
                                dislike_it.text = f"{num} 👎"
                                Post.Dislikes = num
                        else:
                            Post.Likers.remove(User.Name)
                            num = int(like_it.text.split(" ")[0]) - 1
                            like_it.text = f"{num} 👍"
                            Post.Likes = num
                            Logger.debug(f"{User.Name} Убрал отметку 👍")

                    elif call.data == 'i dont like it':
                        if User.Name not in Post.Dislikers:
                            Post.Dislikers.append(User.Name)
                            num = int(dislike_it.text.split(" ")[0]) + 1
                            dislike_it.text = f"{num} 👎"
                            Post.Dislikes = num

                            Logger.debug(f"{User.Name} 👎")

                            if User.Name in Post.Likers:
                                Post.Likers.remove(User.Name)
                                num = int(like_it.text.split(" ")[0]) - 1
                                like_it.text = f"{num} 👍"
                                Post.Likes = num
                                Logger.debug(f"{User.Name} Убрал отметку 👍")
                        else:
                            Post.Dislikers.remove(User.Name)
                            num = int(dislike_it.text.split(" ")[0]) - 1
                            dislike_it.text = f"{num} 👎"
                            Post.Dislikes = num

                            Logger.debug(f"{User.Name} Убрал отметку 👎")

                    User.Save()
                    markup = types.InlineKeyboardMarkup()
                    markup.add(like_it, dislike_it)
                    Bot.edit_message_reply_markup(
                        call.message.chat.id, call.message.id, reply_markup=markup)

        except Exception as e:
            Logger.log(100, repr(e))

    @Bot.message_handler(content_types=['photo'])
    def Start_command(message: Message):
        User = GabriLogic.GabrielUser.Open(
            message.from_user.id, f"{message.from_user.first_name} {message.from_user.last_name}")

        Logger.debug(f"{User.Name} отправил фото")

        markup = types.InlineKeyboardMarkup()

        markup.add(
            types.InlineKeyboardButton("0 👍", callback_data='i like it'),
            types.InlineKeyboardButton("0 👎", callback_data='i dont like it')
        )
        Bot.send_photo(
            message.chat.id, message.photo[0].file_id, disable_notification=True, reply_markup=markup)
        Bot.delete_message(message.chat.id, message.id)

        User.Save()

    # TODO: когда нибудь я обязательно вернусь сюда... когда нибудь

    @Bot.inline_handler(lambda query: len(query.query) == 0)
    def default_query(inline_query):
        try:
            you_see = types.InlineQueryResultArticle
            answer = types.InputTextMessageContent
            Bot.answer_inline_query(inline_query.id, [
                you_see('1', 'Скажи че нить', answer('MAGIC')),
                you_see('2', 'Скажи че нить по дискордвовскому',
                        answer('MAGIC')),
                you_see('3', 'Скажи где', answer('где')),
                you_see('4', 'Время улыбаться', answer('))))')),
                you_see('5', 'цоц', answer('позже позже да обязательно')),
                you_see('6', 'гачи', answer('го кекс')),
                you_see('7', 'иро', answer('MAGIC')),

            ])
        except Exception as e:
            Logger.error(e)


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
