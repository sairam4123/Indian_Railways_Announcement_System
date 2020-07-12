import pyttsx3

from main.trains import Train
from main.utils.converters import convert_list_of_any_to_specific_thing
from main.utils.get_functions import get_station_with_id


class Announcer(pyttsx3.Engine):
    def __init__(self):
        super(Announcer, self).__init__()

    def announce(self, train: Train):
        from_station = get_station_with_id(train.station_from_id)
        to_station = get_station_with_id(train.station_to_id)
        via_stations = convert_list_of_any_to_specific_thing(train.station_via_ids, get_station_with_id)
        print(via_stations)
        via_stations_names = ";".join([station.name for station in via_stations])
        train.correct_number = ";".join(list(train.number)) + ";"
        self.setProperty('rate', 100)
        self.say(f'Your kind attention of Passengers! Train Number {train.correct_number} {train.name} {train.type} '
                 f'bound for {to_station.name} from {from_station.name}' + (f" via {via_stations_names}" if via_stations else "")
                 + f" is scheduled to depart from platform number {2} at {12}:{46} {'PM'}")

# engine = pyttsx3.init()
# engine.say("1;2;3;4;5")
# engine.runAndWait()

# Translator().translate(f'Your kind attention of Passengers! Train Number {train.correct_number} {train.name} {train.type} '
#                  f'bound for {to_station.name} from {from_station.name}' + (f" via {via_stations_names}" if via_stations else "")
#                  + f" is scheduled to depart from platform number {2} at {12}:{46} {'PM'}", dest="ta").text
