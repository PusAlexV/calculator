import telebot
bot=telebot.TeleBot("6446063048:AAEi4iugpi_fuU12tBcIlm51WgZvx-dMe9Y")
@bot.message_handler(content_types=["text"])
def povtor(msg):
    if msg.text=="/start":
        kb=telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        a1=telebot.types.KeyboardButton("да")
        a2 = telebot.types.KeyboardButton("нет")
        kb.add(a1,a2)
        bot.send_message(msg.chat.id, 'привет,готов ли поиграть?',reply_markup=kb)
    if msg.text=="да" or msg.text=="Да":
        kb = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        a1 = telebot.types.KeyboardButton("⭕")
        a2 = telebot.types.KeyboardButton("❌")
        kb.add(a1, a2)
        bot.send_message(msg.chat.id, 'за кого ты хочешь поиграть?',reply_markup=kb)
        bot.register_next_step_handler(msg,func)
    if msg.text=="Нет" or msg.text=="нет":
        bot.send_message(msg.chat.id, 'not cool')
def func(msg):
    img=open("1234.jpg","rb")
    kb = telebot.types.InlineKeyboardMarkup()
    a1 = telebot.types.InlineKeyboardButton(text="да",callback_data="1")
    a2 = telebot.types.InlineKeyboardButton(text="о,нет",callback_data="2")
    kb.add(a1, a2)
    bot.send_photo(msg.chat.id,img,caption="wasd",reply_markup=kb)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "1":
        bot.send_message(call.message.chat.id,"xaxa")



























bot.polling(non_stop=True)