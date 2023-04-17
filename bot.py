import json
import requests
import telebot
from config import token, keys
from extensions import APIException, Converter

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    bot.send_message(message.chat.id, "To use the bot, enter the name of the currency you want to convert, "
                                      "the name of the currency you want to convert to, and the amount of the first "
                                      "currency in the following format: \n<from currency> <to currency> <amount>")
    bot.send_message(message.chat.id, "For example: \nUSD EUR 100 \nThis will convert 100 US dollars to euros.")

@bot.message_handler(commands=['values'])
def handle_values(message):
    text = "Available currencies:\n"
    for currency in Converter.currencies:
        text += currency + '\n'
    bot.send_message(message.chat.id, text)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        base, quote, amount = message.text.split()
        result = Converter.get_price(base.upper(), quote.upper(), float(amount))
    except APIException as e:
        bot.send_message(message.chat.id, f"Error: {e}")
    except Exception as e:
        bot.send_message(message.chat.id, "Error: Invalid input.")
    else:
        bot.send_message(message.chat.id, f"{amount} {base.upper()} is worth {result} {quote.upper()}")

bot.polling()
