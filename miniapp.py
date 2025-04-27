
from aiogram import Bot, Dispatcher, executor,types
from aiogram.types.web_app_info import WebAppInfo
import asyncio

bot = Bot('7287516356:AAETk5S79EUm3YZtATXmMm6csGxhxJg3CFo')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Открыть веб страницу', web_app=WebAppInfo(url='https://github.com/Loorencho/telegram_bot.git')))
    await message.answer('Привет мой друг', reply_markup=markup)

executor.start_polling(dp)







