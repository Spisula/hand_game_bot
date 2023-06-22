from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Text
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery

BOT_TOKEN: str = '5886220274:AAH6QAYckGGLKQAx22bQ4Jb2tUYLMS_a2sU'

bot: Bot = Bot(token=BOT_TOKEN)
dp: Dispatcher = Dispatcher()

url_button_1: InlineKeyboardButton = InlineKeyboardButton(
    text='CALLBACK BUTTON 1',
    callback_data='button_1_pressed')
url_button_2: InlineKeyboardButton = InlineKeyboardButton(
    text='CALLBACK BUTTON 2',
    callback_data='button_2_pressed')

keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[[url_button_1], [url_button_2]])

@dp.message(CommandStart())
async def test_start(msg: Message):
    await msg.answer('Так выглядят callback кнопки', reply_markup=keyboard)

@dp.callback_query(Text(text=['button_1_pressed']))
async def callbc_1(cb:CallbackQuery):
    await cb.answer(text='Была нажата кнопка 1', show_alert=False, reply_markup=cb.message.reply_markup)

@dp.callback_query(Text(text=['button_2_pressed']))
async def callbc_2(cb: CallbackQuery):
    await cb.message.edit_text(text='Была нажата кнопка 2', reply_markup=cb.message.reply_markup)
    await cb.answer(text='pressed button 2')


if __name__ == '__main__':
    dp.run_polling(bot)
