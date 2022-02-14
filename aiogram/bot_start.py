from aiogram import Bot, Dispatcher, executor, types
from config import API_TOKEN

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


# @dp.message_handler(commands='start')
# def start(message: types.Message):
#     start_buttons = ['🔪 Ножи', '🥊 Перчатки', '🔫 Снайперские винтовки']
#     keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     keyboard.add(*start_buttons)
#     message.reply("Hello world!")


# @dp.message_handler(commands=['start'])
# async def send_welcome(message: types.Message):
#     start_buttons = ['🔪 Ножи', '🥊 Перчатки', '🔫 Снайперские винтовки']
#     await message.reply("Hello world!")

@dp.message_handler(commands=['hi1'])
async def process_hi1_command(message: types.Message):
    await message.reply("Первое - изменяем размер клавиатуры", reply_markup=kb.greet_kb1)

# @dp.message_handler(commands=['help'])
# async def send_welcome(message: types.Message):
#     await message.reply("Чем я могу помочь?")
#
#
# @dp.message_handler()
# async def echo(message: types.Message):
#     await message.answer(message.text)
#

if __name__ == '__main__':
    executor.start_polling(dp)
# skip_updates=True
