import json
import random

MIN_ID_NUMBER = 100000000000
MAX_ID_NUMBER = 999999999999


class Train(object):
    def __init__(self, json_object):
        self.id = json_object['trainID']
        self.number = json_object['trainNumber']
        self.name = json_object['trainName']
        self.type = json_object['trainType']
        self.station_from_id = json_object['trainStationFromID']
        self.station_to_id = json_object['trainStationToID']
        self.station_via_ids = json_object.get('trainStationViaIDs', None)

    def __str__(self):
        return f"{self.name} {self.type} with {self.number} from {self.station_from_id} to {self.station_to_id}" + (f" via {self.station_via_ids}." if self.station_via_ids else ".")


class TrainProxy(object):
    def __init__(self, json_object):
        self.id = json_object['trainID']
        self.arrival_time = json_object.get('trainArrivalTime', None)
        self.departure_time = json_object.get('trainDepartureTime', None)
        self.platform_number = json_object['trainPlatformNumber']


def load_trains(file='trains.json'):
    trains = json.load(open(file))['trains']
    for train in trains:
        train = Train(train)
        print(train)


load_trains()
