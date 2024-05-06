from aiogram import filters, types
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile

import AudioEffects
import BotStates as States
import RoundRoutine
import markups as nav
import Data


@Data.dp.message(filters.StateFilter(States.Menu.MAIN))
async def mainMenuHandler(message: types.Message, state: FSMContext) -> None:
    """Handle main menu buttons and messages in main menu state.
       Check for correct settings or set them to default before game has been started."""
    match message.text:
        case 'Play':
            if not Data.currentGenres:
                Data.currentGenres.append('default')
            elif len(Data.currentGenres) > 1 and 'default' in Data.currentGenres:
                Data.currentGenres.remove('default')
            if not Data.currentDiff: Data.currentDiff = 10
            await state.set_state(States.InGame.QUESTION)
            if not Data.currentPack: RoundRoutine.createCurrentRound()
            AudioEffects.applyEffects(f"packs\\{Data.currentPack[0][1]}\\{Data.currentPack[0][0]}.mp3",
                                      Data.currentPack[0][0])
            temp = await message.answer_audio(FSInputFile(f"packs\\currentRound\\{Data.currentPack[0][0]}.wav"),
                                              title=' ',
                                              reply_markup=nav.getAnsMarkup(RoundRoutine.prepareAnswerOptions()))
            Data.currentMessage = temp.message_id
            Data.currentPack.pop(0)

        case 'Mode':
            await state.set_state(States.Menu.MODE)
            temp = await message.answer('Choose game mode', reply_markup=nav.modeMenu)
        case 'Genre':
            await state.set_state(States.Menu.GENRES)
            temp = await message.answer('Choose genre', reply_markup=nav.genresMenu)
        case 'Difficult':
            await state.set_state(States.Menu.DIFFICULT)
            temp = await message.answer('Choose game difficult', reply_markup=nav.difficultMenu)
        case _:
            pass


async def genreRoutine(message: types.Message):
    genre = message.text
    if genre not in ('Rock', 'Pop', 'Classic'): return
    if genre in Data.currentGenres:
        await message.answer(f'{genre} has been already chosen')
        return
    Data.currentGenres.append(genre)
    await message.answer(f'{genre} successfully set')


async def modeRoutine(message: types.Message):
    mode = message.text
    if mode not in ('Speedup', 'Slowed', 'Reverb'): return
    if mode in Data.currentMode:
        await message.answer(f'{mode} has been already chosen')
        return
    Data.currentMode.append(mode)
    await message.answer(f'{mode} successfully set')


async def diffRoutine(message: types.Message):
    diff = message.text
    if diff not in ('1 sec', '5 sec', '10 sec'): return
    if int(diff.split(' ')[0]) == Data.currentDiff:
        await message.answer(f'{diff} has been already chosen')
        return
    Data.currentDiff = int(diff.split(' ')[0])
    await message.answer(f'{diff} successfully set')


@Data.dp.message(filters.StateFilter(States.Menu.GENRES))
async def genreMenuHandler(message: types.Message, state: FSMContext):
    match message.text:
        case 'reset':
            Data.currentGenres.clear()
            await message.answer('Genre settings reset', reply_markup=nav.genresMenu)
        case 'back':
            await state.set_state(States.Menu.MAIN)
            await message.answer('Main menu', reply_markup=nav.mainMenu)
        case _:
            await genreRoutine(message)


@Data.dp.message(filters.StateFilter(States.Menu.MODE))
async def modeMenuHandler(message: types.Message, state: FSMContext):
    match message.text:
        case 'reset':
            Data.currentMode.clear()
            await message.answer('Mode settings reset', reply_markup=nav.modeMenu)
        case 'back':
            await state.set_state(States.Menu.MAIN)
            await message.answer('Main menu', reply_markup=nav.mainMenu)
        case _:
            await modeRoutine(message)


@Data.dp.message(filters.StateFilter(States.Menu.DIFFICULT))
async def difficultMenuHandler(message: types.Message, state: FSMContext):
    match message.text:
        case 'reset':
            Data.currentDiff = 10
            await message.answer('Difficult settings reset', reply_markup=nav.difficultMenu)
        case 'back':
            await state.set_state(States.Menu.MAIN)
            await message.answer('Main menu', reply_markup=nav.mainMenu)
        case _:
            await diffRoutine(message)
