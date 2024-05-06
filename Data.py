import os

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv

load_dotenv()
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot=bot, storage=MemoryStorage())


currentPack = []

currentMessage = 0
correctAnswer = ''
currentMode = []
currentGenres = []
currentDiff = 10
points = 0
total = 1
tries = []
links = dict()

currentOptions = ['Yellowcard - For You, And Your Denial',
                'AFI - Miss Murder',
                'Radiohead - Creep',
                'Hoobastank - The Reason',
                'Green Day - Letterbomb',
                'OK Go - Here It Goes Again',
                'Adele - Rolling In The Deep',
                'Imagine Dragons - Smoke And Mirrors',
                'Eminem - Business',
                'Donna Summer - Hot Stuff',
                'Metallica - Master Of Puppets',
                'Christopher Cross - Sailing',
                'Michael Buble - Feeling Good',
                'Linkin Park - Faint',
                'Depeche Mode - Personal Jesus',
                'Ed Sheeran - Shape of You',
                'Avicii - Wake Me Up',
                'Jim Croce - Time in a Bottle',
                'Imagine Dragons - Zero',
                'The Score - Higher',
                'Queen - I Want To Break Free',
                'AC/DC - Thunderstruck',
                'Gorillaz - Fell Good Inc',
                'Twenty One Pilots - Ride',
                'DNCE - Cake By The Ocean',
                'Eminem - Slim Shady',
                'Nickelback - We Will Rock You',
                'Eurythmics - Sweet Dreams',
                'Africa - Waving Flag',
                'Mattafix - Big City Life',
                'Oasis - Wonderwall',
                'Sting- Shape Of My Heart']

links["ACDC - Back In Black"] = 'https://open.spotify.com/track/08mG3Y1vljYA6bvDt4Wqkj'
links["Eminem - 'Till I Coll AP S E (The Eminem Show - 2002)"] = 'https://open.spotify.com/track/4xkOaSrkexMciUUogZKVTS'
links["Eminem - Lose Your self"] = 'https://open.spotify.com/track/7MJQ9Nfxzh8LPZ9e9u68Fq'
links["AHA - Take On Me"] = 'https://open.spotify.com/track/2WfaOiMkCvy7F5fcp2zZ8L'
links["Imagine Dragons - believer"] = 'https://open.spotify.com/track/0pqnGHJpmpxLKifKRmU6WP'
links["Queen - We Are The Champions"] = 'https://open.spotify.com/track/1lCRw5FEZ1gPDNPzy1K4zW'
links["Rick Astley - Never Gonna Give You Up"] = 'https://open.spotify.com/track/4PTG3Z6ehGkBFwjybzWkR8'
links["Stromae & Kanye West - Alors On Danse"] = 'https://open.spotify.com/track/4I2ENHg65RuKifEHdD0kMu'
links["Xxxtentacion - Moonlight"] = 'https://open.spotify.com/track/0JP9xo3adEtGSdUEISiszL'
links["Бетховен - К Элизе"] = 'https://open.spotify.com/track/7l7jlugqY7z8d8kprBluE6'

links["ACDC - T.N.T."] = 'https://open.spotify.com/track/7LRMbd3LEoV5wZJvXT1Lwb'
links["Bon Jovi - Its My Life"] = 'https://open.spotify.com/track/0v1XpBHnsbkCn7iJ9Ucr1l'
links["Chuck Berry - Johnny B. Goode.mp3"] = 'https://open.spotify.com/track/2QfiRTz5Yc8DdShCxG1tB2'
links["Eagles - Hotel California (2013 Remaster)"] = 'https://open.spotify.com/track/40riOy7x9W7GXjyGp4pjAv'
links["Guns N' Roses - Sweet Child O' Mine"] = 'https://open.spotify.com/track/7snQQk1zcKl8gZ92AnueZW'
links["Joan Jett & the Blackhearts - I Love Rock 'N Roll"] = 'https://open.spotify.com/track/2Cdvbe2G4hZsnhNMKyGrie'
links["Kiss - Detroit Rock City"] = 'https://open.spotify.com/track/3IjrDeaVRFEi3GgHI5xyjX'
links["Led Zeppelin - Stairway to Heaven"] = 'https://open.spotify.com/track/5CQ30WqJwcep0pYcV4AMNc'
links["Lynyrd Skynyrd - Simple Man"] = 'https://open.spotify.com/track/1ju7EsSGvRybSNEsRvc7qY'
links["Metallica - Nothing Else Matters"] = 'https://open.spotify.com/track/0nLiqZ6A27jJri2VCalIUs'

links["Bruno Mars ft. Mark Ronson - Uptown Funk"] = 'https://open.spotify.com/track/32OlwWuMpZ6b0aN2RZOeMS'
links["Carly Rae Jepsen - Call Me Maybe"] = 'https://open.spotify.com/search/Call%20Me%20Maybe'
links["Charlie Puth feat. Selena Gomez - We Don't Talk Anymore"] = 'https://open.spotify.com/track/68EMU2RD1ECNeOeJ5qAXCV'
links["Ed Sheeran - Bad Habits"] = 'https://open.spotify.com/track/3rmo8F54jFF8OgYsqTxm5d'
links["Jason Derulo feat. 2 Chainz - Talk Dirty"] = 'https://open.spotify.com/track/4X4tgBEUiT6WqB2oTJ5ynH'
links["Lady Gaga - Poker Face"] = 'https://open.spotify.com/track/1QV6tiMFM6fSOKOGLMHYYg'
links["LMFAO feat. Lauren Bennett, GoonRock - Party Rock Anthem"] = 'https://open.spotify.com/track/1ve0SgTZkv3wdggJLqtBYU'
links["Maroon 5 - Sugar"] = 'https://open.spotify.com/track/2iuZJX9X9P0GKaE93xcPjk'
links["OneRepublic - Counting Stars"] = 'https://open.spotify.com/track/2tpWsVSb9UEmDRxAl1zhX1'
links["One Direction - Drag Me Down"] = 'https://open.spotify.com/track/2K87XMYnUMqLcX3zvtAF4G'

links["Abel Korzeniowski - Melting Waltz"] = 'https://open.spotify.com/track/12qUtPRTeHP5DOZB9bR5fr'
links["Antonio Vivaldi - The Winter"] = 'https://open.spotify.com/track/6OHOYEMQfPKWZY4Uxxybnh'
links["Bach - Tocata In D Minor"] = 'https://open.spotify.com/track/0BWJNm4TrO6H3qgiCmDBjM'
links["Florian Christl - Vivaldi Variation"] = 'https://open.spotify.com/track/3Dgmyz32dxvtxvUTPS0CUI'
links["Frederic Chopin - Nocturne No. 2"] = 'https://open.spotify.com/track/1VNvsvEsUpuUCbHpVop1vo'
links["Johann Sebastian Bach - Cello Suite No. 1"] = 'https://open.spotify.com/track/17i5jLpzndlQhbS4SrTd0B'
links["Johann Sebastian Bach - Overture No. 2"] = 'https://open.spotify.com/track/3kvBEbswxMAx6QKc10SCon'
links["Johann Sebastian Bach - The Well Tempered Clavier"] = 'https://open.spotify.com/track/4SFBV7SRNG2e2kyL1F6kjU'
links["Julius Katchen - Piano Sonata No. 11"] = 'https://open.spotify.com/artist/36NfRmhEeMBlaQXAG3CP9Q'
links["Ludwig van Beethoven - Bagatelle No. 25"] = 'https://open.spotify.com/track/3zLTPuucd3e6TxZnu2dlVS'
