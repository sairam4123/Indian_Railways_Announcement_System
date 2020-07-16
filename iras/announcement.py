import io
import os
from pathlib import Path

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from googletrans import Translator
from gtts import gTTS

import iras


# To play audio text-to-speech during execution
def announce(train: iras.Train, languages=None):
    from_station = iras.get_station_with_id(train.station_from_id)
    to_station = iras.get_station_with_id(train.station_to_id)
    via_stations = iras.convert_list_of_any_to_specific_thing(train.station_via_ids, iras.get_station_with_id)
    via_stations_names = " ; ".join([station.name for station in via_stations])
    train.correct_number = " ; ".join(list(train.number)) + " ;"
    msg = (f'Your kind attention of Passengers! Train Number {train.correct_number} {train.name} {train.type} '
           f'bound for {to_station.name} from {from_station.name}' + (f" via {via_stations_names}" if via_stations else "")
           + f" is scheduled to depart from platform number {4} at {3}:{45} {'PM'}")

    if languages is None:
        languages = ['en', 'ta', 'hi']
    sound_files = [path for path in (Path('main') / 'sounds').iterdir()]
    pygame.mixer.init()
    sound_file = sound_files[0].open('rb')
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue
    for lang in languages:
        with io.BytesIO() as f:
            translated = Translator().translate(msg, dest=lang).text
            gTTS(text=translated, lang=lang).write_to_fp(f)
            f.seek(0)
            pygame.mixer.init()
            pygame.mixer.music.load(f)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                continue
