import telebot
from telebot import types
bot = telebot.TeleBot('5403302391:AAEluQEA_KoZN-WD4J-NYzwVDvbs4S4Gcmo')
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'Привет меня зовут Ирвин младший! И я буду очень рад с вами познакомиться! Что бы узнать список команд напишите /help')
@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id,'Вот что я могу : 1) /vk')
@bot.message_handler(commands=['vk'])
def vk(message):
    bot.send_message(message.chat.id,'Vk - моего повелителя! https://vk.com/id496842355' )


bot.polling(none_stop=True)
