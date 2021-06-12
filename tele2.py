import telebot
from telebot import types
token = '1817706851:AAHpT8_tRKwVQy9fVY4hWddP4sASm_G1nYI'

bot = telebot.TeleBot(token)
@bot.message_handler(content_types=['text'])

def get_text_messages(message):

   if message.text == "Hi":

       bot.send_message(message.from_user.id,"Hi darling.How can i help you?")

   elif message.text == "/help":

       bot.send_message(message.from_user.id, "Say hi")
   elif message.text == "Would you like to be my friend?":

       bot.send_message(message.from_user.id, "Yep! We can be good friends!")
   elif message.text == "Say something funny":

       bot.send_message(message.from_user.id, "After Tuesday,even the calendar says WTF")
   elif message.text == "I'm sad. What should I do?":

       bot.send_message(message.from_user.id, "You have to rest well after a cup of milk,coffee or tea")
   elif message.text == "Say something funny again":

       bot.send_message(message.from_user.id, "If you think no one cares if you're dead or alive miss a couple of credit card payments.")

   else:

       bot.send_message(message.from_user.id, "i dont understand you,write /help.")


bot.polling(none_stop=True, interval=0)