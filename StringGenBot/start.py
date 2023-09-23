from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_photo(
        chat_id=msg.chat.id,
        caption="""¤¦ اهلا بـك عزيـزي 

¤¦ يمكنك استـخـراج التالـي

¤¦ تيرمڪس تليثون للحسابات

¤¦ تيرمـكـس تليثون للبوتـات

¤¦ بايـروجـرام مـيوزك للحسابات

¤¦ بايـروجـرام مـيوزك للبوتات

""",
photo="https://telegra.ph/file/7fc3395423ac8243ffe93.jpg",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="إضغط لبدا استخراج الكود", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("قناة المطور", url="https://t.me/ZFZ_ZFZ"),
                    InlineKeyboardButton("المطور", user_id=OWNER_ID)
                ]
            ]
        ),
        
    )
