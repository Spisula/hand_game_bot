from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart, Text
from lexicon.lexicon import LEXICON_RU
from keyboards.keyboards import yes_no_kb, game_kb
from services.services import get_bot_choice, get_winner

router: Router = Router()

#def get_name(msg: Message):
 #   name = msg.from_user.username
  #  return name


@router.message(CommandStart())
async def command_start(msg: Message):
    await msg.answer(text=LEXICON_RU['/start'].format(msg.from_user.username),  # type: ignore
                     reply_markup=yes_no_kb)


@router.message(Command('help'))
async def command_help(msg: Message):
    await msg.answer(text=LEXICON_RU['/help'], reply_markup=yes_no_kb)


@router.message(F.text == LEXICON_RU['yes_button'])
async def answer_yes(msg: Message):
    await msg.answer(text=LEXICON_RU['yes'], reply_markup=game_kb)


@router.message(Text(text=LEXICON_RU['no_button']))
async def answer_no(msg: Message):
    await msg.answer(text=LEXICON_RU['no'])


@router.message(Text(text=[LEXICON_RU['rock'],
                     LEXICON_RU['scissors'],
                     LEXICON_RU['paper']]))
async def game(msg: Message):
    bot_choice = get_bot_choice()
    await msg.answer(text=f'{LEXICON_RU["bot_choice"]} '
                          f'- {LEXICON_RU[bot_choice]}')
    winner = get_winner(msg.text, bot_choice)  # type: ignore
    await msg.answer(text=LEXICON_RU[winner], reply_markup=yes_no_kb)

