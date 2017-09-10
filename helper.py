def press_enter():
    print("Press enter...")
    input()


def log_info(msg):
    print(f"INFO: {msg}")


def min_max(iterable):
    _min = iterable[0]
    _max = iterable[0]
    for value in iterable:
        if value < _min:
            _min = value
        elif value > _max:
            _max = value
    return _min, _max
