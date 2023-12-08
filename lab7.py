import logging


class HorseAgeOutOfRangeException(Exception):
    def __init__(self, horse):
        super().__init__(f"Horse's age {horse.age} is outside the acceptable range (3-7 years)")


class HorseAlreadyInRaceException(Exception):
    def __init__(self, horse):
        super().__init__(f"Horse {horse.name} is already participant")


class HorseNotInRaceException(Exception):

    def __init__(self, horse):
        super().__init__(f"Horse {horse.name} isn't in participant")


def logged(exception, mode):
    def wrapper(func):

        def inner(*args, **kwargs):
            try:
                func(*args, **kwargs)

            except exception as e:
                if mode == "console":
                    logging.error(e)
                elif mode == "file":
                    logging.basicConfig(filename="log.txt", level=logging.DEBUG)
                    logging.error(e)

                else:
                    print(f"Exception: {e}")

            finally:
                if mode == "file":
                    logging.shutdown()

        return inner

    return wrapper
