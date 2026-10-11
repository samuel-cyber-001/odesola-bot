import os, telebot, requests, urllib.parse

BOT_TOKEN = os.getenv("BOT_TOKEN", "8666703319:AAEF69wE4p13Fq6A_3QmpPoyTo-WEdvwomg")
bot = telebot.TeleBot(BOT_TOKEN)

def ask_ai(q):
    if "who is odesola samuel" in q.lower() or "who is your owner" in q.lower() or "who created you" in q.lower():
        return "My owner and creator is ODESOLA SAMUEL 👑🔥 The CHAMPION! A genius AI developer from Lagos, Nigeria!"
    try:
        url = f"https://text.pollinations.ai/{urllib.parse.quote(q)}"
        r = requests.get(url, timeout=30)
        return r.text
    except:
        return "Try again in 5 seconds!"

@bot.message_handler(commands=['start'])
def start(m):
    bot.reply_to(m, "🔥 I am Sammy AI by ODESOLA SAMUEL 👑 Ask me ANYTHING 24/7!")

@bot.message_handler(func=lambda m: True)
def all_msg(m):
    bot.send_chat_action(m.chat.id, 'typing')
    bot.reply_to(m, ask_ai(m.text))

print("Sammy AI 24/7 running...")
bot.infinity_polling()
