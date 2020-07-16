__version__ = "0.0.9.1"


# noinspection PyBroadException
def get_input_from_user():
    while True:
        try:
            yield input(">>> ")
        except (KeyboardInterrupt, EOFError):
            exit(1)
        except Exception:
            pass


def execute_user_input(user_input):
    import re
    import iras
    # noinspection PyBroadException
    try:
        train_name_regex = re.compile('get train name (\"[\w\s]+\")')
        station_name_regex = re.compile('get station name (\"[\w\s]+\")')
        if user_input in ['train', 'train builder']:
            print()
            iras.trains.Train.load_trains()
            iras.trains.Train.create_train()
            iras.trains.Train.write_trains_to_json()
        elif user_input in ['station', 'station builder']:
            print()
            iras.stations.Station.load_stations()
            iras.stations.Station.create_station()
            iras.stations.Station.write_stations_to_json()
        elif train_name_regex.fullmatch(user_input):
            train_name = train_name_regex.match(user_input).group(1).strip('"')
            try:
                print(iras.get_train_from_name("".join(train_name.split(" ")[:-1])))
            except iras.TrainNotFoundError:
                print(iras.get_train_from_name("".join(train_name.split(" "))))
        elif station_name_regex.fullmatch(user_input):
            station_name = station_name_regex.match(user_input).group(1).strip('"')
            print(iras.get_station_from_name(station_name))
        elif user_input in ['exit', 'e', 'exit()']:
            prompt = input("Do you want to exit?: >>> ")
            if prompt in ['y', 'yes', 'yes()']:
                print("Exiting!")
                exit(0)
            else:
                pass
    except Exception:
        import traceback
        traceback.print_exc(chain=False)


def main_file():
    # import main.announcement
    # import main.utils.get_functions
    # import main.stations
    # import main.trains
    #
    # main.trains.Train.load_trains()
    # main.stations.Station.load_stations()
    # train = main.trains.Train.create_train()
    # main.trains.Train.write_trains_to_json()
    # print('\n\n')
    # station = main.stations.Station.create_station()
    # main.stations.Station.write_stations_to_json()
    #
    # main.announcement.announce(main.utils.get_functions.get_train_with_id(899803236143))
    print(f"This is the announcement system's interactive interpreter.\n\n\nVersion: {__version__}")
    for user_input in get_input_from_user():
        execute_user_input(user_input)
