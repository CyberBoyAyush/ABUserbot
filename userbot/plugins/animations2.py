#Credits To @Kraken_The_BadASS . Keep credit if you are going to copy paste it.. LOL NOOBS :-) Also Join @Testpy12 for more madafaking awesome plugins.....

import os
import sys
import logging
from telethon import events
import asyncio
from userbot.utils import admin_cmd
from userbot import ALIVE_NAME
import random, re
from userbot import CMD_HELP
from collections import deque
import importlib.util
import random
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Hell User"



@borg.on(admin_cmd(pattern="virus$"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(0, 30)
    await event.edit("Injecting virus....")
    animation_chars = [
            "🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎",
            "◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎",
            "◼️◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎",
            "◼️◼️◼️️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎",
            "◼️◼️◼️◼️🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎",
            "‎◼️◼️◼️◼️◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎",
            "◼️◼️◼️◼️◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎",
            "◼️◼️◼️◼️◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎",
            "◼️◼️◼️◼️◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎",
            "◼️◼️◼️◼️◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️",
            "◼️◼️◼️◼️◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️◼️",
            "◼️◼️◼️◼️◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️◼️◼️",
            "◼️◼️◼️◼️◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎◼️◼️◼️◼️",
            "◼️◼️◼️◼️◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️◼️◼️◼️◼️",
            "◼️◼️◼️◼️◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️◼️◼️◼️◼️",
            "◼️◼️◼️◼️◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️◼️◼️◼️◼️",
            "◼️◼️◼️◼️◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️◼️◼️◼️◼️",
            "◼️◼️◼️◼️◼️\n◼️◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️◼️◼️◼️◼️",
            "◼️◼️◼️◼️◼️\n◼️◼️◼️🔴🔵🌕♓♎⛎◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️◼️◼️◼️◼️",
            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️◼️◼️◼️◼️",
            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️◼️◼️◼️◼️",
            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️◼️\n◼️◼️◼️◼️◼️",
            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️◼️\n◼️🔴🔵🌕♓♎⛎◼️◼️◼️\n◼️◼️◼️◼️◼️",
            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🔴🔵🌕♓♎⛎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
            "◼️◼️◼️◼️\n◼️◼️◼️◼️\n◼️◼️◼️◼️\n◼️◼️◼️◼️",
            "◼️◼️◼️\n◼️◼️◼️\n◼️◼️◼️",
            "◼️◼️\n◼️◼️",
            "◼️"
        ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 30])

@borg.on(admin_cmd(pattern=r"repe$", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.2
    animation_ttl = range(0, 30)
    await event.edit("repe")
    animation_chars = [
        
            "**r**",
            "**ra**",
            "**rap**",
            "**rape**",
            "**rape_**",    
            "**rape_t**",
            "**rape_tr**",
            "**rape_tra**",
            "**rape_trai**",
            "**rape_train**",
            "**ape_train🚅**",
            "**pe_train🚅🚃🚃**",
            "**e_train🚅🚃🚃🚃**",
            "**_train🚅🚃🚃🚃🚃**",
            "**train🚅🚃🚃🚃🚃🚃**",
            "**rain🚅🚃🚃🚃🚃🚃🚃**",
            "**ain🚅🚃🚃🚃🚃🚃🚃🚃**",
            "**in🚅🚃🚃🚃🚃🚃🚃🚃🚃**",
            "**n🚅🚃🚃🚃🚃🚃🚃🚃🚃🚃**",
            "🚅🚃🚃🚃🚃🚃🚃🚃🚃🚃",
            "🚃🚃🚃🚃🚃🚃🚃🚃🚃",
            "🚃🚃🚃🚃🚃🚃🚃🚃",
            "🚃🚃🚃🚃🚃🚃🚃",
            "🚃🚃🚃🚃🚃🚃",
            "🚃🚃🚃🚃🚃",
            "🚃🚃🚃🚃",
            "🚃🚃🚃",
            "🚃🚃",
            "🚃",
            "**rApEd**"
 ]
    for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 30])
            
@borg.on(admin_cmd(pattern=f"squ$",outgoing=True))
async def _(event):
    if event.fwd_from:
        return


    await event.edit("╔═══════════════════╗ \n  \n╚═══════════════════╝")
    await asyncio.sleep(1)
    await event.edit("╔═══════════════════╗ \n \t░ \n╚═══════════════════╝")
    await asyncio.sleep(1)
    await event.edit("╔═══════════════════╗ \n ░ \t░ \n╚═══════════════════╝")
    await asyncio.sleep(1)
    await event.edit("╔═══════════════════╗ \n ░ ░ ░ \n╚═══════════════════╝")
    await asyncio.sleep(1)
    await event.edit("╔═══════════════════╗ \n ░ ░ ░ ░ \n╚═══════════════════╝") 
    await asyncio.sleep(1)
    await event.edit("╔═══════════════════╗ \n ░ ░ ░ ░ ░ \n╚═══════════════════╝")
    await asyncio.sleep(1)
    await event.edit("╔═══════════════════╗ \n ░ ░ ░ ░ ░ ░ \n╚═══════════════════╝")
    await asyncio.sleep(1)
    await event.edit("╔═══════════════════╗ \n ░ ░ ░ ░ ░ ░ ░ \n╚═══════════════════╝")
    await asyncio.sleep(1)
    await event.edit("╔═══════════════════╗ \n ░ ░ ░ ░ ░ ░ ░ ░ \n╚═══════════════════╝")
    await asyncio.sleep(1)
    await event.edit("╔═══════════════════╗ \n ░ ░ ░ ░ ░ ░ ░ ░ ░ \n╚═══════════════════╝")
    await asyncio.sleep(1)
    await event.edit("╔═══════════════════╗ \n ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ \n╚═══════════════════╝")
    await asyncio.sleep(1)
    await event.edit("╔═══════════════════╗ \n ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ \n╚═══════════════════╝")
    await asyncio.sleep(1)
    await event.edit("╔═══════════════════╗ \n ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ \n╚═══════════════════╝")
    await asyncio.sleep(1) 
    await event.edit("╔═══════════════════╗ \n ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ \n╚═══════════════════╝")
    await asyncio.sleep(1)
    await event.edit("╔═══════════════════╗ \n ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ \n╚═══════════════════╝")
    await asyncio.sleep(6)	
	
@borg.on(admin_cmd(pattern=r"star$", outgoing=True))
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("🦋✨🦋✨🦋✨🦋✨"))
	for _ in range(48):
		await asyncio.sleep(0.1)
		await event.edit("".join(deq))
		deq.rotate(1)
		
