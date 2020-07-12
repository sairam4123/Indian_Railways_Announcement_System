from typing import Optional

from ..stations import Station
from ..trains import Train


def get_station_with_id(id_: int) -> Optional[Station]:
    for station in Station.load_stations():
        if id_ == station.id:
            return station
    return None


def get_train_with_id(id_: int) -> Optional[Train]:
    for train in Train.load_trains():
        if id_ == train.id:
            return train
    return None


def get_train_from_name(name: str) -> Optional[Train]:
    for train in Train.load_trains():
        if name == train.name:
            return train
    return None


def get_station_from_name(name: str) -> Optional[Station]:
    for station in Station.load_stations():
        if name == station.name:
            return station
    return None
