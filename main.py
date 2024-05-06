import asyncio
import logging

from aiogram import types, filters
from aiogram.fsm.context import FSMContext

import AudioEffects
import BotStates as States
import markups as nav
from handlers import InGameHandlers, MenuHandlers
import Data


@Data.dp.message(filters.CommandStart())
async def botStartMessage(message: types.Message, state: FSMContext) -> None:
    """Handler for /start command"""
    await state.set_state(States.Menu.MAIN)
    await message.answer("Hello, it's MusicQuiz bot", reply_markup=nav.mainMenu)
    AudioEffects.clearAudio()


async def start():
    logging.basicConfig(level=logging.INFO)
    Data.dp.message.register(MenuHandlers.mainMenuHandler)
    Data.dp.message.register(InGameHandlers.answerHandler)
    Data.dp.message.register(botStartMessage)
    Data.dp.message.register(InGameHandlers.correctAnswerHandler)
    Data.dp.message.register(MenuHandlers.genreMenuHandler)
    Data.dp.message.register(MenuHandlers.difficultMenuHandler)
    Data.dp.message.register(MenuHandlers.modeMenuHandler)

    try:
        await Data.dp.start_polling(Data.bot)
    finally:
        await Data.bot.session.close()


if __name__ == '__main__':
    asyncio.run(start())
