from aiogram.fsm.state import StatesGroup, State


class Menu(StatesGroup):
    MAIN = State()
    GENRES = State()
    MODE = State()
    DIFFICULT = State()


class InGame(StatesGroup):
    QUESTION = State()
    CORRECT_ANSWER_AND_LINK = State()
