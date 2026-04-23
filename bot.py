import telebot

# Bilkul sahi token quotes ke saath
TOKEN = "8506734114:AAHworAWrVu-aUVnso0qVsva91bn14y9ohw"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Assalam-o-Alaikum! Ds5 Virus 🦠 Online Ho Gaya Hai. Kya Hukum Hai Mere Aaqa?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Virus Processing... ⚙️")

print("Bot is starting...")
bot.infinity_polling()
