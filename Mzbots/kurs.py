from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from keyboard import contakt, menu, kurs, harid
from States import asosiy
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from app import bot, dp
from app import contact_send


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

