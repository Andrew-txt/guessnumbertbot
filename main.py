from telebot import TeleBot
import random



TOKEN = "7707549067:AAFlzau4XiwG0XtSUvGBit_82fLhvhChvb8"
bot = TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.send_message(message.chat.id, "This is a Number Guessing Game. Guess a randomly guessed number from 1 to 100 in less than 50 attempts. Click /rules to see rules")

@bot.message_handler(commands=["rules"])
def get_text_messages(message):
    if message.text == "/rules":
        bot.send_message(message.chat.id, "Guess the number in less than 50 attempts. The number can be any from 1 to 100. The bot will answer in two ways: a number less than the proposed one/a number greater than the proposed one. Click /startgame to start the game")
    else:
        bot.send_message(message.chat.id, "Unknown command")

@bot.message_handler(commands=["startgame"])
def start_game(message):
    if message.text == "/startgame":
        bot.send_message(message.chat.id,"The bot guessed a number from 1 to 100")
    else:
        bot.send_message(message.chat.id, "Unknown command")

random_number = str(random.randint(0, 100))

@bot.message_handler(func=lambda message: True)
def game(message):
    user_guess_num = message.text
    if user_guess_num < random_number:
        bot.reply_to(message, "The guessed number is greater!")
    elif user_guess_num > random_number:
        bot.reply_to(message, "The guessed number is less")
    else:
        bot.send_message(message.chat.id, f"You are right, the guessed number is {random_number}")


bot.infinity_polling()