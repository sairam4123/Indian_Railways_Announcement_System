__version__ = "0.0.8"


def get_input_from_user():
    while True:
        try:
            yield input(">>> ")
        except (KeyboardInterrupt, EOFError):
            exit(1)


def execute_user_input(user_input):
    import main.trains
    import main.stations
    if user_input in ['train', 'train builder']:
        print()
        main.trains.Train.load_trains()
        main.trains.Train.create_train()
        main.trains.Train.write_trains_to_json()
    elif user_input in ['station', 'station builder']:
        print()
        main.stations.Station.load_stations()
        main.stations.Station.create_station()
        main.stations.Station.write_stations_to_json()
    elif user_input in ['exit', 'e', 'exit()']:
        prompt = input("Do you want to exit?: >>> ")
        if prompt in ['y', 'yes', 'yes()']:
            print("Exiting!")
            exit(0)
        else:
            pass


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
