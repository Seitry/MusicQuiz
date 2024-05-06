from aiogram import types, filters
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile

import BotStates as States
import markups as nav
import RoundRoutine
import Data
import AudioEffects


@Data.dp.callback_query(
    filters.StateFilter(States.Menu.MAIN, States.Menu.GENRES, States.Menu.DIFFICULT, States.Menu.MODE))
async def plug2(call: types.CallbackQuery, state: FSMContext) -> None:
    """Ignore inline button clicks in menu states."""
    await Data.bot.answer_callback_query(callback_query_id=call.id)


@Data.dp.callback_query(filters.StateFilter(States.InGame.QUESTION))
async def answerHandler(call: types.CallbackQuery, state: FSMContext) -> None:
    """Handle inline buttons in game states."""
    if (call.message.message_id != Data.currentMessage):
        await Data.bot.answer_callback_query(callback_query_id=call.id)
        return

    if (call.data in Data.tries):
        await Data.bot.answer_callback_query(callback_query_id=call.id)
        return

    if (call.data == Data.correctAnswer):
        Data.points += 1
        await state.set_state(States.InGame.CORRECT_ANSWER_AND_LINK)
        temp = await call.message.answer(('Correct! This is ' + Data.correctAnswer + '.'),
                                         reply_markup=nav.getAfterAnsMarkup())
        Data.currentMessage = temp.message_id
        await Data.bot.answer_callback_query(callback_query_id=call.id)
        return
    else:
        Data.tries.append(call.data)
        await call.message.answer(call.data + ' is incorrect, try again!')
        await Data.bot.answer_callback_query(callback_query_id=call.id)

    if len(Data.tries) == 3:
        await state.set_state(States.InGame.CORRECT_ANSWER_AND_LINK)
        temp = await call.message.answer(('The song is ' + Data.correctAnswer + '!'),
                                         reply_markup=nav.getAfterAnsMarkup())
        Data.currentMessage = temp.message_id
        await Data.bot.answer_callback_query(callback_query_id=call.id)
        return


@Data.dp.callback_query(filters.StateFilter(States.InGame.CORRECT_ANSWER_AND_LINK))
async def correctAnswerHandler(call: types.CallbackQuery, state: FSMContext) -> None:
    """Handle inline buttons in after question state
    next - send new question if current pack doesn't end
    quit - show results and return to main menu
    link - go to the song on spotify."""
    Data.tries.clear()
    if (call.message.message_id != Data.currentMessage):
        await Data.bot.answer_callback_query(callback_query_id=call.id)
        return

    if (not Data.currentPack):
        await showResults(call, state)
        await Data.bot.answer_callback_query(callback_query_id=call.id)
        return

    match call.data:
        case 'q':
            await showResults(call, state)
            await Data.bot.answer_callback_query(callback_query_id=call.id)

        case 'next':
            await state.set_state(States.InGame.QUESTION)
            AudioEffects.applyEffects(f"packs\\{Data.currentPack[0][1]}\\{Data.currentPack[0][0]}.mp3",
                                      Data.currentPack[0][0])
            temp = await call.message.answer_audio(FSInputFile(f"packs\\currentRound\\{Data.currentPack[0][0]}.wav"),
                                                   title=' ', reply_markup=nav.getAnsMarkup(
                    RoundRoutine.prepareAnswerOptions()))
            Data.currentMessage = temp.message_id
            Data.currentPack.pop(0)
            Data.currentMessage = temp.message_id
            Data.total += 1
            await Data.bot.answer_callback_query(callback_query_id=call.id)
        case _:
            await Data.bot.answer_callback_query(callback_query_id=call.id)


@Data.dp.message(filters.StateFilter(States.InGame.QUESTION, States.InGame.CORRECT_ANSWER_AND_LINK))
async def plug(message: types.Message, state: FSMContext) -> None:
    """Ignore messages in game states."""
    pass


async def showResults(call: types.CallbackQuery, state: FSMContext) -> None:
    """Shows results of the played pack and clear metadata for the next round."""
    await state.set_state(States.Menu.MAIN)
    temp = await call.message.answer(
        'You guessed ' + str(Data.points) + ' out of ' + str(Data.total) + ' songs!',
        reply_markup=nav.mainMenu)
    Data.currentMessage = temp.message_id
    Data.points = 0
    Data.total = 1
    Data.currentPack.clear()
    AudioEffects.clearAudio()
