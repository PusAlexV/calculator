import telebot
bot=telebot.TeleBot("6446063048:AAEi4iugpi_fuU12tBcIlm51WgZvx-dMe9Y")
@bot.message_handler(content_types=["text"])
def povtor(msg):
    if msg.text=="Не повторяй":
        bot.send_message(msg.chat.id,'ха,размечтался')
    else:
        bot.send_message(msg.chat.id,msg.text)
bot.polling(non_stop=True)
#делает бота цикличным