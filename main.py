from pyrogram import Client
from pytgcalls import PyTgCalls

api_id = 38384933
api_hash = "30766cdba599e79b19d8d6ba78b328d"
bot_token = 8528188755:AAHo-bop-rp-Tknkf1QH176otJR-t0Eur6I

app = Client("MusicBot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)
call = PyTgCalls(app)

@app.on_message()
def start(client, message):
    message.reply_text("🎶 البوت شغال بنجاح!")

app.start()
print("✅ Bot is running...")
app.idle()
