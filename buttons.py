from telebot.types import ReplyKeyboardMarkup, KeyboardButton

def menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = KeyboardButton("Fantastik kinolar")
    btn2 = KeyboardButton("Komediya kinolar")
    btn3 = KeyboardButton("Drama kinolar")
    btn4 = KeyboardButton("Triler kinolar")
    btn5 = KeyboardButton("Dedektiv kinolar")
    markup.add(btn1, btn2, btn3, btn4, btn5)
    return markup