# Anonymize - Forward tag remover bot
# Copyright (C) 2021 @Alain_xD
#
# This file is a part of < https://github.com/BotzCity/ForwardTagRemover/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/BotzCity/ForwardTagRemover/blob/main/LICENSE/>.

import re, os, random, asyncio, html
os.system("pip install pyrogram")
import pyrogram
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

APP_ID = 2888382
API_HASH = "908a8a13c87a6c1899f6e788a05d3d0d"
BOT_TOKEN = "1891306874:AAFwwdIcAAoW47QEnVvKk4btVbCNT-62Lmw"

app = pyrogram.Client("app", api_id=APP_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

start_but = ([[
        InlineKeyboardButton('Hᴇʟᴘ', callback_data='Help'),
        InlineKeyboardButton('Cʟᴏsᴇ', callback_data='close')
    ],
    [
        InlineKeyboardButton('Dᴇᴠᴇʟᴏᴘᴇʀ', url='https://t.me/Alain_xD'),
        InlineKeyboardButton('Uᴘᴅᴀᴛᴇs', url='t.me/BotzCity')
    ]])

button = InlineKeyboardMarkup(start_but)

but = InlineKeyboardMarkup([[InlineKeyboardButton("Hᴇʟᴘ", callback_data="Help"), InlineKeyboardButton("Cʟᴏsᴇ", callback_data="close")],[InlineKeyboardButton("Uᴘᴅᴀᴛᴇs", url="t.me/BotzCity"), InlineKeyboardButton("Dᴇᴠᴇʟᴏᴘᴇʀ", url="t.me/Alain_xD")]])

@app.on_message(filters.command(["start"]))
async def start(lel, message):
    await message.reply_text(f"**Hi** `{message.from_user.first_name}` **!\n\nI'm any forward tag remover // anonymize bot! I can send the file which you sended to me, without forward tag..!**", reply_markup=but)

@app.on_message(filters.command(["help"]))
async def help(ha, message):
    await app.send_message(message.chat.id, """**Help\n
This bot will send back the document/file/pic/video/image/text that you forward, back to you, so that the forwarded from tag is removed and it looks like it's forwarded from the bot!!\n\nMade with ❤️ by @BotzCity**""") 

@app.on_callback_query()
async def button(app, update):
    k = update.data
    if "Help" in k:
       await update.message.delete()
       await help(app, update.message)
    elif "close" in k:
       await update.message.delete()
    elif "home" in k:
       await update.message.delete()
       await start(app, update.message)

@app.on_message(filters.private)
async def copy(fuck, message):
    try:
       await message.copy(message.chat.id)
    except RCPError as lel:
       await message.reply(lel)
       return


print("Started your bot")
print("Send file // any message and party")
print("Join @BotzCity for any help !")
app.run()
