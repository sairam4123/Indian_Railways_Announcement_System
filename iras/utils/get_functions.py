from typing import Optional

import iras


def get_station_with_id(id_: int) -> Optional[iras.Station]:
    for station in iras.Station.load_stations():
        if int(id_) == station.id:
            return station
    raise iras.StationNotFoundError(f"station with the id {id_} could be found. "
                                    f"If you think you have forgot to create a station, "
                                    f"just do station builder in interpreter.")


def get_train_with_id(id_: int) -> Optional[iras.Train]:
    for train in iras.Train.load_trains():
        if int(id_) == train.id:
            return train
    raise iras.TrainNotFoundError(f"train with the id {id_} could be found. "
                                  f"If you think you have forgot to create a train, "
                                  f"just do train builder in interpreter.")


def get_train_from_name(name: str) -> Optional[iras.Train]:
    for train in iras.Train.load_trains():
        if name == train.name:
            return train
    raise iras.TrainNotFoundError(f"train with the name {name} could be found. "
                                  f"If you think you have forgot to create a train, "
                                  f"just do train builder in interpreter.")


def get_station_from_name(name: str) -> Optional[iras.Station]:
    for station in iras.Station.load_stations():
        if name == station.name:
            return station
    raise iras.StationNotFoundError(f"station with the name {name} could be found. "
                                    f"If you think you have forgot to create a station, "
                                    f"just do station builder in interpreter.")
