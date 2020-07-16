import json
import random
from typing import List, Optional, Type

import iras


class Train(object):
    _trains = []

    def __new__(cls: Type['Train'], *args, **kwargs):
        self = super().__new__(cls)
        cls._trains.append(id(self))
        return self

    def __init__(self, json_object):
        self.id: int = json_object['trainID']
        self.number: str = json_object['trainNumber']
        self.name: str = json_object['trainName']
        self.type: str = json_object['trainType']
        self.station_from_id: int = json_object['trainStationFromID']
        self.station_to_id: int = json_object['trainStationToID']
        self.station_via_ids: List[int] = json_object.get('trainStationViaIDs', None)

    @staticmethod
    def load_trains(file=iras.ANNOUNCEMENT_TRAIN_DATA_PATH) -> List['Train']:
        if Train._trains:
            Train._trains.clear()
        trains = json.load(open(file))['trains']
        return [Train(train) for train in trains]

    @classmethod
    def create_train(cls):
        print("This is the Interactive Train Builder!")
        if iras.check_a_list_eq_eq_another_string(['yes()', 'y', 'yes'], input("Do you want to exit?: >>> ")):
            return
        train_number = input("What is the train number?: >>> ")
        if len(train_number) > 5:
            raise iras.TrainNumberError("all train number of trains in India doesn't exceed above 5")
        train_name = input("Don't say the Express or Local or SuperFast Express here.\nWhat is the train name?: >>> ")
        if iras.check_a_list_in_another_string(['exp', 'express', 'sf', 'sf express', 'local', 'l'], train_name):
            raise iras.TrainNameError
        train_type = input("Put the type here.\nWhat is the train type?: >>> ")
        train_station_from_name = input("What is the name of the station your train origin?: >>> ")
        train_station_to_name = input("What is the name of the station your train terminate?: >>> ")
        train_station_via_names = input("Split the via stations using space.\nWhat is the names of the station your train pass via?: >>> ").split(' ') or ['None']
        train_station_from_ = iras.get_station_from_name(train_station_from_name)
        train_station_to_ = iras.get_station_from_name(train_station_to_name)
        train_station_via_ = iras.convert_list_of_any_to_specific_thing(train_station_via_names, iras.get_station_from_name)
        json_obj = {
            'trainID': random.randint(iras.MIN_ID_NUMBER, iras.MAX_ID_NUMBER),
            'trainNumber': train_number,
            'trainName': train_name,
            'trainType': train_type,
            'trainStationFromID': train_station_from_.id,
            'trainStationToID': train_station_to_.id,
            'trainStationViaIDs': [station.id for station in train_station_via_]
        }
        ins = cls.__new__(cls)
        ins.__init__(json_obj)
        return ins

    def __del__(self):
        try:
            self._trains.remove(id(self))
        except (ValueError, TypeError):
            pass

    @staticmethod
    def convert_self_to_dict(train):
        dict_obj = {
            'trainID': train.id,
            'trainNumber': train.number,
            'trainName': train.name,
            'trainType': train.type,
            'trainStationFromID': train.station_from_id,
            'trainStationToID': train.station_to_id,
            'trainStationViaIDs': train.station_via_ids,
        }
        return dict_obj

    @staticmethod
    def write_trains_to_json():
        train_json = {
            'trains': []
        }
        for train in Train.load_trains():
            train_json['trains'].append(Train.convert_self_to_dict(train))

        json.dump(train_json, open(iras.ANNOUNCEMENT_TRAIN_DATA_PATH, mode='w'), indent=4)

    def __str__(self):
        via_stations = iras.convert_list_of_any_to_specific_thing(self.station_via_ids, iras.get_station_with_id)
        return f"{self.name} {self.type} with {self.number} " \
               f"from {iras.get_station_with_id(self.station_from_id).name} to {iras.get_station_with_id(self.station_to_id).name}" + \
               (f" via {', '.join([via_station.name for via_station in via_stations])}." if (self.station_via_ids != ['']) else ".")


class TrainProxy:
    def __init__(self, json_object):
        self.id = json_object['trainID']
        self.station_id = json_object['trainStationID']
        self.arrival_time = json_object.get('trainArrivalTime', None)
        self.departure_time = json_object.get('trainDepartureTime', None)
        self.platform_number = json_object['trainPlatformNumber']

    def convert_to_train(self) -> Optional[Train]:
        trains = Train.load_trains()
        for train in trains:
            if train.id == self.id:
                return train
        else:
            return None


if __name__ == '__main__':
    import os

    os.chdir("")
    from iras.utils.get_functions import get_train_with_id

    Train.load_trains()
    train_1 = get_train_with_id(899803236143)
