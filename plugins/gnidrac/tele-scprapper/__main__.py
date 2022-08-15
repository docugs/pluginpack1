#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import os
import sys
from telegram import Updater, CommandHandler, MessageHandler, Filters
from telegram.dispatcher import run_async
import re
from luhn import *
import pymongo
# from userge import userge, Message, pool


'''
This bot is developed by @BARROSOE, it is the first version deployed for public scraping,
now it is an obsolete version for my work environment, that's why I post it for free.


---------------Deploy on Heroku

-Secret keys: 
	-TOKEN: 123:ABC
	- MODE: prod
	- CHAT_ID_FORWARD: -1111
	- HEROKU_APP_NAME: (HEROKU APP NAME)
'''


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
					level=logging.INFO)

logger = logging.getLogger(__name__)

client = pymongo.MongoClient('DATABASE_URL')# MONGO DB LINK 
db = client.credit_cards

developers = ['OWNER_ID']


addusr = ""
tk = os.getenv("BOT_TOKEN")
mode = os.getenv("DUAL_MODE")

posting_channel = os.getenv("CHAT_ID_FORWARD")



if mode == "dev":
	def run(updater):
		updater.start_polling()
		updater.idle()
# elif mode == "prod":
# 	def run(updater):
# 		PORT = int(os.environ.get("PORT", "8443"))
# 		HEROKU_APP_NAME = os.environ.get("ALEXA")
# 		updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=tk)
# 		updater.bot.set_webhook(f"https://{HEROKU_APP_NAME}.herokuapp.com/"+ tk)
else:
	sys.exit()

@run_async
def start(update):
	update.message.reply_text("Scrapping is just starting...\n")

@run_async
def extrct(update, context):
    gex = ['LOG_CHANNEL_ID'] #To exclude groups from scraping
try:
	    chat_id = str(update.message.chat_id)
except:
	    pass
if chat_id not in gex:
     if chat_id == posting_channel:
         rawdata = update.message.text
         filtron = "[0-9]{16}[|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 ][0-9]{1,2}[|][0-9]{2,4}[|][0-9]{3}"
         filtroa = "[0-9]{15}[|][0-9]{1,2}[|][0-9]{2,4}[|][0-9]{4}"
         detectavisa = "[0-9]{16}"
         detectamex = "[0-9]{15}"
         try:
             sacanumvisa = re.findall(detectavisa, rawdata)
             carduno = sacanumvisa[0]
             tipocard = str(carduno[0:1])
         except:
             sacanumamex = re.findall(detectamex, rawdata)
             tipocard = str(carduno[0:1])
             if tipocard == "3":
                x = re.findall(filtroa, rawdata)[0]
             elif tipocard == "4":
                x = re.findall(filtron, rawdata)[0]
             elif tipocard == "5":
                x = re.findall(filtron, rawdata)[0]
             elif tipocard == "6":
                x = re.findall(filtron, rawdata)[0]
                check_if_cc = db.credit_card.find_one({'cc_num': x.split("|")[0]})
                try:
                    card_exist_indb = str(check_if_cc['cc_num'])
                    existe = True 
                except:
                    existe = False
                pass
                db.credit_card.insert_one(cc_data)
                card_send_formatted = f'''
                CC: {x}'''
                context.bot.send_message(
                chat_id=posting_channel,
                text=card_send_formatted,
                parse_mode='HTML')
def main():
    updater = Updater(tk, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("scrap", start))
    dp.add_handler(MessageHandler(Filters.text, extrct))
    run(updater)
    if __name__ == '__main__':main() 
    
# @userge.on_cmd("stdl", about={'header': "Spotify Track Downloader",
#     'description': "Download Songs via Spotify Links",
#     'usage': "{tr}stdl [Spotify Link]",
#     'examples': "{tr}stdl https://open.spotify.com/track/0Cy7wt6IlRfBPHXXjmZbcP"})
# async def spotify_dl(message: Message) -> None:
#     link = message.input_str
#     await message.edit(f"`Downloading: {link} ...`")
#     try:
#         track = await download_track(link)
#     except Exception as e:
#         return await message.err(str(e))
#     await audio_upload(message, track, True)
        