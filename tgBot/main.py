import telebot
from telebot import types
bot = telebot.TeleBot('7533402681:AAEjXr7PXlw9tIW_6g39D3VQzD_umlw5pZ4')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Перейти на сайт')
    btn2 = types.KeyboardButton('Удалить фото')
    markup.row(btn1, btn2)
    bot.send_message(message.chat.id, 'Привет', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)
    
def on_click(message):
    if message.text == 'Перейти на сайт':
        bot.send_message(message.chat.id, 'Website is open!')
    elif message.text == 'Удалить фото':
        bot.send_message(message.chat.id, 'delited!')

    
    
@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Перейти на сайт', url='https://pypi.org/project/pyTelegramBotAPI/' ))
    bot.reply_to(message, 'Какое красивое фото', reply_markup=markup)


bot.infinity_polling()