# < (c) 2021 @Godmrunal >

import logging
from os import remove

import requests
from decouple import config
from telethon import Button, TelegramClient, events


logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=logging.INFO
)

bot = TelegramClient(None, api_id=6, api_hash="eb06d4abfb49dc3eeb1aeb98ae0f581e").start(
    bot_token=config("BOT_TOKEN")
)

logging.info("Starting bot...")


@bot.on(events.NewMessage(incoming=True, pattern="^/start"))
async def start_(event):
    await event.reply(
        "Hi {}!\nI am A Intimacyfolksmovies Donation Bot. \n\n**Donation:** Thanks for Generosity and your kind Heart. For my masters to keep on updating Movies and Series they need resources. They take their time to download the movies and Series to keep you entertained. Thanks again to hear you wanna donate. Donate by clicking on the button below!".format(
            (await bot.get_entity(event.sender_id)).first_name
        ),
        buttons=[
            [
                Button.url("❤️ Requests Group ❤️", url="https://t.me/intimacyfolksmoviesrequests"),
                Button.url(
                    "❤️ Movies Channel ❤️", url="https://t.me/Intimacyfolksmovies"
                ),
            ],
            [Button.url("❤️ Donate ❤️", url="https://t.me/BeastX_Bots")],
        ],
    )




logging.info("\n\nBot has started.\n(c) @Godmrunal")

bot.run_until_disconnected()
