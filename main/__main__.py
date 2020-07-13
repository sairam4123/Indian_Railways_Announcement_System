def main_file():
    import main.announcement
    import main.utils.get_functions
    import main.stations
    import main.trains

    main.trains.Train.load_trains()
    main.stations.Station.load_stations()
    train = main.trains.Train.create_train()
    main.trains.Train.write_trains_to_json()
    print('\n\n')
    station = main.stations.Station.create_station()
    main.stations.Station.write_stations_to_json()

    main.announcement.announce(main.utils.get_functions.get_train_with_id(899803236143))
