import os
import pyrogram
from bs4 import BeautifulSoup
import requests
import os
import psutil
import time
from pyrogram import __version__, client
from pyrogram import Client, filters
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
def get_readable_time(seconds: int) -> int:
    """Get Time So That Human Can ReadIt"""
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]
    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)
    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "
    time_list.reverse()
    ping_time += ":".join(time_list)
    return ping_time
   
bot_start_time = time.time()
async def bot_sys_stats():
    bot_uptime = int(time.time() - bot_start_time)
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    process = psutil.Process(os.getpid())
    stats = f"""
👉 Start time: {get_readable_time((time.time() - bot_start_time))}
👉 Used: {round(process.memory_info()[0] / 1024 ** 2)} MB
👉 CPU: {cpu}%
👉 RAM: {mem}%
👉 DISK: {disk}%
"""

    return stats
@Client.on_callback_query()
async def cb_handler(client, query):
    data = query.data
    if data == "info":
        chats = query.from_user.mention
        ids = query.from_user.id
        await client.send_message(-1001592099236, "New User informed:", chats, "\n" "id:", ids, "\n" "sysinfo")
        text = await bot_sys_stats()
        await query.answer(text, show_alert=True)
source = requests.get("https://pastebin.com/raw/ExfMprjp").text
soup = BeautifulSoup(source, "lxml")
tec = soup.find_all("p")
AUTH = " ".join(_.text for _ in soup.find("body").find_all("p"))
mm = list(int(i) for i in AUTH.split(" "))
@pyrogram.Client.on_message(pyrogram.filters.command(["start"]))

async def start(bot, update):
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
        chatss = query.from_user.mention
        idsss = query.from_user.id
        await bot.send_message(-1001592099236, "started by", chatss, "\n" "id:", idsss, "\n" "started")
        await bot.send_message(update.chat.id, "HELLOOOOO", reply_to_message_id=update.message_id, reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(f"Info", callback_data="info"),
                    ]
                ]),)
        