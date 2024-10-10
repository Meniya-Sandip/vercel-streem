from flask import Flask, send_file
from pyrogram import Client
import os

app = Flask(__name__)
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Client("my_bot",
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN)

@app.route("/download/<file_id>")
def download(file_id):
    with bot:
        file_path = bot.download_media(file_id)
        return send_file(file_path, as_attachment=True)

if __name__ == "__main__":
    app.run()
