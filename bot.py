bot_token = "6111223991:AAHoyWXCFG_NrCtV8KtSGrkFgA9jnVvecig"

import requests
import telebot
from googletrans import Translator

bot = telebot.TeleBot(bot_token)






@bot.message_handler(commands=["start"])
def start_function(message):
    bot.reply_to(message, "Hello! I'm a chatbot that will tell jokes) write word Joke to start" )

@bot.message_handler(func=lambda msg:True)
def repeat(message):
    if message.text == "Reapet":
        bot.reply_to(message, message.text)
    if message.text == "Hello" or "Hi":
        text = "Hi, how are you"
        sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
        bot.register_next_step_handler(sent_msg, react_on_message)
    if message.text == "Joke":
        text = "Okey) Then say Let's go"
        sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
        bot.register_next_step_handler(sent_msg, react_on_message)

@bot.message_handler(content_types="text")
def react_on_message(message):
    if message.text == "Let's go":
            
        url = "https://dad-jokes7.p.rapidapi.com/dad-jokes/random"

        headers = {
            "X-RapidAPI-Key": "a67b36fb9dmsh834e757535157a9p1585a0jsne23cba86f827",
            "X-RapidAPI-Host": "dad-jokes7.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers)
        
        
        
        bot.reply_to(message, response.json()["joke"])

        
        
    if message.text == "Nice":
        bot.reply_to(message, "It's good!")
    if message.text == "Can be better":
        bot.reply_to(message, "After joke you will feel better)")
    if message.text == "Bad":
        bot.reply_to(message, "Hmm, Maybe ypo want a joke?")    





bot.infinity_polling()
