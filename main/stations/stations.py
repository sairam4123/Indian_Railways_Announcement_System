import json
import random
from pathlib import Path
from typing import Type

from ..constants import *
from ..errors import StationCodeError, StationNameError
from ..trains.trains import TrainProxy
from ..utils.list_manipulation import check_a_list_eq_eq_another_string, check_a_list_in_another_string


class Station(object):
    _stations = []

    def __new__(cls: Type['Station'], *args, **kwargs):
        self = super().__new__(cls)
        cls._stations.append(id(self))
        return self

    def __init__(self, json_object):
        self.id = json_object['stationID']
        self.name = json_object['stationName']
        self.type = json_object['stationType']
        self.platform_count = json_object['stationPlatformCount']
        self.code = json_object.get('stationCode', None)
        self.arrivals = json_object['stationArrivals']['trains'] or []
        self.departures = json_object['stationDepartures']['trains'] or []
        self.converted_train_arrivals = []
        self.converted_train_departures = []
        self.convert_arrivals_and_departures_to_train()

    def convert_arrivals_and_departures_to_train(self):
        for train_proxy in self.arrivals:
            if train_proxy:
                train_proxy['trainStationID'] = self.id
                self.converted_train_arrivals.append(TrainProxy(train_proxy).convert_to_train())
        for train_proxy in self.departures:
            if train_proxy:
                train_proxy['trainStationID'] = self.id
                self.converted_train_departures.append(TrainProxy(train_proxy).convert_to_train())

    @staticmethod
    def load_stations(file=Path('main') / 'data' / 'stations.json'):
        Station._stations.clear()
        stations = json.load(open(file))['stations']
        return [Station(station) for station in stations]

    @classmethod
    def create_station(cls):
        print("This is the Interactive Station Builder!")
        if check_a_list_eq_eq_another_string(['yes', 'y', 'yes()'], input("Do you want to exit?: >>> ")):
            return
        station_name = input("Don't say the Junction here.\nWhat is the station name?: >>> ")
        if check_a_list_in_another_string(['jn', 'jnc', 'jnction', 'junction', 'j'], station_name):
            raise StationNameError("station name must not contain junction")
        station_type = input("Put the type here.\nWhat is the station type?: >>> ")
        station_platform_count = input("What is the number of platforms your station has?: >>> ")
        station_code = input("What is the station code of the station you're inputting?: >>> ").upper()
        if len(station_code) > 5:
            raise StationCodeError("station code must not exceed 4")
        json_obj = {
            'stationID': random.randint(MIN_ID_NUMBER, MAX_ID_NUMBER),
            'stationName': station_name,
            'stationType': station_type,
            'stationCode': station_code,
            'stationArrivals': {'trains': []},
            'stationDepartures': {'trains': []},
            'stationPlatformCount': station_platform_count
        }
        ins = cls.__new__(cls)
        ins.__init__(json_obj)
        return ins

    def __del__(self):
        self._stations.remove(id(self))

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
    def get_station_from_name(name: str):
        for station in Station.load_stations():
            if name == station.name:
                return station
        return None

    @staticmethod
    def get_station_from_id(id_: int):
        for station in Station.load_stations():
            if int(id_) == station.id:
                return station
        return None

    @staticmethod
    def write_stations_to_json():
        train_json = {
            'stations': []
        }
        for train in Station.load_stations():
            train_json['stations'].append(Station.convert_self_to_dict(train))

        json.dump(train_json, open(Path('main') / 'data' / 'stations.json', mode='w'), indent=4)

    def __str__(self):
        return f"{self.name} {self.type} with station code {self.code} and number of platforms {self.platform_count} {len(self.arrivals)} arrivals and {len(self.departures)} departures."
