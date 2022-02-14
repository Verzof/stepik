import json
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.utils.markdown import hbold, hlink
import os
import asyncio
import telebot, re
import telebot, wikipedia, re

# Создаем экземпляр бота
bot = telebot.TeleBot('5026195738:AAEvvgBrxLC1ONQnPHWdVyWoXiZXCuBGnJ0')
# Устанавливаем русский язык в Wikipedia
wikipedia.set_lang("ru")


# Чистим текст статьи в Wikipedia и ограничиваем его тысячей символов
@bot.message_handler(commands=["start"])
def start(message_bot, res=False):
    # bot.send_message(message_bot.chat.id,
    #                  'Это Вики-бот для зайчика, он ищет зайчие запросы, напиши что-нибудь.\nНапример:Заяц')
    start_buttons = ['🔪 Ножи', '🥊 Перчатки', '🔫 Снайперские винтовки']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)


# def getwiki(s):
#     try:
#         ny = wikipedia.page(s)
#         # Получаем первую тысячу символов
#         wikitext = ny.content[:1000]
#         # Разделяем по точкам
#         wikimas = wikitext.split('.')
#         # Отбрасываем
#         wikimas = wikimas[:-1]
#         # Создаем пустую переменную для текста
#         wikitext2 = ''
#         # Проходимся по строкам, где нет знаков
#         for x in wikimas:
#             if not ('==' in x):
#                 # Если в строке осталось больше трех символов, добавляем ее к нашей переменной и возвращаем утерянные
#                 if (len((x.strip())) > 3):
#                     wikitext2 = wikitext2 + x + '.'
#             else:
#                 break
#         # Теперь при помощи регулярных выражений убираем разметку
#         wikitext2 = re.sub('\([^()]*\)', '', wikitext2)
#         wikitext2 = re.sub('\([^()]*\)', '', wikitext2)
#         wikitext2 = re.sub('\{[^\{\}]*\}', '', wikitext2)
#         # Возвращаем текстовую строку
#         return wikitext2
#     # Обрабатываем исключение, которое мог вернуть модуль wikipedia при запросе
#     except Exception as e:
#         return 'В энциклопедии нет информации об этом - заяц, придумай другое слово'
#
#
# # Получение сообщений от юзера
# @bot.message_handler(content_types=["text"])
# def handle_text(message):
#     bot.send_message(message.chat.id, getwiki(message.text))


# Запускаем бота
bot.polling(none_stop=True, interval=0)
