import telebot
import requests
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import BotCommand 

api = '7291100916:AAEkJQic3znSGA1WLQYqoFsjUThzY6dz1a4'
bot = telebot.TeleBot(api)

# Untuk pasang set menu
def set_menu():
    commands = [
        BotCommand('start', 'Mulai boot'),
        BotCommand('help', 'Minta bantuan'),
        BotCommand('keyboard', 'Tampilkan keyboard'),
        BotCommand('logout', 'Keluar akses')
    ]

    bot.set_my_commands(commands)

# Url api coin    
url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=idr'
response = requests.get(url).json()
price_btc = response['bitcoin']['idr']
url_2 = 'https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=idr'
response = requests.get(url_2).json()
price_eth = response['ethereum']['idr']
url_3 = 'https://api.coingecko.com/api/v3/simple/price?ids=binancecoin&vs_currencies=idr'
response = requests.get(url_3).json()
price_bnb = response['binancecoin']['idr']
url_4 = 'https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=idr'
response = requests.get(url_4).json()
price_sol = response['solana']['idr']

# Start 
@bot.message_handler(commands=['start'])
def show_btn(message):
    name_user = message.from_user.first_name
    #Buton inline
    markup = InlineKeyboardMarkup()
    btn_info_btc = InlineKeyboardButton('Harga Bitcoin', callback_data="btc")
    btn_info_eth = InlineKeyboardButton('Harga Ethereum', callback_data="eth")
    btn_info_bnb = InlineKeyboardButton('Harga BNB', callback_data="bnb")
    btn_info_sol = InlineKeyboardButton('Harga Solana', callback_data="sol")

    markup.row(btn_info_btc, btn_info_eth)
    markup.add(btn_info_bnb, btn_info_sol)

    bot.send_message(message.chat.id, f'Hai {name_user}, silahkan pilih COIN yang ingin kamu cek', reply_markup=markup)

# Isi buton inline
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == 'btc':
        msg = f'Harga Bitcoin (BTC) saat ini: Rp{price_btc:,}'
        bot.send_message(call.message.chat.id, msg)
    elif call.data == 'eth':
        msg_u = f'Harga Ethereum (ETH) saat ini: Rp{price_eth:,}'
        bot.send_message(call.message.chat.id, msg_u)
    elif call.data == 'bnb':
        msg_b = f'Harga BNB (BNB) saat ini: Rp{price_bnb:,}'
        bot.send_message(call.message.chat.id, msg_b)
    elif call.data == 'sol':
        msg_c = f'Harga Solana (SOL) saat ini: Rp{price_sol:,}'
        bot.send_message(call.message.chat.id, msg_c)



print('bot running')
#ini fungsi untuk memanggil set menu
set_menu()
bot.infinity_polling()
bot.polling(non_stop=True)


    

