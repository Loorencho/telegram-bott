from pickletools import bytes1

import telebot
import webbrowser
import sqlite3
from telebot import types
bot = telebot.TeleBot('7287516356:AAETk5S79EUm3YZtATXmMm6csGxhxJg3CFo')

@bot.message_handler(commands=['start'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    but1 = (types.InlineKeyboardButton('Перейти на сайт:', url='https://web.telegram.org/'))
    markup.row(but1)
    but2 = (types.InlineKeyboardButton('Удалить объект', callback_data='delete'))
    but3 =  (types.InlineKeyboardButton('Изменить текст', callback_data='edit'))
    markup.row(but2, but3)
    bot.reply_to(message, 'Hello', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)

def on_click(message):
    if message.text == 'Перейти на сайт':
        bot.send_message(message.chat.id, 'Website is open')
    elif message.text == 'Удалить фото':
        bot.send_message(message.chat.id, 'Deleted')



@bot.message_handler(commands=['website'])
def site(message):
    webbrowser.open('https://web.telegram.org/')

@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, 'Help information! This bot made like a test version, working start gonna be soon!!!')

@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Hi,{message.from_user.first_name}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')


bot.message_handler(commands=['base'])
def start(message):
    conn = sqlite3.connect('database.sql')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, name varchar(50),pass varchar(50)')
    conn.commit()
    cur.close()

    bot.send_message(message.chat.id, 'Registration')
    bot.register_next_step_handler(message, user_name)

def user_name(message):
    pass


bot.polling(non_stop=True)