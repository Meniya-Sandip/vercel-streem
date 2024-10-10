from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import os

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Client("my_bot",
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN)

@bot.on_message(filters.command("start"))
async def start(client, message):
    await message.reply("Hello! Upload a file to get a download link.")

@bot.on_message(filters.document)
async def handle_document(client, message):
    file = message.document
    file_path = await client.download_media(file)
    link = f"https://{os.getenv('VERCEL_APP_NAME')}.vercel.app/download/{file.file_id}"
    await message.reply(f"Here is your download link: {link}")

bot.run()
