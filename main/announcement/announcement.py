import pyttsx3

from main.stations import Station
from main.trains import Train


class Announcer(pyttsx3.Engine):
    def __init__(self):
        super(Announcer, self).__init__()

    def announce(self, station: Station, train: Train):
        train.correct_number = ";".join(list(train.number))
        self.say(f'Your kind attention of Passengers! Train Number {train.correct_number} {train.name} {train.type} Bound for {station.name} from ')

# engine = pyttsx3.init()
# engine.say("1;2;3;4;5")
# engine.runAndWait()
