from argparse import ArgumentParser, ArgumentTypeError, ArgumentError


def _check_positive_int(value):
    val = int(value)
    if val <= 0:
        raise ArgumentTypeError(f"{value} is an invalid positive int value")
    return val


def parse_args():
    parser = ArgumentParser(description="Lehmer RNG (Laboratory works #1 and #2)")

    parser.add_argument("-R", "--seed", type=_check_positive_int,
                        help="seed (R0) of the generator",
                        dest="seed",
                        metavar="<seed>", required=True)
    parser.add_argument("-a", "--multiplier", type=_check_positive_int,
                        help="multiplier for the start value",
                        dest="mul",
                        metavar="<mul>", required=True)
    parser.add_argument("-m", "--module", type=_check_positive_int,
                        help="multiplication module",
                        dest="mod",
                        metavar="<mod>", required=True)

    parser.add_argument("-n", "--numbers", type=_check_positive_int,
                        help="generate such number of random values",
                        dest="numbers_count",
                        metavar="<count>", default=1_000_000)
    parser.add_argument("-i", "--intervals", type=_check_positive_int,
                        help="check interval distribution for such number of intervals",
                        dest="intervals_count",
                        metavar="<count>", default=20)

    parsed = parser.parse_args()

    if parsed.mod < parsed.mul:
        raise ArgumentError(argument="-m, --module",
                            message="module must be greater than multiplier (-a, --multiplier option)")

    return parsed