@borg.on(admin_cmd(pattern=r"boxs"))
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("🟥🟧🟨🟩🟦🟪🟫⬛⬜"))
	for _ in range(48):
		await asyncio.sleep(0.1)
		await event.edit("".join(deq))
		deq.rotate(1)
		
@borg.on(admin_cmd(pattern=f"rain$", outgoing=True))
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("🌬☁️🌩🌨🌧🌦🌥⛅🌤"))
	for _ in range(48):
		await asyncio.sleep(0.1)
		await event.edit("".join(deq))
		deq.rotate(1)

@borg.on(admin_cmd(pattern=r"odra$"))
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("🚶🏃🚶🏃🚶🏃🚶🏃"))
	for _ in range(48):
		await asyncio.sleep(0.1)
		await event.edit("".join(deq))
		deq.rotate(1)
		
@borg.on(admin_cmd(pattern="lobe", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.5
    animation_ttl = range(0, 70)
    await event.edit("loveu")
    animation_chars = [
            "😀",
            "👩‍🎨",
            "😁",    
            "😂",
            "🤣",
            "😃",
            "😄",
            "😅",
            "😊",
            "☺",
            "🙂",    
            "🤔",
            "🤨",
            "😐",
            "😑",
            "😶",
            "😣",
            "😥",
            "😮",    
            "🤐",
            "😯",
            "😴",
            "😔",
            "😕",
            "☹",
            "🙁",
            "😖",    
            "😞",
            "😟",
            "😢",
            "😭",
            "🤯",
            "💔",
            "❤",
            "i Love You❤",   
        ]
    for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 35])
    
@borg.on(admin_cmd(pattern=r"muah$"))
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("😗😙😚😚😘"))
	for _ in range(48):
		await asyncio.sleep(0.1)
		await event.edit("".join(deq))
		deq.rotate(1)	
    
@borg.on(admin_cmd(pattern="heart$"))		
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("❤️🧡💛💚💙💜🖤"))
	for _ in range(48):
		await asyncio.sleep(0.1)
		await event.edit("".join(deq))
		deq.rotate(1)        
        
		
@borg.on(admin_cmd(pattern="gym$", outgoing=True))
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("🏃‍🏋‍🤸‍🏃‍🏋‍🤸‍🏃‍🏋‍🤸‍"))
	for _ in range(48):
		await asyncio.sleep(0.1)
		await event.edit("".join(deq))
		deq.rotate(1)
    
@borg.on(admin_cmd(pattern=f"clown$", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.50
    animation_ttl = range(0, 16)
    animation_chars = [
        

            "COMMAND CREATE BY @Kraken_The_BadASS",
            "🤡️",
            "🤡🤡",
            "🤡🤡🤡",
            "🤡🤡🤡🤡",
            "🤡🤡🤡🤡🤡",
            "🤡🤡🤡🤡🤡🤡",    
            "🤡🤡🤡🤡🤡",
            "🤡🤡🤡🤡",
            "🤡🤡🤡",
            "🤡🤡",
            "🤡",
            "You",
            "You Are",
            "You Are A",
            "You Are A Clown 🤡"
        ]

    for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 16])

@borg.on(admin_cmd(pattern=r"theart$", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1.3
    animation_ttl = range(0, 50)
    animation_chars = [
            "❤️",
            "🧡",
            "💛",
            "💚",
            "💙",
            "💜",
            "🖤",
            "💘",
            "💝",
            "💔",
            "❤️",
            "🧡",
            "💛",
            "💚",
            "💙",
            "💜",
            "🖤",
            "💘",
            "💝",
            "💔"
        ]
    for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 20])  
            
           
