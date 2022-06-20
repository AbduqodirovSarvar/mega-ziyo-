from aiogram import Bot, Dispatcher, types, executor
from admins import Token, Admins
from Postgresql import add_user, full
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from keyboard import contakt, menu, kurs, harid, Bosh
from States import asosiy
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import InputFile

bot = Bot(token=Token)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(content_types=types.ContentTypes.PHOTO)
async def contact_send(m:types.Message, state: FSMContext):
    await m.reply(m.photo[-1].file_id)

@dp.message_handler(commands='start')
async def start(ms: types.Message):
    await ms.answer("Salom,\nTelefon raqam jo'nating", reply_markup= contakt)

@dp.message_handler(content_types='contact')
async def contact_send(m:types.Message, state: FSMContext):
    contact = m.contact
    name = m.from_user.full_name
    id = m.from_user.id
    phone=contact['phone_number']
    await m.answer("Raxmat!", add_user(id, name, phone))
    await m.bot.send_message(5278642953, f"{name} \nTelefon raqami: {phone}")
    await m.answer('Kerakli bo\'limni tanlang:',reply_markup=menu)
    await asosiy.main.set()


@dp.message_handler(text="Kurslar", state= asosiy.main)
async def contact_send(m:types.Message, state: FSMContext):
    await m.answer("Kursni tanlang:", reply_markup=kurs)
    await asosiy.kurs.set()
    
@dp.message_handler(text="Testlar", state= asosiy.main)
async def contact_send(m:types.Message, state: FSMContext):
    await m.answer("Qaysi fandan test olmoqchisiz:", reply_markup=kurs)
    await asosiy.test.set()
    
@dp.message_handler(text="Wikipedia", state= asosiy.main)
async def contact_send(m:types.Message, state: FSMContext):
    await m.answer("Sizga nima haqida ma'lumot kerak\nMen sizga uni wikipediadan topib beraman😊", reply_markup=Bosh)
    await asosiy.wiki.set()

@dp.message_handler(text="Mega Ziyo haqida", state= asosiy.main)
async def contact_send(m:types.Message, state: FSMContext):
    rasm=types.MediaGroup()
    r1=InputFile(path_or_bytesio='rasmlar/rasm1.jpg')
    r2=InputFile(path_or_bytesio='rasmlar/rasm2.jpg')
    r3=InputFile(path_or_bytesio='rasmlar/rasm3.jpg')
    rasm.attach_photo(photo=r1)
    rasm.attach_photo(photo=r2)
    rasm.attach_photo(photo=r3)
    await m.answer("MEGA ZIYO o'quv markazi hayotidan lavhalar:", reply_markup=Bosh)
    await m.answer_media_group(media=rasm)
    await asosiy.about.set()

@dp.message_handler(text="Bosh sahifa", state= asosiy.about)
async def contact_send(m:types.Message, state: FSMContext):
    await m.answer('Kerakli bo\'limni tanlang:',reply_markup=menu)
    await asosiy.main.set()

    
@dp.message_handler(text="Filiallarimiz", state= asosiy.main)
async def contact_send(m:types.Message, state: FSMContext):
    oybek='https://goo.gl/maps/zUBCECyCFXqnhe4i9'
    zafar='https://goo.gl/maps/NHrks5qBrajg6hRy8'
    await m.answer("Bizning filiallarimiz manzillari:", reply_markup=Bosh)
    await m.answer(f"Oybek filiali:\n{oybek}")
    await m.answer(f"Zafar filiali:\n{zafar}")
    await asosiy.filial.set()

@dp.message_handler(text="Bosh sahifa", state= asosiy.filial)
async def contact_send(m:types.Message, state: FSMContext):
    await m.answer('Kerakli bo\'limni tanlang:',reply_markup=menu)
    await asosiy.main.set()
    
@dp.message_handler(text="Biz bilan bog'lanish", state= asosiy.main)
async def contact_send(m:types.Message, state: FSMContext):
    group='https://t.me/+TtzUVvzu5Q-v04VX'
    tel='+998 93 162 93 93'
    chan='https://t.me/MegaZiyo_official'
    await m.answer("Bizning online manzilarimiz:", reply_markup=Bosh)
    await m.answer(f"Rasmiy guruh:\n{group}\nRasmiy kanal:\n{chan}\nQo'ng'iroq uchun:\n{tel}")
    await asosiy.aloqa.set()

