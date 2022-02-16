import json
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.utils.markdown import hbold, hlink
from main import collect_data
from os import getenv
import asyncio
import logging
from aiogram.utils.exceptions import BotBlocked
from config import *

# bot = Bot(token=str(TOKEN), parse_mode=types.ParseMode.HTML)
bot = Bot(token=getenv('BOT_TOKEN'), parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands='start')
async def start(message: types.Message):
    start_buttons = ['Кнопка 1', 'Кнопка 2', 'Кнопка 3', 'Кнопка 4']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)

    await message.answer('ТУТ БУДЕТ ТЕКСТ messageA ', reply_markup=keyboard)


@dp.message_handler(commands="answer")
async def cmd_answer(message: types.Message):
    await message.answer("Это простой ответ")


@dp.message_handler(commands="reply")
async def cmd_reply(message: types.Message):
    await message.reply('Это ответ с "ответом"')


@dp.message_handler(Text(equals='Кнопка 1'))
async def get_discount_knives(message: types.Message):
    file_open = open('./порты_открыты.txt', 'r', encoding='UTF-8')
    file_count = file_open.read()
    print(file_count)
    await message.answer(file_count)


# collect_data(cat_type=2)
#
# with open('result.json') as file:
#     data = json.load(file)
#
# for index, item in enumerate(data):
#     card = f'{hlink(item.get("full_name"), item.get("3d"))}\n' \
#         f'{hbold("Скидка: ")}{item.get("overprice")}%\n' \
#         f'{hbold("Цена: ")}${item.get("item_price")}🔥'
#
#
#     if index%20 == 0:
#         asyncio.sleep(3)
#
#     await message.answer(card)
#

@dp.message_handler(Text(equals='Кнопка 2'))
async def get_discount_knives(message: types.Message):
    file_open = open('./порты_закрыты.txt', 'r', encoding='UTF-8')
    file_count = file_open.read()
    print(file_count)
    await message.answer(file_count)


# @dp.message_handler(Text(equals='Кнопка 3'))
# async def get_discount_guns(message: types.Message):
#     file_open = open('порты_открыты.txt', 'r', encoding='UTF-8')
#     file_count = file_open.read()
#     print(file_count)
#     await message.answer(file_count)
#
#
# @dp.message_handler(Text(equals='Кнопка 4'))
# async def get_discount_knives(message: types.Message):
#     file_open = open('порты_открыты.txt', 'r', encoding='UTF-8')
#     file_count = file_open.read()
#     print(file_count)
#     await message.answer(file_count)


# collect_data(cat_type=4)
#
# with open('result.json') as file:
#     data = json.load(file)
#
# for index, item in enumerate(data):
#     card = f'{hlink(item.get("full_name"), item.get("3d"))}\n' \
#         f'{hbold("Скидка: ")}{item.get("overprice")}%\n' \
#         f'{hbold("Цена: ")}${item.get("item_price")}🔥'
#
#
#     if index%20 == 0:
#         asyncio.sleep(3)
#
#     await message.answer(card)
# @dp.message_handler()
# async def echo_message(msg: types.Message):
#     await bot.send_message(msg.from_user.id, msg.text)
#     print(msg.text)


# # @dp.message_handler(commands=['file'])
# async def process_file_command(message: types.Message):
#     user_id = message.from_user.id
#     await bot.send_chat_action(user_id, ChatActions.UPLOAD_DOCUMENT)
#     await asyncio.sleep(1)  # скачиваем файл и отправляем его пользователю
#     await bot.send_document(user_id, TEXT_FILE,
#                             caption='Этот файл специально для тебя!')
@dp.message_handler(commands="url")
async def cmd_inline_url(message: types.Message):
    buttons = [
        types.InlineKeyboardButton(text="GitHub", url="https://github.com"),
        types.InlineKeyboardButton(text="Оф. канал Telegram", url="tg://resolve?domain=telegram")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await message.answer("Кнопки-ссылки", reply_markup=keyboard)


@dp.message_handler(commands="special_buttons")
async def cmd_special_buttons(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # keyboard.add(types.KeyboardButton(text="Запросить геолокацию", request_location=True))
    keyboard.add(types.KeyboardButton(text="Запросить контакт", request_contact=True))
    keyboard.add(types.KeyboardButton(text="Создать викторину",
                                      request_poll=types.KeyboardButtonPollType(type=types.PollType.QUIZ)))
    await message.answer("Выберите действие:", reply_markup=keyboard)



@dp.errors_handler(exception=BotBlocked)
async def error_bot_blocked(update: types.Update, exception: BotBlocked):
    print(f"Меня заблокировал пользователь!\nСообщение: {update}\nОшибка: {exception}")
    return True


def main():
    executor.start_polling(dp)


if __name__ == '__main__':
    main()
