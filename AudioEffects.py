import os
import shutil

from pedalboard import Reverb
from pedalboard_native.io import AudioFile
import Data


def clearAudio() -> None:
    """Clear currentRound dir after round has been completed."""
    shutil.rmtree('packs\\currentRound')
    os.mkdir('packs\\currentRound')


def applyEffects(path: str, name: str) -> None:
    """path - path to the source audio file.
       name - name of the new file in the currentRound dir with edited track."""
    with AudioFile(path) as f:
        speed = 1
        if 'Speedup' in Data.currentMode:
            speed += 0.3
        if 'Slowed' in Data.currentMode:
            speed -= 0.3
        audio = f.read(f.frames)[:, :f.samplerate * (int(speed * Data.currentDiff) + 1)]

        if 'Reverb' in Data.currentMode:
            reverb = Reverb()
            audio = reverb(audio, f.samplerate)

        with AudioFile(f'packs\\currentRound\\{name}.wav', 'w', int(f.samplerate * speed) + 1, num_channels=2) as o:
            o.write(audio)