@dp.message_handler(text="Bosh sahifa", state= asosiy.aloqa)
async def contact_send(m:types.Message, state: FSMContext):
    await m.answer('Kerakli bo\'limni tanlang:',reply_markup=menu)
    await asosiy.main.set()

@dp.message_handler(text="En-Uz tarjimon", state= asosiy.main)
async def contact_send(m:types.Message, state: FSMContext):
    await m.answer("Menga so'z yuboring men sizga uni ingliz tiliga tarjima qilib yuboraman:", reply_markup=ReplyKeyboardRemove())
    await asosiy.translate.set()

@dp.message_handler(text="Bosh sahifa", state= asosiy.translate)
async def contact_send(m:types.Message, state: FSMContext):
    await m.answer('Kerakli bo\'limni tanlang:',reply_markup=menu)
    await asosiy.main.set()

@dp.message_handler(text="Bosh sahifa", state= asosiy.kurs)
async def contact_send(m:types.Message, state: FSMContext):
    await m.answer('Kerakli bo\'limni tanlang:',reply_markup=menu)
    await asosiy.main.set()

@dp.message_handler(text="Bosh sahifa", state= asosiy.test)
async def contact_send(m:types.Message, state: FSMContext):
    await m.answer('Kerakli bo\'limni tanlang:',reply_markup=menu)
    await asosiy.main.set()

@dp.message_handler(text="Bosh sahifa", state= asosiy.wiki)
async def contact_send(m:types.Message, state: FSMContext):
    await m.answer('Kerakli bo\'limni tanlang:',reply_markup=menu)
    await asosiy.main.set()


async def commands(m):
    await m.bot.set_my_commands(
        [
            types.BotCommand("start", 'Botni ishga tushurish'),
            types.BotCommand("help", "Yordam")
        ]
    )
async def habar(m:types.Message):
    for admin in Admins:
        try:
            await m.bot.send_message(admin, "BOT ISHGA TUSHDI")
        except:
            continue
    await commands(dp)

@dp.message_handler(text="Matematika", state= asosiy.test)
async def contact_send1(m:types.Message, state: FSMContext):
    matem='AgACAgIAAxkBAAPeYqmLpHAn1SLD1xvDrn8MmE8jPZEAAjmtMRviAZFINBEqkqiXCdkBAAMCAAN5AAMkBA'
    await m.answer_photo(matem, caption="Bu yilgi titul varoqchasi quyidagicha bo'ladi:", reply_markup=menu)
    await m.answer("testlar tez orada qo'yiladi")
    await asosiy.main.set()

@dp.message_handler(text="Fizika", state= asosiy.test)
async def contact_send2(m:types.Message, state: FSMContext):
    matem='AgACAgIAAxkBAAPeYqmLpHAn1SLD1xvDrn8MmE8jPZEAAjmtMRviAZFINBEqkqiXCdkBAAMCAAN5AAMkBA'
    await m.answer_photo(matem, caption="Bu yilgi titul varoqchasi quyidagicha bo'ladi:", reply_markup=menu)
    await m.answer("testlar tez orada qo'yiladi")
    await asosiy.main.set()

@dp.message_handler(text="Ona-tili", state= asosiy.test)
async def contact_send3(m:types.Message, state: FSMContext):
    matem='AgACAgIAAxkBAAPeYqmLpHAn1SLD1xvDrn8MmE8jPZEAAjmtMRviAZFINBEqkqiXCdkBAAMCAAN5AAMkBA'
    await m.answer_photo(matem, caption="Bu yilgi titul varoqchasi quyidagicha bo'ladi:", reply_markup=menu)
    await m.answer("testlar tez orada qo'yiladi")
    await asosiy.main.set()



@dp.message_handler(text="Matematika", state= asosiy.kurs)
async def contact_send5(m:types.Message, state: FSMContext):
    matem='AgACAgIAAxkBAAPbYqmLpI13O7CA8O-epwrRLGZUc54AAp2tMRtb_7lJTQJ4ctkGenoBAAMCAAN5AAMkBA'
    await m.answer_photo(matem, caption="Matematika kursimizga yozilasizmi:", reply_markup=harid)
    await asosiy.harid.set()

