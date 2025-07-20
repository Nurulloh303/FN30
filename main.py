from telebot import TeleBot
from telebot.types import Message
from buttons import menu
from database import Database

TOKEN = "7713683280:AAGPhVKFz-b1qQCdB1cXHDHBjKMY4fon4mo"

bot = TeleBot(TOKEN)
db = Database()

@bot.message_handler(commands=['start'])
def send_welcome(message: Message):
    chat_id = message.chat.id
    full_name = message.chat.first_name
    bot.send_message(chat_id, f"Assalomu alykum {full_name} hush kelibsiz",
                     reply_markup=menu())

# -------------------------------------------------------

db.insert_category("Fantastik kinolar")
db.insert_category("Komediya kinolar")
db.insert_category("Drama kinolar")
db.insert_category("Triler kinolar")
db.insert_category("Dedektiv kinolar")

# Fantastik kinolar
db.insert_film("Interstellar", "Space-time travel to save humanity.", 1)
db.insert_film("Inception", "Dream within a dream thriller.", 1)

# Komediya kinolar
db.insert_film("The Hangover", "Friends try to remember last night.", 2)
db.insert_film("Mr. Bean's Holiday", "Bean's chaotic French vacation.", 2)

# Drama kinolar
db.insert_film("The Pursuit of Happyness", "A true story of perseverance.", 3)

# Triler kinolar
db.insert_film("Shutter Island", "Psychological mystery on an island.", 4)

# Dedektiv kinolar
db.insert_film("Sherlock Holmes", "A detective solves a dark mystery.", 5)




@bot.message_handler(func=lambda message: True)
def handle_category(message):
    category_name = message.text
    categories = db.get_categories()

    category_id = None
    for cat in categories:
        if cat[1] == category_name:
            category_id = cat[0]
            break

    if category_id:
        films = db.get_films_by_category(category_id)
        if films:
            response = f"🎬 *{category_name}*:\n\n"
            for film in films:
                response += f"🎞 *{film[0]}*\n📖 {film[1]}\n\n"
            bot.send_message(message.chat.id, response, parse_mode='Markdown')
        else:
            bot.send_message(message.chat.id, "Bu kategoriyada hali kinolar mavjud emas.")
    else:
        bot.send_message(message.chat.id, "Iltimos, menyudagi tugmalardan birini tanlang.")


# -------------------------------------------------------


@bot.message_handler(commands=['help'])
def send_help(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id,  "Yordam soramang baribir yordam bermyman!\n"
                               "O'zingiz ozgina boshingizni ishlatib oylang!!!")

if __name__ == "__main__":
    print("Bot ishladi...")
    bot.infinity_polling()