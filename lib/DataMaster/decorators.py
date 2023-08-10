from sys import exit


def getter(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            print("Warning! The selected ticker is either wrong or not on watchlist!")
            exit()

    return wrapper
