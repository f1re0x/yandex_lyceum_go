from telebot import *
bot = telebot.TeleBot('7533402681:AAEjXr7PXlw9tIW_6g39D3VQzD_umlw5pZ4')



@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Здравствуй. Я твой помошник по физике и информатике.')
    bot.send_message(message.chat.id, 'Напиши команды fiz или inf и я помогу тебе')           
    
@bot.message_handler(commands=['fiz'])
def fiz(message):
    bot.send_message(message.chat.id, 'Напишите название физической величины которая вам нужна. Например: Мощность, Энергия, Плотность')
    bot.register_next_step_handler(message, on_clickFiz)
    
def on_clickFiz(message):
    if message.text == 'Давление':
        bot.send_message(message.chat.id, 'p = F/S')
    if message.text == 'Мощность':
        bot.send_message(message.chat.id, 'N = A/T')
    if message.text == 'Плотность':
        bot.send_message(message.chat.id, 'p = p/gh')
        bot.send_message(message.chat.id, 'p = m/V')
    if message.text == 'Энергия':
        markup = types.InlineKeyboardMarkup()
        btn1= types.InlineKeyboardButton(text='Кинетическая', callback_data='E = mv**2/2')
        markup.row(btn1)
        btn2= types.InlineKeyboardButton(text='Потенциальная', callback_data='E = mgh')
        markup.row(btn2)
        bot.reply_to(message, 'выбери нужную', reply_markup=markup)
    if message.text != '/exit':
        bot.register_next_step_handler(message, on_clickFiz)
        
        
        
              

@bot.message_handler(commands=['inf'])
def inf(message):
    bot.send_message(message.chat.id, 'Введите номер задания код которого вам нужен')
    bot.register_next_step_handler(message, on_clickInf)
    
def on_clickInf(message):
    if message.text == '2':
        markup = types.InlineKeyboardMarkup()
        btn1= types.InlineKeyboardButton(text='1 тип', callback_data='1 тип')
        markup.row(btn1)
        btn2 = types.InlineKeyboardButton(text='2 тип', callback_data='2 тип')
        markup.row(btn2)
        bot.reply_to(message, 'выбери нужный тип', reply_markup=markup)
        
    if message.text == '5':
        file_path5= 'C:\\Users\\Roblo\\main\\tgBot\\5.txt'
        with open(file_path5, 'r', encoding='utf-8') as file:
            text = file.read()
        bot.send_message(message.chat.id, text)
    if message.text == '6':
        file_path6= 'C:\\Users\\Roblo\\main\\tgBot\\6.txt'
        with open(file_path6, 'r', encoding='utf-8') as file:
            text = file.read()
        bot.send_message(message.chat.id, text)
    if message.text != '/exit':
        bot.register_next_step_handler(message, on_clickInf)
    




@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'E = mv**2/2':
        bot.send_message(callback.message.chat.id, 'E = mv**2/2')
    if callback.data == 'E = mgh':
        bot.send_message(callback.message.chat.id, 'E = mgh')
    if callback.data == '1 тип':
        file_path2 = 'C:\\Users\\Roblo\\main\\tgBot\\2.1.txt'
        with open(file_path2, 'r', encoding='utf-8') as file:
            text = file.read()
        bot.send_message(callback.message.chat.id, text)
    if callback.data == '2 тип':
        file_path2 = 'C:\\Users\\Roblo\\main\\tgBot\\2.2.txt'
        with open(file_path2, 'r', encoding='utf-8') as file:
            text = file.read()
        bot.send_message(callback.message.chat.id, text)

bot.infinity_polling()
