import os
import random

from aiogram.types import InlineKeyboardButton

import Data


def prepareAnswerOptions() -> list[str]:
    """Select first song from Data.currentPack and fill Data.correctAnswer with its name.
       Select three random answer options from Data.currentOptions in the list and randomly insert Data.correctAnswer into.
       Return list of Data.CorrectAnswer and three options from Data.currentOptions."""
    options = random.sample(Data.currentOptions, 3)
    Data.correctAnswer, _ = Data.currentPack[0]
    options.insert(random.randint(0, 3), Data.correctAnswer)
    return options


def createOptionButtons(options: list[str]) -> list[InlineKeyboardButton]:
    """Create for each option from options inline button.
       Return list of inline buttons."""
    optionButtons = []
    for option in options:
        optionButtons.append(InlineKeyboardButton(text=option, callback_data=option))
    return optionButtons


def createCurrentRound() -> None:
    """Select 10 random songs for each genre from in Data.currentGenres, fill them in Data.currentPack and shuffle."""
    songs = []
    for genre in Data.currentGenres:
        songs.append([x[:-4] for x in os.listdir(f"C:\\Users\\misha\\PycharmProjects\\MusicQuiz\\packs\\{genre}") if
                      ".mp3" in x])
    while len(Data.currentPack) < 10:
        for id, song in enumerate(songs):
            temp = [random.choice(song), Data.currentGenres[id]]
            Data.currentPack.append(temp)
            song.remove(temp[0])
            if len(Data.currentPack) >= 10:
                break
    random.shuffle(Data.currentPack)
