# 1) Translate
from googletrans import Translator
import pyperclip
import keyboard

from googletrans import LANGUAGES

for lang in LANGUAGES:
    print(f'{lang} - {LANGUAGES[lang]}')
print()


first_language = input("first_language : ")
second_language = input("second_language : ")



def TransRU():
    try:
        txt = pyperclip.paste()
        trans = Translator()
        t = trans.translate(
            txt, src= first_language, dest=second_language
        )
        txtTranslate = t.text
        pyperclip.copy(txtTranslate)
        keyboard.write(txtTranslate)
    except Exception:
        print(Exception)
    
def TransEN():
    try:
        txt = pyperclip.paste()
        trans = Translator()
        t = trans.translate(
            txt, src= second_language, dest=first_language
        )
        txtTranslate = t.text
        pyperclip.copy(txtTranslate)
        keyboard.write(txtTranslate)
    except Exception:
        print(Exception)
try:
    def InterpreterTraining(_Text_,_TheMainLanguage_):
        txt_ = ""
        trans = Translator()
        t = trans.translate(_Text_, src= "ru", dest=_TheMainLanguage_);txt_ = t.text
        return txt_
    txt = "Переводчик"
    print(f"{InterpreterTraining(txt,first_language)}")
    txt = "Чтобы перевести текст, его сперва нужно будет копировать."
    print(f"{InterpreterTraining(txt,first_language)}")
    txt = "ctrl+f1 => Перевести текст с рус. на англ."
    print(f"{InterpreterTraining(txt,first_language)}")
    txt = "ctrl+f2 => Перевести текст с англ. на рус."
    print(f"{InterpreterTraining(txt,first_language)}")

    txt = "Версия 0.1 \n Создатель : "
    print(f"{InterpreterTraining(txt,first_language)} KOT32500 (https://vk.com/kot32500)")

    txt = "Конец информации. Текст ниже, означает что была ошибка"
    print(f"{InterpreterTraining(txt,first_language)}")

    keyboard.add_hotkey('ctrl+f1', TransRU)
    keyboard.add_hotkey('ctrl+f2', TransEN)
    keyboard.wait()
except ValueError:
    print("Wrong language is selected, restart the program")




'''
# 2) List supported languages
from googletrans import LANGUAGES

for lang in LANGUAGES:
    print(f'{lang} - {LANGUAGES[lang]}')
print()

# 3) List possible mistakes and translations 
pm = t.extra_data['possible-mistakes']
pt = t.extra_data['possible-translations']

print(f'Possible Mistakes: {pm}')
print(f'Possible Translations: {pt}')
'''