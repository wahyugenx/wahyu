import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

api = '8166341118:AAEWYT2J5rdP9UvH3RFjc37MLHNLWom2_RA'
bot = telebot.TeleBot(api)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'hello')

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, 'ada yang bisa dibantu?')

@bot.message_handler(commands=['hello'])
def send_helloback(message):
    bot.reply_to(message, f'Hallo, apakabar {message.from_user.first_name}')

# INI UNTUK MENAMBAHKAN TOMBOL
@bot.message_handler(commands=['menu'])
def show_menu(message):
    markup = InlineKeyboardMarkup()

    btn_info = InlineKeyboardButton('Info', callback_data="Info")
    btn_link = InlineKeyboardButton('Web Resmi', url="https://www.youtube.com/")
    btn_hello = InlineKeyboardButton('Help', callback_data="help")


    markup.row(btn_info, btn_link)
    markup.add(btn_hello)

    bot.send_message(message.chat.id, 'Silahkan pilih menu dibawah ini', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == 'Info':
        user = call.from_user
        msg = f'Nama kamu: {user.first_name} \n ID: {user.id}'
        bot.send_message(call.message.chat.id, msg)
    elif call.data == 'help':
        user = call.from_user
        msg_u = f'Apa yang bisa kita bantu? mrs/ms {user.first_name}'
        bot.send_message(call.message.chat.id, msg_u)
        
print('bot running')
bot.polling(non_stop=True)