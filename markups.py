from aiogram.types import KeyboardButton, InlineKeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup
import Data


def getAnsMarkup(options: list[str]) -> InlineKeyboardMarkup:
    """Create inline keyboard markup with 2 rows and columns and return it."""
    return InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text=x, callback_data=x) for x in options[0:2]],
                                                 [InlineKeyboardButton(text=x, callback_data=x) for x in options[2:]]],
                                resize_keyboard=True)


def getAfterAnsMarkup() -> InlineKeyboardMarkup:
    """Create inline keyboard markup with 1 row and 3 buttons,
     make url link to the song in the last button and return it."""
    try:
        link = InlineKeyboardButton(text='check song on spotify',
                                    url=Data.links[Data.correctAnswer])
    except:
        link = InlineKeyboardButton(text='cannot find the song :(', callback_data=' ')
    return InlineKeyboardMarkup(inline_keyboard=[[nextSong, quitGame, link]], resize_keyboard=True)


nextSong = InlineKeyboardButton(text='next song', callback_data='next')
quitGame = InlineKeyboardButton(text='quit', callback_data='q')

toMain = KeyboardButton(text='back')

play = KeyboardButton(text='Play')
mode = KeyboardButton(text='Mode')
genres = KeyboardButton(text='Genre')
difficult = KeyboardButton(text='Difficult')

mode1 = KeyboardButton(text='Reverb')
mode2 = KeyboardButton(text='Slowed')
mode3 = KeyboardButton(text='Speedup')

genre1 = KeyboardButton(text='Pop')
genre2 = KeyboardButton(text='Classic')
genre3 = KeyboardButton(text='Rock')

diff1 = KeyboardButton(text='1 sec')
diff2 = KeyboardButton(text='5 sec')
diff3 = KeyboardButton(text='10 sec')

reset = KeyboardButton(text='reset')

mainMenu = ReplyKeyboardMarkup(keyboard=[[play, mode], [genres, difficult]], resize_keyboard=True)

modeMenu = ReplyKeyboardMarkup(keyboard=[[mode1, mode2, mode3], [reset, toMain]], resize_keyboard=True)
genresMenu = ReplyKeyboardMarkup(keyboard=[[genre1, genre2, genre3], [reset, toMain]], resize_keyboard=True)
difficultMenu = ReplyKeyboardMarkup(keyboard=[[diff1, diff2, diff3], [reset, toMain]], resize_keyboard=True)
