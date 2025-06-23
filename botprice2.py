import telebot #Untuk import telebot
import requests # UNtuk import api cooin
from telebot.types import ReplyKeyboardMarkup, KeyboardButton # Untuk keyboard buton
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton # Untuk inline buton
import json # untuk import .json data user
import os # untuk mengimpor modul os, yaitu modul standar yang menyediakan fungsi-fungsi untuk berinteraksi dengan sistem operasi (Operating System).
from datetime import datetime # Import tanggal dan waktu
from telebot.types import BotCommand # Import commands 
from config import API_TOKEN

bot = telebot.TeleBot(API_TOKEN)

# Untuk pasang set menu
def set_menu():
    commands = [
        BotCommand('start', 'Mulai bot'),
        BotCommand('help', 'Minta bantuan'),
    ]

    bot.set_my_commands(commands)

#DATA API UNTUK HARGA COIN
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

# file yang digunakan untuk menyimpan data user
data_file = 'akses_terverifikasi.json'

# Inis akan membuat file jika belum ada
if not os.path.exists(data_file):
    with open(data_file, 'w') as f:
        json.dump([], f)
def simpan_user_ke_file(user):
    with open(data_file, 'r') as f:
        data = json.load(f)

    # Cek apakah user sudah ada
    sudah_terdaftar = any(u['id'] == user.id for u in data)
    if not sudah_terdaftar:
        data.append({
            'id': user.id,
            'nama': user.first_name,
            'username': user.username,
            'waktu_akses': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

        with open(data_file, 'w') as f:
            json.dump(data, f, indent=2)


allowed_users = set()  # Set user_id yang sudah lolos verifikasi
password = 'masuk12345'  # Ganti sesuai kebutuhan

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.from_user.id
    if user_id in allowed_users:
        bot.send_message(message.chat.id, f'Hallo {message.from_user.first_name}, selamat datang kembali')
    else:
        bot.send_message(message.chat.id, 'Silahkan masukkan pasword...')

@bot.message_handler(func=lambda message: message.text == password)
def handle_password(message):
    user_id = message.from_user.id
    allowed_users.add(user_id)

    
 # Simpan data ke file
    simpan_user_ke_file(message.from_user)

    markup = InlineKeyboardMarkup()
    btn_menu = InlineKeyboardButton('KLIK DISINI!', callback_data='open_keyboard')
    markup.add(btn_menu)

    bot.send_message(
        message.chat.id,
        f"Akses diterima, selamat datang {message.from_user.first_name}! Klik tombol di bawah untuk mulai.",
        reply_markup=markup)


#BUTON UNTUK KEYBOARD REPLY
@bot.callback_query_handler(func=lambda call: call.data == "open_keyboard")
def open_keyboard(call):
    user_id = call.from_user.id
    if user_id not in allowed_users:
        bot.send_message(call.message.chat.id, "Kamu belum punya akses.")
        return

    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn_1 = KeyboardButton('Bitcoin')
    btn_2 = KeyboardButton('Ethereum')
    btn_3 = KeyboardButton('BNB')
    btn_4 = KeyboardButton('Solana')

    markup.row(btn_1, btn_2, btn_3, btn_4)
    bot.send_message(call.message.chat.id, "Silahkan pilih coin: ", reply_markup=markup)

#HASIL DARI BUTON
@bot.message_handler(func=lambda message: message.text == 'Bitcoin')
def reply_btc(message):
    nama = message.from_user.first_name + message.from_user.last_name
    bot.reply_to(message, f'Hai {nama}, harga Bitcoin saat ini: Rp {price_btc:,}')

@bot.message_handler(func=lambda message: message.text == 'Ethereum')
def reply_btc(message):
    nama = message.from_user.first_name + message.from_user.last_name
    bot.reply_to(message, f'Hai {nama}, harga Ethereum saat ini: Rp {price_eth:,}')

@bot.message_handler(func=lambda message: message.text == 'BNB')
def reply_btc(message):
    nama = message.from_user.first_name + message.from_user.last_name
    bot.reply_to(message, f'Hai {nama}, harga BNB saat ini: Rp {price_bnb:,}')

@bot.message_handler(func=lambda message: message.text == 'Solana')
def reply_btc(message):
    nama = message.from_user.first_name + message.from_user.last_name
    bot.reply_to(message, f'Hai {nama}, harga Solana saat ini: Rp {price_sol:,}')

@bot.message_handler(commands=['help'])
def bantuan(message):
    bot.reply_to(message, 'ada yang bisa dibantu')

print('bot running')
#ini fungsi untuk memanggil set menu
set_menu()
bot.infinity_polling()
bot.polling(non_stop=True)