from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

mainMenu = ReplyKeyboardMarkup(resize_keyboard= True)
btnProfile =KeyboardButton("Профиль")
mainMenu.add(btnProfile)