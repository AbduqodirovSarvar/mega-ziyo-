from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
contakt = ReplyKeyboardMarkup(
    keyboard=[
        [
        KeyboardButton(text="Share contact⬆️", request_contact=True)
            ],
    ],
resize_keyboard=True
)

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Kurslar"),
            KeyboardButton(text="Testlar")
            ],
        [
            KeyboardButton(text="Mega Ziyo haqida"),
            KeyboardButton(text="Filiallarimiz")
            ],
        [
            KeyboardButton(text="Wikipedia"),
            KeyboardButton(text="En-Uz tarjimon")
            ],
        [
            KeyboardButton(text="Biz bilan bog'lanish")
            ],
    ],
resize_keyboard=True
)

kurs = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Matematika"),
            KeyboardButton(text="Fizika"),
            KeyboardButton(text="Ona-tili")
            ],
        [
            KeyboardButton(text="Tarix"),
            KeyboardButton(text="Ingliz tili"),
            KeyboardButton(text="Rus-tili")
            ],
        [
            KeyboardButton(text="Biologiya"),
            KeyboardButton(text="Geografiya"),
            KeyboardButton(text="Majburiy fanlar")
            ],
        [
            KeyboardButton(text="Bosh sahifa")
        ],
    ],
resize_keyboard=True
)

harid = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Kursga yozilish"),
            KeyboardButton(text="Bosh sahifa")
            ],
        ],
resize_keyboard=True
)

Bosh = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Bosh sahifa")
            ],
        ],
resize_keyboard=True
)