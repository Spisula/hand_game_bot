from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from lexicon.lexicon import LEXICON_RU

# создаем кнопки с помощью билдера
button_yes: KeyboardButton = KeyboardButton(text=LEXICON_RU['yes_button'])
button_no: KeyboardButton = KeyboardButton(text=LEXICON_RU['no_button'])

# инициализируем билдер кнопок
yes_no_kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()

# добавляем кнопки в билдер
yes_no_kb_builder.row(button_yes, button_no, width=2)

# создаем клавиатуру на две кнопки
yes_no_kb = yes_no_kb_builder.as_markup(one_time_keyboard=True, resize_keyboard=True)

#создаем кнопки без помощи билдера
button_rock: KeyboardButton = KeyboardButton(text=LEXICON_RU['rock'])
button_scissors: KeyboardButton = KeyboardButton(text=LEXICON_RU['scissors'])
button_paper: KeyboardButton = KeyboardButton(text=LEXICON_RU['paper'])

game_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
    keyboard =[[button_rock],
               [button_scissors],
               [button_paper]], resize_keyboard=True)