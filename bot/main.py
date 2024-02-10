from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types.web_app_info import WebAppInfo
from db import Database
import markups as nav
import config as cfg

bot = Bot('6816226713:AAFlwqnsck6uYlVtcNQ1ugSYsi-BvYaaDfU')
dp = Dispatcher(bot)
db = Database('proton.db')

game_list = InlineKeyboardMarkup(row_width=2)
game_list.add(InlineKeyboardButton(text='Запустить игру', web_app=WebAppInfo(url='https://artyommedved.github.io/ProtonClick.github.io/')))

@dp.message_handler(commands=['start'])
async def cmd_random(message: types.Message):
    if not db.user_exists(message.from_user.id):
        start_command = message.text
        referrer_id = str(start_command[7:])
        if str(referrer_id) != "":
            if str(referrer_id) != str(message.from_user.id):
                db.add_user(message.from_user.id, referrer_id)
                try:
                    await bot.send_message(referrer_id, "По вашей ссылке зарегестрировался новый пользователь!")

                except:
                    pass
            else:
                db.add_user(message.from_user.id)
                await bot.send_message(message.from_user.id, "Нельзя регистрироваться по собственной реферальной ссылке!")
        else: 
            db.add_user(message.from_user.id)
    await bot.send_message(message.from_user.id, "👋 Привет, чтобы перейти в кликер, нажми на кнопку внизу 👇", reply_markup=game_list)


@dp.message_handler(commands=['profile'])
async def bot_message(message: types.Message):
        await bot.send_message(message.from_user.id, f"ID: {message.from_user.id}\nhttps://t.me/{cfg.BOTNICKNAME}?start={message.from_user.id}\nКол-во рефералов: {db.count_referals(message.from_user.id)}")
    


    
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)