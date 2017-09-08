import argparse

DEFAULT_LOWER_BOUND = 0.0
DEFAULT_UPPER_BOUND = 1.0


def _check_positive_int(value):
    val = int(value)
    if val <= 0:
        raise argparse.ArgumentTypeError(f"{value} is an invalid positive int value")
    return val


def parse_args(args):
    parser = argparse.ArgumentParser(description="Lehmer RNG (Laboratory works #1 and #2)")

    parser.add_argument("-R", "--seed", type=_check_positive_int,
                        help="seed (R0) of the generator",
                        dest="seed",
                        metavar="seed", required=True)
    parser.add_argument("-a", "--multiplier", type=_check_positive_int,
                        help="multiplier for the start value",
                        dest="mul",
                        metavar="mul", required=True)
    parser.add_argument("-m", "--module", type=_check_positive_int,
                        help="multiplication module",
                        dest="mod",
                        metavar="mod", required=True)

    parser.add_argument("-l", "--lower-bound", type=float,
                        help="lower bound for the interval of random",
                        dest="lower_bound",
                        metavar="bound", default=DEFAULT_LOWER_BOUND)
    parser.add_argument("-u", "--upper-bound", type=float,
                        help="upper bound for the interval of random",
                        dest="upper_bound",
                        metavar="bound", default=DEFAULT_UPPER_BOUND)

    parsed = parser.parse_args(args)

    if parsed.upper_bound < parsed.lower_bound:
        raise argparse.ArgumentError(argument="--upper-bound",
                                     message="value must greater than --lower-bound option")

    if parsed.mod < parsed.mul:
        raise argparse.ArgumentError(argument="--module",
                                     message="module must be greater than multiplier (-a option)")

    return parsed
