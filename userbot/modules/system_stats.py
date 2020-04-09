# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot module for getting information about the server. """

from asyncio import create_subprocess_shell as asyncrunapp
from asyncio.subprocess import PIPE as asyncPIPE
from platform import python_version, uname
from shutil import which
from os import remove
from telethon import version

from userbot import CMD_HELP, ALIVE_NAME
from userbot.events import register

# ================= CONSTANT =================
NAMA = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================

@register(outgoing=True, pattern="^.sysd$")
async def sysdetails(sysd):
    """ For .sysd command, get system info using neofetch. """
    try:
        neo = "neofetch --stdout"
        fetch = await asyncrunapp(
            neo,
            stdout=asyncPIPE,
            stderr=asyncPIPE,
        )

        stdout, stderr = await fetch.communicate()
        result = str(stdout.decode().strip()) \
            + str(stderr.decode().strip())

        await sysd.edit("`" + result + "`")
    except FileNotFoundError:
        await sysd.edit("`Install neofetch first !!`")


@register(outgoing=True, pattern="^.botver$")
async def bot_ver(event):
    """ For .botver command, get the bot version. """
    if which("git") is not None:
        invokever = "git describe --all --long"
        ver = await asyncrunapp(
            invokever,
            stdout=asyncPIPE,
            stderr=asyncPIPE,
        )
        stdout, stderr = await ver.communicate()
        verout = str(stdout.decode().strip()) \
            + str(stderr.decode().strip())

        invokerev = "git rev-list --all --count"
        rev = await asyncrunapp(
            invokerev,
            stdout=asyncPIPE,
            stderr=asyncPIPE,
        )
        stdout, stderr = await rev.communicate()
        revout = str(stdout.decode().strip()) \
            + str(stderr.decode().strip())

        await event.edit("`Userbot Version: "
                         f"{verout}"
                         "` \n"
                         "`Revision: "
                         f"{revout}"
                         "`")
    else:
        await event.edit(
            "Shame that you don't have git, You're running 9.0 - 'Extended' anyway"
        )


@register(outgoing=True, pattern="^.pip(?: |$)(.*)")
async def pipcheck(pip):
    """ For .pip command, do a pip search. """
    pipmodule = pip.pattern_match.group(1)
    if pipmodule:
        await pip.edit("`Searching . . .`")
        invokepip = f"pip3 search {pipmodule}"
        pipc = await asyncrunapp(
            invokepip,
            stdout=asyncPIPE,
            stderr=asyncPIPE,
        )

        stdout, stderr = await pipc.communicate()
        pipout = str(stdout.decode().strip()) \
            + str(stderr.decode().strip())

        if pipout:
            if len(pipout) > 4096:
                await pip.edit("`Output too large, sending as file`")
                file = open("output.txt", "w+")
                file.write(pipout)
                file.close()
                await pip.client.send_file(
                    pip.chat_id,
                    "output.txt",
                    reply_to=pip.id,
                )
                remove("output.txt")
                return
            await pip.edit("**Query: **\n`"
                           f"{invokepip}"
                           "`\n**Result: **\n`"
                           f"{pipout}"
                           "`")
        else:
            await pip.edit("**Query: **\n`"
                           f"{invokepip}"
                           "`\n**Result: **\n`No Result Returned/False`")
    else:
        await pip.edit("`Gunakan .help pip untuk melihat cara menggunakannya`")


@register(outgoing=True, pattern="^.on$")
async def amireallyalive(alive):
    """ For .on command, check if the bot is running.  """
    await alive.edit(""
                     "**SenturyBot ONLINE, gunakan dengan bijak ya !!....\n**"
                     f"`------------------------------------\n`"
                     f"•  Nama             : **{NAMA}\n**"
                     f"`------------------------------------\n`"
                     f"•  Python           : `{python_version()}\n`"
                     f"•  Versi Telethon   : `{version.__version__}\n`"
                     f"`------------------------------------\n`"
                     "Beli Phising & Daftar Bot ? Chat [Jefanya Efandchris](t.me/JejakCheat)\n"
                     "")


@register(outgoing=True, pattern="^.aliveu")
async def amireallyaliveuser(username):
    """ For .aliveu command, change the username in the .alive command. """
    message = username.text
    output = '.aliveu [Isi Namamu] karena ini tidak bisa kosong'
    if not (message == '.aliveu' or message[7:8] != ' '):
        newuser = message[8:]
        global NAMA
        NAMA = newuser
        output = 'Username Berhasil Diganti Menjadi ' + newuser + '!'
    await username.edit("`" f"{output}" "`")
    
   
   

@register(outgoing=True, pattern="^.resetalive$")
async def amireallyalivereset(ureset):
    """ For .resetalive command, reset the username in the .alive command. """
    global NAMA
    NAMA = str(ALIVE_NAME) if ALIVE_NAME else uname().node
    await ureset.edit("`" "Sukses mengulangi data awal!" "`")
    
 

CMD_HELP.update({
    "sysd":
    ">`.sysd`"
    "\nFungsi: Memperlihatkan informasi sistem menggunakan neofetch.",
    "botver":
    ">`.botver`"
    "\nFungsi: Melihatkan versi yang digunakan SenturyBot.",
    "pip":
    ">`.pip <module(s)>`"
    "\nFungsi: Melakukan pencarian modul pip(s).",
    "alive":
    ">`.alive`"
    "\nFungsi: Ketik .on Untuk melihat apakah bot **Aktif** atau **Tidak**."
    "\n\n>`.aliveu <text>`"
    "\nFungsi: Mengganti 'nama' di teks .on."
    "\n\n>`.resetalive`"
    "\nFungsi: Mereset setting nama .on menjadi semula."
  
})
