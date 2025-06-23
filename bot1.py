import telebot

api = '7288179247:AAHGf5oCQUtJAnRUiOitZFogGj682Vl6s7c'
bot = telebot.TeleBot(api)

@bot.message_handler(commands=['start'])
def action_start(message):
    nama = message.from_user.first_name
    nama_akhir = message.from_user.last_name
    bot.reply_to(message, 'hallo apa kabar {} {} ?'. format(nama, nama_akhir))

@bot.message_handler(commands=['id'])
def send_welcome(message):
    nomer_id = message.from_user.id
    nama = message.from_user.first_name
    nama_akhir = message.from_user.last_name
    bot.reply_to(message, '''
Hi, id kamu adalah :
ID = {}
Nama = {} {}
        '''.format(nomer_id, nama, nama_akhir))




@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, 'ada yang bisa dibantu')

print('bot start')
bot.polling()