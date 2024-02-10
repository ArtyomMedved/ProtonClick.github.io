from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types.web_app_info import WebAppInfo

bot = Bot('6816226713:AAFlwqnsck6uYlVtcNQ1ugSYsi-BvYaaDfU')
dp = Dispatcher(bot)

game_list = InlineKeyboardMarkup(row_width=2)
game_list.add(InlineKeyboardButton(text='Запустить игру', web_app=WebAppInfo(url='https://artyommedved.github.io/ProtonClicker.github.io/')))

@dp.message_handler(commands=['start'])
async def cmd_random(message: types.Message):
    await message.answer('👋 Привет, чтобы перейти в кликер, нажми на кнопку внизу 👇', reply_markup=game_list)


    

executor.start_polling(dp)