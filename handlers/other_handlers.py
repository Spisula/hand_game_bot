from aiogram import Router
from aiogram.types import Message
from lexicon.lexicon import LEXICON_RU

router: Router = Router()

@router.message()
async def other_text(msg: Message):
    await msg.answer(text=LEXICON_RU['any_text'])