import telebot

bot = telebot.TeleBot("6475104367:AAHOeEgkNSyaQn1DE9V0wVWzO9pPHgzYcN8")
main: telebot.types.Message = None


def keyboard():
    kb = telebot.types.InlineKeyboardMarkup()
    a1 = telebot.types.InlineKeyboardButton(text="1️⃣", callback_data="1")
    a2 = telebot.types.InlineKeyboardButton(text="2️⃣", callback_data="2")
    a3 = telebot.types.InlineKeyboardButton(text="3️⃣", callback_data="3")

    a4 = telebot.types.InlineKeyboardButton(text="4️⃣", callback_data="4")
    a5 = telebot.types.InlineKeyboardButton(text="5️⃣", callback_data="5")
    a6 = telebot.types.InlineKeyboardButton(text="6️⃣", callback_data="6")
    a7 = telebot.types.InlineKeyboardButton(text="7️⃣", callback_data="7")
    a8 = telebot.types.InlineKeyboardButton(text="8️⃣", callback_data="8")
    a9 = telebot.types.InlineKeyboardButton(text="9️⃣", callback_data="9")
    a0 = telebot.types.InlineKeyboardButton(text="0️⃣", callback_data="0")
    aMinus = telebot.types.InlineKeyboardButton(text="➖", callback_data="-")
    aDel = telebot.types.InlineKeyboardButton(text="⬅️", callback_data="del")
    a00 = telebot.types.InlineKeyboardButton(text="0️⃣0️⃣", callback_data="00")
    aPlus = telebot.types.InlineKeyboardButton(text="➕", callback_data="+")
    aRovno = telebot.types.InlineKeyboardButton(text="🟰", callback_data="=")
    aTCHK = telebot.types.InlineKeyboardButton(text=".", callback_data=".")
    aX = telebot.types.InlineKeyboardButton(text="✖️", callback_data="*")
    aDELIT = telebot.types.InlineKeyboardButton(text="➗", callback_data="/")
    aSBROS = telebot.types.InlineKeyboardButton(text="сброс 🔄", callback_data="сброс 🔄")
    kb.add(a1, a2, a3, a4, a5, a6, a7, a8, a9, a0, a00, aDel, aPlus, aMinus, aRovno, aTCHK, aDELIT, aX, aSBROS)
    return kb


@bot.message_handler(content_types=["text"])
def startmsg(msg):
    global main
    if msg.text == "/start":
        kb = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        a1 = telebot.types.KeyboardButton("да")
        a2 = telebot.types.KeyboardButton("нет")
        kb.add(a1, a2)
        bot.send_message(msg.chat.id, 'Привет,готов ли покалькулировать?', reply_markup=kb)
    if msg.text == "да" or msg.text == "Да":
        main = bot.send_message(msg.chat.id, 'Это калькулятор\n→', reply_markup=keyboard())
    if msg.text == "Нет" or msg.text == "нет":
        bot.send_message(msg.chat.id, 'not cool')


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    global main
    main = call.message
    if call.data == "1" or call.data == "2" or call.data == "3" or call.data == "4" or call.data == "5" or \
            call.data == "6" or call.data == "7" or call.data == "8" or call.data == "9" or call.data == "0" or \
            call.data == "*" or call.data == "00" or call.data == "/" or call.data == "-" or call.data == "+":
        bot.edit_message_text(message_id=main.id, chat_id=call.message.chat.id, text=main.text  +call.data)
        bot.edit_message_reply_markup(message_id=main.id, chat_id=call.message.chat.id, reply_markup=keyboard())
    if call.data == "=":
        rez = str(eval(main.text[17:]))
        bot.edit_message_text(message_id=main.id, chat_id=call.message.chat.id, text=main.text + "=" + rez)
        bot.edit_message_reply_markup(message_id=main.id, chat_id=call.message.chat.id, reply_markup=keyboard())
    if call.data == "сброс 🔄":
        bot.edit_message_text(message_id=main.id, chat_id=call.message.chat.id, text="это калькулятор\n→")
        bot.edit_message_reply_markup(message_id=main.id, chat_id=call.message.chat.id, reply_markup=keyboard())
    if call.data == "del":
        bot.edit_message_text(message_id=main.id, chat_id=call.message.chat.id, text=main.text[:-1])
        bot.edit_message_reply_markup(message_id=main.id, chat_id=call.message.chat.id, reply_markup=keyboard())


bot.polling(non_stop=True)
