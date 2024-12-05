from telebot import *
bot = telebot.TeleBot('7533402681:AAEjXr7PXlw9tIW_6g39D3VQzD_umlw5pZ4')



@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Здравствуй. Я твой помошник по физике и информатике.')
    bot.send_message(message.chat.id, 'Напиши команды fiz или inf и я помогу тебе')           
    
@bot.message_handler(commands=['fiz'])
def fiz(message):
    bot.send_message(message.chat.id, 'Напишите название физической величины которая вам нужна. Например: Мощность, Энергия, Плотность. Для выхода пропишите команду "/exit"')
    bot.register_next_step_handler(message, on_clickFiz)
    
def on_clickFiz(message):
    if message.text == 'Давление':
        bot.send_message(message.chat.id, 'p = F/S')
    elif message.text == 'Мощность':
        bot.send_message(message.chat.id, 'N = A/T')
    elif message.text == 'Плотность':
        bot.send_message(message.chat.id, 'p = p/gh')
        bot.send_message(message.chat.id, 'p = m/V')
    elif message.text == 'Энергия':
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
    bot.send_message(message.chat.id, 'Введите номер задания код которого вам нужен. Для выхода пропишите команду "/exit"')
    bot.register_next_step_handler(message, on_clickInf)
    
def on_clickInf(message):
    if message.text == '2':
        markup = types.InlineKeyboardMarkup()
        btn1= types.InlineKeyboardButton(text='1 тип', callback_data='2.1')
        markup.row(btn1)
        btn2 = types.InlineKeyboardButton(text='2 тип', callback_data='2.2')
        markup.row(btn2)
        bot.reply_to(message, 'выбери нужный тип', reply_markup=markup)
    elif message.text == '5':
        file_path5= 'C:\\Users\\Roblo\\main\\tgBot\\5.txt'
        with open(file_path5, 'r', encoding='utf-8') as file:
            text = file.read()
        bot.send_message(message.chat.id, text)
    elif message.text == '6':
        file_path6= 'C:\\Users\\Roblo\\main\\tgBot\\6.txt'
        with open(file_path6, 'r', encoding='utf-8') as file:
            text = file.read()
        bot.send_message(message.chat.id, text)
    elif message.text == '8':
        markup = types.InlineKeyboardMarkup()
        btn1 =types.InlineKeyboardButton(text='1 тип', callback_data='8.1')
        btn2 = types.InlineKeyboardButton(text='2 тип', callback_data='8.2')
        markup.row(btn1, btn2)
        btn3 = types.InlineKeyboardButton(text='3 тип', callback_data='8.3')
        btn4 = types.InlineKeyboardButton(text='4 тип', callback_data='8.4')
        markup.row(btn3, btn4)
        btn5 = types.InlineKeyboardButton(text='Теория по заданию', callback_data='teor8')
        markup.row(btn5)
        bot.reply_to(message, 'выбери нужный тип', reply_markup=markup)
    elif message.text == '/python':
        bot.send_message(message.chat.id, 'https://t.me/sofaavibe/1861')
    else:
        bot.send_message(message.chat.id, 'Данное задание еще не было добавлено или его нет в экзамене')
    if message.text != '/exit':
        bot.register_next_step_handler(message, on_clickInf)




@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'E = mv**2/2':
        bot.send_message(callback.message.chat.id, 'E = mv**2/2')
    if callback.data == 'E = mgh':
        bot.send_message(callback.message.chat.id, 'E = mgh')
    if callback.data == '2.1':
        file_path2 = 'C:\\Users\\Roblo\\main\\tgBot\\2.1.txt'
        with open(file_path2, 'r', encoding='utf-8') as file:
            text = file.read()
        bot.send_message(callback.message.chat.id, text)
    if callback.data == '2.2':
        file_path2 = 'C:\\Users\\Roblo\\main\\tgBot\\2.2.txt'
        with open(file_path2, 'r', encoding='utf-8') as file:
            text = file.read()
        bot.send_message(callback.message.chat.id, text)
    if callback.data == '8.1':
        file_path8 = 'C:\\Users\\Roblo\\main\\tgBot\\8.1.txt'
        with open(file_path8, 'r', encoding='utf-8') as file:
            text = file.read()
        bot.send_message(callback.message.chat.id, text)
    if callback.data == '8.2':
        file_path8 = 'C:\\Users\\Roblo\\main\\tgBot\\8.2.txt'
        with open(file_path8, 'r', encoding='utf-8') as file:
            text = file.read()
        bot.send_message(callback.message.chat.id, text)
    if callback.data == '8.3':
        file_path8 = 'C:\\Users\\Roblo\\main\\tgBot\\8.3.txt'
        with open(file_path8, 'r', encoding='utf-8') as file:
            text = file.read()
        bot.send_message(callback.message.chat.id, text)
    if callback.data == '8.4':
        file_path8 = 'C:\\Users\\Roblo\\main\\tgBot\\8.4.txt'
        with open(file_path8, 'r', encoding='utf-8') as file:
            text = file.read()
        bot.send_message(callback.message.chat.id, text)
    if callback.data == 'teor8':
        file_1 = open('C:\\Users\\Roblo\\main\\tgBot\\teor8_1.jpg', 'rb')
        bot.send_photo(callback.message.chat.id, file_1)
        file_2 = open('C:\\Users\\Roblo\\main\\tgBot\\teor8_2.jpg', 'rb')
        bot.send_photo(callback.message.chat.id, file_2)
        file_3 = open('C:\\Users\\Roblo\\main\\tgBot\\teor8_3.jpg', 'rb')
        bot.send_photo(callback.message.chat.id, file_3)
        file_4 = open('C:\\Users\\Roblo\\main\\tgBot\\teor8_4.jpg', 'rb')
        bot.send_photo(callback.message.chat.id, file_4)
    
        
        
        

bot.infinity_polling()
