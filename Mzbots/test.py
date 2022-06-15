from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher import FSMContext
from admins import Token, Admins
from Postgresql import add_user, full
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from keyboard import contakt, menu, kurs, harid
from States import asosiy
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from app import bot, dp

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