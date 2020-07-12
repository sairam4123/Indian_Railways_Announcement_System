import json
import random
from pathlib import Path
from typing import Type

from ..constants import *
from ..errors import StationNameError
from ..trains.trains import TrainProxy
from ..utils.list_manipulation import check_a_list_eq_eq_another_string, check_a_list_in_another_string


class Station(object):
    stations = []

    def __new__(cls: Type['Station'], *args, **kwargs):
        self = super().__new__(cls)
        cls.stations.append(self)
        return self

    def __init__(self, json_object):
        self.id = json_object['stationID']
        self.name = json_object['stationName']
        self.type = json_object['stationType']
        self.platform_count = json_object['stationPlatformCount']
        self.arrivals = json_object['stationArrivals']['trains'] or []
        self.departures = json_object['stationDepartures']['trains'] or []
        self.converted_train_arrivals = []
        self.converted_train_departures = []
        self.convert_arrivals_and_departures_to_train()

    def convert_arrivals_and_departures_to_train(self):
        for train_proxy in self.arrivals:
            if train_proxy and train_proxy[0]:
                print(train_proxy)
                self.converted_train_arrivals.append(TrainProxy(train_proxy).convert_to_train())
        for train_proxy in self.departures:
            if train_proxy and train_proxy[0]:
                self.converted_train_departures.append(TrainProxy(train_proxy).convert_to_train())

    @staticmethod
    def load_stations(file=Path('main') / 'data' / 'stations.json'):
        stations = json.load(open(file))['stations']
        stations_object = []
        for station in stations:
            stations_object.append(Station(station))
        return stations_object

    @classmethod
    def create_station(cls):
        print("This is the Interactive Station Builder!")
        if check_a_list_eq_eq_another_string(['yes', 'y', 'yes()'], input("Do you want to exit?: >>> ")):
            return
        station_name = input("Don't say the Junction here.\nWhat is the station name?: >>> ")
        if check_a_list_in_another_string(['jn', 'jnc', 'eg', 'jnction', 'junction', 'j'], station_name):
            raise StationNameError()
        station_type = input("Put the type here.\nWhat is the station type?: >>> ")
        station_platform_count = input("What is the number of platforms your station has?: >>> ")
        json_obj = {
            'stationID': random.randint(MIN_ID_NUMBER, MAX_ID_NUMBER),
            'stationName': station_name,
            'stationType': station_type,
            'stationArrivals': {'trains': []},
            'stationDepartures': {'trains': []},
            'stationPlatformCount': station_platform_count
        }
        print(json_obj)
        ins = cls.__new__(cls)
        ins.__init__(json_obj)
        return ins

    @staticmethod
    def convert_self_to_dict(station):
        dict_obj = {
            'stationID': station.id,
            'stationName': station.name,
            'stationType': station.type,
            'stationArrivals': {'trains': station.arrivals},
            'stationDepartures': {'trains': station.departures},
            'stationPlatformCount': station.platform_count
        }
        return dict_obj

    @staticmethod
    def write_stations_to_json():
        train_json = {
            'stations': []
        }
        for train in Station.stations:
            train_json['stations'].append(Station.convert_self_to_dict(train))

        json.dump(train_json, open(Path('main') / 'data' / 'stations.json', mode='w'), indent=4)