@dp.message_handler(text="Kursga yozilish", state= asosiy.harid)
async def contact_send6(m:types.Message, state: FSMContext):
    await m.answer("Raxmat tez orada siz bilan o'zimiz bog'lanamiz.", reply_markup=menu)
    await m.bot.send_message(5278642953, f"Name={m.from_user.full_name} \nID={m.from_user.id}\nMatematika kursiga yozildi:")
    await asosiy.main.set()

@dp.message_handler(text="Bosh sahifa", state= asosiy.harid)
async def contact_send7(m:types.Message, state: FSMContext):
    await m.answer('Kerakli bo\'limni tanlang:', reply_markup=menu)
    await asosiy.main.set()

@dp.message_handler(text="Fizika", state= asosiy.kurs)
async def contact_send8(m:types.Message, state: FSMContext):
    fizika='AgACAgIAAxkBAAPcYqmLpGqIXi_UKM_geB40sFVGTz4AAuisMRsQi7hJEWsXaw3ea2sBAAMCAAN5AAMkBA'
    await m.answer_photo(fizika, caption="Fizika kursimizga yozilasizmi:", reply_markup=harid)
    await asosiy.harid.set()

@dp.message_handler(text="Kursga yozilish", state= asosiy.harid)
async def contact_send9(m:types.Message, state: FSMContext):
    await m.answer("Raxmat tez orada siz bilan o'zimiz bog'lanamiz.", reply_markup=menu)
    await m.bot.send_message(5278642953, f"Name={m.from_user.full_name} \nID={m.from_user.id}\nFizika kursiga yozildi:")
    await asosiy.main.set()

@dp.message_handler(text="Ona-tili", state= asosiy.kurs)
async def contact_send10(m:types.Message, state: FSMContext):
    onatili='AgACAgIAAxkBAAPdYqmLpJfO8_U42gABTKBe0mLDYvv3AALprDEbEIu4SWnkiH_jvBujAQADAgADeQADJAQ'
    await m.answer_photo(onatili, caption="Ona-tili kursimizga yozilasizmi:", reply_markup=harid)
    await asosiy.harid.set()

@dp.message_handler(text="Kursga yozilish", state= asosiy.harid)
async def contact_send(m:types.Message, state: FSMContext):
    await m.answer("Raxmat tez orada siz bilan o'zimiz bog'lanamiz.", reply_markup=menu)
    await m.bot.send_message(5278642953, f"Name={m.from_user.full_name} \nID={m.from_user.id}\nOna-tili kursiga yozildi:")
    await asosiy.main.set()

@dp.message_handler(text="Matematika", state= asosiy.kurs)
async def contact_send11(m:types.Message, state: FSMContext):
    matem='AgACAgIAAxkBAAPbYqmLpI13O7CA8O-epwrRLGZUc54AAp2tMRtb_7lJTQJ4ctkGenoBAAMCAAN5AAMkBA'
    await m.answer_photo(matem, caption="Matematika kursimizga yozilasizmi:", reply_markup=harid)
    await asosiy.harid.set()

@dp.message_handler(text="Kursga yozilish", state= asosiy.harid)
async def contact_send12(m:types.Message, state: FSMContext):
    await m.answer("Raxmat tez orada siz bilan o'zimiz bog'lanamiz.", reply_markup=menu)
    await m.bot.send_message(5278642953, f"Name={m.from_user.full_name} \nID={m.from_user.id}\nMatematika kursiga yozildi:")
    await asosiy.main.set()
@dp.message_handler(text="Bosh sahifa", state= asosiy.test)
async def contact_send7(m:types.Message, state: FSMContext):
    await m.answer('Kerakli bo\'limni tanlang:', reply_markup=menu)
    await asosiy.main.set()

@dp.message_handler(text="Bosh sahifa", state= asosiy.kurs)
async def contact_send7(m:types.Message, state: FSMContext):
    await m.answer('Kerakli bo\'limni tanlang:', reply_markup=menu)
    await asosiy.main.set()

@dp.message_handler(text="Bosh sahifa", state= asosiy.translate)
async def contact_send7(m:types.Message, state: FSMContext):
    await m.answer('Kerakli bo\'limni tanlang:', reply_markup=menu)
    await asosiy.main.set()
@dp.message_handler(text="Bosh sahifa", state= asosiy.aloqa)
async def contact_send7(m:types.Message, state: FSMContext):
    await m.answer('Kerakli bo\'limni tanlang:', reply_markup=menu)
    await asosiy.main.set()

from wikiqism import *


if __name__=="__main__":
    executor.start_polling(dp, on_startup=habar)

