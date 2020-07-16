class TrainError(Exception):
    pass


class TrainNumberError(TrainError):
    pass


class TrainNameError(TrainError):
    pass


class TrainTypeError(TrainError):
    pass


class TrainNotFoundError(TrainError):
    pass


class StationError(Exception):
    pass


class StationNameError(StationError):
    pass


class StationTypeError(StationError):
    pass


class StationNotFoundError(StationError):
    pass


class StationCodeError(StationError):
    pass
