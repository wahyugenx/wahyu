import telebot
import schedule
import threading
import time
import requests

bot = telebot.TeleBot('7512494017:AAEcB5KtJr2UoJLDzL4tjlLXahQ3Gp4p25w')
id_chat = 7556764974

def kirim_harga_btc():
    try:
        url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=idr'
        response = requests.get(url).json()
        price_btc = response['bitcoin']['idr']
        msg = f'Harga *Bitcoin (BTC)* saat ini: Rp{price_btc:,}'
        bot.send_message(id_chat, msg, parse_mode='Markdown')
    except Exception as e:
        bot.send_message(id_chat, f'Gagal ambil harga BTC: {e}')

#schedule.every().day.at("07:00").do(kirim_harga_btc)
#schedule.every().day.at("19:00").do(kirim_harga_btc)

schedule.every(10).seconds.do(kirim_harga_btc)  # Untuk testing


def run_schedule():
    while True:
        schedule.run_pending()
        time.sleep(1)

# Start thread
t = threading.Thread(target=run_schedule)
t.start()

print('bot runing...')
bot.infinity_polling()
bot.polling(non_stop=True)