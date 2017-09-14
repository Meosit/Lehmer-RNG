from argparse import ArgumentParser, ArgumentTypeError, ArgumentError


def _check_positive_int(value):
    val = int(value)
    if val <= 0:
        raise ArgumentTypeError(f"{value} is an invalid positive int value")
    return val


def _check_positive_float(value):
    val = float(value)
    if val <= 0:
        raise ArgumentTypeError(f"{value} is an invalid positive float value")
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

    uniform_parser = subparsers.add_parser("uniform", help="uniform distribution imitation")
    uniform_parser.add_argument("-l", "--lower-bound", type=float,
                                help="lower bound of uniform distribution",
                                dest="lower_bound", metavar="<bound>",
                                default=0.0)
    uniform_parser.add_argument("-u", "--upper-bound", type=float,
                                help="upper bound of uniform distribution",
                                dest="upper_bound", metavar="<bound>",
                                default=1.0)

    gaussian_parser = subparsers.add_parser("gaussian", help="gaussian distribution imitation")
    gaussian_parser.add_argument("-M", "--mean", type=float,
                                 help="mean of gaussian distribution",
                                 dest="mean", metavar="<value>",
                                 required=True)
    gaussian_parser.add_argument("-D", "--deviation", type=float,
                                 help="standard deviation of gaussian distribution",
                                 dest="deviation", metavar="<value>",
                                 required=True)
    gaussian_parser.add_argument("-N", "--base-numbers", type=_check_positive_int,
                                 help="number of p.p randoms as base for every number of gaussian distribution",
                                 dest="base_numbers", metavar="<value>",
                                 default=12)

    exponential_parser = subparsers.add_parser("exponential", help="exponential distribution imitation")
    exponential_parser.add_argument("-L", "--lambda", type=_check_positive_float,
                                    help="rate parameter of exponential distribution",
                                    dest="lambda", metavar="<value>",
                                    required=True)

    gamma_parser = subparsers.add_parser("gamma", help="gamma distribution imitation")
    gamma_parser.add_argument("-L", "--lambda", type=_check_positive_float,
                              help="parameter of gaussian distribution",
                              dest="lambda", metavar="<value>",
                              required=True)
    gamma_parser.add_argument("-e", "--eta", type=_check_positive_int,
                              help="Erlang distribution parameter",
                              dest="eta", metavar="<value>",
                              required=True)

    triangle_parser = subparsers.add_parser("triangle", help="triangle distribution imitation")
    triangle_parser.add_argument("-l", "--lower-bound", type=float,
                                 help="lower bound of triangle distribution",
                                 dest="lower_bound", metavar="<bound>",
                                 default=0.0)
    triangle_parser.add_argument("-u", "--upper-bound", type=float,
                                 help="upper bound of triangle distribution",
                                 dest="upper_bound", metavar="<bound>",
                                 default=1.0)
    triangle_parser.add_argument("-t", "--type",
                                 help="formula type of triangle distribution",
                                 dest="type", metavar="<type>",
                                 choices=['min', 'max'], default='min')

    simpson_parser = subparsers.add_parser("simpson", help="simpsons distribution imitation")
    simpson_parser.add_argument("-l", "--lower-bound", type=float,
                                help="lower bound of simpson distribution",
                                dest="lower_bound", metavar="<bound>",
                                default=0.0)
    simpson_parser.add_argument("-u", "--upper-bound", type=float,
                                help="upper bound of simpson distribution",
                                dest="upper_bound", metavar="<bound>",
                                default=1.0)

    parsed = parser.parse_args()

    if parsed.mod < parsed.mul:
        raise ArgumentError(argument="-m, --module",
                            message="module must be greater than multiplier (-a, --multiplier option)")

    if hasattr(parsed, 'upper_bound') and \
            hasattr(parsed, 'lower_bound') and \
                    parsed.upper_bound < parsed.lower_bound:
        raise ArgumentError(argument="-u, --upper-bound",
                            message="upper bound must be greater than lower bound")

    return parsed
