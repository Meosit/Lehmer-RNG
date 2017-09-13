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

    subparsers = parser.add_subparsers(title="modes",
                                       description="valid generator modes",
                                       dest="mode")
    subparsers.required = True
    subparsers.add_parser("raw", help="plain Lehmer generator without any changes")
    even_parser = subparsers.add_parser("even", help="even distribution imitation")
    even_parser.add_argument("-l", "--lower-bound", type=float,
                             help="lower bound of the random value",
                             dest="even_lower_bound", metavar="<bound>",
                             required=True, default=0.0)
    even_parser.add_argument("-u", "--upper-bound", type=float,
                             help="upper bound of the random value",
                             dest="even_upper_bound", metavar="<bound>",
                             required=True, default=1.0)

    gaussian_parser = subparsers.add_parser("gaussian", help="gaussian distribution imitation")

    exponential_parser = subparsers.add_parser("exponential", help="exponential distribution imitation")

    gamma_parser = subparsers.add_parser("gamma", help="gamma distribution imitation")

    triangle_parser = subparsers.add_parser("triangle", help="triangle distribution imitation")

    simpsons_parser = subparsers.add_parser("simpsons", help="simpsons distribution imitation")

    parsed = parser.parse_args()

    if parsed.mod < parsed.mul:
        raise ArgumentError(argument="-m, --module",
                            message="module must be greater than multiplier (-a, --multiplier option)")

    if parsed.even_upper_bound is not None and \
                    parsed.even_lower_bound is not None and \
                    parsed.even_upper_bound < parsed.even_lower_bound:
        raise ArgumentError(argument="-u, --upper-bound",
                            message="upper bound must be greater than lower bound")

    return parsed
