# Copyright (C) 2021 By EXMusic


import asyncio

from pyrogram import Client, filters
from pyrogram.types import Dialog, Chat, Message
from pyrogram.errors import UserAlreadyParticipant

from EXmusic.services.callsmusic.callsmusic import client as exmusic
from EXmusic.config import SUDO_USERS

@Client.on_message(filters.command(["gcast"]))
async def broadcast(_, message: Message):
    sent=0
    failed=0
    if message.from_user.id not in SUDO_USERS:
        return
    else:
        wtf = await message.reply("`yayını başlatma...`")
        if not message.reply_to_message:
            await wtf.edit("lütfen yayını başlatmak için bir iletiyi yanıtlayın!")
            return
        lmao = message.reply_to_message.text
        async for dialog in exmusic.iter_dialogs():
            try:
                await exmusic.send_message(dialog.chat.id, lmao)
                sent = sent+1
                await wtf.edit(f"`Yayın...` \n\n**gönderildiği yer:** `{sent}` Sohbet \n**başarısız oldu:** {failed} chats")
                await asyncio.sleep(3)
            except:
                failed=failed+1
        await message.reply_text(f"`gcast başarıyla` \n\n**gönderildiği yer:** `{sent}` sohbet \n**başarısız oldu:** {failed} chats")
