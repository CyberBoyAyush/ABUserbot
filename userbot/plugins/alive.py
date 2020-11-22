import asyncio
from telethon import events
from userbot.utils import admin_cmd, sudo_cmd
from userbot import ALIVE_NAME, hellversion
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Hell User"

ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

kraken = bot.uid

PM_IMG = "https://telegra.ph/file/3783bd9bdde374797c704.jpg"
pm_caption = "__**🔥🔥ABUserbot Is Online🔥🔥**__\n\n"

pm_caption += f" __↼🄼🄰🅂🅃🄴🅁⇀__**『[{DEFAULTUSER}](tg://user?id={kraken})』**\n\n"

pm_caption += "🛡️TELETHON🛡️ : `1.15.0` \n"

pm_caption += f"😈Version😈       : `{hellversion}`\n"

pm_caption += f"⚜️Sudo⚜️          : `{sudou}`\n"

pm_caption += "⚠️CHANNEL⚠️   : [ᴊᴏɪɴ](https://t.me/AyushBots)\n"

pm_caption += "🔥CREATOR🔥    : [Click Here](https://t.me/CyberBoyAyush)\n\n"

pm_caption += "      [✨REPO✨](https://github.com/CyberBoyAyush/ABUserbot) 🔹 [📜License📜](https://github.com/CyberBoyAyush/ABUserbot/blob/master/LICENSE)"
#@command(outgoing=True, pattern="^.alive$")
@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    chat = await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete() 
