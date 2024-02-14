import telebot
from telebot import types




bot = telebot.TeleBot('6094605573:AAGchPWrj-a3D09NYUZn37nZp6pJcGsKbto')




@bot.message_handler(commands=['ser', 'start', 'help', 'infoforthisbot','secret'])
def reply(message):
    if message.text == '/start':
        bot.reply_to(message, 'hi i have this command(/ser,/infoforthisbot,/help)')
    if message.text == '/help':
        bot.reply_to(message, 'report the problem to this number +380 67 631 45 74 or telegram https://t.me/Mykitauadack')
    if message.text == '/infoforthisbot':
        bot.reply_to(message, 'this bot will show information about a vacation trip')
    if message.text == '/secret':
        bot.reply_to(message, 'Завдання:ПУТЕШЕСТВЕННИК. Программа, которая поможет выбрать направление для отпуска. Основываясь на бюджете, наличию визы и желаниям пользователя.')
    keyboard = types.InlineKeyboardMarkup()
    if message.text == '/ser':
       btn11 = types.InlineKeyboardButton('7днів', callback_data='123')
       btn12 = types.InlineKeyboardButton('14днів', callback_data='312')
       keyboard.add(btn11, btn12 )
       bot.send_message(message.from_user.id, 'Впишіть кількість днів у відпусці', reply_markup=keyboard)
@bot.callback_query_handler(func=lambda a:True)
def serer(call):
    keyboard = types.InlineKeyboardMarkup()
    btn121 = types.InlineKeyboardButton('1000dollar-1500dollar', callback_data='234')
    btn1212 = types.InlineKeyboardButton('1501dollar-2000dollar', callback_data='432')
    btn213 = types.InlineKeyboardButton('2001dollar-3000dollar', callback_data='1234')
    keyboard.add(btn121, btn1212, btn213)
    if call.data=='123' :
        bot.send_message(call.message.chat.id, 'Виберить грошовий обсяг', reply_markup=keyboard)
    keyboard1 = types.InlineKeyboardMarkup()
    if call.data=='234' :
        btn111 = types.InlineKeyboardButton('Беларусь',url = 'https://www.skyscanner.ru/news/deshevye-strany-dlia-puteshestvii#belarus')
        btn1112 = types.InlineKeyboardButton('Армения',url = 'https://www.skyscanner.ru/news/deshevye-strany-dlia-puteshestvii#armenia')
        btn1113 = types.InlineKeyboardButton('Abhazia',url = 'https://www.skyscanner.ru/news/deshevye-strany-dlia-puteshestvii#abkhazia')
        keyboard1.add(btn111, btn1112, btn1113)
        bot.send_message(call.message.chat.id, 'Вибери країну на 7 днів за обсягом 1000dollar-1500dollar ', reply_markup=keyboard1)
    keyboard2 = types.InlineKeyboardMarkup()
    if call.data=='432' :
        btn11 = types.InlineKeyboardButton('Турция',url = 'https://www.skyscanner.ru/news/deshevye-strany-dlia-puteshestvii#turkey')
        btn112 = types.InlineKeyboardButton('Индия',url = 'https://www.skyscanner.ru/news/deshevye-strany-dlia-puteshestvii#india')
        btn113 = types.InlineKeyboardButton('Казахстан',url = 'https://www.skyscanner.ru/news/deshevye-strany-dlia-puteshestvii#kazakhstan')
        btn114 = types.InlineKeyboardButton('Албания',url = 'https://www.skyscanner.ru/news/deshevye-strany-dlia-puteshestvii#albania')
        btn115 = types.InlineKeyboardButton('Сербия',url = 'https://www.skyscanner.ru/news/deshevye-strany-dlia-puteshestvii#serbia')
        btn116= types.InlineKeyboardButton('Болгария',url = 'https://www.skyscanner.ru/news/deshevye-strany-dlia-puteshestvii#bulgaria')
        btn117 = types.InlineKeyboardButton('Марокко',url = 'https://www.skyscanner.ru/news/deshevye-strany-dlia-puteshestvii#morocco')
        btn118 = types.InlineKeyboardButton('Черногория',url = 'https://www.skyscanner.ru/news/deshevye-strany-dlia-puteshestvii#montenegro')
        keyboard2.add(btn11, btn112, btn113, btn114, btn115, btn116, btn117, btn118)
        bot.send_message(call.message.chat.id, 'Вибери країну на 7 днів за обсягом 1501dollar-2000dollar ', reply_markup=keyboard2)
    keyboard3 = types.InlineKeyboardMarkup()
    if call.data=='1234' :
        btn131 = types.InlineKeyboardButton('Шри-Ланка',url = 'https://www.skyscanner.ru/news/deshevye-strany-dlia-puteshestvii#sri-lanka')
        btn1132 = types.InlineKeyboardButton('Танзания',url = 'https://www.skyscanner.ru/news/deshevye-strany-dlia-puteshestvii#tanzania')
        keyboard3.add(btn131, btn1132)
        bot.send_message(call.message.chat.id, 'Вибери країну на 7 днів за обсягом 2001dollar-3000dollar ', reply_markup=keyboard3)
    keyboard1 = types.InlineKeyboardMarkup()
    if call.data == '312':
        btn1111 = types.InlineKeyboardButton('Turtsiya info',url='https://www.how2go.info/category/turtsiya/')
        btn11112 = types.InlineKeyboardButton('Egypt info',url='https://www.how2go.info/category/egipet/')
        btn111133 = types.InlineKeyboardButton('Frence info',url='https://www.how2go.info/category/frantsiya/')
        btn111134 = types.InlineKeyboardButton('Itali info', url='https://www.how2go.info/category/italiya/')
        btn11113 = types.InlineKeyboardButton('Spain info', url='https://www.how2go.info/category/ispaniya/')
        keyboard1.add(btn1111, btn11112, btn11113,btn111133,btn111134)
        bot.send_message(call.message.chat.id, 'Вибери країну на 14 днів', reply_markup=keyboard1)



bot.infinity_polling()