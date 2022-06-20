from aiogram import Bot, Dispatcher, types
from app import bot, dp
import wikipedia
from States import asosiy
from keyboard import Bosh
wikipedia.set_lang("uz")
@dp.message_handler(content_types="text", state= asosiy.wiki)
async def wiki(m:types.Message):
    text=m.text
    try:
        result=wikipedia.summary(text)
        if len(result)>4096:
            for res in range(0, len(result), 4096):
                await m.answer(result [res:res+4096])
        else:
            await m.reply(result)
    except wikipedia.exceptions.DisambiguationError:
        await m.reply("Batafsilroq kiriting")
    except wikipedia.exceptions.PageError:
        await m.reply("Ma'lumot topilmadi")



