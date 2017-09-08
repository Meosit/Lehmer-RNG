import argparse

DEFAULT_LOWER_BOUND = 0.0
DEFAULT_UPPER_BOUND = 1.0


def _check_positive_int(value):
    val = int(value)
    if val <= 0:
        raise argparse.ArgumentTypeError(f"{value} is an invalid positive int value")
    return val


def parse_args(args):
    parser = argparse.ArgumentParser(description="Lehmer RNG (Laboratory work #1,2)")

    parser.add_argument("-a", type=_check_positive_int,
                        help="upper bound for the interval of random",
                        dest="upper_bound",
                        metavar="value", required=True)
    parser.add_argument("-R", type=float,
                        help="upper bound for the interval of random",
                        dest="upper_bound",
                        metavar="value", required=True)
    parser.add_argument("-m", type=_check_positive_int,
                        help="upper bound for the interval of random",
                        dest="upper_bound",
                        metavar="value", required=True)


    parser.add_argument("-l", "--lower-bound", type=float,
                        help="lower bound for the interval of random",
                        dest="lower_bound",
                        metavar="value", default=DEFAULT_LOWER_BOUND)
    parser.add_argument("-u", "--upper-bound", type=float,
                        help="upper bound for the interval of random",
                        dest="upper_bound",
                        metavar="value", default=DEFAULT_UPPER_BOUND)

    parsed = parser.parse_args(args)

    if parsed.upper_bound < parsed.lower_bound:
        raise argparse.ArgumentError(argument="--upper-bound",
                                     message="Value must greater than --lower-bound option")

    return parsed
