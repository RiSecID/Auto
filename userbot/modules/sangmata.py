#Port to userbot by @JejakCheat

import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from userbot.events import register
from userbot import bot, CMD_HELP

@register(outgoing=True, pattern="^.sg(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.edit("`Balas Pesan Siapapun.`")
       return
    reply_message = await event.get_reply_message() 
    if not reply_message.text:
       await event.edit("```Balas ke chat```")
       return
    chat = "@SangMataInfo_bot"
    sender = reply_message.sender
    if reply_message.sender.bot:
       await event.edit("`Balas ke pesan seseorang.`")
       return
    await event.edit("`Sedang Memproses ...`")
    async with bot.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=461843263))
              await bot.forward_messages(chat, reply_message)
              response = await response 
          except YouBlockedUserError: 
              await event.reply("`Tolong buka blokir @sangmatainfo_bot dan coba lagi`")
              return
          if response.text.startswith("Forward"):
             await event.edit("`Orang ini memprivasi nama dia !`")
          else: 
             await event.edit(f"{response.message.message}")


CMD_HELP.update({
        "sangmata": 
        ".sg \
          \nUsage: Untuk melihat history nama dari pengguna.\n"
    })
