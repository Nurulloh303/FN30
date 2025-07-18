from telebot import TeleBot
from telebot.types import Message
from buttons import menu


TOKEN = "7713683280:AAGPhVKFz-b1qQCdB1cXHDHBjKMY4fon4mo"

bot = TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message: Message):
    chat_id = message.chat.id
    full_name = message.chat.first_name
    bot.send_message(chat_id, f"Assalomu alykum {full_name} hush kelibsiz",
                     reply_markup=menu())

@bot.message_handler(commands=['help'])
def send_help(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id,  "Yordam soramang baribir yordam bermyman!\n"
                               "O'zingiz ozgina boshingizni ishlatib oylang!!!")

if __name__ == "__main__":
    print("Bot ishladi...")
    bot.infinity_polling()