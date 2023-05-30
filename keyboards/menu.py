from aiogram import Bot
from aiogram.types import BotCommand
from lexicon.lexicon import COMMANDS_RU

# Функция для настройки кнопки Menu бота
async def set_main_menu(bot: Bot):
    main_menu_commands = [BotCommand(command=my_command, description=my_description) for my_command, my_description in COMMANDS_RU.items()]
    await bot.set_my_commands(main_menu_commands)