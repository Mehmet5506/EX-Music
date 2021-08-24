# Module by https://github.com/tofikdn
# Copyright (C) 2021 TdMusic
# Ported by @rizexx for EXMusic

import requests
from pyrogram import Client
from EXmusic.config import BOT_USERNAME
from EXmusic.helpers.filters import command

@Client.on_message(command(["asupan", f"asupan@Efsanestar_bot"]))
async def asupan(client, message):
    try:
        resp = requests.get("https://tede-api.herokuapp.com/api/asupan/ptl").json()
        results = f"{resp['url']}"
        return await client.send_video(message.chat.id, video=results)
    except Exception:
        await message.reply_text("`Bir şeyler ters gitti...`")


@Client.on_message(command(["wibu", f"wibu@Efsanestar_bot"]))
async def wibu(client, message):
    try:
        resp = requests.get("https://tede-api.herokuapp.com/api/asupan/wibu").json()
        results = f"{resp['url']}"
        return await client.send_video(message.chat.id, video=results)
    except Exception:
        await message.reply_text("`Bir şeyler ters gitti...`")


@Client.on_message(command(["chika", f"chika@Efsanestar_bot"]))
async def chika(client, message):
    try:
        resp = requests.get("https://tede-api.herokuapp.com/api/chika").json()
        results = f"{resp['url']}"
        return await client.send_video(message.chat.id, video=results)
    except Exception:
        await message.reply_text("`Bir şeyler ters gitti....`")
