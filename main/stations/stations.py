import random

from ..constants import *
from ..trains.trains import TrainProxy


class Station(object):
    def __init__(self, json_object):
        self.id = json_object['stationID']
        self.name = json_object['stationName']
        self.type = json_object['stationType']
        self.arrivals = json_object['stationArrivals']['trains']
        self.departures = json_object['stationDepartures']['trains']
        self.converted_train_arrivals = []
        self.converted_train_departures = []
        self.convert_arrivals_and_departures_to_train()

    def convert_arrivals_and_departures_to_train(self):
        for train_proxy in self.arrivals:
            self.converted_train_arrivals.append(TrainProxy(train_proxy).convert_to_train())
        for train_proxy in self.departures:
            self.converted_train_departures.append(TrainProxy(train_proxy).convert_to_train())

    @classmethod
    def create_station(cls):
        print("This is the Interactive Train Builder!")
        train_number = input("What is the train number?: >>> ")
        # if len(train_number) > 5:
        #     raise TrainNumberError("all train number of trains in India doesn't exceed above 5")
        train_name = input("Don't say the Express or Local or SuperFast Express here.\nWhat is the train name?: >>> ")
        # if check_a_list_in_another_list(['exp', 'express', 'sf', 'sf express', 'local', 'l'], train_name):
        #     raise TrainNameError
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
