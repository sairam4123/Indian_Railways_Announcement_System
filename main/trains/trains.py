import json
import random
from pathlib import Path
from typing import List, Optional, Type

from main.errors import TrainNameError, TrainNumberError
from ..constants import *
from ..utils.list_manipulation import check_a_list_eq_eq_another_string, check_a_list_in_another_string


class Train(object):
    trains = []

    def __new__(cls: Type['Train'], *args, **kwargs):
        self = super().__new__(cls)
        cls.trains.append(self)
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
    def load_trains(file=Path('main') / 'data' / 'trains.json') -> List['Train']:
        trains = json.load(open(file))['trains']
        trains_object = []
        for train in trains:
            trains_object.append(Train(train))
        return trains_object

    @classmethod
    def create_train(cls):
        print("This is the Interactive Train Builder!")
        if check_a_list_eq_eq_another_string(['yes()', 'y', 'yes'], input("Do you want to exit?: >>> ")):
            return
        train_number = input("What is the train number?: >>> ")
        if len(train_number) > 5:
            raise TrainNumberError("all train number of trains in India doesn't exceed above 5")
        train_name = input("Don't say the Express or Local or SuperFast Express here.\nWhat is the train name?: >>> ")
        if check_a_list_in_another_string(['exp', 'express', 'sf', 'sf express', 'local', 'l'], train_name):
            raise TrainNameError
        train_type = input("Put the type here.\nWhat is the train type?: >>> ")
        train_station_from_id = input("What is the ID of the station your train origin?: >>> ")
        train_station_to_id = input("What is the ID of the station your train terminate?: >>> ")
        train_station_via_ids = input("Split the via stations using space.\nWhat is the IDs of the station your train pass via?: >>> ").split(' ') or ['None']
        json_obj = {
            'trainID': random.randint(MIN_ID_NUMBER, MAX_ID_NUMBER),
            'trainNumber': train_number,
            'trainName': train_name,
            'trainType': train_type,
            'trainStationFromID': train_station_from_id,
            'trainStationToID': train_station_to_id,
            'trainStationViaIDs': train_station_via_ids,
        }
        ins = cls.__new__(cls)
        ins.__init__(json_obj)
        return ins

    def __del__(self):
        self.trains.remove(self)

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
        for train in Train.trains:
            train_json['trains'].append(Train.convert_self_to_dict(train))

        json.dump(train_json, open(Path('main') / 'data' / 'trains.json', mode='w'), indent=4)

    def __str__(self):
        return f"{self.name} {self.type} with {self.number} " \
               f"from {self.station_from_id} to {self.station_to_id}" + \
               (f" via {self.station_via_ids}." if (self.station_via_ids != ['']) else ".")


class TrainProxy(object):
    def __init__(self, json_object):
        self.id = json_object['trainID']
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
    Train.load_trains()
    train_1 = Train.create_train()
    print(train_1)
